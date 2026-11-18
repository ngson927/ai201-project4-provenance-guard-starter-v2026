# Extension criteria — before

- Produced by: `run_failures.py::main`
- Run path: `gunicorn app:app --bind 127.0.0.1:5002` (RUNNING.md, on loopback)
- 3 trials per criterion, each from a fresh start · 2026-11-18 15:35

| Criterion | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|
| E1 | met | met | met | MET |
| E2 | met | met | met | MET |
| E3 | met | met | met | MET |
| E4 | **missed** | **missed** | **missed** | MISSED |
| E5 | met | met | met | MET |

---

## E1

**Trial 1** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.06s; slowest 3.54s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.06s; slowest 3.54s",
  "port_open_s": 0.06,
  "results": [
    {
      "status": 200,
      "seconds": 3.54
    },
    {
      "status": 200,
      "seconds": 2.56
    },
    {
      "status": 200,
      "seconds": 1.61
    },
    {
      "status": 200,
      "seconds": 0.65
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
    "[2026-11-18 15:31:56 -0500] [36905] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:31:56 -0500] [36905] [INFO] Listening at: http://127.0.0.1:5002 (36905)",
    "[2026-11-18 15:31:56 -0500] [36905] [INFO] Using worker: sync",
    "[2026-11-18 15:31:56 -0500] [36906] [INFO] Booting worker with pid: 36906",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 15:32:25 -0500] [36905] [INFO] Handling signal: term",
    "[2026-11-18 15:32:25 -0500] [36906] [INFO] Worker exiting (pid: 36906)",
    "[2026-11-18 15:32:25 -0500] [36905] [INFO] Shutting down: Master"
  ]
}
```

**Trial 2** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 19.77s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 19.77s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 19.77
    },
    {
      "status": 200,
      "seconds": 18.8
    },
    {
      "status": 200,
      "seconds": 17.83
    },
    {
      "status": 200,
      "seconds": 16.86
    },
    {
      "status": 200,
      "seconds": 15.89
    },
    {
      "status": 200,
      "seconds": 14.93
    },
    {
      "status": 200,
      "seconds": 13.96
    },
    {
      "status": 200,
      "seconds": 12.99
    },
    {
      "status": 200,
      "seconds": 12.01
    },
    {
      "status": 200,
      "seconds": 11.05
    },
    {
      "status": 200,
      "seconds": 10.08
    },
    {
      "status": 200,
      "seconds": 9.11
    },
    {
      "status": 200,
      "seconds": 8.14
    },
    {
      "status": 200,
      "seconds": 7.17
    },
    {
      "status": 200,
      "seconds": 6.2
    },
    {
      "status": 200,
      "seconds": 5.23
    },
    {
      "status": 200,
      "seconds": 4.26
    },
    {
      "status": 200,
      "seconds": 3.3
    },
    {
      "status": 200,
      "seconds": 2.32
    },
    {
      "status": 200,
      "seconds": 1.36
    },
    {
      "status": 200,
      "seconds": 0.39
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
    }
  ],
  "gunicorn_log_tail": [
    "[2026-11-18 15:32:25 -0500] [36929] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:32:25 -0500] [36929] [INFO] Listening at: http://127.0.0.1:5002 (36929)",
    "[2026-11-18 15:32:25 -0500] [36929] [INFO] Using worker: sync",
    "[2026-11-18 15:32:25 -0500] [36931] [INFO] Booting worker with pid: 36931",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 15:32:54 -0500] [36931] [INFO] Worker exiting (pid: 36931)",
    "[2026-11-18 15:32:54 -0500] [36929] [INFO] Handling signal: term",
    "[2026-11-18 15:32:55 -0500] [36929] [INFO] Shutting down: Master"
  ]
}
```

**Trial 3** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.06s; slowest 4.71s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.06s; slowest 4.71s",
  "port_open_s": 0.06,
  "results": [
    {
      "status": 200,
      "seconds": 4.71
    },
    {
      "status": 200,
      "seconds": 3.74
    },
    {
      "status": 200,
      "seconds": 2.78
    },
    {
      "status": 200,
      "seconds": 1.8
    },
    {
      "status": 200,
      "seconds": 0.83
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
      "seconds": 0.05
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
      "seconds": 0.04
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
      "seconds": 0.04
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
      "seconds": 0.06
    }
  ],
  "gunicorn_log_tail": [
    "[2026-11-18 15:32:55 -0500] [36963] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:32:55 -0500] [36963] [INFO] Listening at: http://127.0.0.1:5002 (36963)",
    "[2026-11-18 15:32:55 -0500] [36963] [INFO] Using worker: sync",
    "[2026-11-18 15:32:55 -0500] [36964] [INFO] Booting worker with pid: 36964",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 15:33:24 -0500] [36964] [INFO] Worker exiting (pid: 36964)",
    "[2026-11-18 15:33:24 -0500] [36963] [INFO] Handling signal: term",
    "[2026-11-18 15:33:24 -0500] [36963] [INFO] Shutting down: Master"
  ]
}
```

## E2

**Trial 1** — killed worker 37006; first 200 after 3.46s; new worker 37020; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 37006; first 200 after 3.46s; new worker 37020; gunicorn log mentions the dead worker: True",
  "recovery_s": 3.46,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 3.46,
      "at_s": 3.46
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 15:33:24 -0500] [37006] [INFO] Booting worker with pid: 37006",
    "[2026-11-18 15:33:29 -0500] [37005] [ERROR] Worker (pid:37006) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 15:33:29 -0500] [37020] [INFO] Booting worker with pid: 37020"
  ]
}
```

**Trial 2** — killed worker 37022; first 200 after 8.89s; new worker 37027; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 37022; first 200 after 8.89s; new worker 37027; gunicorn log mentions the dead worker: True",
  "recovery_s": 8.89,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 8.89,
      "at_s": 8.89
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 15:33:33 -0500] [37022] [INFO] Booting worker with pid: 37022",
    "[2026-11-18 15:33:37 -0500] [37021] [ERROR] Worker (pid:37022) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 15:33:37 -0500] [37027] [INFO] Booting worker with pid: 37027"
  ]
}
```

**Trial 3** — killed worker 37033; first 200 after 2.13s; new worker 37034; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 37033; first 200 after 2.13s; new worker 37034; gunicorn log mentions the dead worker: True",
  "recovery_s": 2.13,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 2.13,
      "at_s": 2.13
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 15:33:47 -0500] [37033] [INFO] Booting worker with pid: 37033",
    "[2026-11-18 15:33:50 -0500] [37032] [ERROR] Worker (pid:37033) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 15:33:50 -0500] [37034] [INFO] Booting worker with pid: 37034"
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
      "seconds": 1.1,
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
    "log_entries": 583,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 15:33:52 -0500] [37035] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:33:52 -0500] [37035] [INFO] Listening at: http://127.0.0.1:5002 (37035)",
    "[2026-11-18 15:33:52 -0500] [37035] [INFO] Using worker: sync",
    "[2026-11-18 15:33:52 -0500] [37036] [INFO] Booting worker with pid: 37036",
    "[2026-11-18 15:33:53 -0500] [37036] [INFO] Worker exiting (pid: 37036)",
    "[2026-11-18 15:33:53 -0500] [37035] [INFO] Handling signal: term",
    "[2026-11-18 15:33:54 -0500] [37035] [INFO] Shutting down: Master"
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
      "seconds": 1.1,
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
    "log_entries": 588,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 15:33:54 -0500] [37037] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:33:54 -0500] [37037] [INFO] Listening at: http://127.0.0.1:5002 (37037)",
    "[2026-11-18 15:33:54 -0500] [37037] [INFO] Using worker: sync",
    "[2026-11-18 15:33:54 -0500] [37038] [INFO] Booting worker with pid: 37038",
    "[2026-11-18 15:33:55 -0500] [37038] [INFO] Worker exiting (pid: 37038)",
    "[2026-11-18 15:33:55 -0500] [37037] [INFO] Handling signal: term",
    "[2026-11-18 15:33:55 -0500] [37037] [INFO] Shutting down: Master"
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
      "seconds": 1.1,
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
    "log_entries": 593,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 15:33:55 -0500] [37039] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 15:33:55 -0500] [37039] [INFO] Listening at: http://127.0.0.1:5002 (37039)",
    "[2026-11-18 15:33:55 -0500] [37039] [INFO] Using worker: sync",
    "[2026-11-18 15:33:55 -0500] [37040] [INFO] Booting worker with pid: 37040",
    "[2026-11-18 15:33:57 -0500] [37040] [INFO] Worker exiting (pid: 37040)",
    "[2026-11-18 15:33:57 -0500] [37039] [INFO] Handling signal: term",
    "[2026-11-18 15:33:57 -0500] [37039] [INFO] Shutting down: Master"
  ]
}
```

## E4

**Trial 1** — 0/5 → 503 audit_unavailable with no content_id; 500s 5; content_ids handed out 0; /ping 200

```json
{
  "passed": false,
  "summary": "0/5 \u2192 503 audit_unavailable with no content_id; 500s 5; content_ids handed out 0; /ping 200",
  "results": [
    {
      "status": 500,
      "seconds": 2.45
    },
    {
      "status": 500,
      "seconds": 0.03
    },
    {
      "status": 500,
      "seconds": 0.04
    },
    {
      "status": 500,
      "seconds": 0.03
    },
    {
      "status": 500,
      "seconds": 0.03
    }
  ],
  "request_log_lines": [
    "{\"timestamp\": \"2026-11-18T20:33:59.954+00:00\", \"request_id\": \"4172cbc36a60\", \"pid\": 37042, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 2393.4, \"creator_id\": \"e4_before_20261118153156_t1_0\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:33:59.986+00:00\", \"request_id\": \"e9ae249d974c\", \"pid\": 37042, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 30.2, \"creator_id\": \"e4_before_20261118153156_t1_1\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:00.025+00:00\", \"request_id\": \"410f1978ae90\", \"pid\": 37042, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 37.3, \"creator_id\": \"e4_before_20261118153156_t1_2\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:00.052+00:00\", \"request_id\": \"0aac8055f228\", \"pid\": 37042, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 26.2, \"creator_id\": \"e4_before_20261118153156_t1_3\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:00.086+00:00\", \"request_id\": \"7b5401c71490\", \"pid\": 37042, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 32.4, \"creator_id\": \"e4_before_20261118153156_t1_4\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:00.087+00:00\", \"request_id\": \"1c6c5e7f1278\", \"pid\": 37042, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null}"
  ],
  "gunicorn_log_tail": [
    "         ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^",
    "  File \"/opt/homebrew/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pathlib/_local.py\", line 537, in open",
    "    return io.open(self, mode, buffering, encoding, errors, newline)",
    "           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
    "PermissionError: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs__2jbqjsb/audit.jsonl'",
    "[2026-11-18 15:34:00 -0500] [37042] [INFO] Worker exiting (pid: 37042)",
    "[2026-11-18 15:34:00 -0500] [37041] [INFO] Handling signal: term",
    "[2026-11-18 15:34:00 -0500] [37041] [INFO] Shutting down: Master"
  ]
}
```

**Trial 2** — 0/5 → 503 audit_unavailable with no content_id; 500s 5; content_ids handed out 0; /ping 200

```json
{
  "passed": false,
  "summary": "0/5 \u2192 503 audit_unavailable with no content_id; 500s 5; content_ids handed out 0; /ping 200",
  "results": [
    {
      "status": 500,
      "seconds": 3.75
    },
    {
      "status": 500,
      "seconds": 0.03
    },
    {
      "status": 500,
      "seconds": 0.04
    },
    {
      "status": 500,
      "seconds": 0.03
    },
    {
      "status": 500,
      "seconds": 0.03
    }
  ],
  "request_log_lines": [
    "{\"timestamp\": \"2026-11-18T20:34:04.240+00:00\", \"request_id\": \"80ba335cd819\", \"pid\": 37044, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 3689.4, \"creator_id\": \"e4_before_20261118153156_t2_0\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:04.272+00:00\", \"request_id\": \"51fd89e66c45\", \"pid\": 37044, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 29.8, \"creator_id\": \"e4_before_20261118153156_t2_1\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:04.309+00:00\", \"request_id\": \"be7f8ea1b4b4\", \"pid\": 37044, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 36.2, \"creator_id\": \"e4_before_20261118153156_t2_2\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:04.336+00:00\", \"request_id\": \"7be52ae9619d\", \"pid\": 37044, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 25.9, \"creator_id\": \"e4_before_20261118153156_t2_3\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:04.370+00:00\", \"request_id\": \"a0cfca0fc961\", \"pid\": 37044, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 32.5, \"creator_id\": \"e4_before_20261118153156_t2_4\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:04.371+00:00\", \"request_id\": \"2e81180ee542\", \"pid\": 37044, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null}"
  ],
  "gunicorn_log_tail": [
    "         ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^",
    "  File \"/opt/homebrew/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pathlib/_local.py\", line 537, in open",
    "    return io.open(self, mode, buffering, encoding, errors, newline)",
    "           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
    "PermissionError: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_hq7g0s5b/audit.jsonl'",
    "[2026-11-18 15:34:04 -0500] [37044] [INFO] Worker exiting (pid: 37044)",
    "[2026-11-18 15:34:04 -0500] [37043] [INFO] Handling signal: term",
    "[2026-11-18 15:34:04 -0500] [37043] [INFO] Shutting down: Master"
  ]
}
```

**Trial 3** — 0/5 → 503 audit_unavailable with no content_id; 500s 5; content_ids handed out 0; /ping 200

```json
{
  "passed": false,
  "summary": "0/5 \u2192 503 audit_unavailable with no content_id; 500s 5; content_ids handed out 0; /ping 200",
  "results": [
    {
      "status": 500,
      "seconds": 19.11
    },
    {
      "status": 500,
      "seconds": 0.03
    },
    {
      "status": 500,
      "seconds": 0.04
    },
    {
      "status": 500,
      "seconds": 0.03
    },
    {
      "status": 500,
      "seconds": 0.03
    }
  ],
  "request_log_lines": [
    "{\"timestamp\": \"2026-11-18T20:34:23.887+00:00\", \"request_id\": \"f3196f18c052\", \"pid\": 37046, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 19049.7, \"creator_id\": \"e4_before_20261118153156_t3_0\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:23.918+00:00\", \"request_id\": \"10dca73878bd\", \"pid\": 37046, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 29.9, \"creator_id\": \"e4_before_20261118153156_t3_1\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:23.956+00:00\", \"request_id\": \"96ffe9214276\", \"pid\": 37046, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 36.1, \"creator_id\": \"e4_before_20261118153156_t3_2\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:23.983+00:00\", \"request_id\": \"6b796e3c7381\", \"pid\": 37046, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 25.8, \"creator_id\": \"e4_before_20261118153156_t3_3\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:24.016+00:00\", \"request_id\": \"4ce324e55cd0\", \"pid\": 37046, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 32.2, \"creator_id\": \"e4_before_20261118153156_t3_4\", \"error\": null}",
    "{\"timestamp\": \"2026-11-18T20:34:24.018+00:00\", \"request_id\": \"d13579479dad\", \"pid\": 37046, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null}"
  ],
  "gunicorn_log_tail": [
    "         ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^",
    "  File \"/opt/homebrew/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pathlib/_local.py\", line 537, in open",
    "    return io.open(self, mode, buffering, encoding, errors, newline)",
    "           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
    "PermissionError: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_qrt0dj17/audit.jsonl'",
    "[2026-11-18 15:34:24 -0500] [37046] [INFO] Worker exiting (pid: 37046)",
    "[2026-11-18 15:34:24 -0500] [37045] [INFO] Handling signal: term",
    "[2026-11-18 15:34:24 -0500] [37045] [INFO] Shutting down: Master"
  ]
}
```

## E5

**Trial 1** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {37048: 1005.1}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {37048: 1005.1}",
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
    "peak_rss_mb": 1005.1,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T20:34:37.154 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.3,
      "mean": 28.7,
      "p50": 28.4,
      "p95": 35.3
    },
    "worker_pid": 37048,
    "worker_started_at": "2026-11-18T20:34:24.457+00:00"
  },
  "worker_rss_mb": {
    "37048": 1005.1
  }
}
```

**Trial 2** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {37059: 1010.2}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {37059: 1010.2}",
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
    "peak_rss_mb": 1010.2,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T20:34:42.743 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.6,
      "mean": 28.9,
      "p50": 28.2,
      "p95": 35.6
    },
    "worker_pid": 37059,
    "worker_started_at": "2026-11-18T20:34:38.252+00:00"
  },
  "worker_rss_mb": {
    "37059": 1010.2
  }
}
```

**Trial 3** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {37068: 1012.2}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {37068: 1012.2}",
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
    "peak_rss_mb": 1012.2,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T20:34:48.124 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.4,
      "mean": 28.8,
      "p50": 28.2,
      "p95": 35.4
    },
    "worker_pid": 37068,
    "worker_started_at": "2026-11-18T20:34:43.848+00:00"
  },
  "worker_rss_mb": {
    "37068": 1012.2
  }
}
```

## X1

**Trial 1** — sent 25; request log 25; client {'200': 17, '429': 3, '400': 5} vs /metrics {'200': 17, '400': 5, '429': 3}; flood .....x.....xx.. (12×200); worker RSS MB {37072: 1010.2, 37073: 929.9, 37074: 929.6}

```json
{
  "passed": false,
  "summary": "sent 25; request log 25; client {'200': 17, '429': 3, '400': 5} vs /metrics {'200': 17, '400': 5, '429': 3}; flood .....x.....xx.. (12\u00d7200); worker RSS MB {37072: 1010.2, 37073: 929.9, 37074: 929.6}",
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
    200,
    200
  ],
  "client_tally": {
    "200": 17,
    "429": 3,
    "400": 5
  },
  "metrics": {
    "by_path": {
      "/appeal": 2,
      "/submit": 23
    },
    "by_status": {
      "200": 17,
      "400": 5,
      "429": 3
    },
    "detector_loaded": true,
    "peak_rss_mb": 1010.2,
    "rate_limited": 3,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T20:34:54.005 00:00",
    "submit_latency_ms": {
      "count": 15,
      "max": 4902.2,
      "mean": 549.0,
      "p50": 26.0,
      "p95": 2973.7
    },
    "worker_pid": 37072,
    "worker_started_at": "2026-11-18T20:34:49.227+00:00"
  },
  "worker_rss_mb": {
    "37072": 1010.2,
    "37073": 929.9,
    "37074": 929.6
  }
}
```
