# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1. Real writers, including plain ones, are not called AI

Submit the 10 texts in the `my own writing` scenario in `scenarios.py`
(`python run_eval.py` does this, three trials). They are pieces I wrote
myself, and the first 3 are written plainly on purpose: short sentences,
everyday words. Read the `guess` field of each response. **At most 1 of the
10 is `"ai"`, and none of the first 3 are**, in every one of the three
trials.

**Why this target:** On a writing site a wrong accusation costs the writer far
more than a missed detection costs the site. Plain writing is exactly where
both my signals are blind. On calibration a plain paragraph scored 0.85 on the
model signal and 0.807 combined, only 0.04 under my 0.85 AI threshold
(DESIGN.md §3, README → Calibration). So I name plain writing separately
rather than let it hide inside an average. If those pieces get flagged, the
threshold is wrong, whatever the overall number says.

---

## 2. All three labels are reachable

Submit the 9 texts in the `clearly AI`, `clearly human` and `borderline`
scenarios in `scenarios.py`:
- **clearly AI:** 3 unedited model essays;
- **clearly human:** Twain, Melville and Thoreau, all published before
  language models existed;
- **borderline:** lightly-edited AI, AI with deliberately varied rhythm, and
  Mill.

Read each response's `guess`. **Each of `"human"`, `"unsure"` and `"ai"`
appears at least once, in every one of the three trials.**

**Why this target:** My unsure band is wide (above 0.42, below 0.85), and "AI"
needs both signals at about 0.70 or more. That makes the two outer labels
easy to squeeze out. A service that can only say "unsure" isn't a detector.
Requiring all three in *every* trial means one lucky run can't hide a label
that is only barely reachable.

---

## 3. Clearly-AI and clearly-human text are far apart

Submit the 3 `clearly AI` and 3 `clearly human` texts in `scenarios.py` and
read each response's `confidence`. **The mean of the AI three is at least
0.30 higher than the mean of the human three, and the highest human score is
below the lowest AI score**, in every one of the three trials.

**Why this target:** If clear cases from each side don't sit well apart, no
placement of my thresholds (0.42 and 0.85) can separate them. A gap of 0.30
was the width of the unsure band I planned in Milestone 1. The "no overlap"
half catches a mean that looks fine while one human text sits among the AI
ones. That is exactly what the plain writer does to the model signal.

---

## 4. Bad input gets a clear refusal, never a crash

Send the 5 bodies in the `bad input` scenario in `scenarios.py`:
- empty `text`;
- no `text` field;
- `text: null`;
- 50,000 words of text;
- no `creator_id`;

**All 5 return HTTP 400 with a JSON body containing an `error` code, 0 return
a 500**, and `GET /log?limit=5` afterwards shows **5 entries with
`"status": "rejected"`**.

**Why this target:** A crash on malformed input is one of the most common real
failures, and unit 8's attack set will send exactly this. A 500 tells the
caller nothing. A refusal that leaves no log entry is an attack I'd never see.
Refusing too-short or enormous text is better than guessing at it.

---

## 5. Every appeal changes status and is recorded

Tested by hand with curl, since it needs the `content_id` a submission
returns:
1. Submit any 5 texts to `POST /submit`.
2. `POST /appeal` each returned `content_id` with any non-empty `reasoning`.
3. Then `POST /appeal` once with `"content_id": "not-a-real-id"`.

**5 of 5 real appeals return HTTP 200 with `"status": "under_review"`.**
`GET /log` shows, for each of the 5 ids, **the `"decided"` entry followed by
an `"event": "appeal"` entry**. **The made-up id returns 404**, not 200.

**Why this target:** The appeal is the only thing between a wrong accusation
and nothing at all, so "usually works" isn't good enough. It has to be 5 of 5.
The made-up id check matters because an appeal that silently "succeeds"
against nothing looks like it worked to the writer, and nobody ever reviews
it.

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
