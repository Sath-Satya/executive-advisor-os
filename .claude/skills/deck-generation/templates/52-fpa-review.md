<!-- TEMPLATE: fpa-review
     CATEGORY: Finance
     USE WHEN: monthly FP&A review with leadership or finance team
     SLIDE COUNT: 10
     PALETTE: Executive cream
     RENDER: marp --pptx 52-fpa-review.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --cream: #f7f4ef;
    --navy: #0e1b2e;
    --gold: #b8965a;
    --muted: #5a6a7a;
    --rule: #d4c9b0;
    --green: #2a7d5f;
    --red: #c0392b;
  }
  section {
    background: var(--cream);
    color: var(--navy);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 60px;
  }
  h1 {
    font-size: 1.85rem;
    font-weight: 700;
    color: var(--navy);
    letter-spacing: -0.3px;
    border-bottom: 3px solid var(--gold);
    padding-bottom: 8px;
    margin-bottom: 20px;
  }
  h2 { font-size: 1.25rem; font-weight: 600; color: var(--gold); margin-bottom: 14px; }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 9px; font-size: 1.0rem; line-height: 1.5; }
  table { width: 100%; border-collapse: collapse; font-size: 0.92rem; margin-top: 10px; }
  th { background: var(--navy); color: var(--cream); padding: 7px 11px; text-align: left; }
  td { padding: 6px 11px; border-bottom: 1px solid var(--rule); }
  tr:nth-child(even) td { background: #ede9e0; }
  .label {
    display: inline-block; background: var(--gold); color: var(--cream);
    font-size: 0.70rem; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; padding: 2px 9px; border-radius: 3px; margin-bottom: 10px;
  }
  .fav { color: var(--green); font-weight: 700; }
  .unfav { color: var(--red); font-weight: 700; }
  .kpi-row { display: flex; gap: 24px; margin-top: 18px; }
  .kpi {
    flex: 1; background: var(--navy); color: var(--cream);
    border-radius: 8px; padding: 18px 20px; text-align: center;
  }
  .kpi .num { font-size: 1.75rem; font-weight: 700; color: var(--gold); }
  .kpi .lbl { font-size: 0.76rem; color: #a0b0c0; margin-top: 4px; }
  section.cover { background: var(--navy); color: var(--cream); display: flex; flex-direction: column; justify-content: center; }
  section.cover h1 { color: var(--cream); border-color: var(--gold); font-size: 2.2rem; }
  section.cover .sub { color: var(--gold); font-size: 1.0rem; margin-top: 8px; }
  section.cover .meta { color: #8899ac; font-size: 0.85rem; margin-top: 20px; }
  section.close { background: var(--navy); color: var(--cream); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
  section.close h1 { color: var(--gold); border: none; font-size: 2.0rem; }
---

<!-- _class: cover -->

<div class="label">Monthly Finance Review</div>

# Northwind Capital — FP&amp;A Review
## June 2026 MTD / YTD Actuals vs. Budget

<div class="sub">Prepared for: Executive Leadership Team</div>
<div class="meta">July 8, 2026 &nbsp;|&nbsp; Finance &amp; Strategy &nbsp;|&nbsp; Confidential</div>

<!-- Presenter notes: This is the monthly FP&A review for June 2026, covering month-to-date and year-to-date performance versus the annual operating plan approved by the board in December 2025. The deck is prepared by the Finance team and is distributed to the executive leadership team and board finance committee only — it is marked confidential and should not be shared externally. The format follows our standard structure: actuals → budget variance → segment breakdown → forecast → risks and opportunities → KPIs → cash → actions. We have 45 minutes allocated; the CFO will walk through slides 2–8 with input from segment leads on slide 4. Please hold questions until the end of each section or raise them in the chat for the CFO to capture. Slide 9 contains the action items from last month's review — we will cover status before closing. -->

---

# MTD and YTD Actuals — June 2026

<div class="label">Revenue Performance</div>

<div class="kpi-row">
  <div class="kpi"><div class="num">$15.8M</div><div class="lbl">June Revenue (MTD)</div></div>
  <div class="kpi"><div class="num">$91.0M</div><div class="lbl">H1 Revenue (YTD)</div></div>
  <div class="kpi"><div class="num">49.2%</div><div class="lbl">YTD Plan Attainment</div></div>
  <div class="kpi"><div class="num">$4.3M</div><div class="lbl">Adj. EBITDA (MTD)</div></div>
</div>

- June revenue $15.8M vs. $14.9M plan — <span class="fav">+$0.9M favorable (6.0%)</span>
- YTD revenue $91.0M vs. $84.2M prior year — <span class="fav">+8.1% YoY growth</span>
- Q2 closed $2.1M above plan; strongest quarter since Q3 2024

<!-- Presenter notes: June marked an exceptionally strong month, driven by three Capital Markets deal closings that were originally planned for July but accelerated at client request. This represents a pull-forward of approximately $1.8M that will create a headwind in July's numbers — the finance team has already adjusted the rolling forecast to reflect this. The 49.2% H1 plan attainment against a $185M annual budget puts us slightly ahead of pace for the year. Historically, Q3 is our strongest quarter (approximately 28% of annual revenue), so H1 slightly below 50% of plan is appropriate and consistent with seasonal patterns. June EBITDA of $4.3M reflects the high-margin advisory mix in the month — three of the four June closings were advisory versus lending, which carry significantly higher margins. The team should note that June results are preliminary pending final adjustments; accruals for compensation, benefits, and certain vendor invoices are estimated. Final close will be complete by July 14. -->

---

# Budget vs. Actual — Income Statement

<div class="label">June 2026 Variance Analysis</div>

| Line Item | Actual | Budget | Variance $ | Variance % |
|---|---|---|---|---|
| Revenue | $15.8M | $14.9M | <span class="fav">+$0.9M</span> | <span class="fav">+6.0%</span> |
| Cost of Revenue | $9.4M | $9.0M | <span class="unfav">-$0.4M</span> | <span class="unfav">-4.4%</span> |
| Gross Profit | $6.4M | $5.9M | <span class="fav">+$0.5M</span> | <span class="fav">+8.5%</span> |
| Compensation &amp; Benefits | $7.5M | $7.3M | <span class="unfav">-$0.2M</span> | <span class="unfav">-2.7%</span> |
| G&amp;A | $1.4M | $1.5M | <span class="fav">+$0.1M</span> | <span class="fav">+6.7%</span> |
| Adjusted EBITDA | $4.3M | $3.7M | <span class="fav">+$0.6M</span> | <span class="fav">+16.2%</span> |

- Revenue outperformance on deal timing; COGS variance reflects variable deal-related costs
- Comp overage: $0.2M driven by incentive accrual true-up on Q2 above-plan performance

<!-- Presenter notes: The income statement variance table shows a net favorable outcome at every level except cost of revenue and compensation. The COGS overage of $0.4M is directly associated with the revenue beat — variable deal costs including due diligence fees, travel, and third-party advisory costs that are deal-contingent. These are fully offset by the revenue upside, so gross profit still improved $0.5M. The compensation overage requires more explanation: our incentive compensation plan provides for above-target payouts when performance exceeds plan by more than 5% in a quarter. Because Q2 closed 5.6% above plan, we triggered an incentive accrual true-up of $0.2M. This was anticipated in our contingent forecast but not in the base budget. Going forward, if full-year performance tracks above plan, we should expect incremental incentive expense of approximately $0.8M versus budget for the full year. This is still net positive given the revenue overperformance. G&A savings of $0.1M reflect the Chicago office closure. -->

---

# Variance by Segment

<div class="label">June Revenue vs. Budget</div>

| Segment | Actual | Budget | Var. $ | Var. % | Key Driver |
|---|---|---|---|---|---|
| Capital Markets | $7.2M | $6.0M | <span class="fav">+$1.2M</span> | <span class="fav">+20.0%</span> | 3 deal closings vs. 2 planned |
| Lending &amp; Credit | $5.3M | $5.6M | <span class="unfav">-$0.3M</span> | <span class="unfav">-5.4%</span> | 1 facility delayed to July |
| Wealth Management | $3.3M | $3.3M | $0.0M | flat | In line; AUM stable |
| **Total** | **$15.8M** | **$14.9M** | **<span class="fav">+$0.9M</span>** | **<span class="fav">+6.0%</span>** | |

- Capital Markets: Atlanta office contributed first revenue ($0.2M); inaugural mandate closed
- Lending shortfall: $0.3M facility delayed — Drew &amp; Associates credit approval extended to July 15

<!-- Presenter notes: The segment breakdown reveals that our June beat was concentrated in Capital Markets and offset slightly by a Lending shortfall. The Capital Markets beat reflects deal timing rather than new business — three mandates closed in June versus two planned, with the third (a $35M acquisition financing for a manufacturing client) closing three weeks ahead of schedule. This is positive in one sense but creates a revenue timing effect: July Capital Markets is currently tracking below plan by approximately $0.8M as a result. The Lending shortfall is more straightforward — the Drew & Associates revolving credit facility ($12M facility, $0.3M fee recognition) required an extended credit committee review due to a covenant renegotiation request. Approval is expected by July 15; revenue will be recognized in July. Wealth Management is exactly on plan, which reflects the stable AUM trajectory and predictable recurring fee structure. The Atlanta inaugural mandate closing is a significant milestone — this is the first revenue from our geographic expansion and validates the investment thesis. -->

---

# Forecast Update — Full Year 2026

<div class="label">Rolling Forecast vs. Annual Operating Plan</div>

| Metric | AOP | Prior Forecast | Updated Forecast | Variance to AOP |
|---|---|---|---|---|
| Revenue | $185.0M | $185.8M | $186.4M | <span class="fav">+$1.4M</span> |
| Gross Margin % | 40.0% | 40.2% | 40.4% | <span class="fav">+40 bps</span> |
| Adjusted EBITDA | $26.9M | $27.2M | $27.6M | <span class="fav">+$0.7M</span> |
| Free Cash Flow | $18.0M | $18.5M | $19.1M | <span class="fav">+$1.1M</span> |

- H2 pull-forward risk: $1.8M of June revenue was originally H2; partially offset by Atlanta ramp
- Forecast confidence level: **Medium-High** — pipeline visible through October; Q4 carry risk remains

<!-- Presenter notes: The updated full-year forecast raises our expected revenue by $1.4M versus the Annual Operating Plan, driven primarily by the strong H1 performance. The key modeling assumptions underlying this forecast are: Capital Markets closes 17 of 18 active pipeline mandates by year-end (one assumed to slip to Q1 2027), Lending adds $22M of new facilities in H2 at current pricing, Wealth Management AUM grows 3% organically in H2 from market appreciation and new inflows, and Atlanta contributes $1.5M in H2 from the three mandates currently in late-stage discussions. The forecast does not include the private credit fund as it is targeted for a Q1 2027 launch. Risks to the upside include additional M&A activity in our mid-market focus (sub-$500M transactions) if deal conditions remain favorable. Risks to the downside include any deterioration in credit markets that could delay Lending closings or M&A deal abandonment in Capital Markets. Our scenario analysis shows a range of $182M (downside: 2 major deal slips) to $190M (upside: 3 pipeline add-ons accelerate). -->

---

# Risks and Opportunities

<div class="label">H2 2026 Outlook</div>

**Upside Risks**
- Atlanta pipeline: 3 mandates in exclusive discussions, potential $1.2M incremental revenue
- Private credit: If launched Q4 rather than Q1 2027, could generate $0.4M in commitment fees

**Downside Risks**
- Deal timing: $3.2M of Capital Markets revenue in single large transaction expected Q4 — slip risk
- Credit quality: 2 Lending facilities on watch list; if covenant breach, $0.8M revenue at risk
- Macro: Rate increase &gt;50 bps could compress NIM and reduce demand for M&amp;A financing

<!-- Presenter notes: The risk register captures the items that sit outside our base forecast that could move results materially in either direction. On the upside, the Atlanta pipeline has advanced faster than our initial assumptions — the three mandates in exclusive discussions would add $1.2M if they all close in Q3/Q4, which our local team believes is achievable. The private credit fund acceleration is speculative but worth flagging given investor interest we have received. On the downside, the single large transaction risk is the most material: we have one Capital Markets mandate for a $280M acquisition where the buyer is expected to close in Q4 but faces regulatory review that could extend the timeline. This transaction alone represents $3.2M in fees. We are monitoring closely and have a risk-adjusted version of the forecast that assumes a 30% probability of a Q1 2027 close. The two Lending facilities on the watch list are in sectors with higher credit sensitivity; we have proactively tightened covenants but revenue recognition is contingent on continued compliance. Finance will provide a credit quality update in the August FP&A review. -->

---

# KPI Scorecard — June 2026

<div class="label">Operating Metrics</div>

| KPI | Target | Actual | Status |
|---|---|---|---|
| Revenue Growth YoY | &gt;7% | 8.4% | <span class="fav">&#x2713; On Track</span> |
| Gross Margin | &gt;40% | 40.5% | <span class="fav">&#x2713; On Track</span> |
| Adj. EBITDA Margin | &gt;14% | 14.4% | <span class="fav">&#x2713; On Track</span> |
| Free Cash Flow Conversion | &gt;100% net income | 134% | <span class="fav">&#x2713; On Track</span> |
| Net Debt / EBITDA | &lt;1.0x | 0.5x | <span class="fav">&#x2713; On Track</span> |
| Capital Markets Pipeline | &gt;15 mandates | 18 mandates | <span class="fav">&#x2713; On Track</span> |
| Wealth AUM | &gt;$2.0B | $2.1B | <span class="fav">&#x2713; On Track</span> |
| Days Sales Outstanding | &lt;30 days | 24 days | <span class="fav">&#x2713; On Track</span> |

All 8 KPIs on track. No red indicators this month.

<!-- Presenter notes: This is only the second month in the past 18 months that all eight KPIs are simultaneously on track — the last time was November 2024. The standout metrics are free cash flow conversion (134% of net income) and DSO (24 days, the lowest since we implemented our current billing practices). DSO improvement reflects our new invoicing workflow implemented in May that sends electronic invoices immediately upon deal close rather than within five business days. The Capital Markets pipeline count of 18 is a record and provides visibility into H2 revenue. The team should note that pipeline count is a leading indicator, not a guarantee — our historical conversion rate from active mandate to closed transaction is approximately 72% within the expected quarter and 88% within the following quarter. Wealth AUM of $2.1B includes $1.8B of discretionary and $0.3B of advisory-only assets. We measure AUM at month-end using custodian reports; the $2.1B figure is as of June 30, 2026. -->

---

# Cash Position and Liquidity

<div class="label">Treasury Summary — June 30, 2026</div>

| Item | Balance | Change MoM | Notes |
|---|---|---|---|
| Operating Cash | $38.4M | +$4.1M | Strong advisory fee collections |
| Revolver Drawn | $4.0M | -$2.0M | Repaid $2M in June |
| Available Revolver | $48.0M | +$2.0M | Total $52M facility |
| Net Cash / (Debt) | +$34.4M available liquidity | | |

- Quarterly dividend payment of $1.7M (21.8M shares &#215; $0.08) due September 15
- Share buyback: $1.3M deployed in Q2; $8.2M remaining authorization
- No material capital expenditures planned in H2; $1.4M base maintenance CapEx

<!-- Presenter notes: Cash position is the strongest it has been in company history. The $38.4M cash balance reflects excellent collections in June — three advisory transactions closed in the final week of the month and all three were collected within ten business days. Our standard advisory fee terms require 50% at engagement letter and 50% at close; the June closings generated approximately $3.2M in final payment collections. Liquidity of $34.4M (cash less revolver drawn) provides substantial cushion for any market dislocation or strategic opportunity. The board has authorized management to maintain a minimum liquidity floor of $15M at all times, which we are well above. The revolver is available for opportunistic use but carries a 35 basis point commitment fee on undrawn balances; we will evaluate whether to further reduce the drawn balance in Q3 given our cash generation trajectory. The dividend of $0.08 per share ($1.7M total) represents a modest payout ratio of approximately 20% of trailing twelve-month adjusted earnings, consistent with our capital return philosophy of prioritizing reinvestment and buybacks over dividends. -->

---

# Actions and Accountability

<div class="label">Decision and Follow-Up Items</div>

| # | Action | Owner | Due Date | Status |
|---|---|---|---|---|
| 1 | Finalize H2 revenue forecast incorporating June pull-forward | CFO | July 14 | In Progress |
| 2 | Present Drew &amp; Associates credit approval update | CCO | July 16 | Pending |
| 3 | Review Atlanta office Q3 revenue plan vs. initial assumption | CRO | July 22 | Not Started |
| 4 | Prepare private credit fund go/no-go decision memo | CFO + CEO | August 1 | Not Started |

Previous month actions: Items 1–3 from June review all completed on time.

<!-- Presenter notes: This slide captures the four action items arising from today's review. Item 1 is the most time-sensitive — the updated forecast must be complete before the July board finance committee call on July 16. The CFO will circulate a draft by July 14 for executive review. Item 2 requires the Chief Credit Officer to brief the executive team on the Drew & Associates situation before the next scheduled payment date. If the credit approval is not received by July 15 as expected, we will need to assess whether to extend the timeline or initiate covenant enforcement procedures — a decision that has P&L implications. Item 3 is a strategic review: the Atlanta office is performing ahead of plan on revenue but we should verify that the cost structure (4 senior advisors plus office setup) is generating the expected return. Item 4 is the highest-stakes decision: the CFO and CEO will prepare a go/no-go memo on the private credit fund launch. Key considerations include LP commitments secured to date, regulatory timeline, and opportunity cost of management bandwidth. Please confirm acceptability of these action items and owners before we close. -->

---

<!-- _class: close -->

# FP&amp;A Review Complete

**Next Review:** August 12, 2026 &nbsp;|&nbsp; July Actuals

Finance Team: finance@northwindcapital.com
Questions outside this session: contact CFO office directly

**Reminder:** This presentation is confidential. Do not distribute.

<!-- Presenter notes: This closes the June FP&A review. Before we adjourn, please confirm that all four action items are accepted with the named owners and due dates. If there are any disagreements on ownership or timeline, resolve them now. The August review will cover July actuals, which will reflect the pull-forward impact on Capital Markets revenue and the Drew & Associates lending resolution. We expect July to show a revenue dip versus June given the timing effects discussed — please calibrate expectations accordingly. The Finance team will distribute written meeting minutes within 48 hours. The next scheduled touchpoint is the board finance committee call on July 16, where the CFO will present a summary of H1 results and the updated full-year forecast. Executive team members are welcome to join that call; dial-in details will be circulated separately. Thank you for your engagement today. -->
