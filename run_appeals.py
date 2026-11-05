#!/usr/bin/env python3
"""
Criterion 5 — every appeal changes status and is recorded.  <- UNIT 8, MILESTONE 3

    python app.py                               # in one terminal
    python run_appeals.py --label before        # in another

run_eval.py can't test this: an appeal needs the content_id its submission
returned. This does the steps criteria.md §5 describes, three trials:

  1. Submit 5 texts to POST /submit.
  2. POST /appeal each returned content_id with a non-empty reasoning.
  3. POST /appeal once with "content_id": "not-a-real-id".

and then reads GET /log to check each id has its "decided" entry followed by
an "event": "appeal" entry. Writes results/appeals_<date>_<label>.md.
"""

import argparse
import datetime as dt
import json
import sys

import requests

import config
from calibrate import CLEARLY_AI, CLEARLY_AI_2, CLEARLY_HUMAN, CLEARLY_HUMAN_2, FORMAL_HUMAN

TEXTS = [CLEARLY_AI, CLEARLY_AI_2, CLEARLY_HUMAN, CLEARLY_HUMAN_2, FORMAL_HUMAN]
REASONING = "I wrote this myself and can show my drafts."


def run_trial(url, trial, stamp):
    appeals = []
    for i, text in enumerate(TEXTS, 1):
        sub = requests.post(f"{url}/submit", timeout=90,
                            json={"text": text, "creator_id": f"eval_appeal_{stamp}_t{trial}_{i}"})
        content_id = sub.json().get("content_id")
        app = requests.post(f"{url}/appeal", timeout=30,
                            json={"content_id": content_id, "reasoning": REASONING})
        appeals.append({"submit_status": sub.status_code, "content_id": content_id,
                        "appeal_status": app.status_code, "appeal_response": app.json()})

    fake = requests.post(f"{url}/appeal", timeout=30,
                         json={"content_id": "not-a-real-id", "reasoning": REASONING})

    log = requests.get(f"{url}/log", timeout=30).json()["entries"]
    for a in appeals:
        events = [("appeal" if e.get("event") == "appeal" else e.get("status"))
                  for e in log if e.get("content_id") == a["content_id"]]
        a["log_sequence"] = events
        a["passed"] = (a["appeal_status"] == 200
                       and a["appeal_response"].get("status") == "under_review"
                       and events == ["decided", "appeal"])

    return {"appeals": appeals,
            "fake_id": {"status": fake.status_code, "response": fake.json()},
            "real_passed": sum(a["passed"] for a in appeals),
            "fake_404": fake.status_code == 404}


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=f"http://{config.HOST}:{config.PORT}")
    args = parser.parse_args()

    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        sys.exit(f"Nothing answering at {args.url}. Start it:  python app.py")

    stamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    trials = []
    for t in range(1, args.trials + 1):
        result = run_trial(args.url, t, stamp)
        trials.append(result)
        print(f"  trial {t}: {result['real_passed']}/5 real appeals passed, "
              f"made-up id -> {result['fake_id']['status']}")

    config.RESULTS_DIR.mkdir(exist_ok=True)
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{dt.datetime.now():%Y-%m-%d_%H%M}{label}.md"
    lines = ["# Criterion 5 — appeals" + (f" — {args.label}" if args.label else ""), "",
             "- Produced by: `run_appeals.py::run_trial`",
             "- Service: `app.py::submit`, `app.py::appeal`, `app.py::get_log`", ""]
    for t, result in enumerate(trials, 1):
        lines += [f"**Trial {t}**: {result['real_passed']}/5 real appeals passed, "
                  f"made-up id returned {result['fake_id']['status']}", "",
                  "```json", json.dumps(result, indent=2, ensure_ascii=False), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
