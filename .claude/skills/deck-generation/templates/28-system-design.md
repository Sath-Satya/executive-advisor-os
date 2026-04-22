<!-- TEMPLATE: system-design
     CATEGORY: Technical
     USE WHEN: walking through a system design problem in an interview or team review setting
     SLIDE COUNT: 12
     PALETTE: Dark dev
     RENDER: marp --pptx 28-system-design.md -->
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
  h2 { color: #2dd4a0; font-size: 1.25em; margin-top: 0; }
  h3 { color: #8899ac; font-size: 0.9em; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; }
  p, li { color: #d0d8e4; line-height: 1.65; }
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
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
  th { background: #111820; color: #3b9eff; padding: 10px 14px; text-align: left; border-bottom: 2px solid #1a2535; }
  td { padding: 9px 14px; border-bottom: 1px solid #1a2535; color: #d0d8e4; }
  tr:nth-child(even) td { background: #0d1117; }
  blockquote { border-left: 3px solid #2dd4a0; padding: 8px 16px; background: #0d1117; margin: 16px 0; }
  blockquote p { color: #2dd4a0; margin: 0; }
  section.title { justify-content: center; }
  section.title h1 { font-size: 2.4em; border: none; padding-bottom: 0; }
  section.title h2 { color: #8899ac; font-weight: 400; font-size: 1.1em; }
---
<!-- _class: title -->

# Design a Real-Time Claims Pipeline
## System Design — Helix at 4 M Claims/Day

**Context:** Engineering interview / team design review
**Time budget:** 45 minutes · Start with requirements, end with Q&A

<!-- SPEAKER NOTES — Slide 1: Title
System design sessions work best with an explicit time structure stated at the start. The interviewer or facilitator controls the clock — the presenter should always ask before going deep on any single component. The Helix claims pipeline is a realistic, domain-appropriate example: it involves high throughput, strict ordering requirements (a claim must be adjudicated before payout), data integrity (healthcare data cannot be lost), and compliance constraints. If presenting in an interview context, acknowledge the constraints and trade-offs out loud as you work through them — interviewers evaluate reasoning, not just answers.
-->

---

# 1 — Requirements

## Functional and Non-Functional

**Functional requirements:**
- Ingest electronic claims from clearing houses (EDI 837, REST, SOAP)
- Adjudicate claims against eligibility, formulary, and plan rules
- Route approved claims to payout; rejected claims to manual review
- Provide claim status to member portal and provider staff

**Non-functional requirements:**
- **Throughput:** 4 M claims/day → ~46 claims/second average, ~200 claims/second peak (open enrollment)
- **Latency:** P99 adjudication-to-ACK ≤ 800 ms
- **Durability:** Zero claim loss — once received, a claim must be processed or queued
- **Availability:** 99.95% uptime — healthcare SLA
- **Compliance:** HIPAA — PHI isolation and audit trail required

<!-- SPEAKER NOTES — Slide 2: Requirements
Always start a system design with requirements gathering — this is the highest signal behavior in an interview or design review. Ask clarifying questions before proposing anything: "Is 800 ms end-to-end or just adjudication?" "Does 'zero claim loss' mean exactly-once semantics or at-least-once with deduplication?" The peak/average ratio (200/46 = ~4.3×) is important — it means you cannot size for average throughput. Open enrollment creates predictable burst, which allows pre-scaling. The HIPAA requirement constrains several technical choices: data must be encrypted at rest and in transit, PHI cannot flow to systems not in the compliance boundary, and an immutable audit trail is required.
-->

---

# 2 — Scope

## What We Will and Will Not Design Today

**In scope (45 min):**
- Ingestion layer — accepting claims from 7 clearing houses
- Adjudication pipeline — eligibility, rules engine, output routing
- Storage — claim records, audit log, status queries
- Basic API for provider and member portal status queries

**Out of scope (note and time-box):**
- Provider enrollment and credentialing
- Payer configuration management
- Fraud detection (would be a separate ML pipeline)
- Member-facing appeals process

> Deliberately deferring fraud detection — it has different latency and model requirements. Worth a separate design session.

<!-- SPEAKER NOTES — Slide 3: Scope
Explicitly scoping a system design session is a signal of maturity — it shows you understand that you cannot design everything in 45 minutes and that trying to do so produces shallow designs. The "note and time-box" framing for out-of-scope items means you are aware they exist and have thought about how they connect, but you are not going to go down those paths today. The fraud detection deferral is a good example: it belongs in a separate session because it involves asynchronous scoring (cannot add to the 800 ms SLA), model management, and retraining pipelines that are completely different from the synchronous adjudication pipeline. Acknowledge the dependency though: fraud holds on a claim would need to integrate with the adjudication output.
-->

---

# 3 — API Design

## External-Facing Interfaces

**Clearing house submission (REST):**
```http
POST /api/v1/claims
X-Clearing-House-ID: {house-id}
X-Idempotency-Key: {client-generated-key}
Content-Type: application/json

{
  "payer_id": "BCBS-CA",
  "member_id": "M-8829401",
  "claim_lines": [...],
  "submission_ts": "2024-11-14T09:12:00Z"
}

→ 202 Accepted  { "claim_id": "CLM-8842019", "status": "received" }
→ 409 Conflict  { "claim_id": "CLM-8842019", "status": "duplicate", "idempotency_hit": true }
```

**Provider status query:**
```http
GET /api/v1/claims/{claim_id}/status
→ 200 OK  { "status": "adjudicated", "decision": "approved", "adjudicated_at": "..." }
```

<!-- SPEAKER NOTES — Slide 4: API Design
The API design slide establishes the system's external contract before diving into internals. The 202 Accepted response (not 200) is a deliberate choice: we are accepting the claim for processing, not completing the adjudication synchronously. This decouples the clearing house from the processing pipeline and allows us to achieve the 800 ms SLA on adjudication without blocking the submission ACK. The 409 Conflict for duplicates (with idempotency_hit flag) is important: clearing houses retry submissions. The provider status query is a simple read path — it will need caching at scale. The `X-Idempotency-Key` header follows the Stripe API convention, which most clearing house integration teams will recognize.
-->

---

# 4 — Data Model

## Core Entities and Storage Choices

| Entity | Storage | Key Fields | Rationale |
|---|---|---|---|
| `claims` | PostgreSQL | claim_id, payer_id, status, submitted_at | Strong consistency; ACID transactions |
| `claim_lines` | PostgreSQL (FK) | claim_id, procedure_code, billed_amount | Co-located with claim; consistent reads |
| `adjudication_results` | PostgreSQL | claim_id, decision, rules_version, adjudicated_at | Append-only; FK to claims |
| `audit_log` | S3 (Parquet) | claim_id, event_type, actor, timestamp, payload_hash | Immutable; HIPAA audit trail; queryable via Athena |
| `claim_status_cache` | Redis | claim_id → {status, ttl} | P99 < 2 ms for provider status queries |
| `idempotency_keys` | Redis | SHA-256 hash → claim_id (TTL 24h) | Deduplication without DB lookup |

<!-- SPEAKER NOTES — Slide 5: Data Model
The storage selection table makes the technology choice explicit and justified, rather than listing everything in PostgreSQL by default. Walk through the rationale column: PostgreSQL for the transactional claims data (consistency required), S3 for audit logs (immutable, cheap, queryable with Athena for compliance reports), Redis for two distinct caching purposes (status queries and idempotency keys). The audit log as S3 Parquet is a healthcare-specific pattern: regulators often request historical audit exports in formats compatible with analytics tools — Parquet + Athena handles this without a separate reporting database. The `payload_hash` in audit_log ensures tamper detection without storing full PHI in the audit record.
-->

---

# 5 — Architecture Diagram

## Component Overview

```
[Clearing Houses / Providers]
         ↓ REST / EDI
[API Gateway + Load Balancer]
         ↓
[Intake Service] → [Kafka: claims.raw (32 partitions)]
                              ↓
                   [Rules Engine (K8s, 3–40 pods)]
                              ↓ adjudicated
                   [Kafka: claims.adjudicated]
                     ↙              ↘
          [Payout Service]    [Audit Service]
               ↓ write              ↓ write
         [PostgreSQL]           [S3: audit-log]
                     ↘         ↙
               [Status Cache (Redis)]
                              ↓
              [Status API] → [Member Portal / Provider API]
```

<!-- SPEAKER NOTES — Slide 6: Architecture Diagram
The ASCII architecture diagram shows the full data flow from intake to status query in a single view. Walk left to right, top to bottom: clearing houses push to the API Gateway, Intake service normalizes the claim and publishes to Kafka, Rules Engine consumes and adjudicates, the adjudicated topic fans out to Payout and Audit in parallel, and the Status Cache is updated so the Status API can serve queries without hitting the DB. Key design choices to highlight: (1) Kafka as the backbone — it provides durability and the ability to replay any window of claims; (2) Rules Engine is horizontally scalable — it is stateless and scales on Kafka consumer group lag; (3) Audit and Payout are separate consumers — adding a new downstream service (e.g., analytics) requires no changes to Rules Engine.
-->

---

# 6 — Scale Estimates

## Back-of-Envelope Calculations

**Throughput:**
- 4 M claims/day = 46.3 claims/s average
- Open enrollment peak: 4× average = ~185 claims/s
- With 10% headroom: size for **200 claims/s**

**Storage (1 year):**
- Claims table: 4M × 365 × 2 KB = ~2.9 TB/yr
- Audit log (S3): 4M × 365 × 800 bytes (compressed Parquet) = ~1.2 TB/yr
- Redis (idempotency, 24h TTL): 4M × 380 bytes = ~1.5 GB/day (small)

**Kafka partitions:**
- Target consumer throughput: 200 claims/s per pod × 40 pods max = 8,000 claims/s ceiling
- 32 partitions → 32 consumer max parallelism → well above peak demand

**DB connections:** PgBouncer pool with max 200 connections; Rules Engine uses 1 conn/pod max.

<!-- SPEAKER NOTES — Slide 7: Scale Estimates
Back-of-envelope math is a required skill for system design sessions. Walk through each calculation and show your work — the goal is not to get an exact number, it is to show that you can reason about scale. The open enrollment 4× multiplier is a healthcare-specific assumption — justify it by noting that enrollment periods are well-known in advance, allowing pre-scaling via EKS node group warm-up. The Kafka partition count calculation is important: 32 partitions sets the ceiling for consumer parallelism. Since Rules Engine auto-scales between 3 and 40 pods, 32 partitions means we will never be able to use all 40 pods effectively — this is a design trade-off worth noting and revisiting if peak throughput requirements increase.
-->

---

# 7 — Bottleneck Analysis

## Where the System Will Break Under Load

| Bottleneck | Trigger Condition | Mitigation |
|---|---|---|
| Rules Engine CPU | Business rules complexity + high TPS | Horizontal auto-scale; cache eligibility lookups (Redis) |
| PostgreSQL write throughput | Peak claim volume (payout + audit writes) | Payout DB separate from adjudication DB; connection pool |
| Redis memory | Large idempotency keyspace at open enrollment | Right-size cluster; TTL management; monitor free memory |
| Kafka consumer lag | Rules Engine pod scaling lag behind burst | Pre-warm pods before open enrollment; HPA stabilization tuning |
| API Gateway TLS termination | Very high connection rate from clearing houses | Persistent connections (HTTP/2); distribute across AZs |

**Hottest path:** Intake → claims.raw → Rules Engine → claims.adjudicated — optimize here first.

<!-- SPEAKER NOTES — Slide 8: Bottleneck Analysis
Bottleneck analysis is what separates a design that works in theory from one that works in production. Walk through each row and explain what monitoring signal would indicate the bottleneck is being hit. For Rules Engine CPU: watch consumer lag — if lag grows faster than pod count scales, the CPU is the limiter. For PostgreSQL: watch lock wait time and replication lag. For Redis memory: watch `freeable_memory` CloudWatch metric. The "hottest path" note at the bottom is a prioritization signal: if you only have time to optimize one thing, start with the critical path. All other bottlenecks are either off the critical path or can be addressed incrementally.
-->

---

# 8 — Trade-offs

## Key Design Decisions and Their Costs

| Decision | Benefit | Cost |
|---|---|---|
| Kafka for messaging | Replay capability, ordered partitions, durability | Operational complexity; min 3-node overhead |
| Stateless Rules Engine | Horizontal scale-out | Must fetch eligibility from DB/cache per claim |
| Avro + Schema Registry | Enforced compatibility, schema evolution | Developer friction; registry as new dependency |
| Separate Payout + Audit consumers | Independent scaling, new consumers at zero cost | Two Kafka consumer groups to manage |
| Redis for idempotency (not DB) | < 2 ms lookup, no DB contention | TTL-based — claims submitted > 24h after initial not deduplicated |
| S3 for audit log (not RDS) | Immutable, cheap, Athena-queryable | Eventual consistency — not for real-time queries |

> No design is free of trade-offs. These are the ones I made and why.

<!-- SPEAKER NOTES — Slide 9: Trade-offs
The trade-offs table is the highest-signal slide for an engineering interview. It shows that you understand there is no "perfect" design and that every choice has a cost. Walk through each row and be prepared to defend the benefit and acknowledge the cost. The Redis idempotency TTL trade-off (24-hour window) is worth explaining in detail: claims that are submitted more than 24 hours after the initial submission are treated as new claims by the idempotency layer. This is acceptable because provider SLA terms typically require re-submission within 24 hours if they do not receive an ACK. For longer windows, the design would need a persistent store (with higher latency cost). The pull-quote at the bottom is a framing statement — say it out loud to signal maturity.
-->

---

# 9 — Deep Dive — Adjudication Engine

## How the Rules Engine Works

```
Claim received from claims.raw topic
    ↓
1. Fetch member eligibility (Redis cache → Eligibility DB on miss)
2. Validate claim format (NPI check, procedure code lookup)
3. Apply plan rules (formulary, annual limits, prior authorization)
4. Apply payer-specific overrides (rate tables, modifiers)
5. Generate adjudication result {approved | denied | pending-review}
    ↓
Publish to claims.adjudicated with:
  { claim_id, decision, rules_version, processing_node_id, adjudicated_at }
```

**Rules version pinning:** Every adjudication result includes `rules_version`. Allows re-adjudication of a historical claim with the same rule set it was originally processed under — critical for appeals.

<!-- SPEAKER NOTES — Slide 10: Deep Dive 1
The adjudication engine deep dive is the most domain-specific slide in the deck. Step 1 (eligibility fetch) is the most performance-critical step: eligibility data changes infrequently (plan year cycle) but is fetched on every claim. A two-level cache (Redis for hot eligibility, PostgreSQL for miss) keeps P99 eligibility fetch under 5 ms. Step 3 (plan rules) is the most computationally expensive step — the rules engine evaluates a directed acyclic graph of conditions. The key optimization is to short-circuit early: if a claim fails format validation in Step 2, skip Steps 3–4 entirely. The `rules_version` in the output is a healthcare-specific requirement: regulators may require re-adjudication of claims if rules change, and you need to know which version of the rules was applied to a specific claim.
-->

---

# 10 — Deep Dive — Reliability

## How We Prevent Claim Loss

**At-least-once guarantee (with deduplication):**

```
Intake Service:
  1. Write to claims.raw (Kafka producer acks from all ISR replicas)
  2. Return 202 Accepted ONLY after Kafka ack
  → If step 1 fails: client retries with same idempotency key
  → If step 2 fails (ack to clearing house): client retries; idempotency key prevents double-adjudication

Rules Engine:
  3. Consumer commits offset ONLY after successful publish to claims.adjudicated
  → If pod dies before commit: claim re-consumed from last committed offset
  → Idempotency key on output topic prevents double-payout
```

**Durability:** Kafka topic replication factor 3; min ISR 2. Claims cannot be lost even with 1 broker failure.

<!-- SPEAKER NOTES — Slide 11: Deep Dive 2
Reliability design is the most important deep dive for a healthcare claims system. The at-least-once guarantee with deduplication is the correct pattern: exactly-once semantics in Kafka are complex and have performance costs; at-least-once with idempotency keys achieves the same correctness guarantee with better operational simplicity. Walk through the two failure scenarios in detail: (1) the client retry after Intake write failure — the clearing house retries with the same idempotency key, so the second submission is either a fresh write or a cache hit, never a double-adjudication; (2) the Rules Engine consumer offset scenario — if a pod dies between processing and committing the Kafka offset, the claim is re-consumed. The idempotency key on the adjudicated topic prevents double-payout in this case. The Kafka durability settings (RF=3, minISR=2) are non-negotiable for a healthcare system.
-->

---

# 11 — Summary

## What We Designed

**Core architecture:** Event-driven pipeline with Kafka as the reliability backbone

**Key decisions:**
- Stateless Rules Engine — horizontal scale without coordination overhead
- At-least-once + idempotency — claim durability without exactly-once Kafka complexity
- PHI isolation at topic boundary — HIPAA compliance by design, not by policy
- Redis for two distinct cache layers — status queries and deduplication (different TTLs and semantics)

**What to build next if time allowed:**
- Fraud detection (async scoring, ML model serving)
- Real-time provider dashboard (WebSocket, Kafka consumer)
- Multi-region active-passive for disaster recovery

> This design handles 200 claims/s with < 400 ms P99 adjudication latency and zero claim loss.

<!-- SPEAKER NOTES — Slide 12: Summary
The summary slide does two things: restates the core design decisions as a coherent narrative, and signals awareness of what was not covered. The "what to build next" section is important for interview contexts — it shows you can prioritize and scope, and that you have a mental model of the full system even though you did not design all of it today. The closing assertion ("handles 200 claims/s with < 400 ms P99") should be grounded in the scale estimates from Slide 7 — it is a claim you can defend with math, not just assertion. End by inviting questions: "What component would you like to drill deeper on?" Leave at least 10 minutes for Q&A.
-->

---

# 12 — Q&A

## Questions and Discussion

**Prepared deep-dive topics:**
- Eligibility cache design — invalidation strategy and consistency model
- Multi-region active-passive failover — RTO/RPO trade-offs
- Fraud detection pipeline integration — async scoring, hold logic
- Schema Registry migration strategy — from current state to proposed
- Load shedding — what happens at 10× expected throughput

**Useful reference numbers:**
- Kafka producer ack latency (RF=3): ~8 ms P99
- Redis read (single key): ~0.9 ms P99
- PostgreSQL indexed read: ~8 ms P99
- EKS pod cold start: ~12–30 s (use pre-warmed pool for burst scenarios)

<!-- SPEAKER NOTES — Slide 13 (final): Q&A
The prepared deep-dive topics signal that you have thought beyond what you presented. If the interviewer or audience asks about one of these topics, you are ready. If they ask about something not on the list, think aloud: "That is an interesting case. My first instinct is X because of Y — let me think through the implications..." The reference numbers are empirical benchmarks — quote the source if challenged (Kafka benchmarks from Confluent official docs; Redis from Redis Labs benchmarks; PostgreSQL from pgBench on r5.2xlarge). The EKS cold start note (12–30 s) is critical for auto-scaling strategy: if a Rules Engine pod needs 15 s to start, your HPA must trigger early enough that pods are ready before consumer lag becomes a problem. This is a common gotcha worth raising in Q&A without being asked.
-->
