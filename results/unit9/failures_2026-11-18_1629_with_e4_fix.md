# Extension criteria — with_e4_fix

- Produced by: `run_failures.py::main`
- Run path: `./serve.sh` → `gunicorn -c gunicorn.conf.py app:app`
- 3 trials per criterion, each from a fresh start · 2026-11-18 16:29

| Criterion | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|
| E1 | met | met | met | MET |
| E2 | met | met | met | MET |
| E3 | met | met | met | MET |
| E4 | met | met | met | MET |
| E5 | met | met | met | MET |

---

## E1

**Trial 1** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.06s; slowest 22.42s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.06s; slowest 22.42s",
  "port_open_s": 0.06,
  "results": [
    {
      "status": 200,
      "seconds": 22.42
    },
    {
      "status": 200,
      "seconds": 21.41
    },
    {
      "status": 200,
      "seconds": 20.41
    },
    {
      "status": 200,
      "seconds": 19.41
    },
    {
      "status": 200,
      "seconds": 18.49
    },
    {
      "status": 200,
      "seconds": 17.49
    },
    {
      "status": 200,
      "seconds": 16.48
    },
    {
      "status": 200,
      "seconds": 15.49
    },
    {
      "status": 200,
      "seconds": 14.54
    },
    {
      "status": 200,
      "seconds": 13.56
    },
    {
      "status": 200,
      "seconds": 12.57
    },
    {
      "status": 200,
      "seconds": 11.55
    },
    {
      "status": 200,
      "seconds": 10.61
    },
    {
      "status": 200,
      "seconds": 9.62
    },
    {
      "status": 200,
      "seconds": 8.64
    },
    {
      "status": 200,
      "seconds": 7.64
    },
    {
      "status": 200,
      "seconds": 6.68
    },
    {
      "status": 200,
      "seconds": 5.69
    },
    {
      "status": 200,
      "seconds": 4.7
    },
    {
      "status": 200,
      "seconds": 3.71
    },
    {
      "status": 200,
      "seconds": 2.74
    },
    {
      "status": 200,
      "seconds": 1.75
    },
    {
      "status": 200,
      "seconds": 0.76
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
      "seconds": 0.05
    }
  ],
  "gunicorn_log_tail": [
    "[2026-11-18 16:27:06 -0500] [38387] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:27:06 -0500] [38387] [INFO] Listening at: http://127.0.0.1:5002 (38387)",
    "[2026-11-18 16:27:06 -0500] [38387] [INFO] Using worker: gthread",
    "[2026-11-18 16:27:06 -0500] [38390] [INFO] Booting worker with pid: 38390",
    "[2026-11-18 16:27:29 -0500] [38390] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 16:27:35 -0500] [38387] [INFO] Handling signal: term",
    "[2026-11-18 16:27:36 -0500] [38390] [INFO] Worker exiting (pid: 38390)",
    "[2026-11-18 16:27:37 -0500] [38387] [INFO] Shutting down: Master"
  ]
}
```

**Trial 2** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 17.75s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 17.75s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 17.75
    },
    {
      "status": 200,
      "seconds": 16.74
    },
    {
      "status": 200,
      "seconds": 15.75
    },
    {
      "status": 200,
      "seconds": 14.75
    },
    {
      "status": 200,
      "seconds": 13.82
    },
    {
      "status": 200,
      "seconds": 12.81
    },
    {
      "status": 200,
      "seconds": 11.82
    },
    {
      "status": 200,
      "seconds": 10.82
    },
    {
      "status": 200,
      "seconds": 9.88
    },
    {
      "status": 200,
      "seconds": 8.89
    },
    {
      "status": 200,
      "seconds": 7.89
    },
    {
      "status": 200,
      "seconds": 6.89
    },
    {
      "status": 200,
      "seconds": 5.96
    },
    {
      "status": 200,
      "seconds": 4.95
    },
    {
      "status": 200,
      "seconds": 3.96
    },
    {
      "status": 200,
      "seconds": 2.97
    },
    {
      "status": 200,
      "seconds": 2.01
    },
    {
      "status": 200,
      "seconds": 1.02
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
    "[2026-11-18 16:27:37 -0500] [38397] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:27:37 -0500] [38397] [INFO] Listening at: http://127.0.0.1:5002 (38397)",
    "[2026-11-18 16:27:37 -0500] [38397] [INFO] Using worker: gthread",
    "[2026-11-18 16:27:37 -0500] [38400] [INFO] Booting worker with pid: 38400",
    "[2026-11-18 16:27:55 -0500] [38400] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 16:28:06 -0500] [38397] [INFO] Handling signal: term",
    "[2026-11-18 16:28:07 -0500] [38400] [INFO] Worker exiting (pid: 38400)",
    "[2026-11-18 16:28:07 -0500] [38397] [INFO] Shutting down: Master"
  ]
}
```

**Trial 3** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 21.22s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 21.22s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 21.22
    },
    {
      "status": 200,
      "seconds": 20.22
    },
    {
      "status": 200,
      "seconds": 19.22
    },
    {
      "status": 200,
      "seconds": 18.22
    },
    {
      "status": 200,
      "seconds": 17.29
    },
    {
      "status": 200,
      "seconds": 16.29
    },
    {
      "status": 200,
      "seconds": 15.28
    },
    {
      "status": 200,
      "seconds": 14.29
    },
    {
      "status": 200,
      "seconds": 13.34
    },
    {
      "status": 200,
      "seconds": 12.36
    },
    {
      "status": 200,
      "seconds": 11.36
    },
    {
      "status": 200,
      "seconds": 10.36
    },
    {
      "status": 200,
      "seconds": 9.41
    },
    {
      "status": 200,
      "seconds": 8.43
    },
    {
      "status": 200,
      "seconds": 7.44
    },
    {
      "status": 200,
      "seconds": 6.44
    },
    {
      "status": 200,
      "seconds": 5.48
    },
    {
      "status": 200,
      "seconds": 4.5
    },
    {
      "status": 200,
      "seconds": 3.5
    },
    {
      "status": 200,
      "seconds": 2.51
    },
    {
      "status": 200,
      "seconds": 1.54
    },
    {
      "status": 200,
      "seconds": 0.55
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
      "seconds": 0.05
    },
    {
      "status": 200,
      "seconds": 0.06
    }
  ],
  "gunicorn_log_tail": [
    "[2026-11-18 16:28:07 -0500] [38414] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:28:07 -0500] [38414] [INFO] Listening at: http://127.0.0.1:5002 (38414)",
    "[2026-11-18 16:28:07 -0500] [38414] [INFO] Using worker: gthread",
    "[2026-11-18 16:28:07 -0500] [38417] [INFO] Booting worker with pid: 38417",
    "[2026-11-18 16:28:29 -0500] [38417] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 16:28:37 -0500] [38414] [INFO] Handling signal: term",
    "[2026-11-18 16:28:38 -0500] [38417] [INFO] Worker exiting (pid: 38417)",
    "[2026-11-18 16:28:38 -0500] [38414] [INFO] Shutting down: Master"
  ]
}
```

## E2

**Trial 1** — killed worker 38445; first 200 after 2.07s; new worker 38447; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 38445; first 200 after 2.07s; new worker 38447; gunicorn log mentions the dead worker: True",
  "recovery_s": 2.07,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 2.07,
      "at_s": 2.07
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 16:28:38 -0500] [38445] [INFO] Booting worker with pid: 38445",
    "[2026-11-18 16:28:41 -0500] [38445] [INFO] detector loaded: gpt2",
    "[2026-11-18 16:28:41 -0500] [38439] [ERROR] Worker (pid:38445) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 16:28:41 -0500] [38447] [INFO] Booting worker with pid: 38447"
  ]
}
```

**Trial 2** — killed worker 38456; first 200 after 1.99s; new worker 38462; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 38456; first 200 after 1.99s; new worker 38462; gunicorn log mentions the dead worker: True",
  "recovery_s": 1.99,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 1.99,
      "at_s": 1.99
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 16:28:43 -0500] [38456] [INFO] Booting worker with pid: 38456",
    "[2026-11-18 16:28:45 -0500] [38456] [INFO] detector loaded: gpt2",
    "[2026-11-18 16:28:45 -0500] [38453] [ERROR] Worker (pid:38456) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 16:28:45 -0500] [38462] [INFO] Booting worker with pid: 38462"
  ]
}
```

**Trial 3** — killed worker 38470; first 200 after 1.94s; new worker 38471; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 38470; first 200 after 1.94s; new worker 38471; gunicorn log mentions the dead worker: True",
  "recovery_s": 1.94,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 1.94,
      "at_s": 1.94
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 16:28:48 -0500] [38470] [INFO] Booting worker with pid: 38470",
    "[2026-11-18 16:28:50 -0500] [38470] [INFO] detector loaded: gpt2",
    "[2026-11-18 16:28:50 -0500] [38467] [ERROR] Worker (pid:38470) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 16:28:50 -0500] [38471] [INFO] Booting worker with pid: 38471"
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
    "[2026-11-18 16:28:52 -0500] [38476] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:28:52 -0500] [38476] [INFO] Listening at: http://127.0.0.1:5002 (38476)",
    "[2026-11-18 16:28:52 -0500] [38476] [INFO] Using worker: gthread",
    "[2026-11-18 16:28:52 -0500] [38479] [INFO] Booting worker with pid: 38479",
    "[2026-11-18 16:28:53 -0500] [38479] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 16:28:53 -0500] [38479] [INFO] Worker exiting (pid: 38479)",
    "[2026-11-18 16:28:53 -0500] [38476] [INFO] Handling signal: term",
    "[2026-11-18 16:28:54 -0500] [38476] [INFO] Shutting down: Master"
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
    "[2026-11-18 16:28:54 -0500] [38480] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:28:54 -0500] [38480] [INFO] Listening at: http://127.0.0.1:5002 (38480)",
    "[2026-11-18 16:28:54 -0500] [38480] [INFO] Using worker: gthread",
    "[2026-11-18 16:28:54 -0500] [38483] [INFO] Booting worker with pid: 38483",
    "[2026-11-18 16:28:55 -0500] [38483] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 16:28:55 -0500] [38483] [INFO] Worker exiting (pid: 38483)",
    "[2026-11-18 16:28:55 -0500] [38480] [INFO] Handling signal: term",
    "[2026-11-18 16:28:55 -0500] [38480] [INFO] Shutting down: Master"
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
    "[2026-11-18 16:28:55 -0500] [38484] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 16:28:55 -0500] [38484] [INFO] Listening at: http://127.0.0.1:5002 (38484)",
    "[2026-11-18 16:28:55 -0500] [38484] [INFO] Using worker: gthread",
    "[2026-11-18 16:28:55 -0500] [38487] [INFO] Booting worker with pid: 38487",
    "[2026-11-18 16:28:57 -0500] [38487] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 16:28:57 -0500] [38487] [INFO] Worker exiting (pid: 38487)",
    "[2026-11-18 16:28:57 -0500] [38484] [INFO] Handling signal: term",
    "[2026-11-18 16:28:57 -0500] [38484] [INFO] Shutting down: Master"
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
      "seconds": 1.99,
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
    "{\"timestamp\": \"2026-11-18T21:28:59.517+00:00\", \"request_id\": \"6f8f65cdfd76\", \"pid\": 38495, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 98.4, \"creator_id\": \"e4_with_e4_fix_20261118162706_t1_0\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 106, \"text_chars\": 552}, \"out\": null, \"stages_ms\": {\"checks\": 0.04, \"signal_one\": 97.03, \"signal_two\": 0.28, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:28:59.549+00:00\", \"request_id\": \"4de36afd8f36\", \"pid\": 38495, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 29.4, \"creator_id\": \"e4_with_e4_fix_20261118162706_t1_1\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 92, \"text_chars\": 685}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 28.74, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:28:59.585+00:00\", \"request_id\": \"eff90760d8fa\", \"pid\": 38495, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 34.8, \"creator_id\": \"e4_with_e4_fix_20261118162706_t1_2\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 119, \"text_chars\": 704}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 34.19, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:28:59.612+00:00\", \"request_id\": \"1598eec725d0\", \"pid\": 38495, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 25.4, \"creator_id\": \"e4_with_e4_fix_20261118162706_t1_3\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 84, \"text_chars\": 392}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 24.77, \"signal_two\": 0.15, \"combine_label\": 0.02}}",
    "{\"timestamp\": \"2026-11-18T21:28:59.644+00:00\", \"request_id\": \"42a627c0cc23\", \"pid\": 38495, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 31.5, \"creator_id\": \"e4_with_e4_fix_20261118162706_t1_4\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 109, \"text_chars\": 588}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 30.86, \"signal_two\": 0.18, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:28:59.646+00:00\", \"request_id\": \"33dafbcfd51c\", \"pid\": 38495, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null, \"in\": null, \"out\": null, \"stages_ms\": null}"
  ],
  "gunicorn_log_tail": [
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_xbub9exq/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_xbub9exq/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_xbub9exq/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_xbub9exq/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_xbub9exq/audit.jsonl'",
    "[2026-11-18 16:28:59 -0500] [38492] [INFO] Handling signal: term",
    "[2026-11-18 16:28:59 -0500] [38495] [INFO] Worker exiting (pid: 38495)",
    "[2026-11-18 16:28:59 -0500] [38492] [INFO] Shutting down: Master"
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
      "seconds": 1.88,
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
    "{\"timestamp\": \"2026-11-18T21:29:01.987+00:00\", \"request_id\": \"2d8fc4964125\", \"pid\": 38499, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 89.7, \"creator_id\": \"e4_with_e4_fix_20261118162706_t2_0\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 106, \"text_chars\": 552}, \"out\": null, \"stages_ms\": {\"checks\": 0.03, \"signal_one\": 88.75, \"signal_two\": 0.29, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:29:02.018+00:00\", \"request_id\": \"8fb845e154c4\", \"pid\": 38499, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 29.4, \"creator_id\": \"e4_with_e4_fix_20261118162706_t2_1\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 92, \"text_chars\": 685}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 28.81, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:29:02.055+00:00\", \"request_id\": \"8bf815adccd2\", \"pid\": 38499, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 35.0, \"creator_id\": \"e4_with_e4_fix_20261118162706_t2_2\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 119, \"text_chars\": 704}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 34.39, \"signal_two\": 0.17, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:29:02.081+00:00\", \"request_id\": \"c92b7467cdc7\", \"pid\": 38499, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 25.2, \"creator_id\": \"e4_with_e4_fix_20261118162706_t2_3\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 84, \"text_chars\": 392}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 24.59, \"signal_two\": 0.15, \"combine_label\": 0.02}}",
    "{\"timestamp\": \"2026-11-18T21:29:02.114+00:00\", \"request_id\": \"31ee2634c45d\", \"pid\": 38499, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 31.6, \"creator_id\": \"e4_with_e4_fix_20261118162706_t2_4\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 109, \"text_chars\": 588}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 30.91, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:29:02.116+00:00\", \"request_id\": \"7135f5f7402c\", \"pid\": 38499, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null, \"in\": null, \"out\": null, \"stages_ms\": null}"
  ],
  "gunicorn_log_tail": [
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_0w861_6c/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_0w861_6c/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_0w861_6c/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_0w861_6c/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_0w861_6c/audit.jsonl'",
    "[2026-11-18 16:29:02 -0500] [38496] [INFO] Handling signal: term",
    "[2026-11-18 16:29:02 -0500] [38499] [INFO] Worker exiting (pid: 38499)",
    "[2026-11-18 16:29:02 -0500] [38496] [INFO] Shutting down: Master"
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
      "seconds": 1.89,
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
    "{\"timestamp\": \"2026-11-18T21:29:04.467+00:00\", \"request_id\": \"877d5a14a581\", \"pid\": 38507, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 88.6, \"creator_id\": \"e4_with_e4_fix_20261118162706_t3_0\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 106, \"text_chars\": 552}, \"out\": null, \"stages_ms\": {\"checks\": 0.03, \"signal_one\": 87.67, \"signal_two\": 0.29, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:29:04.498+00:00\", \"request_id\": \"7af933ec56df\", \"pid\": 38507, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 29.3, \"creator_id\": \"e4_with_e4_fix_20261118162706_t3_1\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 92, \"text_chars\": 685}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 28.66, \"signal_two\": 0.17, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:29:04.535+00:00\", \"request_id\": \"2a85d9d99fef\", \"pid\": 38507, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 35.6, \"creator_id\": \"e4_with_e4_fix_20261118162706_t3_2\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 119, \"text_chars\": 704}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 34.95, \"signal_two\": 0.17, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T21:29:04.562+00:00\", \"request_id\": \"4d28dc15fec2\", \"pid\": 38507, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 25.2, \"creator_id\": \"e4_with_e4_fix_20261118162706_t3_3\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 84, \"text_chars\": 392}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 24.6, \"signal_two\": 0.15, \"combine_label\": 0.02}}",
    "{\"timestamp\": \"2026-11-18T21:29:04.595+00:00\", \"request_id\": \"23a719f94780\", \"pid\": 38507, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 31.6, \"creator_id\": \"e4_with_e4_fix_20261118162706_t3_4\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 109, \"text_chars\": 588}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 30.97, \"signal_two\": 0.19, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T21:29:04.596+00:00\", \"request_id\": \"723b432e6b74\", \"pid\": 38507, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null, \"in\": null, \"out\": null, \"stages_ms\": null}"
  ],
  "gunicorn_log_tail": [
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_qbrl6ypn/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_qbrl6ypn/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_qbrl6ypn/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_qbrl6ypn/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_qbrl6ypn/audit.jsonl'",
    "[2026-11-18 16:29:04 -0500] [38504] [INFO] Handling signal: term",
    "[2026-11-18 16:29:04 -0500] [38507] [INFO] Worker exiting (pid: 38507)",
    "[2026-11-18 16:29:04 -0500] [38504] [INFO] Shutting down: Master"
  ]
}
```

## E5

**Trial 1** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {38511: 1012.4}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {38511: 1012.4}",
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
    "peak_rss_mb": 1012.4,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T21:29:07.341 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.5,
      "mean": 29.0,
      "p50": 28.4,
      "p95": 35.5
    },
    "worker_pid": 38511,
    "worker_started_at": "2026-11-18T21:29:05.046+00:00"
  },
  "worker_rss_mb": {
    "38511": 1012.4
  }
}
```

**Trial 2** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {38521: 1009.0}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {38521: 1009.0}",
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
    "peak_rss_mb": 1009.0,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T21:29:11.549 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.3,
      "mean": 29.2,
      "p50": 29.2,
      "p95": 35.3
    },
    "worker_pid": 38521,
    "worker_started_at": "2026-11-18T21:29:09.487+00:00"
  },
  "worker_rss_mb": {
    "38521": 1009.0
  }
}
```

**Trial 3** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {38527: 1009.9}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {38527: 1009.9}",
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
    "peak_rss_mb": 1009.9,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T21:29:16.087 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.8,
      "mean": 29.3,
      "p50": 29.7,
      "p95": 35.8
    },
    "worker_pid": 38527,
    "worker_started_at": "2026-11-18T21:29:13.734+00:00"
  },
  "worker_rss_mb": {
    "38527": 1009.9
  }
}
```
