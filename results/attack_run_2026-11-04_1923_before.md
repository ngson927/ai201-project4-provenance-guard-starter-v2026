# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 19:23
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `0e6126b4-d15b-48a3-a231-426207f83b23` | unsure | 0.500 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `598e8d75-20b0-465a-9232-4b490717479a` | unsure | 0.500 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `58e4b88e-a3e1-43f3-9622-897bdc526ea6` | unsure | 0.481 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `ea07f4ef-3e32-4e6a-b787-81be77a5e9d5` | unsure | 0.749 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `fb3dbf91-cf7f-4792-915f-ab3f8bce2c80` | human | 0.345 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `feba84f4-8c45-493d-b9b9-431dde7fb405` | unsure | 0.620 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `4399d961-2677-4418-b591-92de4265ffce` | unsure | 0.500 | BROKE |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `175b227c-06f6-4ff7-a4b4-3e320c7f14f0` | unsure | 0.707 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `47d621ac-77f2-4cc6-a643-97719dd9dcd0` | ai | 0.925 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `390440a4-03af-46c8-9898-ed7b09e1c89a` | unsure | 0.685 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `0463b6b9-e6ab-4b18-bbed-696b528cf345` | unsure | 0.751 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c7e2c7b9-e363-47bc-9038-942f4a4595f6` | unsure | 0.788 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `f7c776f6-3b59-4f96-b30b-b5d552b064c1` | unsure | 0.694 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `a2aa0417-442b-49dd-9764-1c3df32728c0` | unsure | 0.741 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `cd61c57d-aae8-4d1e-a028-07fcc297b8f2` | unsure | 0.723 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `95420f90-95b7-4108-9057-993ded2acd27` | unsure | 0.500 | HELD |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c9afd35b-e8eb-4009-8f97-3b01776bbaca` | human | 0.410 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `22da459d-ce4f-4bf5-8862-f956eb7fb6f1` | human | 0.137 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `14e39139-7593-44e0-a17b-d6085260ee81` | unsure | 0.575 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c1cd70cd-6d0e-42ac-ba49-7eabb189190b` | unsure | 0.512 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `ecee9a44-5190-4883-9f8c-624626f1c813` | unsure | 0.563 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `bc23de3d-f04b-406e-9a2e-d4ae4cbb770d` | unsure | 0.649 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

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
  "content_id": "0e6126b4-d15b-48a3-a231-426207f83b23",
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
  "content_id": "598e8d75-20b0-465a-9232-4b490717479a",
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
  "content_id": "58e4b88e-a3e1-43f3-9622-897bdc526ea6",
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
  "content_id": "ea07f4ef-3e32-4e6a-b787-81be77a5e9d5",
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
  "content_id": "fb3dbf91-cf7f-4792-915f-ab3f8bce2c80",
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
  "content_id": "feba84f4-8c45-493d-b9b9-431dde7fb405",
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
  "content_id": "4399d961-2677-4418-b591-92de4265ffce",
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
  "content_id": "175b227c-06f6-4ff7-a4b4-3e320c7f14f0",
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
  "content_id": "47d621ac-77f2-4cc6-a643-97719dd9dcd0",
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
  "content_id": "390440a4-03af-46c8-9898-ed7b09e1c89a",
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
  "content_id": "0463b6b9-e6ab-4b18-bbed-696b528cf345",
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
  "content_id": "c7e2c7b9-e363-47bc-9038-942f4a4595f6",
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
  "content_id": "f7c776f6-3b59-4f96-b30b-b5d552b064c1",
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
  "content_id": "a2aa0417-442b-49dd-9764-1c3df32728c0",
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
  "content_id": "cd61c57d-aae8-4d1e-a028-07fcc297b8f2",
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
  "content_id": "95420f90-95b7-4108-9057-993ded2acd27",
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
  "content_id": "c9afd35b-e8eb-4009-8f97-3b01776bbaca",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.4103,
  "model_score": 0.4625,
  "style_score": 0.3582,
  "label": "We think this was most likely written by a person. Our automated checks didn't find the patterns we usually see in AI-generated writing.",
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
  "content_id": "22da459d-ce4f-4bf5-8862-f956eb7fb6f1",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1367,
  "model_score": 0.2044,
  "style_score": 0.0691,
  "label": "We think this was most likely written by a person. Our automated checks didn't find the patterns we usually see in AI-generated writing.",
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
  "content_id": "14e39139-7593-44e0-a17b-d6085260ee81",
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
  "content_id": "c1cd70cd-6d0e-42ac-ba49-7eabb189190b",
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
  "content_id": "ecee9a44-5190-4883-9f8c-624626f1c813",
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
  "content_id": "bc23de3d-f04b-406e-9a2e-d4ae4cbb770d",
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
