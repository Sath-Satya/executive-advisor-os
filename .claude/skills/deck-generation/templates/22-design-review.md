<!-- TEMPLATE: design-review
     CATEGORY: Technical
     USE WHEN: presenting a feature design to peers before implementation begins
     SLIDE COUNT: 10
     PALETTE: Dark dev
     RENDER: marp --pptx 22-design-review.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'DM Sans', 'Segoe UI', system-ui, sans-serif;
    background: #0a0e14;
    color: #d0d8e4;
    padding: 48px 56px;
  }
  h1 {
    font-family: 'DM Mono', 'Cascadia Code', monospace;
    color: #3b9eff;
    letter-spacing: -0.3px;
    font-size: 1.8em;
    border-bottom: 2px solid #1a2535;
    padding-bottom: 12px;
    margin-bottom: 24px;
  }
  h2 { color: #2dd4a0; font-size: 1.3em; margin-top: 0; }
  h3 { color: #8899ac; font-size: 1em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; }
  p, li { color: #d0d8e4; line-height: 1.6; }
  strong { color: #3b9eff; }
  em { color: #2dd4a0; font-style: normal; font-weight: 600; }
  code {
    font-family: 'DM Mono', 'Cascadia Code', monospace;
    background: #111820;
    padding: 2px 6px;
    border-radius: 3px;
    color: #a78bfa;
    font-size: 0.9em;
  }
  pre {
    background: #111820;
    padding: 16px 20px;
    border-left: 3px solid #3b9eff;
    border-radius: 0 4px 4px 0;
  }
  pre code { background: transparent; padding: 0; color: #d0d8e4; }
  table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
  th { background: #111820; color: #3b9eff; padding: 10px 14px; text-align: left; border-bottom: 2px solid #1a2535; }
  td { padding: 9px 14px; border-bottom: 1px solid #1a2535; color: #d0d8e4; }
  tr:nth-child(even) td { background: #0d1117; }
  blockquote { border-left: 3px solid #2dd4a0; padding: 8px 16px; background: #0d1117; margin: 16px 0; }
  blockquote p { color: #2dd4a0; margin: 0; font-style: italic; }
  section.title { justify-content: center; }
  section.title h1 { font-size: 2.4em; border: none; padding-bottom: 0; }
  section.title h2 { color: #8899ac; font-weight: 400; font-size: 1.1em; }
---
<!-- _class: title -->

# Helix — Design Review
## Idempotent Retry Framework for Claims Adjudication

**Author:** [Engineer Name] &nbsp;|&nbsp; **RFC:** HLX-0047 &nbsp;|&nbsp; **Date:** [YYYY-MM-DD]

<!-- SPEAKER NOTES — Slide 1: Title
A design review is earlier in the lifecycle than an architecture review — you are asking peers to poke holes in your design before you write a line of production code. Set expectations accordingly: "This is a draft design. I want concrete objections, not encouragement." State the RFC number so reviewers can cross-reference the written doc. Identify who should be the approvers vs. who is here for awareness. Keep this slide up for 30 seconds maximum — the audience wants to get into the content.
-->

---

# 1 — Context

## Why This Feature Exists

- Helix processes **1.2 M claims/day**; transient failures (network, DB locks) cause **~0.3% silent drops**
- Dropped claims require manual re-submission by provider staff — **estimated 14 staff-hours/week**
- Current retry logic: 3 attempts with fixed 5 s delay — no idempotency key, no deduplication
- **Trigger:** Provider escalation in Q1; contractual SLA penalty risk if drop rate exceeds 0.5%

> This is an operational reliability feature — it has no new user-visible surface, only reduced error rates.

<!-- SPEAKER NOTES — Slide 2: Context
Ground the design in a real problem before showing any technical content. The 14 staff-hours/week figure should come from the provider support team — get that number confirmed in writing before presenting it. The context slide answers "why are we doing this now?" — the contractual SLA penalty is the forcing function that makes this urgent. Note that this is explicitly not a new feature from the provider's perspective — it is invisible infrastructure that reduces their pain. This framing matters because it will come up in roadmap prioritization discussions.
-->

---

# 2 — Goals and Non-Goals

## Scope Boundary

**Goals (IN)**
- ✓ Idempotent claim submission — duplicate submissions produce a single adjudication result
- ✓ Configurable retry with exponential back-off and jitter
- ✓ Dead-letter queue for claims exceeding retry budget
- ✓ Metrics: retry rate, DLQ depth, deduplication hit rate

**Non-goals (OUT)**
- ✗ Retroactive reprocessing of historical dropped claims
- ✗ Provider-facing UI for retry status
- ✗ Changes to adjudication business logic

<!-- SPEAKER NOTES — Slide 3: Goals and Non-Goals
The non-goals slide is as important as the goals slide. Listing "retroactive reprocessing" as out of scope will prevent scope creep during implementation — someone will ask for it in code review if you do not document this decision now. The provider-facing UI is also important to exclude: that is a separate feature with different stakeholders and timeline. Be prepared for someone to argue that retroactive reprocessing should be in scope — your response is that it requires audit team involvement and a separate design, and that the current SLA risk is addressed by preventing future drops, not fixing historical ones. The metrics goal is important to include explicitly: without observability, you cannot prove the feature is working.
-->

---

# 3 — Proposal

## Idempotency Key Design

```
Idempotency Key = SHA-256( payer_id + member_id + service_date + procedure_code + billed_amount )
```

**Flow:**

```
[Intake] → generate key → check Redis (TTL 24h)
               ↓ HIT                    ↓ MISS
     return cached result       → [Rules Engine] → store result in Redis → return result
```

- Key TTL: **24 hours** (covers all realistic provider retry windows)
- Storage: Redis Cluster (existing infra) — key + compressed adjudication result
- Retry policy: **3 attempts, exponential back-off: 1 s → 8 s → 64 s, ± 20% jitter**

<!-- SPEAKER NOTES — Slide 4: Proposal
Walk through the idempotency key derivation formula first — reviewers will immediately ask "what makes a claim unique?" The SHA-256 of those five fields is deterministic for any given claim, regardless of the submission channel or timestamp. Clarify that the key does not include the submission timestamp — this is intentional and should spark discussion. If a provider submits the same claim at 9 AM and 9:05 AM, we want one adjudication result. The 24-hour TTL is a business decision, not a technical one — it should be validated against the provider SLA terms. The Redis TTL approach is preferred over a database deduplication table because the lookup path is in the critical path of every claim; Redis P99 is ~1 ms, versus ~10–40 ms for a PostgreSQL lookup under load.
-->

---

# 4 — Interface and API

## Changes to Existing Surfaces

**Intake service — new optional header (backward-compatible):**
```http
POST /v1/claims
X-Idempotency-Key: <client-provided key>      # optional; server generates if absent
X-Retry-Attempt: 2                             # optional; for observability only
```

**Response — idempotent hit (HTTP 200, not 201):**
```json
{
  "claim_id": "CLM-8842019",
  "status": "adjudicated",
  "idempotency": { "hit": true, "original_ts": "2024-11-15T09:12:04Z" }
}
```

**No changes to downstream API** (Rules Engine, Payout, Audit are consumers — no API surface).

<!-- SPEAKER NOTES — Slide 5: Interface and API
The design decision to allow a client-provided idempotency key (with server fallback) is important for compatibility with clearing houses that already generate their own transaction IDs. Walk reviewers through the HTTP 200 vs 201 distinction: a 201 means a new resource was created; a 200 on a duplicate means we are returning an existing result. Some clients may behave differently based on this status code — confirm with the integrations team. The `idempotency.hit` field in the response body is for provider-side observability: they can log duplicate submission events. The "no changes to downstream API" note is critical — it bounds the blast radius of this change to the Intake service and Redis.
-->

---

# 5 — Data Model

## Redis Key Schema

| Field | Type | Example | Notes |
|---|---|---|---|
| `key` | `string` | `hlx:idem:a3f9c2…` | `hlx:idem:` prefix + SHA-256 hex |
| `value` | `bytes` | (compressed JSON) | Snappy-compressed adjudication result |
| `TTL` | `seconds` | `86400` | 24 h; set on first write |
| `created_at` | embedded in value | ISO 8601 | For audit on hit |

**Estimated storage per key:** ~380 bytes compressed (vs. ~2.1 KB uncompressed)
**Peak keyspace at 24 h TTL, 1.2 M claims/day:** ~456 MB — fits within existing Redis cluster headroom (current utilization: 31%)

<!-- SPEAKER NOTES — Slide 6: Data Model
The storage estimate is important — reviewers will ask if this fits in existing Redis capacity. The calculation should be pre-validated: 1.2 M claims × 380 bytes = ~456 MB per 24-hour window. Current Redis utilization is 31% of a cluster with N GB capacity — show the specific cluster size if challenged. The `hlx:idem:` key prefix enables targeted Redis keyspace notifications and simplifies operational tooling (you can scan or flush the idempotency namespace without touching other Redis data). The Snappy compression choice should be justified: Snappy is ~3× compression at minimal CPU cost; gzip would achieve ~5× but at 10–15× the CPU cost, which is not worthwhile for this use case.
-->

---

# 7 — Open Questions

## Decisions Needed Before Implementation

| # | Question | Stakes | Proposal |
|---|---|---|---|
| Q1 | Who generates the key for batch EDI submissions? | High | Intake service generates per-claim key within batch |
| Q2 | Should DLQ claims auto-retry after TTL expiry? | Medium | No — require manual re-submission; document in runbook |
| Q3 | What is the correct TTL for real-time vs. batch paths? | Medium | Same 24 h — simpler ops, consistent guarantee |
| Q4 | Redis cluster vs. ElastiCache for managed ops? | Low | ElastiCache — reduces on-call overhead |

> Q1 is a blocker — implementation cannot begin until the batch EDI team confirms the key generation contract.

<!-- SPEAKER NOTES — Slide 7: Open Questions
Open questions are the most valuable part of a design review — do not try to answer them all before the meeting. The table format allows the audience to focus on the high-stakes questions first. Q1 is explicitly marked as a blocker: if the batch EDI team (likely not in this room) generates a different idempotency key format, the SHA-256 derivation formula may need to change. Get a commitment from the product owner to schedule a working session with the EDI team this week. Q2 is a philosophy question: auto-retry after TTL expiry means a claim dropped on Monday could be retried on Tuesday with different business rules (e.g., a new formulary update). Manual re-submission is safer. Document this decision in the RFC.
-->

---

# 8 — Alternatives Considered

## What Was Ruled Out and Why

| Alternative | Why Rejected |
|---|---|
| DB-based deduplication table | P99 ~40 ms on critical path; adds schema migration risk |
| Distributed lock (Redis SETNX) | Lock acquisition is synchronous — worse than current retry for latency |
| Client-only idempotency (trust X-Idempotency-Key header) | Clearing houses do not guarantee unique keys across retransmissions |
| Kafka exactly-once semantics | Available on Kafka 3.x path, but adds producer complexity; overkill for this scope |

<!-- SPEAKER NOTES — Slide 8: Alternatives Considered
This slide builds trust by showing you explored the problem space. Walk through each alternative briefly — the point is not to re-litigate them, but to show that obvious questions ("why not just use the DB?") have been considered. The Kafka exactly-once semantics alternative is worth extra time: it is architecturally elegant but introduces exactly-once semantics at the producer level, which has significant operational complexity for the intake service. Given that the existing Kafka path is in Phase 1 of the migration plan, adding EOS semantics in the same sprint is inadvisable. Note this as a future optimization in the RFC.
-->

---

# 9 — Rollout Plan

## Staged Deployment

| Stage | Scope | Success Criteria | Rollback |
|---|---|---|---|
| Stage 1 | 5% of real-time claims (canary) | DLQ depth < 10, no adjudication errors | Feature flag off |
| Stage 2 | 50% real-time + all batch | Drop rate < 0.1%, P99 latency delta < 20 ms | Feature flag off |
| Stage 3 | 100% traffic | Drop rate ≤ 0.05%, SLA maintained | N/A |
| Monitor | 14-day bake period | Zero P0/P1 incidents in idempotency layer | — |

**Observability:** `helix.idempotency.hit_rate`, `helix.idempotency.dlq_depth`, `helix.retry.attempt_distribution`
**Alerting:** PagerDuty alert if DLQ depth > 50 for 5 consecutive minutes.

<!-- SPEAKER NOTES — Slide 9: Rollout Plan
A feature flag-based staged rollout is standard practice for critical path changes. The success criteria for each stage should be agreed upon before Stage 1 begins — do not move to Stage 2 until Stage 1 criteria are met. The 14-day bake period after Stage 3 is important: idempotency bugs often surface in edge cases that only appear at full volume over multiple days. The three metric names should be final before implementation — they need to be in the monitoring runbook, the on-call playbook, and the PagerDuty alert rule. Confirm with the SRE team that the existing Redis cluster has the correct monitoring hooks. The rollback mechanism (feature flag) must be tested before Stage 1 — add a "verify rollback works" gate to the Stage 1 exit criteria.
-->

---

# 10 — Decision

## What We Need From This Room

**Proposal:** Approve HLX-0047 design for implementation.

| Decision | Owner | Due |
|---|---|---|
| ▲ Approve or reject overall design | Tech Lead + Reviewers | Today |
| → Resolve Q1 (batch EDI key contract) | Product + EDI team | This week |
| → Confirm Redis cluster headroom for 456 MB | Platform / SRE | This week |
| ○ Sign off on metric naming convention | Observability team | Before Stage 1 |

**If approved:** Implementation begins next sprint (Wk [N]).
**Estimated effort:** 8 story points across Intake service + Redis integration + observability.

<!-- SPEAKER NOTES — Slide 10: Decision (final)
Close with a clean decision table. Note that "approve or reject" is the primary ask — avoid "approve with conditions" as a loophole that delays the decision. If reviewers raise significant concerns, explicitly discuss whether those concerns warrant a re-review or can be resolved asynchronously via RFC comments. The 8-story-point estimate should be validated with the implementation team before this meeting — showing an estimate builds confidence that you have thought through scope. After the meeting, update the RFC doc with the decision, any dissenting opinions (important for future reference), and a list of action items with owners and due dates.
-->
