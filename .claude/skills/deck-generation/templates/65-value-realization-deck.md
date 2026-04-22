<!-- TEMPLATE: value-realization-deck
     CATEGORY: ROI / Business Case
     USE WHEN: post-implementation review showing promised vs. realized benefits
     SLIDE COUNT: 10
     PALETTE: Corporate (cream bg, blue accent)
     RENDER: marp --pptx 65-value-realization-deck.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --color-bg: #f7f4ef;
    --color-fg: #0e1b2e;
    --color-accent: #3b9eff;
    --color-gold: #b8965a;
    --color-positive: #2d6a4f;
    --color-negative: #b91c1c;
    --color-neutral: #b8965a;
    --color-muted: #5a6677;
  }
  section {
    background: var(--color-bg);
    color: var(--color-fg);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 64px;
  }
  h1 {
    color: var(--color-fg);
    font-size: 1.9rem;
    font-weight: 700;
    letter-spacing: -0.4px;
    border-bottom: 3px solid var(--color-accent);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  h2 {
    color: var(--color-accent);
    font-size: 1rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 10px;
  }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 10px; font-size: 1.0rem; line-height: 1.5; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
    margin-top: 12px;
  }
  th {
    background: var(--color-fg);
    color: var(--color-bg);
    padding: 8px 12px;
    text-align: left;
  }
  td { padding: 7px 12px; border-bottom: 1px solid #d8d2c8; }
  tr:nth-child(even) td { background: #ede8e0; }
  .positive { color: var(--color-positive); font-weight: 700; }
  .negative { color: var(--color-negative); font-weight: 700; }
  .neutral  { color: var(--color-neutral);  font-weight: 700; }
  .label {
    display: inline-block;
    background: var(--color-accent);
    color: #fff;
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 4px;
    margin-bottom: 14px;
  }
  .cover-sub { font-size: 1.05rem; color: var(--color-muted); margin-top: 10px; }
  .verdict {
    background: #e6f4ea;
    border-left: 4px solid var(--color-positive);
    padding: 12px 18px;
    margin-top: 14px;
  }
  .verdict-warn {
    background: #fff8e6;
    border-left: 4px solid var(--color-neutral);
    padding: 12px 18px;
    margin-top: 14px;
  }
  .footer-note { font-size: 0.78rem; color: var(--color-muted); margin-top: 14px; }
---

<!-- _paginate: false -->
# Meridian Health — Claims Automation<br>Value Realization Review

<div class="cover-sub">18-Month Post-Implementation Assessment &nbsp;|&nbsp; June 2027</div>
<div class="cover-sub">Prepared by: SponAItech LLC &nbsp;|&nbsp; For Executive Committee</div>

<!--
PRESENTER NOTES — Slide 1: Title

This is the 18-month post-implementation review of the Meridian Health Claims Automation initiative approved in April 2026. Value realization reviews are the accountability mechanism for capital investments — they close the feedback loop between what was promised and what was delivered. This review covers the period from go-live (November 2026) through May 2027 — approximately 6 months of live operation. The data is drawn from Meridian's operational systems, not self-reported by the implementation team. Key metrics include: straight-through processing rate, cycle time, headcount, and financial savings achieved versus the business case model. This deck should be delivered by an independent reviewer — not the implementation team.
-->

---

# Context — The Commitment Made in April 2026

<div class="label">Baseline Commitments</div>

| Metric | Business Case Promise | Target Date |
|---|---|---|
| Straight-through processing rate | 40% by Month 6, 68% by Month 18 | Month 6 = May 2027, Month 18 = May 2028 |
| Average claims cycle time | 4.8 days steady state | Month 18 |
| Annual savings at steady state | $13.1M | Year 3 (2029) |
| Year 1 savings (partial year) | $6.4M | FY 2027 |
| Headcount reduction (attrition) | 40 FTEs over 18 months | Month 18 |
| Payback period | 14 months from April 2026 | June 2027 |

<div class="footer-note">Source: Meridian Health ClaimsAI Business Case, April 2026. All metrics defined and agreed at board approval.</div>

<!--
PRESENTER NOTES — Slide 2: Commitments

Before presenting results, re-anchor the audience in the original commitments. This prevents any revisionism — the metrics, targets, and dates were defined and approved by the board in April 2026. The 6-month STP target of 40% is where the programme should be today. The 18-month targets (68% STP, 4.8 days cycle time) are future commitments. This review is a progress assessment against Month 6 targets plus a forward look at trajectory toward Month 18. Note that "steady state" savings of $13.1M are a Year 3 target — we are not measuring against that today. The Year 1 partial-year saving of $6.4M IS the applicable FY 2027 target.
-->

---

# Promised Benefits — The Business Case Baseline

<div class="label">What Was Promised</div>

| Benefit Category | FY 2027 Promise | Monthly Run Rate |
|---|---|---|
| Adjuster headcount saving (attrition ramp) | <span class="positive">$3.6M</span> | $300K–$600K scaling |
| Temp and overtime elimination | <span class="positive">$2.2M</span> | $183K flat |
| Denial rework reduction | <span class="positive">$2.1M</span> | $175K scaling from Month 9 |
| Compliance penalty avoidance | <span class="positive">$0.9M</span> | $75K flat |
| Legacy licence elimination | <span class="positive">$0.7M</span> | $58K flat |
| **FY 2027 Total Promised** | **<span class="positive">$9.5M</span>** | |

<div class="footer-note">FY 2027 promise of $9.5M reflects partial-year operation (go-live November 2026, 7 months of FY 2027 operation). Full-year figure at same run rate = $13.1M.</div>

<!--
PRESENTER NOTES — Slide 3: Promised Benefits

The FY 2027 promise of $9.5M is derived from the original $6.4M "Year 1 partial year" figure adjusted for actual go-live timing. The platform went live in November 2026 — Month 7 as projected — meaning 7 months of FY 2027 are live months. The $9.5M represents 7/12 of the Year 1 pro-rated annualised benefit. This is the correct comparison baseline. Note that the headcount saving ramps across the 7 live months — it starts at $300K/month and scales as attrition progresses. The denial rework benefit starts in Month 9 (January 2027) per the original model — the ML denial management module was scoped to Phase 2. Use this slide to establish exactly what was expected before showing what was achieved.
-->

---

# Realized Benefits — What Was Actually Delivered

<div class="label">Actuals vs. Promise</div>

| Benefit Category | FY 2027 Promise | FY 2027 Actual | Variance |
|---|---|---|---|
| Adjuster headcount saving | $3.6M | <span class="positive">$3.9M</span> | <span class="positive">+$300K (+8%)</span> |
| Temp and overtime elimination | $2.2M | <span class="positive">$2.4M</span> | <span class="positive">+$200K (+9%)</span> |
| Denial rework reduction | $2.1M | <span class="neutral">$1.7M</span> | <span class="negative">-$400K (-19%)</span> |
| Compliance penalty avoidance | $0.9M | <span class="positive">$1.1M</span> | <span class="positive">+$200K (+22%)</span> |
| Legacy licence elimination | $0.7M | <span class="positive">$0.7M</span> | $0 (on target) |
| **Total** | **$9.5M** | **<span class="positive">$9.8M</span>** | **<span class="positive">+$300K (+3%)</span>** |

<div class="verdict">Overall: FY 2027 savings of $9.8M exceed the promise of $9.5M by $300K. Investment is tracking ahead of plan.</div>

<!--
PRESENTER NOTES — Slide 4: Realized Benefits

The headline is positive: total savings of $9.8M beat the $9.5M promise by $300K. Walk the committee through each line. The headcount saving beat the model because voluntary attrition was higher than the conservative 40-FTE forecast — 44 FTEs departed through natural attrition by Month 6. Overtime elimination outperformed because the automation reduced peak-period processing backlogs more effectively than modelled. The denial rework reduction underperformed — the ML Phase 2 module was delayed by 6 weeks due to a data quality issue in the Facets integration. This is the one area requiring attention. The compliance penalty avoidance beat the model significantly — the faster cycle time eliminated 3 CMS late-pay violations that occurred quarterly in the pre-automation period. Legacy licence elimination was exactly on target — a binary contractual event.
-->

---

# Variance Analysis — Where We Beat and Missed

<div class="label">Drivers of Variance</div>

**Over-delivered (+$700K above model):**
- Higher-than-expected voluntary attrition (44 FTEs vs. 40 modelled)
- Overtime reduction exceeded forecast — processing backlogs eliminated faster than expected
- Compliance penalties avoided earlier due to improved cycle time

**Under-delivered (-$400K below model):**
- Denial rework module (Phase 2) delayed 6 weeks due to Facets data quality issues
- ML training dataset required 3 additional weeks of data cleansing before production readiness
- Full denial rework benefit will be captured in Q3 FY 2027 (August 2027 onwards)

<div class="verdict-warn">Net: $300K ahead overall. Denial rework delay is a timing issue, not a structural miss. Full recovery expected by August 2027.</div>

<!--
PRESENTER NOTES — Slide 5: Variance Analysis

This slide is the most important for executive credibility. Explain both the positives and the negative honestly. The denial rework miss is real — $400K of expected savings did not materialise in the period. But the root cause is clear: the Facets data quality issue required remediation before the ML model could be trained on clean data. This was identified in Month 2 post-go-live and reported to the steering committee at the time. The remediation was completed in March 2027; the ML module went live April 15, 2027. From June 2027 onwards, the denial rework benefit will be fully realised. The framing: this is a timing variance, not a structural failure. The total lifetime benefit is unchanged — the savings will arrive in Q3 FY 2027 rather than Q1 FY 2027.
-->

---

# Operational Metrics — Beyond the Financials

<div class="label">Operational Performance</div>

| Metric | Business Case Target | Actual (May 2027) | Status |
|---|---|---|---|
| Straight-through processing rate | 40% by Month 6 | <span class="positive">44%</span> | Ahead |
| Average claims cycle time | 4.8 days (Month 18) | <span class="positive">6.1 days</span> | On track |
| System uptime | 98% SLA | <span class="positive">99.4%</span> | Exceeding |
| Model accuracy (STP decisions) | 95% | <span class="positive">97.2%</span> | Exceeding |
| Member complaint rate (claims-related) | -30% vs. baseline | <span class="positive">-41%</span> | Exceeding |
| Adjuster satisfaction (eNPS) | Maintain neutral | <span class="positive">+18 (positive)</span> | Exceeding |

<!--
PRESENTER NOTES — Slide 6: Operational Metrics

Operational metrics tell the story that financial figures alone cannot. The 44% STP rate at Month 6 exceeds the 40% target — the system is performing better than the conservative projection. The cycle time of 6.1 days is on a clear downward trajectory from the 14.2-day baseline, heading toward the 4.8-day steady-state target. System uptime at 99.4% exceeds the 98% SLA — InvestorFlow's platform has been operationally reliable. Model accuracy at 97.2% exceeds the 95% threshold; this metric is monitored weekly by the claims QA team. The member complaint reduction of 41% (vs. 30% target) is the most significant non-financial metric — it directly impacts Meridian's HEDIS scores and member retention. Adjuster eNPS at +18 is particularly noteworthy — this is the workforce that was most at risk of disengagement.
-->

---

# Lessons — What We Would Do Differently

<div class="label">Retrospective</div>

- **Data quality audit should precede integration work.** The Facets data quality issue was discoverable in Week 2 of the project. A pre-integration data audit would have surfaced it before it impacted the ML timeline.
- **Plan the attrition programme earlier.** Higher-than-expected attrition was a financial positive but a staffing challenge — succession planning for the QA and exception-handling roles should begin earlier.
- **Invest in adjuster communication from Day 1.** The positive adjuster eNPS was a direct result of the transparent redeployment programme. This should be a template for future automation initiatives.
- **Set up real-time dashboards at go-live.** The first 30 days post-go-live relied on manual reporting; the automated dashboard was not ready until Week 6. Earlier visibility would have allowed faster issue detection.

<!--
PRESENTER NOTES — Slide 7: Lessons

Every post-implementation review should include honest lessons — not as criticism, but as institutional learning. The data quality audit lesson is the most actionable: it would have been a 2-week exercise at $40K that would have avoided the 6-week ML delay costing $400K in foregone savings. This is a straightforward process improvement for future projects. The attrition point is a positive problem — more people left voluntarily than expected. The challenge was back-filling the QA and exception roles in the short term. The adjuster communication finding is important: the eNPS result was not accidental. It was the result of a deliberately designed redeployment programme that SponAItech helped design. Sharing this story internally will reduce resistance for Phase 2 and future automation initiatives. The dashboard readiness gap is a project management lesson.
-->

---

# Continued Opportunity — Phase 2 Value at Stake

<div class="label">Forward Look</div>

| Opportunity | Additional Annual Value | Timeline |
|---|---|---|
| Phase 2 ML denial management (already started) | <span class="positive">$2.1M</span> | Full value Q3 FY 2027 |
| Provider portal integration (automated pre-auth) | <span class="positive">$1.8M</span> | FY 2028 |
| Medicare Advantage adjudication module | <span class="positive">$3.4M</span> | FY 2028–2029 |
| Predictive fraud detection layer | <span class="positive">$2.2M</span> | FY 2029 |
| **Total Phase 2–4 opportunity** | **<span class="positive">$9.5M incremental</span>** | Over 3 years |

With Phase 2 complete, total programme annual benefit reaches $22.6M — a 5.4x return on the original $4.2M investment.

<!--
PRESENTER NOTES — Slide 8: Continued Opportunity

A value realisation review should not only look backwards — it should inform forward investment. The Phase 2 ML denial management module is already in production (April 2027 go-live), capturing the $2.1M that was delayed from FY 2027. Beyond that, three additional phases of automation opportunity have been identified through the Phase 1 operational data. Provider portal integration would automate pre-authorisation for 68% of elective procedures — reducing the $1.8M in manual pre-auth labour. The Medicare Advantage module addresses a separate adjudication workflow that ClaimsAI was not originally scoped for. The fraud detection layer would use the ML model's pattern recognition on a new problem set. Total incremental opportunity of $9.5M per year brings the programme's annual benefit to $22.6M — a 5.4x return on the original investment.
-->

---

# Actions — Three Things We Are Doing Now

<div class="label">Action Plan</div>

1. **Complete Facets data quality remediation** — fully resolved April 2027; denial rework module in production. Full $2.1M annual benefit expected from August 2027 onwards.

2. **Initiate Phase 3 scoping** — provider portal integration. Commissioning SponAItech feasibility assessment by July 2027; board presentation expected Q4 FY 2027.

3. **Formalise value realisation process** — all future technology investments >$1M will include a formal 12-month value realisation review with pre-defined metrics. This review serves as the template.

<!--
PRESENTER NOTES — Slide 9: Actions

Three actions, each owned by a named party. The Facets remediation is already done — this is closure, not a future commitment. The Phase 3 scoping is a forward investment decision that this review provides justification for: if Phase 1 delivered $300K above plan and Phase 2 is tracking on target, the case for Phase 3 is strong. The value realisation process formalisation is the meta-lesson: Meridian should not be doing this kind of review only because an external consultant proposed it. It should be standard practice for every major technology investment. The template from this review — metrics defined at approval, independent measurement 12–18 months post-go-live — should be codified in Meridian's capital allocation policy.
-->

---

# Next Review — October 2027

<div class="label">Close</div>

- **Next value realisation checkpoint:** October 2027 (Month 24 post-approval, Month 12 post-go-live)
- **Metrics to be assessed:** Phase 2 denial rework full benefit capture, STP rate trajectory toward 68% target, Phase 3 scoping decision
- **Investment status:** Payback confirmed at Month 14 (June 2027) — on target per original business case

**Overall verdict:** The ClaimsAI programme has delivered $9.8M in FY 2027 savings against a $9.5M promise. The investment is tracking ahead of plan. Payback was achieved on schedule. Phase 2 and beyond represent a clear path to $22.6M in annual benefit.

**Recommend: Continue programme investment and proceed with Phase 3 feasibility assessment.**

<!--
PRESENTER NOTES — Slide 10: Close

Close the loop. The payback was confirmed on schedule — this is the most important closure message for the committee. The programme is ahead of plan in total financial terms despite the denial rework timing miss. The October 2027 review is the next formal accountability checkpoint — set this in the steering committee calendar before leaving the room. The forward recommendation is to proceed with Phase 3 scoping — this should require a separate business case, but the committee should signal intent today so SponAItech can commission the feasibility work. The single strongest message: "We said we would return your $4.2M investment in 14 months. We did. We are now asking you to let us pursue the next $9.5M in annual savings." That message is earned, documented, and credible.
-->
