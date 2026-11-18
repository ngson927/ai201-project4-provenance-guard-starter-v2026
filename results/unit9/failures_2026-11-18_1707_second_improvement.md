# Extension criteria — second_improvement

- Produced by: `run_failures.py::main`
- Run path: `./serve.sh` → `gunicorn -c gunicorn.conf.py app:app`
- 3 trials per criterion, each from a fresh start · 2026-11-18 17:07

| Criterion | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|
| E1 | met | met | met | MET |
| E2 | met | met | met | MET |
| E3 | met | met | met | MET |
| E4 | met | met | met | MET |
| E5 | met | met | met | MET |

---

## E1

**Trial 1** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 5.35s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 5.35s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 5.35
    },
    {
      "status": 200,
      "seconds": 4.34
    },
    {
      "status": 200,
      "seconds": 3.34
    },
    {
      "status": 200,
      "seconds": 2.34
    },
    {
      "status": 200,
      "seconds": 1.39
    },
    {
      "status": 200,
      "seconds": 0.39
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
      "seconds": 0.07
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
    "[2026-11-18 17:04:53 -0500] [40224] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 17:04:53 -0500] [40224] [INFO] Listening at: http://127.0.0.1:5002 (40224)",
    "[2026-11-18 17:04:53 -0500] [40224] [INFO] Using worker: gthread",
    "[2026-11-18 17:04:53 -0500] [40227] [INFO] Booting worker with pid: 40227",
    "[2026-11-18 17:04:53 -0500] [40227] [INFO] loading the detector model (gpt2); on a machine that has never downloaded it this fetches ~550 MB and takes minutes",
    "[2026-11-18 17:04:57 -0500] [40227] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 17:04:58 -0500] [40227] [INFO] detector warmed with one scoring pass in 573 ms",
    "[2026-11-18 17:05:22 -0500] [40224] [INFO] Handling signal: term",
    "[2026-11-18 17:05:23 -0500] [40227] [INFO] Worker exiting (pid: 40227)",
    "[2026-11-18 17:05:23 -0500] [40224] [INFO] Shutting down: Master"
  ]
}
```

**Trial 2** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 6.28s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 6.28s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 6.28
    },
    {
      "status": 200,
      "seconds": 5.27
    },
    {
      "status": 200,
      "seconds": 4.27
    },
    {
      "status": 200,
      "seconds": 3.27
    },
    {
      "status": 200,
      "seconds": 2.33
    },
    {
      "status": 200,
      "seconds": 1.33
    },
    {
      "status": 200,
      "seconds": 0.33
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
    "[2026-11-18 17:05:23 -0500] [40230] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 17:05:23 -0500] [40230] [INFO] Listening at: http://127.0.0.1:5002 (40230)",
    "[2026-11-18 17:05:23 -0500] [40230] [INFO] Using worker: gthread",
    "[2026-11-18 17:05:23 -0500] [40233] [INFO] Booting worker with pid: 40233",
    "[2026-11-18 17:05:23 -0500] [40233] [INFO] loading the detector model (gpt2); on a machine that has never downloaded it this fetches ~550 MB and takes minutes",
    "[2026-11-18 17:05:29 -0500] [40233] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 17:05:29 -0500] [40233] [INFO] detector warmed with one scoring pass in 66 ms",
    "[2026-11-18 17:05:52 -0500] [40230] [INFO] Handling signal: term",
    "[2026-11-18 17:05:53 -0500] [40233] [INFO] Worker exiting (pid: 40233)",
    "[2026-11-18 17:05:54 -0500] [40230] [INFO] Shutting down: Master"
  ]
}
```

**Trial 3** — 30/30 → 200; 5xx 0; dropped 0; port open after 0.11s; slowest 4.72s

```json
{
  "passed": true,
  "summary": "30/30 \u2192 200; 5xx 0; dropped 0; port open after 0.11s; slowest 4.72s",
  "port_open_s": 0.11,
  "results": [
    {
      "status": 200,
      "seconds": 4.72
    },
    {
      "status": 200,
      "seconds": 3.71
    },
    {
      "status": 200,
      "seconds": 2.73
    },
    {
      "status": 200,
      "seconds": 1.71
    },
    {
      "status": 200,
      "seconds": 0.75
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
    "[2026-11-18 17:05:54 -0500] [40241] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 17:05:54 -0500] [40241] [INFO] Listening at: http://127.0.0.1:5002 (40241)",
    "[2026-11-18 17:05:54 -0500] [40241] [INFO] Using worker: gthread",
    "[2026-11-18 17:05:54 -0500] [40244] [INFO] Booting worker with pid: 40244",
    "[2026-11-18 17:05:54 -0500] [40244] [INFO] loading the detector model (gpt2); on a machine that has never downloaded it this fetches ~550 MB and takes minutes",
    "[2026-11-18 17:05:58 -0500] [40244] [INFO] detector loaded: gpt2",
    "`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.",
    "[2026-11-18 17:05:58 -0500] [40244] [INFO] detector warmed with one scoring pass in 61 ms",
    "[2026-11-18 17:06:23 -0500] [40241] [INFO] Handling signal: term",
    "[2026-11-18 17:06:24 -0500] [40244] [INFO] Worker exiting (pid: 40244)",
    "[2026-11-18 17:06:24 -0500] [40241] [INFO] Shutting down: Master"
  ]
}
```

## E2

**Trial 1** — killed worker 40249; first 200 after 5.38s; new worker 40253; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 40249; first 200 after 5.38s; new worker 40253; gunicorn log mentions the dead worker: True",
  "recovery_s": 5.38,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 5.38,
      "at_s": 5.38
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 17:06:24 -0500] [40249] [INFO] Booting worker with pid: 40249",
    "[2026-11-18 17:06:24 -0500] [40249] [INFO] loading the detector model (gpt2); on a machine that has never downloaded it this fetches ~550 MB and takes minutes",
    "[2026-11-18 17:06:33 -0500] [40249] [INFO] detector loaded: gpt2",
    "[2026-11-18 17:06:33 -0500] [40249] [INFO] detector warmed with one scoring pass in 64 ms",
    "[2026-11-18 17:06:34 -0500] [40246] [ERROR] Worker (pid:40249) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 17:06:34 -0500] [40253] [INFO] Booting worker with pid: 40253"
  ]
}
```

**Trial 2** — killed worker 40257; first 200 after 5.22s; new worker 40271; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 40257; first 200 after 5.22s; new worker 40271; gunicorn log mentions the dead worker: True",
  "recovery_s": 5.22,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 5.22,
      "at_s": 5.22
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 17:06:39 -0500] [40257] [INFO] Booting worker with pid: 40257",
    "[2026-11-18 17:06:39 -0500] [40257] [INFO] loading the detector model (gpt2); on a machine that has never downloaded it this fetches ~550 MB and takes minutes",
    "[2026-11-18 17:06:46 -0500] [40257] [INFO] detector loaded: gpt2",
    "[2026-11-18 17:06:46 -0500] [40257] [INFO] detector warmed with one scoring pass in 60 ms",
    "[2026-11-18 17:06:46 -0500] [40254] [ERROR] Worker (pid:40257) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 17:06:46 -0500] [40271] [INFO] Booting worker with pid: 40271"
  ]
}
```

**Trial 3** — killed worker 40276; first 200 after 5.78s; new worker 40278; gunicorn log mentions the dead worker: True

```json
{
  "passed": true,
  "summary": "killed worker 40276; first 200 after 5.78s; new worker 40278; gunicorn log mentions the dead worker: True",
  "recovery_s": 5.78,
  "requests_after_kill": [
    {
      "status": 200,
      "seconds": 5.78,
      "at_s": 5.78
    }
  ],
  "gunicorn_log_lines": [
    "[2026-11-18 17:06:52 -0500] [40276] [INFO] Booting worker with pid: 40276",
    "[2026-11-18 17:06:52 -0500] [40276] [INFO] loading the detector model (gpt2); on a machine that has never downloaded it this fetches ~550 MB and takes minutes",
    "[2026-11-18 17:06:59 -0500] [40276] [INFO] detector loaded: gpt2",
    "[2026-11-18 17:06:59 -0500] [40276] [INFO] detector warmed with one scoring pass in 65 ms",
    "[2026-11-18 17:06:59 -0500] [40273] [ERROR] Worker (pid:40276) was sent SIGKILL! Perhaps out of memory?",
    "[2026-11-18 17:06:59 -0500] [40278] [INFO] Booting worker with pid: 40278"
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
    "log_entries": 2287,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 17:07:05 -0500] [40279] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 17:07:05 -0500] [40279] [INFO] Listening at: http://127.0.0.1:5002 (40279)",
    "[2026-11-18 17:07:05 -0500] [40279] [INFO] Using worker: gthread",
    "[2026-11-18 17:07:05 -0500] [40282] [INFO] Booting worker with pid: 40282",
    "[2026-11-18 17:07:05 -0500] [40282] [INFO] loading the detector model (ai201-missing-model); on a machine that has never downloaded it this fetches ~550 MB and takes minutes",
    "[2026-11-18 17:07:06 -0500] [40282] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 17:07:06 -0500] [40282] [INFO] Worker exiting (pid: 40282)",
    "[2026-11-18 17:07:06 -0500] [40279] [INFO] Handling signal: term",
    "[2026-11-18 17:07:06 -0500] [40279] [INFO] Shutting down: Master"
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
    "log_entries": 2292,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 17:07:06 -0500] [40283] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 17:07:06 -0500] [40283] [INFO] Listening at: http://127.0.0.1:5002 (40283)",
    "[2026-11-18 17:07:06 -0500] [40283] [INFO] Using worker: gthread",
    "[2026-11-18 17:07:06 -0500] [40286] [INFO] Booting worker with pid: 40286",
    "[2026-11-18 17:07:06 -0500] [40286] [INFO] loading the detector model (ai201-missing-model); on a machine that has never downloaded it this fetches ~550 MB and takes minutes",
    "[2026-11-18 17:07:08 -0500] [40286] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 17:07:08 -0500] [40283] [INFO] Handling signal: term",
    "[2026-11-18 17:07:08 -0500] [40286] [INFO] Worker exiting (pid: 40286)",
    "[2026-11-18 17:07:08 -0500] [40283] [INFO] Shutting down: Master"
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
    "log_entries": 2297,
    "ok": true,
    "rate_limiting": true
  },
  "gunicorn_log_tail": [
    "[2026-11-18 17:07:08 -0500] [40287] [INFO] Starting gunicorn 23.0.0",
    "[2026-11-18 17:07:08 -0500] [40287] [INFO] Listening at: http://127.0.0.1:5002 (40287)",
    "[2026-11-18 17:07:08 -0500] [40287] [INFO] Using worker: gthread",
    "[2026-11-18 17:07:08 -0500] [40290] [INFO] Booting worker with pid: 40290",
    "[2026-11-18 17:07:08 -0500] [40290] [INFO] loading the detector model (ai201-missing-model); on a machine that has never downloaded it this fetches ~550 MB and takes minutes",
    "[2026-11-18 17:07:09 -0500] [40290] [ERROR] detector NOT loaded, serving 503s for /submit: Couldn't load 'ai201-missing-model': We couldn't connect to 'https://huggingface.co' to load the files, and couldn't find them in the cached files.",
    "[2026-11-18 17:07:09 -0500] [40287] [INFO] Handling signal: term",
    "[2026-11-18 17:07:09 -0500] [40290] [INFO] Worker exiting (pid: 40290)",
    "[2026-11-18 17:07:10 -0500] [40287] [INFO] Shutting down: Master"
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
      "seconds": 6.11,
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
    "{\"timestamp\": \"2026-11-18T22:07:16.264+00:00\", \"request_id\": \"aa5fc69621b5\", \"pid\": 40294, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 38.9, \"creator_id\": \"e4_second_improvement_20261118170453_t1_0\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 106, \"text_chars\": 552}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 38.01, \"signal_two\": 0.3, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T22:07:16.296+00:00\", \"request_id\": \"0c4cdcf43e84\", \"pid\": 40294, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 30.0, \"creator_id\": \"e4_second_improvement_20261118170453_t1_1\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 92, \"text_chars\": 685}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 29.33, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T22:07:16.334+00:00\", \"request_id\": \"5ade30a9999f\", \"pid\": 40294, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 36.4, \"creator_id\": \"e4_second_improvement_20261118170453_t1_2\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 119, \"text_chars\": 704}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 35.75, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T22:07:16.361+00:00\", \"request_id\": \"6c3dc37e70d4\", \"pid\": 40294, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 26.3, \"creator_id\": \"e4_second_improvement_20261118170453_t1_3\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 84, \"text_chars\": 392}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 25.67, \"signal_two\": 0.15, \"combine_label\": 0.02}}",
    "{\"timestamp\": \"2026-11-18T22:07:16.395+00:00\", \"request_id\": \"d04786901d91\", \"pid\": 40294, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 32.2, \"creator_id\": \"e4_second_improvement_20261118170453_t1_4\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 109, \"text_chars\": 588}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 31.58, \"signal_two\": 0.21, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T22:07:16.396+00:00\", \"request_id\": \"cec31eb80f80\", \"pid\": 40294, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null, \"in\": null, \"out\": null, \"stages_ms\": null}"
  ],
  "gunicorn_log_tail": [
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_mjsinb2z/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_mjsinb2z/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_mjsinb2z/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_mjsinb2z/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_mjsinb2z/audit.jsonl'",
    "[2026-11-18 17:07:16 -0500] [40294] [INFO] Worker exiting (pid: 40294)",
    "[2026-11-18 17:07:16 -0500] [40291] [INFO] Handling signal: term",
    "[2026-11-18 17:07:16 -0500] [40291] [INFO] Shutting down: Master"
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
      "seconds": 3.16,
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
    "{\"timestamp\": \"2026-11-18T22:07:20.020+00:00\", \"request_id\": \"b26537c0efd3\", \"pid\": 40320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 39.8, \"creator_id\": \"e4_second_improvement_20261118170453_t2_0\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 106, \"text_chars\": 552}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 38.86, \"signal_two\": 0.29, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T22:07:20.052+00:00\", \"request_id\": \"c1730a96a1c6\", \"pid\": 40320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 30.1, \"creator_id\": \"e4_second_improvement_20261118170453_t2_1\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 92, \"text_chars\": 685}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 29.46, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T22:07:20.090+00:00\", \"request_id\": \"ebb966085cec\", \"pid\": 40320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 36.1, \"creator_id\": \"e4_second_improvement_20261118170453_t2_2\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 119, \"text_chars\": 704}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 35.46, \"signal_two\": 0.2, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T22:07:20.117+00:00\", \"request_id\": \"b67a072b36ad\", \"pid\": 40320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 25.9, \"creator_id\": \"e4_second_improvement_20261118170453_t2_3\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 84, \"text_chars\": 392}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 25.25, \"signal_two\": 0.16, \"combine_label\": 0.02}}",
    "{\"timestamp\": \"2026-11-18T22:07:20.151+00:00\", \"request_id\": \"a202c43fa1fa\", \"pid\": 40320, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 32.1, \"creator_id\": \"e4_second_improvement_20261118170453_t2_4\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 109, \"text_chars\": 588}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 31.5, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T22:07:20.152+00:00\", \"request_id\": \"edb54afc0a02\", \"pid\": 40320, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null, \"in\": null, \"out\": null, \"stages_ms\": null}"
  ],
  "gunicorn_log_tail": [
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_h1_y1n9g/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_h1_y1n9g/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_h1_y1n9g/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_h1_y1n9g/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_h1_y1n9g/audit.jsonl'",
    "[2026-11-18 17:07:20 -0500] [40320] [INFO] Worker exiting (pid: 40320)",
    "[2026-11-18 17:07:20 -0500] [40317] [INFO] Handling signal: term",
    "[2026-11-18 17:07:20 -0500] [40317] [INFO] Shutting down: Master"
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
      "seconds": 14.91,
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
    "{\"timestamp\": \"2026-11-18T22:07:35.525+00:00\", \"request_id\": \"81b6333ffc31\", \"pid\": 40333, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 39.5, \"creator_id\": \"e4_second_improvement_20261118170453_t3_0\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 106, \"text_chars\": 552}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 38.57, \"signal_two\": 0.29, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T22:07:35.556+00:00\", \"request_id\": \"a4038792f154\", \"pid\": 40333, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 29.9, \"creator_id\": \"e4_second_improvement_20261118170453_t3_1\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 92, \"text_chars\": 685}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 29.19, \"signal_two\": 0.17, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T22:07:35.593+00:00\", \"request_id\": \"6d24314d7857\", \"pid\": 40333, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 35.3, \"creator_id\": \"e4_second_improvement_20261118170453_t3_2\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 119, \"text_chars\": 704}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 34.68, \"signal_two\": 0.18, \"combine_label\": 0.03}}",
    "{\"timestamp\": \"2026-11-18T22:07:35.620+00:00\", \"request_id\": \"11a3b7179cc4\", \"pid\": 40333, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 25.9, \"creator_id\": \"e4_second_improvement_20261118170453_t3_3\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 84, \"text_chars\": 392}, \"out\": null, \"stages_ms\": {\"checks\": 0.01, \"signal_one\": 25.25, \"signal_two\": 0.15, \"combine_label\": 0.02}}",
    "{\"timestamp\": \"2026-11-18T22:07:35.654+00:00\", \"request_id\": \"c505cdd75b2e\", \"pid\": 40333, \"method\": \"POST\", \"path\": \"/submit\", \"status\": 503, \"latency_ms\": 31.9, \"creator_id\": \"e4_second_improvement_20261118170453_t3_4\", \"error\": \"audit_unavailable\", \"in\": {\"text_words\": 109, \"text_chars\": 588}, \"out\": null, \"stages_ms\": {\"checks\": 0.02, \"signal_one\": 31.24, \"signal_two\": 0.18, \"combine_label\": 0.04}}",
    "{\"timestamp\": \"2026-11-18T22:07:35.655+00:00\", \"request_id\": \"d58feb28c71e\", \"pid\": 40333, \"method\": \"POST\", \"path\": \"/ping\", \"status\": 200, \"latency_ms\": 0.1, \"creator_id\": null, \"error\": null, \"in\": null, \"out\": null, \"stages_ms\": null}"
  ],
  "gunicorn_log_tail": [
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_5uv6pr76/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_5uv6pr76/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_5uv6pr76/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_5uv6pr76/audit.jsonl'",
    "submit refused, decision not recorded: audit log not writable: [Errno 13] Permission denied: '/var/folders/89/h1l_hb695gg521zj3m264fch0000gn/T/e4_logs_5uv6pr76/audit.jsonl'",
    "[2026-11-18 17:07:35 -0500] [40333] [INFO] Worker exiting (pid: 40333)",
    "[2026-11-18 17:07:35 -0500] [40330] [INFO] Handling signal: term",
    "[2026-11-18 17:07:35 -0500] [40330] [INFO] Shutting down: Master"
  ]
}
```

## E5

**Trial 1** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {40362: 1028.2}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {40362: 1028.2}",
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
    "peak_rss_mb": 1028.2,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T22:07:41.539 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.6,
      "mean": 29.1,
      "p50": 28.4,
      "p95": 35.6
    },
    "worker_pid": 40362,
    "worker_started_at": "2026-11-18T22:07:36.103+00:00"
  },
  "worker_rss_mb": {
    "40362": 1028.2
  }
}
```

**Trial 2** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {40388: 1029.8}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {40388: 1029.8}",
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
    "peak_rss_mb": 1029.8,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T22:07:47.465 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.1,
      "mean": 28.7,
      "p50": 28.3,
      "p95": 35.1
    },
    "worker_pid": 40388,
    "worker_started_at": "2026-11-18T22:07:43.700+00:00"
  },
  "worker_rss_mb": {
    "40388": 1029.8
  }
}
```

**Trial 3** — sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5×200); worker RSS MB {40394: 1026.2}

```json
{
  "passed": true,
  "summary": "sent 25; request log 25; client {'200': 10, '429': 10, '400': 5} vs /metrics {'200': 10, '400': 5, '429': 10}; flood .....xxxxxxxxxx (5\u00d7200); worker RSS MB {40394: 1026.2}",
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
    "peak_rss_mb": 1026.4,
    "rate_limited": 10,
    "requests": 25,
    "server_errors": 0,
    "since": "2026-11-18T22:07:53.321 00:00",
    "submit_latency_ms": {
      "count": 8,
      "max": 35.4,
      "mean": 27.9,
      "p50": 26.9,
      "p95": 35.4
    },
    "worker_pid": 40394,
    "worker_started_at": "2026-11-18T22:07:49.505+00:00"
  },
  "worker_rss_mb": {
    "40394": 1026.2
  }
}
```
