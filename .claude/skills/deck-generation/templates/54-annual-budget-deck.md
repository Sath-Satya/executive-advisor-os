<!-- TEMPLATE: annual-budget-deck
     CATEGORY: Finance
     USE WHEN: annual budget presentation to board or executive committee
     SLIDE COUNT: 12
     PALETTE: Executive cream
     RENDER: marp --pptx 54-annual-budget-deck.md -->

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
    font-size: 1.85rem; font-weight: 700; color: var(--navy);
    letter-spacing: -0.3px; border-bottom: 3px solid var(--gold);
    padding-bottom: 8px; margin-bottom: 20px;
  }
  h2 { font-size: 1.2rem; font-weight: 600; color: var(--gold); margin-bottom: 12px; }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 9px; font-size: 0.98rem; line-height: 1.5; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88rem; margin-top: 10px; }
  th { background: var(--navy); color: var(--cream); padding: 7px 10px; text-align: left; }
  td { padding: 6px 10px; border-bottom: 1px solid var(--rule); }
  tr:nth-child(even) td { background: #ede9e0; }
  .label {
    display: inline-block; background: var(--gold); color: var(--cream);
    font-size: 0.68rem; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; padding: 2px 9px; border-radius: 3px; margin-bottom: 10px;
  }
  .kpi-row { display: flex; gap: 20px; margin-top: 16px; }
  .kpi {
    flex: 1; background: var(--navy); color: var(--cream);
    border-radius: 8px; padding: 16px 18px; text-align: center;
  }
  .kpi .num { font-size: 1.6rem; font-weight: 700; color: var(--gold); }
  .kpi .lbl { font-size: 0.74rem; color: #a0b0c0; margin-top: 4px; }
  .fav { color: var(--green); font-weight: 700; }
  .unfav { color: var(--red); font-weight: 700; }
  section.cover { background: var(--navy); color: var(--cream); display: flex; flex-direction: column; justify-content: center; }
  section.cover h1 { color: var(--cream); border-color: var(--gold); font-size: 2.2rem; }
  section.cover .sub { color: var(--gold); font-size: 1.0rem; margin-top: 8px; }
  section.cover .meta { color: #8899ac; font-size: 0.85rem; margin-top: 20px; }
  section.ask { background: #1a2a3a; color: var(--cream); display: flex; flex-direction: column; justify-content: center; }
  section.ask h1 { color: var(--gold); border: none; font-size: 1.9rem; }
  section.ask ul li { color: #c0cfd8; margin-bottom: 14px; font-size: 1.05rem; }
---

<!-- _class: cover -->

<div class="label">Annual Operating Plan — Board Presentation</div>

# Northwind Capital — FY 2027 Annual Budget

<div class="sub">Fiscal Year January 1 – December 31, 2027</div>
<div class="meta">October 21, 2026 &nbsp;|&nbsp; Board of Directors Finance Committee &nbsp;|&nbsp; Confidential</div>

<!-- Presenter notes: Good morning. This presentation covers Northwind Capital's proposed Annual Operating Plan for FY 2027, submitted to the board finance committee for review and approval at today's meeting. The deck follows our standard format: prior year review, then each P&L line plan with supporting assumptions, capital requirements, headcount, investment priorities, sensitivity analysis, quarterly phasing, risks, and the specific board asks. The FY 2027 AOP was developed through a 10-week bottoms-up planning process involving all three business segments and the Finance, IT, and HR functions. Segment plans were reviewed by the CFO in September and consolidated by the Finance team. We will cover all 12 sections; I ask that you hold detailed questions until the end of each section. The board vote on the AOP is scheduled for the end of today's session. Total presentation time is approximately 75 minutes including Q&A. -->

---

# FY 2026 Prior Year Review — How We Performed

<div class="label">2026 Actuals vs. AOP</div>

| Metric | FY 2026 AOP | FY 2026 Actual | Variance |
|---|---|---|---|
| Total Revenue | $185.0M | $187.2M | <span class="fav">+$2.2M (+1.2%)</span> |
| Gross Margin | 40.0% | 40.6% | <span class="fav">+60 bps</span> |
| Adjusted EBITDA | $26.9M | $27.8M | <span class="fav">+$0.9M (+3.3%)</span> |
| Free Cash Flow | $18.0M | $19.6M | <span class="fav">+$1.6M</span> |
| Headcount (EoY) | 148 | 144 | <span class="fav">-4 (lower spend)</span> |

FY 2026 is the third consecutive year of revenue beat vs. AOP. Capital Markets drove outperformance; Lending in line; Wealth Management slightly below on AUM.

<!-- Presenter notes: FY 2026 closed strongly — full-year revenue of $187.2M exceeded our AOP by $2.2M, and all financial metrics came in at or above plan. This is the third consecutive year we have beat the AOP, which the board should view positively but also as a calibration signal: our planning process has been consistently conservative. For FY 2027, we have attempted to calibrate our assumptions more tightly using a structured scenario analysis that I will cover on slide 8. The gross margin outperformance of 60 bps reflects the favorable revenue mix shift toward Capital Markets advisory (which carries ~55% gross margins) and the G&A savings from the Chicago office consolidation. Free cash flow of $19.6M is a record and positions us well entering 2027 with $38.4M in cash and minimal debt. The headcount underage of 4 versus plan reflects our decision to be more selective in H2 hiring given strong productivity gains from technology investments. The four open positions have been deferred to Q1 2027 and are reflected in the FY 2027 headcount plan. -->

---

# FY 2027 Revenue Plan

<div class="label">Revenue by Segment</div>

| Segment | FY 2026 Actual | FY 2027 Budget | Growth | Assumptions |
|---|---|---|---|---|
| Capital Markets | $82.4M | $89.4M | +8.5% | 34 mandates (+4 vs 2026); Atlanta contributes $6M |
| Lending &amp; Credit | $62.0M | $65.5M | +5.6% | NIM +10 bps; $30M new facilities |
| Wealth Management | $42.8M | $45.1M | +5.4% | AUM +8% to $2.3B; 80 new households |
| **Total** | **$187.2M** | **$200.0M** | **+6.8%** | |

**$200M revenue plan — first time crossing the milestone.** Requires consistent execution across all three segments.

<!-- Presenter notes: The FY 2027 revenue plan of $200.0M represents our first-ever $200M budget, and the team is appropriately excited about the milestone. However, I want to be direct about what needs to go right to achieve it. Capital Markets growth of 8.5% requires 34 closed mandates, which is 4 more than our 2026 actuals of 30. Our Atlanta office, now in its second year, is budgeted to contribute $6M — this is a significant step up from the $1.5M H2 run-rate in 2026 and requires the team to ramp as expected. The 34 mandate assumption reflects a 15% growth in pipeline from our current 18 active mandates, which we believe is achievable given the mid-market M&A environment and our expanded geographic presence. Lending growth is more conservative at 5.6%, reflecting the mature nature of this segment and uncertainty around rate environment. We have modeled NIM improvement of 10 bps based on the current forward curve, but this is rate-environment dependent. Wealth Management growth of 5.4% is entirely organic — we are not assuming any acquisition or strategic partnership. The AUM growth to $2.3B reflects 5% market appreciation and 3% net new inflows from new client relationships. -->

---

# FY 2027 Operating Expense Plan

<div class="label">OpEx Budget</div>

| Category | FY 2026 Actual | FY 2027 Budget | Change | Notes |
|---|---|---|---|---|
| Compensation &amp; Benefits | $90.6M | $96.8M | +6.9% | 8 net new hires; merit 3.5% |
| Technology &amp; Systems | $8.4M | $12.2M | +45.2% | Salesforce FSC ($1.8M); data infra ($2.0M) |
| Occupancy | $6.8M | $7.2M | +5.9% | Atlanta full-year; NYC rent step-up |
| Professional Services | $4.2M | $4.5M | +7.1% | Legal, audit, compliance |
| Marketing &amp; BD | $3.8M | $4.2M | +10.5% | Brand investment; conference presence |
| G&amp;A | $5.1M | $5.1M | flat | Tight cost control maintained |
| **Total OpEx** | **$118.9M** | **$130.0M** | **+9.3%** | |

Gross Profit: $70.0M (35.0% margin); **Adjusted EBITDA: $30.5M (15.3% margin)**

<!-- Presenter notes: The FY 2027 OpEx plan totals $130.0M, a 9.3% increase over 2026. The two largest drivers are compensation and technology. On compensation: the $6.2M increase reflects 8 net new hires (primarily in Capital Markets: 4 senior advisors, 2 analysts, 1 credit officer, and 1 technology hire) at an average total compensation of $285K plus a 3.5% merit pool for existing staff. The merit pool is consistent with our compensation philosophy and peer benchmarks from our annual compensation survey. On technology: the $3.8M increase is the most significant OpEx delta in this plan. $1.8M is the Salesforce FSC platform investment approved (pending) at the August board meeting — this is the Phase 1 and Phase 2 implementation cost plus FY 2027 licensing. The remaining $2.0M covers our data infrastructure upgrade (cloud data warehouse migration to Snowflake) and cybersecurity enhancements following our 2026 security assessment. These investments are non-discretionary from a risk management perspective. The resulting adjusted EBITDA of $30.5M at 15.3% margin represents meaningful expansion versus 2026's 14.8% — proof that the technology investment is expected to generate operating leverage through the revenue leakage prevention and productivity improvements we presented in August. -->

---

# FY 2027 Capital Expenditure Plan

<div class="label">CapEx Budget</div>

| Item | Amount | Type | Depreciable Life |
|---|---|---|---|
| Salesforce FSC Implementation (Phase 1–2) | $1.2M | Development (capitalized portion) | 5 years |
| Atlanta Office Build-Out | $0.8M | Leasehold improvements | Lease term (5 years) |
| IT Infrastructure Refresh | $0.6M | Hardware / servers | 3–5 years |
| Furniture &amp; Equipment | $0.2M | FF&amp;E | 7 years |
| **Total CapEx** | **$2.8M** | | |

- Prior-year CapEx: $1.4M (maintenance only)
- FY 2027 CapEx elevated due to Atlanta build-out and technology capitalization
- D&amp;A projected: $2.4M (up from $2.4M in 2026 — new assets offset by legacy fully depreciated)

<!-- Presenter notes: The FY 2027 CapEx plan of $2.8M is approximately double the FY 2026 maintenance-only run-rate of $1.4M. This is intentional and reflects two investment decisions made in 2026. The Salesforce FSC implementation has both OpEx and CapEx components: the OpEx portion (license fees, training, most implementation services) is $1.8M and sits in the OpEx budget. The capitalized portion ($1.2M) covers the configuration and development work that creates an identifiable intangible asset — specifically the custom integration code and the database migration work. We worked with our auditors to determine the appropriate capitalization policy consistent with ASC 350-40. The Atlanta office build-out of $0.8M covers tenant improvements for the 4,500 square foot office space we leased in June 2026. We are amortizing this over the 5-year initial lease term. The IT infrastructure refresh replaces servers that are 6+ years old and at end of useful life. This is maintenance-driven, not growth-driven. Total D&A is expected to be $2.4M in FY 2027, essentially flat with 2026 because the new assets' depreciation is offset by legacy assets that become fully depreciated in 2026. CapEx is expected to normalize back to $1.5–1.8M annually starting in 2028 when the investment cycle is complete. -->

---

# FY 2027 Headcount Plan

<div class="label">People Plan</div>

| Department | FY 2026 EoY | Adds | Attrition | FY 2027 EoY |
|---|---|---|---|---|
| Capital Markets | 58 | +6 | -3 | 61 |
| Lending &amp; Credit | 42 | +1 | -2 | 41 |
| Wealth Management | 28 | +1 | -1 | 28 |
| Technology &amp; Data | 8 | +1 | 0 | 9 |
| Finance &amp; Ops | 8 | 0 | -1 | 7 |
| **Total** | **144** | **+9** | **-7** | **146** |

- Revenue per employee: $1.37M (2027 budget) vs. $1.30M (2026 actual) — 5.4% productivity gain
- Net adds concentrated in Capital Markets to support Atlanta expansion and mandate growth
- Voluntary attrition assumption: 4.9% (consistent with 2026 actuals)

<!-- Presenter notes: The FY 2027 headcount plan ends the year at 146 employees, a net increase of 2 from the 144 at year-end 2026. This disciplined approach reflects our commitment to productivity-driven growth — we are growing revenue 6.8% while growing headcount only 1.4%. Revenue per employee improves from $1.30M to $1.37M, a 5.4% gain driven by the mix shift toward high-value advisory work and the technology productivity investments. The Capital Markets additions are the most critical to the plan: we are adding 4 senior advisors (3 in Atlanta, 1 in New York), 1 deal analyst, and 1 client development role. All six positions have been pre-screened and we have LOIs out to two of the four senior advisor candidates — this is a significant de-risking step. The Lending add is a credit officer to manage the growing watch-list portfolio and support the new facilities pipeline. The Technology hire is a data engineer to support the Snowflake migration and ongoing data platform needs. Attrition assumption of 4.9% is based on our 5-year average. We have implemented retention programs for our top-quartile performers including equity refreshes for 12 senior advisors that we expect will reduce voluntary turnover in this cohort. -->

---

# Investment Priorities — FY 2027

<div class="label">Strategic Allocation</div>

- **Technology modernization** — $3.8M incremental spend enabling $2.4M annual benefit and competitive parity with peers
- **Geographic expansion** — Atlanta investment thesis: $6M budgeted revenue vs. $2.2M all-in cost (HR, RE, technology) = 2.7x revenue-to-cost ratio
- **Brand and business development** — $0.4M incremental for conference presence, digital marketing, and thought leadership content targeting mid-market M&amp;A buyers

<!-- Presenter notes: The three investment priorities for FY 2027 are sequenced by expected return and strategic importance. Technology modernization is the highest-priority and highest-ROI investment — the ROI analysis was presented in August and showed a 14-month payback and $3.2M 3-year NPV. Geographic expansion via Atlanta is our second priority — the 2.7x revenue-to-cost ratio is based on the budget assumption of $6M in Atlanta revenue versus $2.2M in all-in costs (4 advisor compensation at $400K average, office rent at $180K, technology, and administrative allocation). This ratio is achievable if the mandate assumptions hold, but Atlanta is the highest-execution-risk item in the plan. The board should note that Atlanta will likely be cash-negative in Q1 2027 as advisors ramp — we expect break-even around Q2 and profitability beginning Q3. Brand and business development is the smallest investment but strategically important: we are underpresent at the key mid-market M&A conferences relative to our competitive set. The $0.4M incremental covers two flagship conference sponsorships and a quarterly thought leadership publication targeting CFOs of mid-market companies — our primary buyer audience. All three investments are included in the OpEx budget and have been stress-tested in the sensitivity analysis on slide 8. -->

---

# Sensitivity Analysis

<div class="label">Scenario Planning — Revenue and EBITDA</div>

| Scenario | Revenue | EBITDA | Probability |
|---|---|---|---|
| Upside (deal acceleration + Atlanta outperforms) | $210M | $33.5M | 20% |
| Base Case (AOP) | $200M | $30.5M | 50% |
| Downside (2 major deal slips + Atlanta misses) | $190M | $27.0M | 25% |
| Stress (M&amp;A market contraction) | $178M | $22.0M | 5% |

- Base case probability-weighted revenue: **$198.5M** — management comfortable with $200M plan
- Stress scenario EBITDA of $22M remains above minimum viability threshold; cash covers obligations

<!-- Presenter notes: The sensitivity analysis provides the board with a range of outcomes and management's probability-weighted view. The probability weights reflect our internal assessment: base case remains most likely at 50%, but we have been deliberately conservative about the upside at 20%, recognizing that our planning has historically been conservative. The downside scenario at 25% reflects the known risks: two major Capital Markets deals slipping to Q1 2028, Atlanta revenue coming in at $4M versus $6M budget, and Lending NIM compression of 15 bps versus plan. Even in the downside scenario, EBITDA of $27.0M is healthy and free cash flow remains positive. The stress scenario at 5% probability represents a material deterioration in M&A market conditions — comparable to Q2 2023 when deal volumes dropped 30%. In this scenario, we cut $5M in variable compensation (incentive pool) and defer technology investment Phase 2 to preserve cash. Cash remains above $30M throughout the stress scenario, and we have $48M of revolver availability as further cushion. The board should note that our covenant-light revolver does not have financial maintenance covenants; we are not at risk of a technical default even in the stress scenario. Management will provide a board update in Q1 2027 if the probability of the stress scenario increases materially. -->

---

# Quarterly Phasing — FY 2027

<div class="label">Revenue and EBITDA by Quarter</div>

| Quarter | Revenue | EBITDA | EBITDA Margin | Notes |
|---|---|---|---|---|
| Q1 2027 | $44.0M | $5.5M | 12.5% | Ramp quarter; SF FSC go-live |
| Q2 2027 | $49.5M | $7.8M | 15.8% | Technology benefit begins; Atlanta ramp |
| Q3 2027 | $57.0M | $10.2M | 17.9% | Seasonally strong; peak deal closings |
| Q4 2027 | $49.5M | $7.0M | 14.1% | Deal timing risk; holiday slowdown |
| **FY 2027** | **$200.0M** | **$30.5M** | **15.3%** | |

- Q1 is intentionally lightest — deal pipeline not yet at full velocity; Atlanta early ramp
- Q3 is seasonally strongest; 3 of our top 5 historical deal closings occurred in Q3

<!-- Presenter notes: The quarterly phasing reflects seasonal patterns consistent with our historical experience. Q1 is consistently our weakest quarter in Capital Markets because we enter the year with deals that were in progress at year-end but require Q1 work before close — this creates a revenue recognition lag. Q1 2027 is further impacted by the Salesforce FSC go-live in January, which will require advisor time for training and transition. We expect a one-to-two week productivity dip during the transition. Q2 improves as Atlanta ramps and the Salesforce FSC productivity benefits begin to materialize. The technology benefit is modeled conservatively — we assume only 50% of the full productivity gain is realized in Q2, with 100% not until Q3. Q3 is our seasonally strongest quarter for Capital Markets — the mid-year deal calendar traditionally sees the most closings, particularly for calendar-year-end companies that want to close before the busy season. Q4 is moderately strong but subject to deal timing risk as buyers and sellers push deals that were expected in October-November into Q1 of the following year. We have built a $2M conservative buffer into Q4 Capital Markets versus the Q3 run rate to reflect this risk. The EBITDA margin phasing from 12.5% in Q1 to 17.9% in Q3 reflects the operating leverage in our model — fixed costs are relatively stable while revenue varies significantly by quarter. -->

---

# Risks to the Plan

<div class="label">Key Assumptions and Risk Register</div>

| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| Atlanta underperformance | -$2M revenue | Medium | 2 of 4 advisors already sourcing; milestone reviews quarterly |
| M&amp;A market softening | -$5M–10M revenue | Low-Medium | Diversified mandate pipeline; Lending segment provides buffer |
| Technology implementation delay | -$1M EBITDA benefit | Medium | Accenture has fixed-fee contract; go-live milestone contractual |
| Senior advisor attrition | -$3M revenue per departure | Low | Equity refresh program; retention agreements on top 5 |
| Rate environment change | ±$1.5M NIM impact | Medium | Modest; partially hedged through fixed-rate portfolio |

No new regulatory risks identified; standard financial services compliance requirements assumed unchanged.

<!-- Presenter notes: The risk register captures the five most material risks to the FY 2027 plan, along with impact estimates, probability assessments, and specific mitigations. Atlanta underperformance is our highest-concern risk: if the four advisors do not ramp as expected, revenue could be $2M below plan. We are mitigating this by holding quarterly milestone reviews starting in Q1, with predetermined actions if Q1 Atlanta revenue is below $1M (i.e., pause additional hiring and redirect marketing budget). The M&A market softening risk is macro and largely outside our control, but our pipeline diversification across 12 industry verticals and our Lending segment (which has different economic sensitivity) provides meaningful buffer. Technology delay risk is mitigated by our contract structure: Accenture is on a fixed-fee contract with milestone-based payments and a contractual go-live date of January 31, 2027, with a $150K penalty per week of delay beyond March 31. Senior advisor attrition is the risk we worry most about qualitatively — losing a single $3M-per-year producer would materially impact the plan and is difficult to replace quickly. The equity refresh program is our primary retention tool; the board should know that we have entered into 18-month retention agreements with our top five revenue producers. The rate environment risk is two-directional; a 50 bps rate increase would expand our NIM slightly ($1.5M upside) while a decrease of the same magnitude would compress it ($1.5M headwind). -->

---

# FY 2027 Board Asks

<div class="label">Resolutions Requested</div>

- **Approve** FY 2027 Annual Operating Plan: $200M revenue, $30.5M adjusted EBITDA
- **Approve** FY 2027 CapEx authorization of $2.8M for technology and Atlanta build-out
- **Authorize** CFO to manage to the AOP within a ±5% revenue variance without further board approval
- **Ratify** FY 2026 final dividend of $0.08/share for Q4, payable December 15, 2026

Management will provide quarterly board updates comparing actuals to this AOP at each scheduled board meeting.

<!-- Presenter notes: We are requesting four specific board resolutions today. First, AOP approval: this is the primary action required for management to operate against a board-approved budget in 2027. The AOP as presented is the base case; management will operate to this plan with the quarterly variance reporting structure I described. Second, CapEx authorization: our charter requires board approval for CapEx projects exceeding $2.0M in aggregate annually. The $2.8M plan exceeds this threshold, so we need explicit board authorization. Third, CFO variance authority: this is a standard resolution that allows management flexibility to respond to market conditions without convening a special board meeting for every revenue variance. The ±5% range is consistent with prior years. Fourth, the Q4 dividend ratification: we are continuing our $0.08/share quarterly dividend, consistent with our capital return policy. Are there any questions on the AOP before we proceed to the vote? I am happy to discuss any line item in more detail. -->

---

<!-- _class: ask -->

# Appendix — Segment Detail and Assumptions

<div class="label">Supporting Analysis</div>

- Capital Markets mandate pipeline: 18 active + 6 early-stage = 24 mandates tracked
- Lending new facility pipeline: $48M in credit committee; $30M expected to close in H1 2027
- Wealth Management — net new household target: 80 (requires 110 gross adds, 30 attrition)
- Technology investment NPV: $3.2M over 3 years at 10% discount rate (August 2026 analysis)
- Atlanta office 5-year pro forma: $30M cumulative revenue vs. $8M cumulative cost = 3.75x

Full segment models, headcount by role, and technology business case available in board materials portal.

<!-- Presenter notes: The appendix slide provides the key supporting assumptions behind the FY 2027 AOP for board members who wish to drill deeper. The detailed segment models, including quarterly breakdowns by deal type for Capital Markets and by facility type for Lending, are available in the board materials portal and can be shared with board finance committee members who request them. The Atlanta 5-year pro forma is particularly important context: the $8M in cumulative cost includes all people, real estate, technology, and allocated overhead — the fully-loaded cost view. Against $30M in 5-year cumulative revenue, the net contribution is $22M, making Atlanta the highest-ROI geographic expansion in our history. This is of course dependent on advisor ramp and mandate assumptions that have meaningful uncertainty in Years 1 and 2, but we are confident in the long-term thesis. Management is happy to schedule one-on-one sessions with any board member who wishes to discuss the assumptions in more detail before the vote. The CFO office will be available by phone through end of business on Friday. Thank you for your time and attention to this presentation. We look forward to your questions. -->
