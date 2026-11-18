#!/usr/bin/env python3
"""
Unit 9 — run the five extension criteria (criteria_extension.md) against the
real run path, three trials each, every trial from a fresh start.

    python run_failures.py --mode before --label before   # RUNNING.md's plain gunicorn command
    python run_failures.py --mode after  --label after    # ./serve.sh (gunicorn.conf.py)
    python run_failures.py --mode after  --only E2 --trials 1

Nothing is faked inside the service. Each failure is caused for real:
  E1  start the service and send traffic while the model is still loading
  E2  kill -9 the worker
  E3  point the service at a model that isn't there, with Hugging Face offline
  E4  make the audit log file read-only
  E5  mixed traffic, then compare the client's tally with the request log and /metrics

It also runs one extra measurement, X1: the same flood against
`gunicorn -w 3`, the usual "more workers" advice, to show what that does to the
rate limit and to memory.

Writes results/unit9/failures_<date>_<label>.md with the raw evidence.
"""

import argparse
import datetime as dt
import json
import os
import shutil
import signal
import socket
import stat
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

import config
from calibrate import CLEARLY_AI, CLEARLY_HUMAN, CLEARLY_HUMAN_2, FORMAL_HUMAN, PLAIN_HUMAN

ROOT = Path(__file__).parent
PORT = 5002                      # 5000 is macOS AirPlay on this machine
URL = f"http://127.0.0.1:{PORT}"
GUNICORN = str(Path(sys.executable).parent / "gunicorn")
VALID = [CLEARLY_HUMAN, CLEARLY_AI, FORMAL_HUMAN, PLAIN_HUMAN, CLEARLY_HUMAN_2]
OUT_DIR = config.RESULTS_DIR / "unit9"


def now_iso():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="milliseconds")


# ── Starting and stopping the real service ───────────────────────────────────

class Service:
    def __init__(self, mode, env_extra=None, workers=None, tag=""):
        self.mode, self.env_extra, self.workers, self.tag = mode, env_extra or {}, workers, tag
        self.proc = None
        self.output_path = Path(tempfile.mkstemp(prefix="gunicorn_", suffix=".log")[1])

    def command(self):
        if self.mode == "after":
            return [str(ROOT / "serve.sh")]
        cmd = [GUNICORN, "app:app", "--bind", f"127.0.0.1:{PORT}"]   # RUNNING.md, on loopback
        if self.workers:
            cmd += ["--workers", str(self.workers)]
        return cmd

    def start(self):
        env = {**os.environ, "PORT": str(PORT), "HOST": "127.0.0.1", **self.env_extra}
        self.out = open(self.output_path, "w")
        self.t_start = time.monotonic()
        self.proc = subprocess.Popen(self.command(), cwd=ROOT, env=env, stdout=self.out,
                                     stderr=subprocess.STDOUT, start_new_session=True)
        # Time until the port accepts a TCP connection (not an HTTP answer).
        while time.monotonic() - self.t_start < 30:
            if self.proc.poll() is not None:
                break
            try:
                socket.create_connection(("127.0.0.1", PORT), timeout=0.2).close()
                self.bind_s = round(time.monotonic() - self.t_start, 2)
                return self
            except OSError:
                time.sleep(0.05)
        self.bind_s = None
        return self

    def stop(self):
        if self.proc and self.proc.poll() is None:
            os.killpg(self.proc.pid, signal.SIGTERM)
            try:
                self.proc.wait(timeout=30)
            except subprocess.TimeoutExpired:
                os.killpg(self.proc.pid, signal.SIGKILL)
                self.proc.wait()
        self.out.close()
        # Make sure the port is free before the next trial starts.
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            try:
                socket.create_connection(("127.0.0.1", PORT), timeout=0.2).close()
                time.sleep(0.2)
            except OSError:
                break
        return self.output_path.read_text(errors="replace")

    def worker_pids(self):
        out = subprocess.run(["pgrep", "-P", str(self.proc.pid)], capture_output=True, text=True).stdout
        # serve.sh execs gunicorn, so the master is proc.pid either way.
        return [int(p) for p in out.split()]


def rss_mb(pid):
    out = subprocess.run(["ps", "-o", "rss=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
    return round(int(out) / 1024, 1) if out else None


def post(path, body, timeout=120):
    t = time.monotonic()
    try:
        r = requests.post(f"{URL}{path}", json=body, timeout=timeout)
        try:
            payload = r.json()
        except ValueError:
            payload = {"_not_json": r.text[:120]}
        return {"status": r.status_code, "seconds": round(time.monotonic() - t, 2), "body": payload}
    except requests.RequestException as exc:
        return {"status": None, "seconds": round(time.monotonic() - t, 2),
                "error": f"{type(exc).__name__}: {str(exc)[:120]}"}


def get(path, timeout=30):
    try:
        r = requests.get(f"{URL}{path}", timeout=timeout)
        return r.status_code, (r.json() if r.headers.get("content-type", "").startswith("application/json") else None)
    except requests.RequestException as exc:
        return None, {"error": type(exc).__name__}


def warm(timeout=120):
    """One valid submit, retried until a 200 — leaves the model loaded."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        r = post("/submit", {"text": VALID[0], "creator_id": f"warmup_{time.time_ns()}"})
        if r["status"] == 200:
            return True
        time.sleep(1)
    return False


def brief(r):
    return {k: v for k, v in r.items() if k != "body"} | (
        {"error": r["body"].get("error")} if isinstance(r.get("body"), dict) and r["body"].get("error") else {})


# ── The five criteria ────────────────────────────────────────────────────────

def e1(mode, tag):
    svc = Service(mode).start()
    t0 = time.monotonic()

    def fire(i):
        time.sleep(max(0, t0 + i - time.monotonic()))
        return post("/submit", {"text": VALID[i % len(VALID)], "creator_id": f"e1_{tag}_{i}"})

    with ThreadPoolExecutor(max_workers=30) as pool:
        results = list(pool.map(fire, range(30)))
    log = svc.stop()
    ok = sum(r["status"] == 200 for r in results)
    return {
        "passed": ok == 30,
        "summary": f"{ok}/30 → 200; 5xx {sum((r['status'] or 0) >= 500 for r in results)}; "
                   f"dropped {sum(r['status'] is None for r in results)}; "
                   f"port open after {svc.bind_s}s; slowest {max(r['seconds'] for r in results)}s",
        "port_open_s": svc.bind_s,
        "results": [brief(r) for r in results],
        "gunicorn_log_tail": log.splitlines()[-12:],
    }


def e2(mode, tag):
    svc = Service(mode).start()
    warmed = warm()
    status, m = get("/metrics")
    victim = (m or {}).get("worker_pid")
    os.kill(victim, signal.SIGKILL)
    t_kill = time.monotonic()
    seen, first_ok = [], None
    while time.monotonic() - t_kill < 90 and first_ok is None:
        r = post("/submit", {"text": VALID[1], "creator_id": f"e2_{tag}_{len(seen)}"}, timeout=90)
        r["at_s"] = round(time.monotonic() - t_kill, 2)
        seen.append(brief(r))
        if r["status"] == 200:
            first_ok = r["at_s"]
        else:
            time.sleep(1)
    _, m2 = get("/metrics")
    log = svc.stop()
    died = [l for l in log.splitlines() if str(victim) in l or "SIGKILL" in l or "Booting worker" in l]
    return {
        "passed": bool(warmed and first_ok is not None and first_ok <= 60 and any(str(victim) in l for l in died)),
        "summary": f"killed worker {victim}; first 200 after {first_ok}s; new worker "
                   f"{(m2 or {}).get('worker_pid')}; gunicorn log mentions the dead worker: "
                   f"{any(str(victim) in l for l in died)}",
        "recovery_s": first_ok,
        "requests_after_kill": seen,
        "gunicorn_log_lines": died,
    }


def e3(mode, tag):
    svc = Service(mode, env_extra={"AI201_DETECTOR_MODEL": "ai201-missing-model",
                                   "HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1"}).start()
    deadline = time.monotonic() + 60
    while time.monotonic() < deadline and get("/ping")[0] is None and svc.proc.poll() is None:
        time.sleep(0.5)
    ids = [f"e3_{tag}_{i}" for i in range(5)]
    results = [post("/submit", {"text": VALID[i], "creator_id": cid}) for i, cid in enumerate(ids)]
    ping = post("/ping", {"message": "still there?"})["status"]
    h_status, health = get("/health")
    log = svc.stop()
    logged = [e for e in _audit_entries() if e.get("creator_id") in ids and e.get("status") == "rejected"
              and e.get("reason") == "detector_unavailable"]
    ok503 = sum(r["status"] == 503 and r["body"].get("error") == "detector_unavailable" for r in results)
    return {
        "passed": ok503 == 5 and ping == 200 and h_status == 200
                  and (health or {}).get("detector_loaded") is False and len(logged) == 5,
        "summary": f"{ok503}/5 → 503 detector_unavailable; /ping {ping}; /health {h_status} "
                   f"detector_loaded={(health or {}).get('detector_loaded')}; {len(logged)}/5 rejections logged; "
                   f"service exited early: {svc.proc.returncode is not None and svc.bind_s is None}",
        "results": [brief(r) for r in results],
        "health": health,
        "gunicorn_log_tail": log.splitlines()[-12:],
    }


def e4(mode, tag):
    log_dir = Path(tempfile.mkdtemp(prefix="e4_logs_"))
    audit_file = log_dir / "audit.jsonl"
    audit_file.write_text("")
    audit_file.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)      # read-only
    svc = Service(mode, env_extra={"AI201_LOG_DIR": str(log_dir)}).start()
    results = [post("/submit", {"text": VALID[i], "creator_id": f"e4_{tag}_{i}"}) for i in range(5)]
    ping = post("/ping", {"message": "still there?"})["status"]
    log = svc.stop()
    req_log = (log_dir / "requests.jsonl").read_text() if (log_dir / "requests.jsonl").exists() else ""
    audit_file.chmod(stat.S_IRUSR | stat.S_IWUSR)
    shutil.rmtree(log_dir, ignore_errors=True)
    good = sum(r["status"] == 503 and isinstance(r["body"], dict)
               and r["body"].get("error") == "audit_unavailable" and "content_id" not in r["body"]
               for r in results)
    leaked = sum(isinstance(r["body"], dict) and "content_id" in r["body"] for r in results)
    return {
        "passed": good == 5 and ping == 200 and not any(r["status"] == 500 for r in results),
        "summary": f"{good}/5 → 503 audit_unavailable with no content_id; 500s "
                   f"{sum(r['status'] == 500 for r in results)}; content_ids handed out {leaked}; /ping {ping}",
        "results": [brief(r) for r in results],
        "request_log_lines": req_log.splitlines()[-7:],
        "gunicorn_log_tail": log.splitlines()[-8:],
    }


MALFORMED = [
    {"creator_id": "e5_bad_1"},
    {"text": "", "creator_id": "e5_bad_2"},
    {"text": None, "creator_id": "e5_bad_3"},
    {"text": "too short to judge", "creator_id": "e5_bad_4"},
    {"text": ["a", "b"], "creator_id": "e5_bad_5"},
]


def e5(mode, tag, workers=None):
    svc = Service(mode, workers=workers).start()
    warm()
    time.sleep(0.05)
    t_start = now_iso()
    time.sleep(0.05)
    tally = []
    flood = [post("/submit", {"text": VALID[3], "creator_id": f"e5_{tag}_flood"})["status"] for _ in range(15)]
    tally += flood
    tally += [post("/submit", b)["status"] for b in MALFORMED]
    valid = [post("/submit", {"text": VALID[i], "creator_id": f"e5_{tag}_v{i}"}) for i in range(3)]
    tally += [r["status"] for r in valid]
    ids = [r["body"].get("content_id") for r in valid if r["status"] == 200][:2]
    tally += [post("/appeal", {"content_id": cid, "reasoning": "I wrote this myself."})["status"] for cid in ids]
    time.sleep(0.3)
    _, m = get(f"/metrics?since={t_start}")
    rss = {pid: rss_mb(pid) for pid in svc.worker_pids()}
    svc.stop()
    logged = [r for r in __import__("audit").read_requests(t_start) if r.get("path") != "/metrics"]
    client = {}
    for s in tally:
        client[str(s)] = client.get(str(s), 0) + 1
    flood_ok = flood == [200] * 5 + [429] * 10
    return {
        "passed": len(tally) == 25 and len(logged) == 25 and (m or {}).get("by_status") == client and flood_ok,
        "summary": f"sent {len(tally)}; request log {len(logged)}; client {client} vs /metrics "
                   f"{(m or {}).get('by_status')}; flood {''.join('.' if s == 200 else 'x' for s in flood)} "
                   f"({flood.count(200)}×200); worker RSS MB {rss}",
        "flood": flood,
        "client_tally": client,
        "metrics": m,
        "worker_rss_mb": rss,
    }


def _audit_entries():
    import audit
    return audit.read_entries()


CRITERIA = {"E1": e1, "E2": e2, "E3": e3, "E4": e4, "E5": e5}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["before", "after"], required=True)
    ap.add_argument("--label", default="")
    ap.add_argument("--trials", type=int, default=3)
    ap.add_argument("--only", default="")
    ap.add_argument("--skip-x1", action="store_true")
    args = ap.parse_args()

    try:
        socket.create_connection(("127.0.0.1", PORT), timeout=0.2).close()
        sys.exit(f"Something is already listening on {PORT}. Stop it first.")
    except OSError:
        pass

    chosen = [c for c in CRITERIA if not args.only or c in args.only.split(",")]
    stamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    report = {}
    for c in chosen:
        report[c] = []
        for t in range(1, args.trials + 1):
            result = CRITERIA[c](args.mode, f"{args.label}_{stamp}_t{t}")
            report[c].append(result)
            print(f"{c} trial {t}: {'MET ' if result['passed'] else 'MISS'}  {result['summary']}", flush=True)

    if not args.skip_x1 and not args.only:
        x1 = e5("before", f"{args.label}_{stamp}_x1", workers=3)
        report["X1"] = [x1]
        print(f"X1 (gunicorn -w 3): {x1['summary']}", flush=True)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / f"failures_{dt.datetime.now():%Y-%m-%d_%H%M}{'_' + args.label if args.label else ''}.md"
    lines = [f"# Extension criteria — {args.label or args.mode}", "",
             "- Produced by: `run_failures.py::main`",
             f"- Run path: {'`./serve.sh` → `gunicorn -c gunicorn.conf.py app:app`' if args.mode == 'after' else '`gunicorn app:app --bind 127.0.0.1:5002` (RUNNING.md, on loopback)'}",
             f"- {args.trials} trials per criterion, each from a fresh start · {dt.datetime.now():%Y-%m-%d %H:%M}", "",
             "| Criterion | " + " | ".join(f"Run {i}" for i in range(1, args.trials + 1)) + " | Verdict |",
             "|---|" + "---|" * args.trials + "---|"]
    for c in chosen:
        runs = report[c]
        lines.append(f"| {c} | " + " | ".join("met" if r["passed"] else "**missed**" for r in runs)
                     + f" | {'MET' if all(r['passed'] for r in runs) else 'MISSED'} |")
    lines += ["", "---", ""]
    for c, runs in report.items():
        lines += [f"## {c}", ""]
        for t, r in enumerate(runs, 1):
            lines += [f"**Trial {t}** — {r['summary']}", "", "```json", json.dumps(r, indent=2, default=str), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
