#!/usr/bin/env python3
"""
Unit 9 stretch — measured, against a service already running via ./serve.sh.

    PORT=5001 ./serve.sh                                 # in one terminal (real config)
    python run_perf.py --url http://127.0.0.1:5001       # in another

Two measurements, both declared in the README before they were built:

  latency   50 warm /submit requests, one at a time. Where the time goes,
            from the `stages_ms` each request writes to logs/requests.jsonl.
  load      "normal" (1 submission/second for 60 s), then 10x that
            (10/second for 60 s), each request with its own creator_id.
            Throughput, latency, errors, memory, and how many were in flight.

Writes results/unit9/perf_<date>.md.
"""

import argparse
import datetime as dt
import json
import statistics
import subprocess
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests

import audit
import config
from calibrate import CLEARLY_AI, CLEARLY_HUMAN, CLEARLY_HUMAN_2, FORMAL_HUMAN, PLAIN_HUMAN

TEXTS = [CLEARLY_HUMAN, CLEARLY_AI, FORMAL_HUMAN, PLAIN_HUMAN, CLEARLY_HUMAN_2]
STAGES = ["checks", "signal_one", "signal_two", "combine_label", "audit_write"]


def pct(values, p):
    v = sorted(values)
    return round(v[min(len(v) - 1, int(round(p * (len(v) - 1))))], 2) if v else None


def rss_mb(pid):
    out = subprocess.run(["ps", "-o", "rss=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
    return round(int(out) / 1024, 1) if out else None


def latency(url, n, tag):
    ids = [f"perf_lat_{tag}_{i}" for i in range(n)]
    for i, cid in enumerate(ids):
        r = requests.post(f"{url}/submit", json={"text": TEXTS[i % 5], "creator_id": cid}, timeout=60)
        assert r.status_code == 200, r.text
    time.sleep(0.3)
    rows = [r for r in audit.read_requests() if r.get("creator_id") in set(ids)]
    total = [r["latency_ms"] for r in rows]
    out = {"requests": len(rows), "total_ms": {"mean": round(statistics.mean(total), 2),
                                                "p50": pct(total, .5), "p95": pct(total, .95)}}
    stage_rows = {}
    for s in STAGES:
        vals = [r["stages_ms"][s] for r in rows]
        stage_rows[s] = {"mean": round(statistics.mean(vals), 3), "p50": pct(vals, .5), "p95": pct(vals, .95)}
    overhead = [r["latency_ms"] - sum(r["stages_ms"].values()) for r in rows]
    stage_rows["outside the stages (Flask, JSON, rate-limit check, request log)"] = {
        "mean": round(statistics.mean(overhead), 3), "p50": pct(overhead, .5), "p95": pct(overhead, .95)}
    mean_total = statistics.mean(total)
    for v in stage_rows.values():
        v["share_of_mean"] = f"{100 * v['mean'] / mean_total:.1f}%"
    out["stages"] = stage_rows
    out["example_line"] = rows[0]
    return out


def load(url, rate, seconds, tag, pid):
    n = rate * seconds
    results, in_flight, peak = [None] * n, [0], [0]
    lock = threading.Lock()
    rss_samples = []
    stop = threading.Event()

    def sampler():
        while not stop.is_set():
            rss_samples.append(rss_mb(pid))
            stop.wait(2)

    def fire(i):
        target = t0 + i / rate
        time.sleep(max(0, target - time.monotonic()))
        lag = time.monotonic() - target
        with lock:
            in_flight[0] += 1
            peak[0] = max(peak[0], in_flight[0])
        t = time.monotonic()
        try:
            r = requests.post(f"{url}/submit", json={"text": TEXTS[i % 5], "creator_id": f"perf_load_{tag}_{i}"},
                              timeout=60)
            status = r.status_code
        except requests.RequestException as exc:
            status = type(exc).__name__
        done = time.monotonic()
        with lock:
            in_flight[0] -= 1
        results[i] = {"status": status, "ms": (done - t) * 1000, "sent_at": t - t0, "done_at": done - t0,
                      "client_lag_ms": lag * 1000}

    th = threading.Thread(target=sampler, daemon=True)
    th.start()
    t0 = time.monotonic()
    with ThreadPoolExecutor(max_workers=min(200, n)) as pool:
        list(pool.map(fire, range(n)))
    wall = time.monotonic() - t0
    stop.set()
    th.join()

    ms = [r["ms"] for r in results if r["status"] == 200]
    statuses = {}
    for r in results:
        statuses[str(r["status"])] = statuses.get(str(r["status"]), 0) + 1
    windows = []
    for w in range(0, seconds, 10):
        part = [r["ms"] for r in results if w <= r["sent_at"] < w + 10 and r["status"] == 200]
        windows.append({"window_s": f"{w}-{w + 10}", "n": len(part), "p50_ms": pct(part, .5), "p95_ms": pct(part, .95)})
    return {
        "rate_per_s": rate, "seconds": seconds, "sent": n, "statuses": statuses,
        "wall_s": round(wall, 2),
        "throughput_per_s": round(statuses.get("200", 0) / (max(r["done_at"] for r in results)), 2),
        "latency_ms": {"p50": pct(ms, .5), "p95": pct(ms, .95), "p99": pct(ms, .99), "max": round(max(ms), 1) if ms else None,
                       "mean": round(statistics.mean(ms), 1) if ms else None},
        "peak_in_flight": peak[0],
        "client_send_lag_ms_max": round(max(r["client_lag_ms"] for r in results), 1),
        "worker_rss_mb": {"min": min(rss_samples), "max": max(rss_samples)},
        "by_10s_window": windows,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url", default="http://127.0.0.1:5001")
    ap.add_argument("--latency-n", type=int, default=50)
    ap.add_argument("--seconds", type=int, default=60)
    args = ap.parse_args()

    m = requests.get(f"{args.url}/metrics", timeout=10).json()
    if not m.get("detector_loaded"):
        raise SystemExit("Model not loaded yet — wait for /health to say detector_loaded: true.")
    pid = m["worker_pid"]
    tag = dt.datetime.now().strftime("%H%M%S")
    report = {"worker_pid": pid, "rss_before_mb": rss_mb(pid)}
    print("latency breakdown …", flush=True)
    report["latency"] = latency(args.url, args.latency_n, tag)
    print("load: normal (1/s) …", flush=True)
    report["load_normal"] = load(args.url, 1, args.seconds, tag + "n", pid)
    print("load: 10x (10/s) …", flush=True)
    report["load_10x"] = load(args.url, 10, args.seconds, tag + "x", pid)
    report["rss_after_mb"] = rss_mb(pid)

    out = config.RESULTS_DIR / "unit9" / f"perf_{dt.datetime.now():%Y-%m-%d_%H%M}.md"
    out.write_text("# Unit 9 stretch — latency breakdown and load observation\n\n"
                   "- Produced by: `run_perf.py::main` against `./serve.sh` (real config, rate limiting on; one creator_id per request)\n"
                   f"- {dt.datetime.now():%Y-%m-%d %H:%M}\n\n```json\n"
                   + json.dumps(report, indent=2) + "\n```\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("rss_before_mb", "rss_after_mb")}))
    print(json.dumps(report["latency"]["stages"], indent=1))
    for k in ("load_normal", "load_10x"):
        print(k, json.dumps({x: report[k][x] for x in report[k] if x != "by_10s_window"}))
        print("  windows", report[k]["by_10s_window"])
    print(f"Wrote {out.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
