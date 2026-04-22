<!-- TEMPLATE: launch-readiness
     CATEGORY: Technical
     USE WHEN: presenting a go/no-go decision to approve a feature for production
     SLIDE COUNT: 11
     PALETTE: Corporate hybrid (cream bg, navy headings, electric blue accents)
     RENDER: marp --pptx 27-launch-readiness.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'DM Sans', 'Segoe UI', system-ui, sans-serif;
    background: #f7f4ef;
    color: #2c3340;
    padding: 48px 60px;
  }
  h1 {
    font-family: 'DM Mono', 'Cascadia Code', monospace;
    color: #0e1b2e;
    letter-spacing: -0.3px;
    font-size: 1.75em;
    border-bottom: 2px solid #d8d2c6;
    padding-bottom: 12px;
    margin-bottom: 22px;
  }
  h2 { color: #3b9eff; font-size: 1.2em; margin-top: 0; }
  h3 { color: #8899ac; font-size: 0.9em; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; }
  p, li { color: #2c3340; line-height: 1.65; }
  strong { color: #0e1b2e; font-weight: 700; }
  em { color: #3b9eff; font-style: normal; font-weight: 600; }
  code {
    font-family: 'DM Mono', 'Cascadia Code', monospace;
    background: #e8e2d8;
    padding: 2px 6px;
    border-radius: 3px;
    color: #4a5568;
    font-size: 0.9em;
    border: 1px solid #d0c8ba;
  }
  pre {
    background: #e8e2d8;
    padding: 16px 20px;
    border-left: 3px solid #3b9eff;
    border-radius: 0 4px 4px 0;
    border: 1px solid #d0c8ba;
  }
  pre code { background: transparent; padding: 0; color: #2c3340; border: none; font-size: 0.9em; }
  table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
  th { background: #0e1b2e; color: #f7f4ef; padding: 10px 14px; text-align: left; border-bottom: none; font-family: 'DM Mono', monospace; font-size: 0.85em; }
  td { padding: 9px 14px; border-bottom: 1px solid #d8d2c6; color: #2c3340; }
  tr:nth-child(even) td { background: #f0ece4; }
  blockquote { border-left: 3px solid #3b9eff; padding: 10px 16px; background: #eae6de; margin: 16px 0; border-radius: 0 4px 4px 0; }
  blockquote p { color: #0e1b2e; margin: 0; font-weight: 600; }
  .go { color: #2a7d4f; font-weight: 700; }
  .nogo { color: #b91c1c; font-weight: 700; }
  .conditional { color: #92400e; font-weight: 700; }
  section.title { justify-content: center; background: #0e1b2e; }
  section.title h1 { color: #f7f4ef; border-bottom-color: #1a2e48; font-size: 2.2em; }
  section.title h2 { color: #3b9eff; font-weight: 400; font-size: 1.1em; }
  section.title p { color: #8899ac; font-size: 0.9em; }
---
<!-- _class: title -->

# Helix — Launch Readiness Review
## Idempotent Retry Framework — Production Go/No-Go

**Feature:** HLX-0047 &nbsp;|&nbsp; **Target Launch:** [Date] &nbsp;|&nbsp; **DRI:** [Name]
**Audience:** Engineering, Product, SRE, Security

<!-- SPEAKER NOTES — Slide 1: Title
A launch readiness review is a gate, not a presentation. The outcome is a binary decision: GO, NO-GO, or CONDITIONAL GO with specific conditions and timelines. Be explicit about the format from the first slide. Identify the decision maker (usually VP Engineering or CTO) before beginning. Everyone else is an advisor. The DRI is accountable for ensuring all conditions are met before launch — confirm that person is in the room. If this is a SEV-1-risk launch (large surface area, healthcare data), consider whether the security team needs a separate pre-brief before this meeting.
-->

---

# 1 — Feature Overview

## What Is Launching

**HLX-0047 — Idempotent Retry Framework for Claims Adjudication**

- Prevents duplicate claim adjudications when providers re-submit claims
- Adds configurable exponential back-off with jitter for transient failures
- Routes exhausted-retry claims to dead-letter queue for manual review
- No user-visible surface — operational reliability improvement only

**Why now:**
- Provider SLA compliance review in [Month] — drop rate must be ≤ 0.05% before then
- Current drop rate: **0.31%** — 6× above target

**Feature flag:** `HELIX_IDEMPOTENCY_ENABLED` — controls rollout per environment/payer

<!-- SPEAKER NOTES — Slide 2: Feature Overview
Keep the feature summary brief — everyone in a launch readiness review should already have context from the RFC or design review. Emphasize the feature flag: this is the single most important risk mitigation for a launch readiness review. If the feature flag is not in place, the review should not proceed. The "why now" context is important for timing — the SLA review is a hard external deadline. If this launch is postponed, there is a real contractual consequence. State that consequence explicitly so the NO-GO decision carries appropriate weight.
-->

---

# 2 — Scope

## What Is and Is Not in Scope for This Launch

**In scope:**
- ✓ Real-time claim submissions (all payers, all claim types)
- ✓ Batch EDI submissions
- ✓ Retry with exponential back-off (3 attempts, 1 s → 8 s → 64 s)
- ✓ Dead-letter queue routing with alerting

**Out of scope (future releases):**
- ✗ Retroactive reprocessing of historical dropped claims
- ✗ Provider-facing retry status UI
- ✗ Configurable retry count per payer

**Known limitations at launch:**
- DLQ reprocessing is manual — provider operations team must initiate via runbook
- Idempotency key TTL is fixed at 24 hours — configurable TTL is post-launch

<!-- SPEAKER NOTES — Slide 3: Scope
Scope creep in launch reviews is common — someone will suggest adding a capability "since we are already in there." Use this slide to anchor the room on the agreed scope from the RFC. The "known limitations" section is important for setting expectations with Product and Customer Success: if they have communicated something to providers that is not in scope, you need to know now, not after launch. Confirm with Product whether the manual DLQ reprocessing process has been communicated to the provider operations team — they need to be trained on the runbook before launch day.
-->

---

# 3 — Testing Summary

## Test Coverage and Results

| Test Category | Count | Pass Rate | Notes |
|---|---|---|---|
| Unit tests | 147 | 100% | All idempotency paths covered |
| Integration tests | 38 | 100% | Redis, Kafka, DLQ paths |
| E2E tests (staging) | 22 | 100% | Happy path + failure scenarios |
| Load test (10k msg/s, 30 min) | — | Passed | P99 latency delta: +4 ms (target: < 20 ms) |
| Chaos test (Redis failover) | — | Passed | Failover completed in 38 s; no claims lost |
| Duplicate submission test | — | Passed | 1,000 duplicate submissions → 0 double adjudications |
| Security scan | — | Passed | No high/critical findings (SAST + dependency audit) |

**Coverage:** 94% line, 89% branch — above 80% floor.

<!-- SPEAKER NOTES — Slide 4: Testing Summary
This is the most scrutinized slide in a launch readiness review. Every row must have a real result, not a placeholder. The load test P99 delta (+4 ms against a 20 ms threshold) is a key number — explain where the 20 ms threshold came from (it is 2.5% of the claims pipeline SLA budget). The chaos test result (38 s failover with no claims lost) demonstrates that the DLQ buffering works as designed. The duplicate submission test (1,000 submissions, 0 double adjudications) is the direct validation of the core feature claim. If any test failed and was subsequently fixed, document that — don't omit it. Reviewers will ask whether all tests passed on the first run or after fixes.
-->

---

# 4 — Performance Results

## Latency and Throughput Under Load

**Baseline (without feature):**

| Metric | P50 | P95 | P99 |
|---|---|---|---|
| Claim adjudication latency | 118 ms | 340 ms | 892 ms |
| Redis read (schema cache) | 0.8 ms | 2.1 ms | 4.2 ms |

**With feature enabled (load test, 10k msg/s):**

| Metric | P50 | P95 | P99 | Delta |
|---|---|---|---|---|
| Claim adjudication latency | 120 ms | 344 ms | 896 ms | +4 ms |
| Redis idempotency lookup | 0.9 ms | 2.3 ms | 4.6 ms | +0.4 ms |
| DLQ write (failure path) | 6 ms | 14 ms | 28 ms | N/A (new) |

**Verdict:** ✓ Within SLA budget. No degradation beyond acceptable threshold.

<!-- SPEAKER NOTES — Slide 5: Performance Results
The before/after table format makes the performance impact immediately comparable. The +4 ms P99 delta is within the 20 ms threshold and leaves substantial headroom before the 800 ms SLA. The Redis idempotency lookup numbers are important for the Platform team — they validate that the Redis cluster can handle the additional load without memory or throughput issues. The DLQ write latency is a new metric with no baseline comparison — explain that DLQ writes are on the failure path only (affecting ~0.31% of claims) and thus not in the critical path for SLA compliance. Have the full load test report available in a linked document — reviewers may want to see the full time series, not just percentiles.
-->

---

# 5 — Security Review

## Security Assessment Summary

**Review type:** Pre-launch security review (SAST + manual review of auth boundaries)
**Reviewer:** [Security Team / Name] &nbsp;|&nbsp; **Date:** [Date]

| Area | Finding | Status |
|---|---|---|
| Authentication | No new auth surface — internal service only | ✓ Clear |
| Authorization | IAM role scope unchanged — no new permissions | ✓ Clear |
| PHI handling | Idempotency key does not contain PHI (SHA-256 hash of claim fields) | ✓ Clear |
| Redis data | Payload compressed but not encrypted — acceptable for internal cluster | ✓ Accepted |
| Dependency scan | 0 high/critical CVEs in added dependencies | ✓ Clear |

**Security verdict:** ✓ APPROVED for production.

<!-- SPEAKER NOTES — Slide 6: Security Review
A formal security review result must be presented by the security reviewer or confirmed in writing. Do not present security findings on behalf of the security team without their explicit sign-off. The "Redis data not encrypted" finding with "Accepted" status is important — this was a deliberate decision documented in the design review. The rationale is that the Redis cluster is internal-only, the data is compressed (not cleartext), and encrypting individual Redis values would add ~1.5 ms per operation, which was deemed not justified given the internal-only access pattern. If the security reviewer disagrees with this acceptance, it is a NO-GO condition. Confirm the security approval in writing (Slack or email) before this meeting.
-->

---

# 6 — Rollout Plan

## Production Launch Sequence

| Stage | Traffic | Duration | Success Gate |
|---|---|---|---|
| Stage 0: Dark launch | 0% (shadow mode, log only) | 24 hours | Zero unexpected errors in shadow logs |
| Stage 1: Canary | 5% (Blue Shield payer only) | 48 hours | DLQ depth < 10, drop rate < 0.1% |
| Stage 2: Expansion | 25% → 50% → 100% | 72 hours | Drop rate ≤ 0.05%, P99 delta < 20 ms |
| Stage 3: Full traffic | 100% | Ongoing | 14-day bake period |

**Feature flag:** `HELIX_IDEMPOTENCY_ENABLED=true` per payer in LaunchDarkly

**Rollback procedure (all stages):**
→ Set `HELIX_IDEMPOTENCY_ENABLED=false` in LaunchDarkly for affected payers
→ Confirm consumer lag returns to baseline within 5 minutes
→ Page Platform if lag does not recover within 10 minutes

<!-- SPEAKER NOTES — Slide 7: Rollout Plan
The staged rollout with explicit success gates is the most important risk mitigation in the launch plan. The 24-hour dark launch (shadow mode) is a zero-risk first step — it exercises the code path without affecting production behavior. If dark launch reveals unexpected errors, you stop before Stage 1 without any customer impact. For Stage 1, choosing Blue Shield as the canary payer should be justified — they should be a payer with high enough volume to be statistically meaningful but not so large that an incident would be catastrophic. Confirm this choice with the product team. The rollback procedure must be tested before Stage 1 — add a "verify rollback works" step to the Stage 0 checklist.
-->

---

# 7 — Rollback Plan

## If Something Goes Wrong

**Rollback decision criteria (immediately roll back if ANY of these are true):**
- DLQ depth > 200 sustained for 5 minutes
- Claim adjudication P99 > 1,500 ms
- Error rate > 1% on any single payer for 3 consecutive minutes
- Any SEV-1 or SEV-2 incident attributed to the new feature

**Rollback procedure:**
```
1. Disable feature flag in LaunchDarkly: HELIX_IDEMPOTENCY_ENABLED=false
2. Confirm consumer lag recovery (target: < 5 min)
3. Verify drop rate returns to pre-launch baseline
4. Page on-call if any DLQ items need manual reprocessing
5. Notify stakeholders via #helix-incidents
```

**Data state after rollback:** DLQ items remain intact; reprocess after root cause identified.

<!-- SPEAKER NOTES — Slide 8: Rollback Plan
A launch readiness review cannot approve a launch without a documented, tested rollback plan. The four decision criteria should be reviewed by the SRE team before this meeting — they will likely add or modify thresholds based on their on-call experience. The step-by-step rollback procedure should be in the runbook (linked in the slide or notes) and not just in the deck. The "Data state after rollback" note is critical for a claims system: healthcare data cannot be lost. Confirm that DLQ items are durable and will survive a rollback — they are stored in Kafka with standard replication, so yes. State this explicitly.
-->

---

# 8 — Monitoring and Alerting

## What Gets Watched Post-Launch

| Signal | Metric Name | Alert Threshold | Severity |
|---|---|---|---|
| DLQ depth | `helix.idempotency.dlq_depth` | > 50 for 5 min | P2 |
| Idempotency hit rate | `helix.idempotency.hit_rate` | < 0.1% (suspicious) | P3 |
| Retry attempt distribution | `helix.retry.attempt_distribution` | P99 attempts > 2 | P2 |
| Claims drop rate | `helix.claims.drop_rate` | > 0.1% | P1 |
| Redis memory utilization | `aws.elasticache.freeable_memory` | < 20% available | P2 |

**Dashboard:** `[Grafana dashboard link]`
**Runbook:** `[Confluence runbook link]`
**On-call rotation:** Platform team primary, Backend team secondary for 14-day bake period.

<!-- SPEAKER NOTES — Slide 9: Monitoring and Alerting
Every metric in this table should already be live in the monitoring stack before this meeting. If any metric does not exist yet, it is a NO-GO condition. The on-call rotation assignment (Platform primary, Backend secondary for 14 days) should be confirmed with the Platform and Backend team leads in this meeting — do not assume it. The idempotency hit rate lower bound alert (< 0.1%) is an unusual alert: if the feature is working correctly, you expect to see some duplicate submissions. If hit rate is zero, either there are no retries (suspicious given historical data) or the idempotency key generation is broken. Explain this logic to the SRE team before the meeting so the alert is not dismissed as a false positive.
-->

---

# 9 — On-Call Readiness

## Is the Team Ready to Support This?

| Readiness Area | Status | Owner |
|---|---|---|
| Runbook published and reviewed | ✓ Complete | [Name] |
| On-call rotation briefed | ✓ Complete | Platform TL |
| PagerDuty routing rules configured | ✓ Complete | SRE |
| Redis failover procedure tested | ✓ Tested in staging | Platform |
| DLQ manual reprocessing tested | ✓ Tested in staging | Backend |
| Provider ops team trained | ✓ Brown bag held [Date] | [Name] |
| Rollback tested in staging | ✓ Verified | Platform |

**On-call coverage confirmed for launch window:** [Date range]

<!-- SPEAKER NOTES — Slide 10: On-Call Readiness
Every row in this table must be ✓ Complete before GO is declared. Any ✗ or "In Progress" is a NO-GO condition or a CONDITIONAL GO with a specific completion date. The provider ops team training is often the last item completed — confirm it was done and who attended. If the rollback was tested in staging, describe what the test looked like: "We ran a feature flag toggle during an active load test and confirmed consumer lag recovered within 3 minutes." Concrete evidence is more credible than a checkbox. Ask the SRE lead to verbally confirm on-call coverage for the launch window — do not rely on a calendar invite alone.
-->

---

# 10 — Risks

## Outstanding Risks at Launch

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| Redis memory pressure at open enrollment (3× volume) | Medium | High | Redis cluster right-sized for 4 M claims/day; monitor utilization alert |
| DLQ growth if new payer-specific edge cases surface | Low | Medium | P2 alert at depth 50; manual reprocess runbook ready |
| Shadow mode reveals unexpected compatibility issue | Low | High | Shadow mode precedes Stage 1 by 24 hours; stop gate before customer impact |
| On-call ramp time on new Redis metrics | Medium | Low | Pre-brief scheduled for on-call rotation; runbook covers all alert paths |

> No critical risk blocks launch. All risks have active mitigations and monitoring coverage.

<!-- SPEAKER NOTES — Slide 11: Risks
The risk table should be presented to the decision maker as a "here is what we know, here is how we are managing it" statement — not as a reason to delay. The pull-quote at the bottom is the risk verdict: no risk is unmitigated or unknown. If there are any UNKNOWN risks or risks with NO mitigation, they are NO-GO conditions. The open enrollment volume risk is worth extra discussion: the right-sizing claim ("sized for 4 M claims/day") should be validated by the Platform team, not just asserted by the feature DRI. Get that validation before this meeting.
-->

---

# 11 — Go / No-Go

## Decision

**GO conditions — all must be true:**
- ✓ All tests passing (147 unit, 38 integration, 22 E2E)
- ✓ Security review approved
- ✓ Monitoring and alerting live
- ✓ Rollback tested and confirmed
- ✓ On-call rotation briefed and coverage confirmed
- ✓ Runbook published

**Current status: ALL CONDITIONS MET**

> Recommendation: **GO** — launch Stage 0 (dark launch) on [Date] at [Time] PST

**Decision maker:** [Name] &nbsp;|&nbsp; **Decision by end of this meeting**

<!-- SPEAKER NOTES — Slide 12 (final): Go/No-Go
The final slide is the decision. Read each GO condition aloud and confirm its status. If any condition is NOT MET, state the specific action needed and the timeline to resolve before returning to the launch decision. The decision maker should state their decision verbally and on record. After the meeting, send a decision confirmation email within 1 hour with: decision, conditions met, launch timeline, and any conditions placed on a CONDITIONAL GO. If the decision is NO-GO, document the specific conditions that must be met and schedule a re-review date. Do not leave the meeting without a committed re-review date.
-->
