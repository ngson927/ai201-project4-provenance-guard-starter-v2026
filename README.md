# Provenance Guard

**Repository (submitted for units 7 and 8; do not recreate):**
https://github.com/ngson927/ai201-project4-provenance-guard-starter-v2026

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

Full design, including the false-positive trace and both endpoint contracts:
[DESIGN.md](DESIGN.md).

1. **`POST /submit` receives the request** (`app.py::submit`): JSON
   `{"text", "creator_id"}` arrives as raw input we can't trust yet.
2. **Validation and identity:** bad, empty, too-short (< 20 words) or too-long
   (> 10,000 chars) input is refused with a 400 and logged as a rejection.
   Valid input gets a new `content_id`.
3. **Signal one, `detector.model_signal`:** gpt2 measures how predictable the
   text is. Adds `model_score` (0–1, higher = more AI-like).
4. **Signal two, `stylometry.style_signal`:** sentence-length spread,
   vocabulary variety and punctuation variety. Adds `style_score` (0–1,
   higher = more AI-like).
5. **The combining rule, `scoring.combine_signals`:** two scores become one.
   Adds `confidence`, the combined score.
6. **The label mapping, `scoring.score_to_label`:** thresholds turn the number
   into a `guess` (human / unsure / ai) and the `label` sentence a person
   reads.
7. **Audit log, then response:** `audit.log_decision` appends all nine fields
   with `status: "decided"`. The reader gets the label and the `content_id`
   they'd need for `POST /appeal`, which moves the item to `under_review`.



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a local language model
(gpt2), as perplexity. Low perplexity maps to a high score, so higher means
more AI-like.

**Why that might differ between human and AI writing:** A model writes by
picking likely next words, so its output is easy for a similar model to
predict. People make choices a model wouldn't rank first (odd words, specific
details, abrupt turns), and that raises perplexity.

**What it can't see:** Authorship. Predictability really rewards common words
in short, plain sentences. A second-language writer, a younger writer, or
anyone writing plainly on purpose scores as machine-like as a machine. In the
other direction, AI text with rare words added, paraphrased, or sampled hot
reads as human, and so does ornate human prose. It also ignores everything
after the first 400 tokens, and gpt2 is far older than the models writing
today's AI text.

### Signal two — the style signal

**What it measures:** The shape of the text with no understanding of it:
- sentence-length spread (coefficient of variation);
- vocabulary variety (windowed type–token ratio);
- variety of expressive punctuation (`; : — ( ) ! ?`).

Each measure is flipped so that uniform text scores high, put on 0–1, then
averaged. Higher means more AI-like.

**Why that might differ between human and AI writing:** "Most likely next
word" produces even prose on average: mid-length sentences, a narrow band of
vocabulary, tidy punctuation. Human writing is lumpier.

**What it can't see:** Meaning. Anything that changes shape without changing
substance moves it:
- typos (which raise vocabulary variety);
- chopped or merged sentences;
- sprinkled dashes;
- a pasted quotation;
- a prompt to "vary sentence length".

It can't tell an even-handed human from a machine either. Technical, legal
and plain-style writing all look uniform. On short texts it's mostly noise.
Both blind spots point at the same person, the plain, careful writer, so the
two signals aren't independent witnesses for them.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Average the two signals with equal weight. When they disagree
sharply, don't average: return 0.5, a coin flip, which always lands in
"unsure". Two methods contradicting each other *is* uncertainty, and an
average would hide it behind a confident-looking number. The thresholds
then make "AI" the hardest label to get. An average of 0.85 needs both
signals at 0.70 or above, so neither signal can make the call alone.

**The numbers** (all in `config.py`):

| Setting | Value | Why |
|---|---|---|
| `WEIGHT_MODEL_SIGNAL` / `WEIGHT_STYLE_SIGNAL` | 0.5 / 0.5 | Neither is more trustworthy. The model signal is biased against plain writers, and the style signal is cheap to game |
| `SPLIT_GAP` | 0.40 | A gap this size means the signals point opposite ways. On the calibration set only the deliberately split case reaches it. The largest ordinary gap is 0.23 |
| `HUMAN_THRESHOLD` | 0.42 | Above both clearly-human inputs (0.369, 0.398) and below every AI input that isn't split (lowest 0.667) |
| `AI_THRESHOLD` | 0.85 | Set above the plain human writer (0.807) rather than at the starter's 0.65, per the DESIGN.md §3 trace |

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**Calibration** (`python calibrate.py --raw`). Spread, MATTR and punct are the
raw style measures. MATTR is shown but not scored.

| Input | model | style | combined | label | spread | MATTR | punct /100w |
|---|---|---|---|---|---|---|---|
| clearly AI | 0.850 | 1.000 | 0.925 | ai | 0.20 | 0.90 | 0.00 |
| lightly-edited AI | 0.648 | 0.686 | 0.667 | unsure | 0.35 | 0.89 | 1.25 |
| AI, varied rhythm | 0.597 | 0.156 | **0.500** (split) | unsure | 1.10 | 0.92 | 2.94 |
| clearly human (Twain) | 0.463 | 0.333 | 0.398 | human | 0.72 | 0.71 | 2.78 |
| formal human (Mill) | 0.709 | 0.510 | 0.610 | unsure | 0.54 | 0.77 | 0.00 |
| plain human | 0.847 | 0.767 | 0.807 | unsure | 0.18 | 0.84 | 0.00 |
| ornate human | 0.254 | 0.484 | 0.369 | human | 1.16 | 0.84 | 1.37 |

Twain and Mill are real public-domain text. "Plain human" and "ornate human"
are stand-ins until I swap in my own writing.

**Where they agree and where they split:**
- **Agree on AI:** the clearly-AI text.
- **Agree on human:** Twain.
- **Mild splits:** Mill and the ornate paragraph, under 0.25 apart.
- **Both wrong together:** the plain human writer, both signals over 0.75.
  Nothing in the rule can fix shared evidence. Only the AI threshold keeps
  this person out of the AI label, and the margin is thin (0.807 against
  0.85).

**A case where my two signals split, and what my rule does with it:** AI
prose that varies its rhythm on purpose, with a one-word question, a fragment
and a dash. The model signal still reads it as AI-leaning (0.597). The style
signal reads it as strongly human (0.156), because varied rhythm is exactly
what style measures and it can't read meaning. A plain average gives 0.376,
which is under the human threshold. AI text would get a "high-confidence
human" label just by varying its rhythm. The gap is 0.44 ≥ `SPLIT_GAP`, so the
rule returns 0.5 and the reader gets "unsure" instead.

**Surprises I followed up by printing the signals separately:**
- **Mill is not read as human by signal one** (0.709), despite the starter's
  note that formal prose scores human. Long sentences of common words are
  predictable even when they're formal.
- **Type–token ratio points the wrong way** on this set. The AI texts have
  the *most* varied vocabulary. That's why it's computed but kept out of the
  score.
- **The lightly-edited AI drops to "unsure"** (0.667), not "AI". A minute of
  editing is enough to get out of the AI label. That's the price of an AI
  threshold high enough to protect the plain writer, and I'm choosing to pay
  it.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.42 | We think this was most likely written by a person. Our automated checks didn't find the patterns we usually see in AI-generated writing. |
| unsure | above 0.42, below 0.85 | We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing — and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review. |
| high-confidence AI | 0.85 – 1.00 | Our automated checks found strong patterns that are common in AI-generated writing. This is an estimate, not proof: the checks can be wrong, especially about plain, straightforward writing. If you wrote this yourself, you can ask for a review and a person will look at it. |

Scores of exactly 0.42 get the human label, and exactly 0.85 the AI label, so
every score lands in exactly one band. I reached all three with real
submissions: the clearly-AI text gave `ai` (0.9247), the plain human text
`unsure` (0.8069) and Twain `human` (0.3982). The text lives in
`scoring.py` as `LABEL_HUMAN`, `LABEL_UNSURE` and `LABEL_AI`.

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

The person most likely to read it is the plain writer from DESIGN.md §3. With
my thresholds, "unsure" is where that person lands (0.807). So it does four
things:
- **Starts with what we don't know.** "We can't tell either way" comes before
  anything about AI.
- **Explains why clear writing lands here,** so a careful, simple writer
  doesn't read it as a judgement on their style.
- **Says outright that nothing here means they did anything wrong.**
- **Offers a person without making it sound like a defence they owe.**

It never uses "suspicious", "flagged" or "detected". The AI label is the
only one that mentions AI patterns as a finding, and even that one calls
itself an estimate, names who it gets wrong, and says how to get a person to
look.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

The plain writer from DESIGN.md §3, end to end.

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I moved to this city two years ago for my job. At first it was very hard because I did not know anyone. I worked every day and I went home every night. Then I started to go to a running club on Saturday. Now I have some good friends there. We run in the park and after we drink coffee together. I think it is important to try new things when you are lonely. It is not easy but it is worth it.", "creator_id": "student-9"}'
```

```json
{
  "confidence": 0.8069,
  "content_id": "eee1e5c5-1df1-487e-91be-2a06f4a484ca",
  "creator_id": "student-9",
  "guess": "unsure",
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing — and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "model_score": 0.847,
  "status": "decided",
  "style_score": 0.7667
}
```

A refused one, which is logged as well:

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "", "creator_id": "student-42"}'
```

```json
{
  "error": "missing_text",
  "message": "There's no text to check. Send it in the 'text' field."
}
```
(HTTP 400)

**Signal one on its own, before wiring it in** (`python detector.py "..."`):

| Text | Perplexity | `model_signal` |
|---|---|---|
| Generic AI paragraph about AI ethics | 12.2 | 0.8896 |
| Human, specific and ornate (grandmother's button tin) | 88.2 | 0.2543 |
| Human, plain (moving to a new city, short sentences) | 15.1 | **0.8513** |

The plain human paragraph scores almost as AI-like as the AI text. This is
the false positive from DESIGN.md §3, and it's worse than the 0.79 I
predicted.

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "eee1e5c5-1df1-487e-91be-2a06f4a484ca", "reasoning": "I wrote this myself about my first year in the city. English is my second language, so I keep my sentences simple."}'
```

```json
{
  "content_id": "eee1e5c5-1df1-487e-91be-2a06f4a484ca",
  "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
  "original_guess": "unsure",
  "status": "under_review"
}
```

Also checked: a second appeal on the same id gives **409**
`already_under_review`, a made-up `content_id` gives **404**
`unknown_content_id`, and missing reasoning or a non-JSON body gives **400**.

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

The original decision stays where it was. The appeal is appended after it
with `status: "under_review"`.

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.8069,
      "content_id": "eee1e5c5-1df1-487e-91be-2a06f4a484ca",
      "creator_id": "student-9",
      "guess": "unsure",
      "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
      "model_score": 0.847,
      "status": "decided",
      "style_score": 0.7667,
      "timestamp": "2026-10-28T23:42:51+00:00"
    },
    {
      "content_id": "eee1e5c5-1df1-487e-91be-2a06f4a484ca",
      "creator_id": "student-9",
      "event": "appeal",
      "reasoning": "I wrote this myself about my first year in the city. English is my second language, so I keep my sentences simple.",
      "status": "under_review",
      "timestamp": "2026-10-28T23:42:51+00:00"
    }
  ]
}
```

---

## Stretch: `GET /content/<id>`

**Declared before building.** `GET /content/<content_id>` returns one item's
*current* state, so a writer who appealed can check where it stands without
reading the whole audit log.

**Plan:**
- **Lookup:** read every log entry for that id with `audit.entries_for`.
- **Unknown id:** if there's no `decided` entry, return 404
  `unknown_content_id`, the same error as `/appeal`.
- **Otherwise, return:**
  - `content_id`, `creator_id`, `guess`, `label`, `confidence`,
    `model_score`, `style_score` from the original decision;
  - `status` from the **latest** entry (`decided`, or `under_review` after an
    appeal);
  - `submitted_at`;
  - `appealed_at`, which is `null` if there's been no appeal.
- **Not returned:** the appeal's `reasoning`. That's for the reviewer, not
  for anyone who happens to have the id.
- **No writes:** it never changes the log.

**Built** in `app.py::content_status`, as planned above. This is the writer
from Sample Run after their appeal:

```bash
$ curl http://127.0.0.1:5000/content/eee1e5c5-1df1-487e-91be-2a06f4a484ca
```

```json
{
  "appealed_at": "2026-10-28T23:42:51+00:00",
  "confidence": 0.8069,
  "content_id": "eee1e5c5-1df1-487e-91be-2a06f4a484ca",
  "creator_id": "student-9",
  "guess": "unsure",
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "model_score": 0.847,
  "status": "under_review",
  "style_score": 0.7667,
  "submitted_at": "2026-10-28T23:42:51+00:00"
}
```

An item with no appeal returns `"status": "decided"` and `"appealed_at":
null`. A made-up id returns **404** `unknown_content_id`.

**What it changed:**
- **For the writer:** they can now see that their appeal landed and that the
  label is under review, without access to the full audit log.
- **For the log:** nothing. The route only reads.
- **For unit 8:** it's another route an attacker can probe, and a run of
  404s from it would mean someone is guessing ids.

---

## How I Used AI

I used Claude Code (Claude Opus 5.5) as a pair through all six milestones. I
gave it each milestone's brief, it wrote and ran the code, and I checked the
numbers it produced before each commit.

**Moment 1: the false-positive prediction, and the threshold it moved**

- *What I asked for:* the Milestone 1 trace. That meant following a real
  writer who gets called AI through the service and predicting their score
  before any code existed.
- *What came back:* a second-language writer with plain, short sentences,
  and a predicted model score of about 0.79 worked out from the formula in
  `detector.py`. It proposed raising `AI_THRESHOLD` from the starter's 0.65
  to "around 0.80".
- *What I changed:* the prediction was wrong, and running it is how I found
  out. In Milestone 3 the plain paragraph actually scored **0.85** on signal
  one, nearly the same as the AI text (0.89). In Milestone 4 its combined
  score was 0.807, so a threshold of 0.80 would still have accused that
  writer. I moved `AI_THRESHOLD` to **0.85** and accepted the cost: the
  lightly-edited AI text now gets "unsure" instead of "AI". A threshold
  taken from the paper trace would have shipped the exact false positive the
  trace was written to prevent.

**Moment 2: the vocabulary measure that pointed the wrong way**

- *What I asked for:* signal two, built from the three measures the starter
  names, including type–token ratio, using the starter's hypothesis that AI
  text has a narrower vocabulary.
- *What came back:* the three measures implemented. A moving-average
  type–token ratio was there so short and long texts could be compared.
- *What I changed:* before scaling anything I printed the raw measures over
  the calibration set (`python calibrate.py --raw`). Type–token ratio came
  out *highest* for the AI paragraph (0.90) and lowest for Twain (0.71), the
  opposite of the hypothesis, across a narrow range. I took it out of the
  score, kept the function so it's still reported, and replaced it with a
  mid-length-sentence reading. Unlike signal one, that reading does *not*
  reward short plain sentences, so the two signals stop sharing a blind spot
  for the plain writer. Had I averaged in the starter's version, it would
  have pushed AI text toward "human".

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [x] criteria.md has five numbered criteria, each naming a target
       [x] Each has a reason underneath
       [x] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [x] Two signals that measure DIFFERENT things, each with a named blind spot
       [x] Three label variants, all reachable, written out in full
       [x] POST /appeal changes status and writes to the log
       [x] Signals and Scoring names scoring.py::combine_signals
       [x] Sample Run: a submission AND an appeal, as pasted text
       [x] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
