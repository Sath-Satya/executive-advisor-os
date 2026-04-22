<!-- TEMPLATE: exec-briefing
CATEGORY: Executive
USE WHEN: Briefing a C-suite executive on a specific topic or decision — structured problem, options, and explicit ask in under 30 minutes.
SLIDE COUNT: 7
PALETTE: Executive cream
RENDER: marp --pptx 04-exec-briefing.md   (produces 04-exec-briefing.pptx)
-->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&family=DM+Serif+Display&family=DM+Mono&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #f7f4ef;
    color: #1c1a18;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', serif;
    color: #0e1b2e;
    font-size: 2.1em;
    letter-spacing: -0.5px;
    margin-bottom: 0.2em;
  }
  h2 { color: #b8965a; font-size: 0.92em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5em; }
  h3 { color: #0e1b2e; font-size: 1.05em; margin: 0.8em 0 0.3em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.87em; }
  li { margin-bottom: 0.4em; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.86em; margin-top: 0.8em; }
  th { background: #0e1b2e; color: #f7f4ef; padding: 0.5em 0.8em; text-align: left; }
  td { padding: 0.45em 0.8em; border-bottom: 1px solid #e0dcd4; }
  tr:nth-child(even) td { background: #f0ece4; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.7em; color: #6b6560; }
  section.lead h1 { font-size: 2.6em; }
  section.lead p { font-size: 1.1em; color: #6b6560; }
  section.ask { border-left: 6px solid #b8965a; padding-left: 58px; }
---

<!-- _class: lead -->

# Cloud Infrastructure Migration — Executive Briefing

**Prepared for: Elena Voss, Chief Operating Officer**

*IT Strategy — Meridian Health &nbsp;|&nbsp; October 2025*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
Open by confirming the topic and time available. "Elena, I have 25 minutes. I want to walk you through the infrastructure migration decision — what it is, why it matters now, and exactly what I need from you before I leave this room."

This briefing is structured for executives who prefer to read the room before they engage. Send this deck 24 hours in advance. Assume the executive has skimmed slides 1-3 and will engage most on slides 5-7.

The goal: leave the room with a go/no-go decision and, if go, an approved budget release. Do not leave with "let me think about it" — drive to a specific resolution or a specific follow-up date.
-->

---

## Problem — Why This Matters Now

**Current state:** Meridian's core platform runs on a 2019-era data center footprint. 47% of compute is dedicated hardware. Mean time to scale: 72 hours.

**Business impact of the status quo:**

- **Claims AI** cannot scale to 100+ health plans without cloud elasticity — we are at capacity on current hardware
- **Pacific Southwest launch** requires 3 new regional endpoints; current architecture cannot support them without $2.4M in new hardware investment
- **Uptime SLA** of 99.9% is at risk — last 12 months actual: 99.7% (2.6 hours of downtime, two incidents)

*The migration is not a technology upgrade. It is a prerequisite for the business plan.*

<!--
SPEAKER NOTES — SLIDE 2 (Problem)
The executive needs to understand this is not an IT project — it is a business risk. Frame the three bullets as business risks, not IT problems. "Claims AI cannot scale" is a revenue risk. "Pacific Southwest endpoints" is a launch risk. "Uptime SLA" is a contract risk.

On the 99.7% actual vs. 99.9% SLA: two incidents in 12 months. Be prepared to name them: the March batch processing failure (47 minutes) and the August API gateway outage (108 minutes). Both had root causes tied to on-premise hardware limitations that cloud architecture would eliminate.

Anticipate: "Can we just buy more hardware?" Answer: yes, but it costs $2.4M in capex with no flexibility if we later downsize. The cloud migration costs $1.1M in the first year and delivers elastic scale at no additional capex.
-->

---

## Context — What We Evaluated

**Evaluation period:** June — September 2025 (4 months)

**Options assessed:**

| Approach | One-Time Cost | Annual Run Rate | Scale Flexibility | Timeline |
|---|---|---|---|---|
| Expand on-premise | $2.4M capex | $580K | None | 4 months |
| Lift-and-shift to Azure | $320K | $720K | Moderate | 3 months |
| Cloud-native on Azure | $1.1M | $640K | Full elastic | 6 months |
| Hybrid (on-prem + cloud) | $1.6M | $690K | Partial | 5 months |

*Cloud-native on Azure is the only option that satisfies all three business constraints simultaneously.*

<!--
SPEAKER NOTES — SLIDE 3 (Context)
Walk the table quickly — executives do not want to read every cell. Highlight the key comparison points: cloud-native is the most expensive upfront but the most flexible, and within 18 months the annual run rate savings over expand-on-premise pay back the incremental capex.

On the evaluation methodology: the 4-month evaluation involved 2 Azure architects, 1 external consultant, and the internal infrastructure team. The cost models are based on actual workload profiling, not estimates. Confidence interval on the $640K annual run rate: ±8%.

Be prepared for the question: "Why not lift-and-shift? It is cheaper." Answer: lift-and-shift preserves the architectural constraints of the on-premise system. We would still be constrained on the Claims AI scaling and Pacific Southwest endpoint requirements. Cloud-native is the only option that solves the root problem.
-->

---

## Options — Three Paths Forward

**Option 1 — Cloud-Native Now (Recommended)**
$1.1M investment, 6-month implementation, full elastic scale. Enables Claims AI to 100+ plans and Pacific Southwest launch on schedule.

**Option 2 — Lift-and-Shift as Bridge**
$320K investment, 3-month implementation. Buys time but does not solve the scaling constraint. Requires a second migration in 12-18 months — cumulative cost exceeds Option 1.

**Option 3 — Defer Migration**
No investment this quarter. Accept the scaling ceiling and delay Pacific Southwest to Q1 2027. Risk: Claims AI SLA degradation as load increases through Q4.

*Management recommends Option 1.*

<!--
SPEAKER NOTES — SLIDE 4 (Options)
Three options, clearly labeled. The executive may ask why Option 2 was not selected as a lower-risk bridge. The answer is that the cumulative cost of a two-step migration (lift-and-shift now, cloud-native in 18 months) is $1.3M — more than Option 1 — with twice the implementation disruption.

On Option 3: do not present this dismissively. The COO may have budget constraints you are not fully aware of. Present it as a real choice with real consequences: Pacific Southwest slips to 2027, and Claims AI will hit its scaling ceiling in Q2 2026 based on current growth projections.

Transition to slide 5 by saying: "Option 1 is our recommendation, and I want to show you specifically what the risks are — because I want to be transparent about what we are committing to."
-->

---

## Recommendation — Cloud-Native Migration

**Decision: Approve Option 1 — Cloud-Native on Azure**

**What we commit to:**
- Week 1-4: Non-production environments migrated; zero production disruption
- Week 5-12: Rolling production migration; each service migrated with 2-week validation window
- Week 13-26: Decommission on-premise hardware; full cloud operation confirmed

**Guardrails:**
- Production cutover requires sign-off from CTO and VP Engineering at each phase
- Rollback plan tested and documented before each service cutover
- Weekly status updates to COO for the 6-month duration

*First milestone: Q4 2025 non-prod environments live. Zero impact to current SLA.*

<!--
SPEAKER NOTES — SLIDE 5 (Recommendation)
This is the "here is what we are actually proposing" slide. Be specific. Executives do not approve vague plans; they approve milestone-based commitments with visible accountability.

The three guardrails are deliberate: they give the COO visibility and control without requiring her to be in the weeds. Weekly status updates are a standing calendar invite — make that offer explicit: "I will send a 5-line email update every Monday for 26 weeks."

On the rollback plan: this is the most important risk control. Every service cutover will have a documented rollback procedure tested in staging before the production cutover is attempted. This is non-negotiable and should be stated as such.

Pause after this slide and ask: "Any questions before I cover the risks?" Give the executive space to engage before moving to risk discussion.
-->

---

## Risks — What Could Go Wrong

**Active risks and our mitigations:**

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Claims AI performance regression post-migration | Medium | High | Parallel run for 30 days; automated regression test suite |
| Azure cost overrun vs. model | Medium | Medium | Cost alerts at $50K increments; monthly CFO review |
| Implementation timeline slip | Low | Medium | 2-week buffer built into each phase; no hard external deadlines |
| Data residency compliance issue | Low | High | Legal review of Azure region selection complete — US-only confirmed |

*No unmitigated high-impact risks.*

<!--
SPEAKER NOTES — SLIDE 6 (Risks)
The risk table is here because the executive will ask about it if you do not show it. Lead with the mitigation for each risk, not the risk itself. You are demonstrating that the team has thought ahead.

On data residency: this will be the top question from legal and compliance. Confirm that all Azure services will use US East and US West 2 regions only, with data replication confined to domestic regions. Legal has signed off. Have the memo available if requested.

On cost overrun risk: the $640K annual run rate has an 8% variance. The cost alert mechanism means any 10% overage triggers a review before it compounds. The CFO has been briefed and agrees this is an acceptable control.

After this slide, move directly to the ask. Do not linger on risks — you have addressed them, now close.
-->

---

<!-- _class: ask -->

## Ask — Three Decisions Before You Leave

**Decision 1 — Budget release**
Release $1.1M from the technology capital reserve for FY2025 Q4 — Q2 2026. *Approval needed by October 31.*

**Decision 2 — Executive sponsor**
Designate an executive sponsor (COO or CTO) for monthly governance reviews. *Naming needed today.*

**Decision 3 — Communication authority**
Authorize the communication to health plan partners about the migration timeline. *Templates prepared and ready.*

*With your approval today, we start November 1 and deliver full cloud operation by April 30, 2026.*

<!--
SPEAKER NOTES — SLIDE 7 (Ask / CTA)
Three asks. Read them in order. Do not editorialize. After you read ask #1, pause and look at the executive. Do not fill the silence. Wait for a response before moving to #2.

On the budget release: the $1.1M is within the existing technology capital reserve approved in the annual plan. You are not asking for new budget authority — you are asking for a release from funds already allocated.

On the executive sponsor: offer yourself as the default operational lead, but name the COO specifically because the decision requires cross-functional authority that IT alone does not have.

On the communication authority: the templates are ready. Waiting until approval to send them has cost two weeks of preparation time — you are ready to go the day the decision is made.

Close by stating the start date and delivery date clearly. "November 1 to April 30. That is 26 weeks. We are confident." Then stop talking.
-->
