<!-- TEMPLATE: board-deck-detailed
CATEGORY: Executive
USE WHEN: Full quarterly or annual board meeting requiring a complete narrative arc — context, findings, risks, options, and formal recommendation with appendix.
SLIDE COUNT: 12
PALETTE: Executive cream
RENDER: marp --pptx 02-board-deck-detailed.md   (produces 02-board-deck-detailed.pptx)
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
    font-size: 2.2em;
    letter-spacing: -0.5px;
    margin-bottom: 0.15em;
  }
  h2 { color: #b8965a; font-size: 0.95em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5em; }
  h3 { color: #0e1b2e; font-size: 1.1em; margin-bottom: 0.3em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.87em; }
  li { margin-bottom: 0.35em; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; margin-top: 0.8em; }
  th { background: #0e1b2e; color: #f7f4ef; padding: 0.5em 0.8em; text-align: left; }
  td { padding: 0.45em 0.8em; border-bottom: 1px solid #e0dcd4; }
  tr:nth-child(even) td { background: #f0ece4; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.7em; color: #6b6560; }
  section.lead h1 { font-size: 2.8em; }
  section.lead p { font-size: 1.1em; color: #6b6560; }
  section.divider { background: #0e1b2e; color: #f7f4ef; }
  section.divider h1 { color: #f7f4ef; font-size: 2.6em; }
  section.divider h2 { color: #b8965a; }
  section.appendix { background: #f0ece4; }
---

<!-- _class: lead -->

# FY2025 Board Review — Meridian Health

**Board of Directors &nbsp;|&nbsp; Annual Strategy Session**

*Confidential — Prepared by the Executive Team — September 2025*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
Welcome the board and acknowledge any directors joining remotely. This is the annual strategy review — a more substantive session than the quarterly updates. The agenda covers: 30 minutes for financial and operational review (slides 3-6), 20 minutes for risk and strategic options (slides 7-9), 15 minutes for the formal recommendation and vote (slides 10-11), and 10 minutes for Q&A before the appendix is opened.

Set expectations: presenters will keep each slide to 3 minutes to preserve time for discussion. Board members are welcome to interrupt for clarifying questions at any point. Substantive debate is reserved for the options and recommendation sections.

Distribute the data room link. The appendix in this deck (slide 12) is a condensed version of the full financial model; the live model is linked in the data room for directors who want to stress-test assumptions.
-->

---

## Agenda

1. **Opening** — State of the business
2. **Context** — Market and competitive landscape
3. **Finding 1** — Revenue performance
4. **Finding 2** — Product and customer success
5. **Finding 3** — Operational efficiency
6. **Finding 4** — Talent and culture
7. **Risks** — What could go wrong
8. **Options** — Strategic paths available
9. **Recommendation** — Management's preferred path
10. **Next Steps** — 90-day commitments
11. **Appendix** — Supporting financials

<!--
SPEAKER NOTES — SLIDE 2 (Agenda)
Briefly walk through the agenda to orient the board. Emphasize that slides 8-9 (Options and Recommendation) are where you want the board's greatest engagement. The earlier slides are evidence-setting — if a director has a question that will be answered later, ask them to hold it.

Note the time allocation for each section. If discussion runs long on the context slides, the chair has authority to table detailed questions to the data room review and move to the recommendation section. Time management is critical in board sessions.
-->

---

<!-- _class: divider -->

## Part 1

# State of the Business

<!--
SPEAKER NOTES — SLIDE 3 (Section Divider)
Transition slide. Brief pause, no narration needed beyond "Let's start with where we are." The divider signals a shift in register from logistics to substance.
-->

---

## Context — Market and Competitive Landscape

**Tailwinds driving our category:**
- Value-based care mandates expanded to 14 new states in 2025
- CMS prior authorization rule change creates $2.1B addressable spend shift
- AI adoption in health plan administration accelerating — 3 of 5 top Blues plans now issuing RFPs with AI requirements

**Headwinds we are navigating:**
- Pricing pressure in the mid-market segment — average deal size down 8%
- Two well-funded competitors raised Series C rounds in Q1 (combined $340M)
- Regulatory timeline uncertainty in Pacific Southwest (see Finding 1)

*Net assessment: market fundamentals are strongly favorable; competitive intensity is rising.*

<!--
SPEAKER NOTES — SLIDE 4 (Context)
This slide sets the stage for the four findings. Spend 2-3 minutes. The key message is that macro conditions are favorable but competition is intensifying — which makes the timing and execution of our growth investments more critical, not less.

On the CMS prior authorization rule: this is the single largest demand catalyst in our pipeline. Four of our top 10 prospects have explicitly cited it as the reason they are evaluating solutions now. The rule takes effect January 1, 2026 — our implementation cycle is 90-120 days, which means we need signed contracts by September 30 to deliver on time.

On the competitor fundraises: neither company has launched a competing prior auth product yet, but their runway gives them 18-24 months to build. Our moat is the existing contract base and the 42% efficiency improvement from Claims AI — which they cannot replicate without 12 months of training data.
-->

---

## Finding 1 — Revenue Performance

**FY2025 YTD Revenue: $183.4M** &nbsp;*(Plan: $178.2M — +$5.2M ahead)*

| Segment | Revenue | vs. Plan | YoY |
|---|---|---|---|
| Enterprise Health Plans | $112.1M | +$3.8M | ▲ 14% |
| Mid-Market Plans | $48.7M | +$2.1M | ▲ 9% |
| Government & Public | $22.6M | *(0.7M)* | ▲ 4% |

- **Net Revenue Retention:** 118% — highest in company history
- **Gross Margin:** 63.8% — ▲ 220 bps YoY, driven by Claims AI margin expansion
- **Pacific Southwest:** $0 revenue YTD; launch gating on state approval

<!--
SPEAKER NOTES — SLIDE 5 (Finding 1 — Revenue)
Walk the table segment by segment. Enterprise is the star — the $3.8M beat reflects three deals that closed ahead of plan in Q1. Mid-market beat is driven by the new SMB pricing tier introduced in February. Government segment missed slightly due to a federal contract renewal that slipped one quarter — it will close in Q4 and is not at risk.

Net Revenue Retention at 118% is a board-level metric to call out explicitly. It means our existing customer base is growing on its own — we are generating $1.18 for every $1.00 of ARR we had last year from existing customers alone. This is above the industry benchmark of 105-110% for our category.

Pacific Southwest zero revenue is expected and not a miss — it is gated on state regulatory approval which has been slower than originally projected. This is the context for the options discussion in slide 9.
-->

---

## Finding 2 — Product and Customer Success

**Claims AI Module — deployed to 47 health plans (▲ from 31 in Q2)**

- Average manual review time reduced: 42% → 51% over the deployment cohort
- CSAT score: 4.6/5.0 across 2,847 survey responses
- 3 plans have signed expansion amendments totaling $8.2M TCV

**Member Portal — v3.0 launched August 2025**
- Mobile engagement ▲ 67% vs. v2.0
- Accessibility audit: WCAG 2.1 AA compliant (first in category)
- Implementation timeline: avg 38 days vs. 62-day industry benchmark

*Product market fit indicators remain strong across both flagship products.*

<!--
SPEAKER NOTES — SLIDE 6 (Finding 2 — Product)
Two stories here: Claims AI momentum and Member Portal launch. On Claims AI, the 51% improvement figure is important — we said 42% in Q2 and the number is improving as the model trains on more plan-specific data. This is a compounding advantage that competitors who enter the market later will struggle to match.

On Member Portal v3.0: the WCAG 2.1 AA compliance is a competitive differentiator with government and public sector prospects, which require accessibility compliance by law. This opens a procurement pathway that was previously closed to us.

Anticipate questions about the 3 expansion amendments — be ready to name the plans if a director asks (Blue Shield, Highmark, and a regional plan in the Southeast). TCV is total contract value over the amendment term.
-->

---

## Finding 3 — Operational Efficiency

**Unit Economics Improving Across All Three Metrics**

| Metric | FY2024 | FY2025 YTD | Target |
|---|---|---|---|
| CAC (blended) | $84K | $71K | $70K |
| LTV:CAC Ratio | 4.2x | 5.1x | 5.0x |
| Payback Period | 22 months | 19 months | 18 months |

- **Cloud Infrastructure Cost:** ▼ 18% per customer YoY (Azure optimization program)
- **Support Ticket Volume:** ▼ 31% post-Claims AI v2 release (fewer manual exceptions)
- **G&A as % of Revenue:** 11.2% → 9.8% *(industry avg: 12-14%)*

<!--
SPEAKER NOTES — SLIDE 7 (Finding 3 — Operations)
The LTV:CAC ratio crossing 5.0x is a milestone worth pausing on. It means for every $1 we spend to acquire a customer, we expect $5.10 in lifetime value. This gives us room to increase sales and marketing investment without degrading returns — which is the basis for the investment ask in slide 10.

The Azure optimization story is tied to a workload migration we completed in Q1 — we moved 4 legacy batch processing jobs to serverless architecture. The 18% unit cost reduction applies to all existing and new customers, so it compounds as we grow.

G&A efficiency improvement is a result of the shared services consolidation completed last year. The board approved that investment in 2023; it is now showing up in the P&L. This is a good example of a prior board decision generating visible return.
-->

---

## Finding 4 — Talent and Culture

**Headcount: 847 FTEs** *(Plan: 840 — slightly ahead due to early R&D hires)*

- **Employee NPS:** 52 *(industry benchmark: 30-40)*
- **Voluntary Attrition:** 8.4% *(industry: 13-15%)*
- **Engineering Fill Rate:** 94% of open roles filled within 60 days

**Culture investments delivering:**
- Remote-first policy reduced time-to-hire by 24 days vs. 2023
- Manager effectiveness program: 87% of managers rated effective by reports
- DEI representation in leadership: 44% women, 31% underrepresented minorities

*Talent risk is low. Capacity for planned growth is confirmed.*

<!--
SPEAKER NOTES — SLIDE 8 (Finding 4 — Talent)
This slide closes the evidence section. The message is: the team is healthy, attrition is low, and we have the human capital to execute the plan being proposed in slide 10.

Employee NPS at 52 is exceptionally high. Benchmark context: most mid-size SaaS companies sit in the 30-40 range. Our score reflects the remote-first policy and the manager effectiveness program, which was a direct response to the 2023 engagement survey that flagged management quality as the top concern.

On DEI: these are not just compliance numbers. Diverse leadership teams show measurable outperformance on innovation metrics in our segment. This is an operating advantage we should protect.

Anticipate board questions about succession planning. We can address that in the Q&A; the full succession matrix is in the data room.
-->

---

<!-- _class: divider -->

## Part 2

# Risks — Options — Recommendation

<!--
SPEAKER NOTES — SLIDE 9 (Section Divider)
Transition to the decision section. This is where the board's analytical energy should focus. Frame it as: "We've shown you the evidence. Now we want to show you what we see as the risks, the choices in front of us, and what we recommend."
-->

---

## Risks — What Could Derail the Plan

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Regulatory delay in Pacific SW | High | Medium | Defer capex until approval confirmed |
| Competitor product launch | Medium | High | Accelerate enterprise contract lock-in |
| CMS rule rollback | Low | High | Contract language insulates revenue; scenario modeled |
| Key person departure (CTO) | Low | High | Retention package approved; succession identified |

**Risk posture:** Two risks are active (regulatory, competitor). Both are mitigated. No existential risks identified.

<!--
SPEAKER NOTES — SLIDE 10 (Risks)
Be direct about the risk table. Boards respect candor about risk more than they respect confident glossing-over. The two active risks are the ones the board will probe.

On Pacific Southwest regulatory delay: we have a lobbyist engaged in Nevada and Arizona. The current timeline projects approval by October 15, which gives us a Q4 launch. If approval slips past November 1, we recommend deferring to Q1 2026 to avoid a holiday-period launch. This is a pre-committed decision rule, not a judgment call — it removes ambiguity from the team.

On competitor risk: our strategy is to accelerate enterprise contract renewals with 3-year terms before a competitor can make contact. We have 12 enterprise renewals due in the next 6 months — the sales team is treating these as a defensive priority.

On CMS rule rollback: legal has reviewed our master subscription agreements. The revenue impact of a rollback is buffered by the contract terms for 18-24 months in most cases.
-->

---

## Options — Strategic Paths Available

**Option A — Accelerate (Recommended)**
Invest $18M incremental over 18 months: $8M Pacific Southwest launch, $6M R&D on prior auth module, $4M enterprise sales capacity. Projected outcome: $240M revenue by FY2026, 65% gross margin.

**Option B — Maintain Current Trajectory**
No incremental investment. Organic growth continues at 11-13% annually. Projected outcome: $205M revenue by FY2026, 63% gross margin. Market position stable but competitor gap narrows.

**Option C — Strategic Transaction**
Pursue acquisition of a competitor or adjacent capability. Capital requirement: $40-80M. Timeline: 12-18 months. Outcome: uncertain; execution risk high.

*Management recommends Option A. Option C is not recommended at this time.*

<!--
SPEAKER NOTES — SLIDE 11 (Options)
Present all three options with equal rigor — do not editorialize while walking through them. Reserve the recommendation language for after you have presented Option C. Boards that see only one option feel they are being led; boards that see three options feel they are governing.

On Option A: the $18M number is a net incremental ask on top of the existing operating budget. The capital allocation by bucket has been modeled in the financial appendix. IRR on the combined investment at base-case assumptions is 31%.

On Option B: this is the "do nothing" option, but do not present it negatively. It is a defensible choice — it preserves cash and maintains profitability. The argument against it is that the competitive window is open now and may close in 12-18 months.

On Option C: briefly explain why management is not recommending it. The core reasons are: (1) no identified acquisition target meets our quality and culture bar at a reasonable price, (2) integration risk is high given our current growth phase, (3) the organic opportunity is large enough that we do not need inorganic acceleration.
-->

---

## Recommendation and Next Steps

**Management recommends Option A — Accelerate.**

**Formal ask:**
1. Approve $18M incremental investment authority (fiscal year tranche: $9M)
2. Authorize Pacific Southwest market entry upon regulatory approval
3. Approve CTO retention package (terms in closed session)

**90-day commitments if approved:**
- October 1 — $4M R&D tranche deployed; prior auth module sprint kickoff
- October 15 — Pacific Southwest regulatory decision; capex drawdown triggered or deferred
- November 30 — 3 enterprise renewal contracts signed with 3-year terms
- December 31 — Q4 revenue on track for $52M; full-year at $236M

*Motion requested: approve Items 1-3 as presented.*

<!--
SPEAKER NOTES — SLIDE 12 (Recommendation / CTA)
This is the close. Be precise about what you are asking the board to vote on. Three items — read them clearly. Do not rush.

On Item 3 (CTO retention): flag that the discussion of package terms should move to closed session per governance protocol. Do not share amounts in the open session.

On the 90-day commitments: these are management's accountability anchors. By committing to specific dates and metrics, you are telling the board exactly how to hold you accountable at the next quarterly meeting. This is a sign of confidence, not vulnerability.

End by asking for a motion, then go quiet. Do not fill the silence. Let the chair manage the vote. If there are questions before the vote, answer them directly. If a director wants to defer, name the exact date and format you will use to re-present.
-->

---

<!-- _class: appendix -->

## Appendix — Supporting Financials

**Revenue Bridge: FY2024 Actual → FY2025 Projected**

| Bridge Item | $ Impact |
|---|---|
| Existing customer NRR (118%) | +$29.4M |
| New enterprise logos (14 new) | +$18.7M |
| New mid-market logos (62 new) | +$12.1M |
| Churn and downsells | *(6.2M)* |
| Pacific Southwest | $0 (gated) |
| **FY2025 Projected Total** | **$236.4M** |

*Full financial model available in the secure data room. Link distributed to all directors via board portal.*

<!--
SPEAKER NOTES — SLIDE 13 (Appendix)
This slide is only shown if directors request it or if time allows. Do not walk through it during the main presentation. Reference it by saying "The appendix has the revenue bridge — I will not walk through it now, but it is there if anyone wants to stress-test the numbers."

The revenue bridge methodology: starting from $182M in FY2024 actual, NRR of 118% on $142M of retained ARR adds $29.4M. New logo additions are based on closed deals plus the current late-stage pipeline with a 70% close rate applied. Churn is modeled at 3.1% of beginning ARR, consistent with Q2 actual.

If a director challenges the 70% close rate assumption: the trailing 12-month close rate on late-stage deals is 73%. The 70% assumption is therefore conservative.
-->
