#!/usr/bin/env python3
"""
Provenance Guard — the web service.

    python app.py

Then, in another terminal:

    curl -X POST http://127.0.0.1:5000/ping \
      -H "Content-Type: application/json" \
      -d '{"message": "hello"}'

That's the example route. It works right now, before you've written anything.
**Leave it alone** — it's your control. When something breaks later, check that
`/ping` still answers: if it does, the problem is in your handler; if it
doesn't, it's the service itself.

Routes:

    POST /ping        the worked example. Already works. Don't edit it
    POST /submit      ← YOU BUILD THIS (Milestone 3, 4, 5)
    POST /appeal      ← YOU BUILD THIS (Milestone 5)
    GET  /log         the audit log. Already works
    GET  /health      is the service up, and is the model loaded
"""

import os
import re
import resource
import statistics
import sys
import time
import uuid
from datetime import datetime, timezone

from flask import Flask, g, jsonify, request

import audit
import config
import scoring
import stylometry

app = Flask(__name__)

STARTED_AT = datetime.now(timezone.utc).isoformat(timespec="milliseconds")


# ── Instrumentation — UNIT 9 ──────────────────────────────────────────────────
# Every request, whatever happens to it, gets one line in logs/requests.jsonl:
# path, status, latency, which worker served it. The audit log can't show a
# request that never became a decision, or how long anything took.

@app.before_request
def _start_request():
    g.request_started = time.perf_counter()
    g.request_id = uuid.uuid4().hex[:12]


@app.after_request
def _record_request(response):
    started = g.get("request_started")
    payload = request.get_json(silent=True) if request.is_json else None
    body = response.get_json(silent=True) if response.is_json else None
    audit.log_request({
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "request_id": g.get("request_id"),
        "pid": os.getpid(),
        "method": request.method,
        "path": request.path,
        "status": response.status_code,
        "latency_ms": round((time.perf_counter() - started) * 1000, 1) if started else None,
        "creator_id": payload.get("creator_id") if isinstance(payload, dict)
                      and isinstance(payload.get("creator_id"), str) else None,
        "error": body.get("error") if isinstance(body, dict) else None,
        # /submit only: what came in (size, never the text itself), what came
        # out, and where the time went (unit 9 stretch: latency breakdown).
        "in": g.get("io_in"),
        "out": g.get("io_out"),
        "stages_ms": g.get("stages") or None,
    })
    if g.get("request_id"):
        response.headers["X-Request-ID"] = g.request_id
    return response


def _stage(name: str, since: float) -> float:
    """Record how long a /submit stage took, in ms; returns the new start."""
    now = time.perf_counter()
    g.stages[name] = round((now - since) * 1000, 2)
    return now


def _peak_rss_mb() -> float:
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes, Linux kilobytes.
    return round(peak / (1024 * 1024) if sys.platform == "darwin" else peak / 1024, 1)


@app.get("/metrics")
def metrics():
    """
    The numbers, computed from the request log.

        curl "http://127.0.0.1:5000/metrics"                     # since this worker started
        curl "http://127.0.0.1:5000/metrics?since=2026-11-18T…"  # since a moment you choose

    /metrics' own requests are left out of the counts.
    """
    import detector

    since = request.args.get("since") or STARTED_AT
    rows = [r for r in audit.read_requests(since) if r.get("path") != "/metrics"]
    by_status, by_path = {}, {}
    for r in rows:
        by_status[str(r.get("status"))] = by_status.get(str(r.get("status")), 0) + 1
        by_path[r.get("path")] = by_path.get(r.get("path"), 0) + 1
    submit_ms = sorted(r["latency_ms"] for r in rows
                       if r.get("path") == "/submit" and r.get("status") == 200
                       and r.get("latency_ms") is not None)

    def pct(p):
        return submit_ms[min(len(submit_ms) - 1, int(round(p * (len(submit_ms) - 1))))] if submit_ms else None

    return jsonify({
        "since": since,
        "worker_pid": os.getpid(),
        "worker_started_at": STARTED_AT,
        "detector_loaded": detector._model is not None,
        "peak_rss_mb": _peak_rss_mb(),
        "requests": len(rows),
        "by_status": by_status,
        "by_path": by_path,
        "rate_limited": by_status.get("429", 0),
        "server_errors": sum(n for s, n in by_status.items() if s.startswith("5")),
        "submit_latency_ms": {
            "count": len(submit_ms),
            "p50": pct(0.50),
            "p95": pct(0.95),
            "max": submit_ms[-1] if submit_ms else None,
            "mean": round(statistics.mean(submit_ms), 1) if submit_ms else None,
        },
    })


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────
# Off until you turn it on. In unit 8, Milestone 1:
#
#   1. Set RATE_LIMITING_ENABLED = True in config.py (or AI201_RATE_LIMITS=1)
#   2. Choose your numbers there
#   3. Uncomment the @limiter.limit(...) line on /submit below
#
# The order doesn't matter. While limiting is off, that decorator is a no-op
# that quietly does nothing, so uncommenting it early costs you nothing — but
# it also means no 429 until you've done step 1.
#
# The storage backend is preconfigured, which stops Flask-Limiter printing a
# warning on every start. In-memory is right for one laptop and wrong for
# anything real — a restart forgets every count.

class _LimiterOff:
    """
    Stands in for the real limiter while rate limiting is off.

    It makes @limiter.limit(...) a decorator that returns the route
    untouched, so uncommenting the line before you flip the setting is
    harmless instead of a crash on startup.
    """

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Who a request counts against.

        Falling back to the caller's address is the easy version. Unit 8's
        stretch asks about per-creator limits instead — and the difference
        matters: one script can look like a thousand callers, and one household
        can look like one.
        """
        payload = request.get_json(silent=True)
        # A body that parses as JSON but isn't an object — a bare list or
        # string — has no .get. Without this guard the key function raises
        # BEFORE the route runs, and a malformed request becomes a 500 that
        # looks like your handler crashed when your handler never ran.
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """
        A rejected request still leaves a trace.

        ⚠️ An attack that shows up only as an absence is one you'll never find.
        """
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        _log_rejection_best_effort(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
        )
        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── The worked example. Already works. Don't edit. ────────────────────────────

@app.post("/ping")
def ping():
    """
    Everything a route needs, in six lines.

    JSON arrives as a dict. You pull things out of it. You return a dict and
    the framework turns it into a response. That's the whole idea.
    """
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    """Is the service up, and has the model been downloaded yet?"""
    import detector

    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── YOU BUILD THIS ────────────────────────────────────────────────────────────

# Input limits — the contract in DESIGN.md §4. Below 20 words there's too
# little to judge, so we refuse rather than guess.
MIN_TEXT_WORDS = 20
MAX_TEXT_CHARS = 10_000
MAX_CREATOR_ID_CHARS = 100
MAX_REASONING_CHARS = 2_000

# Unit 8, Milestone 5 — the one change. Text that talks to the checker
# ("SYSTEM: …", "ignore all previous instructions", `guess=human`) isn't
# writing, and its odd tokens and clipped sentences drag BOTH signals down at
# once, so the split rule never fires and the average lands on "human" (PI01,
# PI02). Neither signal can tell, so the route refuses to *certify* such text
# as human: the label is capped at "unsure". It never pushes a score toward AI,
# so it can't accuse anyone. It matches phrasing, not intent — a paraphrase
# gets past it (README → The Improvement).
CHECKER_DIRECTED = re.compile(
    r"^\s*(system|assistant|developer)\s*:"                                     # role prefix
    r"|\b(ignore|disregard)\b[^.\n]{0,40}\b(instructions?|analysis|check|checks|scoring)\b"
    r"|\b(guess|confidence|combined_score|model_score|style_score)\s*="          # key=value
    r"|\"(guess|label|confidence|combined_score)\"\s*:"                         # injected JSON
    r"|\breturn\s+(a\s+|an\s+)?(human|ai)\b"
    r"|\bnote to the [a-z ]{0,20}(system|checker|detector|classifier)\b",
    re.IGNORECASE | re.MULTILINE,
)

@app.post("/submit")
@limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """
    Take a piece of text, decide about it, log the decision, answer.
    ← TODO — Milestones 3, 4 and 5

    Expects JSON:
        {"text": "...", "creator_id": "..."}

    Should return JSON with, at minimum:
        {"content_id": "...", "guess": "...", "confidence": 0.0, "label": "...",
         "model_score": 0.0, "style_score": 0.0}

    ⚠️ **Both signal scores go in the response, not just the log.** Unit 8's
    `run_attacks.py` and `run_eval.py` read `model_score` and `style_score`
    straight off this response and put them in your reports. Leave them out and
    every row of next unit's evidence says `null` — which is exactly the
    diagnostic you need to name a stage and a mechanism. You do not want to
    find that out after running the attack set.

    ─────────────────────────────────────────────────────────────────────────
    Build it in three passes. Do not skip ahead — the ordering is how you tell
    a broken route from a broken signal.

    **Milestone 3 — the route answers.**
      1. Return a hardcoded response. Confirm `curl` gets it back before you
         add any logic at all.
      2. Then pull `text` and `creator_id` out of the payload.
      3. Then call ONE signal — `detector.model_signal(text)` — and put the
         real number in. Leave confidence and label as placeholders.
      4. Log every submission with `audit.log_decision(...)`. The content_id
         matters: `/appeal` needs it, and a student who skips it rebuilds this
         whole flow later.

    **Milestone 4 — the second signal and the score.**
      5. Add `stylometry.style_signal(text)`.
      6. Combine them with `scoring.combine_signals(...)`.
      7. Log BOTH signal scores alongside the combined one, and put them in the
         response too. Next unit you can't diagnose anything without them.

    **Milestone 5 — the label.**
      8. `scoring.score_to_label(...)` and put the real label in the response.

    ─────────────────────────────────────────────────────────────────────────
    Worth deciding early, because unit 8's attack set will decide it for you:
    what should this do when `text` is missing, empty, or enormous? A crash on
    a malformed input is one of the most common real failures there is.
    """
    g.stages = {}
    t = time.perf_counter()
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return _refuse("unknown", "invalid_json", "Send a JSON object with 'text' and 'creator_id'.")

    raw_creator = payload.get("creator_id")
    creator_id = raw_creator.strip() if isinstance(raw_creator, str) else ""
    log_creator = creator_id or "unknown"

    text = payload.get("text")
    if not isinstance(text, str) or not text.strip():
        return _refuse(log_creator, "missing_text", "There's no text to check. Send it in the 'text' field.")
    text = text.strip()
    g.io_in = {"text_words": len(text.split()), "text_chars": len(text)}
    if len(text) > MAX_TEXT_CHARS:
        return _refuse(log_creator, "text_too_long",
                       f"That's too long to check. Send at most {MAX_TEXT_CHARS:,} characters.")
    if len(text.split()) < MIN_TEXT_WORDS:
        return _refuse(log_creator, "text_too_short",
                       f"That's too short to judge fairly. Send at least {MIN_TEXT_WORDS} words.")

    if not creator_id or len(creator_id) > MAX_CREATOR_ID_CHARS:
        return _refuse(log_creator, "missing_creator_id",
                       f"Send a 'creator_id' of 1 to {MAX_CREATOR_ID_CHARS} characters.")

    content_id = str(uuid.uuid4())
    t = _stage("checks", t)

    import detector

    try:
        model_score = detector.model_signal(text)
    except detector.DetectorUnavailable:
        return _refuse(creator_id, "detector_unavailable",
                       "The checker isn't available right now. Try again shortly.", status=503)
    t = _stage("signal_one", t)

    style_score = stylometry.style_signal(text)
    t = _stage("signal_two", t)
    confidence = scoring.combine_signals(model_score, style_score)

    guess, label = scoring.score_to_label(confidence)

    checker_directed = bool(CHECKER_DIRECTED.search(text))
    if checker_directed and guess == "human":
        guess, label = "unsure", scoring.LABEL_UNSURE
    t = _stage("combine_label", t)

    # Unit 9 (criteria_extension.md E4): /appeal finds a submission through
    # this log. A content_id handed out without an entry is an appeal that
    # will 404, so if the decision can't be recorded, it isn't handed out.
    try:
        audit.log_decision(
            content_id=content_id,
            creator_id=creator_id,
            guess=guess,
            model_score=model_score,
            style_score=style_score,
            combined_score=confidence,
            label=label,
            checker_directed=checker_directed,
        )
    except audit.AuditUnavailable as exc:
        print(f"submit refused, decision not recorded: {exc}", file=sys.stderr, flush=True)
        return _audit_unavailable()
    _stage("audit_write", t)
    g.io_out = {"content_id": content_id, "guess": guess, "confidence": confidence,
                "model_score": model_score, "style_score": style_score}

    return jsonify({
        "content_id": content_id,
        "creator_id": creator_id,
        "guess": guess,
        "confidence": confidence,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
        "checker_directed": checker_directed,
        "status": "decided",
    })


def _refuse(creator_id, error, message, status=400):
    """Turn a request away, and leave a trace of it in the log."""
    _log_rejection_best_effort(creator_id=creator_id, reason=error)
    return jsonify({"error": error, "message": message}), status


def _log_rejection_best_effort(**fields):
    """
    Unit 9: a refusal must still be a clean refusal when the audit log can't
    be written. The request log (logs/requests.jsonl) still has it, and the
    failure goes to stderr, which is gunicorn's error log.
    """
    try:
        audit.log_rejection(**fields)
    except audit.AuditUnavailable as exc:
        print(f"rejection not recorded in audit log: {exc} {fields}", file=sys.stderr, flush=True)


def _audit_unavailable():
    return jsonify({
        "error": "audit_unavailable",
        "message": "We can't record decisions right now, so we're not making one. "
                   "Nothing was saved. Please try again shortly.",
    }), 503


@app.errorhandler(Exception)
def _unexpected(exc):
    """
    Unit 9: anything nobody planned for still comes back as JSON with an error
    code, not Flask's HTML page. The traceback goes to the error log; the
    request log records the 500 with `error: internal_error`.
    """
    from werkzeug.exceptions import HTTPException

    if isinstance(exc, HTTPException):          # 404, 405, 429… keep their own answer
        return exc
    app.logger.exception("unhandled error in %s", request.path)
    return jsonify({"error": "internal_error",
                    "message": "Something went wrong on our side. Nothing was decided."}), 500


@app.post("/appeal")
def appeal():
    """
    A writer says you got it wrong. ← TODO — Milestone 5

    Expects JSON:
        {"content_id": "...", "reasoning": "..."}

    Should:
      1. Check the content_id actually exists — `audit.entries_for(id)` tells
         you. A typo here fails silently and looks like a broken endpoint,
         which is the single most common way this milestone eats an hour.
      2. Record the appeal with `audit.log_appeal(...)`, which moves the item
         to `under_review`.
      3. Confirm to the writer. No automatic re-checking needed.

    This is the smallest endpoint in the project and the one that matters most
    to the person on the other end. It's the only thing standing between a
    wrong accusation and nothing at all.
    """
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return _refuse("unknown", "invalid_json", "Send a JSON object with 'content_id' and 'reasoning'.")

    content_id = payload.get("content_id")
    if not isinstance(content_id, str) or not content_id.strip():
        return _refuse("unknown", "missing_content_id",
                       "Send the 'content_id' you got back when you submitted your writing.")
    content_id = content_id.strip()

    reasoning = payload.get("reasoning")
    if not isinstance(reasoning, str) or not reasoning.strip() or len(reasoning) > MAX_REASONING_CHARS:
        return _refuse("unknown", "missing_reasoning",
                       f"Tell us in 'reasoning' why you think we got it wrong "
                       f"(1 to {MAX_REASONING_CHARS:,} characters).")
    reasoning = reasoning.strip()

    entries = audit.entries_for(content_id)
    decision = next((e for e in entries if e.get("status") == "decided" and "event" not in e), None)
    if decision is None:
        return _refuse("unknown", "unknown_content_id",
                       "We couldn't find a submission with that content_id. Check it was copied exactly.",
                       status=404)

    # The creator comes from the original decision, never the request — so
    # nobody can appeal under someone else's name.
    creator_id = decision.get("creator_id", "unknown")
    if any(e.get("event") == "appeal" for e in entries):
        return _refuse(creator_id, "already_under_review",
                       "This one is already waiting for a person to review it.", status=409)

    try:
        audit.log_appeal(content_id=content_id, creator_id=creator_id, reasoning=reasoning)
    except audit.AuditUnavailable as exc:
        # An appeal that isn't recorded never reaches a reviewer. Saying it was
        # received would be the worst answer here.
        print(f"appeal not recorded: {exc}", file=sys.stderr, flush=True)
        return _audit_unavailable()

    return jsonify({
        "content_id": content_id,
        "status": "under_review",
        "original_guess": decision.get("guess"),
        "message": "Thanks — your appeal has been recorded and a person will review this "
                   "decision. Until then, the automated label is not a final judgement.",
    })


@app.get("/content/<content_id>")
def content_status(content_id):
    """
    One item's current state — stretch feature, declared in the README first.

    Status comes from the latest entry, so an appealed item reads
    `under_review`. The appeal's reasoning is left out: that's for the
    reviewer, not for anyone who has the id. Read-only — never writes.
    """
    entries = audit.entries_for(content_id)
    decision = next((e for e in entries if e.get("status") == "decided" and "event" not in e), None)
    if decision is None:
        return jsonify({
            "error": "unknown_content_id",
            "message": "We couldn't find a submission with that content_id. Check it was copied exactly.",
        }), 404

    appeal_entry = next((e for e in entries if e.get("event") == "appeal"), None)
    return jsonify({
        "content_id": content_id,
        "creator_id": decision.get("creator_id"),
        "status": entries[-1].get("status"),
        "guess": decision.get("guess"),
        "label": decision.get("label"),
        "confidence": decision.get("combined_score"),
        "model_score": decision.get("model_score"),
        "style_score": decision.get("style_score"),
        "submitted_at": decision.get("timestamp"),
        "appealed_at": appeal_entry.get("timestamp") if appeal_entry else None,
    })


# ── Already works ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    """
    The audit log, most recent last.

        curl "http://127.0.0.1:5000/log?limit=10"

    You need this in unit 8 to paste entries into your README, and you need it
    now to see whether your logging is actually working.
    """
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    # debug=True hands out an interactive debugger, so it's local-only — see config.py
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
