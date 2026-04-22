<!-- TEMPLATE: 08-investor-update-deck  CATEGORY: Executive / Pitch  USE WHEN: Monthly or quarterly investor update — metrics, highlights, lowlights, asks  SLIDE COUNT: 9  PALETTE: Executive cream (#f7f4ef bg, #0e1b2e headings, #b8965a accent)  RENDER: marp --pptx 08-investor-update-deck.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: 'DM Sans', system-ui, sans-serif; background: #f7f4ef; color: #1c1a18; padding: 60px 80px; }
  h1 { font-family: 'DM Serif Display', Georgia, serif; color: #0e1b2e; letter-spacing: -0.5px; font-size: 2em; }
  h2 { color: #b8965a; font-size: 1.25em; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.5em; }
  strong { color: #0e1b2e; }
  table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
  th { background: #0e1b2e; color: #f7f4ef; padding: 10px 14px; text-align: left; }
  td { padding: 10px 14px; border-bottom: 1px solid #ddd6c8; }
  .big { font-size: 2.8em; font-weight: 700; color: #0e1b2e; display: block; line-height: 1; }
  .label { font-size: 0.8em; color: #7a6e60; text-transform: uppercase; letter-spacing: 0.06em; }
  .gold { color: #b8965a; font-weight: 600; }
  .grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; margin-top: 24px; }
  .metric-box { background: #fff; border: 1px solid #ddd6c8; border-top: 4px solid #b8965a; padding: 24px; border-radius: 6px; }
---

# Helix — Investor Update
## April 2026 &nbsp;|&nbsp; Month 18

**Prepared for:** Series A Investors &nbsp;|&nbsp; **Confidential**

---
<!-- Slide 2: Headline Metrics -->

# Metrics — April 2026

<div class="grid3">
  <div class="metric-box">
    <span class="big">$1.7M</span>
    <span class="label">ARR &nbsp; ▲ 22% MoM</span>
  </div>
  <div class="metric-box">
    <span class="big">94</span>
    <span class="label">Active Health Systems</span>
  </div>
  <div class="metric-box">
    <span class="big">112%</span>
    <span class="label">Net Revenue Retention</span>
  </div>
</div>

| KPI | Mar 2026 | Apr 2026 | Target |
|---|---|---|---|
| MRR | $116K | $142K | $140K |
| Gross Margin | 71% | 73% | 72% |
| CAC Payback | 9.4 mo | 8.7 mo | < 10 mo |
| Churn (logo) | 0.8% | 0.6% | < 1% |

<!-- Speaker notes:
The headline tells the story: $1.7M ARR on a 22% month-over-month growth curve, ahead of the $140K MRR plan we set in January. Net Revenue Retention at 112% means existing health systems are expanding faster than we are losing them — every seat we sell today compounds upward. Gross margin improved three points as we migrated the last two legacy customers onto our v2 inference stack, which processes prior-auth decisions at roughly one-third the compute cost of v1. CAC payback continues to shorten because our land motion is increasingly driven by peer referrals inside regional health system consortia — one CFO calls another. Churn dropped to 0.6% logo churn; the two health systems that did not renew last quarter were both sub-$10K ACV accounts we chose not to pursue renewal on due to implementation complexity. This deck covers highlights, lowlights, product, team, and our two asks for this month. Questions after each section are welcome.
-->

---

# Highlights

- **Dignity Health signed** — 7-hospital system, $180K ACV, live in 60 days; largest single logo to date
- **CMS interoperability audit cleared** — zero findings; positions us for VA procurement shortlist in Q3
- **Inference latency** reduced from 4.2s &#8594; 1.8s after model distillation; NPS jumped 11 points to 58
- **Partnerships** — signed data-sharing agreement with Epic App Orchard; bi-directional FHIR sync shipping May 1

<!-- Speaker notes:
Four items deserve emphasis. First, Dignity Health is our strategic anchor for the Catholic health system segment — 47 hospitals nationally, and this 7-system deal opens a warm referral path to the rest of their network. Second, the CMS audit was not planned but became a proof point; three prospects specifically cited it when accelerating procurement timelines. Third, the inference latency improvement is a direct result of the model distillation work we funded with the bridge we raised in February — it paid back in user satisfaction faster than projected, and we expect the NPS gain to translate into expansion revenue in Q2. Fourth, the Epic App Orchard agreement means our product appears natively inside Epic workflows used by 38% of US hospitals. The first co-developed workflow — prior-auth request pre-population — ships May 1 and is already in pilot with four Dignity sites. No other AI clinical-workflow vendor has a comparable integration depth at our stage.
-->

---

# Lowlights

- **Implementation backlog** — 11 signed contracts awaiting onboarding; current capacity handles 4/month; hiring to fix
- **Enterprise sales cycle** extended from 78 &#8594; 105 days average; new legal review layer at IDN-level buyers
- **Data pipeline incident** — Mar 14, 6-hour delay in prior-auth sync for 3 customers; root cause fixed; SLA credits issued
- **Series A timeline** slipping 6 weeks — lead investor diligence extended; anticipated close now early June

<!-- Speaker notes:
We operate with a no-spin policy: here is what went wrong. The implementation backlog is our most urgent operational risk. We are sitting on $1.4M of signed ACV that is not yet live and therefore not yet recognized. Two customers have already escalated through their procurement contacts. We have hired a Head of Customer Implementations — she starts May 5 — and we are piloting a partner-led implementation model with Nordic Consulting that could double throughput by July. The enterprise sales cycle extension is structural: IDN-level procurement now requires a legal opinion from outside counsel on AI liability. We are building a standard BAA addendum and liability cap schedule to accelerate this. The March pipeline incident was a Kafka consumer group lag that cascaded under a batch update; it is patched, and we have added a circuit-breaker. Series A close slipping is disappointing but not alarming — the lead has not reduced their commitment, they have added a technical partner to diligence. We expect term sheet counter by May 10.
-->

---

# Product Update

| Initiative | Status | Ship Date |
|---|---|---|
| Epic FHIR bi-directional sync | &#9646; In QA | May 1 |
| Denial prediction v2 (96% accuracy) | &#9646; In Build | May 28 |
| Bulk prior-auth batch API | &#9646; In Design | Jun 15 |
| HIPAA audit log export (SOC 2 prep) | &#9646; Complete | Apr 12 |

**One metric that matters:** Denial prediction accuracy &#8594; **94.1%** (benchmark: human reviewer 89%)

<!-- Speaker notes:
Product this month is execution-heavy rather than strategy-heavy. The FHIR sync is the highest-stakes item — it is the linchpin of the Epic partnership and four live pilots are waiting on it. QA is green on 41 of 44 test cases; the remaining three involve edge cases in payer-specific PA forms that we are resolving with our clinical informatics team. Denial prediction v2 is the model upgrade that takes accuracy from 90% to a targeted 96% using the 18-month retrospective dataset we licensed from Definitive Healthcare. At 94.1% current accuracy versus a trained human reviewer's 89%, we are already delivering measurable clinical value — but at 96% we can credibly market a reduction in denial appeal labor cost, which CFOs budget separately and can measure directly. The bulk batch API came directly from Dignity Health's implementation team: they process 2,400 prior-auth requests per week and need async processing. This is also likely to apply to two other large prospects. SOC 2 Type 2 audit prep is on track; we expect the audit window to open July 1.
-->

---

# Team Update

| Role | Status |
|---|---|
| Head of Customer Implementations | Offer accepted — starts May 5 |
| Senior ML Engineer (denial prediction) | Interviewing — final round May 3 |
| Enterprise AE (West) | Sourcing — target close May 31 |

**Headcount:** 18 &#8594; 19 (May) &#8594; 21 (Q2 target)

**Culture note:** Completed first all-hands offsite (Apr 10-11, Austin). Engagement survey: 87% favorable.

<!-- Speaker notes:
Three open roles are directly tied to our two biggest risks: implementations backlog and Series A close. The Head of Implementations is our most urgent hire — she comes from Olive AI where she managed 23 concurrent health system onboardings, exactly the operational profile we need. The ML engineer is needed for denial prediction v2; without this hire the May 28 date slips to late June. The West AE opens coverage for California and the Pacific Northwest, where we have three warm inbound leads but no dedicated coverage. On culture: the Austin offsite was our first full-team gathering since founding. The 87% favorable engagement score (benchmark: 78% for Series A-stage companies, per Lattice) tells us the team is aligned and motivated despite the implementation pressure. We operate a 4-day structured week with no internal meetings on Fridays — a retention mechanism that has been mentioned positively in every candidate conversation in the last quarter.
-->

---

# Runway & Financials

<div class="grid3">
  <div class="metric-box">
    <span class="big">14 mo</span>
    <span class="label">Runway at Current Burn</span>
  </div>
  <div class="metric-box">
    <span class="big">$218K</span>
    <span class="label">Monthly Net Burn</span>
  </div>
  <div class="metric-box">
    <span class="big">Jun 26</span>
    <span class="label">Series A Projected Close</span>
  </div>
</div>

| | Q1 Actual | Q2 Plan | Q2 Forecast |
|---|---|---|---|
| Revenue | $348K | $420K | $412K |
| Gross Profit | $247K | $306K | $305K |
| Operating Expenses | $614K | $648K | $641K |
| Net Burn | $367K | $342K | $336K |

<!-- Speaker notes:
At $218K monthly net burn and $3.1M cash on hand, we have 14 months of runway — or 8 months to Series A close with 6 months buffer. That buffer is intentional; we will not run a distressed fundraise. Q1 revenue came in at $348K against a $360K plan, a 3% miss driven by the implementation backlog delaying two customer go-lives by an average of 19 days. Q2 revenue forecast is $412K versus a $420K plan — we are holding the same conservative posture. Operating expenses are tracking slightly below plan because two engineering hires slipped from April to May. Gross margin expanded again: from 68% in Q1 to a projected 74% in Q2 as the Epic integration reduces our per-customer data-prep labor. We are targeting cash-flow breakeven at $4.2M ARR, which at current growth rate is a Q1 2027 event — well within the runway provided by the Series A we are closing.
-->

---

# Asks

**1. Introductions** — Two warm intros would move our pipeline materially:
- **Dr. Sarah Chen**, CMIO at Providence Health (West Coast expansion)
- **Mark Ellison**, Partner at Kaiser Ventures (strategic investor slot in Series A)

**2. Advisory input** — Seeking board guidance on:
- Build vs. buy decision for denial appeal workflow (staff, tool, or partner?)
- Pricing model for bulk batch API — per-request vs. platform tier

<!-- Speaker notes:
We keep asks specific because vague asks produce no action. On introductions: Providence Health is our number-one West Coast strategic target — 51 hospitals, 24K employed physicians. Dr. Chen is the internal champion who approved the Epic App Orchard evaluation criteria that Helix currently meets. A warm introduction from an existing investor who sits on a Providence committee would compress our sales cycle from the current 105-day average to a targeted 45 days. Kaiser Ventures is a strategic investor whose participation would give us patient-flow data access under a research agreement — data that would make our denial model more accurate for HMO patient populations. On the build-versus-buy question for denial appeal: we have a $180K build estimate, a $90K/year SaaS tool option from Waystar, and a partnership term sheet from a legal-tech startup. We would value 20 minutes of board time before May 15 to align on the framework. On batch API pricing: we have two models modeled out and would like investor input before we go to market with Dignity Health's procurement team in May.
-->

---

# Close — One Number to Remember

<div style="text-align: center; margin-top: 40px;">
  <span class="big" style="font-size: 3.5em;">112%</span>
  <p class="label" style="margin-top: 12px;">Net Revenue Retention — our existing customers are funding our next hire</p>
</div>

**Next update:** May 20, 2026 &nbsp;|&nbsp; **Next board meeting:** June 3, 2026

Connect the two intros above before May 10 — that is the single action that most accelerates our June close.

<!-- Speaker notes:
We close on one number because investors track many companies and a single anchor is more durable than a summary. 112% NRR means that even with zero new logo sales, Helix grows. It is the signal that product-market fit is real and that the clinical value we deliver compounds inside each health system. Every expansion dollar is earned without a sales motion — a nurse manager upgrades a department, a CFO adds a payer, a CMIO rolls out to a second facility. That compounding dynamic is what justifies the Series A valuation we are targeting. Thank you for your continued support. The two intros — Dr. Chen at Providence and Mark Ellison at Kaiser Ventures — are the highest-leverage action you can take before our next update. We will follow up individually with context packets for each introduction by Friday. See you on May 20.
-->
