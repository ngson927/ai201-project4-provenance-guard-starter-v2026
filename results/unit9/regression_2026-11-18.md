# Regression check — does the original system still work? (2026-11-18)

Unit 8's own tests, run on the capstone run path (`PORT=5001 ./serve.sh`, the hardened code with
the new logging), compared row by row with the last runs before the extension. The scoring code
didn't change, so every guess and score should match exactly.

| Check | Compared with | Result |
|---|---|---|
| `python test.py` | — | 9 passed, 0 failed |
| Full attack set, 56 rows → `results/attack_run_2026-11-18_1639_regression.md` | `results/attack_run_2026-11-04_1945_after2.md` | **56/56 identical** status, guess, confidence, both signal scores; 0 auto-BROKE |
| `run_eval.py`, 5 criteria × 3 → `results/run_2026-11-18_1639_regression_alone.md` | `results/run_2026-11-18_1616_final_standins.md` | **all 5 scenarios, all 3 trials identical** |
| `run_appeals.py` × 3 → `results/appeals_2026-11-18_1639_regression.md` | criterion 5 target | 5/5 real appeals → `under_review` + logged, made-up id → 404, every trial |
| gunicorn stderr during the run | — | 0 tracebacks, 0 errors |

**One false alarm, explained and re-run.** The first `run_eval.py`
(`results/run_2026-11-18_1639_regression.md`) ran seconds after the attack set. Its "no
`creator_id`" body came back **429** instead of 400. A request with no creator is rate-limited by IP
address, and the attack set's malformed rows (several without a creator) had just used that
address's 5-per-minute allowance. RQ10 and RQ11 hit the same thing in unit 8. Running `run_eval.py`
on its own against a fresh service gave the original 400 and an exact match. So this is test
ordering, not a regression. It's also a reminder that two test scripts run back to back share one
rate-limit bucket when they send requests without a `creator_id`.
