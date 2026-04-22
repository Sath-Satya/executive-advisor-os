<!-- TEMPLATE: annual-plan-deck
CATEGORY: Executive
USE WHEN: Annual operating plan presentation — year-in-review, lessons learned, next-year theme, goals, initiatives, budget, and team.
SLIDE COUNT: 12
PALETTE: Executive cream
RENDER: marp --pptx 07-annual-plan-deck.md   (produces 07-annual-plan-deck.pptx)
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
    font-size: 2.15em;
    letter-spacing: -0.5px;
    margin-bottom: 0.2em;
  }
  h2 { color: #b8965a; font-size: 0.92em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5em; }
  h3 { color: #0e1b2e; font-size: 1.05em; margin: 0.7em 0 0.3em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.87em; }
  li { margin-bottom: 0.38em; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.85em; margin-top: 0.7em; }
  th { background: #0e1b2e; color: #f7f4ef; padding: 0.45em 0.75em; text-align: left; }
  td { padding: 0.42em 0.75em; border-bottom: 1px solid #e0dcd4; }
  tr:nth-child(even) td { background: #f0ece4; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.7em; color: #6b6560; }
  section.lead h1 { font-size: 2.7em; }
  section.lead p { font-size: 1.05em; color: #6b6560; }
  section.theme { background: #0e1b2e; color: #f7f4ef; }
  section.theme h1 { color: #f7f4ef; font-size: 2.5em; }
  section.theme h2 { color: #b8965a; }
  section.theme p { color: #d0c8b8; font-size: 1.05em; }
---

<!-- _class: lead -->

# Meridian Health — 2026 Annual Operating Plan

**Leadership Team Planning Session**

*December 2025 — Presented by the Office of the CEO*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
The annual operating plan is the translation of strategy into executable commitments with budget and headcount. This is different from the strategic plan: the strategic plan defines where we are going; the operating plan defines exactly how we get there in the next 12 months.

This presentation is the culmination of the planning cycle that started in October. Department heads have submitted their bottom-up plans; this deck is the integrated view, reconciled against the top-down financial model. If there are unresolved tensions between department asks and budget, they surface here.

Distribute the full budget model workbook the morning of the session. This presentation is the narrative; the workbook is the evidence.
-->

---

## 2025 Year-in-Review — What the Numbers Say

| Metric | 2025 Plan | 2025 Actual | Delta |
|---|---|---|---|
| Revenue | $196M | $198.4M | +$2.4M |
| New ARR | $34M | $33.0M | *(1.0M)* |
| Gross Margin | 62.5% | 63.8% | +1.3 pts |
| Plans on Platform | 60 | 47 | *(13 plans)* |
| Headcount (FTEs) | 820 | 847 | +27 |
| Operating Cash Flow | $22M | $26.8M | +$4.8M |

**Verdict:** Revenue and profitability beat. Platform growth missed. Operating cash flow well ahead.

<!--
SPEAKER NOTES — SLIDE 2 (Year-in-Review)
Start with an honest accounting. The year was strong on financial metrics and mixed on operating metrics. The platform count miss (47 vs. 60) is the most significant operational underperformance — and it has implications for 2026 because plan growth drives NRR, data moat, and long-term revenue.

The operating cash flow beat ($4.8M ahead) is the hidden story of the year. Our capital efficiency improved materially — we generated $1.35 in cash for every $1 of operating margin improvement. This gives us flexibility in the 2026 plan.

On the headcount overage (+27 FTEs vs. plan): 24 of the 27 are in Engineering, driven by accelerated Claims AI development in Q3-Q4. These are productive hires who contributed to the product performance numbers. Three are in G&A and will be reviewed in the headcount plan on slide 9.
-->

---

## 2025 Lessons — What We Carry Forward

**What we did well:**
- Claims AI product-market fit stronger than modeled — every deployment has renewed or expanded
- Engineering hiring velocity improved from 74% → 94% fill rate with remote-first policy
- Customer Success motion reduced churn from 3.9% (2024) to 3.1% — a structural improvement

**What we must do differently:**
- Platform growth requires a dedicated implementation team — we cannot grow to 90 plans in 2026 without one
- Mid-market sales cycle is too long — integration complexity is the constraint, not the product
- Pacific Southwest launch delay cost 6 months — regulatory risk must be budgeted into market entry plans

*These lessons are wired directly into the 2026 plan.*

<!--
SPEAKER NOTES — SLIDE 3 (Lessons)
The lessons slide is the intellectual bridge between 2025 and 2026. Without it, the plan looks like a fresh-start document disconnected from what actually happened. With it, the board can see that leadership has internalized the year's experience.

On the implementation team: this is the biggest structural change in the 2026 plan. In 2025, implementations were led by the product team with CS support. In 2026, a dedicated implementation team of 8 (4 technical, 4 project management) will be responsible for all new plan onboarding. The cost is $2.1M in headcount; the benefit is a 40% reduction in time-to-value for new plans, which unlocks faster NRR realization.

On mid-market sales cycle: the action is a pre-built integration library for the 5 most common legacy health plan systems, deployed Q1 2026. This eliminates the 2-3 week delay in technical evaluation that was the primary conversion barrier in 2025.
-->

---

<!-- _class: theme -->

## 2026 Annual Theme

# The Year of Implementation

In 2025 we proved the product. In 2026 we prove the machine.

Every strategy we designed, every product we built, every market we entered — all of it depends on our ability to implement at scale. 90 plans by December 31. No exceptions.

<!--
SPEAKER NOTES — SLIDE 4 (Annual Theme)
The annual theme is the cultural north star for the year. Every team meeting, every planning decision, every hiring choice should be filtered through this question: does this help us implement at scale?

"The Year of Implementation" is specifically chosen to counterbalance the tendency in fast-growing companies to over-invest in building and under-invest in deploying. We have a strong product. We have proven demand. The constraint is now operational — can we implement 43 net new plans in 12 months? The answer is yes, but only if we treat implementation as a first-class priority, not a post-sales afterthought.

Let this slide breathe. Read the theme statement. Pause. Then move on. The weight of the commitment should land before the room sees the next slide.
-->

---

## 2026 Goals — Four Outcome Targets

**Goal 1 — Revenue: $240M** *(+21% YoY)*
90+ plans on platform, NRR 120%, 47 net new logos.

**Goal 2 — Margin: 64.5% gross** *(▲ 70 bps YoY)*
Azure migration Phase 1-2 complete; Claims AI infrastructure fully amortized.

**Goal 3 — Platform scale: 90 plans** *(▲ 91% YoY)*
Dedicated implementation team operational Q1; time-to-value target ≤ 45 days.

**Goal 4 — Product: Prior Authorization AI generally available**
30 health plans on Prior Auth AI by December 31; $4.8M ARR contribution.

<!--
SPEAKER NOTES — SLIDE 5 (Goals)
Four goals, each specific and measurable. These are not aspirations — they are the outcomes the board will use to evaluate the CEO and leadership team at next year's annual review.

On Goal 1 ($240M, 21% growth): this is within the strategic plan range and reflects the platform growth catch-up from the 2025 miss. The 47 net new logos assumption is aggressive — it requires a 2.3x improvement on 2025's pace. The dedicated implementation team and mid-market conversion improvements are the two mechanisms that make this achievable.

On Goal 3 (90 plans): the 45-day time-to-value target is the internal metric that enables this. At 60-day average time-to-value (our 2025 actual), we cannot implement 43 new plans in 12 months with the current team. At 45 days, with the new implementation team, we can.
-->

---

## 2026 Initiatives — Q1 and Q2 Priorities

**Q1 Priorities (January — March):**
- Hire and onboard implementation team (4 technical, 4 PM) by February 15
- Prior Authorization AI GA release — production-ready by March 31
- Integration library v1.0 for 5 legacy systems — shipped February 28
- Enterprise data team hire complete (4 FTEs from 2025 strategic plan approval)

**Q2 Priorities (April — June):**
- Pacific Southwest market launch — go-live June 1 or defer to Q4 per regulatory gate
- Federated learning infrastructure — deployed to production June 30
- 20 net new plans live by June 30 *(50% of annual target by mid-year)*
- Member Services AI MVP with 5 pilot plans — kickoff April 15

<!--
SPEAKER NOTES — SLIDE 6 (Q1-Q2 Initiatives)
Front-loading the plan is deliberate. If Q1 slips, Q2 compounds, and by Q3 the annual targets are out of reach. The Q1 priorities are the critical path for the entire year.

On the implementation team hire: 8 FTEs by February 15 requires job descriptions posted by January 5 and an aggressive recruiting sprint. The HR team has pre-approved the JDs. This is the first milestone the CEO will check at the February board call.

On Pacific Southwest: the June 1 target is conditional on regulatory approval by May 15. If approval comes after May 15, the launch moves to Q4 to avoid a summer launch during health plan budget season. The defer gate is a pre-committed decision rule — it prevents a launch in a suboptimal window.
-->

---

## 2026 Initiatives — Q3 and Q4 Priorities

**Q3 Priorities (July — September):**
- Claims AI Open API beta — 3 certified third-party integrations by September 30
- Member Services AI expanded to 10 plans *(from 5 pilot)*
- Azure migration Phase 2 — production services migration July — September
- Mid-year plan review — board check-in at Q2 board meeting; adjust Q4 if needed

**Q4 Priorities (October — December):**
- 90 plans on platform by December 31 *(≥70 plans required to be on track)*
- Prior Auth AI: 30 plans live by December 31
- Annual plan retrospective — December 15 leadership session
- FY2027 planning kickoff — November 1

<!--
SPEAKER NOTES — SLIDE 7 (Q3-Q4 Initiatives)
The Q3 and Q4 initiatives are deliberately lighter than Q1 and Q2 — this is intentional sequencing. Companies that load initiatives evenly across quarters run into execution debt in H2 when hiring, product development, and customer onboarding all collide. Front-loading allows H2 to be an execution and consolidation period.

On the 70-plan mid-year gate: if we are below 70 plans by October 1, the board will likely want to discuss the Q4 target. This is a realistic early-warning threshold — 70 plans with 90 days remaining is achievable with the implementation team at capacity; below 70 is a signal that something structural is wrong.

On FY2027 planning kickoff in November: start planning 14 months out. This is earlier than most companies start, but it allows department heads to make hiring decisions in Q4 that the 2027 budget can absorb, rather than waiting for February approvals.
-->

---

## 2026 Budget — Revenue and Cost Summary

| Line | 2025 Actual | 2026 Budget | YoY Change |
|---|---|---|---|
| Revenue | $198.4M | $240M | +21% |
| Cost of Revenue | $72.5M | $85.2M | +18% |
| **Gross Profit** | **$125.9M** | **$154.8M** | **+23%** |
| R&D | $24.8M | $28.4M | +14% |
| Sales & Marketing | $16.1M | $18.2M | +13% |
| G&A | $18.2M | $19.8M | +9% |
| **Operating Income** | **$66.8M** | **$88.4M** | **+32%** |

**Operating Margin:** 33.7% (2025) → 36.8% (2026)

<!--
SPEAKER NOTES — SLIDE 8 (Budget Summary)
Walk through the P&L efficiently. The key story is operating leverage: revenue growing at 21% while operating expenses grow at 12-14%. This gap is how margin expands. The leadership team should understand that we are at a scale where growth becomes increasingly profitable.

On Cost of Revenue: the 18% increase (below revenue growth of 21%) reflects the Azure architecture delivering lower marginal cost per new plan. This is the infrastructure investment paying off.

On R&D at 14% growth: we are spending more on R&D in absolute terms but less as a percentage of revenue (from 12.5% to 11.8%). This is appropriate for a company transitioning from product development to product scaling.

On G&A at 9% growth: this is below revenue growth, demonstrating the shared services efficiency from 2024's consolidation. The 27 over-hire in 2025 Engineering is not carried into 2026 — department heads have been briefed to stay within new headcount approvals.
-->

---

## 2026 Team Plan — Headcount by Function

| Function | Dec 2025 FTEs | Net New 2026 | Dec 2026 FTEs |
|---|---|---|---|
| Engineering | 312 | +28 | 340 |
| Implementation (new) | 0 | +8 | 8 |
| Customer Success | 94 | +12 | 106 |
| Sales | 78 | +14 | 92 |
| Product | 62 | +8 | 70 |
| G&A | 64 | +4 | 68 |
| Data Science | 41 | +8 | 49 |
| **Total** | **651** | **+82** | **733** |

*Implementation team is the highest-priority hire class for H1 2026.*

<!--
SPEAKER NOTES — SLIDE 9 (Team Plan)
The headcount plan is where many planning sessions get the most debate. Walk through each function:

Engineering +28: roughly 9% growth, consistent with the product roadmap requirements. All new Engineering hires are tied to specific product tracks (Prior Auth AI, Open API, Member Services AI).

Implementation +8: this is the new function. All 8 hires must be in seat by February 15. HR has the JDs; recruiting agency has been briefed. The cost is $2.1M fully loaded; the benefit is 43 additional plans in 2026.

Customer Success +12: supporting the expanded customer base. The CS team takes 3 months to become productive; all Q1 hires will be productive by Q2.

Sales +14: this assumes a 60-day ramp time and the need for 2 additional enterprise AEs, 6 mid-market AEs, 4 SDRs, and 2 Solution Engineers.

Data Science +8: all for the federated learning and data moat initiative. These are specialized hires with 90-day recruiting lead times — JDs must be posted by December 15.
-->

---

## 2026 Risk Register — Operating Plan Level

**Operational risks (within our control):**
- Implementation team ramp: 8 hires by February 15. Risk: recruiting timeline. Mitigation: agency retained November 15.
- Prior Auth AI GA quality: 2 remaining performance bugs. Risk: March 31 slip to May. Mitigation: 4-week buffer built into launch plan.

**External risks (outside our control):**
- Pacific Southwest regulatory delay: probability 30%. Mitigation: launch gate pre-committed; marketing budget held pending approval.
- Health plan budget freezes: 15% of pipeline in at-risk segments. Mitigation: diversified pipeline across 3 geographic markets.

*No risks identified that would prevent $220M revenue floor if all mitigation actions execute.*

<!--
SPEAKER NOTES — SLIDE 10 (Risk Register)
The operating plan risk register is more granular than the strategic plan risk register — it is focused on the specific execution risks in the next 12 months.

The $220M revenue floor is the "what's the floor if things go wrong?" answer. Even if the Pacific Southwest launch slips to Q4, even if one enterprise deal delays, even if mid-market conversion improves only modestly — we still hit $220M if everything else executes. This is the downside case, and it is 11% growth on 2025 actual — still a strong result.

On the implementation recruiting risk: the agency was retained November 15. First candidate slate is due December 20. First offers should be extended January 10. This is a sprint — flag it explicitly to HR and the leadership team.
-->

---

## 2026 Commitments — The Leadership Team Contract

**By March 31:** Implementation team of 8 in seat; Prior Auth AI GA released; integration library shipped

**By June 30:** 20 net new plans live; Pacific Southwest launch gate evaluated; federated learning in production

**By September 30:** 55 plans on platform; Claims AI Open API in beta; mid-year financial review at or above plan

**By December 31:** 90 plans on platform; $240M revenue; Prior Auth AI at 30 plans; FY2027 plan board-approved

*These commitments are reviewed at each quarterly board meeting. Variances are explained, not hidden.*

<!--
SPEAKER NOTES — SLIDE 11 (Commitments)
This is the accountability close. Four quarterly checkpoints, four sets of commitments. The leadership team is agreeing to be evaluated against these milestones publicly at board meetings.

Read each commitment aloud. After each one, ask: "Does anyone on this team have a concern about this commitment that we should surface now?" This is the last chance to adjust before the plan is finalized.

On the December 31 commitment: 90 plans, $240M, Prior Auth at 30 plans — these three numbers together describe a company that is executing its strategy. If we hit all three, FY2027 planning starts from a position of strength. If we miss one, we will have a clear explanation from the quarterly reviews about what happened and what we changed.
-->

---

## Close — What Approval of This Plan Authorizes

**Approval of the 2026 Annual Operating Plan authorizes:**

1. Release of $78.5M operating budget (Q1 tranche: $19.6M)
2. Headcount approvals as specified in slide 9 (82 net new FTEs)
3. Implementation team recruiting to begin December 16
4. Prior Auth AI launch preparation to proceed on March 31 timeline
5. Pacific Southwest marketing budget held in reserve pending regulatory gate

*Next checkpoint: Q1 Board Meeting — April 3, 2026*

<!--
SPEAKER NOTES — SLIDE 12 (Close / Authorization)
End with the specific authorization list. This is what a "yes" in this room means. Make it explicit so there is no ambiguity about what has been approved.

The Q1 tranche release ($19.6M) allows the company to operate through March without returning for budget approval. The remaining $58.9M will be released in Q2-Q4 based on milestone achievement.

After the vote, send the authorization memo to all department heads within 24 hours. The memo should include their specific headcount approvals, Q1 budget lines, and the milestone at which their Q2-Q4 tranches unlock.

Final note: the 2026 Annual Plan session should end with a brief team acknowledgment. The year ahead is ambitious. The team built this plan together. Name the people in the room and the work they did to get here. Then go execute.
-->
