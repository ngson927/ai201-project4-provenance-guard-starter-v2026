# Provenance Guard — Milestone 1 design

Written before any of `/submit`, `/appeal`, `stylometry.py` or `scoring.py`
exists. This is the contract the later milestones build against. If the code
and this file disagree, one of them is wrong and gets fixed on purpose.

---

## 1. The path a submission takes

From arriving to the label a reader sees:

1. **The request arrives at `POST /submit`** (`app.py::submit`).
   A client sends JSON `{"text": ..., "creator_id": ...}`. Flask parses it.
   *Adds:* nothing yet. All we have is raw input we can't trust.

2. **Validation and identity** (`app.py::submit`).
   Reject a body that isn't a JSON object. Reject `text` that is missing,
   not a string, too short to judge (< 20 words) or too long (> 10,000
   characters). Reject a missing `creator_id`. Every rejection is written with
   `audit.log_rejection` and returns a 400. Nothing is guessed about text we
   refused. If the input passes, mint a `content_id` (`uuid4`).
   *Adds:* a `content_id`, plus the guarantee that everything downstream
   receives a usable string.

3. **Signal one: the model signal** (`detector.model_signal`).
   gpt2 runs locally and measures the text's perplexity (only the first 400
   tokens). A logistic curve maps that onto 0–1.
   *Adds:* `model_score`, where higher means more predictable and so more
   AI-like.

4. **Signal two: the style signal** (`stylometry.style_signal`).
   It measures sentence-length spread, vocabulary variety (type–token ratio)
   and punctuation variety, rescales each onto 0–1 and points them the same
   direction.
   *Adds:* `style_score`, where higher means more uniform and so more AI-like.

5. **The combining rule** (`scoring.combine_signals`).
   Turns two scores into one.
   *Adds:* the combined score, returned as `confidence` and logged as
   `combined_score`. This is where the false-positive decision actually gets
   made (see §3).

6. **The label mapping** (`scoring.score_to_label`).
   Thresholds in `config.py` turn the number into one of three outcomes.
   *Adds:* `guess` (`"human"` / `"unsure"` / `"ai"`) and `label`, the
   sentence a person reads.

7. **The audit log, then the response** (`audit.log_decision`, then `jsonify`).
   Writes one append-only line with all nine fields and `status: "decided"`,
   then returns the response.
   *Adds:* a permanent record that `/appeal` and unit 8 can find again by
   `content_id`. The reader sees the `label`, and the `content_id` they need
   in order to appeal.

The loop back: if the reader disagrees, `POST /appeal` with that `content_id`
looks up the decision with `audit.entries_for` and records the appeal with
`audit.log_appeal`. The item moves to `status: "under_review"`. The original
decision is never overwritten.

---

## 2. The two signals

### Signal one: the model signal (`detector.py`, given)

**What it measures.** How predictable the text is to a language model
(gpt2). This is perplexity: the average surprise per token, mapped so that
low perplexity gives a high score.

**Why it might differ between human and AI writing.** A language model writes
by repeatedly choosing a likely next token. Its output is therefore text a
similar model finds easy to predict. People make choices a model wouldn't
rank first: an odd word, a specific detail, an abrupt turn. That raises
perplexity.

**What it can't see.** Authorship. It measures predictability, and
predictability really rewards *common words in short, ordinary sentences*.
Plenty of humans write that way: a second-language writer sticking to words
they're sure of, a younger writer, anyone writing plainly on purpose. These
writers score as machine-like as a machine does. It is blind in the other
direction too. AI text with rare vocabulary added, paraphrased, or generated
at high temperature reads as surprising and scores human. Ornate human prose
also scores human. It also can't see:
- anything after the first 400 tokens;
- that gpt2 is much older and smaller than the models producing today's AI
  text;
- that topic and length shift perplexity on their own.

### Signal two: the style signal (`stylometry.py`, mine to build)

**What it measures.** The *shape* of the text, with no understanding of the
words:
- **Sentence-length spread:** standard deviation of words-per-sentence divided
  by the mean (coefficient of variation). Low spread is more AI-like, so this
  one gets flipped.
- **Type–token ratio:** unique words over total words, computed over
  fixed-size windows and averaged so long and short texts are comparable.
  Low variety is more AI-like, so this one is flipped too.
- **Punctuation variety:** density of the expressive marks (`; : — ( ) ! ?`)
  per sentence, not full stops. Low variety is more AI-like, flipped.

Each measure is clamped onto 0–1 and the three are averaged, so the result
points the same way as signal one: **higher means more likely AI**.

**Why it might differ between human and AI writing.** "Most likely next word"
produces prose that is even on average: mid-length sentences, a narrow band
of vocabulary, tidy punctuation. Human writing is lumpier. A three-word
sentence sits next to a forty-word one, words get repeated or swapped on a
whim, and dashes and asides come and go.

**What it can't see.** Meaning. Anything that changes the shape without
changing the substance moves it, and that is cheap to do on purpose:
- adding typos (new "unique" words raise type–token ratio);
- chopping or merging sentences;
- sprinkling dashes and semicolons;
- pasting in a quotation;
- prompting the model to "vary sentence length".

It also can't tell a human who writes evenly from a machine. Technical writing,
legal writing, a plain-style essay and a non-native writer's careful
sentences all look uniform. On short texts (a few sentences) all three
measures are mostly noise.

**Where the blind spots overlap.** Both signals push the same person toward
"AI": the plain, careful writer. They are not independent witnesses for that
person. That is why §3 matters.

---

## 3. The false positive, traced

**The person.** A student writing in English as a second language submits a
220-word personal essay they wrote themselves. They use vocabulary they're
confident with: short declarative sentences, *important*, *because*, *very*
repeated, almost no punctuation beyond full stops and commas.

**Through the service:**

| Step | What happens to them | Expected number |
|---|---|---|
| 2 Validation | Passes: 220 words, has a `creator_id` | — |
| 3 Model signal | Common words and plain syntax mean low perplexity, around 20 | `1/(1+(20/45)^1.6)` ≈ **0.79** |
| 4 Style signal | Even sentence lengths, repeated words, few expressive marks | ≈ **0.65–0.75** |
| 5 Combine (placeholder 0.5/0.5 average) | Both signals lean the same wrong way | ≈ **0.72–0.77** |
| 6 Label (placeholder `AI_THRESHOLD = 0.65`) | Lands above the AI threshold | `guess: "ai"` |

These numbers are predictions from the formula in `detector.py` and from how
I plan to build the style measures. Milestone 4 checks them by running a
plainly written human paragraph alongside the calibration inputs.

**What the label says to them.** With the placeholder thresholds it says, in
effect, "this was written by AI". That is a wrong accusation, made with full
confidence, against someone who has the least room to argue back. **This is
the outcome the thresholds exist to prevent.**

**What they can do about it.** The response gives them a `content_id`. They
`POST /appeal` with that id and their reasoning (e.g. "I wrote this myself,
here is my draft history"). The service checks the id exists, logs the
appeal next to the original decision, moves the item to `under_review`, and
tells them a person will look at it. Nothing is automatically re-scored. The
appeal is a route to a human, not a second roll of the dice.

**What this decides for later milestones (provisional, confirmed in
Milestones 4–5):**
- **Thresholds.** "High-confidence AI" has to sit *above* where plain human
  writing lands, not at 0.65. Expect `AI_THRESHOLD` around 0.80 and a wide
  "unsure" band. That costs us: more AI text lands in "unsure" instead of
  being caught. That is the trade I'm choosing, because a missed detection
  costs the site a little and a false accusation costs this person a lot.
- **Combining rule.** Because both blind spots point at the same person, a
  plain average double-counts them. The rule should not give "AI" on one
  signal alone. When the signals split widely, the result should land in
  "unsure".
- **Labels.** No label states AI authorship as fact. The "AI" label says
  *patterns often seen in AI-generated text*, says it's an automated estimate,
  and tells the reader they can appeal and how. The "unsure" label must not
  read as an accusation at all.

---

## 4. Endpoint contracts

All bodies are JSON. Every error response has the same shape:
`{"error": "<machine_code>", "message": "<sentence for a person>"}`.
Scores are floats rounded to 4 decimal places.

### `POST /submit`

**Request**

| Field | Type | Required | Rules |
|---|---|---|---|
| `text` | string | yes | After trimming whitespace: at least 20 words, at most 10,000 characters |
| `creator_id` | string | yes | Non-empty after trimming, at most 100 characters. Who submitted it; used for logging and (unit 8) rate limiting |

Extra fields are ignored.

**Response: `200 OK`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string (UUID4) | The id of this decision. Needed for `/appeal` |
| `creator_id` | string | Echoed back, trimmed |
| `guess` | string | Exactly one of `"human"`, `"unsure"`, `"ai"` |
| `confidence` | float 0–1 | The combined score from `scoring.combine_signals`. **Higher means more likely AI** (0 = confidently human, 1 = confidently AI). Same number as `combined_score` in the log |
| `label` | string | The full sentence a reader sees for this `guess` |
| `model_score` | float 0–1 | Signal one, higher means more AI-like |
| `style_score` | float 0–1 | Signal two, higher means more AI-like |
| `status` | string | Always `"decided"` on a fresh submission |

```json
{
  "content_id": "3f2c9a1e-5b7d-4e1a-9c3f-2a8b6d0e4f11",
  "creator_id": "student-42",
  "guess": "unsure",
  "confidence": 0.5873,
  "label": "<the unsure label text, written in Milestone 5>",
  "model_score": 0.7412,
  "style_score": 0.4334,
  "status": "decided"
}
```

**Errors.** Each is also written with `audit.log_rejection`, with `reason`
set to the error code.

| Status | `error` | When |
|---|---|---|
| 400 | `invalid_json` | Body missing, not JSON, or not a JSON object |
| 400 | `missing_text` | `text` absent, not a string, or empty/whitespace |
| 400 | `text_too_short` | Fewer than 20 words. Too little to judge, so we refuse instead of guessing |
| 400 | `text_too_long` | More than 10,000 characters |
| 400 | `missing_creator_id` | `creator_id` absent, not a string, empty, or over 100 characters |
| 429 | `rate_limited` | Unit 8, once limiting is on (response shape already in `app.py`) |
| 503 | `detector_unavailable` | The local model couldn't load (`DetectorUnavailable`) |

### `POST /appeal`

**Request**

| Field | Type | Required | Rules |
|---|---|---|---|
| `content_id` | string | yes | Must match a `content_id` from a previous `/submit` decision in the log |
| `reasoning` | string | yes | Non-empty after trimming, at most 2,000 characters. The writer's own words |

`creator_id` is **not** taken from the request. It's copied from the original
decision, so nobody can appeal under someone else's name.

**Response: `200 OK`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | The decision being appealed |
| `status` | string | Always `"under_review"` |
| `original_guess` | string | The `guess` being challenged |
| `message` | string | A confirmation to the writer that a person will review it and that the original label is not final |

```json
{
  "content_id": "3f2c9a1e-5b7d-4e1a-9c3f-2a8b6d0e4f11",
  "status": "under_review",
  "original_guess": "ai",
  "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement."
}
```

Side effect: one `audit.log_appeal` entry (`event: "appeal"`,
`status: "under_review"`, with the reasoning) appended after the original
decision. Nothing is deleted or rewritten.

**Errors**

| Status | `error` | When |
|---|---|---|
| 400 | `invalid_json` | Body missing, not JSON, or not a JSON object |
| 400 | `missing_content_id` | `content_id` absent, not a string, or empty |
| 400 | `missing_reasoning` | `reasoning` absent, not a string, empty, or over 2,000 characters |
| 404 | `unknown_content_id` | No decision with that id in the log. A typo fails loudly, not silently |
| 409 | `already_under_review` | An appeal for this id is already recorded |

### Read-back check

Could someone build against this without asking me a question? Going field
by field:
- Every input has a type, whether it's required, and limits.
- Every output field has a type and a direction. `confidence` is stated as
  "higher = AI", not "how sure".
- Every failure has a status code and a machine-readable `error`.
- The one remaining open question is the exact `label` wording and the final
  threshold numbers. Those belong to Milestones 4–5, and the contract only
  promises that `guess` is one of three fixed strings and `label` is a
  sentence.
