<!-- TEMPLATE: rfc-presentation
     CATEGORY: Technical
     USE WHEN: pitching an RFC to get stakeholder buy-in before formal approval
     SLIDE COUNT: 10
     PALETTE: Dark dev
     RENDER: marp --pptx 26-rfc-presentation.md -->
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
  table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
  th { background: #111820; color: #3b9eff; padding: 10px 14px; text-align: left; border-bottom: 2px solid #1a2535; }
  td { padding: 9px 14px; border-bottom: 1px solid #1a2535; color: #d0d8e4; }
  tr:nth-child(even) td { background: #0d1117; }
  blockquote { border-left: 3px solid #2dd4a0; padding: 8px 16px; background: #0d1117; margin: 16px 0; }
  blockquote p { color: #2dd4a0; margin: 0; }
  section.title { justify-content: center; }
  section.title h1 { font-size: 2.2em; border: none; padding-bottom: 0; }
  section.title h2 { color: #8899ac; font-weight: 400; font-size: 1em; }
---
<!-- _class: title -->

# Helix — RFC Presentation
## HLX-0052: Unified Schema Registry for Claims Data Contracts

**Author:** [Name] &nbsp;|&nbsp; **RFC Status:** Draft &nbsp;|&nbsp; **Date:** [YYYY-MM-DD]
**Review window:** [Start] – [End]

<!-- SPEAKER NOTES — Slide 1: Title
An RFC presentation is different from an architecture review — the audience is here to give formal feedback, not just absorb information. State the RFC number and link the written document before beginning. Clarify the review window: stakeholders need to know whether their feedback today is sufficient or whether written comments are also expected. If this is a pre-read RFC (you asked people to read it before the session), acknowledge that: "I know some of you have already read the RFC — this presentation is a structured walk-through to surface questions, not a replacement for the written doc." Keep the RFC doc open in another browser tab in case someone references a specific section number.
-->

---

# 1 — Problem Statement

## What We Are Trying to Solve

Helix services currently manage **7 independent schema definitions** across 4 teams with no shared registry:

- Schema changes require **manual coordination** — 3 Slack threads per change average
- Breaking changes have caused **2 production incidents** in the past 6 months
- New services spend **avg. 3 days** discovering and documenting the data contracts they need
- No source of truth for schema version history — rollback requires reading git blame

> The cost of undocumented data contracts compounds with every new service we add.

<!-- SPEAKER NOTES — Slide 2: Problem Statement
Ground the RFC in quantified pain before proposing anything. The four bullets should all be sourced from real data — the "3 Slack threads per change" figure should come from a Slack analytics export or a rough count from a known incident. If you do not have exact numbers, frame them as estimates: "approximately 3 Slack threads." The two production incidents should be referenced by incident number if they are public to the audience. The pull-quote is the thesis: this is a compounding problem, not a fixed cost. Every new service makes the problem worse. This framing supports investment in a solution.
-->

---

# 2 — Proposal Summary

## What HLX-0052 Proposes

**Core proposal:** Adopt a centralized schema registry (Confluent Schema Registry, self-hosted on MSK) as the single source of truth for all Helix data contracts.

**Three capabilities this unlocks:**
- **Schema validation at produce time** — producers rejected if schema violates registered contract
- **Consumer auto-discovery** — services query registry for schema instead of checking documentation
- **Compatibility enforcement** — registry blocks backward-incompatible schema changes without approval

**What this does NOT change:**
- Topic naming conventions (separate RFC)
- Ownership model for schemas (teams still own their schemas)
- Existing clients — migration is opt-in with 90-day deprecation window

<!-- SPEAKER NOTES — Slide 3: Proposal Summary
The proposal summary should be short enough that a reviewer can repeat it in a meeting they attend later. Three capabilities is the right level of detail for a summary slide — go deeper in the Design slide. The "what this does NOT change" section is critical for managing scope creep and stakeholder anxiety: people will immediately wonder if this changes their team's ownership model, and the answer is no. The 90-day deprecation window for migration is a specific, negotiable commitment — reviewers may push for longer or shorter. Be prepared to explain why 90 days is appropriate.
-->

---

# 3 — Design

## How It Works

```
[Producer Service]
    ↓ register schema (first time) / validate schema (subsequent)
[Schema Registry API]  ←→  [Schema Store (ZooKeeper / Kafka internal topic)]
    ↑ fetch schema by ID or subject
[Consumer Service]
```

**Schema subject naming convention:**
```
{environment}.{domain}.{entity}.{version}

Examples:
  prod.claims.adjudication-result.v1
  prod.claims.member-eligibility.v2
  staging.payout.disbursement-event.v1
```

**Compatibility modes per subject:** `BACKWARD` (default), `FORWARD`, `FULL` (opt-in per schema)

<!-- SPEAKER NOTES — Slide 4: Design
The ASCII diagram for the registry integration is intentionally simple — the key insight is that the registry sits between producer and consumer as an intermediary for schema negotiation, not as a data plane. Walk through the subject naming convention carefully: the four-part convention (env.domain.entity.version) is a new standard that all teams will need to adopt. This will generate questions about migration of existing subjects. The compatibility mode table deserves explanation: BACKWARD (default) means new schema can read old data; FORWARD means old schema can read new data; FULL means both. Most teams should use BACKWARD — they write new schemas to read historical data. FULL is for high-stakes schemas where both forward and backward compatibility are required.
-->

---

# 4 — Alternatives Considered

## Other Approaches Evaluated

| Alternative | Why Not Chosen |
|---|---|
| Git-based schema repo (current + formalized) | No runtime validation; still requires Slack coordination for changes |
| AWS Glue Schema Registry | Kafka-native path limited; additional AWS dependency; vendor lock-in |
| Custom service (build our own) | Build + maintenance cost exceeds self-hosted Confluent SR; no community |
| Protobuf IDL in each service repo | Solves versioning but not discovery or runtime enforcement |

**Why Confluent Schema Registry:**
- Native Kafka/Avro integration (already using Avro post-architecture-review)
- Widely deployed — strong community, known operational patterns
- Self-hosted on MSK keeps cost within existing infrastructure

<!-- SPEAKER NOTES — Slide 5: Alternatives Considered
The alternatives table preempts the most common objection questions. Walk through each row briefly — the goal is not to re-litigate each option, but to show the analysis was done. The "Git-based schema repo" alternative will resonate with anyone who has proposed that as a simpler solution — acknowledge its appeal and explain specifically why runtime validation changes the calculus. The Glue Schema Registry alternative should be addressed carefully: it is a valid managed option, but the Kafka-native path limitations (Glue SR works better with Avro on Glue Catalog than with MSK directly) are a real technical constraint. Confirm this with the Platform team before presenting.
-->

---

# 5 — Trade-offs

## What We Gain and What We Accept

**What we gain:**
- Single source of truth for all data contracts — eliminates coordination overhead
- Automated compatibility enforcement — breaking changes blocked before reaching production
- Self-documenting system — new services find schemas without reading docs

**What we accept:**
- Schema Registry is a new operational dependency — must be included in disaster recovery planning
- Registry latency adds ~2 ms per produce operation (measured on Confluent benchmark, 10k msg/s)
- Teams must learn the subject naming convention and Avro compatibility rules

**Risk accepted:** Registry downtime halts all schema registration (not existing produce/consume — schema IDs are cached). Mitigated by SR high-availability mode (3-node).

<!-- SPEAKER NOTES — Slide 6: Trade-offs
The trade-offs slide is where intellectual honesty shows. Do not frame this as all upside — every RFC has costs. The 2 ms latency addition is within acceptable bounds for the claims pipeline (P99 target is 800 ms), but state it explicitly. The "teams must learn" bullet is a real adoption cost — plan for documentation and two brown bag sessions to transfer knowledge. The "risk accepted" paragraph is critical: many teams will worry that registry downtime means claims processing stops. Clarify the client-side schema cache: once a schema ID is fetched and cached, producers and consumers can continue operating without the registry. The registry is only required for new schema registrations, not for ongoing message production.
-->

---

# 6 — Impact Assessment

## Who Is Affected and How

| Team | Impact | Migration Effort | Timeline |
|---|---|---|---|
| Claims / Intake | Low — schema already in Avro | Register existing schemas | Wk 1–2 |
| Rules Engine | Low — consumer only | Update to fetch by subject | Wk 2–3 |
| Payout | Medium — 2 schemas need refactoring | Schema cleanup + registration | Wk 3–5 |
| Audit | Low — read-only consumer | Fetch schema by subject | Wk 2–3 |
| Platform | High — owns registry infra | Deploy, HA config, monitoring | Wk 1–4 |
| New services (future) | Positive — discovery is built in | N/A | Ongoing |

**Cross-team dependency:** All schema registrations must complete before any team switches to registry-based validation.

<!-- SPEAKER NOTES — Slide 7: Impact Assessment
The per-team impact table is essential for an RFC that spans multiple teams. Each team lead in the room should be able to find their row and understand their effort and timeline. The Payout team "schema cleanup + registration" entry is worth explaining: it means their current Avro schemas have fields that would fail Confluent's compatibility check, so a one-time cleanup is needed before registration. That cleanup is already scoped in the RFC appendix — reference the specific section. The "cross-team dependency" note at the bottom is a coordination risk: if one team delays registration, other teams cannot switch to registry validation. Address this by proposing a shared migration kickoff meeting in Week 1.
-->

---

# 7 — Open Questions

## What We Need Feedback On

| # | Question | Context | Proposed Default |
|---|---|---|---|
| Q1 | Should schema registration be blocking or non-blocking during migration? | Blocking enforces adoption; non-blocking reduces migration risk | Non-blocking for 90 days |
| Q2 | Who approves schema compatibility exceptions? | Registry blocks incompatible changes; who can override? | Schema owner + Platform |
| Q3 | Should staging and production share a registry or have separate instances? | Shared reduces cost; separate provides stronger isolation | Separate instances |
| Q4 | What is the SLA for registry availability? | Currently undefined; DR plan depends on this | 99.9% (3 nines) |

<!-- SPEAKER NOTES — Slide 8: Open Questions
Open questions in an RFC presentation are structured differently from an ad-hoc Q&A — they are the specific decisions you need the stakeholder group to make. Each question has a proposed default, which signals that you have thought through the answer but need ratification. Q1 (blocking vs non-blocking) is the highest-stakes question: choosing blocking enforces adoption but could cause production incidents if a schema fails to register correctly. Non-blocking is safer for migration but allows teams to defer indefinitely. Recommend non-blocking with a hard cutover date. Q3 (shared vs separate registry) is a cost-vs-isolation trade-off: separate instances cost ~$180/mo more but provide stronger isolation for staging experiments. Get the Platform team's recommendation before the meeting if possible.
-->

---

# 8 — Timeline

## Proposed Implementation Schedule

| Phase | Duration | Deliverable |
|---|---|---|
| P0: Infrastructure | Wk 1–2 | Deploy SR on MSK; HA config; monitoring |
| P1: Schema registration | Wk 2–4 | All existing schemas registered by each team |
| P2: Consumer migration | Wk 4–6 | All consumers fetch schema from registry |
| P3: Validation enforcement | Wk 7–10 | Producer-side schema validation enabled |
| P4: Deprecation window | Wk 10–22 | Old contract documents marked deprecated; teams migrate |
| P5: Cleanup | Wk 23 | Remove deprecated docs; registry as sole source of truth |

**Review window close:** [Date]
**Implementation start (if approved):** [Date]

<!-- SPEAKER NOTES — Slide 9: Timeline
The phased timeline is important for cross-team coordination — each phase has a clear deliverable, which means teams can plan their sprint allocation. The 90-day deprecation window (Wk 10–22, approximately 12 weeks) is generous but justified for a change that affects 4 teams with existing contracts. If the review group wants to accelerate, the negotiation should happen at Phase 4 — the earlier phases are fixed by infrastructure and migration effort. Confirm the "Review window close" date before presenting — it should match the RFC document exactly. If the RFC has not received minimum required reviewers by the close date, the RFC author is responsible for soliciting additional reviews.
-->

---

# 9 — Owners

## Who Is Responsible for What

| Area | Owner | Backup |
|---|---|---|
| Schema Registry infrastructure | Platform Team (DRI: [Name]) | [Backup] |
| Registry HA and DR planning | SRE Team | Platform |
| Schema naming convention | [RFC Author] | Platform |
| Per-team migration | Each team's tech lead | [RFC Author] |
| Compatibility exception process | [RFC Author] + Platform | — |
| Documentation and training | [RFC Author] | — |

**RFC DRI:** [Name] — responsible for review completion and implementation kickoff.

<!-- SPEAKER NOTES — Slide 10 of 10: Owners (final)
The owners table converts the RFC from a document into an accountable plan. Every row needs a specific named person, not a team. "Platform team" is not an owner — "[Name] from Platform" is an owner. If any cell in the table has a TBD, resolve it before leaving the room. The RFC DRI is responsible for tracking the review window and ensuring a decision is made — this should be the RFC author unless there is a specific reason to delegate. Close by reiterating the two things you need from the room: (1) formal written comments in the RFC document before the review close date, and (2) any blocking objections stated explicitly today so they can be addressed in a revision. Thank reviewers for their time.
-->

---

# 10 — Ask for Feedback

## How to Contribute to This RFC

**Your feedback is needed before [Close Date]:**

| Channel | Use for |
|---|---|
| RFC document comments | Detailed technical objections, proposed edits |
| This session Q&A | High-level direction questions, clarifications |
| Async Slack thread (#rfc-hlx-0052) | Quick questions, +1s, minor suggestions |

**Decision criteria for approval:**
- ✓ No blocking objections from Platform or SRE teams
- ✓ All open questions (Q1–Q4) resolved
- ✓ At least 3 engineering team leads have reviewed and approved

> If you have a blocking objection, state it now or in writing by [Close Date]. Silence is not approval.

<!-- SPEAKER NOTES — Slide 11 — Ask for Feedback (final)
The three-channel approach for feedback collection reduces the friction of contribution. Some people prefer writing, others prefer synchronous discussion. The decision criteria are explicit — "no blocking objections from Platform or SRE" is a veto right, and those teams should know that upfront. The three team leads approval requirement means this cannot be pushed through by a single team. The pull-quote "silence is not approval" is the most important sentence on this slide — in RFC processes, it is common for people to not respond and then object after implementation begins. State this norm explicitly and document it in the RFC process guidelines.
-->
