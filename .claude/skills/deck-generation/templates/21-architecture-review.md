<!-- TEMPLATE: architecture-review
     CATEGORY: Technical
     USE WHEN: presenting a proposed architecture change to engineering leadership
     SLIDE COUNT: 12
     PALETTE: Dark dev
     RENDER: marp --pptx 21-architecture-review.md -->
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
    overflow-x: auto;
  }
  pre code { background: transparent; padding: 0; color: #d0d8e4; }
  table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
  th { background: #111820; color: #3b9eff; padding: 10px 14px; text-align: left; border-bottom: 2px solid #1a2535; }
  td { padding: 9px 14px; border-bottom: 1px solid #1a2535; color: #d0d8e4; }
  tr:nth-child(even) td { background: #0d1117; }
  .tag { display: inline-block; background: #111820; border: 1px solid #3b9eff; color: #3b9eff; border-radius: 4px; padding: 2px 8px; font-size: 0.78em; font-family: 'DM Mono', monospace; }
  section.title { justify-content: center; text-align: left; }
  section.title h1 { font-size: 2.4em; border: none; padding-bottom: 0; }
  section.title h2 { color: #8899ac; font-size: 1.1em; font-weight: 400; }
---
<!-- _class: title -->

# Helix — Architecture Review
## Real-Time Claims Processing Pipeline — Proposed Redesign

**Presenter:** [Engineer Name] &nbsp;|&nbsp; **Date:** [YYYY-MM-DD]
**Audience:** Engineering Leadership, Platform Team

<!-- SPEAKER NOTES — Slide 1: Title
Set the stage before diving into content. This is an architecture review, not a post-mortem — the goal is to get explicit approval on the proposed direction before any code is written. Clarify your role (proposing architect or DRI), the stakeholders in the room, and what decision you need by end of session. State the time budget: "We have 45 minutes — 30 for the deck, 15 for Q&A and decision." If there are known objections already surfaced in pre-read reviews, acknowledge them here so the audience knows they will be addressed. Keep this slide on screen no longer than 60 seconds.
-->

---

# 1 — The Problem

## Why We Are Here

- **Latency**: Helix P99 adjudication latency is **4.2 s** — SLA requires ≤ 800 ms
- **Coupling**: Claims ingestion, rules engine, and payout are a single deployable unit — one release blocks all three
- **Scaling ceiling**: Monolith auto-scales vertically only; burst traffic (open enrollment) causes OOM evictions

> The current design was right for 2021. We process 3× the volume with the same topology.

<!-- SPEAKER NOTES — Slide 2: The Problem
Anchor the whole review in a crisp problem statement. Avoid starting with the solution. The three bullets follow a "what → why it matters" structure: latency is a user-facing SLA breach; coupling is a dev-velocity problem; scaling ceiling is a cost and reliability risk. The pull-quote from below the bullets is intentional — it frames this as evolution, not blame. If anyone in the room built the original system, acknowledge the original constraints were real. Have the exact P99 numbers from your APM tool ready — someone will ask "where does 4.2 s come from?" Cite the dashboard or runbook link in your speaker notes before presenting.
-->

---

# 2 — Current Architecture

## What Exists Today

```
[EDI Intake] → [Monolith: Parser + Rules + Payout] → [PostgreSQL] → [Outbound ACK]
                         ↑
              [Admin Console (RPC)]
```

**Pain points mapped to components:**

| Component | Pain Point | Blast Radius |
|---|---|---|
| Monolith rules engine | CPU-bound, no horizontal scale | All claims |
| Shared PostgreSQL | Lock contention on batch updates | All writes |
| Admin Console RPC | Synchronous — blocks processing | Entire pipeline |

<!-- SPEAKER NOTES — Slide 3: Current Architecture
Walk the audience through the diagram slowly — not everyone has the same mental model of the system. The ASCII diagram is intentionally minimal: it shows the critical path, not every service. For a deeper audience, you can reference a Confluence C4 diagram link. The table maps each pain point to blast radius — this helps leadership understand why a local fix will not work. Emphasize that the Admin Console RPC coupling is the most surprising finding: a low-traffic internal tool can starve the critical path. Mention this was confirmed by tracing data, not hypothesis. Expected questions: "Why not just scale up the DB?" — address preemptively by noting lock contention is logical, not capacity.
-->

---

# 3 — Proposed Architecture

## Event-Driven Decomposition

```
[EDI Intake] → [Kafka: claims.raw] → [Rules Engine (K8s, auto-scale)]
                                              ↓
                               [Kafka: claims.adjudicated]
                                              ↓
                              [Payout Service] → [PostgreSQL: payouts]
                                              ↓
                              [Audit Service]  → [S3: audit-log]
```

- **Intake**, **Rules**, **Payout**, and **Audit** are independent deployables
- Rules Engine scales horizontally on consumer group lag
- Admin Console moves to async event subscription — no RPC coupling

<!-- SPEAKER NOTES — Slide 4: Proposed Architecture
This is the most important slide in the deck. Walk left to right through the event flow, pausing at each Kafka topic to explain what lives there and why it is a topic boundary. Explain the horizontal scaling story for the Rules Engine: Kafka consumer group lag is a well-understood scale signal — no custom HPA metrics needed. For Payout and Audit, clarify that they are separate consumers on the same adjudicated topic, so adding new downstream services later (e.g., analytics) requires zero changes to the Rules Engine. Anticipated question: "Why Kafka and not SQS?" — have the comparison ready for the trade-offs slide. Be explicit that PostgreSQL is retained for payout records; only the write path is decoupled.
-->

---

# 4 — Trade-off Analysis

## Key Architectural Decisions

| Decision | Option A (Chosen) | Option B | Reason |
|---|---|---|---|
| Messaging | Kafka (self-hosted) | AWS SQS + SNS | Replay capability, ordered partitions |
| Rules engine | Stateless K8s pods | Drools stateful | Simpler ops, rules in DB |
| Schema contract | Avro + Schema Registry | JSON + validation | Enforced compatibility |
| DB topology | Separate schemas, same cluster | Separate clusters | Cost vs isolation trade-off |

> **Accepted risk:** Kafka ops complexity. Mitigated by managed MSK + runbook coverage.

<!-- SPEAKER NOTES — Slide 5: Trade-off Analysis
The table format makes it easy for the audience to scan decisions quickly. Do not defend every choice aggressively — acknowledge the trade-offs honestly. The "Accepted risk" callout at the bottom is intentional: showing that you have thought through the downside and have a mitigation builds credibility more than claiming the design is perfect. Walk through the Kafka vs SQS row in detail — this is the highest-stakes choice and will likely draw the most discussion. Key points: SQS does not support log compaction or deterministic replay, which the Claims audit team requires for regulatory backfill. If someone argues for SQS, acknowledge the operational simplicity advantage, then anchor on the replay requirement as a non-negotiable constraint.
-->

---

# 5 — Data Flow — Claim Lifecycle

## Happy Path — Adjudication in Under 400 ms

```
T+0 ms    EDI file arrives → Intake service parses → claims.raw topic
T+15 ms   Rules Engine consumer picks up claim → eligibility check
T+60 ms   Business rules evaluated (NPI, diagnosis codes, plan limits)
T+80 ms   Result written → claims.adjudicated topic
T+120 ms  Payout service debits member account
T+200 ms  Audit service writes immutable record → S3
T+380 ms  ACK returned to clearing house
```

- **Failure path:** Dead-letter topic `claims.dlq` → alerting → manual review queue
- **Replay path:** Re-consume `claims.raw` from offset 0 for any time window

<!-- SPEAKER NOTES — Slide 6: Data Flow
The timeline format is highly effective for latency arguments — it makes the 380 ms total feel concrete and auditable. Walk through each step and note that 60 ms for business rules evaluation is a modeled estimate from the current engine's benchmark data — share the spreadsheet link. The failure path bullet is critical for a healthcare audience: claims that fail must not silently disappear. Show that the DLQ feeds a manual review queue, not just an alert. The replay path is the most powerful architectural selling point for the audit team: being able to re-adjudicate a historical window for any regulatory change is something the monolith cannot support. Expected question: "What happens during Kafka downtime?" — cover this in the Risk slide.
-->

---

# 6 — Scale and Performance Model

## Capacity Targets

| Metric | Current | Target | Headroom |
|---|---|---|---|
| Claims/day | 1.2 M | 4 M | 3.3× |
| P99 latency | 4,200 ms | ≤ 800 ms | 5.25× |
| Rules Engine pods | 3 (fixed) | 3–40 (auto) | — |
| Kafka partitions | — | 32 (rules topic) | Supports 40 consumers |
| DB write TPS | 4,200 (contended) | 1,800 (payout only) | 57% reduction |

**Scaling model:** Rules Engine HPA triggers at consumer lag > 5,000 messages, scales down at lag < 500 for 3 consecutive minutes.

<!-- SPEAKER NOTES — Slide 7: Scale and Performance
These numbers need to be defensible. The 4 M claims/day target should come from the product team's 3-year volume forecast — cite the doc. The HPA trigger values (5,000 lag / 500 lag) come from load test simulations at the projected P95 volume — reference the load test report. The DB write TPS reduction is a key cost and reliability argument: by scoping PostgreSQL writes to payout records only, you eliminate the lock contention caused by rules engine checkpointing. If anyone asks about Kafka partition count, explain that 32 partitions sets the maximum parallelism ceiling for the consumer group; you can always add consumers up to that ceiling without rebalancing. Note that partition count is a one-time decision — changing it later requires a new topic migration.
-->

---

# 7 — Security Design

## Threat Model and Controls

- **Data in transit:** TLS 1.3 enforced on all Kafka producers and consumers; mTLS between services
- **Data at rest:** MSK encryption enabled; S3 audit log with SSE-KMS; RDS encryption at rest
- **PHI handling:** Claim payload stripped of member PII before `claims.adjudicated` topic — payout service receives only claim ID + amount
- **Auth boundary:** Each service has a dedicated IAM role; no shared credentials; least-privilege S3 and MSK policies
- **Audit:** Every `claims.adjudicated` event includes `processing_node_id`, `rules_version`, and `timestamp` — immutable in S3

> HIPAA: PHI isolation at topic boundary satisfies minimum-necessary standard.

<!-- SPEAKER NOTES — Slide 8: Security Design
This slide is non-negotiable for a healthcare system. Walk through each bullet methodically. The PHI stripping at the topic boundary is the most important design decision from a compliance standpoint — it means the Payout and Audit services never see member PII, which dramatically reduces their HIPAA scope. Be prepared to show the security team a data flow diagram that traces PII through each service boundary. The IAM role-per-service model should be validated by your cloud security team before this review — confirm that before presenting. If the organization has a security review process, note the stage this design is at (e.g., "SRA submitted, pending response"). Expected question: "Who has access to the claims.raw topic?" — answer: only the Rules Engine consumer group and the Intake producer, enforced by MSK ACLs.
-->

---

# 8 — Cost Model

## 12-Month TCO Delta vs. Current

| Line item | Current/mo | Proposed/mo | Delta |
|---|---|---|---|
| EC2 (monolith, r5.4xl × 3) | $2,100 | $0 | -$2,100 |
| EKS node group (t3.xlarge, 3–8) | $0 | $620–$1,650 | +$620–$1,650 |
| Amazon MSK (kafka.m5.large × 3) | $0 | $890 | +$890 |
| RDS Multi-AZ (no change) | $480 | $480 | $0 |
| S3 audit log (est.) | $0 | $45 | +$45 |
| **Total** | **$2,580** | **$2,035–$3,065** | **-$545 to +$485** |

**Break-even at current volume; positive ROI above 2.5 M claims/day** due to auto-scale.

<!-- SPEAKER NOTES — Slide 9: Cost Model
Always show cost before asking for approval — leadership expects it. The table includes a range for the EKS node group because it scales with load. The conservative case (upper end) is still comparable to current spend; the optimistic case (lower end) saves $545/mo. The key insight is the auto-scale story: the monolith pays for peak capacity 24/7; the proposed design only pays for capacity when it is needed. At open enrollment (3–4× normal volume), the monolith would require a manual scale-up event and likely OOM events; the proposed design absorbs it automatically. Have the AWS Cost Calculator link ready. One caveat to be honest about: MSK is a fixed cost regardless of volume — it is the floor, not a variable cost. That is why break-even is at 2.5 M claims/day.
-->

---

# 9 — Migration Plan

## Phased Rollout — 14 Weeks

| Phase | Duration | Deliverable | Risk |
|---|---|---|---|
| P0: Infrastructure | Wk 1–2 | MSK cluster, EKS namespace, Schema Registry | Low |
| P1: Intake service | Wk 3–4 | Dual-write to monolith DB + claims.raw topic | Medium |
| P2: Rules Engine | Wk 5–8 | Shadow mode — compare outputs vs monolith | Medium |
| P3: Payout service | Wk 9–11 | Feature flag per payer, gradual traffic shift | High |
| P4: Cutover + deprecation | Wk 12–14 | Monolith reads-only → decommission | High |

- **Shadow mode (P2):** Both paths run in parallel; results diffed automatically — no business risk
- **Rollback:** Feature flag disables new path per payer in < 60 s

<!-- SPEAKER NOTES — Slide 10: Migration Plan
A phased plan with a concrete rollback story is what separates a credible architecture proposal from a whiteboard sketch. Walk through each phase and its risk rating. Emphasize shadow mode in Phase 2 — this is the highest-value risk mitigator in the entire plan. By running the new Rules Engine in parallel and diffing outputs against the monolith, you can validate correctness for weeks before any business traffic touches the new path. The feature flag rollback is also critical for a healthcare context: if a payer-specific edge case causes incorrect adjudication, you can disable the new path for that payer in under 60 seconds without a deployment. Expected question: "What does dual-write in Phase 1 mean for DB consistency?" — answer: Intake writes to the monolith DB AND publishes to the Kafka topic; the monolith continues to be the system of record until Phase 4.
-->

---

# 10 — Risks

## Identified Risks and Mitigations

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| MSK operational complexity | Medium | Medium | Runbooks + MSK managed service; Kafka training for on-call |
| Schema evolution breaking consumers | Low | High | Avro backward-compatible schema evolution enforced by registry |
| Shadow mode diff divergence | Medium | High | Automated diff alerts; P2 exit gate = 0 unresolved diffs |
| EKS cold-start latency during scale-out | Medium | Low | Pre-warm minimum 3 pods; HPA stabilization window 60 s |
| Phased migration extends beyond 14 wk | Medium | Medium | P2 has 4-week buffer; P4 can slip without customer impact |

<!-- SPEAKER NOTES — Slide 11: Risks
This slide demonstrates intellectual honesty — it is also one of the most scrutinized slides in any architecture review. Do not downplay risks. The schema evolution risk deserves extra attention: Avro backward compatibility is enforced by the Schema Registry, but it requires developer discipline. Consider proposing a PR check that validates schema changes before merge. The shadow mode exit gate is explicit: you will not advance to Phase 3 until diff alerts are at zero. This should be non-negotiable. If anyone raises a risk not on this table, add it in real time — having a blank row ready signals you expect to learn something in the review. Be prepared to discuss the "what if Kafka goes down?" scenario: answer is that MSK SLA is 99.99%, and during an outage, Intake service buffers to a local disk queue with configurable depth.
-->

---

# 11 — Timeline

## Execution Schedule

```
Wk 1–2   [P0 Infra]         ████████
Wk 3–4   [P1 Intake]                 ████████
Wk 5–8   [P2 Rules Engine]                   ████████████████
Wk 9–11  [P3 Payout]                                         ████████████
Wk 12–14 [P4 Cutover]                                                    ████████████
```

**Team:** 2 platform engineers, 1 SRE (part-time), 1 security review slot (Wk 7)
**Dependencies:** MSK quota increase request (submit this week) · SRA approval before P3

> Target GA: [Target Date] — 14 weeks from kickoff approval

<!-- SPEAKER NOTES — Slide 12 (of 12): Timeline
End with a concrete, committal timeline. The ASCII Gantt makes the schedule scannable without requiring a separate project management tool. Highlight the two dependencies that are outside engineering's control: the MSK quota increase (takes 3–7 business days from AWS) and the Security Risk Assessment approval before Phase 3. If either slips, the timeline slips — be explicit about this. The team size is intentionally small: two platform engineers keeps coordination overhead low. If you need to accelerate, the first lever is adding a second SRE to the Kafka operations track, not adding more feature developers. Close the presentation by restating what you need from the room: "We need a go/no-go decision today, and a DRI assigned for the MSK quota request." Leave 15 minutes for discussion. Have the decision slide or a blank whiteboard ready.
-->

---

# 12 — Decision

## What We Need From This Room

**Proposal:** Approve phased event-driven decomposition of Helix as described.

| Ask | Owner | Due |
|---|---|---|
| ▲ Approve architecture direction | Engineering Leadership | Today |
| → Assign DRI for MSK quota increase | Platform Team | Today |
| → Schedule SRA slot for Wk 7 | Security Team | This week |
| ○ Review and sign off on Avro schema standards | Data Platform | Wk 2 |

**If approved:** Kickoff P0 infrastructure sprint next Monday.
**If deferred:** Re-review after [specific condition] is resolved.

<!-- SPEAKER NOTES — Slide 13 — Decision (final)
This is the action slide — every architecture review should close with a concrete ask table, not open-ended discussion. The four rows map to four different owners, which prevents the "someone else will handle it" trap. Read each row aloud and confirm the owner is in the room and agrees to the timeline. If there is no decision today, document the specific condition that must be resolved before re-review — "we will revisit when ready" is not acceptable. After the meeting, send the decision log as a follow-up within 24 hours, referencing this slide. If the decision is "approved with modifications," capture the modifications explicitly before leaving the room.
-->
