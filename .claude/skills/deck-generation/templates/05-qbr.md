<!-- TEMPLATE: qbr
CATEGORY: Executive
USE WHEN: Quarterly business review covering revenue, pipeline, wins, misses, prior-quarter commitments, and the forward plan.
SLIDE COUNT: 11
PALETTE: Executive cream
RENDER: marp --pptx 05-qbr.md   (produces 05-qbr.pptx)
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
    padding: 46px 62px;
  }
  h1 {
    font-family: 'DM Serif Display', serif;
    color: #0e1b2e;
    font-size: 2.1em;
    letter-spacing: -0.5px;
    margin-bottom: 0.2em;
  }
  h2 { color: #b8965a; font-size: 0.9em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5em; }
  h3 { color: #0e1b2e; font-size: 1.05em; margin: 0.6em 0 0.25em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.87em; }
  li { margin-bottom: 0.35em; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.85em; margin-top: 0.7em; }
  th { background: #0e1b2e; color: #f7f4ef; padding: 0.45em 0.75em; text-align: left; }
  td { padding: 0.42em 0.75em; border-bottom: 1px solid #e0dcd4; }
  tr:nth-child(even) td { background: #f0ece4; }
  .win { color: #2a7d5f; font-weight: 600; }
  .miss { color: #b84040; font-weight: 600; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.68em; color: #6b6560; }
  section.lead h1 { font-size: 2.6em; }
  section.lead p { font-size: 1.05em; color: #6b6560; }
---

<!-- _class: lead -->

# Q3 2025 — Quarterly Business Review

**Meridian Health &nbsp;|&nbsp; Enterprise Revenue Team**

*Prepared by: Jordan Kim, VP Revenue &nbsp;|&nbsp; October 8, 2025*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
Open by confirming the QBR agenda and time allocation: 60-90 minutes total. Distribute a printed one-pager of the key metrics before the session starts — executives who hold the numbers in hand engage more substantively than those reading from the screen.

Frame the review: Q3 was a mixed quarter. Two headline numbers are above plan; one is below. We will cover all three, along with what we are doing about the miss. The second half of the QBR focuses on Q4 commitments and what we need from leadership to execute.

Tone: factual, accountable, forward-looking. QBRs that dwell on explaining the past spend energy that should go to fixing the future.
-->

---

## Q3 Scorecard — Headline Numbers

| Metric | Q3 Plan | Q3 Actual | vs. Plan | YoY |
|---|---|---|---|---|
| Revenue | $47.1M | $48.3M | **+$1.2M** | +11% |
| New ARR | $8.4M | $7.1M | *(1.3M)* | +6% |
| NRR | 116% | 118% | +2 pts | +4 pts |
| Gross Margin | 62.0% | 63.4% | +1.4 pts | +1.8 pts |
| Churn Rate | 3.5% | 3.1% | -0.4 pts | -0.8 pts |

**Verdict:** Revenue, NRR, and margin beat plan. New ARR missed by $1.3M. Root cause identified — see slide 4.

<!--
SPEAKER NOTES — SLIDE 2 (Scorecard)
Walk the table row by row but efficiently — executives have seen this scorecard before and will engage if something is off. Flag the New ARR miss immediately rather than building to it. "Revenue beat, but New ARR missed. I am going to walk you through exactly why on slide 4."

On NRR at 118%: this is the highest in company history. It means the existing customer base is generating expansion revenue that more than covers our plan shortfall on new logos. The business is durable even if new business development has a rough quarter.

On gross margin: the 1.4 point beat is driven by Claims AI operational efficiency and the Azure cost optimization completed in Q1. This is a structural improvement, not a one-time event.
-->

---

## Q3 Pipeline — State of the Funnel

| Stage | Deals | Total ARR Value | Avg Cycle |
|---|---|---|---|
| Marketing Qualified | 48 | $14.2M | — |
| Discovery | 22 | $8.7M | 18 days |
| Proposal | 14 | $6.1M | 34 days |
| Negotiation | 8 | $4.4M | 22 days |
| **Closed / Won Q3** | **11** | **$7.1M** | **74 days avg** |

**Pipeline coverage for Q4:** 3.8x (plan requires 3.0x minimum)

**Top 3 Q4 deals in negotiation:** Blue Shield CA ($1.4M), Highmark ($0.9M), Mountain West ($0.7M)

<!--
SPEAKER NOTES — SLIDE 3 (Pipeline)
Pipeline coverage at 3.8x is healthy — we have more than enough in the funnel to hit Q4 new ARR plan of $9.1M even at our current close rate. The question is cycle time, not volume.

On the three named deals: these are the most important calls in Q4. Each one has a named executive sponsor on their side. Blue Shield CA requires a COO-level reference call — I will come back to that ask in slide 10. Highmark is stalled on legal review of the data processing agreement; our legal team is tracking it. Mountain West is close — final pricing negotiation.

Anticipate: "Why did we only close 11 deals in Q3 against 14 in proposal?" Answer: 3 deals slipped to Q4 — one due to a budget freeze at the prospect (Blue Shield CA), one due to our own implementation capacity constraints (since resolved), and one due to a competitive evaluation that extended the cycle. All three are in the Q4 negotiation column now.
-->

---

## Q3 Wins — What Worked

**Three deals that closed ahead of schedule:**

- **Cascade Health Plan** — $1.1M ARR. Closed in 58 days vs. 90-day average. Driver: Claims AI demo was the decision-maker — no competing evaluation.
- **Northern Alliance Blues** — $0.8M ARR expansion. Existing customer added Member Portal module. No acquisition cost — pure NRR upside.
- **Tri-State Health Co-op** — $0.6M ARR. First mid-market win using the new SMB pricing tier launched in February.

**Pattern:** Technical differentiation on Claims AI is shortening sales cycles when the champion is a claims operations leader.

<!--
SPEAKER NOTES — SLIDE 4 (Wins)
Lead with wins before the miss. This is deliberate — it is not spin, it is sequencing. Start from what works so the miss discussion is additive, not defensive.

The pattern observation at the bottom is the most important takeaway: Claims AI is a sales accelerant when the champion is in claims operations. That means our SDR targeting should prioritize claims VPs and directors at target accounts — this is an action item for slide 10.

On Cascade Health Plan: the 58-day cycle is worth calling out as a benchmark. Standard industry cycle is 90-120 days. If we can systematically replicate this, we can increase Q4 close count by 2-3 deals without increasing pipeline volume.
-->

---

## Q3 Miss — New ARR Fell $1.3M Short

**Root cause analysis:**

- **Mid-market conversion rate:** 38% vs. 55% plan. Primary driver of the miss.
- **Specific issue:** 6 mid-market prospects stalled after the technical evaluation phase. Common objection: implementation timeline concern (integration with legacy plan systems).
- **Contributing factor:** Capacity constraint in Solutions Engineering delayed custom demo delivery by 2-3 weeks for 4 of the 6 stalled deals.

**What we have changed:**
- Added 2 Solutions Engineers in September — demo backlog cleared
- New integration guide for 3 most common legacy systems published October 1
- Mid-market champion enablement program launching Q4

*This is a solvable problem. The pipeline and product are not the issue.*

<!--
SPEAKER NOTES — SLIDE 5 (Miss Analysis)
Be direct and specific. "We missed new ARR by $1.3M. Here is exactly why." The root cause is two operational constraints, not a market problem or a product problem. This is important to establish clearly — it changes the conversation from "should we worry about our position?" to "how do we fix the execution issue?"

The 38% vs. 55% mid-market conversion rate is the headline number. Trace it through: 6 stalled deals, each with $200K-300K ARR, would have hit the plan. The Solutions Engineering backlog was the proximate cause; the legacy system integration objection was the trigger.

The three changes named are already in motion. You are not proposing solutions — you are reporting that the response is already executing. This is the difference between a reactive QBR and a proactive one.
-->

---

## Prior Quarter Commitments — Closed Loop

**Commitments made at Q2 QBR:**

| Commitment | Owner | Status |
|---|---|---|
| Launch SMB pricing tier | Jordan Kim | ✓ Complete — 1 win in Q3 |
| Add 2 Solutions Engineers | Priya Nair (HR) | ✓ Complete — both started Sept 1 |
| Claims AI demo v2 for mid-market | Engineering | ✓ Complete — deployed Aug 28 |
| Pacific Southwest pipeline qualified | Jordan Kim | Partial — 4 of 8 prospects qualified |
| Enterprise renewal lock-in (3-year terms) | Jordan Kim | ✗ 1 of 3 signed — 2 in Q4 pipeline |

**Net: 3 of 5 commitments fully delivered. 2 in-progress with Q4 close dates.**

<!--
SPEAKER NOTES — SLIDE 6 (Prior Commitments Closeout)
This slide closes the accountability loop from the last QBR. It is the single most important slide for building leadership trust in the QBR process. If you skip this slide or hide the misses, you undermine credibility.

On Pacific Southwest pipeline: 4 of 8 is behind plan. The delay is regulatory — the state approval timeline extended 60 days. This is outside our control, but we should have flagged it earlier. Acknowledge this directly.

On enterprise renewal lock-in: 1 of 3 is a miss on the commitment. Have a specific date for the remaining 2. "Highmark signs November 15 per their confirmed legal timeline. Mountain West signs before December 15 — that is my personal commitment."

The rule for this slide: report results accurately. If you missed, say you missed, say why, and say what you are doing about it. Boards and executives reward honesty far more than they punish misses.
-->

---

## Customer Health — Retention and Expansion

**Customer Health Dashboard — October 1 snapshot**

| Segment | Accounts | Health: Green | Health: Yellow | Health: Red |
|---|---|---|---|---|
| Enterprise | 34 | 28 (82%) | 5 (15%) | 1 (3%) |
| Mid-Market | 148 | 121 (82%) | 21 (14%) | 6 (4%) |
| Total | 182 | 149 (82%) | 26 (14%) | 7 (4%) |

**Red accounts requiring action:**
- **Pinnacle Health (Enterprise)** — Integration issue since August; engineering ticket escalated. 90-day resolution plan in place. Renewal in March.
- **6 Mid-Market accounts** — 4 underutilizing Claims AI module; 2 in budget review at their organizations.

<!--
SPEAKER NOTES — SLIDE 7 (Customer Health)
Customer health is a leading indicator of NRR — if this slide deteriorates, the next QBR revenue story gets harder. 82% green is healthy for a 182-account base.

On Pinnacle Health: this is the one red enterprise account and it will attract disproportionate attention. Be specific: the integration issue is a data format mismatch between their legacy claims system and our API. Our engineering team has a fix in staging; deployment is scheduled for October 22. The customer's VP of Operations has been on weekly calls since September. Renewal is March — we have time, but we cannot slip the fix.

On the 4 mid-market accounts underutilizing Claims AI: this is a CS failure, not a product failure. We sold them a module they are not using. The Q4 remediation plan is a free onboarding session with a Claims AI specialist — already on the calendar for all 4.
-->

---

## Q4 Plan — Revenue and New ARR Targets

**Q4 Targets:**

| Metric | Q4 Plan | Key Assumption |
|---|---|---|
| Revenue | $52.1M | NRR holds at 117%+; 3 enterprise renewals |
| New ARR | $9.1M | Close rate improves to 47% mid-market; 3 named enterprise deals close |
| Gross Margin | 64.0% | Azure migration Phase 1 complete |
| Churn Rate | ≤3.2% | Pinnacle Health resolved; 4 CS interventions delivered |

**Q4 Stretch Target:** $54M revenue if Blue Shield CA closes before November 30

*This plan is achievable. It requires the three asks on slide 10.*

<!--
SPEAKER NOTES — SLIDE 8 (Q4 Plan)
The Q4 plan is a 7.8% revenue increase over Q3 — achievable given the pipeline coverage of 3.8x and the improvements to mid-market conversion already in motion.

On the gross margin target: the 0.6 point improvement is contingent on the Azure migration Phase 1 (non-production environments) completing by November 15. The infrastructure team has confirmed the timeline. If it slips, margin stays at 63.4% — still above annual plan.

On the stretch target: $54M requires Blue Shield CA to close before November 30. The deal is in final negotiation. Mention the reference call ask from slide 10 here to link the ask to the outcome: "If we can get a COO-to-COO reference call by October 20, we believe we can accelerate the close."
-->

---

## Lookback on Annual Plan — Where We Stand

**Annual Plan Scorecard — 9 months in:**

| Annual Metric | Full-Year Plan | 9-Month Actual | Projected FY Outcome |
|---|---|---|---|
| Revenue | $196M | $146.3M | $198.4M (▲ 1%) |
| New ARR | $34M | $23.9M | $33.0M (▼ 3%) |
| Gross Margin | 62.5% | 63.4% | 63.8% (▲ 1.3 pts) |
| Churn Rate | 3.5% | 3.1% | 3.2% |
| Net New Logos | 52 | 37 | 50 (▼ 4%) |

*Full-year revenue on track to beat plan. New ARR and logos slight miss. Profitability significantly ahead.*

<!--
SPEAKER NOTES — SLIDE 9 (Annual Lookback)
Three months left in the year. This slide puts Q3 performance in full-year context. Revenue beats, profitability beats, volume metrics slightly miss. This is a high-quality miss — we are making more money per deal while closing slightly fewer deals. That is a strategic positioning improvement, not a performance concern.

On New ARR projected miss of $1M: this is within the confidence interval of the annual plan model. It is not a business concern; it is a plan accuracy concern. For next year's plan, the approach will tighten the mid-market conversion assumption based on Q2-Q3 actual data.

On net new logos: 50 vs. 52 is 2 logos short. This number will land at exactly 52 if the two Q4 enterprise deals and any mid-market acceleration close by December 31. It is achievable.
-->

---

## Q4 Asks — What We Need from Leadership

**Ask 1 — Reference call**
COO or CRO to conduct a peer reference call with Blue Shield CA COO by October 20. Deal value: $1.4M ARR.

**Ask 2 — Solutions Engineering headcount**
Approve 1 additional Solutions Engineer hire for Q1 2026. Current capacity is still the binding constraint for mid-market growth. Cost: $180K fully loaded annual.

**Ask 3 — Marketing investment release**
Release $240K from marketing reserve for Pacific Southwest demand generation — tied to regulatory approval confirmation (expected October 15). Pre-approved in annual plan.

<!--
SPEAKER NOTES — SLIDE 10 (Asks)
Three asks. This is the action section of the QBR. Every ask is specific, time-bounded, and tied to a revenue outcome.

On the reference call: the Blue Shield CA deal is the highest-ROI activity any executive can do this quarter. A 45-minute peer call could accelerate a $1.4M deal by 6 weeks. Prepare the executive sponsor with a one-page briefing on the prospect, their key concerns, and the talking points. Send it 24 hours before the call.

On Solutions Engineering headcount: this is a Q1 hire, not a Q4 action — but the recruiting cycle requires approval now. The mis-sizing in Q3 cost us $1.3M in new ARR. One additional SE at $180K fully loaded is a 7x return if it closes the equivalent miss next year.

On marketing investment: this is not new money — it is a conditional release already approved in the annual plan. The condition is regulatory approval, which is expected October 15. You just need confirmation that the mechanism for releasing it is ready.
-->

---

## Q4 Commitments — Accountability Anchors

**From the Revenue team — by December 31:**

- Close Blue Shield CA, Highmark, and Mountain West *(combined $3.0M ARR)*
- Sign 2 remaining enterprise 3-year renewal contracts *(Highmark Nov 15, Mountain West Dec 15)*
- Deliver mid-market champion enablement program to 12 qualified prospects
- Resolve Pinnacle Health integration issue by October 22 — confirmed by customer VP
- Q4 new ARR: $9.1M *(plan)* or $10.5M *(stretch if Blue Shield CA accelerates)*

*These commitments will be reviewed at Q4 QBR on January 8, 2026.*

<!--
SPEAKER NOTES — SLIDE 11 (Commitments / Close)
End on commitments, not on a summary of what you just said. Commitments create accountability and give the executive team a concrete set of outcomes to hold the revenue team to at the next QBR.

Read through each commitment with specificity. If any commitment generates pushback — for instance, if leadership does not think the reference call will materialize in time — adjust the commitment in real-time. It is better to set a realistic commitment and beat it than to set an optimistic one and miss it again.

The final line — "reviewed at Q4 QBR on January 8, 2026" — closes the loop. It tells the room that this is a repeating cycle with public accountability, not a one-time exercise.

After the slide: open for Q&A. Keep the asks on screen during discussion so action items are visible.
-->
