"""
How Provenance Guard runs for real — unit 9, Path B (local, with logs).

    ./serve.sh                     # which runs: gunicorn -c gunicorn.conf.py app:app

Every number below has a reason; most of them were measured, not guessed
(README → Capstone, results/unit9/).
"""

import os
import sys

# Same variables as config.py, so `./serve.sh` and `python app.py` agree.
# Loopback by default: this is a laptop service. HOST=0.0.0.0 to open it up.
bind = f"{os.getenv('HOST', '127.0.0.1')}:{os.getenv('PORT', '5000')}"

# ONE worker. Measured (X1 in results/unit9/): each worker loads its own copy of
# GPT-2, about 1,000 MB resident. And the rate limiter keeps its counts in that
# worker's memory, so `-w 3` let 12 of a 15-request flood through instead of 5.
workers = 1

# Threads, so /health and /ping aren't stuck behind a 1–3 s scoring call. The
# model load is locked (detector._load), so threads can't load it twice.
worker_class = "gthread"
threads = 4

# The worst cold load seen before hardening was 19.8 s *inside a request*, and
# the default 30 s timeout kills a worker that goes quiet that long. With the
# model loaded at worker start (post_worker_init below) no request pays that,
# but the load itself still has to fit inside the timeout on a slower laptop.
timeout = 120
graceful_timeout = 30

# Gunicorn's own log (worker boots, deaths, tracebacks) goes to stderr. The
# structured run record is logs/requests.jsonl and logs/audit.jsonl.
errorlog = "-"
loglevel = "info"
accesslog = None
capture_output = True


def post_worker_init(worker):
    """
    Load the model before this worker takes its first request, so a cold start
    makes requests wait in the queue instead of loading inside one of them
    (criteria_extension.md E1, E2).

    A model that won't load must NOT crash the worker: a worker that fails to
    boot makes gunicorn shut the whole service down. Instead the worker comes
    up, /submit answers 503 detector_unavailable, and /health says the model
    isn't loaded (E3).
    """
    import detector

    try:
        detector.warm_up()
        worker.log.info("detector loaded: %s", os.getenv("AI201_DETECTOR_MODEL", "gpt2"))
    except detector.DetectorUnavailable as exc:
        worker.log.error("detector NOT loaded, serving 503s for /submit: %s",
                         str(exc).splitlines()[0])
    except Exception as exc:  # noqa: BLE001 — never let warm-up take the worker down
        worker.log.error("detector warm-up failed unexpectedly: %r", exc)
    sys.stderr.flush()
