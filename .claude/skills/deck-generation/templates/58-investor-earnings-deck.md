<!-- TEMPLATE: investor-earnings-deck
     CATEGORY: Finance
     USE WHEN: full quarterly investor presentation — earnings webcast or roadshow
     SLIDE COUNT: 12
     PALETTE: Dark premium (navy/white/blue)
     RENDER: marp --pptx 58-investor-earnings-deck.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --dark: #0a0e14;
    --surface: #111820;
    --white: #ffffff;
    --blue: #3b9eff;
    --muted: #8899ac;
    --rule: #1e2a38;
    --green: #2dd4a0;
    --amber: #f0a050;
    --red: #f06070;
  }
  section {
    background: var(--dark);
    color: var(--white);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 60px;
  }
  h1 {
    font-size: 1.85rem; font-weight: 700; color: var(--white);
    letter-spacing: -0.3px; border-bottom: 2px solid var(--blue);
    padding-bottom: 8px; margin-bottom: 20px;
  }
  h2 { font-size: 1.15rem; font-weight: 600; color: var(--blue); margin-bottom: 12px; }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 9px; font-size: 1.0rem; line-height: 1.55; color: #d0d8e4; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88rem; margin-top: 10px; }
  th { background: var(--surface); color: var(--blue); padding: 8px 12px; text-align: left; border-bottom: 1px solid var(--blue); }
  td { padding: 7px 12px; border-bottom: 1px solid var(--rule); color: #d0d8e4; }
  tr:nth-child(even) td { background: #0d1520; }
  .label {
    display: inline-block; background: var(--blue); color: var(--dark);
    font-size: 0.68rem; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; padding: 3px 10px; border-radius: 3px; margin-bottom: 12px;
  }
  .kpi-row { display: flex; gap: 20px; margin-top: 18px; }
  .kpi {
    flex: 1; background: var(--surface); border: 1px solid var(--rule);
    border-radius: 10px; padding: 18px 22px; text-align: center;
    border-top: 3px solid var(--blue);
  }
  .kpi .num { font-size: 1.8rem; font-weight: 700; color: var(--blue); }
  .kpi .lbl { font-size: 0.76rem; color: var(--muted); margin-top: 6px; }
  .fav { color: var(--green); font-weight: 700; }
  .unfav { color: var(--red); font-weight: 700; }
  .neutral { color: var(--amber); font-weight: 700; }
  section.cover {
    background: linear-gradient(135deg, #0a0e14 60%, #0f1e35 100%);
    display: flex; flex-direction: column; justify-content: center;
  }
  section.cover h1 { color: var(--white); border-color: var(--blue); font-size: 2.4rem; }
  section.cover .tagline { color: var(--blue); font-size: 1.1rem; margin-top: 10px; }
  section.cover .meta { color: var(--muted); font-size: 0.88rem; margin-top: 28px; line-height: 1.8; }
  section.harbor { background: var(--surface); }
  section.harbor h1 { font-size: 1.6rem; }
  section.harbor li { font-size: 0.95rem; }
  section.appendix { background: var(--surface); }
  section.appendix h1 { font-size: 1.5rem; }
  section.close {
    background: linear-gradient(135deg, #0a0e14 0%, #0f1e35 100%);
    display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
  }
  section.close h1 { color: var(--blue); border: none; font-size: 2.2rem; }
  section.close p { color: var(--muted); font-size: 0.95rem; line-height: 1.8; }
---

<!-- _class: cover -->

<div class="label">Q3 2026 Investor Presentation</div>

# Northwind Capital — Q3 2026 Results

NYSE: NWC &nbsp;|&nbsp; Market Cap ~$635M &nbsp;|&nbsp; 21.8M Shares Outstanding

<div class="tagline">Building the Premier Mid-Market Financial Services Platform</div>
<div class="meta">
  November 6, 2026 &nbsp;|&nbsp; Earnings Webcast — 8:00 AM ET<br>
  CEO: James Northwind &nbsp;|&nbsp; CFO: Sarah Kim &nbsp;|&nbsp; CRO: Marcus Chen
</div>

<!-- Presenter notes: Welcome to Northwind Capital's third quarter 2026 earnings presentation. This is our quarterly investor webcast covering results for the three and nine months ended September 30, 2026. The replay of this call and this presentation will be available on our investor relations website at ir.northwindcapital.com within two hours of the call's conclusion. We have approximately 45 minutes for prepared remarks followed by Q&A. Questions can be submitted through the webcast portal or via the toll-free dial-in number provided in the webcast instructions. Joining me today are CEO James Northwind and Chief Revenue Officer Marcus Chen. James will cover strategic context and the quarter highlights, I will walk through the financials in detail, Marcus will cover the segment business updates, and then we will open for Q&A. Before we begin, please note that this presentation contains forward-looking statements which are subject to risks and uncertainties. Please review the safe harbor on the following slide. The Form 10-Q will be filed with the SEC by November 14. -->

---

<!-- _class: harbor -->

# Safe Harbor — Forward-Looking Statements

<div class="label">Required Disclosure</div>

This presentation contains forward-looking statements as defined in the Private Securities Litigation Reform Act of 1995. These statements are based on management's current expectations and are subject to risks, uncertainties, and other factors that may cause actual results to differ materially from those described.

- Forward-looking statements include all guidance, projected financials, and strategic commentary
- Actual results may differ materially due to competitive dynamics, economic conditions, regulatory changes, deal timing, credit quality deterioration, and capital market conditions
- Northwind Capital undertakes no obligation to update forward-looking statements, except as required by law
- See "Risk Factors" in our most recent Form 10-K (filed February 14, 2026) for a complete description of risks

Non-GAAP measures presented include Adjusted EBITDA, Adjusted EPS, and Free Cash Flow. See appendix for reconciliation to GAAP.

<!-- Presenter notes: This safe harbor statement covers all forward-looking statements made in this presentation, including revenue guidance, EBITDA margin targets, headcount plans, capital allocation intentions, and strategic commentary. The safe harbor is required for Regulation FD compliance and to qualify for the PSLRA's litigation safe harbor. The risk factors most material to Northwind's business are disclosed in detail in our 10-K filed in February 2026. Key risks include: deal timing and M&A market conditions (primary driver of Capital Markets revenue variability), credit quality in our Lending portfolio, competitive pressures in mid-market advisory from larger banks and regional boutiques, interest rate sensitivity in our Lending NIM, and key person retention risk. Investors should not place undue reliance on any specific forward-looking statement. The non-GAAP reconciliation is in the appendix and is required by SEC Regulation G. We present adjusted metrics because we believe they better represent the operating performance of the business, but they are not GAAP and should not be used in isolation. -->

---

# Q3 2026 — Quarter at a Glance

<div class="label">Headline Results</div>

<div class="kpi-row">
  <div class="kpi"><div class="num">$52.1M</div><div class="lbl">Revenue (+9.9% YoY)</div></div>
  <div class="kpi"><div class="num">41.3%</div><div class="lbl">Gross Margin (+160 bps)</div></div>
  <div class="kpi"><div class="num">$8.4M</div><div class="lbl">Adj. EBITDA (16.1% margin)</div></div>
  <div class="kpi"><div class="num">$0.37</div><div class="lbl">Adj. EPS (+23% YoY)</div></div>
</div>

- Q3 revenue best quarter in company history; beat consensus $50.4M by $1.7M (3.4%)
- 12 Capital Markets deal closings — record quarter; Atlanta contributed 2 closings ($2.8M)
- Free cash flow $10.2M; net cash position $49.8M — first debt-free quarter since 2019

<!-- Presenter notes: Q3 2026 is a landmark quarter for Northwind Capital across every dimension. Let me highlight the three numbers that matter most to long-term investors. First, revenue of $52.1M at 9.9% YoY growth — this accelerates from 8.4% in Q2 and demonstrates that our growth is not decelerating. We are growing faster this year than last, which is unusual and reflects our strategic bets paying off: Atlanta geographic expansion, advisor productivity improvement, and the Capital Markets pipeline that is at record levels. Second, EBITDA margin of 16.1% is the highest in company history and is above our stated full-year guidance range of 14–15%. I will address whether we are raising the margin guidance in the guidance section. Third, net cash of $49.8M with zero debt is a milestone that demonstrates the cash generative nature of our capital-light advisory model. We are a company that converts earnings to cash efficiently — FCF conversion of 134% of net income YTD. The beat versus analyst consensus of $1.7M (3.4%) is our eighth consecutive quarterly beat, and I want to be straightforward: part of that pattern reflects our conservative guidance approach, which we are actively working to calibrate more accurately. Analysts should expect tighter guidance ranges going forward. -->

---

# Revenue Detail — Q3 2026

<div class="label">Revenue by Segment and Type</div>

| Segment | Q3 2026 | Q3 2025 | YoY | YTD 2026 | YTD 2025 |
|---|---|---|---|---|---|
| Capital Markets Advisory | $24.2M | $21.1M | +14.7% | $65.0M | $58.2M |
| Lending &amp; Credit | $16.1M | $15.6M | +3.2% | $46.1M | $44.5M |
| Wealth Management | $11.8M | $11.2M | +5.4% | $31.6M | $30.8M |
| **Total** | **$52.1M** | **$47.9M** | **+8.8%** | **$143.1M** | **$133.5M** |

- Recurring revenue: 38% of Q3 (Wealth Management fees + Lending NII) — expanding mix
- Atlanta: $2.8M Q3 contribution, ahead of $2.0M internal target; YTD $4.4M
- Wealth Management AUM: $2.1B; 12-month AUM growth 11.8%

<!-- Presenter notes: The revenue breakdown by segment shows strong performance in Capital Markets and solid contributions from Wealth Management and Lending. Capital Markets growth of 14.7% in Q3 is the fastest quarterly growth rate in two years and reflects both the record 12-mandate close quarter and the Atlanta office contribution. The two Atlanta closings in Q3 ($2.8M) exceeded our internal target and validate our investment thesis — we are 18 months into the Atlanta buildout and ahead of plan on both revenue and cost metrics. Lending growth of 3.2% reflects the mature nature of this segment and some NIM headwinds from the rate environment. We are not experiencing credit quality problems in the core portfolio — the two watch-list facilities I described in prior reporting have been remediated (one facility renewed with tightened covenants in September; one repaid in full in October). Wealth Management's steady 5.4% growth reflects the recurring nature of AUM-based fees. The 38% recurring revenue mix is important strategically: as this grows, our revenue visibility improves and our earnings quality increases. Our three-year target is to grow recurring revenue to 45% of total, primarily through Wealth Management AUM growth. -->

---

# Margin Analysis — Operating Leverage in Action

<div class="label">Cost Structure and Profitability</div>

| Metric | Q3 2026 | Q3 2025 | Q2 2026 | FY Guidance |
|---|---|---|---|---|
| Gross Margin | 41.3% | 39.7% | 40.5% | 40–41% |
| Comp / Revenue | 47.1% | 49.8% | 48.2% | ~48% |
| G&amp;A / Revenue | 8.4% | 10.3% | 9.1% | ~9% |
| Adj. EBITDA Margin | 16.1% | 13.8% | 14.4% | 14–15% |

- Q3 margin above guidance range due to revenue mix (Capital Markets 46.4% of Q3 vs. 42.3% in Q2)
- Comp ratio improvement: fewer analyst hires in Q3 vs. plan; defer to Q4/Q1 timing
- G&amp;A leverage sustained: office consolidation savings ($0.6M/year) now fully annualized

<!-- Presenter notes: The margin story in Q3 is notable and requires some explanation to prevent misinterpretation. EBITDA margin of 16.1% is above our guidance range of 14–15%, which raises the question of whether we are raising full-year guidance. The answer is nuanced: Q3 benefited from a favorable revenue mix, with Capital Markets representing 46.4% of Q3 revenue versus our typical 43–44% range. Capital Markets carries approximately 55% gross margins versus the blended 41%, so a higher Capital Markets mix mechanically lifts the overall margin. This is not a permanent structural shift — Q4 is expected to have a more balanced mix. Therefore, we are comfortable with the full-year guidance range of 14–15% but have tightened it to 14.5–15.5% to reflect the strong Q3 performance. The compensation ratio improvement in Q3 reflects timing: we planned to hire 4 analysts in Q3 but moved those offers to Q4 because the pipeline of candidates was better for fall recruiting. This is a timing difference, not a structural cost improvement. The G&A leverage is structural — the Chicago office savings are now fully reflected in the run rate, and we expect this to be sustained. -->

---

# Operations Update — Segment Performance

<div class="label">Operational Highlights by Division</div>

- **Capital Markets** — 12 closings; 18 active mandates entering Q4; Atlanta on track for $6M annual run-rate; 3 new senior advisor hires (2 New York, 1 Atlanta) start Q4
- **Lending &amp; Credit** — Portfolio $148M; NIM 3.45% (+4 bps QoQ); watch-list cleared; new pipeline $24M in underwriting
- **Wealth Management** — AUM $2.1B; 47 net new households Q3; NPS 67 (record); implementing digital portal for client self-service Q4 2026

<!-- Presenter notes: The operational highlights provide business context behind the financial results. In Capital Markets, the 18 active mandates entering Q4 is our highest ever and provides strong visibility into Q4 and Q1 2027 revenue. The important caveat is that deal timing is always uncertain in the final weeks of a quarter — we typically see 15–20% of expected Q4 closings push into Q1. Our Q4 guidance accounts for this. The three new senior advisor hires starting Q4 represent our Q1 2027 revenue investment — they will not contribute meaningful revenue in 2026, but by Q2 2027 we expect them to be generating business. In Lending, the watch-list clearance is a significant positive development. Both facilities that were on watch — the Drew & Associates revolving facility ($12M) and the Apex Manufacturing term loan ($6.4M) — have been resolved: Drew renewed with tightened covenants, Apex repaid in full. Our current portfolio is clean with no facilities in default or on watch. In Wealth Management, the record NPS of 67 is a leading indicator of referral-driven growth. We track NPS closely because 38% of our new Wealth Management households come from existing client referrals. A rising NPS predicts rising net new households 2–3 quarters forward. The digital portal launch in Q4 is a service investment, not a revenue investment, but it will reduce advisor administrative time by approximately 20 minutes per client per quarter. -->

---

# Cash Flow and Balance Sheet

<div class="label">Capital Position — September 30, 2026</div>

| Item | Sept 30, 2026 | Jun 30, 2026 | Dec 31, 2025 |
|---|---|---|---|
| Cash &amp; Equivalents | $44.8M | $38.4M | $31.2M |
| Short-Term Investments | $5.0M | — | — |
| Total Debt | $0 | $4.0M | $9.0M |
| Net Cash | $49.8M | $34.4M | $22.2M |
| Book Value / Share | $15.68 | $14.82 | $13.97 |

- YTD free cash flow: $22.1M (19.6M target; beat driven by working capital efficiency)
- Dividend declared: $0.08/share Q3 (payable December 15); 8th consecutive quarterly dividend
- Q3 buyback: $2.1M at average $28.90 (73K shares); $6.1M authorization remaining

<!-- Presenter notes: The balance sheet transformation in 2026 has been remarkable. We started the year with $22.2M in net debt (debt minus cash) and ended Q3 with $49.8M in net cash — a swing of $72M in just three quarters. This reflects three things: strong operating earnings, disciplined working capital management (particularly advisory fee collections), and the early repayment of our revolving credit facility. Book value per share of $15.68 has grown $1.71 per share in 2026, driven by retained earnings and the buyback. On the buyback: we deployed $2.1M in Q3 at an average price of $28.90. We believe this represents value at approximately 0.9x trailing book value and 9.8x trailing EBITDA — below what we consider intrinsic value of $33–36 per share. We will continue executing the buyback systematically within our policy parameters. The dividend of $0.08 per share is maintained, representing an 1.1% annual yield at current prices. Capital allocation policy remains: first, maintain operating liquidity floor; second, invest organically for growth; third, systematic buyback; fourth, strategic acquisitions subject to board approval. We are not considering special dividends at this time. -->

---

# Guidance — Q4 2026 and Full Year Update

<div class="label">Financial Outlook</div>

| Metric | Prior FY Guidance | Updated FY Guidance | Q4 2026 Estimate |
|---|---|---|---|
| Total Revenue | $185M–$189M | $188M–$192M | $45M–$49M |
| Gross Margin | 40%–41% | 40.5%–41.5% | 40%–41% |
| Adj. EBITDA Margin | 14%–15% | 14.5%–15.5% | 13%–15% |
| Adjusted EPS | $1.22–$1.32 | $1.32–$1.42 | $0.25–$0.35 |

- Full-year revenue guidance raised $3M at midpoint; third raise in 2026
- EPS raise reflects EBITDA expansion and 73K shares removed via buyback
- Q4 guidance reflects 2 mandates at risk of slipping to Q1; range captures both outcomes

<!-- Presenter notes: We are raising full-year guidance for the third time in 2026, reflecting our strong Q3 performance and visibility into Q4. This is the most aggressive guidance raise of the year: we are taking the midpoint up by $3M (versus $1.5M in the Q1 raise and $2M in the Q2 raise). The rationale: YTD revenue of $143.1M puts us well on pace, Q3 EBITDA margins above guidance give us operating leverage confidence, and the Q4 pipeline is the strongest we have had entering any Q4 in company history. The Q4 guidance range of $45–49M is wider than typical because of the two mandates at risk of slipping to Q1. These two transactions represent $3.2M of Q4 fee expectations. If both close in Q4, we are at the high end of range and could even exceed $190M for the full year. If both slip, we are at the low end. The EBITDA margin guidance of 14.5–15.5% for the full year reflects a Q4 expectation of 13–15% (lower than Q3's 16.1% due to mix normalization and Q4 incentive compensation true-ups). Investors should note that full-year 2026 results will be reported on Q4 earnings in February 2027; we will provide FY 2027 initial guidance at that time. -->

---

# Strategic Priorities — Building for 2027 and Beyond

<div class="label">Long-Term Value Drivers</div>

- **Platform scale** — $200M revenue plan for 2027 (board-approved AOP); 6.8% growth; first company milestone
- **Geographic expansion** — Atlanta fully operational; no additional markets planned for 2027; deepen before expanding
- **Private credit fund** — $150M target raise; Q1 2027 launch; fee income begins Q2 2027; extends Capital Markets client value chain
- **Technology** — Salesforce FSC go-live January 2027; advisor productivity gain, revenue leakage prevention, real-time management reporting

<!-- Presenter notes: The four strategic priorities for the coming year provide investors with the framework for evaluating management's execution. On platform scale: the $200M revenue plan for 2027 is ambitious but achievable based on our pipeline and operating momentum. We will provide 2027 initial guidance on the Q4 2026 earnings call in February. On geographic expansion: after Atlanta, we are committed to deepening our presence in the Southeast rather than opening additional markets. We want Atlanta to be fully self-sustaining on a 12-month basis before considering the next geography — our current model suggests that will happen by Q3 2027. On private credit: this is the most significant strategic development we will announce today. We have decided to launch a private credit fund targeting $150M in capital commitments, aimed at mid-market borrowers who are Northwind advisory clients or prospects. This extends our value proposition to clients beyond M&A advisory into capital formation. The fee income model is management fees of 1.5% on committed capital beginning at close, plus performance fees of 15% above an 8% hurdle. If we raise $150M, management fees alone are $2.25M annually — a new high-margin recurring revenue stream. We have engaged placement agents and expect to announce the first close by Q2 2027. On technology: the Salesforce go-live in January is on track; I covered this in detail in prior communications. -->

---

# Q&amp;A Anchor — Anticipated Topics

<div class="label">Analyst Questions — Prepared Context</div>

| Likely Topic | Management Position |
|---|---|
| Q3 margin sustainability | Q3 margin elevated by mix; full-year target 14.5–15.5%; structural improvement but not 16% run rate |
| Atlanta run-rate | On track for $6M annual; Q4 expected $1.8M; 2027 target $8M as team fully productive |
| Private credit fund timeline | Q1 2027 close; $150M target; $75M minimum viable; LP conversations underway |
| Capital allocation — $49.8M cash | Maintain $15M floor; continue $6.1M buyback; reserve $20M for M&A; remainder available |
| 2027 guidance preview | Not providing at this call; February 12 Q4 call; AOP range $188–192M reflective of current visibility |

Questions: press *1 or submit via webcast portal.

<!-- Presenter notes: This slide provides management alignment on the likely analyst topics before we open Q&A. On margin: analysts will ask whether 16.1% is the new baseline. It is not — we have been clear about the mix effect. However, we are trending toward the high end of our 14–15% target range, and the private credit fund (once operational) will be accretive to margins given its high-margin fee structure. On Atlanta: analysts will probe the ramp trajectory. Be specific: Q3 was $2.8M, Q4 expected $1.8M (slightly lower due to two deal timing items), FY 2026 total $6.0M, FY 2027 target $8M. On private credit: this is new information. Analysts will want the fee structure, LP pipeline, minimum viable size, and risk factors. Have the investment memo available for follow-up one-on-one discussions. On capital allocation: the $49.8M cash balance will generate questions about special dividends or large acquisitions. Be consistent with the framework: no special dividends, strategic acquisitions subject to board approval, continue the systematic buyback. On 2027 guidance: do not provide it on this call. The AOP is approved but not yet public. February 12 is the right venue for 2027 guidance with the full year closed. If pressed, confirm the AOP exists and will be shared at the Q4 call. Do not disclose $200M. -->

---

<!-- _class: appendix -->

# Appendix — Non-GAAP Reconciliation

<div class="label">GAAP to Adjusted EBITDA Bridge</div>

| Item | Q3 2026 | Q3 2025 | YTD 2026 | YTD 2025 |
|---|---|---|---|---|
| GAAP Net Income | $5.4M | $3.8M | $13.2M | $10.3M |
| Add: D&amp;A | $1.2M | $1.1M | $3.6M | $3.3M |
| Add: Stock-Based Comp | $0.8M | $0.6M | $2.2M | $1.8M |
| Add: Restructuring | $0 | $0 | $0.7M | $0 |
| Add: Other non-recurring | $1.0M | $0.4M | $2.4M | $0.8M |
| **Adjusted EBITDA** | **$8.4M** | **$5.9M** | **$22.1M** | **$16.2M** |

Adjusted EPS: Q3 $0.37 | YTD $1.07 | GAAP EPS: Q3 $0.24 | YTD $0.60 | Diluted shares: 21.8M

<!-- Presenter notes: The non-GAAP reconciliation is provided pursuant to SEC Regulation G and our earnings release. Adjusted EBITDA is not a GAAP measure and should be considered only in conjunction with GAAP net income. The reconciliation shows that the primary adjustments are stock-based compensation ($0.8M in Q3) and depreciation ($1.2M). The "other non-recurring" line of $1.0M in Q3 includes $0.7M in deal-related expenses for the private credit fund launch (legal, placement agent retainer, regulatory filings) which are non-recurring in nature and $0.3M in severance related to the office consolidation. We have chosen to exclude these from adjusted EBITDA because they do not reflect recurring operating performance. Analysts may disagree with this classification — we are happy to discuss the rationale in one-on-ones. The GAAP EPS of $0.24 versus adjusted EPS of $0.37 — the $0.13 difference represents $0.03 D&A per share, $0.04 SBC per share, and $0.06 other per share (all tax-effected at 28.4%). Free cash flow of $10.2M in Q3 is calculated as operating cash flow of $11.6M less capital expenditures of $1.4M. Full quarterly financial statements will be available in the Form 10-Q filed November 14, 2026. -->

---

<!-- _class: close -->

# Q&amp;A — We Welcome Your Questions

**Northwind Capital — NYSE: NWC**

IR Contact: Sarah Chen, VP Investor Relations
ir@northwindcapital.com &nbsp;|&nbsp; +1 (212) 555-0180

Next Event: Q4 2026 Earnings — February 12, 2027 (8:00 AM ET)
Conference: Jefferies Financial Services — September 2027 &amp; Morgan Stanley Financial Partners — January 2027

Replay available within 2 hours at ir.northwindcapital.com

<!-- Presenter notes: This closes the prepared remarks. We are now opening the Q&A. Operator, please provide dial-in instructions. As a reminder, we request one question and one follow-up per analyst to allow broader participation. Additional questions can be submitted in writing to IR after the call. For investors and analysts interested in one-on-one meetings: the CFO and IR team will be conducting meetings at the Morgan Stanley Financial Partners conference in January 2027. Meeting requests should be directed to Sarah Chen in Investor Relations. We are also available for individual calls between now and the Q4 earnings call; please contact IR to schedule. The webcast replay will be available within two hours. The 10-Q will be filed by November 14. Thank you for your continued interest in Northwind Capital. We believe we are executing well and are excited about the opportunities ahead. Operator, please open the Q&A queue. -->
