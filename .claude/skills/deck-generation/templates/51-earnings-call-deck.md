<!-- TEMPLATE: earnings-call-deck
     CATEGORY: Finance
     USE WHEN: presenting quarterly earnings to analysts/public
     SLIDE COUNT: 11
     PALETTE: Executive cream
     RENDER: marp --pptx 51-earnings-call-deck.md -->

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
  }
  section {
    background: var(--cream);
    color: var(--navy);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 52px 64px;
  }
  h1 {
    font-size: 2.0rem;
    font-weight: 700;
    color: var(--navy);
    letter-spacing: -0.4px;
    border-bottom: 3px solid var(--gold);
    padding-bottom: 10px;
    margin-bottom: 24px;
  }
  h2 {
    font-size: 1.4rem;
    font-weight: 600;
    color: var(--gold);
    letter-spacing: -0.2px;
    margin-bottom: 16px;
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
    background: var(--navy);
    color: var(--cream);
    padding: 8px 12px;
    text-align: left;
  }
  td {
    padding: 7px 12px;
    border-bottom: 1px solid var(--rule);
  }
  tr:nth-child(even) td { background: #ede9e0; }
  .label {
    display: inline-block;
    background: var(--gold);
    color: var(--cream);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 3px;
    margin-bottom: 12px;
  }
  .kpi-row {
    display: flex;
    gap: 32px;
    margin-top: 20px;
  }
  .kpi {
    flex: 1;
    background: var(--navy);
    color: var(--cream);
    border-radius: 8px;
    padding: 20px 24px;
    text-align: center;
  }
  .kpi .num { font-size: 2.0rem; font-weight: 700; color: var(--gold); }
  .kpi .lbl { font-size: 0.80rem; color: #a0b0c0; margin-top: 4px; }
  section.cover {
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: var(--navy);
    color: var(--cream);
  }
  section.cover h1 {
    color: var(--cream);
    border-bottom-color: var(--gold);
    font-size: 2.4rem;
  }
  section.cover .sub { color: var(--gold); font-size: 1.1rem; margin-top: 8px; }
  section.cover .meta { color: #8899ac; font-size: 0.88rem; margin-top: 24px; }
  section.close {
    background: var(--navy);
    color: var(--cream);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.close h1 { color: var(--gold); border: none; font-size: 2.2rem; }
  section.close p { color: #a0b0c0; font-size: 1.05rem; }
---

<!-- _class: cover -->

<div class="label">Q2 2026 Earnings Call</div>

# Northwind Capital — Second Quarter 2026 Results

<div class="sub">Investor Conference Call &amp; Webcast</div>
<div class="meta">August 7, 2026 &nbsp;|&nbsp; 8:00 AM ET &nbsp;|&nbsp; NYSE: NWC</div>

<!-- Presenter notes: Welcome analysts and investors to Northwind Capital's Q2 2026 earnings call. This presentation covers results for the quarter ended June 30, 2026. The call is being webcast live and a replay will be available on our investor relations site at ir.northwindcapital.com within two hours of the call's conclusion. Participants may submit questions through the webcast portal or via the dial-in queue. We have approximately 45 minutes for prepared remarks and Q&A. Management present today includes our CEO, CFO, and Chief Revenue Officer. All figures are unaudited. Forward-looking guidance is subject to risks described on the following slide. Before we begin, I will turn the call over to our CFO for the safe harbor statement. -->

---

# Safe Harbor Statement

<div class="label">Forward-Looking Statements</div>

This presentation contains forward-looking statements within the meaning of the Private Securities Litigation Reform Act of 1995. These statements involve known and unknown risks, uncertainties, and other factors that may cause actual results to differ materially from those expressed or implied.

- Statements regarding future revenue, margins, and guidance are estimates only
- Past performance is not indicative of future results
- Northwind Capital undertakes no obligation to update forward-looking statements
- Full risk factors are disclosed in our most recent Form 10-K and 10-Q filings with the SEC

<!-- Presenter notes: This safe harbor statement must be read into the record or acknowledged before any forward-looking statements are made. Key risk factors for Northwind Capital include macroeconomic conditions affecting our advisory and lending businesses, credit quality deterioration, interest rate sensitivity, regulatory changes in financial services, and competitive pressures in our core markets. Investors are encouraged to read our SEC filings in full, particularly the Risk Factors and MD&A sections of our most recent 10-K. Nothing in this call constitutes an offer to sell or solicitation of any securities. Any projections or estimates are based on assumptions management believes reasonable but which may prove incorrect. The Q2 report will be filed on Form 10-Q within 40 days of quarter-end per SEC requirements. -->

---

# Q2 2026 — Headline Results

<div class="label">Quarter Summary</div>

<div class="kpi-row">
  <div class="kpi"><div class="num">$47.2M</div><div class="lbl">Revenue (+8.4% YoY)</div></div>
  <div class="kpi"><div class="num">$19.1M</div><div class="lbl">Gross Profit (40.5% Margin)</div></div>
  <div class="kpi"><div class="num">$6.8M</div><div class="lbl">Adjusted EBITDA</div></div>
  <div class="kpi"><div class="num">$0.31</div><div class="lbl">Adjusted EPS</div></div>
</div>

- Revenue of $47.2M exceeded consensus estimate of $45.8M by $1.4M (3.1%)
- Gross margin of 40.5% expanded 80 bps year-over-year; operating leverage improving
- Net income of $4.2M; GAAP EPS $0.19 includes $2.6M in non-recurring restructuring charges

<!-- Presenter notes: Q2 2026 marks our seventh consecutive quarter of revenue growth above 7%. The beat versus consensus was driven primarily by stronger-than-expected advisory fee revenues in our Capital Markets segment ($2.1M above internal plan) and disciplined cost management in G&A, which came in $0.4M under budget. The non-recurring restructuring charges relate to our office consolidation in Chicago completed in June; there are no further charges expected in the back half. Gross margin expansion reflects our continued shift toward higher-margin recurring revenue streams — subscription advisory fees now represent 34% of total revenue versus 28% in Q2 2025. Adjusted EBITDA of $6.8M represents a 14.4% margin, up from 12.9% in Q2 2025. We define adjusted EBITDA excluding stock-based compensation, depreciation, and the restructuring charge. A full reconciliation table is in the appendix. -->

---

# Segment Revenue — Q2 2026

<div class="label">Revenue by Business Line</div>

| Segment | Q2 2026 | Q2 2025 | Change | YTD 2026 | YTD 2025 |
|---|---|---|---|---|---|
| Capital Markets Advisory | $21.4M | $19.3M | +10.9% | $40.8M | $37.1M |
| Lending &amp; Credit Solutions | $15.6M | $14.8M | +5.4% | $30.4M | $28.9M |
| Wealth Management | $10.2M | $9.4M | +8.5% | $19.8M | $18.2M |
| **Total** | **$47.2M** | **$43.5M** | **+8.4%** | **$91.0M** | **$84.2M** |

- Capital Markets growth driven by M&amp;A advisory completions (+3 deals vs Q2 2025)
- Lending segment benefiting from higher net interest margin (NIM +22 bps to 3.41%)
- Wealth Management AUM grew to $2.1B, up 11% year-over-year

<!-- Presenter notes: All three segments delivered positive revenue growth in Q2. Capital Markets is our largest segment and continues to benefit from robust M&A activity in the mid-market, which is Northwind's primary focus. We closed nine advisory mandates in the quarter, compared to six in Q2 2025. Pipeline entering Q3 is 18 active mandates at various stages — our highest ever — though deal timing is always uncertain. Lending saw NIM expansion despite the flat rate environment as we repriced certain legacy floating-rate loans and reduced higher-cost deposits. Our Wealth Management business added 47 net new client relationships in Q2, bringing total client households to 1,820. Average AUM per household increased to $1.15M, up from $1.04M in Q2 2025, reflecting both market appreciation and wallet-share deepening. We do not break out revenue by client beyond these three segments at this time. -->

---

# Margins and Operating Leverage

<div class="label">Profitability Metrics</div>

| Metric | Q2 2026 | Q2 2025 | Q1 2026 | FY 2026 Guide |
|---|---|---|---|---|
| Gross Margin | 40.5% | 39.7% | 39.8% | 40–41% |
| Adjusted EBITDA Margin | 14.4% | 12.9% | 13.1% | 14–15% |
| Comp &amp; Benefits / Revenue | 48.2% | 49.8% | 49.1% | ~48% |
| G&amp;A / Revenue | 9.1% | 10.3% | 9.6% | ~9% |

- Compensation efficiency improving as revenue mix shifts toward recurring fees
- G&amp;A reduction reflects office consolidation savings ($0.6M annual run rate) effective Q3
- D&amp;A of $1.2M; no material change expected

<!-- Presenter notes: Margin improvement is the clearest evidence of operating leverage in our model. We have been transparent over the past three quarters that our target is to reach a 15% adjusted EBITDA margin on a sustainable basis by year-end 2026, and Q2 results give us confidence we are on track. The key driver is mix shift: our Capital Markets advisory fees carry approximately 55% gross margins versus 28% for our Lending segment. As advisory grows as a percentage of total revenue, blended margins expand without any cost cutting. On the cost side, compensation as a percentage of revenue is declining as we scaled headcount more slowly than revenue this year — we added 12 net new employees in the first half versus 22 in the same period last year, primarily by increasing productivity of existing staff through technology investments. G&A savings from the Chicago consolidation will be fully reflected in Q3 and beyond. We remain comfortable with our full-year guidance range of 14–15% adjusted EBITDA margin. -->

---

# Cash Flow and Balance Sheet

<div class="label">Liquidity and Capital Position</div>

| Item | June 30, 2026 | Dec 31, 2025 | Change |
|---|---|---|---|
| Cash &amp; Equivalents | $38.4M | $31.2M | +$7.2M |
| Total Debt | $52.0M | $57.0M | -$5.0M |
| Net Debt | $13.6M | $25.8M | -$12.2M |
| Book Value Per Share | $14.82 | $13.97 | +$0.85 |

- Free cash flow of $9.1M in Q2; operating cash conversion ratio 134% of net income
- Repaid $5M on revolving credit facility; $48M of capacity available
- Quarterly dividend of $0.08 per share declared, payable September 15, 2026

<!-- Presenter notes: Balance sheet strength is a core strategic priority for Northwind Capital. We ended Q2 with $38.4M in cash — our highest quarter-end balance since inception. The strong free cash flow reflects our capital-light advisory model, which requires minimal working capital and generates cash quickly upon deal close. We define free cash flow as operating cash flow less capital expenditures of $1.4M in Q2. Our debt consists entirely of a senior secured revolving credit facility at SOFR plus 185 basis points, maturing in November 2028. Net debt to adjusted EBITDA is now 0.5x on a trailing twelve-month basis, well within our target range of 0–1x. The board declared our eighth consecutive quarterly dividend; yield at current share price is approximately 1.1%. We also repurchased 85,000 shares in Q2 at an average price of $27.40, leaving $8.2M of capacity remaining under the current buyback authorization. No changes to capital allocation policy. -->

---

# Full-Year 2026 Guidance

<div class="label">Financial Outlook</div>

| Metric | Prior Guidance | Updated Guidance | Change |
|---|---|---|---|
| Total Revenue | $183M–$187M | $185M–$189M | +$2M midpoint |
| Gross Margin | 39.5%–40.5% | 40%–41% | +50 bps floor |
| Adjusted EBITDA | $26M–$28M | $27M–$29M | +$1M midpoint |
| Adjusted EPS | $1.18–$1.28 | $1.22–$1.32 | +$0.04 midpoint |

- Revenue guidance raised at midpoint reflecting strong H1 performance and robust pipeline
- Margin guidance tightened higher on mix shift and confirmed G&amp;A savings
- H2 seasonality expected: Q3 historically strongest, Q4 softer on deal timing

<!-- Presenter notes: We are raising full-year guidance across all metrics after a strong first half. Revenue of $91.0M in H1 puts us well on track for the updated $185–189M full-year range. The raise reflects our H1 beat plus continued confidence in our Capital Markets pipeline, which has 18 active mandates. I want to be clear about the risks to guidance: deal timing is the primary variable. Advisory fees are recognized upon transaction close, and deals can slip by a quarter. If our pipeline closes as expected, we will be at or above the high end; if any material transactions slip to Q1 2027, we may be at the low end. We do not guide to specific deal counts. Macro risks include a deterioration in M&A market conditions, though we have seen no evidence of this. Interest rate changes would modestly affect our Lending NIM but are not material to overall guidance. We expect to update guidance again with Q3 results in November. -->

---

# Strategic Updates

<div class="label">Growth Initiatives</div>

- **Technology Investment** — CRM and deal management platform upgrade on track for Q4 launch; improves advisor productivity and pipeline visibility
- **Geographic Expansion** — Atlanta office opened June 2026; 4 senior advisors hired; first mandates expected Q3
- **Product Extension** — Private credit fund launch targeted for Q1 2027; $150M target raise; fills gap between lending balance sheet and capital markets advisory

<!-- Presenter notes: Three strategic initiatives are worth highlighting. First, our technology modernization: we have invested $2.8M in a new Salesforce-based CRM and deal management platform that will go live in Q4. This will replace two legacy systems and give management real-time visibility into pipeline health and advisor activity. We expect a 15% improvement in advisor productivity based on benchmarking against peers who have completed similar implementations. Second, our Atlanta office targets the Southeast M&A market, where we have historically been underrepresented. The four senior advisors we hired have an average of 17 years of experience and bring established client relationships. We expect them to be revenue-generating by Q4. Third, our private credit fund is a strategic initiative to capture the growing demand from middle-market borrowers for non-bank lending. This complements our existing lending business and advisory practice. We are in preliminary discussions with institutional LPs. More details will be provided when appropriate. -->

---

# Q&amp;A — Prepared Topics

<div class="label">Analyst Guidance</div>

We invite questions on the following topics from analyst coverage:

- H2 pipeline composition and deal timing assumptions
- Private credit fund structure and target LP composition
- Capital allocation — buyback pace vs. organic investment
- Margin trajectory and compensation leverage as revenue scales

**To ask a question:** Press *1 on your phone keypad, or submit via the webcast portal. Please limit initial questions to one plus one follow-up.

<!-- Presenter notes: As we open the Q&A, the IR team has flagged the following likely topics from analyst coverage: Morgan Stanley has previewed questions on the private credit fund timeline and fee structure. Goldman Sachs has signaled interest in the Atlanta office ramp trajectory and cost basis. Wells Fargo is likely to probe the sustainability of gross margin expansion. Jefferies may ask about the share buyback pace given rising cash balance. Management should be prepared to discuss these openly but avoid providing forward guidance beyond what is in the deck. If asked about deal-specific pipeline items, maintain standard policy of not discussing confidential mandates. The CFO will field all financial questions; the CEO will take strategic and market questions. IR will manage the queue. Estimated Q&A duration: 20–25 minutes. -->

---

# Appendix — Reconciliation Tables

<div class="label">Non-GAAP to GAAP Bridge</div>

| Item | Q2 2026 | Q2 2025 | YTD 2026 | YTD 2025 |
|---|---|---|---|---|
| GAAP Net Income | $4.2M | $3.4M | $7.8M | $6.5M |
| Add: D&amp;A | $1.2M | $1.1M | $2.4M | $2.2M |
| Add: Stock-Based Comp | $0.7M | $0.6M | $1.4M | $1.2M |
| Add: Restructuring Charges | $0.7M | — | $0.7M | — |
| **Adjusted EBITDA** | **$6.8M** | **$5.1M** | **$12.3M** | **$9.9M** |

GAAP EPS $0.19 | Adjusted EPS $0.31 | Shares outstanding: 21.8M diluted

<!-- Presenter notes: The appendix contains our standard non-GAAP reconciliation required for Regulation G compliance. Adjusted EBITDA is not a GAAP measure and should not be considered in isolation. We present it because we believe it better reflects the operating performance of our business by excluding non-cash and non-recurring items. Stock-based compensation is primarily performance-vested RSUs granted to senior advisors and management; expense was $0.7M in Q2, which we expect to remain approximately flat for the remainder of the year. The restructuring charge of $0.7M is the final tranche related to the Chicago office closure — lease termination costs and leasehold improvement write-offs. There are no expected future restructuring charges under the current plan. The full 10-Q with GAAP financial statements will be filed with the SEC by August 14, 2026 and will be available on EDGAR and our investor relations website. -->

---

<!-- _class: close -->

# Thank You — Questions?

**Investor Relations Contact**

Sarah Chen, VP Investor Relations
ir@northwindcapital.com &nbsp;|&nbsp; +1 (212) 555-0180
ir.northwindcapital.com

Next reporting event: Q3 2026 Earnings — November 6, 2026

<!-- Presenter notes: This closes the prepared remarks portion of the call. We will now open the line for Q&A. Operator, please provide instructions to callers. As a reminder, this call is being recorded and a replay will be available on our IR website within two hours. For questions not addressed today, please reach out to Sarah Chen in Investor Relations. We look forward to speaking with many of you at the upcoming Jefferies Financial Services Conference in September. Thank you for your continued interest in Northwind Capital. We are proud of the progress we have made and remain confident in our ability to deliver sustainable value to shareholders. Operator, please begin the Q&A queue. -->
