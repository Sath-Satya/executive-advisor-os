<!-- TEMPLATE: product-launch
     CATEGORY: Internal / GTM
     USE WHEN: internal product launch readiness review, GTM alignment meeting, launch steering committee
     SLIDE COUNT: 11
     PALETTE: Executive cream (corporate)
     RENDER: marp --pptx 18-product-launch.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', 'DM Sans', system-ui, sans-serif;
    background: #f7f4ef;
    color: #1c1a18;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'Georgia', serif;
    color: #0e1b2e;
    letter-spacing: -0.4px;
    font-size: 2.1em;
    line-height: 1.2;
    margin-bottom: 0.3em;
  }
  h2 {
    color: #b8965a;
    font-size: 0.85em;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 { color: #0e1b2e; font-size: 1em; font-weight: 700; }
  strong { color: #0e1b2e; font-weight: 700; }
  em { color: #b8965a; font-style: normal; font-weight: 600; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "▸ "; color: #b8965a; }
  ul li { margin-bottom: 0.55em; font-size: 0.98em; line-height: 1.55; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88em;
  }
  th {
    background: #ede9e1;
    color: #0e1b2e;
    padding: 10px 14px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.05em;
    font-size: 0.8em;
    text-transform: uppercase;
    border-bottom: 2px solid #c8c2b8;
  }
  td { padding: 10px 14px; border-bottom: 1px solid #ede9e1; }
  tr:last-child td { border-bottom: none; }
  .status-go { color: #2a7a5a; font-weight: 700; }
  .status-risk { color: #b85a2a; font-weight: 700; }
  .status-tbd { color: #8899ac; font-weight: 600; }
  section::after { color: #c4bdb3; font-size: 0.75em; }
---

## Launch Readiness Review

# Helix 2.0 — Appeals Automation Launch
## May 12, 2026

*Steering Committee &nbsp;|&nbsp; Confidential &nbsp;|&nbsp; Version 3.1*

**Go / No-Go decision required by April 28, 2026**

<!-- Speaker notes:
This is an internal launch readiness deck — the audience is your steering committee, not customers or investors. The tone is operational: decisions, owners, risks. The version number (3.1) signals this is an iterated document, which is normal for a mature launch review. The "Go / No-Go decision required" line is the single most important element on this slide — it sets the stakes for the meeting. Everyone in the room needs to understand that they are here to make a decision, not have a status update. If this is the first review (pre-decision), replace with "Go / No-Go decision target: April 28, 2026." If the launch date has shifted, update it here first — do not bury a date change on slide 8. Distribute this deck 24 hours before the meeting so attendees can review async and come with prepared questions.
-->

---

## Product — What We Are Launching

# Helix 2.0 — Automated Appeals, Full Loop Closed

- **Core feature:** AI-generated appeal letters with supporting evidence, auto-submitted within 4 minutes of denial
- **New integrations:** Aetna, Cigna, and United Healthcare real-time API (replaces fax fallback)
- **Performance:** 73% appeal win rate in beta &nbsp;|&nbsp; 4-minute submission vs. 3–4 day manual average

*Beta participants: 3 health systems, 12,400 denial events, 8-week period*

<!-- Speaker notes:
The product slide in a launch review is a brief restatement of what is being launched — everyone in the room should already know this. Use this slide to confirm that the team is aligned on scope: "We are launching the appeals automation. We are not launching the payer analytics dashboard in this release — that moves to v2.1." Scope clarity prevents last-minute additions that derail timelines. The beta data is the key credibility signal for the steering committee: 12,400 denial events is a statistically significant sample. If any beta participant had a negative experience, name it and explain the resolution: "Beta site 2 had a 3-day outage due to a Cigna API change in week 5 — we have added an automatic fallback and circuit-breaker to prevent recurrence." Transparency about beta issues builds more confidence than hiding them.
-->

---

## Target Market

# Primary Launch Segment — Mid-Market Health Systems

| Segment | Size | Current Customers | Launch Target |
|---|---|---|---|
| Large academic medical centers (500+ beds) | 280 in US | 4 customers | Expansion only |
| Mid-market community hospitals (200–500 beds) | 1,100 in US | 7 customers | **Primary acquisition** |
| Critical access hospitals (&lt;200 beds) | 1,342 in US | 0 customers | 2027 roadmap |

*ICP for v2.0 launch: community hospital, Epic or Cerner, existing Helix PA customer upsell OR net-new logo*

<!-- Speaker notes:
Launch segmentation prevents sales teams from chasing every opportunity and losing focus. The "expansion only" on large academic centers signals that the enterprise team is not prioritizing new logos in that segment — they are focused on upselling the 4 existing customers to v2.0. The critical access hospital segment is explicitly deferred to 2027 — this is a responsible decision because the product needs configuration work to fit their lower-volume, higher-complexity workflow. The ICP line at the bottom is the most actionable element: every sales rep should be able to recite it. If the sales team uses a CRM for ICP scoring, confirm that the mid-market community hospital segment is tagged and routed correctly before launch day.
-->

---

## Positioning

# "Helix Closes the Loop — From Denial to Approval, Automatically"

**Positioning statement:** For health system operations leaders who are losing revenue and staff time to manual denial management, Helix 2.0 is the only prior-authorization platform that automatically generates, submits, and wins appeals — without requiring a physician to leave the EHR.

**Key differentiators vs. competitors:**
- Only platform with full PA-to-appeal loop automation
- 4-minute appeal submission (vs. 3–4 day industry standard)
- 73% win rate (vs. 42% manual)

<!-- Speaker notes:
The positioning statement follows the Geoffrey Moore "For X who Y, our product Z is the only A that B" format. It is internal-facing for this launch review — it is the statement that marketing, sales, and product alignment on. If different team members are using different language to describe the product, this slide is the source of truth. The three differentiators should map to objections that competitors raise: "What about Cohere Health?" — Cohere does not have automated appeals. "What about doing it manually?" — 3–4 days vs. 4 minutes. "What about accuracy?" — 73% vs. 42%. Test the positioning statement with 3 customers before the launch meeting: "Does this statement accurately describe why you use Helix?" Their language should inform the final wording. Do not launch with positioning that has not been validated with real buyers.
-->

---

## Launch Plan

# Phased Launch — Reduce Risk, Maximize Learning

| Phase | Scope | Date | Owner |
|---|---|---|---|
| **Soft launch** | 3 existing customers, self-serve upgrade | May 12 | Product |
| **Controlled release** | 10 existing customers, assisted upgrade | May 19 | Customer Success |
| **General availability** | All existing customers + new logo | June 2 | Sales + Marketing |
| **Partner channel** | [Partner] co-sell activation | June 16 | BD |

*Rollback plan: v1.9 remains in production until June 2; any customer can revert within 4 hours*

<!-- Speaker notes:
A phased launch is the risk mitigation strategy. Soft launch (May 12) is the canary deployment: 3 familiar customers with high-touch support, monitoring every API call. If there are issues, you catch them before they affect the full customer base. The rollback plan footnote is non-negotiable in a launch readiness review: the steering committee will ask about it. "v1.9 remains in production" means no customer is forced onto v2.0 until you are confident it is stable. The 4-hour revert SLA is operational — confirm with Engineering that this is achievable before this slide goes in the deck. If it is not achievable, replace with the actual time. Do not make SLA commitments in a steering committee deck that Engineering has not confirmed. The partner channel activation on June 16 is after GA — partners should not be selling a product before it is stable at scale.
-->

---

## Channels

# Three Acquisition Motions — Clear Ownership

| Channel | Target | Owner | KPI |
|---|---|---|---|
| Existing customer upsell | 8 of 11 customers upgrade by June 30 | Customer Success | Upgrade rate ≥ 70% |
| Outbound enterprise sales | 5 net-new logos, Q2 2026 | AE team (3 reps) | Meetings booked: 30 |
| Partner co-sell (post-June 16) | 3 partner-sourced deals, Q3 2026 | BD + Partner | Partner pipeline $900K |
| Marketing / inbound | 15 MQLs per month from launch | Marketing | MQL &gt; SQL rate ≥ 35% |

<!-- Speaker notes:
The channels slide is where GTM falls apart most often — when there is no clear owner and no measurable KPI, channels get blamed for each other's failures. This table assigns an owner and a KPI to every channel. Customer Success owns the upsell (not Sales — upselling existing customers requires a different conversation and a different skill set). The outbound target of 30 meetings for 5 closes assumes a 6:1 meeting-to-close ratio, which is consistent with enterprise health IT benchmarks. Confirm these targets with each team lead before the steering committee meeting: if the AE team says "30 meetings in one quarter is not achievable with 3 reps," you need to know that before the review. The MQL-to-SQL rate target (35%) should be based on historical data — if your current rate is 28%, target 32% as a stretch, not 35% as a baseline.
-->

---

## Metrics

# How We Measure a Successful Launch

| Metric | 30-Day Target | 90-Day Target | Owner |
|---|---|---|---|
| Customers upgraded to v2.0 | 5 | 11 (all) | CS |
| Net-new logos acquired | 1 | 5 | Sales |
| Appeal win rate (production) | 70% | 73% | Product |
| Average submission time | &lt;5 min | &lt;4 min | Engineering |
| Support tickets (Sev-1) | 0 | 0 | Support |
| NPS (post-upgrade survey) | 60 | 68 | CS |

<!-- Speaker notes:
Launch metrics need to be agreed upon before launch day, not measured after. Walk through each row with the steering committee: "Does everyone agree this is the right metric and the right target?" If someone objects to a target — "70% appeal win rate in 30 days is too high for a new deployment" — have the conversation now. Post-launch is too late to reset expectations. The Sev-1 support ticket target of zero is a reliability claim — Engineering needs to confirm this is defensible based on beta performance. If beta had any Sev-1 incidents, name them and explain why they will not recur. The NPS targets should be tracked separately from the existing customer NPS to avoid confounding the data — launch NPS reflects the upgrade experience, not the overall product satisfaction. Set up the survey instrument before May 12 so it fires automatically at day 7 post-upgrade.
-->

---

## Risks

# Three Risks That Could Affect the Launch

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Payer API instability (Cigna, United) | **Medium** | High — fallback to fax | Circuit breaker + fax fallback deployed in v2.0.1 |
| Customer upgrade resistance | **Low** | Medium — delays revenue | CS-assisted upgrade for all 11 customers; incentive: 60-day discount |
| Competitor announcement at HIMSS (May 10) | **Medium** | Low — messaging noise | PR briefings pre-HIMSS; analyst outreach April 28 |

*No Sev-1 issues observed in beta. No regulatory changes expected before June 2.*

<!-- Speaker notes:
A risk table demonstrates launch maturity. The steering committee needs to see that risks have been identified and mitigated — not that risks do not exist. Every launch has risks; pretending otherwise destroys credibility. The payer API instability risk is the most technically serious: if Cigna changes their API (which they did once during beta), appeals revert to fax. The circuit breaker mitigates this so customers experience a delay, not a failure. The competitor HIMSS announcement risk is real — if a competitor announces at HIMSS two days before your launch, you need to be ready with comparison messaging. Assign an owner for competitive monitoring: "Marketing monitors HIMSS press releases starting May 8. If a material competitive announcement is made, we convene an emergency messaging call within 4 hours." The "no regulatory changes expected" footnote is a risk acknowledgment — you have checked and there are no pending CMS rule changes that would affect the PA API requirements before GA.
-->

---

## Timeline

# Launch Calendar — April 28 to June 16

| Date | Activity | Owner |
|---|---|---|
| April 28 | **Go/No-Go decision** by steering committee | Steering Committee |
| May 1 | Sales and CS enablement complete (training + battle cards) | Enablement |
| May 8 | HIMSS presence: analyst briefings, customer dinners | Marketing + AE |
| May 12 | Soft launch — 3 beta customers upgraded | Product + CS |
| May 15 | Launch metrics review (day 3 status) | Product |
| May 19 | Controlled release — 10 customers | CS |
| June 2 | **General availability** | All |
| June 16 | Partner channel activation | BD |

<!-- Speaker notes:
The timeline slide is the operational backbone of the launch. Every date should have been confirmed with the relevant owner before this slide was finalized. The April 28 Go/No-Go is the decision gate that this entire meeting is leading to — make sure the criteria for Go are explicit: "We will proceed if: (1) zero Sev-1 incidents in extended beta, (2) sales enablement complete, (3) legal review of updated ToS signed off." If any criterion is not met, the decision is No-Go with a new target date. The HIMSS entry (May 8) is both an event and a risk mitigation activity — analyst briefings before HIMSS set the narrative. If your product is launching at HIMSS rather than before it, restructure the timeline accordingly. The June 16 partner activation should not move — rushing it before GA creates channel support complexity.
-->

---

## Team and Ownership

# Named Owners for Every Launch Workstream

| Workstream | Owner | Status |
|---|---|---|
| Product readiness | James Okafor (CTO) | GO |
| Customer success and upgrade | Lisa Park (VP CS) | GO |
| Sales enablement | David Torres (VP Sales) | RISK — training 60% complete |
| Marketing and PR | Anita Sharma (CMO) | GO |
| Legal and compliance | External counsel | TBD — ToS review in progress |
| Support infrastructure | Ben Liu (Support Lead) | GO |
| Partner activation | Chen Wei (BD Lead) | GO |

<!-- Speaker notes:
Named owners create accountability. Every workstream on this table should have a person, not a team, as the owner. If sales enablement is at 60% with 11 days to the Go/No-Go, that is a risk that needs to be surfaced here — do not soften it. "Sales enablement is at 60%. David has committed to 100% by May 1, which is the day before HIMSS. If he misses that date, we are launching with undertrained reps at the most important conference of the year. Mitigation: accelerate the remaining 40% by April 28." The legal TBD is also a risk — Terms of Service must be complete before GA. Legal review in progress is acceptable for the soft launch phase but must be resolved before June 2. The status column uses plain language — GO, RISK, TBD. Never use green/yellow/red without a corresponding legend, because presentation tools render colors inconsistently.
-->

---

## The Ask

# Three Decisions Required Today

1. **Go / No-Go for May 12 soft launch** — based on product readiness, risk assessment
2. **Approval of final launch metrics** — confirm 30-day and 90-day targets
3. **Sales enablement escalation** — authorize David to bring in external trainer to close the 40% gap

*Next review: May 15 (day 3 of soft launch) &nbsp;|&nbsp; Escalation threshold: any Sev-1 event*

**Decision owners: CEO + CTO + VP Sales + CMO**

<!-- Speaker notes:
The final slide of a launch review is a decision slate, not a summary. Three specific decisions, each with a named owner. Decision 1 is the primary outcome of this meeting — frame it explicitly: "I am asking the steering committee to vote Go or No-Go on the May 12 soft launch." If it is No-Go, the immediate output of this meeting should be a revised date and a list of outstanding conditions. Decision 2 — metrics approval — is often skipped and then becomes a source of conflict post-launch. Get explicit alignment today. Decision 3 — the escalation on sales enablement — is an executive decision: it requires budget approval and VP Sales' acknowledgment that the gap is real. The escalation threshold ("any Sev-1 event") is a standing operating procedure: you should not need another steering committee to escalate if something breaks. Define it now so everyone knows the response protocol. End the meeting by asking for the vote: "Can I get a Go from each of you for the May 12 soft launch, subject to legal clearing the ToS by May 10?"
-->
