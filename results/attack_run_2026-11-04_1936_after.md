# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 19:36
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `ba702f95-4594-4603-a03d-98d2f78162db` | unsure | 0.500 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `53cd70f8-bbd8-4f52-aca5-0890441a5209` | unsure | 0.500 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `13663c23-378b-4adc-b1aa-992acfe80752` | unsure | 0.481 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `bed447ec-ab77-408d-97c0-9f948fa47596` | unsure | 0.749 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `1e5a734f-e569-4546-953a-fa963e7432b4` | human | 0.345 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `09273ba1-04dd-40ba-b7c5-b52143bb17c9` | unsure | 0.620 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `5cafa2d6-8ad6-4f53-9b90-f45dbd94c477` | unsure | 0.500 |  |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `dd4cc77b-de6b-4634-8b5a-c1c68b5a02a2` | unsure | 0.707 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c55aca60-a8d0-4be7-bec1-46aa5ca75649` | ai | 0.925 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `528ec85c-4daa-48c9-8d65-f68b036e8c35` | unsure | 0.685 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `7641ce5a-b480-4296-a83e-7e939c18adca` | unsure | 0.751 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `80d0104f-04af-4458-a632-83992f36527c` | unsure | 0.788 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `1bef3a79-adb7-4ba2-bb02-2969646b0287` | unsure | 0.694 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `325837c3-dfa1-4137-bc81-6ac41bdffa0e` | unsure | 0.741 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `7219abb6-6777-47bc-8b0a-c2e05065450a` | unsure | 0.723 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `108d3cd7-6c97-4f20-b092-6694c05ee5cd` | unsure | 0.500 |  |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `a0429a8a-36d1-4e62-aa5c-524e4ffdd862` | unsure | 0.410 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `0ea834da-72dc-4bf4-ba91-9ddd1e43b92b` | unsure | 0.137 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `d9ace8f4-59fd-4b59-991e-07e216da028c` | unsure | 0.575 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `82fac7b3-ca54-4e7e-9f50-8c2d37b6c1d1` | unsure | 0.512 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a2f45aea-d2bb-4598-8d16-5e38797cf942` | unsure | 0.563 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `7fcae5ed-9805-4ed3-9b1a-c642fa218318` | unsure | 0.649 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "ba702f95-4594-4603-a03d-98d2f78162db",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.1635,
  "style_score": 0.8762,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "53cd70f8-bbd8-4f52-aca5-0890441a5209",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5943,
  "style_score": 0.0,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "13663c23-378b-4adc-b1aa-992acfe80752",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4808,
  "model_score": 0.6662,
  "style_score": 0.2953,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "bed447ec-ab77-408d-97c0-9f948fa47596",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.7486,
  "model_score": 0.6114,
  "style_score": 0.8857,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "1e5a734f-e569-4546-953a-fa963e7432b4",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3447,
  "model_score": 0.3212,
  "style_score": 0.3682,
  "label": "We think this was most likely written by a person. Our automated checks didn't find the patterns we usually see in AI-generated writing.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "09273ba1-04dd-40ba-b7c5-b52143bb17c9",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.6197,
  "model_score": 0.5727,
  "style_score": 0.6667,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "5cafa2d6-8ad6-4f53-9b90-f45dbd94c477",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5862,
  "style_score": 0.0,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_EV08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "dd4cc77b-de6b-4634-8b5a-c1c68b5a02a2",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.7074,
  "model_score": 0.7042,
  "style_score": 0.7105,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c55aca60-a8d0-4be7-bec1-46aa5ca75649",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9249,
  "model_score": 0.9792,
  "style_score": 0.8707,
  "label": "Our automated checks found strong patterns that are common in AI-generated writing. This is an estimate, not proof: the checks can be wrong, especially about plain, straightforward writing. If you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "528ec85c-4daa-48c9-8d65-f68b036e8c35",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6854,
  "model_score": 0.6175,
  "style_score": 0.7533,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "7641ce5a-b480-4296-a83e-7e939c18adca",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7511,
  "model_score": 0.7387,
  "style_score": 0.7636,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "80d0104f-04af-4458-a632-83992f36527c",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7884,
  "model_score": 0.8051,
  "style_score": 0.7717,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "1bef3a79-adb7-4ba2-bb02-2969646b0287",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6942,
  "model_score": 0.8329,
  "style_score": 0.5555,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "325837c3-dfa1-4137-bc81-6ac41bdffa0e",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7413,
  "model_score": 0.8005,
  "style_score": 0.6821,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "7219abb6-6777-47bc-8b0a-c2e05065450a",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7232,
  "model_score": 0.8814,
  "style_score": 0.565,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "108d3cd7-6c97-4f20-b092-6694c05ee5cd",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8816,
  "style_score": 0.3333,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "a0429a8a-36d1-4e62-aa5c-524e4ffdd862",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4103,
  "model_score": 0.4625,
  "style_score": 0.3582,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "0ea834da-72dc-4bf4-ba91-9ddd1e43b92b",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.1367,
  "model_score": 0.2044,
  "style_score": 0.0691,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "d9ace8f4-59fd-4b59-991e-07e216da028c",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5745,
  "model_score": 0.5943,
  "style_score": 0.5546,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "82fac7b3-ca54-4e7e-9f50-8c2d37b6c1d1",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.512,
  "model_score": 0.4998,
  "style_score": 0.5241,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "a2f45aea-d2bb-4598-8d16-5e38797cf942",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5629,
  "model_score": 0.6401,
  "style_score": 0.4857,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "7fcae5ed-9805-4ed3-9b1a-c642fa218318",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.6492,
  "model_score": 0.5583,
  "style_score": 0.7401,
  "label": "We can't tell either way, so we're not making a call on this piece. It has some patterns that show up in both human and AI writing \u2014 and a lot of writing people do themselves lands here, especially clear, straightforward writing. Nothing about this result says you did anything wrong. If you'd like a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
