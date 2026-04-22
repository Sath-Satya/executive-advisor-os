<!-- TEMPLATE: npv-irr-deck
     CATEGORY: ROI / Business Case
     USE WHEN: presenting NPV and IRR financial analysis for a capital investment decision
     SLIDE COUNT: 8
     PALETTE: Executive cream
     RENDER: marp --pptx 63-npv-irr-deck.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --color-bg: #f7f4ef;
    --color-fg: #0e1b2e;
    --color-accent: #b8965a;
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
    font-size: 2rem;
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
  .kpi-row {
    display: flex;
    gap: 32px;
    margin-top: 16px;
  }
  .kpi {
    background: #ede8e0;
    border-left: 4px solid var(--color-accent);
    padding: 12px 18px;
    min-width: 180px;
  }
  .kpi-val { font-size: 1.7rem; font-weight: 700; color: var(--color-positive); }
  .kpi-lbl { font-size: 0.8rem; color: var(--color-muted); margin-top: 2px; }
  .footer-note { font-size: 0.78rem; color: var(--color-muted); margin-top: 16px; }
  blockquote {
    border-left: 3px solid var(--color-accent);
    padding: 8px 16px;
    margin: 12px 0;
    color: var(--color-muted);
    font-style: italic;
  }
---

<!-- _paginate: false -->
# Meridian Finance — IR Consolidation<br>NPV / IRR Investment Analysis

<div class="cover-sub">Capital Allocation Decision Support &nbsp;|&nbsp; Finance Committee — April 2026</div>
<div class="cover-sub">Prepared by: SponAItech LLC &nbsp;|&nbsp; Confidential</div>

<!--
PRESENTER NOTES — Slide 1: Title

This deck presents the NPV and IRR analysis for Meridian Finance's investor-relations platform consolidation initiative. Meridian currently operates three separate IR platforms — one for institutional investor reporting, one for retail shareholder communications, and one for regulatory filing management. Consolidation onto a single integrated platform is projected to reduce operating cost, improve data consistency, and accelerate reporting timelines. The Finance Committee needs to make a capital allocation decision: approve the investment, hold pending further analysis, or decline. This deck provides the rigorous financial basis for that decision. All figures are derived from Meridian Finance's own cost data and vendor proposals received in Q1 2026.
-->

---

# The Investment — What We Are Deciding

<div class="label">Investment Overview</div>

- **Programme:** IR Platform Consolidation — replace 3 legacy platforms with a single integrated solution
- **Vendor selected:** InvestorFlow Enterprise (shortlisted following 6-month RFP process)
- **Total capital required:** $3.6M over 24 months
- **Funding source:** Technology capital budget FY 2026–2027
- **Decision type:** Approve / Hold / Decline

**Investment components:**

- Platform licence (5-year term): $1.2M
- Implementation and data migration: $1.6M
- Integration (Bloomberg, SEC EDGAR, Nasdaq IR): $0.5M
- Change management and training: $0.3M

<!--
PRESENTER NOTES — Slide 2: Investment Overview

This slide establishes precisely what the committee is being asked to fund. The $3.6M total is a firm number — InvestorFlow provided a fixed-price implementation proposal. The 6-month RFP process included evaluation of 8 vendors; InvestorFlow was selected on the basis of feature fit, implementation track record, and price. The breakdown matters: the $1.6M implementation cost is the largest single component and the area of highest execution risk. The integration with Bloomberg Terminal and SEC EDGAR filing systems is technically complex but has been scoped at $0.5M based on InvestorFlow's existing certified connectors. Change management at $0.3M covers training for 22 IR staff and a 6-month adoption support programme.
-->

---

# Cash Flow Projection — 5-Year Model

<div class="label">Financial Model</div>

| Year | Investment Outflow | Gross Benefit | Net Cash Flow | Discount Factor (8%) | PV of Cash Flow |
|---|---|---|---|---|---|
| Year 0 | <span class="negative">($3,600K)</span> | — | <span class="negative">($3,600K)</span> | 1.000 | <span class="negative">($3,600K)</span> |
| Year 1 | <span class="negative">($120K)</span> | <span class="positive">$1,820K</span> | <span class="positive">$1,700K</span> | 0.926 | <span class="positive">$1,574K</span> |
| Year 2 | <span class="negative">($120K)</span> | <span class="positive">$2,640K</span> | <span class="positive">$2,520K</span> | 0.857 | <span class="positive">$2,159K</span> |
| Year 3 | <span class="negative">($120K)</span> | <span class="positive">$2,780K</span> | <span class="positive">$2,660K</span> | 0.794 | <span class="positive">$2,112K</span> |
| Year 4 | <span class="negative">($120K)</span> | <span class="positive">$2,860K</span> | <span class="positive">$2,740K</span> | 0.735 | <span class="positive">$2,014K</span> |
| Year 5 | <span class="negative">($120K)</span> | <span class="positive">$2,940K</span> | <span class="positive">$2,820K</span> | 0.681 | <span class="positive">$1,920K</span> |
| **Sum** | | | **$8,840K** | | **<span class="positive">$6,179K</span>** |

<div class="footer-note">Ongoing annual cost = $120K support + maintenance. Benefits include labour saving, platform fee elimination, and compliance penalty avoidance. Discount factor = (1 / (1.08)^n).</div>

<!--
PRESENTER NOTES — Slide 3: Cash Flow Projection

Walk through the mechanics. The discount factor column is included deliberately — many committee members are not financial specialists, and showing the calculation builds confidence. Year 0 is the full $3.6M investment. Year 1 benefits of $1,820K reflect a partial-year ramp: the platform goes live in Month 9, so savings accrue for only 4 months of Year 1. Year 2 onwards captures the full annual benefit of $2,640K–$2,940K (growing 3% per year with headcount inflation). The ongoing $120K annual cost covers the platform support SLA. The sum of undiscounted net cash flows is $8,840K — raw return on $3.6M investment. The sum of present values is $6,179K — this is the input to NPV.
-->

---

# Discount Rate — Rationale for 8%

<div class="label">Discount Rate</div>

**Three inputs to the hurdle rate:**

- **Meridian's weighted average cost of capital (WACC):** 6.8%
- **Project risk premium:** +1.0% (technology implementation risk, vendor dependency)
- **Liquidity premium:** +0.2% (illiquid capital commitment, 5-year term)
- **Selected rate: 8.0%**

**What the rate means:**

> An 8% discount rate means we require this investment to return at least 8 cents of value today for every dollar committed — after accounting for the time value of money and project-specific risk.

If the committee believes implementation risk is higher, a 10% rate is modelled in the sensitivity slide.

<!--
PRESENTER NOTES — Slide 4: Discount Rate

The discount rate is the single most contested assumption in any NPV analysis. Anchor it in Meridian's own WACC — which the committee should recognise from the annual financial plan. The 1% risk premium for technology implementation is standard for IT capital projects per Meridian's own capital allocation policy (Section 4.2). The 0.2% liquidity premium is small but principled: once committed, this capital cannot easily be redeployed for 5 years. An 8% combined rate is deliberately conservative — it is higher than the WACC alone. If the committee challenges the rate, offer the sensitivity analysis on Slide 6 which models 10% and 12%. Explain that even at 12%, the project remains NPV-positive.
-->

---

# NPV Result — $2.58M Positive

<div class="label">NPV Analysis</div>

**NPV Formula:**

NPV = Sum of [Net Cash Flow(t) / (1 + r)^t] − Initial Investment

NPV = $6,179K (sum of discounted cash flows) − $3,600K (initial investment)

**NPV = <span class="positive">+$2,579K</span>**

**Interpretation:**

- NPV > 0 — the investment creates value above the hurdle rate
- Every dollar invested returns $1.72 in present value terms
- Accepting this project increases Meridian's enterprise value by approximately $2.58M in today's dollars

<!--
PRESENTER NOTES — Slide 5: NPV Result

Show the arithmetic. NPV is the sum of all discounted cash flows from the projection table ($6,179K) minus the Year 0 investment ($3,600K). The result is +$2,579K — approximately $2.58M of value created above and beyond Meridian's cost of capital. The 1.72x present-value return means that for every dollar invested today, $1.72 of present value is returned over five years. This is a strong result for a technology investment. Anticipate the question: "Why don't we just keep the $3.6M in cash?" Answer: cash earns approximately 5% risk-free today. This investment earns 8% hurdle-adjusted returns. The incremental return above the risk-free rate justifies the investment risk.
-->

---

# IRR Result — 54% Exceeds All Hurdle Rates

<div class="label">IRR Analysis</div>

**IRR is the discount rate at which NPV = 0**

Solving iteratively:

| Discount Rate | NPV |
|---|---|
| 8% | <span class="positive">+$2,579K</span> |
| 20% | <span class="positive">+$1,247K</span> |
| 40% | <span class="positive">+$142K</span> |
| **54%** | **$0** — break-even |
| 60% | <span class="negative">-$298K</span> |

**IRR = <span class="positive">54%</span>** — more than 6x the 8% hurdle rate

This investment would remain NPV-positive even if Meridian's cost of capital tripled to 27%.

<!--
PRESENTER NOTES — Slide 6: IRR Result

IRR is the most intuitive financial metric for many committee members because it expresses return as a percentage — comparable to interest rates and equity return targets. The IRR of 54% means this investment earns 54 cents per dollar per year in present-value terms. The table shows the NPV at various discount rates, illustrating the convergence toward zero at 54%. The 6x coverage ratio (54% IRR vs 8% hurdle) provides substantial cushion against adverse scenarios. The "tripled cost of capital" statement is the resilience punchline — Meridian would need to fundamentally restructure its balance sheet before this investment becomes value-destructive. Use this slide to pre-empt discount rate debates: even at rates far above any plausible WACC, the project is positive.
-->

---

# Sensitivity — Tested Against Key Assumptions

<div class="label">Sensitivity Analysis</div>

| Scenario | NPV | IRR | Decision |
|---|---|---|---|
| Base case (8% rate, benefits as modelled) | <span class="positive">+$2,579K</span> | <span class="positive">54%</span> | GO |
| Conservative benefits (20% haircut) | <span class="positive">+$1,103K</span> | <span class="positive">36%</span> | GO |
| Pessimistic benefits (40% haircut) | <span class="negative">-$373K</span> | <span class="negative">6.8%</span> | HOLD |
| Higher discount rate (10%) | <span class="positive">+$2,186K</span> | <span class="positive">54%</span> | GO |
| Higher discount rate (12%) | <span class="positive">+$1,828K</span> | <span class="positive">54%</span> | GO |
| Implementation overrun (+$500K) | <span class="positive">+$2,079K</span> | <span class="positive">47%</span> | GO |

<div class="footer-note">Project enters HOLD territory only if realised benefits fall 40%+ below modelled levels AND discount rate exceeds 10%. Probability assessed as low given vendor fixed-fee contract and documented baseline savings.</div>

<!--
PRESENTER NOTES — Slide 7: Sensitivity

Sensitivity analysis is where credibility is established or lost. Show the HOLD scenario honestly — a 40% benefit shortfall flips the decision. Then explain why that scenario is unlikely: (1) $1.1M of the $2.64M annual benefit is platform fee elimination — three legacy contracts cancelled on day 1 of go-live. This is not projected, it is contractual. (2) $0.9M is IR staff headcount reduction through attrition — 4 FTEs over 18 months, already in the workforce plan. (3) Only $0.64M is productivity improvement — the portion subject to estimation uncertainty. For the project to deliver a 40% shortfall, the productivity gains would need to be zero AND the contractual savings would need to underperform — an extremely unlikely combination.
-->

---

# Go / Hold Framework — The Decision

<div class="label">Decision Framework</div>

**Approve (GO) if:**
- Committee accepts 8% hurdle rate as appropriate — NPV = **+$2.58M**
- Committee accepts benefit model assumptions — IRR = **54%**
- Committee accepts implementation risk as mitigated by fixed-fee contract

**Hold if:**
- Committee requires a higher hurdle rate (>27%) — rerun with revised WACC
- Committee believes benefit shortfall >40% is likely — requires operational re-validation
- Budget constraint requires deferral — note: each 12-month deferral costs ~$2.0M in foregone NPV

**The ask:** Finance Committee approval of $3.6M capital appropriation, Q2 2026 commencement.

<!--
PRESENTER NOTES — Slide 8: Go / Hold Decision

Close with a decision framework that respects the committee's authority while making the GO case clearly. The three GO conditions are all defensible — the committee knows its own hurdle rate, can challenge the benefit assumptions with operational data, and can assess the fixed-fee contract as a risk mitigator. The HOLD conditions are honest — if the committee genuinely believes benefits will fall 40% short, a hold is rational. But challenge that belief: the contractual savings alone ($1.1M/year in eliminated platform fees) deliver positive NPV of $0.8M even with zero productivity benefit. The deferral cost of $2.0M per year in foregone NPV is a real incentive to decide today. Ask for the vote.
-->
