<!-- TEMPLATE: payback-deck
     CATEGORY: ROI / Business Case
     USE WHEN: payback-focused pitch where speed-to-break-even is the primary decision criterion
     SLIDE COUNT: 7
     PALETTE: Clean light
     RENDER: marp --pptx 64-payback-deck.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --color-bg: #ffffff;
    --color-fg: #0e1b2e;
    --color-accent: #3b9eff;
    --color-positive: #2d6a4f;
    --color-negative: #b91c1c;
    --color-neutral: #b8965a;
    --color-muted: #5a6677;
    --color-surface: #f0f4f8;
  }
  section {
    background: var(--color-bg);
    color: var(--color-fg);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 64px;
  }
  h1 {
    color: var(--color-fg);
    font-size: 1.95rem;
    font-weight: 700;
    letter-spacing: -0.4px;
    border-bottom: 3px solid var(--color-accent);
    padding-bottom: 10px;
    margin-bottom: 22px;
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
  li { margin-bottom: 10px; font-size: 1.02rem; line-height: 1.5; }
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
  td { padding: 7px 12px; border-bottom: 1px solid #e2e8f0; }
  tr:nth-child(even) td { background: var(--color-surface); }
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
  .kpi-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
    margin-top: 18px;
  }
  .kpi {
    background: var(--color-surface);
    border-top: 4px solid var(--color-accent);
    padding: 14px 18px;
    border-radius: 6px;
  }
  .kpi-val { font-size: 1.8rem; font-weight: 700; }
  .kpi-lbl { font-size: 0.82rem; color: var(--color-muted); margin-top: 4px; }
  .breakeven-box {
    background: #e6f4ea;
    border: 2px solid var(--color-positive);
    border-radius: 8px;
    padding: 16px 24px;
    margin-top: 18px;
    text-align: center;
  }
  .breakeven-val { font-size: 2.4rem; font-weight: 700; color: var(--color-positive); }
  .footer-note { font-size: 0.78rem; color: var(--color-muted); margin-top: 16px; }
---

<!-- _paginate: false -->
# Meridian Health — Claims Automation<br>Payback Analysis

<div class="cover-sub">Speed-to-Break-Even Review &nbsp;|&nbsp; Operations Finance Committee — April 2026</div>
<div class="cover-sub">Prepared by: SponAItech LLC &nbsp;|&nbsp; Confidential</div>

<!--
PRESENTER NOTES — Slide 1: Title

This deck is the payback-focused companion to the full business case. It is designed for audiences who are less concerned with NPV mechanics and more concerned with a simple question: "When do we get our money back?" For mid-market healthcare organisations with constrained capital budgets and 12-month planning cycles, payback period is often the primary investment screen. This presentation shows that the Meridian Claims Automation initiative recovers its full $4.2M investment within 14 months of board approval — a payback period that is exceptional for a healthcare technology deployment of this scale. All benefit timing assumptions are documented and testable.
-->

---

# The Investment — $4.2M for $13.1M in Annual Savings

<div class="label">Investment Summary</div>

<div class="kpi-grid">
  <div class="kpi">
    <div class="kpi-val negative">$4.2M</div>
    <div class="kpi-lbl">Total Investment</div>
  </div>
  <div class="kpi">
    <div class="kpi-val positive">$13.1M</div>
    <div class="kpi-lbl">Annual Savings at Steady State</div>
  </div>
  <div class="kpi">
    <div class="kpi-val positive">14 mo</div>
    <div class="kpi-lbl">Payback from Board Approval</div>
  </div>
</div>

**Investment breakdown:**

- ClaimsAI platform licence and implementation: $2.1M
- Facets EHR integration and data migration: $0.8M
- Training and change management: $0.7M
- Contingency (15%): $0.6M

<!--
PRESENTER NOTES — Slide 2: Investment Summary

The three KPI boxes give the audience the headline numbers before any detail. $4.2M invested, $13.1M returned annually — a 3.1x annual return at steady state. The 14-month payback figure will be the most-discussed number in this room; the following slides explain exactly how it is derived. The investment breakdown is important: note that the $0.6M contingency is explicitly included. This is not a "best case" number — it is a risk-adjusted number. If the contingency is not needed, payback improves to approximately 11 months. The $2.1M platform cost is fixed-price per contract; the integration cost carries a 10% variance allowance per the Facets professional services estimate.
-->

---

# Benefits Timing — When Savings Flow

<div class="label">Benefit Schedule</div>

| Benefit Category | Annual Value | Start Month | Ramp Period |
|---|---|---|---|
| Adjuster headcount reduction (attrition, 40 FTE) | <span class="positive">$7.2M</span> | Month 7 | 12-month ramp |
| Eliminated temp and overtime spend | <span class="positive">$2.2M</span> | Month 7 | Immediate |
| Denial rework elimination (automated rules) | <span class="positive">$2.1M</span> | Month 9 | 3-month ramp |
| Compliance penalty avoidance | <span class="positive">$0.9M</span> | Month 7 | Immediate |
| Legacy platform licence elimination | <span class="positive">$0.7M</span> | Month 7 | Immediate |
| **Total steady-state annual benefit** | **<span class="positive">$13.1M</span>** | | |

<div class="footer-note">Month 7 = projected go-live date for Phase 1 production cutover. "Immediate" = full value on go-live day. "Ramp" = linear increase over stated period to full value.</div>

<!--
PRESENTER NOTES — Slide 3: Benefits Timing

Benefit timing is where payback calculations are most often challenged. This table shows the precise start month and ramp schedule for each benefit category. The $7.2M headcount saving does not start at $7.2M on Day 1 — it ramps linearly over 12 months as 40 FTEs are redeployed through attrition. At Month 7 (go-live), the headcount saving is zero; by Month 18 (one year post-go-live), it reaches full run rate. By contrast, the $0.7M legacy platform licence elimination is a binary event — the day ClaimsAI goes live, the three legacy adjudication tool contracts are cancelled. That $58K per month saving starts on go-live day. The benefits timing model is the foundation of the cumulative cash chart on the next slide.
-->

---

# Cumulative Cash — Break-Even at Month 14

<div class="label">Cash Flow Chart</div>

| Month | Investment | Monthly Benefit | Cumulative Cash |
|---|---|---|---|
| 0 | <span class="negative">($4,200K)</span> | — | <span class="negative">($4,200K)</span> |
| 3 | — | — | <span class="negative">($4,200K)</span> |
| 6 | — | — | <span class="negative">($4,200K)</span> |
| 7 (go-live) | — | <span class="positive">$342K</span> | <span class="negative">($3,858K)</span> |
| 9 | — | <span class="positive">$593K</span> | <span class="negative">($2,672K)</span> |
| 12 | — | <span class="positive">$775K</span> | <span class="negative">($743K)</span> |
| **14** | — | <span class="positive">$880K</span> | <span class="positive">**$17K**</span> |
| 18 | — | <span class="positive">$1,092K</span> | <span class="positive">$3,593K</span> |
| 24 | — | <span class="positive">$1,092K</span> | <span class="positive">$10,145K</span> |

<!--
PRESENTER NOTES — Slide 4: Cumulative Cash Chart

This table is the payback story in numbers. Months 1–6 show zero benefit because the implementation is underway — no savings accrue before go-live. Month 7 marks the go-live event: $342K in monthly benefits from immediate savings (overtime elimination, compliance penalty avoidance, licence elimination) plus early headcount attrition. The monthly benefit grows from $342K at Month 7 to $880K at Month 14 as the headcount attrition ramp progresses. The cumulative cash line crosses zero between Months 13 and 14 — we report this conservatively as Month 14. By Month 18 (full headcount ramp complete), monthly benefit reaches $1,092K and cumulative cash is $3.6M positive. At 24 months, the cumulative return is $10.1M on a $4.2M investment — a 2.4x return in two years.
-->

---

# Break-Even — Month 14 from Board Approval

<div class="label">Payback Summary</div>

<div class="breakeven-box">
  <div style="font-size:1rem; color:#5a6677; margin-bottom:8px;">PAYBACK PERIOD</div>
  <div class="breakeven-val">14 Months</div>
  <div style="font-size:1rem; color:#5a6677; margin-top:8px;">from board approval to full investment recovery</div>
</div>

**Timeline breakdown:**
- Months 1–7: Implementation (no savings)
- Months 7–14: Savings ramp (savings accumulate to $4.2M)
- Month 14+: Every dollar of savings is pure return

**Industry context:** Average healthcare IT payback = 28–36 months. This project returns investment in **half the typical time.**

<!--
PRESENTER NOTES — Slide 5: Break-Even

This is the pivotal slide. Present the 14-month payback number with confidence and provide the industry context benchmark: the average healthcare IT investment takes 28–36 months to pay back. This project does it in 14 months — approximately half the typical time. The reason is simple: the savings are large (13x the annual support cost) and they start early (Month 7). The implementation period is only 7 months because Phase 1 is scoped tightly — rules-based automation only, no ML, no AI model training required before go-live. Acknowledge that the 14-month figure is from board approval. If the committee approves today (April 2026), break-even occurs in June 2027. Ask: "Is there anyone in this room who believes Meridian's operating cost will be lower in June 2027 than it is today if we do nothing?" That question reframes the cost of waiting.
-->

---

# Sensitivity — Payback Under Adverse Conditions

<div class="label">Sensitivity Analysis</div>

| Scenario | Payback Period | Still within 24 months? |
|---|---|---|
| Base case | <span class="positive">14 months</span> | Yes |
| Go-live delayed 2 months (Month 9) | <span class="neutral">16 months</span> | Yes |
| Benefits 20% below model | <span class="neutral">18 months</span> | Yes |
| Implementation overrun +$500K (total $4.7M) | <span class="neutral">16 months</span> | Yes |
| Go-live delay + 20% benefit shortfall | <span class="neutral">21 months</span> | Yes |
| All adverse factors combined | <span class="negative">26 months</span> | Borderline |

Even in the worst combined scenario, payback is achieved within 26 months — still below the 28-month industry average.

<!--
PRESENTER NOTES — Slide 6: Sensitivity

Show the downside honestly. The most common risks for projects like this are implementation delay and benefit shortfall — test both individually and together. A 2-month go-live delay pushes payback to 16 months. Benefits 20% below model pushes it to 18 months. Both together push it to 21 months. Only if every adverse factor materialises simultaneously — delay, benefit shortfall, AND cost overrun — does payback extend to 26 months. That is still below the industry average of 28 months for healthcare IT. The committee should note: the fixed-fee implementation contract directly limits the cost overrun risk. And the $0.6M contingency reserve already absorbs the most likely implementation risks. The 20% benefit shortfall scenario assumes the headcount attrition plan fails to fully materialise — which is unlikely given the workforce reduction plan is already in the HR budget.
-->

---

# The Ask — Approve to Capture 14-Month Payback

<div class="label">Decision Required</div>

- Approve $4.2M capital appropriation for ClaimsAI Phase 1 implementation
- Authorise contract execution with SponAItech LLC and Facets PS within 10 business days
- Receive monthly progress report against payback milestones starting Month 1

**Cost of delay:**

- Each month of delay defers go-live by one month
- Each month of deferred go-live costs Meridian approximately **$342K in Month 7 savings** and compounds from there
- A 3-month delay in approval costs approximately **$1.8M in Year 1 savings foregone**

**Recommendation: Approve today. Break-even is June 2027.**

<!--
PRESENTER NOTES — Slide 7: The Ask

The close is disciplined and specific. The ask is a capital appropriation approval — not a request for further analysis, not a pilot. The cost of delay is quantified: $342K in foregone savings for each month of implementation delay, compounding as the ramp savings are also pushed out. A 3-month approval delay (e.g., waiting for the July 2026 committee cycle) costs $1.8M in Year 1 savings — which is nearly half the total implementation contingency. Anticipate the "can we do a pilot first?" question. Response: Phase 1 IS the conservative option — it is rules-based only, with parallel human review for 90 days post-go-live. A pre-Phase-1 pilot would add 4–6 months and $300K in incremental cost with minimal risk reduction, since the Facets integration is the primary risk and it must be built regardless. Thank the committee and request a decision.
-->
