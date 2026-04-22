<!-- TEMPLATE: cfo-briefing
     CATEGORY: Finance
     USE WHEN: CFO briefing to board finance committee or audit committee
     SLIDE COUNT: 8
     PALETTE: Executive cream
     RENDER: marp --pptx 55-cfo-briefing.md -->

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
    padding: 52px 64px;
  }
  h1 {
    font-size: 1.9rem; font-weight: 700; color: var(--navy);
    letter-spacing: -0.4px; border-bottom: 3px solid var(--gold);
    padding-bottom: 10px; margin-bottom: 22px;
  }
  h2 { font-size: 1.25rem; font-weight: 600; color: var(--gold); margin-bottom: 14px; }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 10px; font-size: 1.02rem; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.92rem; margin-top: 12px; }
  th { background: var(--navy); color: var(--cream); padding: 8px 12px; text-align: left; }
  td { padding: 7px 12px; border-bottom: 1px solid var(--rule); }
  tr:nth-child(even) td { background: #ede9e0; }
  .label {
    display: inline-block; background: var(--gold); color: var(--cream);
    font-size: 0.70rem; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; padding: 3px 10px; border-radius: 3px; margin-bottom: 12px;
  }
  .kpi-row { display: flex; gap: 28px; margin-top: 20px; }
  .kpi {
    flex: 1; background: var(--navy); color: var(--cream);
    border-radius: 10px; padding: 20px 24px; text-align: center;
  }
  .kpi .num { font-size: 1.9rem; font-weight: 700; color: var(--gold); }
  .kpi .lbl { font-size: 0.78rem; color: #a0b0c0; margin-top: 6px; }
  .status-green { color: var(--green); font-weight: 700; }
  .status-red { color: var(--red); font-weight: 700; }
  .status-amber { color: #c87000; font-weight: 700; }
  section.cover { background: var(--navy); color: var(--cream); display: flex; flex-direction: column; justify-content: center; }
  section.cover h1 { color: var(--cream); border-color: var(--gold); font-size: 2.3rem; }
  section.cover .sub { color: var(--gold); font-size: 1.05rem; margin-top: 10px; }
  section.cover .meta { color: #8899ac; font-size: 0.88rem; margin-top: 24px; }
  section.asks { background: var(--navy); color: var(--cream); display: flex; flex-direction: column; justify-content: center; }
  section.asks h1 { color: var(--gold); border: none; font-size: 2.0rem; }
  section.asks li { color: #c0cfd8; font-size: 1.05rem; margin-bottom: 16px; }
---

<!-- _class: cover -->

<div class="label">Board Finance Committee Briefing</div>

# Northwind Capital — CFO Briefing
## Q3 2026 Financial and Strategic Update

<div class="sub">Presented by: Sarah Kim, Chief Financial Officer</div>
<div class="meta">November 5, 2026 &nbsp;|&nbsp; Board Finance Committee &nbsp;|&nbsp; Strictly Confidential</div>

<!-- Presenter notes: Good afternoon, committee members. This briefing covers the CFO's quarterly financial and strategic update for Q3 2026, ahead of the full earnings release scheduled for November 6. The format today is condensed relative to the full earnings deck — this briefing is designed for the finance committee's deeper analytical discussion rather than the public-facing presentation. I will cover eight topics: financial summary, cash and runway, revenue trajectory, key risks, capital allocation, KPI scorecard, asks, and close. We have 60 minutes. Please note that Q3 figures are preliminary and unaudited; final results will be confirmed with our external auditors by November 14 and filed on Form 10-Q by November 14, 2026. This presentation is strictly confidential and subject to Regulation FD — it should not be discussed with parties outside the board until after tomorrow's earnings release. -->

---

# Q3 2026 Financial Summary

<div class="label">Preliminary Q3 Results</div>

<div class="kpi-row">
  <div class="kpi"><div class="num">$52.1M</div><div class="lbl">Q3 Revenue</div></div>
  <div class="kpi"><div class="num">$21.5M</div><div class="lbl">Gross Profit (41.3%)</div></div>
  <div class="kpi"><div class="num">$8.4M</div><div class="lbl">Adj. EBITDA (16.1%)</div></div>
  <div class="kpi"><div class="num">$0.37</div><div class="lbl">Adj. EPS</div></div>
</div>

- Q3 revenue $52.1M — strongest quarter in company history; beat Q2 by $4.9M (10.4%)
- YTD revenue $143.1M; on pace for $188–190M full year (above raised guidance midpoint)
- Net income $5.4M; GAAP EPS $0.24; Tax rate 28.4% in line with plan

<!-- Presenter notes: Q3 2026 is Northwind's best quarter on record across every financial metric. Revenue of $52.1M reflects our seasonal peak in Capital Markets — Q3 is historically our best quarter and 2026 did not disappoint, with 12 deal closings in the quarter versus 9 in Q3 2025. The 41.3% gross margin is also a record, reflecting the continued mix shift toward higher-margin advisory work and the full-quarter impact of the G&A savings from the Chicago office closure. Adjusted EBITDA margin of 16.1% exceeds our full-year guidance range of 14–15%, though I want to be careful not to extrapolate Q3 as the run rate — Q4 is typically 12–15% lighter than Q3 in Capital Markets, which will bring the full-year margin back toward 15%. Tax rate of 28.4% is consistent with our annual estimate; no discrete items affected Q3. EPS of $0.37 adjusted puts us at $1.07 YTD adjusted EPS, ahead of the $1.22–1.32 full-year guidance midpoint of $1.27. -->

---

# Cash Position and Runway

<div class="label">Liquidity and Capital Structure — September 30, 2026</div>

| Item | Balance | Change QoQ | Notes |
|---|---|---|---|
| Cash &amp; Equivalents | $44.8M | +$6.4M | Record high; advisory collection timing |
| Short-Term Investments | $5.0M | — | T-bills; 5.1% yield; &lt;90 day maturity |
| Total Liquidity | $49.8M | +$6.4M | |
| Revolver Drawn | $0 | -$4.0M | Fully repaid in Q3 |
| Revolver Available | $52.0M | | Nov. 2028 maturity |
| Net Cash | $49.8M | | |

- 12-month operating cash burn: N/A — company is cash flow positive
- Debt-free as of September 30; first time since 2019
- Minimum liquidity covenant: $15M floor; current position: 3.3x coverage

<!-- Presenter notes: The balance sheet is in the strongest position in company history. For the first time since our 2019 revolving credit facility was established, we ended a quarter with zero drawn on the revolver — we repaid the remaining $4M balance in August from operating cash flow. The $49.8M in total liquidity (cash plus short-term T-bill investments) provides substantial capacity for strategic opportunities, capital return, or weathering an extended market downturn. The $5M T-bill investment was initiated in Q3 in coordination with our treasury policy update — we approved investing up to $10M in 90-day T-bills to generate incremental yield on our cash balance rather than leaving it in our 0.5% operating account. At 5.1% yield, this generated $64K of interest income in Q3, which will be included in other income on our income statement. Going forward, if rates remain above 4%, we will continue investing operating cash above the $20M operating floor in short-duration T-bills. This is conservative treasury management, not speculation. The record cash position raises an important capital allocation question that I will address in Slide 6. -->

---

# Revenue Trajectory and Outlook

<div class="label">Full-Year 2026 Revised Guidance</div>

| Quarter | Revenue | YoY Growth |
|---|---|---|
| Q1 2026 | $43.8M | +7.8% |
| Q2 2026 | $47.2M | +8.4% |
| Q3 2026 | $52.1M | +9.9% |
| Q4 2026E | $45–47M | +6–11% |
| **FY 2026E** | **$188–190M** | **+8–9%** |

- Guidance raised for the second time in 2026; original AOP was $185M
- Q4 pipeline: 8 mandates expected to close; 2 at risk of slipping to Q1 2027
- Wealth Management and Lending tracking at or above full-year targets

<!-- Presenter notes: The revenue trajectory through Q3 shows consistent acceleration: growth rates of 7.8%, 8.4%, and 9.9% in successive quarters. This is unusual — most financial services firms see growth decelerate as the year progresses due to deal timing and seasonality. Our acceleration reflects the Atlanta office contribution, which is ramping through the year, and a particularly active mid-market M&A environment in our core sectors (business services, healthcare services, and industrials). Raising guidance for the second time in 2026 reflects our confidence in Q4. The $45–47M Q4 range is based on 8 pipeline mandates expected to close. The 2 mandates at risk of slipping represent $3.2M in combined fees — if both slip, Q4 comes in at $45M; if both close as expected, Q4 is $47M. I am not comfortable raising guidance beyond $190M at this stage because deal timing in the final weeks of the quarter is always uncertain. We will provide final 2026 full-year results and 2027 initial guidance on the Q4 earnings call scheduled for February 12, 2027. Wealth Management is tracking to $43M for the year (vs. $42.8M AOP) and Lending is at $62M year-to-date, in line with the $62M plan. -->

---

# Key Risks — Q4 and 2027

<div class="label">Material Uncertainties</div>

- **M&amp;A market concentration:** 3 Capital Markets mandates represent $8.4M of Q4+Q1 expected fees — single-client risk if any buyer withdraws
- **Rate environment:** Fed signaling potential Q1 2027 rate decrease of 25–50 bps; would compress NIM by $0.6–1.2M annually — net negative for Lending
- **Technology execution:** Salesforce FSC go-live January 2027; 3-week advisor productivity dip modeled in Q1 forecast; risk of extended delay
- **Talent:** Head of Capital Markets considering outside opportunity; contingency planning in progress (confidential — do not disclose)

<!-- Presenter notes: I want to flag four specific risks that the finance committee should be aware of, some of which are not in the public-facing earnings materials. First, mandate concentration: three of our active Capital Markets mandates are in the business services sector and involve buyers who are serial acquirers. If any single buyer pauses its M&A program, we lose a disproportionate share of Q4 and Q1 pipeline. We are monitoring this closely and I will provide an update at the next board call if the situation changes. Second, rate environment: the forward curve now prices in a 25 bps cut in Q1 2027 with 60% probability. This is a headwind for our Lending NIM — I have modeled the impact at $0.6–1.2M annually depending on the magnitude of cuts. This is a manageable headwind given our revenue growth, but I wanted the committee to be aware. Third, technology: the Salesforce go-live is contractually scheduled for January 2027 but depends on data migration completing by December 15. Migration is on schedule as of today; I will update the committee if this changes. Fourth, and strictly confidential: our Head of Capital Markets has received an outside offer. We are in retention discussions. Loss of this executive would be material to the Atlanta expansion and mandate pipeline. CEO and I are managing this personally. -->

---

# Capital Allocation Framework

<div class="label">Deployment of $49.8M in Liquidity</div>

| Use of Capital | Committed | Available | Timeline |
|---|---|---|---|
| Operating reserve (min. floor) | $15.0M | — | Permanent |
| Technology platform (Salesforce FSC) | $1.8M FY27 | — | Q1–Q3 2027 |
| Atlanta office CapEx | $0.8M | — | Q4 2026–Q1 2027 |
| Share buyback ($8.2M authorization remaining) | Up to $8.2M | $8.2M | Through Q4 2027 |
| Acquisitions / strategic opportunities | TBD | Up to $20M | Board approval required |
| **Unallocated cash above floor** | — | **~$24M** | Available for board direction |

Management recommendation: accelerate buyback to $3–4M in Q4 2026 given current valuation.

<!-- Presenter notes: The capital allocation framework is the most important strategic discussion for this briefing. We have approximately $24M in unallocated cash above our operating reserve and committed investments — this is unprecedented for Northwind and requires a clear framework. Management's recommendation has three components. First, maintain the $15M operating floor as a permanent minimum — this is non-negotiable from a covenant and liquidity management perspective. Second, accelerate the share buyback in Q4 2026. At the current share price of approximately $29, our stock is trading at 10.4x trailing adjusted EBITDA, which we consider below intrinsic value. We have $8.2M of authorization remaining and recommend deploying $3–4M in Q4 at current prices. This is below our intrinsic value estimate of $33–36 per share (12–13x forward EBITDA). Third, reserve up to $20M for strategic acquisitions or investments subject to board approval. We have had preliminary conversations with two potential tuck-in acquisitions: a boutique capital markets advisory firm in Chicago (5 senior advisors, $8M annual revenue) and a wealth management book ($400M AUM, $3.2M annual revenue). Neither is in formal discussions, but the committee should know these opportunities are developing. Full acquisition analysis will be presented for board approval if either advances. -->

---

# KPI Scorecard — Q3 2026

<div class="label">Board-Level Metrics</div>

| KPI | Target | Q3 2026 | Status |
|---|---|---|---|
| Revenue Growth YoY | &gt;7% | 9.9% | <span class="status-green">&#x25CF; Green</span> |
| Adj. EBITDA Margin | &gt;14% | 16.1% | <span class="status-green">&#x25CF; Green</span> |
| Net Debt / EBITDA | &lt;1.0x | -1.2x (net cash) | <span class="status-green">&#x25CF; Green</span> |
| Return on Equity | &gt;15% | 18.4% | <span class="status-green">&#x25CF; Green</span> |
| Voluntary Attrition | &lt;6% | 4.2% (YTD) | <span class="status-green">&#x25CF; Green</span> |
| NPS — Advisory Clients | &gt;60 | 67 | <span class="status-green">&#x25CF; Green</span> |
| Technology Go-Live Progress | On track | On track | <span class="status-amber">&#x25CF; Amber</span> |
| Head of CapMkts Retention | Retained | Under review | <span class="status-amber">&#x25CF; Amber</span> |

6 of 8 KPIs green. 2 amber items flagged for active management.

<!-- Presenter notes: The KPI scorecard shows excellent performance across the financial metrics, with six of eight indicators at green. Two items are amber and require committee awareness. Technology go-live progress is amber because while we are on schedule today, the December 15 data migration deadline is approaching and any slip in the next 6 weeks could delay the January go-live. I have escalated this to the CIO as a P1 priority. The Head of Capital Markets retention is amber given the outside offer situation — we are not in a crisis, but until the retention discussion is concluded, this remains a watch item. I will remove the amber flag as soon as we have a resolution, which we expect by November 15. On the financial KPIs: return on equity of 18.4% is particularly strong and reflects both earnings growth and our lean capital structure. The NPS of 67 is based on our annual client survey conducted in September — this is above our target of 60 and represents a 4-point improvement from the 2025 survey score of 63. High client satisfaction is a leading indicator of repeat mandate business, which is critical to our Capital Markets revenue sustainability. The attrition rate of 4.2% YTD is the lowest in our history and below target, reflecting the retention investments we have made. -->

---

<!-- _class: asks -->

# Board Actions Requested

<div class="label">Finance Committee Decisions</div>

- **Ratify** preliminary Q3 results for tomorrow's earnings release; authorize CFO to certify Form 10-Q
- **Approve** accelerated buyback of up to $4M in Q4 2026 from existing $8.2M authorization
- **Direct** management to prepare full acquisition analysis on Chicago boutique within 60 days
- **Acknowledge** Head of CapMkts retention risk; authorize CEO to execute retention package within existing compensation guidelines

Next scheduled finance committee meeting: February 11, 2027 (Q4 2026 preliminary results briefing)

<!-- Presenter notes: We are requesting four specific actions from the finance committee tonight. First, Q3 ratification: this is procedural but important — the CFO must certify that the committee has reviewed the preliminary results and is not aware of any material issues before the earnings release tomorrow morning. I am not aware of any such issues and am prepared to certify. Second, buyback approval: the existing $8.2M buyback authorization gives management flexibility, but accelerating to $4M in Q4 requires committee concurrence given our capital allocation policy. I believe the current share price represents compelling value and recommend acting before potential Q4 earnings-driven appreciation. Third, acquisition analysis: the Chicago boutique represents an opportunity to add 5 senior advisors with established client relationships in our core Chicago market. We need 60 days to conduct proper due diligence and prepare a full recommendation. I am not pre-approving the acquisition tonight — only requesting authorization to invest management time in the analysis. Fourth, retention package: the CEO and I have identified a retention package for the Head of Capital Markets within existing compensation guidelines ($250K retention bonus + accelerated equity vesting). We need committee acknowledgment that this is appropriate before we execute — it is within our delegated authority but given the seniority of the executive, I wanted the committee's awareness. Are there questions on any of these items before we vote? -->
