<!-- TEMPLATE: investment-committee
     CATEGORY: ROI / Business Case
     USE WHEN: IC-style investment memo deck for private equity or venture investment decisions
     SLIDE COUNT: 12
     PALETTE: Dark premium
     RENDER: marp --pptx 67-investment-committee.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --color-bg: #0a0e14;
    --color-surface: #111820;
    --color-fg: #ffffff;
    --color-accent: #3b9eff;
    --color-purple: #a78bfa;
    --color-positive: #2dd4a0;
    --color-negative: #f06070;
    --color-neutral: #f0a050;
    --color-muted: #8899ac;
    --color-border: #1e2d40;
  }
  section {
    background: var(--color-bg);
    color: var(--color-fg);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 46px 60px;
  }
  h1 {
    color: var(--color-fg);
    font-size: 1.85rem;
    font-weight: 700;
    letter-spacing: -0.4px;
    border-bottom: 2px solid var(--color-accent);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  h2 {
    color: var(--color-accent);
    font-size: 0.95rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    margin-bottom: 10px;
  }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 9px; font-size: 0.98rem; line-height: 1.5; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    margin-top: 12px;
  }
  th {
    background: var(--color-surface);
    color: var(--color-accent);
    padding: 8px 12px;
    text-align: left;
    border-bottom: 1px solid var(--color-border);
    font-size: 0.82rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }
  td {
    padding: 7px 12px;
    border-bottom: 1px solid var(--color-border);
    color: var(--color-fg);
  }
  tr:nth-child(even) td { background: #0d1520; }
  .positive { color: var(--color-positive); font-weight: 700; }
  .negative { color: var(--color-negative); font-weight: 700; }
  .neutral  { color: var(--color-neutral);  font-weight: 700; }
  .label {
    display: inline-block;
    background: var(--color-accent);
    color: #000;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 4px;
    margin-bottom: 14px;
  }
  .label-purple {
    display: inline-block;
    background: var(--color-purple);
    color: #fff;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 4px;
    margin-bottom: 14px;
  }
  .cover-sub { font-size: 1.0rem; color: var(--color-muted); margin-top: 10px; }
  .thesis-card {
    background: var(--color-surface);
    border-left: 4px solid var(--color-accent);
    padding: 14px 20px;
    margin-top: 14px;
    border-radius: 4px;
  }
  .metric-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-top: 16px;
  }
  .metric {
    background: var(--color-surface);
    border-top: 3px solid var(--color-accent);
    padding: 12px 14px;
    border-radius: 4px;
  }
  .metric-val { font-size: 1.5rem; font-weight: 700; }
  .metric-lbl { font-size: 0.78rem; color: var(--color-muted); margin-top: 4px; }
  .verdict-go {
    background: #0d2018;
    border: 1px solid var(--color-positive);
    border-radius: 6px;
    padding: 14px 20px;
    margin-top: 14px;
    text-align: center;
    color: var(--color-positive);
    font-weight: 700;
    font-size: 1.2rem;
  }
  .footer-note { font-size: 0.76rem; color: var(--color-muted); margin-top: 14px; }
---

<!-- _paginate: false -->
# Northwind PE<br>Series Investment — Investment Committee Memo

<div class="cover-sub">Confidential — For IC Use Only &nbsp;|&nbsp; April 2026</div>
<div class="cover-sub">Deal Team: SponAItech Advisory &nbsp;|&nbsp; Target: [Company Name Redacted]</div>
<div class="cover-sub">Investment Size: $8.5M &nbsp;|&nbsp; Series A Lead</div>

<!--
PRESENTER NOTES — Slide 1: Title

This is the IC memo deck for Northwind Private Equity's proposed $8.5M Series A lead investment in a B2B SaaS target operating in the mid-market healthcare technology space. The memo format follows Northwind's standard IC process: Opportunity, Thesis, Market, Business, Financials, Returns, Risks, Diligence, Terms, Recommendation, Conditions, Decision. All financial projections are derived from the target's audited financials (FY 2024, FY 2025) and management forecasts validated by the Northwind deal team. Legal and tax diligence is complete. The deal team recommends approval with three closing conditions. This presentation is for IC members only; do not distribute externally.
-->

---

# Opportunity — Why This Deal, Why Now

<div class="label">Opportunity</div>

- Target is a **Series A SaaS company** serving mid-market healthcare payers — a segment underserved by both enterprise incumbents and early-stage point solutions
- **ARR of $4.8M** growing at 68% YoY; net revenue retention of **124%**
- Operating in the **$18B US claims adjudication software market**, growing at 14% CAGR driven by value-based care mandates
- **Window of opportunity:** two PE-backed competitors have just raised Series C rounds; the target's category leadership position is at risk without growth capital within 6–12 months
- Deal sourced by Northwind's healthcare technology network — no auction; **proprietary deal**

<!--
PRESENTER NOTES — Slide 2: Opportunity

Lead with why Northwind should care about this deal above others. The 68% ARR growth and 124% net revenue retention are exceptional by any benchmark — the target is not just growing, it is expanding revenue within its existing customer base. The $18B market with 14% CAGR provides the underlying growth tailwind. The window-of-opportunity framing is genuine: two better-funded competitors are scaling GTM teams right now. The proprietary sourcing is a key quality signal — this is not a broadly marketed deal, which means Northwind has pricing power in the term sheet negotiation. Use this slide to establish urgency and conviction before the IC members have had time to ask "why this target?"
-->

---

# Investment Thesis — Three Value Creation Levers

<div class="label">Thesis</div>

<div class="thesis-card">
  <strong>Lever 1 — GTM Acceleration:</strong> Target currently closes deals through founder-led sales. $3M of the investment funds a VP of Sales hire + 4 AEs. Based on comparable Series A SaaS deals, this team configuration generates $6–8M in incremental ARR within 18 months at 2x+ pipeline coverage.
</div>

<div class="thesis-card">
  <strong>Lever 2 — Product Expansion:</strong> Denial management module is 70% built; $2M completes development and enables upsell to existing 38 customers. Average contract value increases from $126K to $210K — a 67% ACV expansion.
</div>

<div class="thesis-card">
  <strong>Lever 3 — Series B Positioning:</strong> With $12M+ ARR and denial management launched, target reaches Series B qualification criteria within 24 months. Northwind's preferred entry at Series A enables 2.5–4x multiple expansion at the B round.
</div>

<!--
PRESENTER NOTES — Slide 3: Thesis

Three levers is the right number — more becomes a laundry list, fewer feels under-thought. Each lever is quantified where possible. The GTM lever is benchmarked against comparable Series A SaaS deals — the 2x pipeline coverage assumption is conservative; top performers achieve 3–4x. The product expansion lever is compelling because the denial management module is already 70% complete — this is not greenfield R&D risk, it is finishing an asset that exists. The 67% ACV expansion assumption is validated by the target's existing customers who have informally expressed interest in the module. The Series B positioning lever connects this investment to Northwind's expected exit: the target needs to reach $12M+ ARR for a Series B at 8–10x ARR multiple, which is the entry point for the fund's return targets.
-->

---

# Market — $18B and Growing

<div class="label">Market Sizing</div>

| Segment | 2025 TAM | 2030 TAM | CAGR |
|---|---|---|---|
| Claims adjudication software (all payers) | $18.0B | $35.4B | 14.5% |
| Mid-market payer segment (100–5,000 lives admin.) | $4.2B | $8.8B | 16.0% |
| Target's addressable segment (denial management + STP) | $1.8B | $4.1B | 17.9% |
| Target's current market share | 0.27% | — | — |

**Market tailwinds:**
- CMS value-based care mandates accelerating payer technology investment
- Prior authorisation reform (H.R. 3591) creates compliance automation demand
- Legacy adjudication platforms (average age: 14 years) due for replacement cycle

<!--
PRESENTER NOTES — Slide 4: Market

The market sizing table shows the TAM hierarchy: total claims adjudication software market, the mid-market payer segment Northwind's target specifically addresses, and the target's direct addressable segment in denial management and STP automation. The 0.27% current market share highlights the enormous runway — the target doesn't need to be the market leader to generate exceptional returns; it needs to grow from 0.27% to 1–2% of its addressable segment. The three market tailwinds are important: they explain why now is the right time to invest rather than waiting for the market to develop. The H.R. 3591 prior authorisation reform is a specific regulatory driver that creates a compliance automation opportunity — the target's rules engine is purpose-built to accommodate these changes.
-->

---

# Business — Unit Economics and Key Metrics

<div class="label">Business Quality</div>

<div class="metric-row">
  <div class="metric">
    <div class="metric-val positive">$4.8M</div>
    <div class="metric-lbl">ARR (April 2026)</div>
  </div>
  <div class="metric">
    <div class="metric-val positive">68%</div>
    <div class="metric-lbl">YoY ARR Growth</div>
  </div>
  <div class="metric">
    <div class="metric-val positive">124%</div>
    <div class="metric-lbl">Net Revenue Retention</div>
  </div>
  <div class="metric">
    <div class="metric-val neutral">$126K</div>
    <div class="metric-lbl">Average Contract Value</div>
  </div>
</div>

| Metric | Value | Benchmark |
|---|---|---|
| Gross margin | <span class="positive">78%</span> | SaaS benchmark: 70–80% — on target |
| CAC payback period | <span class="neutral">19 months</span> | SaaS benchmark: <18 months — slight miss |
| LTV:CAC ratio | <span class="positive">4.8x</span> | SaaS benchmark: >3x — strong |
| Churn (logo) | <span class="positive">2.1%</span> | SaaS benchmark: <5% — excellent |

<!--
PRESENTER NOTES — Slide 5: Business Metrics

This is the business quality assessment. The headline metrics are strong: 68% ARR growth, 124% NRR, 2.1% logo churn. These are top-quartile metrics for a Series A SaaS company. The 78% gross margin confirms the software economics — this is not a services-heavy business. The one area of concern is the 19-month CAC payback — slightly above the 18-month benchmark. The root cause is the founder-led sales model: the founders are efficient at closing but cannot scale. The GTM investment (Lever 1) directly addresses this by adding dedicated AEs who should reduce CAC payback to 14–16 months. The 4.8x LTV:CAC is healthy and validates the unit economics at current CAC levels. The 2.1% annual logo churn is excellent — it implies customers stay for an average of 47 years, which is a reflection of high switching cost and genuine product value.
-->

---

# Financials — Three-Year Projections

<div class="label">Financial Model</div>

| Metric | FY 2025 (Actual) | FY 2026 (Est.) | FY 2027 (Proj.) | FY 2028 (Proj.) |
|---|---|---|---|---|
| ARR | $2.86M | $4.80M | $9.20M | $16.8M |
| Revenue | $2.6M | $4.3M | $8.4M | $15.7M |
| Gross profit | $2.0M | $3.4M | $6.6M | $12.2M |
| EBITDA | <span class="negative">($1.8M)</span> | <span class="negative">($3.2M)</span> | <span class="negative">($4.1M)</span> | <span class="positive">$1.6M</span> |
| Cash burn (monthly) | $150K | $267K | $342K | — |
| Implied runway (post-investment) | — | 31 months | — | — |

<div class="footer-note">FY 2025 audited by Deloitte. FY 2026–2028 management forecast reviewed and risk-adjusted by Northwind deal team. $8.5M investment provides 31 months of runway at projected burn rates.</div>

<!--
PRESENTER NOTES — Slide 6: Financials

The financial model shows the classic high-growth SaaS pattern: accelerating ARR, deepening losses through the investment period, turning EBITDA-positive in FY 2028 as the GTM team becomes productive and the denial management module adds high-margin ARR. The ARR growth trajectory (68% to 92% to 83%) reflects the GTM investment kicking in from Q3 2026 onwards. The FY 2027 EBITDA loss of $4.1M is the peak burn year — the GTM team is fully ramped but the AE productivity ramp (typically 6–9 months) has not yet fully materialised. By FY 2028, the target reaches $16.8M ARR with positive EBITDA. The 31-month runway post-investment provides ample time to reach Series B qualification without distressed fundraising. Deloitte audits the historical financials; the deal team has stress-tested the forward projections at 20% and 35% below management's assumptions.
-->

---

# Returns — Three Scenarios

<div class="label">Return Analysis</div>

| Scenario | Assumption | Exit ARR | Exit Multiple | Exit Value | Northwind Return (2.5x dilution) |
|---|---|---|---|---|---|
| Bear | 40% below model, exit in 5 years | $9.8M | 6x | $58.8M | <span class="neutral">2.1x MOIC / 16% IRR</span> |
| Base | Model as presented, exit in 4 years | $16.8M | 8x | $134.4M | <span class="positive">4.3x MOIC / 44% IRR</span> |
| Bull | 20% above model, strategic acquisition | $21.0M | 12x | $252.0M | <span class="positive">7.8x MOIC / 68% IRR</span> |

Northwind's ownership post-Series A: **18.5%** (pre-dilution) &nbsp;|&nbsp; Investment: **$8.5M** &nbsp;|&nbsp; Post-money valuation: **$46M**

<!--
PRESENTER NOTES — Slide 7: Returns

The returns table models three scenarios. In the bear case — ARR 40% below model, delayed exit at 5 years — Northwind still generates a 2.1x MOIC and 16% IRR. The 16% IRR in the downside case exceeds the fund's 12% preferred return threshold. The base case of 4.3x MOIC / 44% IRR is the deal team's central estimate; it assumes an 8x ARR exit multiple, which is conservative for a high-NRR healthcare SaaS business (comparable exits have achieved 10–14x). The bull case of 7.8x MOIC / 68% IRR assumes a strategic acquirer — likely a major EHR or payer services company — pays a premium for the technology. The $46M post-money valuation implies a 9.6x forward ARR multiple on the FY 2026 estimated ARR, which is within the range of recent comparable Series A deals.
-->

---

# Key Risks — Identified and Assessed

<div class="label">Risk Register</div>

| Risk | Severity | Probability | Mitigation |
|---|---|---|---|
| GTM execution fails to scale | High | Medium | Hire VP Sales before close; Northwind board seat for GTM oversight |
| Denial management module delayed | Medium | Low | 70% complete; milestone-based $2M tranche |
| Competitor funding accelerates | High | High | Speed to market; 18-month product advantage |
| Key-person dependency (CEO) | High | Low | Retention package; 4-year vest with 1-year cliff |
| Regulatory change (CMS rule changes) | Medium | Low | Rules engine architecture supports rapid rule updates |
| Down-round risk if Series B market softens | Medium | Medium | 31-month runway provides bridge; EBITDA breakeven by FY 2028 |

<!--
PRESENTER NOTES — Slide 8: Key Risks

The deal team's honest risk assessment. The most material risk is GTM execution — founder-led sales to a professional GTM team is one of the highest-failure transitions in early-stage SaaS. The mitigation is contractual: Northwind's term sheet requires the VP of Sales hire to be agreed by both parties before close, and Northwind receives a board seat specifically to provide GTM oversight. The competitor funding risk is assessed as high probability — two Series C competitors are already funded. The mitigation is speed: the $3M GTM tranche deploys immediately, and the target has an 18-month product advantage in the denial management module. The down-round risk is mitigated by the 31-month runway — the target does not need to raise Series B under duress. An EBITDA breakeven by FY 2028 provides an alternative path if Series B markets remain challenged.
-->

---

# Diligence — Findings Summary

<div class="label">Due Diligence</div>

| Workstream | Status | Key Finding |
|---|---|---|
| Financial audit (Deloitte) | Complete | FY 2025 ARR confirmed at $2.86M; no material adjustments |
| Legal and IP (Gunderson) | Complete | IP fully assigned; no third-party claims; HIPAA compliance verified |
| Technical (SponAItech) | Complete | Architecture sound; denial management 70% complete; 3 technical debt items noted |
| Customer references (8 interviews) | Complete | NPS: 72; primary churn risk: integration complexity for smaller payers |
| Management assessment | Complete | CEO and CTO strong; sales leadership gap confirmed — addressable with VP hire |
| Market (Gartner primary research) | Complete | Market sizing confirmed; target ranked #2 in NPS among 11 competitors evaluated |

<!--
PRESENTER NOTES — Slide 9: Diligence

Diligence is complete across all six workstreams — this deal is ready to close. The most important finding is the Deloitte ARR confirmation: the $2.86M FY 2025 ARR was independently verified, which eliminates the most common Series A risk — revenue recognition manipulation. The Gunderson IP work confirmed clean ownership — critical for a SaaS company whose primary asset is its software. SponAItech's technical review flagged three technical debt items: a legacy authentication module, outdated API versioning, and incomplete unit test coverage. None are material to the business, and all are scheduled for remediation in the 12-month product roadmap. The 8 customer reference interviews produced an NPS of 72, which is top-quartile for enterprise SaaS. The integration complexity issue for smaller payers is a known limitation — it is the primary reason the target focuses on mid-market rather than SMB.
-->

---

# Terms — Proposed Term Sheet

<div class="label">Term Sheet Summary</div>

| Term | Proposed |
|---|---|
| Investment amount | $8.5M |
| Security type | Series A Preferred |
| Pre-money valuation | $37.5M |
| Post-money valuation | $46.0M |
| Northwind ownership (post-money) | 18.5% |
| Liquidation preference | 1x non-participating |
| Anti-dilution | Weighted average broad-based |
| Board composition | 5 seats: 2 founders, 1 Northwind, 2 independent |
| Pro-rata rights | Yes — up to $3M in future rounds |
| Information rights | Standard monthly + quarterly |
| Closing conditions | 3 (see next slide) |

<!--
PRESENTER NOTES — Slide 10: Terms

The term sheet is market-standard for a Series A of this size and stage. The $37.5M pre-money valuation implies a 7.8x forward ARR multiple on FY 2026 estimated ARR — within the range for comparable deals. The 1x non-participating liquidation preference is clean and founder-friendly; it signals Northwind's confidence in the equity outcome. The weighted average broad-based anti-dilution protects Northwind in a down-round scenario without creating punitive dilution for the founders. The 5-seat board with 2 independents creates governance balance — Northwind gets its oversight seat without majority control. The $3M pro-rata right is important: it allows Northwind to maintain ownership percentage through the Series B round without committing to a specific amount today.
-->

---

# Recommendation — Approve with Conditions

<div class="label">Recommendation</div>

<div class="verdict-go">DEAL TEAM RECOMMENDATION: APPROVE — Subject to 3 Conditions</div>

**Closing Conditions:**
1. **VP Sales hire agreed** — candidate identified and reference-checked before wire transfer; Northwind co-approves the hire decision
2. **Denial management milestone tranche** — $2M of the $8.5M held in escrow, released upon denial management module GA (expected Q4 2026); prevents capital deployment to non-performing workstream
3. **HIPAA Business Associate Agreement** — executed with all 38 existing customers before close; Gunderson confirms 34 of 38 executed; 4 outstanding

<div class="footer-note">Deal team confidence: High. Primary risk is GTM execution, mitigated by closing condition 1. Financial projections stress-tested at 35% below management forecast; base case returns remain above fund threshold in that scenario.</div>

<!--
PRESENTER NOTES — Slide 11: Recommendation

The recommendation is clear and bounded: approve, subject to three specific conditions. Each condition is directly tied to a risk identified in the diligence. Condition 1 addresses the GTM execution risk — no wire until the VP Sales hire is co-approved. Condition 2 converts the denial management module from an assumption to a contingency: $2M is held in escrow until the module ships, eliminating the risk of capital deployment before the asset is verified. Condition 3 is a legal/compliance hygiene item — 4 customers have not executed updated BAAs under HIPAA. These must be in place before close. All three conditions are achievable within 30 days. The deal team expects to close by May 30, 2026.
-->

---

# Decision — Required from IC Today

<div class="label">Decision Required</div>

**IC is asked to:**

1. Approve the $8.5M Series A investment in the target company
2. Approve the proposed term sheet as presented
3. Confirm the three closing conditions as sufficient
4. Authorize the deal team to execute the term sheet and proceed to close

**Timeline to close:** 30 days from IC approval (May 30, 2026 target)

**What happens if Northwind declines:** The target is likely to receive a competing term sheet from [Firm A] within 30 days. At their proposed valuation ($42M pre-money), the deal represents inferior returns at comparable risk. Northwind's proprietary access expires with this IC cycle.

<!--
PRESENTER NOTES — Slide 12: Decision

The IC needs four specific approvals — be explicit. The timeline to close is 30 days, which is achievable given diligence completion. The "what if Northwind declines" section is not a threat — it is honest context. The deal team has intelligence that a competing term sheet is likely from a known competitor. At $42M pre-money (vs. Northwind's $37.5M), the competing terms are less attractive but could be accepted if Northwind declines. The proprietary nature of this deal sourcing is Northwind's key advantage; it expires once the target broadens the process. The IC should make a binary decision today: invest on these terms, or pass and accept that the opportunity will close to Northwind.
-->
