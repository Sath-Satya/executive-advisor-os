<!-- TEMPLATE: treasury-review
     CATEGORY: Finance
     USE WHEN: quarterly treasury operations review with CFO or finance committee
     SLIDE COUNT: 9
     PALETTE: Dark developer palette
     RENDER: marp --pptx 60-treasury-review.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --dark: #0a0e14;
    --surface: #111820;
    --surface2: #162030;
    --white: #ffffff;
    --text: #d0d8e4;
    --muted: #8899ac;
    --subtle: #556677;
    --blue: #3b9eff;
    --green: #2dd4a0;
    --amber: #f0a050;
    --red: #f06070;
    --rule: #1e2a38;
  }
  section {
    background: var(--dark);
    color: var(--text);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 60px;
  }
  h1 {
    font-size: 1.85rem; font-weight: 700; color: var(--white);
    letter-spacing: -0.3px; border-bottom: 2px solid var(--green);
    padding-bottom: 8px; margin-bottom: 20px;
  }
  h2 { font-size: 1.15rem; font-weight: 600; color: var(--green); margin-bottom: 12px; }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 9px; font-size: 0.98rem; line-height: 1.55; color: var(--text); }
  table { width: 100%; border-collapse: collapse; font-size: 0.88rem; margin-top: 10px; }
  th {
    background: var(--surface); color: var(--green);
    padding: 8px 12px; text-align: left;
    border-bottom: 1px solid var(--blue);
    font-weight: 600;
  }
  td { padding: 7px 12px; border-bottom: 1px solid var(--rule); color: var(--text); }
  tr:nth-child(even) td { background: var(--surface); }
  .label {
    display: inline-block; background: var(--green); color: var(--dark);
    font-size: 0.68rem; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; padding: 3px 10px; border-radius: 3px; margin-bottom: 12px;
  }
  .kpi-row { display: flex; gap: 20px; margin-top: 18px; }
  .kpi {
    flex: 1; background: var(--surface); border: 1px solid var(--rule);
    border-radius: 10px; padding: 18px 20px; text-align: center;
    border-top: 3px solid var(--green);
  }
  .kpi .num { font-size: 1.8rem; font-weight: 700; color: var(--green); }
  .kpi .lbl { font-size: 0.75rem; color: var(--muted); margin-top: 6px; }
  .status-green { color: var(--green); font-weight: 700; }
  .status-red { color: var(--red); font-weight: 700; }
  .status-amber { color: var(--amber); font-weight: 700; }
  .metric-block {
    background: var(--surface); border-radius: 8px; padding: 14px 18px;
    margin-bottom: 10px; border-left: 3px solid var(--blue);
    font-size: 0.92rem;
  }
  .metric-block .title { color: var(--muted); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 4px; }
  .metric-block .value { color: var(--white); font-weight: 700; font-size: 1.1rem; }
  section.cover {
    background: linear-gradient(135deg, #0a0e14 50%, #0d1e2e 100%);
    display: flex; flex-direction: column; justify-content: center;
  }
  section.cover h1 { color: var(--white); border-color: var(--green); font-size: 2.2rem; }
  section.cover .sub { color: var(--green); font-size: 1.0rem; margin-top: 10px; }
  section.cover .meta { color: var(--muted); font-size: 0.86rem; margin-top: 24px; line-height: 1.8; }
  section.close {
    background: linear-gradient(135deg, #0a0e14 0%, #0d1e2e 100%);
    display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
  }
  section.close h1 { color: var(--green); border: none; font-size: 2.0rem; }
  section.close p { color: var(--muted); font-size: 0.92rem; line-height: 1.8; }
---

<!-- _class: cover -->

<div class="label">Treasury Operations Review — Q4 2026</div>

# Northwind Capital — Treasury Review

<div class="sub">Quarterly Treasury Operations Report: Cash, Liquidity, FX, Debt, and Investments</div>
<div class="meta">
  Prepared by: Jennifer Walsh, Treasurer &nbsp;|&nbsp; Reviewed by: Sarah Kim, CFO<br>
  Period: October 1 – December 31, 2026 &nbsp;|&nbsp; Presented: January 14, 2027<br>
  Audience: CFO + Finance Committee &nbsp;|&nbsp; Confidential
</div>

<!-- Presenter notes: Good morning. This is the Q4 2026 Treasury Operations Review, covering the four-quarter period ending December 31, 2026. The treasury report is a quarterly internal document reviewed by the CFO and presented to the finance committee on a semi-annual basis. Q4 2026 is a particularly eventful treasury quarter: we initiated the Project Compass term loan ($30M), completed our T-bill investment program, and began the post-acquisition cash position rebuild. I will cover nine sections in approximately 50 minutes: cash position, liquidity, FX exposure, debt portfolio, investments, counterparty risk, covenant status, treasury initiatives, and close with recommended actions. Where applicable I have included comparisons to our approved Treasury Policy limits. Any breach of a Treasury Policy limit is flagged in red; there are none this quarter. The full supporting data, daily cash position history, and bank statement reconciliations are in the appendix binder distributed to the CFO in advance. -->

---

# Cash Position — December 31, 2026

<div class="label">Quarter-End Cash Summary</div>

<div class="kpi-row">
  <div class="kpi"><div class="num">$22.1M</div><div class="lbl">Operating Cash (JPMorgan)</div></div>
  <div class="kpi"><div class="num">$5.0M</div><div class="lbl">T-Bill Portfolio</div></div>
  <div class="kpi"><div class="num">$3.4M</div><div class="lbl">Payroll / Operating Reserves</div></div>
  <div class="kpi"><div class="num">$30.5M</div><div class="lbl">Total Cash &amp; Equiv.</div></div>
</div>

- Q4 cash position reflects: $40M Beacon acquisition close (January 31 — cash held in escrow Q4)
- Escrow balance: $40M held at JPMorgan Escrow Services pending January 31 close
- Total available liquidity including revolver: $30.5M cash + $52M revolver = $82.5M

<!-- Presenter notes: The Q4 cash position requires context to interpret correctly. The $30.5M operating cash balance is lower than the Q3 high of $49.8M, but this reflects the funding structure for the Beacon acquisition rather than cash consumption. The $40M acquisition consideration was funded by drawing down the $30M JPMorgan term loan (closed December 20, 2026) and deploying $10M of operating cash into JPMorgan's acquisition escrow account. The escrow account holds $40M as of December 31 and will be released to Beacon selling shareholders upon transaction close on January 31, 2027. For covenant purposes, the $40M escrow is treated as restricted cash and does not count toward our $15M liquidity floor — we are in full compliance with the floor using only the $22.1M operating balance. The T-bill portfolio was maintained at $5M during Q4 (30-day rolling); at the current 5.1% yield, we earned $64K in interest income in Q4 — modest but meaningful for essentially risk-free returns. The payroll and operating reserves represent our standard segregated accounts for payroll funding ($2.0M) and vendor payment reserves ($1.4M). I will note that post-Beacon close in January, the escrow releases and the operating cash balance will be at approximately $22M — above the $15M floor but below our typical operating level of $38–40M. We expect FCF generation in Q1 2027 to rebuild the balance to $28–30M by March 31. -->

---

# Liquidity Analysis

<div class="label">12-Month Liquidity Forecast</div>

| Period | Opening Cash | Operating FCF | Beacon Acquisition | Debt Draw | Closing Cash |
|---|---|---|---|---|---|
| Q4 2026 (actual) | $49.8M | $10.2M | -$10M (escrow) | +$30M (term) | $30.5M + $40M escrow |
| Q1 2027 (forecast) | $22.1M | $8.5M | -$40M (close) | — | ~$21.1M |
| Q2 2027 (forecast) | ~$21.1M | $10.5M | — | — | ~$31.6M |
| Q3 2027 (forecast) | ~$31.6M | $14.0M | — | — | ~$45.6M |

- **Minimum cash in 12 months:** ~$21M (Q1 2027 post-close) — above $15M floor &#x2713;
- Revolver: $52M available throughout; provides additional cushion at any point
- Interest on $30M term loan: $2.2M annual; $550K per quarter beginning Q1 2027

<!-- Presenter notes: The 12-month liquidity forecast is the most important slide in the treasury review for the finance committee. The critical constraint is Q1 2027 post-close, when cash drops to approximately $21M after the $40M acquisition payment flows from escrow to Beacon shareholders. At $21M, we are $6M above the $15M policy floor — tight but compliant. The revolver provides an important backstop: if Q1 revenue comes in below plan (possible given the Salesforce FSC go-live timing effects discussed in the earnings deck), we have $52M of undrawn revolver to cover any temporary cash needs without stress. Q2 and Q3 2027 show rapid cash rebuilding driven by strong FCF from the combined Northwind + Beacon business. By Q3 2027, we expect to be back above $45M in cash, consistent with our pre-acquisition levels. The term loan interest of $550K per quarter is included in the FCF estimates and does not materially affect the trajectory. Key assumptions in this forecast: FCF is modeled at 90% of adjusted EBITDA (consistent with our 2026 conversion rate), Beacon closes on January 31, and no additional acquisitions or capital returns are assumed beyond the existing $6.1M buyback authorization. I have stress-tested this forecast assuming Q1 FCF 30% below plan ($5.9M versus $8.5M base): cash still clears the $15M floor at $17.5M. The committee should feel comfortable that liquidity is well managed through this acquisition period. -->

---

# Foreign Exchange Exposure

<div class="label">FX Risk Inventory — Q4 2026</div>

| Currency | Exposure Type | Notional | Tenor | Hedged? | Notes |
|---|---|---|---|---|---|
| Canadian Dollar (CAD) | Revenue — 2 advisory mandates | $1.8M USD equiv. | &lt;90 days | <span class="status-amber">Partial — 50%</span> | Hedge cost: $12K/month |
| British Pound (GBP) | Vendor payment | $0.4M USD equiv. | 30 days | <span class="status-red">No</span> | Immaterial; no hedge warranted |
| Euro (EUR) | Potential Beacon EU referral | $0 current | Future | <span class="status-amber">Monitoring</span> | Beacon had 1 EU client; assess post-close |

Total FX exposure: $2.2M — **below $5M materiality threshold** for full hedging program

Overall FX risk: **Low.** Northwind's revenue is 97% USD-denominated. FX policy: hedge exposures &gt;$5M or &gt;90 days tenor.

<!-- Presenter notes: Northwind's FX risk profile is very simple relative to most financial services firms because our advisory revenue is predominantly USD-denominated. The two Canadian dollar exposures relate to advisory mandates for Canadian companies with US operations — we quoted our fees in USD equivalents at mandate signing, but payment will be made in CAD and converted on receipt. The two mandates have a combined USD equivalent of $1.8M. We have hedged 50% of this exposure through forward contracts at a cost of $12K per month — the residual $900K exposure is small enough that we believe the hedging cost on the remaining 50% is not warranted. The GBP exposure of $0.4M is a technology vendor payment for a licensing fee that we pay annually in sterling; at this level, the hedge cost exceeds the FX risk in expected value terms, so we leave this unhedged. The EUR monitoring item is a prudent pre-close assessment: one of Beacon's long-standing clients is a European private equity firm that occasionally engages Beacon for US M&A advisory. If we see more EUR-denominated advisory work post-acquisition, we will add EUR hedging to our program. The $5M materiality threshold is defined in our Treasury Policy, last approved by the board in February 2025. I will recommend a Treasury Policy refresh in Q2 2027 given the acquisition and expanded geographic footprint. -->

---

# Debt Portfolio

<div class="label">Debt Obligations — December 31, 2026</div>

| Facility | Type | Outstanding | Rate | Maturity | Covenants |
|---|---|---|---|---|---|
| JPMorgan Term Loan | Senior Secured | $30.0M | SOFR + 200 bps (7.42%) | Dec 2031 | Incurrence only |
| JPMorgan Revolver | Senior Secured | $0 | SOFR + 185 bps | Nov 2028 | Incurrence only |
| **Total Debt** | | **$30.0M** | | | |

- Term loan amortization: $3M/year (10% annually); balloon $21M at maturity
- Net leverage: 0.74x (total debt $30M / pro forma EBITDA $40.4M incl. Beacon)
- All-in cost of debt: 7.42% gross; 5.35% after-tax (28.4% effective rate)

<!-- Presenter notes: The debt portfolio is straightforward: one term loan ($30M) and an undrawn revolver. The term loan closed December 20, 2026 at SOFR plus 200 basis points, currently translating to 7.42% (3-month SOFR of 5.42% as of December 31). We secured incurrence-only covenants as the committee directed — there are no financial maintenance covenants in this facility. The only covenant restrictions that apply to ongoing operations are: we cannot incur additional debt above $20M without lender consent (does not apply given our current plans), we cannot pay dividends above 50% of trailing twelve-month FCF (our current $0.32 annual dividend represents approximately 12% of FCF — well within limit), and we cannot make acquisitions above $30M without lender notification. The revolver remains a $52M backup liquidity facility; we have not drawn on it and do not plan to. Both facilities are with JPMorgan, which is our primary relationship bank. The concentration of banking relationship with a single institution is a consideration: we are evaluating adding a second bank facility in 2027 as we grow beyond $200M in revenue. Net leverage of 0.74x on a pro forma basis is the first time we have carried debt in three years and represents a deliberate financing decision for the Beacon acquisition. Our target is to be below 0.5x by Q3 2027 through FCF paydown. The SOFR + 200 bps spread was the best rate we received across three competing term sheets. -->

---

# Investment Portfolio

<div class="label">Short-Term Investment Program</div>

| Instrument | Balance | Yield | Maturity | Credit Rating |
|---|---|---|---|---|
| US Treasury Bills (30-day) | $3.0M | 5.08% | Rolling 30-day | AAA / Government |
| US Treasury Bills (90-day) | $2.0M | 5.14% | March 31, 2027 | AAA / Government |
| Money Market Fund (JPMorgan) | $1.5M | 4.95% | Daily liquidity | AAA (fund rating) |
| **Total Investment Portfolio** | **$6.5M** | **Blended 5.07%** | | |

- Q4 2026 investment income: $82K (vs. $0 in Q4 2025 — new program initiated Q3 2026)
- FY 2026 investment income: $146K — incremental to operating income
- Policy compliance: All instruments rated AA or above; no single instrument &gt;$5M; all maturities &lt;90 days &#x2713;

<!-- Presenter notes: The investment program was initiated in Q3 2026 to generate yield on our cash balance above the $20M operating floor. In Q4, we expanded the program to $6.5M and added a 90-day T-bill tranche to capture slightly higher yield while maintaining overall portfolio liquidity. The blended yield of 5.07% on $6.5M generates approximately $330K annually in investment income — not transformative but meaningful and essentially risk-free. All investments comply with our Treasury Policy's investment guidelines: AA or above credit rating, maximum $5M per instrument, maximum 90-day tenor. The $2M in 90-day T-bills matures March 31, 2027 — we will decide at maturity whether to roll or deploy into debt paydown depending on the FCF trajectory and SOFR environment. If SOFR decreases materially (e.g., Fed cuts 50+ bps), we may accelerate term loan paydown with investment proceeds rather than rolling. The Money Market Fund provides daily liquidity and serves as our primary sweep vehicle for excess operating cash — any operating account balance above $3M at day-end sweeps into the MMF overnight. This automated sweep generated $23K in Q4 from intraday cash balances. I will recommend increasing the investment portfolio target from $6.5M to $8M in Q1 2027 once the Beacon acquisition closes and the cash rebuild trajectory is clear. This will require CFO approval per Treasury Policy. -->

---

# Counterparty Risk

<div class="label">Banking and Counterparty Exposure</div>

| Counterparty | Relationship | Exposure | Rating (S&amp;P) | Policy Limit | Status |
|---|---|---|---|---|---|
| JPMorgan Chase | Primary bank; term loan; revolver; escrow | $30M debt + $40M escrow | AA- | $75M | <span class="status-green">&#x25CF; Within policy</span> |
| US Treasury (T-bills) | Investment | $5.0M | AAA | No limit | <span class="status-green">&#x25CF; Within policy</span> |
| JPMorgan MMF | Cash sweep | $1.5M | AAA (fund) | $10M | <span class="status-green">&#x25CF; Within policy</span> |
| FX Forward Counterparty (BofA) | CAD hedge | $0.9M notional | A+ | $5M | <span class="status-green">&#x25CF; Within policy</span> |

- Primary concentration risk: JPMorgan relationship covers 72% of our banking exposure
- Mitigation: Diversification review planned for Q2 2027 post-Beacon integration

<!-- Presenter notes: Counterparty risk management is a core treasury function. The concentrated exposure to JPMorgan is the primary concern I want to flag for the committee's awareness — not as an immediate action item but as a medium-term planning point. 72% of our banking exposure (the $30M term loan, $52M revolver availability, $40M acquisition escrow, and primary operating accounts) rests with a single institution. In normal market conditions, JPMorgan's AA- credit rating and systemically important bank status make this an acceptable concentration. However, as we grow toward $200M+ in revenue and potentially carry more debt, diversifying our banking relationships to a primary and at least one secondary bank would be prudent risk management. I have initiated conversations with Wells Fargo Corporate Banking about a potential secondary revolver ($25–30M) for diversification purposes — not because we need the liquidity, but to reduce single-bank dependency. I will present a recommendation to the CFO in Q2 2027 on banking diversification. The BofA FX forward counterparty is appropriate — BofA is A+ rated and within our $5M per-counterparty limit for derivatives. We use BofA for FX rather than JPMorgan to avoid concentration and because BofA offered better forward pricing on CAD/USD for our specific tenor and notional. All counterparty exposures are within Treasury Policy limits; there are no exceptions to report. -->

---

# Covenant Status — Compliance Dashboard

<div class="label">Financial Covenant Monitoring — December 31, 2026</div>

| Covenant | Threshold | Actual | Cushion | Status |
|---|---|---|---|---|
| Minimum Liquidity | &gt; $15M | $22.1M | $7.1M (47%) | <span class="status-green">&#x25CF; Compliant</span> |
| Net Leverage (Debt/EBITDA) | &lt; 2.5x | 0.74x | 70% | <span class="status-green">&#x25CF; Compliant</span> |
| Interest Coverage (EBITDA/Interest) | &gt; 4.0x | 18.4x | 360% | <span class="status-green">&#x25CF; Compliant</span> |
| CapEx Limit | &lt; $10M/yr | $2.8M | $7.2M remaining | <span class="status-green">&#x25CF; Compliant</span> |
| Restricted Payment Test | &lt; 50% LTM FCF | $6.9M paid (35%) | $2.8M remaining | <span class="status-green">&#x25CF; Compliant</span> |

All 5 covenants compliant. No waiver requests pending. Q1 2027 compliance forecast: all green.

<!-- Presenter notes: All five covenant metrics are compliant as of December 31, 2026 and are forecast to remain compliant throughout Q1 2027. The tightest covenant is minimum liquidity at $22.1M versus the $15M floor — $7.1M of cushion (47%). This will be the tightest point in our forecast: post-Beacon close in January 2027, cash drops to approximately $21M, giving a $6M cushion. This is adequate but warrants close monitoring. I have set up a weekly liquidity report that automatically alerts the CFO and Treasurer when cash drops below $20M — this gives us a two-week warning buffer before approaching the floor. The interest coverage ratio of 18.4x is extremely comfortable and will remain well above the 4x floor even in stress scenarios. The restricted payment test covers dividends and share repurchases — $6.9M paid in 2026 (quarterly dividends of $6.3M + buybacks $0.6M) represents 35% of LTM FCF of $19.6M, within the 50% limit. For 2027, the dividend program continues at $0.32/share annually ($7.0M for 21.8M shares); combined with $6.1M remaining buyback authorization, total potential restricted payments are $13.1M versus a 50% covenant headroom of approximately $20M (50% of $40M pro forma FCF). We are comfortably within bounds. I run a monthly covenant compliance report and will flag any projections of covenant stress immediately — no issues are on the horizon. -->

---

# Treasury Initiatives — 2027 Plan

<div class="label">Priority Programs for the Coming Year</div>

- **Banking diversification** — Add secondary revolver at Wells Fargo ($25–30M) by Q2 2027; reduces JPMorgan concentration from 72% to approximately 45%
- **FX policy refresh** — Update Treasury Policy to address EUR exposure from Beacon EU client; add EUR and GBP monitoring thresholds; present to board in March
- **Term loan paydown** — Target $5M principal paydown by Q4 2027 from FCF (above mandatory $3M annual amortization); reduces net leverage to 0.55x
- **Investment program expansion** — Increase to $8M once post-Beacon cash rebuilds; evaluate adding 6-month T-bills for yield pickup if SOFR curve permits

<!-- Presenter notes: The four treasury initiatives for 2027 are logical extensions of the work completed in 2026 and responsive to the strategic changes from the Beacon acquisition. Banking diversification is the highest priority: the JPMorgan concentration is manageable today but will feel increasingly concentrated as we scale. Wells Fargo has been proactive in pursuing the secondary revolver relationship; their indicative terms are competitive with our JPMorgan facility. I will have a full recommendation with pricing and covenant comparison to the CFO by February 15. The FX policy refresh is triggered by the Beacon acquisition and the potential EUR exposure. Our current policy was written when our FX exposure was entirely theoretical — now we have $2.2M of actual FX exposure and the Beacon acquisition may add more. A policy update is overdue. I will circulate a draft to the CFO and General Counsel in February for board ratification at the March finance committee meeting. Term loan paydown above the mandatory amortization is a capital allocation decision that I am flagging as a treasury preference, subject to the CFO and board's capital allocation framework. Paying down $5M above the $3M mandatory gives us a lower net leverage of 0.55x by year-end 2027 and reduces annual interest by approximately $370K. This needs to be balanced against the buyback program and potential acquisition opportunities. Investment program expansion is the lowest-stakes initiative: adding $1.5M to the program once cash rebuilds generates approximately $80K in additional annual income at current yields. I will propose expanding the program in a routine memo to the CFO once Q2 cash levels are established. -->

---

<!-- _class: close -->

# Treasury Review Complete

**Four Recommended Actions**

1. Note all 5 covenants green; no action required on compliance
2. Approve banking diversification analysis — proceed to Wells Fargo term sheet
3. Note Q1 2027 liquidity floor cushion of ~$6M; confirm weekly alert protocol is active
4. Authorize FX policy refresh for March board presentation

Next Treasury Review: April 10, 2027 (Q1 2027 Post-Beacon-Close)

<!-- Presenter notes: This concludes the Q4 2026 Treasury Operations Review. Four recommended actions are presented for CFO acknowledgment. Action 1 is informational — all covenants are clean, no issues. Action 2 requires CFO direction to proceed with the Wells Fargo secondary revolver analysis; I need the CFO's authorization before approaching Wells Fargo formally, as establishing a new banking relationship involves certain relationship management considerations. Action 3 is a process acknowledgment — the weekly liquidity alert is already configured and active; I am asking the CFO to confirm that the $20M alert threshold is appropriate. Action 4 requires CFO direction to draft the FX policy update and schedule it for the March board finance committee. I recommend we present the FX policy refresh alongside the first post-acquisition treasury update, which naturally frames the need. The next treasury review will be held in April and will cover the first full quarter post-Beacon close, including: the integration of Beacon treasury functions into Northwind's structure, the full-year debt service schedule for the term loan, and the updated covenant projections for 2027. Are there questions on any section before we close? I have the full supporting data available for any line item the CFO wishes to drill into. Thank you. -->
