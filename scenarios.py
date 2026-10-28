"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

from calibrate import (
    CLEARLY_AI, CLEARLY_AI_2, CLEARLY_AI_3,
    CLEARLY_HUMAN, CLEARLY_HUMAN_2, CLEARLY_HUMAN_3,
    FORMAL_HUMAN, LIGHTLY_EDITED_AI, VARIED_AI,
)

# The inputs criteria.md names, word for word. Criteria 2 and 3 share the
# clearly-AI and clearly-human sets; criterion 2 adds the borderline one.

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ Ten pieces I actually wrote. The FIRST THREE are the plain ones —
        # short sentences, everyday words — that criterion 1 says must never
        # be labelled AI. run_eval.py refuses to run until these are real.
        "texts": [
            "REPLACE ME — plain piece 1 of 3 (short sentences, everyday words).",
            "REPLACE ME — plain piece 2 of 3.",
            "REPLACE ME — plain piece 3 of 3.",
            "REPLACE ME — my own writing, piece 4.",
            "REPLACE ME — my own writing, piece 5.",
            "REPLACE ME — my own writing, piece 6.",
            "REPLACE ME — my own writing, piece 7.",
            "REPLACE ME — my own writing, piece 8.",
            "REPLACE ME — my own writing, piece 9.",
            "REPLACE ME — my own writing, piece 10.",
        ],
    },
    {
        "name": "clearly AI",
        "criterion": 3,   # also half of criterion 2's nine inputs
        # Unedited model output on stock essay topics.
        "texts": [CLEARLY_AI, CLEARLY_AI_2, CLEARLY_AI_3],
    },
    {
        "name": "clearly human",
        "criterion": 3,   # also part of criterion 2's nine inputs
        # Published before language models existed: Twain, Melville, Thoreau.
        "texts": [CLEARLY_HUMAN, CLEARLY_HUMAN_2, CLEARLY_HUMAN_3],
    },
    {
        "name": "borderline",
        "criterion": 2,
        # Lightly-edited AI, AI with deliberately varied rhythm, and Mill's
        # formal prose — each one sits between the two clear sets.
        "texts": [LIGHTLY_EDITED_AI, VARIED_AI, FORMAL_HUMAN],
    },
    {
        "name": "bad input",
        "criterion": 4,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
            {"text": CLEARLY_AI},                        # no creator_id
        ],
    },
    # Criterion 5 (appeals) can't be expressed here: it needs the content_id a
    # submission returns. It's tested by hand with curl — see criteria.md.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
