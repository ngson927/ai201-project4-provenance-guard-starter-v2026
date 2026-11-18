# Extension criteria — after

- Produced by: `run_failures.py::main`
- Run path: `./serve.sh` → `gunicorn -c gunicorn.conf.py app:app`
- 3 trials per criterion, each from a fresh start · 2026-11-18 15:40

| Criterion | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|
| E1 | met | met | met | MET |
| E2 | met | met | met | MET |
| E3 | met | met | met | MET |
| E4 | met | met | met | MET |
| E5 | met | met | met | MET |

---

## E1

**Trial 1** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.38s; slowest 4.24s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.38s; slowest 4.24s",
  "port_open_s": 0.38,
  "results": [
    {
      "status": 200,
      "seconds": 4.24
    },
    {
      "status": 200,
      "seconds": 3.23
    },
    {
      "status": 200,
      "seconds": 2.23
    },
    {
      "status": 200,
      "seconds": 1.23
    },
    {
      "status": 200,
      "seconds": 0.27
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.05
    }
  ],
  "gunicorn_log_tail": [
    "[2026-11-18 15:37:07 -0500] [37197] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:37:07 -0500] [37197] [INFO] Listening at: http://127.0.0.1:5002 (37197)",
    "[2026-11-18 15:37:07 -0500] [37197] [INFO] Using worker: gthread",
    "[2026-11-18 15:37:07 -0500] [37200] [INFO] Booting worker with pid: 37200",
    "[2026-11-18 15:37:12 -0500] [37200] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 15:37:37 -0500] [37197] [INFO] Handling signal: term",
    "[2026-11-18 15:37:38 -0500] [37200] [INFO] Worker exiting (pid: 37200)",
    "[2026-11-18 15:37:38 -0500] [37197] [INFO] Shutting down: Master"
  ]
}
```

**Trial 2** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 12.94s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 12.94s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 12.94
    },
    {
      "status": 200,
      "seconds": 11.93
    },
    {
      "status": 200,
      "seconds": 10.94
    },
    {
      "status": 200,
      "seconds": 9.94
    },
    {
      "status": 200,
      "seconds": 9.01
    },
    {
      "status": 200,
      "seconds": 8.01
    },
    {
      "status": 200,
      "seconds": 7.0
    },
    {
      "status": 200,
      "seconds": 6.02
    },
    {
      "status": 200,
      "seconds": 5.07
    },
    {
      "status": 200,
      "seconds": 4.09
    },
    {
      "status": 200,
      "seconds": 3.09
    },
    {
      "status": 200,
      "seconds": 2.09
    },
    {
      "status": 200,
      "seconds": 1.13
    },
    {
      "status": 200,
      "seconds": 0.13
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    }
  ],
  "gunicorn_log_tail": [
    "[2026-11-18 15:37:38 -0500] [37219] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:37:38 -0500] [37219] [INFO] Listening at: http://127.0.0.1:5002 (37219)",
    "[2026-11-18 15:37:38 -0500] [37219] [INFO] Using worker: gthread",
    "[2026-11-18 15:37:38 -0500] [37222] [INFO] Booting worker with pid: 37222",
    "[2026-11-18 15:37:51 -0500] [37222] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 15:38:07 -0500] [37219] [INFO] Handling signal: term",
    "[2026-11-18 15:38:08 -0500] [37222] [INFO] Worker exiting (pid: 37222)",
    "[2026-11-18 15:38:08 -0500] [37219] [INFO] Shutting down: Master"
  ]
}
```

**Trial 3** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 3.62s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 3.62s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 3.62
    },
    {
      "status": 200,
      "seconds": 2.62
    },
    {
      "status": 200,
      "seconds": 1.62
    },
    {
      "status": 200,
      "seconds": 0.61
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.04
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    },
    {
      "status": 200,
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    }
  ],
  "gunicorn_log_tail": [
    "[2026-11-18 15:38:09 -0500] [37230] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:38:09 -0500] [37230] [INFO] Listening at: http://127.0.0.1:5002 (37230)",
    "[2026-11-18 15:38:09 -0500] [37230] [INFO] Using worker: gthread",
    "[2026-11-18 15:38:09 -0500] [37233] [INFO] Booting worker with pid: 37233",
    "[2026-11-18 15:38:12 -0500] [37233] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 15:38:38 -0500] [37230] [INFO] Handling signal: term",
    "[2026-11-18 15:38:39 -0500] [37233] [INFO] Worker exiting (pid: 37233)",
    "[2026-11-18 15:38:39 -0500] [37230] [INFO] Shutting down: Master"
  ]
}
```

## E2

**Trial 1** — killed worker 37243; first 200 after 6.46s; new worker 37245; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 37243; first 200 after 6.46s; new worker 37245; gunicorn log mentions the dead worker: True",
  "recovery_s": 6.46,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 6.46,
      "at_s": 6.46
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 15:38:39 -0500] [37243] [INFO] Booting worker with pid: 37243",
    "[2026-11-18 15:38:45 -0500] [37243] [INFO] detector loaded: gpt2",
    "[2026-11-18 15:38:45 -0500] [37240] [ERROR] Worker (pid:37243) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 15:38:45 -0500] [37245] [INFO] Booting worker with pid: 37245"
  ]
}
```

**Trial 2** — killed worker 37249; first 200 after 4.11s; new worker 37250; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 37249; first 200 after 4.11s; new worker 37250; gunicorn log mentions the dead worker: True",
  "recovery_s": 4.11,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 4.11,
      "at_s": 4.11
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 15:38:52 -0500] [37249] [INFO] Booting worker with pid: 37249",
    "[2026-11-18 15:38:57 -0500] [37249] [INFO] detector loaded: gpt2",
    "[2026-11-18 15:38:57 -0500] [37246] [ERROR] Worker (pid:37249) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 15:38:57 -0500] [37250] [INFO] Booting worker with pid: 37250"
  ]
}
```

**Trial 3** — killed worker 37254; first 200 after 4.47s; new worker 37255; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 37254; first 200 after 4.47s; new worker 37255; gunicorn log mentions the dead worker: True",
  "recovery_s": 4.47,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 4.47,
      "at_s": 4.47
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 15:39:01 -0500] [37254] [INFO] Booting worker with pid: 37254",
    "[2026-11-18 15:39:07 -0500] [37254] [INFO] detector loaded: gpt2",
    "[2026-11-18 15:39:08 -0500] [37251] [ERROR] Worker (pid:37254) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 15:39:08 -0500] [37255] [INFO] Booting worker with pid: 37255"
  ]
}
```

## E3

**Trial 1** — 5/5 → 503 detector_unavailable; /ping 200; /health 200 detector_loaded=False; 5/5 rejections logged; service exited early: False

```json
{
  "passed": true,
  "summary": "5/5 \u2192 503 detector_unavailable; /ping 200; /health 200 detector_loaded=False; 5/5 rejections logged; service exited early: False",
  "results": [
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    }
  ],
  "health": {
    "detector_loaded": false,
    "detector_model": "ai201-missing-model",
    "log_entries": 798,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 15:39:13 -0500] [37256] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:39:13 -0500] [37256] [INFO] Listening at: http://127.0.0.1:5002 (37256)",
    "[2026-11-18 15:39:13 -0500] [37256] [INFO] Using worker: gthread",
    "[2026-11-18 15:39:13 -0500] [37259] [INFO] Booting worker with pid: 37259",
    "[2026-11-18 15:39:14 -0500] [37259] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 15:39:14 -0500] [37259] [INFO] Worker exiting (pid: 37259)",
    "[2026-11-18 15:39:14 -0500] [37256] [INFO] Handling signal: term",
    "[2026-11-18 15:39:14 -0500] [37256] [INFO] Shutting down: Master"
  ]
}
```

**Trial 2** — 5/5 → 503 detector_unavailable; /ping 200; /health 200 detector_loaded=False; 5/5 rejections logged; service exited early: False

```json
{
  "passed": true,
  "summary": "5/5 \u2192 503 detector_unavailable; /ping 200; /health 200 detector_loaded=False; 5/5 rejections logged; service exited early: False",
  "results": [
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    }
  ],
  "health": {
    "detector_loaded": false,
    "detector_model": "ai201-missing-model",
    "log_entries": 803,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 15:39:14 -0500] [37260] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:39:14 -0500] [37260] [INFO] Listening at: http://127.0.0.1:5002 (37260)",
    "[2026-11-18 15:39:14 -0500] [37260] [INFO] Using worker: gthread",
    "[2026-11-18 15:39:14 -0500] [37263] [INFO] Booting worker with pid: 37263",
    "[2026-11-18 15:39:15 -0500] [37263] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 15:39:15 -0500] [37263] [INFO] Worker exiting (pid: 37263)",
    "[2026-11-18 15:39:15 -0500] [37260] [INFO] Handling signal: term",
    "[2026-11-18 15:39:16 -0500] [37260] [INFO] Shutting down: Master"
  ]
}
```

**Trial 3** — 5/5 → 503 detector_unavailable; /ping 200; /health 200 detector_loaded=False; 5/5 rejections logged; service exited early: False

```json
{
  "passed": true,
  "summary": "5/5 \u2192 503 detector_unavailable; /ping 200; /health 200 detector_loaded=False; 5/5 rejections logged; service exited early: False",
  "results": [
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.0,
      "error": "detector_unavailable"
    }
  ],
  "health": {
    "detector_loaded": false,
    "detector_model": "ai201-missing-model",
    "log_entries": 808,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 15:39:16 -0500] [37264] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:39:16 -0500] [37264] [INFO] Listening at: http://127.0.0.1:5002 (37264)",
    "[2026-11-18 15:39:16 -0500] [37264] [INFO] Using worker: gthread",
    "[2026-11-18 15:39:16 -0500] [37267] [INFO] Booting worker with pid: 37267",
    "[2026-11-18 15:39:17 -0500] [37267] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 15:39:17 -0500] [37267] [INFO] Worker exiting (pid: 37267)",
    "[2026-11-18 15:39:17 -0500] [37264] [INFO] Handling signal: term",
    "[2026-11-18 15:39:17 -0500] [37264] [INFO] Shutting down: Master"
  ]
}
```

## E4

**Trial 1** — 5/5 → 503 audit_unavailable with no content_id; 500s 0; content_ids handed out 0; /ping 200

```json
{
  "passed": true,
  "summary": "5/5 \u2192 503 audit_unavailable with no content_id; 500s 0; content_ids handed out 0; /ping 200",
  "results": [
    {
      "status": 503,
      "seconds": 12.55,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.03,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.04,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.03,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.03,
      "error": "audit_unavailable"
    }
  ],
  "request_log_lines": [
    "{\"timestamp\": \"2026-11-18T20:39:30.485+00:00\", \"request_id\": \"5e187eea5d6e\", \"pid\": 37271, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 101.2, \"creator_id\": \"e4_after_20261118153707_t1_0\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:30.517+00:00\", \"request_id\": \"69d2d56f15bb\", \"pid\": 37271, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 29.6, \"creator_id\": \"e4_after_20261118153707_t1_1\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:30.553+00:00\", \"request_id\": \"22ca8d9b3ce2\", \"pid\": 37271, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 35.4, \"creator_id\": \"e4_after_20261118153707_t1_2\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:30.580+00:00\", \"request_id\": \"fc211ff7306a\", \"pid\": 37271, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 25.3, \"creator_id\": \"e4_after_20261118153707_t1_3\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:30.613+00:00\", \"request_id\": \"c76c7f54a937\", \"pid\": 37271, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 31.6, \"creator_id\": \"e4_after_20261118153707_t1_4\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:30.614+00:00\", \"request_id\": \"aff3c9dc9f67\", \"pid\": 37271, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null}"
  ],
  "gunicorn_log_tail": [
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_ubeqs7vb/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_ubeqs7vb/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_ubeqs7vb/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_ubeqs7vb/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_ubeqs7vb/audit.jsonl'",
    "[2026-11-18 15:39:30 -0500] [37268] [INFO] Handling signal: term",
    "[2026-11-18 15:39:30 -0500] [37271] [INFO] Worker exiting (pid: 37271)",
    "[2026-11-18 15:39:30 -0500] [37268] [INFO] Shutting down: Master"
  ]
}
```

**Trial 2** — 5/5 → 503 audit_unavailable with no content_id; 500s 0; content_ids handed out 0; /ping 200

```json
{
  "passed": true,
  "summary": "5/5 \u2192 503 audit_unavailable with no content_id; 500s 0; content_ids handed out 0; /ping 200",
  "results": [
    {
      "status": 503,
      "seconds": 4.63,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.03,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.04,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.03,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.03,
      "error": "audit_unavailable"
    }
  ],
  "request_log_lines": [
    "{\"timestamp\": \"2026-11-18T20:39:35.756+00:00\", \"request_id\": \"6d3871a9288c\", \"pid\": 37276, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 87.4, \"creator_id\": \"e4_after_20261118153707_t2_0\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:35.788+00:00\", \"request_id\": \"9861f690250c\", \"pid\": 37276, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 30.4, \"creator_id\": \"e4_after_20261118153707_t2_1\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:35.824+00:00\", \"request_id\": \"131f84b34927\", \"pid\": 37276, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 35.3, \"creator_id\": \"e4_after_20261118153707_t2_2\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:35.851+00:00\", \"request_id\": \"9c16bfd6330b\", \"pid\": 37276, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 25.1, \"creator_id\": \"e4_after_20261118153707_t2_3\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:35.884+00:00\", \"request_id\": \"6f3f81a6590b\", \"pid\": 37276, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 31.6, \"creator_id\": \"e4_after_20261118153707_t2_4\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:35.885+00:00\", \"request_id\": \"1419e79b501a\", \"pid\": 37276, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null}"
  ],
  "gunicorn_log_tail": [
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_nj8tygof/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_nj8tygof/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_nj8tygof/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_nj8tygof/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_nj8tygof/audit.jsonl'",
    "[2026-11-18 15:39:35 -0500] [37276] [INFO] Worker exiting (pid: 37276)",
    "[2026-11-18 15:39:35 -0500] [37273] [INFO] Handling signal: term",
    "[2026-11-18 15:39:36 -0500] [37273] [INFO] Shutting down: Master"
  ]
}
```

**Trial 3** — 5/5 → 503 audit_unavailable with no content_id; 500s 0; content_ids handed out 0; /ping 200

```json
{
  "passed": true,
  "summary": "5/5 \u2192 503 audit_unavailable with no content_id; 500s 0; content_ids handed out 0; /ping 200",
  "results": [
    {
      "status": 503,
      "seconds": 5.63,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.03,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.04,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.03,
      "error": "audit_unavailable"
    },
    {
      "status": 503,
      "seconds": 0.03,
      "error": "audit_unavailable"
    }
  ],
  "request_log_lines": [
    "{\"timestamp\": \"2026-11-18T20:39:42.018+00:00\", \"request_id\": \"18dc9b075f8a\", \"pid\": 37285, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 100.6, \"creator_id\": \"e4_after_20261118153707_t3_0\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:42.049+00:00\", \"request_id\": \"c1f9b1d5cb52\", \"pid\": 37285, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 29.5, \"creator_id\": \"e4_after_20261118153707_t3_1\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:42.087+00:00\", \"request_id\": \"32832f2f4f7f\", \"pid\": 37285, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 36.1, \"creator_id\": \"e4_after_20261118153707_t3_2\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:42.115+00:00\", \"request_id\": \"a607cfa4bbbb\", \"pid\": 37285, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 27.0, \"creator_id\": \"e4_after_20261118153707_t3_3\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:42.149+00:00\", \"request_id\": \"f3ca5a684508\", \"pid\": 37285, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 32.9, \"creator_id\": \"e4_after_20261118153707_t3_4\", \"error\": \"audit_unavailable\"}",
    "{\"timestamp\": \"2026-11-18T20:39:42.151+00:00\", \"request_id\": \"2f96c698674a\", \"pid\": 37285, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null}"
  ],
  "gunicorn_log_tail": [
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_gfljzzm7/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_gfljzzm7/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_gfljzzm7/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_gfljzzm7/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_gfljzzm7/audit.jsonl'",
    "[2026-11-18 15:39:42 -0500] [37285] [INFO] Worker exiting (pid: 37285)",
    "[2026-11-18 15:39:42 -0500] [37282] [INFO] Handling signal: term",
    "[2026-11-18 15:39:42 -0500] [37282] [INFO] Shutting down: Master"
  ]
}
```

## E5

**Trial 1** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {37291: 1008.2}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {37291: 1008.2}",
  "flood": [
    200,
    200,
    200,
    200,
    200,
    429,
    429,
    429,
    429,
    429,
    429,
    429,
    429,
    429,
    429
  ],
  "client_tally": {
    "200": 10,
    "429": 10,
    "400": 5
  },
  "metrics": {
    "by_path": {
      "/appeal": 2,
      "/submit": 23
    },
    "by_status": {
      "200": 10,
      "400": 5,
      "429": 10
    },
    "detector_loaded": true,
    "peak_rss_mb": 1008.2,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T20:39:51.168 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.5,
      "mean": 28.9,
      "p50": 28.3,
      "p95": 35.5
    },
    "worker_pid": 37291,
    "worker_started_at": "2026-11-18T20:39:42.646+00:00"
  },
  "worker_rss_mb": {
    "37291": 1008.2
  }
}
```

**Trial 2** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {37297: 1007.7}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {37297: 1007.7}",
  "flood": [
    200,
    200,
    200,
    200,
    200,
    429,
    429,
    429,
    429,
    429,
    429,
    429,
    429,
    429,
    429
  ],
  "client_tally": {
    "200": 10,
    "429": 10,
    "400": 5
  },
  "metrics": {
    "by_path": {
      "/appeal": 2,
      "/submit": 23
    },
    "by_status": {
      "200": 10,
      "400": 5,
      "429": 10
    },
    "detector_loaded": true,
    "peak_rss_mb": 1007.7,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T20:39:57.891 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.4,
      "mean": 28.7,
      "p50": 28.2,
      "p95": 35.4
    },
    "worker_pid": 37297,
    "worker_started_at": "2026-11-18T20:39:53.298+00:00"
  },
  "worker_rss_mb": {
    "37297": 1007.7
  }
}
```

**Trial 3** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {37303: 1006.9}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {37303: 1006.9}",
  "flood": [
    200,
    200,
    200,
    200,
    200,
    429,
    429,
    429,
    429,
    429,
    429,
    429,
    429,
    429,
    429
  ],
  "client_tally": {
    "200": 10,
    "429": 10,
    "400": 5
  },
  "metrics": {
    "by_path": {
      "/appeal": 2,
      "/submit": 23
    },
    "by_status": {
      "200": 10,
      "400": 5,
      "429": 10
    },
    "detector_loaded": true,
    "peak_rss_mb": 1006.9,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T20:40:03.738 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.6,
      "mean": 29.0,
      "p50": 28.3,
      "p95": 35.6
    },
    "worker_pid": 37303,
    "worker_started_at": "2026-11-18T20:40:00.020+00:00"
  },
  "worker_rss_mb": {
    "37303": 1006.9
  }
}
```

## X1

**Trial 1** — sent 25; request log 25; client {'200': 15, '429': 5, '400': 5} vs /metrics {'200': 15, '400': 5, '429': 5}; flood .....x.....xxxx (10×200); worker RSS MB {37307: 930.4, 37308: 953.3, 37309: 1010.6}

```json
{
  "passed": false,
  "summary": "sent 25; request log 25; client {'200': 15, '429': 5, '400': 5} vs /metrics {'200': 15, '400': 5, '429': 5}; flood .....x.....xxxx (10\u00d7200); worker RSS MB {37307: 930.4, 37308: 953.3, 37309: 1010.6}",
  "flood": [
    200,
    200,
    200,
    200,
    200,
    429,
    200,
    200,
    200,
    200,
    200,
    429,
    429,
    429,
    429
  ],
  "client_tally": {
    "200": 15,
    "429": 5,
    "400": 5
  },
  "metrics": {
    "by_path": {
      "/appeal": 2,
      "/submit": 23
    },
    "by_status": {
      "200": 15,
      "400": 5,
      "429": 5
    },
    "detector_loaded": true,
    "peak_rss_mb": 953.3,
    "rate_limited": 5,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T20:40:11.634 00:00",
    "submit_latency_ms": {
      "count": 13,
      "max": 7104.5,
      "mean": 839.8,
      "p50": 26.2,
      "p95": 3510.4
    },
    "worker_pid": 37308,
    "worker_started_at": "2026-11-18T20:40:05.892+00:00"
  },
  "worker_rss_mb": {
    "37307": 930.4,
    "37308": 953.3,
    "37309": 1010.6
  }
}
```
