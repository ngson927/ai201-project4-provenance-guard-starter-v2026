# Criterion 5 — appeals — before

- Produced by: `run_appeals.py::run_trial`
- Service: `app.py::submit`, `app.py::appeal`, `app.py::get_log`

**Trial 1**: 5/5 real appeals passed, made-up id returned 404

```json
{
  "appeals": [
    {
      "submit_status": 200,
      "content_id": "ac4d5966-bc8e-425c-ae4e-fca5bef2ad91",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "ac4d5966-bc8e-425c-ae4e-fca5bef2ad91",
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
      "content_id": "2b95b808-ab40-4b9b-94b4-bf8709ff6554",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "2b95b808-ab40-4b9b-94b4-bf8709ff6554",
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
      "content_id": "1fe83360-2a1b-43fb-b439-671510a2166c",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "1fe83360-2a1b-43fb-b439-671510a2166c",
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
      "content_id": "5cc6a8d6-7a0a-41c0-9231-fa8c5339c59a",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "5cc6a8d6-7a0a-41c0-9231-fa8c5339c59a",
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
      "content_id": "32d13cf8-86b5-4c52-b6d6-01b1da82e92f",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "32d13cf8-86b5-4c52-b6d6-01b1da82e92f",
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
      "content_id": "6b9f59e3-5ef7-41c5-a9e7-19279f2083c8",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "6b9f59e3-5ef7-41c5-a9e7-19279f2083c8",
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
      "content_id": "b9e9097a-db71-4873-a2e7-c8885725a0d6",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "b9e9097a-db71-4873-a2e7-c8885725a0d6",
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
      "content_id": "dccae6db-18da-4704-8e58-0dbfda025864",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "dccae6db-18da-4704-8e58-0dbfda025864",
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
      "content_id": "6b9511f1-15a6-4b0a-af24-db66b5c9830e",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "6b9511f1-15a6-4b0a-af24-db66b5c9830e",
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
      "content_id": "c867ff54-e92c-4404-9fc1-159d567c58c1",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "c867ff54-e92c-4404-9fc1-159d567c58c1",
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
      "content_id": "85fd2dd9-3516-48b0-9c2f-491abbed42cc",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "85fd2dd9-3516-48b0-9c2f-491abbed42cc",
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
      "content_id": "bed1ee0b-210c-4456-a865-032147ad2e58",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "bed1ee0b-210c-4456-a865-032147ad2e58",
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
      "content_id": "0ae088d4-41d0-4720-82b9-6e879dd44830",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "0ae088d4-41d0-4720-82b9-6e879dd44830",
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
      "content_id": "e3b6d498-cb47-40ee-ac71-6374db5b983e",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "e3b6d498-cb47-40ee-ac71-6374db5b983e",
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
      "content_id": "a24bb9e3-820b-4c83-a311-b6e583574661",
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "a24bb9e3-820b-4c83-a311-b6e583574661",
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
