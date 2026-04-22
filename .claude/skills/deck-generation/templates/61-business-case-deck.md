<!-- TEMPLATE: business-case-deck
     CATEGORY: ROI / Business Case
     USE WHEN: presenting a full business case for a capital investment
     SLIDE COUNT: 12
     PALETTE: Executive cream
     RENDER: marp --pptx 61-business-case-deck.md -->

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
    margin-bottom: 24px;
  }
  h2 {
    color: var(--color-accent);
    font-size: 1.1rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 8px;
  }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 10px; font-size: 1.05rem; line-height: 1.5; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
    margin-top: 12px;
  }
  th {
    background: var(--color-fg);
    color: var(--color-bg);
    padding: 8px 12px;
    text-align: left;
    font-weight: 600;
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
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 4px;
    margin-bottom: 14px;
  }
  .cover-sub {
    font-size: 1.1rem;
    color: var(--color-muted);
    margin-top: 12px;
  }
  .footer-note {
    font-size: 0.8rem;
    color: var(--color-muted);
    margin-top: 20px;
  }
---

<!-- _paginate: false -->
# Meridian Health<br>Claims Automation Initiative

<div class="cover-sub">Business Case — Capital Investment Request</div>
<div class="cover-sub">Prepared for: Executive Leadership Committee &nbsp;|&nbsp; April 2026</div>
<div class="cover-sub">Presented by: SponAItech LLC &nbsp;|&nbsp; Confidential</div>

<!--
PRESENTER NOTES — Slide 1: Title

Welcome the executive committee. Set the tone: this presentation makes the case for a $4.2 million investment in AI-powered claims automation at Meridian Health. You have 30 minutes. Summarise the agenda: problem, status quo cost, proposed solution, options comparison, recommendation, financials, payback, risk, phasing, governance, and the ask. Remind the audience that all numbers are derived from Meridian's own operational data validated by SponAItech analysis in Q1 2026. If there are questions mid-deck, capture them for the appendix section — you have supporting detail there.
-->

---

# The Problem — Manual Claims Drain Margin

<div class="label">Problem Statement</div>

- Meridian processes **1.4 million claims per month** across three regional hubs
- **72% of all claims** require at least one manual touch — adjuster review, data re-entry, or denial rework
- End-to-end cycle time averages **14.2 days**, vs. industry benchmark of **6.5 days**
- Member and provider complaints about delays rose **38% YoY** in 2025

> "We are spending money to be slow. Every dollar paid in manual labor is a dollar that does not reach care delivery."
> — CFO, Meridian Health (Q4 2025 ops review)

<!--
PRESENTER NOTES — Slide 2: The Problem

This slide grounds the audience in operational reality before any financial discussion. The 72% manual-touch figure comes from Meridian's own claims system audit conducted in November 2025 — it is not an estimate. The 14.2-day average cycle time is the trailing 12-month figure from the claims management platform. The 38% YoY increase in complaints was reported in the Q4 CSAT summary. Use the CFO quote to validate that leadership has already acknowledged the pain — this is not news to them, it is confirmation that the pain is real and documented. Pause here for any additions from operational leaders in the room.
-->

---

# Status Quo — Loaded Cost of Current Operations

<div class="label">Baseline</div>

| Cost Category | Annual Spend |
|---|---|
| Claims adjuster headcount (FTE × loaded rate) | <span class="negative">$18.4M</span> |
| Re-work and denial management | <span class="negative">$4.1M</span> |
| Overtime and temp staff (peak months) | <span class="negative">$2.2M</span> |
| Compliance penalties (late-pay violations) | <span class="negative">$0.9M</span> |
| Technology maintenance (legacy systems) | <span class="negative">$1.6M</span> |
| **Total annual baseline cost** | **<span class="negative">$27.2M</span>** |

<div class="footer-note">Source: Meridian Finance operational cost report, FY 2025. Loaded FTE rate = salary + benefits + overhead at 1.42x.</div>

<!--
PRESENTER NOTES — Slide 3: Status Quo Cost

Walk through each line deliberately. The $18.4M FTE cost is the largest driver — 342 FTEs at an average loaded rate of $53,800. Emphasise that this is not just salary; benefits, management overhead, training, and facilities are included at the 1.42x multiplier. The $4.1M re-work cost reflects the cost of denied claims that cycle back through the system — on average, each denial re-work costs $47 in labor plus extended cycle time. Compliance penalties at $0.9M are real dollars paid to CMS and state agencies for late adjudication violations — these are recoverable immediately upon automation. The $1.6M legacy technology maintenance is a sunk cost today but a replacement obligation within 24 months regardless of this investment.
-->

---

# Proposed Solution — AI-Powered Claims Engine

<div class="label">Recommendation Preview</div>

- Deploy SponAItech **ClaimsAI platform** — rules-based + ML hybrid adjudication engine
- Integrate with Meridian's existing Facets claims management system via certified API
- Automate **straight-through processing (STP)** for low-complexity claim types (est. 68% of volume)
- Human-in-the-loop review retained for complex, high-value, and disputed claims

**Projected steady-state outcome (Year 3):**

- STP rate: <span class="positive">68%</span> (from current 28%)
- Average cycle time: <span class="positive">4.8 days</span> (from 14.2)
- Annual operating cost: <span class="positive">$14.1M</span> (from $27.2M)

<!--
PRESENTER NOTES — Slide 4: Proposed Solution

This is the pivot from problem to solution. ClaimsAI uses a two-layer approach: first, a deterministic rules engine handles clear-cut eligibility and coverage decisions with zero human touch. Second, an ML model trained on Meridian's own historical adjudication decisions handles the ambiguous middle tier. Only genuinely complex cases — appeals, multi-party liability, experimental treatment disputes — go to a human adjuster. The 68% STP target is conservative; pilot data from comparable payers shows 71-74% achievable, but we projected 68% to build in margin for Meridian's higher-acuity member mix. The 4.8-day cycle time is derived from the automated processing time plus a 1-day buffer for exception routing.
-->

---

# Options Compared — Three Paths Forward

<div class="label">Options Analysis</div>

| Criterion | Option A — Do Nothing | Option B — Incremental RPA | Option C — ClaimsAI (Recommended) |
|---|---|---|---|
| 3-Year total cost | <span class="negative">$81.6M</span> | <span class="neutral">$68.2M</span> | <span class="positive">$51.4M</span> |
| STP rate (Year 3) | 28% | 41% | 68% |
| Cycle time (Year 3) | 14.2 days | 9.8 days | 4.8 days |
| Implementation risk | Low | Medium | Medium |
| Compliance exposure | High | Medium | Low |
| Scalability | None | Limited | Full |

<!--
PRESENTER NOTES — Slide 5: Options Compared

Always present at least three options — do nothing, partial solution, and full solution. Option A is not truly "free" — it locks in $27.2M per year of operating cost, growing 3% annually with headcount inflation, and carries escalating compliance risk. Option B — incremental RPA using tools like UiPath — would automate data-entry tasks only, not adjudication decisions. It delivers modest improvement at $4.2M implementation cost but creates significant technical debt and reaches a ceiling at 41% STP. Option C is the recommended path. The $51.4M 3-year cost includes the full ClaimsAI implementation and support fees. The net saving versus do nothing is $30.2M over three years.
-->

---

# Recommended Option — Financial Summary

<div class="label">Investment Case</div>

| Metric | Value |
|---|---|
| Total implementation investment | <span class="negative">$4.2M</span> |
| Annual savings at steady state (Year 3+) | <span class="positive">$13.1M</span> |
| Net present value (5-year, 8% discount rate) | <span class="positive">$38.4M</span> |
| Internal rate of return | <span class="positive">187%</span> |
| Payback period | <span class="positive">5.8 months</span> |
| Benefit-cost ratio | <span class="positive">9.1x</span> |

All financial projections assume 3% annual headcount cost inflation and 98% system uptime SLA.

<!--
PRESENTER NOTES — Slide 6: Financial Summary

These are the headline numbers the committee needs. The $4.2M investment breaks down as: $2.1M ClaimsAI platform license and implementation (Year 1), $0.8M integration and data migration, $0.7M training and change management, and $0.6M contingency. The $13.1M annual saving at steady state is Year 3 actual — Year 1 saving is $6.4M (partial year ramp) and Year 2 is $11.2M. NPV of $38.4M uses an 8% hurdle rate — if the committee prefers 10%, NPV remains strongly positive at $32.1M. The 187% IRR and 5.8-month payback period are exceptional even by aggressive investment standards. Invite the CFO to confirm the hurdle rate assumption.
-->

---

# ROI Breakdown — Year-by-Year Detail

<div class="label">Financial Model</div>

| Year | Investment | Gross Savings | Net Cash Flow | Cumulative |
|---|---|---|---|---|
| Year 0 | <span class="negative">($4.2M)</span> | — | <span class="negative">($4.2M)</span> | <span class="negative">($4.2M)</span> |
| Year 1 | <span class="negative">($0.4M)</span> | <span class="positive">$6.4M</span> | <span class="positive">$6.0M</span> | <span class="positive">$1.8M</span> |
| Year 2 | <span class="negative">($0.4M)</span> | <span class="positive">$11.2M</span> | <span class="positive">$10.8M</span> | <span class="positive">$12.6M</span> |
| Year 3 | <span class="negative">($0.4M)</span> | <span class="positive">$13.1M</span> | <span class="positive">$12.7M</span> | <span class="positive">$25.3M</span> |
| Year 4 | <span class="negative">($0.4M)</span> | <span class="positive">$13.5M</span> | <span class="positive">$13.1M</span> | <span class="positive">$38.4M</span> |

<div class="footer-note">Year 1 savings reflect 6-month ramp-up. Ongoing annual support fee = $0.4M. Savings grow 3% annually post-Year 3.</div>

<!--
PRESENTER NOTES — Slide 7: ROI Breakdown

Walk the table row by row. Year 0 is the implementation investment — front-loaded to enable the fastest possible payback. Note that Year 1 shows a net positive cash flow of $6.0M because savings begin accruing within the first six months once the platform goes live in Month 7. By end of Year 1, cumulative cash flow is already positive at $1.8M. This is unusual for a technology investment of this scale and reflects the high operating leverage inherent in automating labor-intensive processes. The ongoing $0.4M annual support fee covers platform updates, model retraining, and 24x7 support SLA. Ask: does anyone want to revisit the Year 1 savings assumption? We can walk through the ramp model in detail in the appendix.
-->

---

# Payback — Break-Even in Month 6

<div class="label">Payback Analysis</div>

- Implementation begins **Month 1** — platform configuration and data integration
- Go-live target: **Month 7** — production cutover with parallel run period
- Cumulative savings equal total investment at **Month 12.6** (call it Month 13 conservatively)
- For planning purposes: **payback in under 14 months** from board approval

**Sensitivity check — what if savings are 20% lower than projected?**

- Revised annual saving: $10.5M (vs. $13.1M base case)
- Revised payback: 19 months
- Revised 5-year NPV: <span class="positive">$28.2M</span> — still strongly positive

<!--
PRESENTER NOTES — Slide 8: Payback

The payback of 5.8 months referenced on the prior slide measures from go-live, not from board approval. From board approval, adding the 7-month implementation period gives a total of approximately 13 months — which we conservatively state as 14 months. This is the right number to communicate to a board that thinks in annual planning cycles. The 20% downside sensitivity is important — even if the operations team is pessimistic about the automation rate, the investment remains highly attractive. In fact, the project would need to deliver less than 32% of projected savings to break even over five years. That threshold is extremely unlikely to miss.
-->

---

# Risks — Identified and Mitigated

<div class="label">Risk Register</div>

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Integration delay (Facets API) | Medium | High | Dedicated integration sprint; vendor SLA contractual |
| Model accuracy below 95% threshold | Low | High | Parallel run period; human review fallback for 90 days |
| Staff resistance / change fatigue | Medium | Medium | Change management workstream; redeployment plan for 40 FTEs |
| Regulatory interpretation changes | Low | Medium | Rules engine updatable in <24hrs; compliance team on retainer |
| Scope creep | Medium | Medium | Fixed-scope Phase 1; Phase 2 governed separately |

<!--
PRESENTER NOTES — Slide 9: Risks

Every credible business case acknowledges risk honestly — a risk-free case is not credible. The highest-impact risk is integration delay, because Facets is a notoriously complex legacy platform. We have mitigated this by contracting Facets' own professional services team for the API work, with a fixed-fee SLA. The staff resistance risk is real — 342 adjusters are aware that automation is coming. The mitigation is a formal redeployment plan: 40 FTEs will be retrained for quality assurance, exception handling, and member advocacy roles — net headcount reduction is achieved through attrition, not layoffs, over 18 months. This is a deliberate choice to preserve Meridian's workforce brand and reduce union risk.
-->

---

# Phasing — Three-Phase Delivery Plan

<div class="label">Implementation Roadmap</div>

| Phase | Timeline | Scope | Investment |
|---|---|---|---|
| Phase 1 — Foundation | Months 1–7 | Platform deployment, Facets integration, STP for Tier 1 claims | <span class="negative">$2.8M</span> |
| Phase 2 — Expansion | Months 8–14 | ML adjudication for Tier 2 claims, denial management automation | <span class="negative">$1.0M</span> |
| Phase 3 — Optimization | Months 15–24 | Model retraining, provider portal integration, analytics dashboard | <span class="negative">$0.4M</span> |

Gate criteria between phases: Phase 1 STP rate must reach **40%** before Phase 2 begins.

<!--
PRESENTER NOTES — Slide 10: Phasing

Phasing de-risks the investment and creates natural decision gates. Phase 1 delivers the highest-confidence automation — Tier 1 claims are those with complete data, no coordination of benefits, and straightforward coverage rules. These represent approximately 40% of volume but account for only 18% of claims spend. The Phase 1 go/no-go gate requires achieving a 40% STP rate, which is well below the steady-state 68% target. If Phase 1 underperforms, the committee can pause before committing Phase 2 capital. Phase 2 adds the ML layer for the harder adjudication decisions. Phase 3 is optimization — model drift correction, provider-facing automation, and executive analytics. The Phase 3 scope is effectively self-funding from Phase 2 savings.
-->

---

# Governance — Decision Rights and Oversight

<div class="label">Operating Model</div>

- **Executive Sponsor:** Chief Financial Officer
- **Programme Director:** VP, Claims Operations
- **Technical Owner:** CIO / VP Engineering
- **Vendor Management:** SponAItech LLC (prime) + Facets PS (sub)
- **Steering Committee:** Monthly — CFO, COO, CIO, VP Claims, Legal
- **Reporting cadence:** Weekly dashboard (automated) | Monthly steering deck | Quarterly board update
- **Change control:** Any scope change >$100K or >2-week timeline impact requires steering committee approval

<!--
PRESENTER NOTES — Slide 11: Governance

Clear governance is the difference between a programme that drifts and one that delivers. The CFO as executive sponsor signals that this is a financial performance initiative, not just an IT project — that framing matters for adjuster engagement and vendor accountability. The monthly steering committee is deliberately cross-functional: CFO owns the financial gate, COO owns operational readiness, CIO owns technical delivery, and Legal monitors regulatory risk. The $100K change control threshold is intentionally low — it creates a habit of discipline from Day 1. SponAItech will produce the weekly automated dashboard from system telemetry; no manual reporting burden falls on Meridian staff.
-->

---

# The Ask — Approve and Move

<div class="label">Decision Required</div>

**We are requesting Executive Committee approval for:**

- Phase 1 capital appropriation: **$2.8M** (Months 1–7)
- Phase 2 conditional approval: **$1.0M** (subject to Phase 1 gate passing)
- Phase 3 deferred to Month 12 steering review

**Immediate next steps upon approval:**

1. Contract execution with SponAItech LLC — target 10 business days
2. Kickoff and integration sprint planning — Month 1
3. Facets PS engagement — Month 1

**Without approval today:** Each month of delay costs Meridian approximately **$1.1M** in avoidable operating expense.

<!--
PRESENTER NOTES — Slide 12: The Ask

Close with clarity and urgency. The committee is being asked to approve Phase 1 today and Phase 2 conditionally — Phase 3 is explicitly deferred so the ask feels bounded. The $1.1M monthly cost of delay is calculated as $13.1M annual saving divided by 12 — it is real, documentable, and persuasive without being alarmist. Anticipate two objections: (1) "Can we wait until Q3 budget cycle?" — answer: each quarter of delay forfeits $3.3M in savings, which exceeds the full Phase 1 investment. (2) "What if the model doesn't work?" — answer: Phase 1 contains no ML; it is rules-based only. The parallel run period ensures zero claims are processed without human oversight until accuracy is validated. Thank the committee and open for questions.

APPENDIX NOTE: Slides A1–A6 (not shown) contain: detailed FTE redeployment plan, Facets API architecture diagram, model accuracy validation methodology, full 5-year cash flow model, vendor due diligence summary, and legal/compliance review.
-->
