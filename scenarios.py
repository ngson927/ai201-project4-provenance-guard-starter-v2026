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
        # ⚠️ STAND-INS, NOT THE STUDENT'S WRITING. These ten were written by
        # Claude (Claude Code, Opus 5.5) on 2026-11-18, at the student's request,
        # because no pieces of the student's own writing were supplied. The
        # first three imitate plain writing (short sentences, everyday words).
        # README → Run Log and Verdicts → "Criterion 1, run with stand-ins"
        # says what that does and doesn't let this run show.
        "texts": [
            # 1 — plain
            "I got up late on Saturday. The kitchen was cold, so I made tea and "
            "sat by the window. My sister called at ten. She wanted to borrow my "
            "car for the afternoon. I said yes, but she had to fill the tank. "
            "After that I cleaned my room and did two loads of washing. In the "
            "evening we ordered pizza and watched an old film. It was a quiet "
            "day, and that was fine with me.",
            # 2 — plain
            "Our team lost the game on Sunday. We were tired from the start. The "
            "other side was faster and they passed the ball well. I missed an "
            "easy shot in the first half. The coach did not shout at us. He said "
            "we need to run more in practice. I think he is right. Next week we "
            "play the team from the north side of town. They beat us last year, "
            "so we want this one.",
            # 3 — plain
            "My first job was at a small shop near the bus station. I worked "
            "there on weekends when I was sixteen. I put things on the shelves "
            "and helped people find what they needed. The owner was strict but "
            "fair. If you came late, he cut your hours. If you worked hard, he "
            "gave you extra time. I learned to count change fast and to talk to "
            "strangers. I still use both every week.",
            # 4 — email
            "Hi Professor Lee, I'm writing about the lab report due Friday. Our "
            "group's sensor stopped giving readings on Tuesday, and the "
            "replacement from the stockroom only arrived this morning, so we've "
            "lost about two days of data collection. Would it be possible to "
            "hand in on Monday instead? If not, we can submit what we have on "
            "Friday and add the rest as an appendix later. Either way, thanks "
            "for your time, and sorry for the late notice.",
            # 5 — reflection
            "The hardest part of this project wasn't the code; it was deciding "
            "what counted as finished. Every time a test passed, I found another "
            "case it didn't cover — an empty string, a list where I expected "
            "text, a request that arrived twice. At some point I had to stop "
            "adding checks and write down what I wasn't handling. That list "
            "turned out to be more useful than half the checks, because it told "
            "the next person where to look first.",
            # 6 — review
            "I wanted to like this café more than I did. The coffee is good — "
            "strong, not bitter — and the window seats are the best place on the "
            "street to watch the rain. But the music is loud enough that you "
            "have to lean in to hear anyone, and the one outlet near the tables "
            "is always taken by nine. I'd go back for a quick cup on the way "
            "somewhere. I wouldn't go back to study.",
            # 7 — opinion
            "People say group projects teach teamwork, and sometimes they do. "
            "More often they teach one person to do the work while everyone "
            "else watches the deadline. What fixed it for us was boring: a "
            "shared list with names next to every task and a ten-minute check-in "
            "each Monday. Nobody liked the check-in. Nobody missed a task "
            "either. I don't think that's teamwork exactly, but it got us to the "
            "end without anyone quitting.",
            # 8 — instructions
            "To reset the router, first unplug it and wait thirty seconds. Plug "
            "it back in and wait until the light on the front turns solid green; "
            "that can take two or three minutes. If it blinks orange instead, "
            "press the small button on the back with a paperclip and hold it "
            "for ten seconds. Then reconnect your laptop to the network named on "
            "the sticker underneath, using the password printed beside it.",
            # 9 — description
            "My grandmother's house had a back porch that leaned a little to "
            "the left, like it was listening for something. In summer she kept "
            "tomatoes in buckets along the railing and a radio on the step that "
            "only played one station. We shelled peas there in the evenings, "
            "dropping the pods into a paper bag between us, and she told the "
            "same three stories in a different order each time.",
            # 10 — cover letter
            "I'm applying for the part-time data assistant role in your "
            "admissions office. Last semester I cleaned and merged three years "
            "of survey responses for a professor's study, about four thousand "
            "rows with inconsistent dates and duplicate entries, and wrote a "
            "short guide so the next student could repeat it. I'm comfortable "
            "in spreadsheets and Python, careful with private data, and "
            "available fifteen hours a week, including Friday mornings.",
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
