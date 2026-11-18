# Extension criteria — unit 9, shape B (harden against failure)

Written **before** building anything for unit 9. Unit 8's `criteria.md` is
untouched; these are new criteria for the extension.

Each one is about the **bad path**. That means what happens when the service
is starting, crashing, missing its model, or unable to write its log. Each one
runs against the real run path (gunicorn, via `./serve.sh`), not Flask's
development server, and each runs **three trials**, each from a fresh start.
A target has to hold in all three.

---

## E1. A request sent during a cold start waits; it doesn't fail

Start the service with `./serve.sh`. Starting within 1 second, send one valid
`POST /submit` per second for 30 seconds (30 requests, a different
`creator_id` on each). **30 of 30 return HTTP 200. Zero return a 5xx, and zero
drop the connection.**

**Why this target:** a cold start is the slowest moment this service has.
Loading GPT-2 takes 10–20 seconds, and gunicorn kills any worker that stays
silent past its timeout. A writer who submits as the service comes up should
wait a few seconds longer, not get an error page. 30 of 30 because one
dropped request during startup is the bug.

---

## E2. A crashed worker comes back on its own

With the service warm, kill its worker with `kill -9`. Starting at once, send
one valid `POST /submit` per second. **A 200 comes back within 60 seconds of
the kill, with no manual action. The gunicorn log records that the worker
died.**

**Why this target:** a laptop service with nobody watching it has to recover
by itself, or it's down until someone notices. 60 seconds is a cold start
(E1) plus margin. A worker restart that takes longer means the model is being
loaded somewhere it shouldn't be.

---

## E3. A missing model is a clear 503, never a crash

Start the service with a model that isn't there (`AI201_DETECTOR_MODEL` set
to a name that doesn't exist, Hugging Face set to offline). Send 5 valid
`POST /submit`. **5 of 5 return HTTP 503 with JSON
`"error": "detector_unavailable"`. `/ping` and `/health` still return 200,
with `/health` reporting the detector as not loaded. 5 `rejected` entries
appear in the audit log with that reason.**

**Why this target:** if the model fails to load at startup, the worker must
not crash during boot. Gunicorn gives up on a worker that can't boot and the
whole service exits. A service that's up and says plainly "the checker isn't
available" can be diagnosed; a service that's gone can't.

---

## E4. A decision that can't be logged is not handed out

Start the service with its audit log file made read-only. Send 5 valid
`POST /submit`. **5 of 5 return HTTP 503 with JSON
`"error": "audit_unavailable"` and no `content_id` in the body. Zero return a
500, and `/ping` still answers.**

**Why this target:** `/appeal` finds a submission through the audit log. A
`content_id` handed out without a log entry is an appeal that will come back
404: a writer told they can ask for a review, who can't. Refusing is better
than an accusation nobody can challenge.

---

## E5. Every request leaves an operational trace, and the numbers match

Each trial sends the same mixed traffic, 25 requests:
- a 15-request flood from one `creator_id`;
- 5 malformed bodies;
- 3 valid submissions;
- 2 appeals.

**The request log gets exactly 25 new lines,** each with path, status and
latency. **`GET /metrics` reports status counts that match exactly** what the
client received. **The flood comes back as exactly 5 × 200 then 10 × 429**
under gunicorn.

**Why this target:** the audit log records *decisions*. It can't show a
request that died before a decision was made, or how long anything took. The
operational numbers only mean something if every request is in them, so the
count must match exactly. A 429 that leaves no trace looks like a quiet
afternoon. The flood half checks the deployed configuration: limits stored in
memory aren't shared between gunicorn workers, so a second worker would
quietly double the limit.
