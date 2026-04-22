<!-- TEMPLATE: postmortem-deck
     CATEGORY: Technical
     USE WHEN: presenting a post-incident review to engineering and stakeholders
     SLIDE COUNT: 9
     PALETTE: Dark dev with red/amber incident accents
     RENDER: marp --pptx 23-postmortem-deck.md -->
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
    color: #f06070;
    letter-spacing: -0.3px;
    font-size: 1.8em;
    border-bottom: 2px solid #2a1520;
    padding-bottom: 12px;
    margin-bottom: 24px;
  }
  h2 { color: #f0a050; font-size: 1.3em; margin-top: 0; }
  h3 { color: #8899ac; font-size: 1em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; }
  p, li { color: #d0d8e4; line-height: 1.6; }
  strong { color: #f0a050; }
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
    border-left: 3px solid #f06070;
    border-radius: 0 4px 4px 0;
  }
  pre code { background: transparent; padding: 0; color: #d0d8e4; }
  table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
  th { background: #1a0e10; color: #f06070; padding: 10px 14px; text-align: left; border-bottom: 2px solid #2a1520; }
  td { padding: 9px 14px; border-bottom: 1px solid #1a2535; color: #d0d8e4; }
  tr:nth-child(even) td { background: #0d1117; }
  blockquote { border-left: 3px solid #f0a050; padding: 8px 16px; background: #120d08; margin: 16px 0; }
  blockquote p { color: #f0a050; margin: 0; }
  .sev1 { color: #f06070; font-weight: 700; }
  .sev2 { color: #f0a050; font-weight: 700; }
  section.title { justify-content: center; }
  section.title h1 { font-size: 2.2em; border: none; padding-bottom: 0; color: #f06070; }
  section.title h2 { color: #8899ac; font-weight: 400; font-size: 1em; }
---
<!-- _class: title -->

# Post-Incident Review
## Helix Claims Pipeline Outage — 2024-11-14

**Severity:** SEV-1 &nbsp;|&nbsp; **Duration:** 3h 22m &nbsp;|&nbsp; **Lead:** [On-Call Name]
**Status:** Complete — Action items assigned

<!-- SPEAKER NOTES — Slide 1: Title
Set the tone immediately: this is a blameless post-mortem. The goal is to understand what happened, not to assign fault. If anyone in the room was directly involved in the incident, acknowledge their effort in responding — incidents are handled by people under pressure with incomplete information. State your norms up front: "We will identify system and process failures, not individual errors. Every finding leads to an action item, not a performance note." The SEV-1 classification means this had direct customer impact. Leadership may be in the room — that is expected and healthy for SEV-1s.
-->

---

# 1 — Incident Overview

## What Happened

- **Start:** 2024-11-14 14:07 PST — Claims adjudication latency began climbing
- **Peak impact:** 14:31 PST — 100% of claims failing; clearing house ACKs timing out
- **Resolution:** 17:29 PST — full service restored following Redis cluster failover
- **Duration:** 3 hours 22 minutes

**Impact summary:**
- **42,000 claims** unprocessed during outage window
- **3 clearing houses** triggered timeout alerts and suspended submissions
- **0 claims lost** — all buffered in DLQ, reprocessed within 4 hours of resolution

> No PHI exposure. No data loss. Regulatory notification not required.

<!-- SPEAKER NOTES — Slide 2: Incident Overview
Lead with the timeline and then immediately state what was NOT affected — no data loss, no PHI exposure. In a healthcare context, the first question from leadership is always "was patient data affected?" Answer that before anyone asks. The 42,000 unprocessed claims sounds alarming but the "0 claims lost" finding is the critical mitigator. Have the exact DLQ reprocessing confirmation from your monitoring tool available. The three clearing houses that suspended submissions will need a formal communication — confirm with the account management team whether that has been sent. The PST timestamps should match exactly what is in the incident timeline doc — cross-reference before presenting.
-->

---

# 2 — Customer Impact

## Who Was Affected and How

| Affected Group | Impact | Duration | Status |
|---|---|---|---|
| Provider staff | Submissions rejected / timed out | 3h 22m | Resolved |
| Clearing houses (3 of 7) | Suspended batch submissions | 3h 22m | Resumed 18:15 PST |
| Member portal (claim status) | Stale status displays | 4h 10m (post-incident) | Resolved after reprocessing |
| Internal claims team | Manual review queue spiked | 4h | Cleared 21:00 PST |

**Financial impact estimate:** [TBD — finance team calculating SLA credit liability]

**Communications sent:**
- 14:45 PST — Status page updated to "Investigating"
- 15:10 PST — Clearing house notification sent
- 17:35 PST — Status page updated to "Resolved"

<!-- SPEAKER NOTES — Slide 3: Customer Impact
Impact quantification is essential for SEV-1 reviews. The table maps each affected group to their specific experience, not just "service was down." The member portal stale status display is a secondary impact that often gets overlooked — the DLQ reprocessing took 48 minutes after service restoration, during which members would see incorrect claim statuses. The financial impact estimate should be finalized before the next stakeholder communication — the "TBD" is appropriate for the internal review, not for the external incident report. The communications timeline is important for two reasons: it shows response discipline, and it is likely to be audited if a clearing house files an SLA claim. Confirm exact timestamps from the PagerDuty incident timeline, not from memory.
-->

---

# 3 — Incident Timeline

## Minute-by-Minute Reconstruction

```
14:07 PST  Redis primary node CPU spikes to 94% — no alert fires
14:09 PST  Rules Engine consumers begin timing out on Redis reads
14:12 PST  DLQ depth starts climbing; no alert threshold set
14:18 PST  PagerDuty alert fires: "Kafka consumer lag > 10,000"
14:22 PST  On-call (Kim) begins investigation; suspects Kafka issue
14:31 PST  Claims 100% failing; clearing house ACKs timing out
14:45 PST  Status page updated; escalation to Platform team
15:03 PST  Platform identifies Redis as root cause (not Kafka)
15:40 PST  Redis failover initiated; secondary elected as primary
16:12 PST  Redis primary stable; consumer lag begins decreasing
17:29 PST  Full service restored; all consumers healthy
17:35 PST  Status page updated to Resolved
21:00 PST  DLQ fully reprocessed; claims team queue cleared
```

<!-- SPEAKER NOTES — Slide 4: Incident Timeline
The timeline is the most factual slide in the post-mortem — every entry should be sourced from a log timestamp or PagerDuty event, not from memory. If there are gaps in the timeline (periods where no one knew what was happening), leave them in — they often reveal detection and response gaps. Note the 11-minute delay between the first sign (CPU spike at 14:07) and the PagerDuty alert at 14:18 — this is a detection gap that belongs in the root cause analysis. Also note the misdiagnosis: on-call initially suspected Kafka, not Redis. This is not a failure of the responder — it is a system observability gap, because the Redis CPU alert was not configured. Each of these gaps generates an action item on a later slide.
-->

---

# 4 — Detection

## How Long Did It Take to Know Something Was Wrong?

| Signal | Time | Lag From Incident Start | Alert? |
|---|---|---|---|
| Redis CPU 94% | 14:07 PST | 0 min | ✗ No alert |
| Rules Engine timeouts | 14:09 PST | 2 min | ✗ No alert |
| DLQ depth climbing | 14:12 PST | 5 min | ✗ No threshold set |
| Kafka consumer lag | 14:18 PST | 11 min | ✓ PagerDuty fired |
| Clearing house complaints | 14:30 PST | 23 min | (external) |

**Detection gap: 11 minutes** — the only alert that fired was a downstream symptom, not the root cause.

> We were alerted to a symptom (Kafka lag) 11 minutes after the cause (Redis CPU). This is a monitoring gap, not a responder failure.

<!-- SPEAKER NOTES — Slide 5: Detection
Detection analysis is often the most actionable part of a post-mortem. The table makes it clear that we had four visible signals before the alert fired, and none of them triggered a page. This is a systemic monitoring gap — three separate metrics lacked alert thresholds. The pull-quote at the bottom explicitly frames this as a system failure, not a responder failure. This is critical for maintaining blameless culture. Emphasize that Kim responded appropriately given the alert that fired — the initial Kafka diagnosis was reasonable based on the information available. The action items from this slide are clear: add Redis CPU alerting, add DLQ depth alerting, add Rules Engine timeout rate alerting. These should all be in the action items slide.
-->

---

# 5 — Root Cause

## What Actually Caused the Outage

**Immediate cause:**
Redis primary node exhausted available memory due to a misconfigured `maxmemory-policy` setting, causing the node to begin evicting keys under the default `noeviction` policy — which halted all write operations rather than evicting old keys.

**Why this happened:**
- A configuration change on 2024-11-13 (HLX-deploy-441) increased the Avro payload compression level, unintentionally increasing Redis value sizes by ~2.3×
- The Redis cluster was operating at 78% memory utilization before the deployment — no capacity review was part of the deploy checklist
- `maxmemory-policy` was set to `noeviction` — the safe default for a cache where eviction would cause data loss, but catastrophic for an availability-critical path

<!-- SPEAKER NOTES — Slide 6: Root Cause
The root cause slide requires precision — "Redis ran out of memory" is not a root cause, it is a symptom. The real root cause is the combination of: a configuration change that increased payload size, insufficient capacity headroom, and a Redis policy that prioritized data integrity over availability. Walk through the causal chain clearly: compression level change → larger payloads → Redis memory pressure → noeviction policy triggered → write halt → pipeline failure. The "Why this happened" section covers the contributing system conditions, not individual decisions. Avoid language like "the engineer misconfigured" — use "the deploy checklist did not include a Redis capacity review." This is a process gap, not a human error.
-->

---

# 6 — Contributing Factors

## What Made This Worse Than It Should Have Been

- **Monitoring gap:** No alert on Redis memory utilization or write rejection rate
- **Deploy process gap:** No Redis capacity review step in the deployment checklist
- **Runbook gap:** No documented procedure for Redis memory pressure recovery — responders improvised
- **Alert routing:** Kafka consumer lag alert went to on-call (backend), not to Platform (Redis owners) — added 41 minutes to diagnosis
- **Configuration drift:** `maxmemory-policy` was set at cluster creation in 2022 and never reviewed against current usage patterns

> None of these are individual failures. All are system design gaps.

<!-- SPEAKER NOTES — Slide 7: Contributing Factors
Contributing factors are distinct from root cause — they are conditions that made the incident worse or longer, even if they did not cause it. The alert routing issue is particularly important: the Kafka consumer lag alert fired to the backend on-call, who correctly escalated to Platform, but that handoff took 41 minutes. If the alert had gone to Platform directly, the Redis diagnosis might have been reached 30–40 minutes earlier, potentially halving the outage duration. The configuration drift issue (maxmemory-policy set in 2022 and never reviewed) is a common systems debt pattern — it belongs in the action items as a configuration audit task. Emphasize the closing statement: these are all system gaps with clear remediation paths.
-->

---

# 7 — Action Items

## What We Are Doing About It

| # | Action | Owner | Due | Priority |
|---|---|---|---|---|
| A1 | Add Redis memory utilization alert (threshold: 70%) | Platform | Nov 21 | High |
| A2 | Add DLQ depth alert (threshold: 50 messages, 5 min) | Backend | Nov 21 | High |
| A3 | Add Redis write rejection rate alert | Platform | Nov 21 | High |
| A4 | Add Redis capacity review to deploy checklist | Platform | Nov 28 | High |
| A5 | Update `maxmemory-policy` to `allkeys-lru` + document | Platform | Nov 21 | High |
| A6 | Write Redis memory pressure runbook | Platform | Nov 28 | Medium |
| A7 | Fix alert routing — Redis alerts → Platform on-call | Platform | Nov 21 | High |
| A8 | Audit all Redis cluster configurations across envs | Platform | Dec 5 | Medium |

<!-- SPEAKER NOTES — Slide 8: Action Items
Action items are the most important output of a post-mortem. Every finding must have an owner, a due date, and a priority — "team" is not an owner. The five High-priority items with Nov 21 due dates address the immediate detection and response gaps. The Medium-priority items address longer-term systemic risk. At the end of this meeting, confirm every owner verbally — do not let anyone leave without acknowledging their action items. Schedule a 30-minute check-in for Nov 21 to confirm the High-priority items are done. The Dec 5 configuration audit (A8) is likely to surface additional drift — budget time for follow-up action items from that audit.
-->

---

# 8 — Learnings

## What This Incident Taught Us

**Technical learnings:**
- `noeviction` is the wrong `maxmemory-policy` for an availability-critical cache path — prefer `allkeys-lru` with appropriate TTLs
- Payload size changes have non-obvious downstream effects on cache infrastructure — require explicit impact assessment

**Process learnings:**
- Deploy checklists must include infrastructure capacity reviews for any change that affects data size
- Alert ownership should match service ownership — cross-team routing adds diagnosis latency

**What went well:**
- DLQ buffering prevented data loss — the decision to use DLQ in the idempotency design was validated
- On-call response was rapid and methodical — escalation happened within 4 minutes of alert

<!-- SPEAKER NOTES — Slide 9: Learnings (final)
Ending with learnings — including what went well — is critical for blameless culture. The "what went well" section is not a consolation prize: it identifies the design decisions and behaviors that should be reinforced. The DLQ buffering specifically prevented what could have been a data loss incident on top of an availability incident — that design decision saved significant remediation work. The on-call escalation speed was genuinely good. Acknowledge it. The technical and process learnings should be written to the engineering knowledge base after this review. Use the `knowledge-base-extractor` skill to promote these findings to the domain knowledge base for future reference. Close by thanking everyone who responded to the incident — their work under pressure is what kept the impact bounded.
-->
