# Criterion 5 — appeals — regression

- Produced by: `run_appeals.py::run_trial`
- Service: `app.py::submit`, `app.py::appeal`, `app.py::get_log`

**Trial 1**: 5/5 real appeals passed, made-up id returned 404

```json
{
  "appeals": [
    {
      "submit_status": 200,
      "content_id": "ceb780a7-c7cc-4dd1-855b-e6b342c1149e",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "ceb780a7-c7cc-4dd1-855b-e6b342c1149e",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "ai",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "39bd9544-b596-48dc-90bd-48514b8a507e",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "39bd9544-b596-48dc-90bd-48514b8a507e",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "ai",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "6ca1d99b-5c9e-4501-b6b2-6b502010dc13",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "6ca1d99b-5c9e-4501-b6b2-6b502010dc13",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "human",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "65f8584e-f98e-4527-be6a-7ecc2a7e3c52",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "65f8584e-f98e-4527-be6a-7ecc2a7e3c52",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "human",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "baa56c0a-9a78-46ab-a13d-384953aeeb62",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "baa56c0a-9a78-46ab-a13d-384953aeeb62",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "unsure",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    }
  ],
  "fake_id": {
    "status": 404,
    "response": {
      "error": "unknown_content_id",
      "message": "We couldn't find a submission with that content_id. Check it was copied exactly."
    }
  },
  "real_passed": 5,
  "fake_404": true
}
```

**Trial 2**: 5/5 real appeals passed, made-up id returned 404

```json
{
  "appeals": [
    {
      "submit_status": 200,
      "content_id": "3e056155-f126-4b65-83ef-4b4b29c047f4",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "3e056155-f126-4b65-83ef-4b4b29c047f4",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "ai",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "65395b84-94ac-4608-9d67-86cacc413224",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "65395b84-94ac-4608-9d67-86cacc413224",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "ai",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "a38c523a-40c8-439c-b982-e3f2b1ce8665",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "a38c523a-40c8-439c-b982-e3f2b1ce8665",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "human",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "90e52a50-1b8f-4152-b7f6-e994ea6fa985",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "90e52a50-1b8f-4152-b7f6-e994ea6fa985",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "human",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "f144bbfa-48fc-4b0f-a24e-15678e69a498",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "f144bbfa-48fc-4b0f-a24e-15678e69a498",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "unsure",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    }
  ],
  "fake_id": {
    "status": 404,
    "response": {
      "error": "unknown_content_id",
      "message": "We couldn't find a submission with that content_id. Check it was copied exactly."
    }
  },
  "real_passed": 5,
  "fake_404": true
}
```

**Trial 3**: 5/5 real appeals passed, made-up id returned 404

```json
{
  "appeals": [
    {
      "submit_status": 200,
      "content_id": "f1fe3448-b722-490b-bfc7-d7006f78f5d7",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "f1fe3448-b722-490b-bfc7-d7006f78f5d7",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "ai",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "d6199a1e-5bdc-4136-8521-85097b270893",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "d6199a1e-5bdc-4136-8521-85097b270893",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "ai",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "6d81b49e-abd6-46aa-ad57-c359676ab735",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "6d81b49e-abd6-46aa-ad57-c359676ab735",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "human",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "70c2834c-f066-4db5-bd2f-fe0e91686470",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "70c2834c-f066-4db5-bd2f-fe0e91686470",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "human",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    },
    {
      "submit_status": 200,
      "content_id": "61a6ec3f-a604-4c9c-ad7b-c28f1e84e4e9",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "61a6ec3f-a604-4c9c-ad7b-c28f1e84e4e9",
        "message": "Thanks — your appeal has been recorded and a person will review this decision. Until then, the automated label is not a final judgement.",
        "original_guess": "unsure",
        "status": "under_review"
      },
      "log_sequence": [
        "decided",
        "appeal"
      ],
      "passed": true
    }
  ],
  "fake_id": {
    "status": 404,
    "response": {
      "error": "unknown_content_id",
      "message": "We couldn't find a submission with that content_id. Check it was copied exactly."
    }
  },
  "real_passed": 5,
  "fake_404": true
}
```
