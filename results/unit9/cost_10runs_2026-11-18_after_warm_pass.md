# Ten runs after the second improvement (warm-up runs one scoring pass) — 2026-11-18

- Same method as `cost_10runs_2026-11-18.md`: `PORT=5001 ./serve.sh`, one `/submit` at a time, 0.5 s apart; client timer; `ps -o cputime` on the worker; each request's line in `logs/requests.jsonl`.

| Run | Words | Client wall ms | Server `latency_ms` | of which signal one | Worker CPU ms | Guess |
|---|---|---|---|---|---|---|
| 1 | 106 | 57.8 | 53.7 | 52.43 | 170 | human |
| 2 | 92 | 52.0 | 47.5 | 46.12 | 130 | ai |
| 3 | 119 | 55.7 | 51.2 | 50.1 | 160 | unsure |
| 4 | 84 | 40.7 | 37.3 | 36.21 | 100 | unsure |
| 5 | 109 | 51.9 | 47.4 | 46.22 | 140 | human |
| 6 | 106 | 49.7 | 46.1 | 44.95 | 140 | human |
| 7 | 92 | 48.3 | 44.2 | 43.08 | 130 | ai |
| 8 | 119 | 51.4 | 47.6 | 46.45 | 140 | unsure |
| 9 | 84 | 45.7 | 41.1 | 39.93 | 120 | unsure |
| 10 | 109 | 52.6 | 48.1 | 46.9 | 150 | human |
| **average** | | **50.6** | **46.4** | **45.2** | **138** | |
