# Clean-checkout test — 2026-11-18

A fresh `git clone` of commit `1301919` into an empty folder, set up and started with only the commands in RUNNING.md → "Run it for real". Transcript from `sh -x` (the poll loop and the cloned repo's own committed logs are trimmed).

**Caveat:** pip installed from its local wheel cache, and the GPT-2 weights came from the shared `~/.cache/huggingface`, so the first-time ~550 MB model download is not part of this test.

```
+ cd /private/tmp/claude-501/-Users-sonnguyen-ai201-project4-provenance-guard-starter-v2026/fb4d5db2-51a0-4914-86cd-b5e5460894d7/scratchpad/clean
+ git log --oneline -1
1301919 Unit 9: harden the bad paths and give the service a real run path
+ date
Wed Nov 18 15:41:11 EST 2026
+ python3 -m venv .venv
+ .venv/bin/pip install -q -r requirements.txt
+ tail -3

[notice] A new release of pip is available: 24.3.1 -> 26.3
[notice] To update, run: python3.13 -m pip install --upgrade pip
+ date
Wed Nov 18 15:41:36 EST 2026
+ .venv/bin/python --version
Python 3.13.1
+ PORT=5003
+ ./serve.sh
+ MASTER=37414
+ curl -s -X POST http://127.0.0.1:5003/ping -H 'Content-Type: application/json' -d '{"message":"clean checkout"}'
{"ok":true,"service":"provenance-guard","you_sent":"clean checkout"}
+ echo

+ curl -s -X POST http://127.0.0.1:5003/submit -H 'Content-Type: application/json' -d '{"text":"We got to the campsite about four. The pitch was fine, a bit sloped, but there was a tap nearby and the toilets were clean enough. Putting the tent up took longer t
+ head -c 400
{"checker_directed":false,"confidence":0.5961,"content_id":"51875564-1f53-4ddf-9c9b-715ac69111a0","creator_id":"clean_checkout","guess":"unsure","label":"We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in b

+ curl -s http://127.0.0.1:5003/health
{"detector_loaded":true,"detector_model":"gpt2","log_entries":913,"ok":true,"rate_limiting":true}
+ echo

+ kill -TERM 37414
+ sleep 3
+ cat serve.out
[2026-11-18 15:41:36 -0500] [37414] [INFO] Starting gunicorn 23.0.0
[2026-11-18 15:41:36 -0500] [37414] [INFO] Listening at: http://127.0.0.1:5003 (37414)
[2026-11-18 15:41:36 -0500] [37414] [INFO] Using worker: gthread
[2026-11-18 15:41:36 -0500] [37420] [INFO] Booting worker with pid: 37420
[2026-11-18 15:41:42 -0500] [37420] [INFO] detector loaded: gpt2
`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
[2026-11-18 15:41:43 -0500] [37414] [INFO] Handling signal: term
[2026-11-18 15:41:44 -0500] [37420] [INFO] Worker exiting (pid: 37420)
[2026-11-18 15:41:44 -0500] [37414] [INFO] Shutting down: Master
+ cat logs/requests.jsonl      # (only the 3 lines this run added)
{"timestamp": "2026-11-18T20:41:43.326+00:00", "request_id": "2fd493ad26fc", "pid": 37420, "method": "POST", "path": "/ping", "status": 200, "latency_ms": 0.2, "creator_id": null, "error": null}
{"timestamp": "2026-11-18T20:41:43.405+00:00", "request_id": "56374cd42c2d", "pid": 37420, "method": "POST", "path": "/submit", "status": 200, "latency_ms": 70.1, "creator_id": "clean_checkout", "error": null}
{"timestamp": "2026-11-18T20:41:43.414+00:00", "request_id": "3000a7af3c2c", "pid": 37420, "method": "GET", "path": "/health", "status": 200, "latency_ms": 1.9, "creator_id": null, "error": null}
```
