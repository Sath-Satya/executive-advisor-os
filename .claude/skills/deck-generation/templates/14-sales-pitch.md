<!-- TEMPLATE: sales-pitch
     CATEGORY: Sales / Enterprise
     USE WHEN: enterprise sales pitch to economic buyers, VP/C-suite discovery or proposal meeting
     SLIDE COUNT: 9
     PALETTE: Executive cream
     RENDER: marp --pptx 14-sales-pitch.md -->
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
    font-family: 'Georgia', 'DM Serif Display', serif;
    color: #0e1b2e;
    letter-spacing: -0.4px;
    font-size: 2.2em;
    line-height: 1.15;
    margin-bottom: 0.3em;
  }
  h2 {
    color: #b8965a;
    font-size: 0.88em;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 { color: #0e1b2e; font-size: 1.05em; font-weight: 700; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; font-weight: 700; }
  em { color: #b8965a; font-style: normal; font-weight: 600; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "▸ "; color: #b8965a; }
  ul li { margin-bottom: 0.6em; font-size: 1em; line-height: 1.55; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9em;
  }
  th {
    background: #ede9e1;
    color: #8899ac;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.06em;
    font-size: 0.8em;
    text-transform: uppercase;
    border-bottom: 2px solid #d6cfc3;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #ede9e1; }
  tr:last-child td { border-bottom: none; }
  blockquote {
    border-left: 4px solid #b8965a;
    padding: 12px 24px;
    margin: 1em 0;
    background: #ede9e1;
    border-radius: 0 8px 8px 0;
    font-style: italic;
    color: #0e1b2e;
    font-size: 1.05em;
  }
  section::after { color: #c4bdb3; font-size: 0.75em; }
---

## Enterprise Proposal

# The Administrative Burden Costing You $4.2M Annually

*Prepared for: [Client Organization] &nbsp;|&nbsp; April 2026*

This proposal addresses a specific, measurable problem in your operations — and provides a path to resolution within 90 days.

<!-- Speaker notes:
The title should be customized for every meeting — replace $4.2M with the actual number you calculated from their data during discovery. If you do not have their number yet, use a credible industry benchmark and flag it: "Based on industry benchmarks for a health system your size — we will refine this with your actual data." The executive buyer opened this meeting because someone in their organization flagged a problem. Your job in this first slide is to confirm you have diagnosed the same problem they are feeling. Do not start with who you are. Start with their problem. "Before I show you our solution, I want to confirm we are solving the right problem." That phrase alone earns credibility because it signals you listened. The "90 days" commitment in the subtext sets a concrete horizon for the conversation — executives think in quarters, not in "someday."
-->

---

## Current State

# Your Team Is Fighting a Broken Process — Every Day

- **Prior authorization approvals:** 11-day average cycle, 3 FTE dedicated
- **Denial rate:** 19% on first submission — above the 17% national average
- **Appeals process:** manual, averaging 4 weeks to resolution per case
- *Impact: 340 delayed procedures per month in FY25 &nbsp;|&nbsp; $4.2M in administrative cost*

<!-- Speaker notes:
This slide is built from your discovery call notes. Replace every number with their specific data. If you do not have specifics, use industry benchmarks and clearly label them as benchmarks — then ask for their numbers in the meeting: "These are national averages. Can you share your denial rate from last quarter? It will help us calibrate the ROI model." The "impact" line at the bottom is the economic translation — 340 delayed procedures is human cost; $4.2M is the board-room language. You need both. The current-state slide should make the economic buyer slightly uncomfortable — not in a manipulative way, but in the way that an accurate mirror is uncomfortable. If they push back ("our numbers are better than that"), great: "What are your numbers?" Now you have their data and a more credible baseline. Never argue about benchmarks — use them as conversation starters.
-->

---

## Future State

# What Your Operations Look Like in 12 Months

- **PA cycle time:** 11 days &nbsp;▸&nbsp; **3 days** (average) &nbsp;|&nbsp; same-day for 60% of cases
- **Denial rate:** 19% &nbsp;▸&nbsp; **6%** through AI-driven completeness checks
- **Staff redeployment:** 2.5 FTE freed for higher-value clinical coordination work
- *Net impact: **$3.1M annual savings** + 280 additional procedures per month*

<!-- Speaker notes:
The future state slide is the aspirational mirror of the current state — same structure, dramatically different numbers. Pair each current-state bullet with its future-state outcome. The word "redeployment" in the third bullet is intentional: do not say "headcount reduction." Healthcare executives are not trying to lay off nurses. They are trying to redeploy skilled staff away from administrative work and toward patient care. Framing it as redeployment is accurate and resonates with their values. The net impact line — $3.1M savings + 280 additional procedures — needs a source. Be ready to explain the math: "We modeled $3.1M based on 2.5 FTE at fully-loaded $75K, plus the $1.9M revenue impact of 280 additional procedures at average $6,800 reimbursement." If they want the spreadsheet, have it ready as a leave-behind or data room attachment.
-->

---

## Our Solution

# Helix — The AI Layer Between Your EHR and Every Payer

- **Integrates in 6 weeks** — no new hardware, no custom development, FHIR R4 native
- **Reasons from your records** — reads clinical notes, labs, imaging to build complete PA requests
- **Fights denials automatically** — AI-generated appeals with 73% win rate

*Production deployment at 11 health systems. Zero unplanned downtime in 14 months.*

<!-- Speaker notes:
This is not a features slide — it is a solution-to-problem mapping slide. Each bullet directly addresses a pain established in the current-state slide. "Integrates in 6 weeks" answers the deployment complexity fear. "Reasons from your records" answers the "will it know our data?" fear. "Fights denials automatically" answers the appeals-process pain. The "zero unplanned downtime in 14 months" footnote is the reliability signal for the CTO or VP IT who is in the room but has not said anything yet. They are thinking about maintenance windows and support tickets. Pre-empt it. If they ask about Epic certification: "Helix is in Epic's App Orchard — your Epic administrator can approve the connection in minutes without a custom integration project." If they ask about data security: "HIPAA BAA is included in every contract. SOC 2 Type II audit completed Q4 2025. Report available in the data room."
-->

---

## Proof — What Our Customers Say

> "We went from three staff managing PA full-time to one — and that person now focuses on complex cases. The simple stuff is Helix."
> — Director of Clinical Informatics, Mercy Health System

- **Mercy Health** (1,200 beds): $1.9M saved in Year 1, deployed in 5 weeks
- **St. Catherine's Medical** (800 beds): denial rate dropped from 21% to 5% in 90 days
- **Riverside Regional** (600 beds): NPS 74 from physicians after 6-month deployment

<!-- Speaker notes:
The quote at the top is the most persuasive element on this slide. Choose a quote from a customer who is similar to your prospect — same size, same EHR, same pain point. Ask permission before using a customer's name in a proposal. If the customer prefers anonymity: "A 1,200-bed integrated delivery network — reference available under NDA." The three proof points should each tell a different story: financial impact, quality impact, and adoption. The NPS number from physicians is particularly important in enterprise healthcare sales — it signals that the tool is being used, not just licensed. If the prospect asks for a reference call, have three names ready and offer them a choice: "I can introduce you to the CMO at Mercy or the VP Ops at St. Catherine's — which would be more useful?" Offering a choice signals confidence that any reference you provide will be positive.
-->

---

## ROI Summary

# Your Investment Pays Back in Under 5 Months

| Category | Annual Value |
|---|---|
| Staff time savings (2.5 FTE redeployed) | $187,500 |
| Denial reduction (13% improvement) | $1,420,000 |
| Additional procedure revenue (280/mo) | $1,905,600 |
| Appeals acceleration (time to resolution) | $580,000 |
| **Total annual value** | **$4,093,100** |
| Helix annual investment (Enterprise tier) | $228,000 |
| **Net annual benefit** | **$3,865,100** |
| **Payback period** | **&lt;5 months** |

<!-- Speaker notes:
ROI tables win deals. This table should be customized for every prospect — do not leave generic numbers in a proposal sent to a specific organization. The methodology for each line: FTE savings = 2.5 x $75K fully-loaded. Denial reduction = current denial volume x 13% improvement x average claim value. Additional procedures = 280/mo x 12 x average reimbursement. Appeals acceleration = current appeals volume x average days-to-resolution reduction x FTE cost per day. Walk through the math if asked — do not hide it. The payback period is the number that drives commitment: "Your procurement committee will ask: 'When do we break even?' The answer is five months. That is not a three-year ROI story — that is a budget-year story." If the actual payback for this prospect is longer (7–8 months), still lead with it. Eight months is still excellent for an enterprise software ROI. Never inflate the model — it will be validated against actuals at the 12-month review.
-->

---

## Next Steps

# A 90-Day Path to Production

| Week | Milestone |
|---|---|
| 1–2 | Pilot agreement signed &nbsp;|&nbsp; IT intro call &nbsp;|&nbsp; FHIR access approved |
| 3–4 | Helix sandbox configured with your EHR environment |
| 5–6 | First department live &nbsp;|&nbsp; PA submissions begin |
| 7–10 | Rollout to 3 departments &nbsp;|&nbsp; analytics dashboard live |
| 12 | 90-day review: actual vs. projected impact &nbsp;|&nbsp; expansion decision |

*Dedicated customer success manager assigned on contract signature.*

<!-- Speaker notes:
The timeline slide converts the ROI conversation into a project plan. Use a table rather than a Gantt chart — it is cleaner and reads faster. Each row should feel achievable, not aspirational. Week 1–2 items are all on the customer side: signature, IT intro, FHIR approval. This signals that the ball is in their court from day one — you are ready to start. Week 5–6 is where they start seeing value: actual PA submissions going through the system. The 90-day review is a built-in accountability checkpoint. Frame it as a success mechanism, not a contract review: "At 90 days, we will sit down with you and compare your actual denial rate and submission time to the projections in this proposal. If we are tracking below projections, we course-correct. If we are ahead, we discuss expansion." The dedicated CSM note is a retention signal for large accounts — they are not buying software and being left alone.
-->

---

## The Ask

# Sign the Pilot Agreement This Quarter

- **Proposed start:** May 5, 2026 &nbsp;|&nbsp; **First department live:** June 16, 2026
- **Pilot scope:** 2 departments, 90 days, full refund if KPIs not met
- **Pilot investment:** $38,000 (converts to first 2 months of Enterprise subscription)

**Three decisions needed today:**
1. Confirm departmental scope for pilot (cardiology or radiology?)
2. Identify IT owner for FHIR access coordination
3. Flag any procurement steps we should plan around

*Sarah Chen &nbsp;|&nbsp; sarah.chen@helix.health &nbsp;|&nbsp; (415) 555-0192*

<!-- Speaker notes:
The final slide is not a summary — it is a set of decisions. "Three decisions needed today" is a technique for moving conversations from discussion to commitment. Decision 1 is about scope — asking them to choose between cardiology or radiology means they are already thinking in deployment terms, not procurement terms. Decision 2 names an owner — vague commitments die; named owners create accountability. Decision 3 opens the procurement conversation, which is often the invisible blocker in enterprise sales. Better to surface it now than to lose three weeks to a procurement discovery that could have been planned for. The pilot risk reversal — "full refund if KPIs not met" — removes the final objection. If they ask what the KPIs are: "We will jointly define them in the pilot agreement. Typically: denial rate, submission cycle time, and physician satisfaction. You set the targets; we commit to them." That level of accountability is unusual in enterprise software and is a strong close.
-->
