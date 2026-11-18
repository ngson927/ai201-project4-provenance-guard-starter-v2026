#!/bin/sh
# Provenance Guard — the one command that starts it (unit 9, Path B).
#
#   ./serve.sh                    # http://127.0.0.1:5000
#   PORT=5002 ./serve.sh          # another port (macOS AirPlay often holds 5000)
#
# Setup, once, from a clean checkout — see RUNNING.md → "Run it for real".
set -e
cd "$(dirname "$0")"

if [ ! -x .venv/bin/gunicorn ]; then
    echo "No .venv with gunicorn here. Set up first:" >&2
    echo "  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt" >&2
    exit 1
fi

mkdir -p "${AI201_LOG_DIR:-logs}"
exec .venv/bin/gunicorn -c gunicorn.conf.py app:app
