<!-- TEMPLATE: roi-deck
     CATEGORY: Sales / Business Case
     USE WHEN: CFO or procurement committee business case, late-stage deal justification, board approval for software purchase
     SLIDE COUNT: 8
     PALETTE: Executive cream with green accent for positive numbers
     RENDER: marp --pptx 20-roi-deck.md -->
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
  .positive { color: #1a7a4a; font-weight: 700; }
  .negative { color: #b85a2a; }
  .neutral { color: #8899ac; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "▸ "; color: #b8965a; }
  ul li { margin-bottom: 0.6em; font-size: 0.98em; line-height: 1.55; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88em;
  }
  th {
    background: #ede9e1;
    color: #0e1b2e;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.05em;
    font-size: 0.8em;
    text-transform: uppercase;
    border-bottom: 2px solid #c8c2b8;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #ede9e1; }
  tr:last-child td { border-bottom: none; }
  .total-row td { font-weight: 700; background: #ede9e1; border-top: 2px solid #c8c2b8; }
  section::after { color: #c4bdb3; font-size: 0.75em; }
---

## Business Case

# Helix Prior Authorization Automation
## ROI Analysis — [Organization Name]

*Prepared by: Helix Health Technologies &nbsp;|&nbsp; April 2026 &nbsp;|&nbsp; Confidential*
*Based on your provided data: 28,000 PA/year &nbsp;|&nbsp; 19% denial rate &nbsp;|&nbsp; 3 FTE dedicated*

<!-- Speaker notes:
This is a CFO-facing document, not a sales pitch. The audience is evaluating a capital expenditure decision. Every number must be sourced, every assumption must be stated, and the model must be reproducible — the CFO's analyst will rebuild your spreadsheet to verify it. The "based on your provided data" line on slide 1 is critical: it signals that this is not a generic benchmark analysis, it is a model built on their numbers. If you do not have their actual data yet, use industry benchmarks and flag them explicitly — never present a generic model as if it were custom. The three data inputs shown (28,000 PA/year, 19% denial rate, 3 FTE) are the primary drivers of the entire model. If any of these change during the conversation, recalculate before sending the deck. A model built on wrong inputs destroys the business case and your credibility.
-->

---

## Status Quo — The Cost of Doing Nothing

# Your Current PA Operations Cost $1.84M Per Year

| Cost Category | Unit Cost | Volume | Annual Cost |
|---|---|---|---|
| Staff labor (3 FTE, fully loaded) | $85,000/FTE | 3 | $255,000 |
| Supervisor time allocated to PA | $110,000 x 30% | 1 | $33,000 |
| Denied claims — lost revenue (unrecovered) | $1,200/claim | 560 | $672,000 |
| Appeal labor (manual, 40% win rate) | $180/appeal | 2,240 | $403,200 |
| Delayed procedure revenue lost | $6,800/procedure x 5% | 1,400 | $476,000 |
| **Total annual cost** | | | **$1,839,200** |

*Assumptions documented in appendix. Peer-reviewed benchmarks available on request.*

<!-- Speaker notes:
The status quo cost is not what the client pays for Helix — it is what they are already paying to NOT have Helix. Frame it this way: "You are already spending $1.84M per year on this problem. The question is not whether to invest — you are already investing. The question is whether to invest efficiently." Walk through each row in detail because the CFO's analyst will challenge every line. Staff labor: 3 FTE at $85K fully-loaded (salary + benefits + overhead) — confirm this with their HR benchmark or use their actual number. Denied claims — lost revenue: 19% denial rate x 28,000 PA = 5,320 denied claims. 90% are overturned on appeal. 10% are permanently lost. 560 lost claims x $1,200 average claim value. Appeal labor: 2,240 appeals x $180 per appeal (1.5 hours x $120/hour blended rate). Each number should be a cell in a spreadsheet that references a source. The "assumptions documented in appendix" line is essential — never present a model without a documented assumptions page.
-->

---

## Proposed Investment — Helix

# Total Cost of Ownership — 3-Year Horizon

| Component | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|
| Platform subscription (Enterprise) | $228,000 | $228,000 | $228,000 | $684,000 |
| Implementation and onboarding (one-time) | $38,000 | — | — | $38,000 |
| Internal IT time (estimated, one-time) | $12,000 | — | — | $12,000 |
| Training (one-time, 1 day) | $4,000 | — | — | $4,000 |
| **Total investment** | **$282,000** | **$228,000** | **$228,000** | **$738,000** |

*No hidden fees. No per-seat licensing. No infrastructure changes required.*

<!-- Speaker notes:
The total cost of ownership table prevents the CFO from being surprised by hidden costs post-signature. List every cost: implementation fee, internal IT time (even if not billed by Helix, the client's IT team will spend time on the FHIR connection — estimate it honestly), and training. The "no hidden fees, no per-seat licensing, no infrastructure changes" footer is a trust signal: many enterprise software contracts have costs that only surface at renewal. You are pre-empting that concern. If your pricing has changed since the discovery call, update this table before the ROI meeting. Discrepancies between a quoted price and the ROI deck destroy trust. Year 1 is higher than Years 2 and 3 because of the one-time implementation costs — that is normal for enterprise SaaS and the CFO will expect it. Note that the 3-year total ($738,000) will be compared to the 3-year benefit on the next slide.
-->

---

## Projected Savings

# What Helix Returns Over 3 Years

| Savings Category | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|
| Staff redeployment (2.5 FTE freed) | $187,500 | $193,000 | $198,800 | $579,300 |
| Denial rate reduction (19% &rarr; 6%) | $420,000 | $433,000 | $446,000 | $1,299,000 |
| Appeal win rate improvement (38% &rarr; 73%) | $152,000 | $157,000 | $161,700 | $470,700 |
| Procedure revenue recovered (cycle time) | $380,000 | $391,000 | $403,000 | $1,174,000 |
| **Total savings** | **$1,139,500** | **$1,174,000** | **$1,209,500** | **$3,523,000** |

*Year 1 savings are partial-year (6-month ramp). Years 2–3 include 3% annual benchmark inflation.*

<!-- Speaker notes:
Each savings row needs a calculation methodology. Staff redeployment: 2.5 FTE x $75,000 annual fully-loaded cost = $187,500. Note: this is "redeployment value" not "cost reduction" — you are not promising that Mercy will eliminate 2.5 positions. The value is that those 2.5 people shift from low-value PA administration to higher-value care coordination. If the client's CFO is a strict cost-reduction mindset, you may need to model this as "reduction in contract staff" rather than "redeployment" — know your audience. Denial rate reduction: current denied and permanently lost = 560 claims x $1,200 = $672,000. With Helix, denial rate drops to 6%: permanently lost claims drop from 560 to 168. Savings = 392 claims x $1,200 = $470,400. The $420,000 in Year 1 is partial because the model ramps over 6 months. Procedure revenue: cycle time drops from 12 days to 2.8 days — this unlocks procedures that were being delayed or cancelled. The 3% annual inflation adjustment on Years 2–3 is a credibility signal: you are modeling realistic cost growth, not flat projections.
-->

---

## ROI Summary

# Net Benefit — $2.785M Over 3 Years

| | Year 1 | Year 2 | Year 3 | **3-Year Total** |
|---|---|---|---|---|
| Total savings | $1,139,500 | $1,174,000 | $1,209,500 | $3,523,000 |
| Total investment | $282,000 | $228,000 | $228,000 | $738,000 |
| **Net benefit** | **$857,500** | **$946,000** | **$981,500** | **$2,785,000** |
| **ROI** | **304%** | | | **377%** |
| **Payback period** | **&lt;4 months** | | | |

*Cumulative positive cash flow by month 4 of Year 1*

<!-- Speaker notes:
The ROI summary is the slide the CFO will screenshot and share with the board. Every number here is derived directly from the previous two slides — there are no new assumptions introduced here. The ROI percentage (304% in Year 1, 377% cumulative) is calculated as net benefit / total investment. Walk through it: "For every dollar you invest in Helix, you get $4 back in Year 1 and $4.77 back by Year 3." The payback period — under 4 months — is the headline number for the board: "This is not a multi-year ROI story. You break even before your Q2 budget review." The "cumulative positive cash flow by month 4" footnote is the specific version of that claim. If your model produces a different payback period for this client, use their actual number. A 6-month payback is still excellent; a 12-month payback is reasonable for enterprise software. Do not inflate the payback period claim — it will be verified.
-->

---

## Risks and Sensitivities

# What If the Assumptions Are Wrong?

| Scenario | Change | Impact on Payback |
|---|---|---|
| Base case | No changes | &lt;4 months |
| Conservative (50% of projected denial savings) | Denial savings halved | 7 months |
| Pessimistic (25% of projected denial savings, 1 FTE only) | Major underperformance | 14 months |
| Upside (73% &rarr; 80% appeal win rate) | Outperformance | &lt;3 months |

*Even in the pessimistic scenario: full payback in 14 months on a 3-year contract.*

<!-- Speaker notes:
Sensitivity analysis is the credibility test of a business case. CFOs who have seen inflated ROI projections will immediately ask "what if you're wrong?" This slide pre-empts that question and shows you have modeled the downside. The key message from this table: even in the worst-case scenario (25% of projected denial savings, only 1 FTE freed), Helix pays back in 14 months — well within the 3-year contract. The footnote makes this explicit. If a prospect's CFO wants to run their own sensitivity analysis, offer the model: "I can share the underlying Excel model so your team can adjust the assumptions directly. All the formulas are documented." That level of transparency is unusual in vendor-provided ROI analysis and builds significant trust. The upside scenario (appeal win rate exceeding 73%) is based on Mercy's 16-month performance improvement — Helix gets better at each payer's criteria over time.
-->

---

## Decision Criteria

# What You Are Deciding — and What You Are Not

**You ARE deciding:**
- Whether the investment meets your capital hurdle rate (typical: 15–25% ROI)
- Whether the payback period fits your budget planning cycle
- Whether the business case assumptions are defensible to your board

**You ARE NOT deciding:**
- Whether prior authorization is a problem worth solving (it costs you $1.84M today)
- Whether AI can process clinical data accurately (validated at 11 health systems)
- Whether Helix works (reference call with Mercy available this week)

*This investment meets a 377% 3-year ROI — well above a 25% hurdle rate.*

<!-- Speaker notes:
The decision criteria slide is unusual in a business case deck, but it is extremely effective with CFOs and procurement committees. By listing what the decision IS and IS NOT about, you pre-frame the conversation to avoid relitigating proven points. The "you are not deciding" list handles the three most common objections that delay enterprise software deals: "we're not sure the problem is big enough" — here is the $1.84M cost. "We're not sure the AI is accurate" — 11 health systems, verified data. "We're not sure it works" — reference call available. If you present this slide and someone raises one of the "you are not deciding" objections anyway, you can politely redirect: "That's a great question — and it's one we addressed with the $1.84M cost baseline on slide 2. What would help you feel confident on that point?" This is not dismissive; it is structured. The hurdle rate callout at the bottom is the final ask: "Your hurdle rate is 25%. Our ROI is 377%. This clears your threshold by 15x."
-->

---

## The Ask

# Approve the Purchase — Here Is What Happens Next

1. **Sign the order form** — Enterprise subscription + implementation, total Year 1: $282,000
2. **Assign IT owner** — 1 hour to approve FHIR connection (we handle the rest)
3. **Set the kickoff date** — we target go-live for your highest-volume department in 6 weeks

**Expected financial impact by end of Q3 2026 (first 90 days):**
- Denial rate below 6% &nbsp;|&nbsp; PA cycle time under 3 days &nbsp;|&nbsp; 2+ FTE redeployed
- Cumulative savings exceeding your Year 1 investment by month 4

*sarah.chen@helix.health &nbsp;|&nbsp; (415) 555-0192 &nbsp;|&nbsp; Order form available for signature today*

<!-- Speaker notes:
The ask in a business case deck is different from a sales pitch — you are asking for a purchase authorization, not a next-step meeting. Be specific about what "yes" means operationally: three actions, each with a clear owner and time estimate. Action 1 is the decision. Action 2 is the only technical ask — IT owner, 1 hour. The "we handle the rest" is load-bearing: the CFO's fear is that "yes" means months of IT work. Eliminate that fear. Action 3 is the forward motion: "Set the kickoff date" keeps the conversation in project planning rather than procurement. The expected financial impact by end of Q3 is a soft commitment — not a contractual SLA, but a stated expectation that you will be measured against. If you miss it, you will hear about it at the 90-day review. Only commit to what you have delivered for comparable customers. "Cumulative savings exceeding your Year 1 investment by month 4" is based on Mercy's trajectory — confirm it is achievable for this client's volume before stating it.
-->
