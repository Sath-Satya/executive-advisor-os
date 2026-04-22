<!-- TEMPLATE: bootcamp-lesson
     CATEGORY: Training / Bootcamp
     USE WHEN: delivering a single lesson in a bootcamp or intensive program
     SLIDE COUNT: 10
     PALETTE: Light clean dev
     RENDER: marp --pptx 35-bootcamp-lesson.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&family=DM+Serif+Display&family=DM+Mono&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #ffffff;
    color: #1c1a18;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', serif;
    color: #0e1b2e;
    font-size: 2.1em;
    letter-spacing: -0.4px;
    margin-bottom: 0.2em;
  }
  h2 { color: #0e1b2e; font-size: 1.3em; font-weight: 600; margin-bottom: 0.5em; }
  h3 { color: #3b9eff; font-size: 1em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.35em; }
  strong { color: #0e1b2e; }
  em { color: #556677; font-style: normal; font-size: 0.87em; }
  code { font-family: 'DM Mono', monospace; background: #f0f4f8; color: #0e1b2e; padding: 0.15em 0.45em; border-radius: 3px; font-size: 0.88em; }
  pre { background: #f0f4f8; border-left: 4px solid #3b9eff; border-radius: 4px; padding: 1em 1.2em; font-size: 0.85em; }
  ul { margin-top: 0.5em; }
  li { margin-bottom: 0.4em; line-height: 1.6; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #8899ac; }
  section.lead h1 { font-size: 2.6em; }
  section.lead p { font-size: 1.1em; color: #556677; margin-top: 0.4em; }
  section.demo { background: #f8faff; border-top: 3px solid #3b9eff; }
  section.guided { background: #f0f7ff; border-left: 5px solid #3b9eff; }
  section.independent { background: #fff; border: 2px solid #3b9eff; border-radius: 8px; }
  section.mistakes { background: #fff8f0; border-left: 5px solid #f0a050; }
  .lesson-meta { font-family: 'DM Mono', monospace; font-size: 0.8em; color: #8899ac; margin-top: 0.4em; }
  .time-badge {
    display: inline-block;
    background: #3b9eff;
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 0.78em;
    padding: 0.2em 0.7em;
    border-radius: 3px;
    margin-bottom: 0.6em;
  }
---

<!-- _class: lead -->

# Python API Design — Lesson 4

**SponAItech Dev Bootcamp** &nbsp;|&nbsp; Module 2 — FastAPI Foundations

<p class="lesson-meta">Lesson 4 of 6 &nbsp;|&nbsp; 60 min &nbsp;|&nbsp; v1.1 &nbsp;|&nbsp; April 2025</p>

<!--
SPEAKER NOTES — SLIDE 1 (Title)
This lesson is Lesson 4 of 6 in the FastAPI Foundations module. Participants should have completed Lessons 1–3, which covered: Python type hints (L1), Pydantic models (L2), and dependency injection basics (L3). If anyone has not completed those lessons, direct them to the recordings before this session.

Today's lesson covers API design principles — how to structure routes, name resources, handle errors consistently, and design for the consumer of the API, not the implementor. These are judgment skills, not just syntax skills.

The lesson is structured in five phases: Prior Knowledge check (5 min), Concept (15 min), Demo (10 min), Guided Practice (15 min), Independent Practice (10 min), then wrap (5 min). Hold to timing — the independent practice phase is where the real learning happens and it is the phase most often cut when sessions run long.

Energy check: if it is after lunch, do a 2-minute physical activity before starting. Stand up, shake out hands, or do a 30-second discussion with the person next to them on "what is the worst API you have ever used?" The last option is always high energy and directly relevant to today's topic.
-->

---

## Prior Knowledge Check

**Before we start — 60 seconds, no looking:**

Write down (or say aloud) the answers to:

1. What is the purpose of a Pydantic `BaseModel` in a FastAPI route handler?
2. What HTTP status code means "the resource was created successfully"?
3. What does `Depends()` do in a FastAPI path function signature?

*We will revisit these in context during the lesson*

<!--
SPEAKER NOTES — SLIDE 2 (Prior Knowledge Check)
Run this as a genuine retrieval exercise — not a quiz with scoring, but an activation of prior knowledge before new content is introduced. Retrieval at the start of a lesson primes the memory pathways that the new content will connect to.

Answers to have ready:
1. Pydantic BaseModel: provides typed data validation, automatic serialization/deserialization, and OpenAPI schema generation for request and response bodies.
2. HTTP 201 Created: indicates the resource was successfully created. 200 OK is for retrieval or general success.
3. Depends(): declares a dependency — FastAPI will resolve it, call it, and inject the result into the path function. Used for authentication, DB sessions, configuration, etc.

If participants struggle with Q3, make a note — dependency injection will be used throughout today's demo and they may need a quick recap before diving into the code. Two minutes of Q3 review now saves 10 minutes of confusion during the guided practice.

Do not dwell on this slide. 60 seconds to answer, 90 seconds to discuss. Then move on. The purpose is activation, not assessment.
-->

---

## Concept — REST API Design Principles

Three rules that separate usable APIs from painful ones:

- **Resource-oriented URLs** — nouns, not verbs: `/api/v1/claims` not `/getClaim`
- **Consistent error contracts** — every error returns `{ "detail": "...", "code": "..." }`
- **Version in the path** — `/api/v1/...` from day one; breaking changes go in v2

**What makes an API consumer-friendly:**

The consumer should not need to read your source code to understand how to use your API.

<!--
SPEAKER NOTES — SLIDE 3 (Concept)
The three rules are opinionated and intentionally simple. In a bootcamp context, simplicity and consistency beat nuance. Once participants have internalized these rules, they can develop their own exceptions with experience.

Resource-oriented URLs: the verb in a URL is a design smell. REST semantics use HTTP methods (GET, POST, PUT, PATCH, DELETE) as the verbs — the URL should describe the resource, not the action. Common violations: `/getUsers`, `/createOrder`, `/deleteAccount`. Correct: `GET /users`, `POST /orders`, `DELETE /accounts/{id}`.

Consistent error contracts: this is the rule most frequently violated in practice. When an API returns a plain string for some errors, a JSON object for others, and an HTML error page for a third category, the consumer must write three different error handlers. Consistent structure means one error handler. The structure `{ "detail": "...", "code": "..." }` matches FastAPI's default `HTTPException` format — which is a deliberate choice in this lesson.

Versioning from day one: adding version numbers to an existing unversioned API is a breaking change. Starting with `/api/v1/` costs nothing and prevents future pain. When v2 is needed, v1 continues to work for existing consumers.

The consumer-friendly test: after building any endpoint, ask "Can someone call this without reading my code?" If the answer is no, the API needs work.
-->

---

<!-- _class: demo -->

## Demo — Building a Versioned Claims Endpoint

<div class="time-badge">10 min live demo</div>

**What we are building:**

```
GET  /api/v1/claims          → list claims (paginated)
POST /api/v1/claims          → create a new claim
GET  /api/v1/claims/{id}     → get one claim by ID
PUT  /api/v1/claims/{id}     → update a claim
DELETE /api/v1/claims/{id}   → delete a claim
```

**Standard error response:**

```json
{ "detail": "Claim not found", "code": "CLAIM_NOT_FOUND" }
```

*Follow along in `lesson-04/starter/main.py`*

<!--
SPEAKER NOTES — SLIDE 4 (Demo)
Open VS Code before this slide and have `lesson-04/starter/main.py` ready. The file should contain the router and model scaffolding but no route handlers — participants will fill those in during guided practice.

Demo sequence (10 minutes):
1. Show the empty router (1 min) — explain the `APIRouter` with prefix `/api/v1/claims`
2. Implement `GET /claims` with pagination (3 min) — `skip: int = 0, limit: int = 20` as query params
3. Implement `POST /claims` with a `ClaimCreate` Pydantic model (3 min) — return 201 with the created resource
4. Implement the `HTTPException` pattern for 404 (2 min) — raise `HTTPException(status_code=404, detail={"detail": "Claim not found", "code": "CLAIM_NOT_FOUND"})`
5. Run the server and show the OpenAPI docs at `/docs` (1 min)

Talk while you type. Do not go silent during the demo — narrate every decision. "I am using `skip` and `limit` instead of `page` because it is easier to implement cursor-based pagination later without a breaking change."

If you make a mistake during the demo: do not panic. Leave it in, debug it live, and name what you are doing. "I see a 422 — that is FastAPI telling me the request body does not match my Pydantic model. Let me check the field types." This is more instructive than a clean demo.
-->

---

<!-- _class: guided -->

## Guided Practice — Complete the Router

<div class="time-badge">15 min — together</div>

**Your task — in `lesson-04/guided/main.py`:**

Add the two missing handlers:

1. `PUT /api/v1/claims/{claim_id}` — accepts a `ClaimUpdate` model, returns updated claim or 404
2. `DELETE /api/v1/claims/{claim_id}` — deletes the claim, returns `204 No Content`

**Constraints:**
- Use the same error contract as the demo (`detail` + `code` fields)
- Return `204` with no body on successful delete — do not return `200` with a message

*Facilitator walks the room — raise your hand if stuck*

<!--
SPEAKER NOTES — SLIDE 5 (Guided Practice)
Start the timer when you show this slide. 15 minutes is enough time for participants who followed the demo. For participants who fell behind during the demo, they should focus on the PUT handler first and skip DELETE if time runs low — PUT is the more complex pattern.

Walk the room actively. Do not stand at the front. Look over shoulders, ask "what is the error message?" rather than "what is wrong?" — guide participants to diagnose before you explain.

Common issues you will see:
1. Returning 200 on DELETE instead of 204. Remind them: 204 means "success, no content." The response body must be empty. In FastAPI: `return Response(status_code=204)` — not `return None` which defaults to a 200 with null body.
2. 422 Unprocessable Entity on the PUT request. This means the request body does not match the `ClaimUpdate` schema. Check whether all fields are optional (they should be for an update model).
3. Forgetting the `response_model` parameter on the route decorator. Without it, FastAPI does not validate the response shape.

At 10 minutes: do a check-in. "Raise your hand if you have PUT working." "Raise your hand if you are stuck on 204." This tells you where to focus the last 5 minutes.

At 15 minutes: stop. Show the solution on screen. Do not rush through it — explain one key decision. Today's key decision: why `204 No Content` and not `200 OK with {"deleted": true}`? Because 204 is self-documenting. The status code carries the semantics — no body needed.
-->

---

## Independent Practice — Design the Error Layer

<div class="time-badge">10 min — solo</div>

**In `lesson-04/independent/errors.py`:**

Create a custom exception handler that:

1. Catches all `HTTPException` instances
2. Converts the detail to the standard contract: `{ "detail": "...", "code": "..." }`
3. Registers the handler with the FastAPI app via `@app.exception_handler(HTTPException)`

**Bonus:** handle `RequestValidationError` and return `{ "detail": "validation error", "code": "VALIDATION_ERROR", "fields": [...] }`

*Do not look at the guided solution — attempt this from memory first*

<!--
SPEAKER NOTES — SLIDE 6 (Independent Practice)
Independent practice is where the real learning happens. The guided phase was scaffolded — this phase removes the scaffold. The "do not look at the guided solution" instruction is a retrieval practice trigger. Participants who attempt from memory and struggle will retain the solution better than participants who look it up immediately.

Set the expectation before the timer: "You will not finish both tasks in 10 minutes. The bonus is genuinely bonus. Focus on completing task 1 and 2 well."

During independent practice: do not help unless asked. Resist the urge to walk around and offer unsolicited hints. The struggle is the learning. The only help you should offer in the first 5 minutes is pointing to the FastAPI documentation for `exception_handler` if someone cannot find the API surface.

At 8 minutes: give a 2-minute warning.

At 10 minutes: stop everyone. Show the complete solution. Ask: "How many of you got a different result than the solution?" Raise hands. "Let us look at the difference." Diff-based learning — comparing what you wrote to the solution — is one of the highest-value activities in a bootcamp.

If many participants hit the same issue: add it to your facilitator notes for next iteration. This is lesson-level feedback that improves the next cohort.
-->

---

<!-- _class: mistakes -->

## Common Mistakes — Lesson 4

**1. Verbs in URLs** — `/getClaim` is an anti-pattern; use `GET /claims/{id}`

**2. Inconsistent status codes** — returning `200` for creation; use `201 Created`

**3. Empty error bodies** — returning `raise HTTPException(404)` with no `detail`; always include detail

**4. No versioning** — `/claims` will break consumers when you need `/v2/claims`; version from day one

**5. Returning deleted resource** — `DELETE` should return `204`, not the deleted object

<!--
SPEAKER NOTES — SLIDE 7 (Common Mistakes)
This slide exists to make the most common errors explicit and memorable. Research on error-based learning (Metcalfe & Kornell, 2007) shows that explicitly naming errors — especially errors the learner just made during practice — significantly improves retention of the correct pattern.

Deliver this slide with a light touch. These are not criticisms — they are patterns that every developer encounters. "I have written all five of these mistakes myself. Probably this week."

Mistake 3 (empty error bodies) is particularly important for API consumers: an empty 404 body forces the consumer to hard-code meaning into the status code. A 404 on `/claims/{id}` could mean the claim does not exist, the user does not have access, or the endpoint is wrong. The detail string disambiguates.

Mistake 4 (no versioning) is the most painful to fix retroactively. The moment you remove or rename a field on an unversioned endpoint, every consumer breaks simultaneously with no migration path. The cost of adding `/v1/` up front is zero characters plus a prefix.

Ask participants: "Which of these did you make during practice today?" This is not a shaming exercise — it normalizes the mistakes and anchors the memory to their personal experience.
-->

---

## Recap — Lesson 4

**What you built:**

- ✓ A fully versioned REST router at `/api/v1/claims`
- ✓ All five CRUD handlers with correct status codes
- ✓ A consistent error contract (`detail` + `code`)
- ✓ A global exception handler that enforces the contract

**The principle that unifies it all:**

*Design for the consumer — they should not need your source code to use your API.*

<!--
SPEAKER NOTES — SLIDE 8 (Recap)
Read through the recap at a deliberate pace. Four items. Four things participants built in this lesson. Make it concrete — point to the files they modified.

The unifying principle at the bottom is the "one thing to remember" from this lesson. If a participant can only retain one idea, it is this: design for the consumer. Every specific decision in the lesson flows from this principle. Resource-oriented URLs are consumer-friendly. Consistent error contracts are consumer-friendly. Versioning is consumer-friendly. 204 on DELETE is consumer-friendly.

Ask the group: "If you had to teach Lesson 4 to someone in two sentences, what would you say?" Take one or two responses. This is a synthesis exercise that exposes whether the core principle landed. If the responses are about syntax ("use APIRouter and prefix"), prompt for the deeper principle. If they get to "design for the consumer," the lesson worked.

Time remaining: if you have 3+ minutes after the recap, do a rapid Q&A. "What questions came up during independent practice that we did not get to address?" This surfaces the genuine confusion points that will become the strongest learning artifacts.
-->

---

## Homework — Before Lesson 5

**Required (30 min):**

- ● Extend your `lesson-04/independent/errors.py` to handle `RequestValidationError`
- ● Read FastAPI documentation: "Response Model" — fastapi.tiangolo.com/tutorial/response-model
- ● Write one question about today's lesson that you could not answer on your own

**Optional (45 min additional):**

- ○ Add pagination metadata to the `GET /claims` response: `{ "items": [...], "total": 100, "skip": 0, "limit": 20 }`
- ○ Implement an `async` dependency that injects a fake DB session

*Submit your homework repo link before Lesson 5 starts*

<!--
SPEAKER NOTES — SLIDE 9 (Homework)
The homework is calibrated to 30 minutes for the required portion. Participants who do less than this will struggle in Lesson 5, which builds directly on today's error handling patterns.

The "write one question" homework item is non-negotiable. Questions that participants cannot answer on their own are the most valuable input to the facilitator. They tell you where the lesson failed to transfer, which topics need more coverage in Lesson 5, and which participants are actively engaging with the material.

Collect the questions before Lesson 5 starts (via Slack or a shared doc). Spend the first 5 minutes of Lesson 5 answering the two or three most common questions. This signals that homework is read and valued — which increases completion rates.

The optional pagination metadata task is a genuine extension that will come up in the real SponAItech codebase. It is not busywork. The structure `{ "items": [...], "total": N, "skip": N, "limit": N }` is the SponAItech standard for all paginated list responses. Participants who complete this optional task are ahead of the curve.

Submission logistics: replace the generic "homework repo link" with the specific GitHub repository and branch naming convention used in your cohort.
-->

---

<!-- _class: lead -->

## Next — Lesson 5 — Authentication with JWT

**What you will build:**

- FastAPI OAuth2PasswordBearer flow
- JWT token creation and validation
- Protected routes with `Depends(get_current_user)`

*Prerequisites: complete Lesson 4 homework before Lesson 5*

**SponAItech Dev Bootcamp** &nbsp;|&nbsp; `Module 2 · Lesson 5`

<!--
SPEAKER NOTES — SLIDE 10 (Next Lesson)
End on a forward look that creates anticipation. Authentication is one of the most practically important topics in the bootcamp — it is the skill participants will use on every real project. The preview creates a reason to complete the homework.

The "protected routes with Depends(get_current_user)" line deliberately references the dependency injection pattern from Lesson 3 — connecting the prior learning to the upcoming content. This forward connection builds the mental scaffolding for Lesson 5.

Before participants leave: verify that everyone has their homework repo set up and can push to it. A participant who cannot push code cannot submit homework. Five minutes of tech support now prevents zero homework submissions before Lesson 5.

Facilitator self-reflection (complete before the next session): write down the three moments in today's lesson where participants were most engaged and the three moments where energy dropped. The engagement peaks tell you what is working. The dips tell you where to cut, restructure, or add a practice activity in the next iteration.
-->
