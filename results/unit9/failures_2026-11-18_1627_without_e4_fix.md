# Extension criteria — without_e4_fix

- Produced by: `run_failures.py::main`
- Run path: `./serve.sh` → `gunicorn -c gunicorn.conf.py app:app`
- 3 trials per criterion, each from a fresh start · 2026-11-18 16:27

| Criterion | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|
| E1 | met | met | met | MET |
| E2 | met | met | met | MET |
| E3 | met | met | met | MET |
| E4 | **missed** | **missed** | **missed** | MISSED |
| E5 | met | met | met | MET |

---

## E1

**Trial 1** — 30/30 → 200; 5xx 0; dropped 0; port open after 1.79s; slowest 3.77s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 1.79s; slowest 3.77s",
  "port_open_s": 1.79,
  "results": [
    {
      "status": 200,
      "seconds": 3.77
    },
    {
      "status": 200,
      "seconds": 2.76
    },
    {
      "status": 200,
      "seconds": 1.76
    },
    {
      "status": 200,
      "seconds": 0.76
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
      "seconds": 0.04
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
    "[2026-11-18 16:21:49 -0500] [38223] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:21:49 -0500] [38223] [INFO] Listening at: http://127.0.0.1:5002 (38223)",
    "[2026-11-18 16:21:49 -0500] [38223] [INFO] Using worker: gthread",
    "[2026-11-18 16:21:49 -0500] [38226] [INFO] Booting worker with pid: 38226",
    "[2026-11-18 16:21:53 -0500] [38226] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 16:22:18 -0500] [38223] [INFO] Handling signal: term",
    "[2026-11-18 16:22:19 -0500] [38226] [INFO] Worker exiting (pid: 38226)",
    "[2026-11-18 16:22:20 -0500] [38223] [INFO] Shutting down: Master"
  ]
}
```

**Trial 2** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 1.98s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 1.98s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 1.98
    },
    {
      "status": 200,
      "seconds": 0.97
    },
    {
      "status": 200,
      "seconds": 0.04
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
      "seconds": 0.04
    },
    {
      "status": 200,
      "seconds": 0.03
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
    "[2026-11-18 16:22:20 -0500] [38227] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:22:20 -0500] [38227] [INFO] Listening at: http://127.0.0.1:5002 (38227)",
    "[2026-11-18 16:22:20 -0500] [38227] [INFO] Using worker: gthread",
    "[2026-11-18 16:22:20 -0500] [38230] [INFO] Booting worker with pid: 38230",
    "[2026-11-18 16:22:22 -0500] [38230] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 16:22:49 -0500] [38227] [INFO] Handling signal: term",
    "[2026-11-18 16:22:50 -0500] [38230] [INFO] Worker exiting (pid: 38230)",
    "[2026-11-18 16:22:50 -0500] [38227] [INFO] Shutting down: Master"
  ]
}
```

**Trial 3** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 2.07s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 2.07s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 2.07
    },
    {
      "status": 200,
      "seconds": 1.06
    },
    {
      "status": 200,
      "seconds": 0.07
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
      "seconds": 0.04
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
    "[2026-11-18 16:22:50 -0500] [38268] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:22:50 -0500] [38268] [INFO] Listening at: http://127.0.0.1:5002 (38268)",
    "[2026-11-18 16:22:50 -0500] [38268] [INFO] Using worker: gthread",
    "[2026-11-18 16:22:50 -0500] [38271] [INFO] Booting worker with pid: 38271",
    "[2026-11-18 16:22:52 -0500] [38271] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 16:23:19 -0500] [38268] [INFO] Handling signal: term",
    "[2026-11-18 16:23:20 -0500] [38271] [INFO] Worker exiting (pid: 38271)",
    "[2026-11-18 16:23:21 -0500] [38268] [INFO] Shutting down: Master"
  ]
}
```

## E2

**Trial 1** — killed worker 38276; first 200 after 8.1s; new worker 38277; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 38276; first 200 after 8.1s; new worker 38277; gunicorn log mentions the dead worker: True",
  "recovery_s": 8.1,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 8.1,
      "at_s": 8.1
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 16:23:21 -0500] [38276] [INFO] Booting worker with pid: 38276",
    "[2026-11-18 16:23:23 -0500] [38276] [INFO] detector loaded: gpt2",
    "[2026-11-18 16:23:23 -0500] [38273] [ERROR] Worker (pid:38276) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 16:23:23 -0500] [38277] [INFO] Booting worker with pid: 38277"
  ]
}
```

**Trial 2** — killed worker 38283; first 200 after 24.37s; new worker 38290; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 38283; first 200 after 24.37s; new worker 38290; gunicorn log mentions the dead worker: True",
  "recovery_s": 24.37,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 24.37,
      "at_s": 24.37
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 16:23:31 -0500] [38283] [INFO] Booting worker with pid: 38283",
    "[2026-11-18 16:23:42 -0500] [38283] [INFO] detector loaded: gpt2",
    "[2026-11-18 16:23:43 -0500] [38280] [ERROR] Worker (pid:38283) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 16:23:43 -0500] [38290] [INFO] Booting worker with pid: 38290"
  ]
}
```

**Trial 3** — killed worker 38296; first 200 after 19.41s; new worker 38298; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 38296; first 200 after 19.41s; new worker 38298; gunicorn log mentions the dead worker: True",
  "recovery_s": 19.41,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 19.41,
      "at_s": 19.41
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 16:24:07 -0500] [38296] [INFO] Booting worker with pid: 38296",
    "[2026-11-18 16:24:29 -0500] [38296] [INFO] detector loaded: gpt2",
    "[2026-11-18 16:24:30 -0500] [38293] [ERROR] Worker (pid:38296) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 16:24:30 -0500] [38298] [INFO] Booting worker with pid: 38298"
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
    "log_entries": 1145,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 16:24:49 -0500] [38305] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:24:49 -0500] [38305] [INFO] Listening at: http://127.0.0.1:5002 (38305)",
    "[2026-11-18 16:24:49 -0500] [38305] [INFO] Using worker: gthread",
    "[2026-11-18 16:24:49 -0500] [38308] [INFO] Booting worker with pid: 38308",
    "[2026-11-18 16:24:51 -0500] [38308] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 16:24:51 -0500] [38308] [INFO] Worker exiting (pid: 38308)",
    "[2026-11-18 16:24:51 -0500] [38305] [INFO] Handling signal: term",
    "[2026-11-18 16:24:51 -0500] [38305] [INFO] Shutting down: Master"
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
    "log_entries": 1150,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 16:24:51 -0500] [38309] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:24:51 -0500] [38309] [INFO] Listening at: http://127.0.0.1:5002 (38309)",
    "[2026-11-18 16:24:51 -0500] [38309] [INFO] Using worker: gthread",
    "[2026-11-18 16:24:51 -0500] [38312] [INFO] Booting worker with pid: 38312",
    "[2026-11-18 16:24:52 -0500] [38312] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 16:24:52 -0500] [38309] [INFO] Handling signal: term",
    "[2026-11-18 16:24:52 -0500] [38312] [INFO] Worker exiting (pid: 38312)",
    "[2026-11-18 16:24:52 -0500] [38309] [INFO] Shutting down: Master"
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
    "log_entries": 1155,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 16:24:53 -0500] [38313] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:24:53 -0500] [38313] [INFO] Listening at: http://127.0.0.1:5002 (38313)",
    "[2026-11-18 16:24:53 -0500] [38313] [INFO] Using worker: gthread",
    "[2026-11-18 16:24:53 -0500] [38316] [INFO] Booting worker with pid: 38316",
    "[2026-11-18 16:24:54 -0500] [38316] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 16:24:54 -0500] [38313] [INFO] Handling signal: term",
    "[2026-11-18 16:24:54 -0500] [38316] [INFO] Worker exiting (pid: 38316)",
    "[2026-11-18 16:24:54 -0500] [38313] [INFO] Shutting down: Master"
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
      "seconds": 21.57,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.03,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.04,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.03,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.03,
      "error": "internal_error"
    }
  ],
  "request_log_lines": [
    "{\"timestamp\": \"2026-11-18T21:25:16.246+00:00\", \"request_id\": \"497a0715f89c\", \"pid\": 38320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 102.8, \"creator_id\": \"e4_without_e4_fix_20261118162147_t1_0\", \"error\": \"internal_error\", \"in\": {\"text_words\": 106, \"text_chars\": 552}, \"out\": null, \"stages_ms\": {\"checks\": 0.07, \"signal_one\": 98.49, \"signal_two\": 0.29, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:25:16.277+00:00\", \"request_id\": \"5feb80dfbbf8\", \"pid\": 38320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 29.7, \"creator_id\": \"e4_without_e4_fix_20261118162147_t1_1\", \"error\": \"internal_error\", \"in\": {\"text_words\": 92, \"text_chars\": 685}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 28.4, \"signal_two\": 0.17, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:25:16.315+00:00\", \"request_id\": \"bf2f00a5c76a\", \"pid\": 38320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 36.6, \"creator_id\": \"e4_without_e4_fix_20261118162147_t1_2\", \"error\": \"internal_error\", \"in\": {\"text_words\": 119, \"text_chars\": 704}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 35.25, \"signal_two\": 0.17, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:25:16.343+00:00\", \"request_id\": \"9f40ebf23687\", \"pid\": 38320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 26.0, \"creator_id\": \"e4_without_e4_fix_20261118162147_t1_3\", \"error\": \"internal_error\", \"in\": {\"text_words\": 84, \"text_chars\": 392}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 24.69, \"signal_two\": 0.15, \"combine_label\": 0.02}}",
    "{\"timestamp\": \"2026-11-18T21:25:16.376+00:00\", \"request_id\": \"304dc2899594\", \"pid\": 38320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 32.3, \"creator_id\": \"e4_without_e4_fix_20261118162147_t1_4\", \"error\": \"internal_error\", \"in\": {\"text_words\": 109, \"text_chars\": 588}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 31.05, \"signal_two\": 0.18, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:25:16.378+00:00\", \"request_id\": \"622d9294a9e5\", \"pid\": 38320, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null, \"in\": null, \"out\": null, \"stages_ms\": null}"
  ],
  "gunicorn_log_tail": [
    "         ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^",
    "  File \"/opt/homebrew/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pathlib/_local.py\", line 537, in open",
    "    return io.open(self, mode, buffering, encoding, errors, newline)",
    "           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
    "PermissionError: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_9648hwvr/audit.jsonl'",
    "[2026-11-18 16:25:16 -0500] [38320] [INFO] Worker exiting (pid: 38320)",
    "[2026-11-18 16:25:16 -0500] [38317] [INFO] Handling signal: term",
    "[2026-11-18 16:25:16 -0500] [38317] [INFO] Shutting down: Master"
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
      "seconds": 18.52,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.03,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.04,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.03,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.03,
      "error": "internal_error"
    }
  ],
  "request_log_lines": [
    "{\"timestamp\": \"2026-11-18T21:25:35.362+00:00\", \"request_id\": \"d9578a719d58\", \"pid\": 38326, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 101.0, \"creator_id\": \"e4_without_e4_fix_20261118162147_t2_0\", \"error\": \"internal_error\", \"in\": {\"text_words\": 106, \"text_chars\": 552}, \"out\": null, \"stages_ms\": {\"checks\": 0.04, \"signal_one\": 98.41, \"signal_two\": 0.28, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:25:35.393+00:00\", \"request_id\": \"030c3a6c7bd8\", \"pid\": 38326, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 30.1, \"creator_id\": \"e4_without_e4_fix_20261118162147_t2_1\", \"error\": \"internal_error\", \"in\": {\"text_words\": 92, \"text_chars\": 685}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 28.7, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:25:35.430+00:00\", \"request_id\": \"cdd96e7bde49\", \"pid\": 38326, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 35.2, \"creator_id\": \"e4_without_e4_fix_20261118162147_t2_2\", \"error\": \"internal_error\", \"in\": {\"text_words\": 119, \"text_chars\": 704}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 33.96, \"signal_two\": 0.17, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:25:35.458+00:00\", \"request_id\": \"7d606337c7b9\", \"pid\": 38326, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 26.2, \"creator_id\": \"e4_without_e4_fix_20261118162147_t2_3\", \"error\": \"internal_error\", \"in\": {\"text_words\": 84, \"text_chars\": 392}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 24.89, \"signal_two\": 0.14, \"combine_label\": 0.02}}",
    "{\"timestamp\": \"2026-11-18T21:25:35.491+00:00\", \"request_id\": \"6e8dae502f48\", \"pid\": 38326, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 32.2, \"creator_id\": \"e4_without_e4_fix_20261118162147_t2_4\", \"error\": \"internal_error\", \"in\": {\"text_words\": 109, \"text_chars\": 588}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 30.95, \"signal_two\": 0.18, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:25:35.493+00:00\", \"request_id\": \"693e22bc4f7b\", \"pid\": 38326, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null, \"in\": null, \"out\": null, \"stages_ms\": null}"
  ],
  "gunicorn_log_tail": [
    "         ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^",
    "  File \"/opt/homebrew/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pathlib/_local.py\", line 537, in open",
    "    return io.open(self, mode, buffering, encoding, errors, newline)",
    "           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
    "PermissionError: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_u86407eb/audit.jsonl'",
    "[2026-11-18 16:25:35 -0500] [38323] [INFO] Handling signal: term",
    "[2026-11-18 16:25:35 -0500] [38326] [INFO] Worker exiting (pid: 38326)",
    "[2026-11-18 16:25:35 -0500] [38323] [INFO] Shutting down: Master"
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
      "seconds": 23.25,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.03,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.04,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.03,
      "error": "internal_error"
    },
    {
      "status": 500,
      "seconds": 0.03,
      "error": "internal_error"
    }
  ],
  "request_log_lines": [
    "{\"timestamp\": \"2026-11-18T21:25:59.202+00:00\", \"request_id\": \"d812026227f2\", \"pid\": 38332, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 103.2, \"creator_id\": \"e4_without_e4_fix_20261118162147_t3_0\", \"error\": \"internal_error\", \"in\": {\"text_words\": 106, \"text_chars\": 552}, \"out\": null, \"stages_ms\": {\"checks\": 0.07, \"signal_one\": 100.37, \"signal_two\": 0.28, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:25:59.234+00:00\", \"request_id\": \"e76a28e5d92e\", \"pid\": 38332, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 30.5, \"creator_id\": \"e4_without_e4_fix_20261118162147_t3_1\", \"error\": \"internal_error\", \"in\": {\"text_words\": 92, \"text_chars\": 685}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 29.21, \"signal_two\": 0.17, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:25:59.272+00:00\", \"request_id\": \"5fc56fd0a110\", \"pid\": 38332, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 37.0, \"creator_id\": \"e4_without_e4_fix_20261118162147_t3_2\", \"error\": \"internal_error\", \"in\": {\"text_words\": 119, \"text_chars\": 704}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 35.61, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:25:59.300+00:00\", \"request_id\": \"4ecb5062940d\", \"pid\": 38332, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 26.5, \"creator_id\": \"e4_without_e4_fix_20261118162147_t3_3\", \"error\": \"internal_error\", \"in\": {\"text_words\": 84, \"text_chars\": 392}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 25.2, \"signal_two\": 0.15, \"combine_label\": 0.02}}",
    "{\"timestamp\": \"2026-11-18T21:25:59.334+00:00\", \"request_id\": \"8f23a99c31fe\", \"pid\": 38332, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 500, \"latency_ms\": 32.4, \"creator_id\": \"e4_without_e4_fix_20261118162147_t3_4\", \"error\": \"internal_error\", \"in\": {\"text_words\": 109, \"text_chars\": 588}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 31.07, \"signal_two\": 0.19, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:25:59.335+00:00\", \"request_id\": \"dc5f5f4c0da4\", \"pid\": 38332, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null, \"in\": null, \"out\": null, \"stages_ms\": null}"
  ],
  "gunicorn_log_tail": [
    "         ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^",
    "  File \"/opt/homebrew/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pathlib/_local.py\", line 537, in open",
    "    return io.open(self, mode, buffering, encoding, errors, newline)",
    "           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
    "PermissionError: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_3ommxnyp/audit.jsonl'",
    "[2026-11-18 16:25:59 -0500] [38332] [INFO] Worker exiting (pid: 38332)",
    "[2026-11-18 16:25:59 -0500] [38329] [INFO] Handling signal: term",
    "[2026-11-18 16:25:59 -0500] [38329] [INFO] Shutting down: Master"
  ]
}
```

## E5

**Trial 1** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {38341: 1007.6}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {38341: 1007.6}",
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
    "peak_rss_mb": 1007.6,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T21:26:20.339 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.8,
      "mean": 28.9,
      "p50": 28.5,
      "p95": 35.8
    },
    "worker_pid": 38341,
    "worker_started_at": "2026-11-18T21:25:59.786+00:00"
  },
  "worker_rss_mb": {
    "38341": 1007.6
  }
}
```

**Trial 2** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {38347: 1007.0}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {38347: 1007.0}",
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
    "peak_rss_mb": 1007.0,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T21:26:46.093 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 37.1,
      "mean": 29.2,
      "p50": 28.7,
      "p95": 37.1
    },
    "worker_pid": 38347,
    "worker_started_at": "2026-11-18T21:26:22.358+00:00"
  },
  "worker_rss_mb": {
    "38347": 1007.0
  }
}
```

**Trial 3** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {38382: 1011.8}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {38382: 1011.8}",
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
    "peak_rss_mb": 1011.8,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T21:27:04.747 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.8,
      "mean": 29.0,
      "p50": 28.4,
      "p95": 35.8
    },
    "worker_pid": 38382,
    "worker_started_at": "2026-11-18T21:26:48.237+00:00"
  },
  "worker_rss_mb": {
    "38382": 1011.8
  }
}
```
