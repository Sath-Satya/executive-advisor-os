<!-- TEMPLATE: ma-financing
     CATEGORY: Finance
     USE WHEN: M&A financing options pitch to board or transaction committee
     SLIDE COUNT: 10
     PALETTE: Corporate cream with gold accents
     RENDER: marp --pptx 59-ma-financing.md -->

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
    --dark-gold: #8a6f3a;
    --light-gold: #e8d5a8;
    --muted: #5a6a7a;
    --rule: #d4c9b0;
    --green: #2a7d5f;
    --red: #c0392b;
    --blue: #2c5f8a;
  }
  section {
    background: var(--cream);
    color: var(--navy);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 62px;
  }
  h1 {
    font-size: 1.85rem; font-weight: 700; color: var(--navy);
    letter-spacing: -0.3px; border-bottom: 3px solid var(--gold);
    padding-bottom: 9px; margin-bottom: 20px;
  }
  h2 { font-size: 1.2rem; font-weight: 600; color: var(--dark-gold); margin-bottom: 12px; }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 10px; font-size: 0.98rem; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88rem; margin-top: 10px; }
  th { background: var(--navy); color: var(--cream); padding: 8px 12px; text-align: left; }
  td { padding: 6px 11px; border-bottom: 1px solid var(--rule); }
  tr:nth-child(even) td { background: #ede9e0; }
  .label {
    display: inline-block; background: var(--gold); color: var(--cream);
    font-size: 0.68rem; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; padding: 3px 10px; border-radius: 3px; margin-bottom: 12px;
  }
  .option-card {
    border: 1px solid var(--rule); border-radius: 8px; padding: 16px 20px; margin-bottom: 12px;
    background: white; border-top: 4px solid var(--gold);
  }
  .option-card .title { font-weight: 700; font-size: 1.05rem; color: var(--navy); margin-bottom: 6px; }
  .option-card .detail { font-size: 0.88rem; color: var(--muted); }
  .rec-box {
    background: var(--navy); color: var(--cream); border-radius: 10px;
    padding: 22px 30px; margin-top: 18px; border-left: 6px solid var(--gold);
  }
  .rec-box .title { font-size: 1.1rem; font-weight: 700; color: var(--gold); margin-bottom: 10px; }
  .rec-box .detail { font-size: 0.95rem; color: #c0cfd8; line-height: 1.5; }
  .fav { color: var(--green); font-weight: 700; }
  .unfav { color: var(--red); font-weight: 700; }
  .neutral { color: var(--blue); font-weight: 700; }
  section.cover {
    background: var(--navy); color: var(--cream);
    display: flex; flex-direction: column; justify-content: center;
  }
  section.cover h1 { color: var(--cream); border-color: var(--gold); font-size: 2.1rem; }
  section.cover .sub { color: var(--gold); font-size: 1.0rem; margin-top: 8px; }
  section.cover .meta { color: #8899ac; font-size: 0.85rem; margin-top: 22px; line-height: 1.8; }
  section.close {
    background: var(--navy); color: var(--cream);
    display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
  }
  section.close h1 { color: var(--gold); border: none; font-size: 1.9rem; }
  section.close p { color: #8899ac; font-size: 0.92rem; line-height: 1.8; }
---

<!-- _class: cover -->

<div class="label">Confidential — Board Transaction Committee</div>

# Project Compass — M&amp;A Financing Options

<div class="sub">Acquisition of Beacon Capital Partners — Financing Alternatives Analysis</div>
<div class="meta">
  Prepared by: Northwind Capital Finance Team<br>
  Transaction Size: $52M Enterprise Value &nbsp;|&nbsp; Date: December 8, 2026<br>
  Presented to: Board Transaction Committee (Confidential — Do Not Distribute)
</div>

<!-- Presenter notes: Good afternoon, transaction committee members. This presentation covers the financing alternatives for Project Compass — the proposed acquisition of Beacon Capital Partners, a 5-person boutique capital markets advisory firm in Chicago with $8M in annual revenue and an established mid-market M&A client base. The board approved management to conduct full due diligence on this transaction at the November 5 finance committee meeting. Today we are presenting the financing options analysis, and we are requesting the committee's direction on a preferred financing approach before we engage with external parties. The transaction is at the letter of intent stage; we have signed a mutual NDA and exclusivity agreement through January 15, 2027. This presentation is subject to M&A confidentiality protocols — please do not discuss specifics outside this meeting. The deck covers: transaction summary, financing options, cost of capital, dilution analysis, covenant analysis, credit metrics, recommendation, risks, timeline, and close. -->

---

# Transaction Summary — Project Compass

<div class="label">Acquisition Overview</div>

| Item | Detail |
|---|---|
| Target | Beacon Capital Partners LLC — Chicago boutique advisory |
| Enterprise Value | $52.0M (5.5x LTM EBITDA of $9.5M; 6.5x revenue of $8.0M) |
| Consideration | $40M cash + $12M earnout (3-year, revenue-based) |
| Strategic Rationale | 5 senior advisors + Chicago client base; accelerates mid-market M&A footprint |
| Revenue Synergies | $4–6M Year 1 (cross-sell Northwind Lending and Wealth to Beacon clients) |
| Cost Synergies | $1.2M Year 1 (G&amp;A, real estate, technology consolidation) |
| Pro Forma Revenue | ~$195M YTD run-rate (Northwind $187M + Beacon $8M) |
| Due Diligence Status | Financial, legal, and talent DD complete; no material issues identified |

Northwind's first acquisition. Deal structure approved in principle by CFO and General Counsel.

<!-- Presenter notes: The transaction economics are attractive. At 5.5x LTM EBITDA, we are acquiring Beacon at a discount to Northwind's own trading multiple of approximately 8x trailing EBITDA. The $40M cash consideration is within our capital allocation framework — we have $49.8M in net cash and the board has pre-authorized management to use up to $20M for acquisitions subject to board approval for the specific transaction. The $12M earnout is structured over three years tied to Beacon revenue retention above $7M per year — this protects us against client attrition following the transaction, which is the primary risk in advisory acquisitions. The five Beacon advisors have all signed letters of intent to remain with Northwind for a minimum of 3 years, subject to completion of definitive agreements. Compensation packages are consistent with Northwind's advisor comp structure; total incremental compensation cost is approximately $2.4M annually. Revenue synergies of $4–6M in Year 1 reflect the opportunity to cross-sell Northwind's Lending products to Beacon's manufacturing and business services clients who currently do not have a lending relationship with Northwind. The $1.2M cost synergies are real and achievable: Beacon's IT infrastructure ($320K), real estate ($480K as they move into Northwind Chicago space), and G&A ($400K) will be consolidated. Due diligence found no material liabilities, no pending litigation, and no client concentration above 15%. We are ready to proceed to definitive agreement pending committee direction on financing. -->

---

# Financing Options — Overview

<div class="label">Three Alternatives</div>

<div class="option-card">
  <div class="title">Option A — All-Cash from Balance Sheet</div>
  <div class="detail">Deploy $40M from existing $49.8M cash position. No new debt. No dilution. Leaves $9.8M cash (below $15M operating floor — requires exception or temporary floor reduction).</div>
</div>

<div class="option-card">
  <div class="title">Option B — Debt-Financed (Senior Secured Term Loan)</div>
  <div class="detail">Borrow $30M at SOFR + 200 bps (est. 7.4%); fund $10M from cash. Preserves $39.8M cash. Adds $30M debt (1.0x pro forma net leverage). 5-year amortizing term.</div>
</div>

<div class="option-card">
  <div class="title">Option C — Mixed (Debt + Equity)</div>
  <div class="detail">Issue $15M common equity (~500K shares at $29.90); borrow $15M at SOFR + 175 bps (est. 7.15%); fund $10M from cash. Lowest leverage. 2.1% dilution.</div>
</div>

<!-- Presenter notes: The three financing options represent the full range of approaches available to Northwind given our balance sheet and capital market access. Option A (all-cash) is the simplest and least expensive in terms of financing cost, but it creates a temporary cash position below our board-mandated $15M operating floor. Management would need to request a temporary floor waiver from the board for 90 days while operating cash flow rebuilds the balance. Based on Q3 FCF run-rate of $10M per quarter, we would return to $15M in approximately 6 weeks. The board would need to approve this waiver explicitly. Option B (debt-financed) preserves the most cash flexibility and keeps our equity count unchanged. At $30M of new debt, pro forma net leverage is 1.0x trailing EBITDA (combined $30M debt / $27.8M EBITDA) — within our 0–1x target range but at the ceiling. The interest cost of $2.2M annually is easily covered by Beacon's EBITDA contribution. Option C (mixed) is the most expensive in total cost (combined interest plus dilution) but the most conservative from a leverage standpoint. Issuing equity at current prices (~0.9x book value) is not optimal timing from a per-share dilution perspective, but the market environment may be receptive to a small secondary offering given our strong Q3 results. All three options are feasible; the committee's direction on risk appetite and dilution tolerance will drive the recommendation. -->

---

# Cost of Capital Analysis

<div class="label">Financing Cost Comparison</div>

| Option | Financing Cost | After-Tax Cost | All-In Rate | Annual Interest/Dilution $ |
|---|---|---|---|---|
| A — Cash | 5.1% (T-bill yield foregone) | 3.6% | 3.6% | $1.4M/year (opportunity cost) |
| B — $30M Term Loan | SOFR + 200 bps (~7.4%) | 5.3% | 5.3% | $2.2M/year |
| C — $15M Equity + $15M Debt | Blended ~6.8% | ~4.9% | 4.9% + dilution | $1.1M + ~$0.02 EPS dilution/year |
| Weighted Average Cost of Capital | — | ~10% | — | Hurdle rate for investment |

- Beacon transaction IRR: 18.4% (base case, including synergies) — exceeds WACC by 840 bps
- All three financing options generate positive NPV given 18.4% acquisition IRR
- Cheapest financing: Option A. Most strategic flexibility: Option B.

<!-- Presenter notes: The cost of capital analysis frames the financing decision in terms of return vs. cost. All three options generate a significant positive spread to WACC — the acquisition IRR of 18.4% exceeds our 10% WACC hurdle by 840 basis points regardless of financing approach, so the transaction creates value under any option. The financing choice is therefore about risk management and strategic flexibility, not about whether the deal clears the hurdle. Option A has the lowest financing cost — the foregone T-bill yield of 5.1% (3.6% after-tax) is less than the cost of debt in Options B and C. However, Option A leaves us with minimal cash cushion, which has strategic cost: we cannot pursue additional opportunities, we have less flexibility in a market downturn, and we temporarily breach our operating floor. Option B is slightly more expensive on a cost-of-capital basis (5.3% after-tax) but preserves significantly more strategic flexibility. The annual interest of $2.2M is fully covered by Beacon's $9.5M EBITDA in the first year, even before synergies. Option C blends the costs but adds EPS dilution — approximately $0.02 per year on the equity component. At current share price, we are issuing equity at approximately 0.9x book value, which is modestly dilutive to book value per share. We would not recommend Option C at current prices unless strategic flexibility is the paramount concern. -->

---

# Dilution Impact Analysis

<div class="label">Per-Share Impact Under Each Option</div>

| Metric | Pre-Transaction | Option A | Option B | Option C |
|---|---|---|---|---|
| Shares Outstanding | 21.8M | 21.8M | 21.8M | 22.3M |
| % Dilution | — | 0% | 0% | 2.1% |
| Book Value / Share | $15.68 | $13.84 | $15.46 | $15.32 |
| FY 2027 Adj. EPS (est.) | $1.52 | $1.62 | $1.55 | $1.49 |
| EPS Accretion / (Dilution) | — | +$0.10 | +$0.03 | -$0.03 |

- Options A and B are EPS accretive from Year 1; Option C is modestly dilutive
- Book value impact: Option A reduces book value by $1.84/share (Beacon carries no tangible book value)
- Earnout of $12M (if fully earned) will further reduce book value over 3 years across all options

<!-- Presenter notes: The per-share impact table is critical for committee members thinking about shareholder value. EPS accretion is the most watched metric for public company M&A. Options A and B are both EPS accretive in Year 1 — Beacon's EBITDA contribution and cost synergies more than offset the financing cost, generating net accretion of $0.10 and $0.03 per share respectively. Option C is modestly dilutive at $0.03 per share due to the equity issuance. Book value impact is more nuanced: Beacon does not carry meaningful tangible book value (it is a people business), so the entire $40M cash consideration is goodwill and intangible assets. This reduces reported book value per share under all options. The earnout of up to $12M, if fully earned over three years, will be an additional P&L charge of approximately $4M per year under ASC 805 earnout accounting, which I have included in the EPS estimates. I want to flag one important consideration: because we recently repurchased stock at an average of $28.90 (0.9x book), issuing equity at similar prices for Option C would be economically inconsistent. We were a net buyer of our own shares at 0.9x book; issuing at the same level dilutes existing shareholders' book value for the same reason we were buying. This is a strong argument against Option C at current prices. -->

---

# Covenant Analysis

<div class="label">Debt Covenant Compliance — Options B and C</div>

| Covenant | Requirement | Pro Forma (Option B) | Pro Forma (Option C) | Cushion (B) |
|---|---|---|---|---|
| Net Leverage (Debt/EBITDA) | &lt; 2.5x | 0.78x | 0.39x | 68.8% |
| Interest Coverage (EBITDA/Interest) | &gt; 4.0x | 16.8x | 28.3x | 320% |
| Min. Liquidity | &gt; $15M | $39.8M | $44.8M | $24.8M above |
| Capex Limit | &lt; $10M/yr | $2.8M planned | $2.8M planned | $7.2M below |

- Covenant package proposed: leverage covenant + interest coverage + liquidity floor; no financial maintenance covenant (incurrence-based preferred)
- Rating agencies: No new rating required; transaction is under bond-exempt threshold
- Lender: Existing revolving credit facility lender (JPMorgan) has confirmed willingness to provide term loan at indicative terms

<!-- Presenter notes: If the committee selects Option B or C, the covenant package will be negotiated with the lender. Our existing bank (JPMorgan) has provided a term sheet with indicative terms for a $30M or $15M senior secured term loan. The proposed covenant package is conservative from our perspective: net leverage of 2.5x versus our pro forma 0.78x gives us 68.8% cushion before any covenant tension. We are requesting incurrence-based covenants rather than maintenance covenants — the distinction is important. A maintenance covenant would require us to stay below 2.5x leverage every quarter, even if market conditions caused a temporary earnings dip. An incurrence covenant only applies when we want to take a new action (like another acquisition). Most mid-market borrowers our size have maintenance covenants; given our strong cash position and track record, we believe we can negotiate incurrence-only, and JPMorgan has indicated they would accept this given our relationship. Interest coverage of 16.8x under Option B is extremely comfortable — even if Beacon contributes zero revenue in the first year (a stress scenario), our interest coverage is still well above 4x on Northwind's standalone earnings. The liquidity floor minimum of $15M is our own policy; the covenant would be set at $10M (more conservative than the lender typically requires) to give us contractual protection against management decisions to over-deploy cash. -->

---

# Credit Metrics — Pro Forma Analysis

<div class="label">Balance Sheet Quality Post-Transaction</div>

| Metric | Current | Pro Forma (Option B) | Pro Forma (Option C) |
|---|---|---|---|
| Cash &amp; Equivalents | $49.8M | $39.8M | $44.8M |
| Total Debt | $0 | $30.0M | $15.0M |
| Net Cash / (Net Debt) | +$49.8M | +$9.8M | +$29.8M |
| EBITDA (Pro Forma with Beacon) | $27.8M | $37.3M | $37.3M |
| Net Leverage | -1.8x (net cash) | 0.54x | 0.40x |
| Book Value | $342M | $342M | $342M |

Goodwill and intangibles: $40M added to balance sheet; amortizable intangibles ~$18M over 10 years.

<!-- Presenter notes: The credit metrics slide shows that Northwind's balance sheet remains very strong under all three financing options. Even under Option B (the most leveraged), net leverage of 0.54x is well below our 1.0x target ceiling and below the peer group median of 0.8x. The pro forma EBITDA of $37.3M reflects Northwind's $27.8M plus Beacon's $9.5M for a full year. I want to note two accounting items that the committee should be aware of. First, goodwill: the $40M consideration will be allocated under ASC 805 purchase accounting. We expect approximately $18M to be allocated to customer relationships and non-compete agreements (amortizable over 10 years — approximately $1.8M per year in additional D&A) and $22M to goodwill (non-amortizing but subject to annual impairment testing). This incremental D&A of $1.8M per year is included in the EPS estimates on the dilution slide but does not affect EBITDA or cash flow. Second, earnout accounting: the $12M earnout will be recognized as compensation expense over the 3-year earnout period, contingent on achievement. This is a P&L charge of up to $4M per year, which is included in our EPS estimates. If the earnout is not fully earned (i.e., Beacon revenue falls below $7M), actual charges will be lower. -->

---

<div class="rec-box">
  <div class="title">Management Recommendation — Option B: $30M Senior Secured Term Loan</div>
  <div class="detail">
    Borrow $30M at SOFR + 200 bps (incurrence covenants). Fund $10M from cash. Preserves $39.8M liquidity.
    Rationale: EPS accretive, minimal leverage at 0.54x, preserves strategic flexibility for additional opportunities,
    avoids equity issuance at below-intrinsic-value prices, and JPMorgan has confirmed availability of terms.
  </div>
</div>

- **Against:** Option A reduces cash below policy floor (requires waiver); Option C dilutes at sub-intrinsic-value prices
- **Key condition:** Incurrence-only covenants; no financial maintenance covenants
- **Second choice:** Option A with board-approved temporary floor waiver if debt terms deteriorate

<!-- Presenter notes: Management's recommendation is Option B for three reasons. First, it is EPS accretive (+$0.03 per share) and preserves the maximum strategic flexibility of the three options, leaving $39.8M in liquidity versus $9.8M under Option A. Second, it avoids equity issuance at prices we believe are below intrinsic value — we have been buying back stock at 0.9x book, so issuing at similar levels is economically inconsistent. Third, the leverage of 0.54x is very conservative and well within our policy targets. The annual interest cost of $2.2M is covered approximately 17x by pro forma EBITDA. The critical condition on Option B is the covenant structure: we must secure incurrence-only covenants. If JPMorgan insists on maintenance covenants, we should evaluate whether the resulting constraint on strategic flexibility justifies the debt. Our preliminary discussion with JPMorgan suggests they will accept incurrence covenants given our track record and cash position. Our second choice is Option A with a temporary board-approved floor waiver, to be used if debt market conditions deteriorate materially before closing. The earnout structure of $12M provides additional seller alignment and reduces our upfront risk — if Beacon's revenue declines post-close, the earnout payments are reduced proportionally. Management is confident in this recommendation but is seeking the committee's direction before proceeding to formal term sheet negotiations. -->

---

# Risks and Mitigants

<div class="label">Transaction Risk Register</div>

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Advisor attrition post-close | Medium | High | 3-year LOIs signed; retention structure aligns comp to performance |
| Client concentration loss | Medium | Medium | No client &gt;15% of Beacon revenue; due diligence included client relationship reviews |
| Integration complexity | Low | Medium | Salesforce FSC integration plan drafted; IT integration timeline Q2 2027 |
| Earnout dispute | Low | Low | Earnout formula clear; revenue defined as invoiced advisory fees; quarterly true-up |
| Rate increase impact (debt cost) | Medium | Low | $30M floating rate; 100 bps increase = $0.3M annual cost — immaterial |

<!-- Presenter notes: The risk register covers the five most material transaction risks. Advisor attrition is the primary risk in advisory acquisitions — you are buying people, and if the key people leave, value erodes quickly. We have mitigated this through three-year LOIs for all five Beacon advisors, structured as retention agreements with performance-based vesting. These are legally binding and include 12-month non-compete provisions. We have personally interviewed each of the five advisors; all expressed genuine enthusiasm for joining a larger platform with more resources. The client concentration analysis is important: we reviewed Beacon's top 20 clients with their managing partner. The largest client represents 14.8% of Beacon revenue — below our 15% threshold. We also conducted soft reference checks with three of the largest clients, all of whom indicated they would expect to continue the relationship post-acquisition. Integration complexity is manageable given our technology investment — the Salesforce FSC go-live in January 2027 includes a module specifically designed for acquired practices, and the Beacon integration is planned for Q2 2027. The earnout dispute risk is low because we have deliberately structured a clean formula: Beacon revenue is defined as invoiced advisory fees (not collected fees, to avoid disputes on timing), measured quarterly, with a true-up mechanism. The rate risk is the most straightforward — at $30M floating, a 100 bps increase in rates adds $0.3M to annual interest, which is below 1% of pro forma revenue. -->

---

# Transaction Timeline

<div class="label">Path to Close</div>

| Milestone | Target Date | Owner | Status |
|---|---|---|---|
| Committee financing direction | December 8, 2026 | Board Committee | Today |
| JPMorgan term sheet finalization | December 15, 2026 | CFO | Indicative terms received |
| Definitive Purchase Agreement signed | December 22, 2026 | GC + CFO | LOI signed; definitive in drafting |
| Board final approval | January 7, 2027 | Full Board | Scheduled |
| Regulatory clearance (HSR) | January 20, 2027 | GC | HSR filing December 10 |
| Transaction close | January 31, 2027 | CFO | Target (subject to HSR) |
| Beacon integration launch | February 1, 2027 | CIO + CRO | Plans drafted |

HSR filing threshold: $101.4M (2026 threshold); transaction at $52M is below HSR — voluntary filing for prudence only.

<!-- Presenter notes: The timeline is aggressive but achievable given the work completed to date. We have been in diligence for six weeks and have resolved all material items. The key milestones in the next 30 days: first, the committee must provide financing direction today or by December 10 at the latest to allow JPMorgan to finalize terms. Second, the definitive purchase agreement is in near-final form — outside counsel estimates 3–4 days of remaining negotiation once we provide the financing decision. Third, the full board approval on January 7 is a special meeting called for this purpose; the agenda, materials, and board consent documents will be circulated by December 22. On regulatory: Northwind and Beacon combined revenue is approximately $195M, which is below the 2026 HSR Act filing threshold of $101.4M for the size-of-the-parties test. However, General Counsel has recommended a voluntary HSR filing for the protection it provides. If the DOJ declines to issue a Second Request within 30 days of filing (the standard early termination period), we are clear to close. We do not expect any antitrust issues — Northwind and Beacon have negligible competitive overlap in the Chicago mid-market advisory market. Transaction close is targeted for January 31, 2027, which is a meaningful date: it allows Beacon revenue to be included in Q1 2027 results from day one. -->

---

<!-- _class: close -->

# Committee Direction Requested — December 8, 2026

**Three decisions required today:**

1. Confirm financing approach (Option A, B, or C)
2. Authorize CFO to finalize JPMorgan term sheet (Option B/C) or board floor waiver (Option A)
3. Authorize execution of Definitive Purchase Agreement by December 22, 2026

Failure to decide today delays close by 7–14 days and risks exclusivity expiration (January 15, 2027).

<!-- Presenter notes: The committee needs to make three specific decisions today. Without a financing decision, we cannot finalize the JPMorgan term sheet, which is a prerequisite to the Definitive Purchase Agreement. The definitive agreement purchase price mechanics require the financing structure to be documented. We have an exclusivity window through January 15 — if we miss the December 22 definitive agreement target by more than a week, we risk the Beacon founding partners reopening negotiations with a competing buyer (one has been identified in our discussions). Management's strong preference is to close this transaction. We have negotiated favorable deal economics, completed thorough due diligence, and secured commitment from the Beacon advisors to join Northwind. This is a high-quality asset at a fair price that will accelerate our Chicago market position, contribute Day 1 EPS accretion, and create a platform for further geographic growth. The committee's direction today enables a clean January 31 close and allows us to announce the acquisition alongside our Q4 2026 earnings in February — a positive narrative for the market. Management recommends Option B. Are there questions before the committee discusses and votes? -->
