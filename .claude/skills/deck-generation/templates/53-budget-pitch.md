<!-- TEMPLATE: budget-pitch
     CATEGORY: Finance
     USE WHEN: pitching a budget request to the CFO or finance committee
     SLIDE COUNT: 9
     PALETTE: Corporate hybrid (cream + navy + gold)
     RENDER: marp --pptx 53-budget-pitch.md -->

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
    --amber: #d97706;
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
    padding-bottom: 8px; margin-bottom: 20px;
  }
  h2 { font-size: 1.2rem; font-weight: 600; color: var(--gold); margin-bottom: 12px; }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 9px; font-size: 1.0rem; line-height: 1.5; }
  table { width: 100%; border-collapse: collapse; font-size: 0.90rem; margin-top: 10px; }
  th { background: var(--navy); color: var(--cream); padding: 7px 11px; text-align: left; }
  td { padding: 6px 11px; border-bottom: 1px solid var(--rule); }
  tr:nth-child(even) td { background: #ede9e0; }
  .label {
    display: inline-block; background: var(--gold); color: var(--cream);
    font-size: 0.70rem; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; padding: 2px 9px; border-radius: 3px; margin-bottom: 10px;
  }
  .ask-box {
    background: var(--navy); color: var(--cream); border-radius: 10px;
    padding: 24px 32px; margin-top: 16px;
  }
  .ask-box .total { font-size: 2.2rem; font-weight: 700; color: var(--gold); }
  .ask-box .desc { font-size: 0.88rem; color: #a0b0c0; margin-top: 6px; }
  .pill {
    display: inline-block; border-radius: 4px; padding: 2px 10px;
    font-size: 0.78rem; font-weight: 700; margin-left: 6px;
  }
  .pill-green { background: #d4edda; color: var(--green); }
  .pill-red { background: #fde8e8; color: var(--red); }
  .pill-amber { background: #fef3cd; color: var(--amber); }
  section.cover { background: var(--navy); color: var(--cream); display: flex; flex-direction: column; justify-content: center; }
  section.cover h1 { color: var(--cream); border-color: var(--gold); font-size: 2.1rem; }
  section.cover .sub { color: var(--gold); font-size: 1.0rem; margin-top: 8px; }
  section.cover .meta { color: #8899ac; font-size: 0.85rem; margin-top: 20px; }
  section.decision { background: var(--navy); color: var(--cream); display: flex; flex-direction: column; justify-content: center; }
  section.decision h1 { color: var(--gold); border: none; font-size: 1.9rem; }
  section.decision ul li { color: #c0cfd8; }
---

<!-- _class: cover -->

<div class="label">Budget Request — FY 2027</div>

# Capital Markets Technology Platform — Budget Request

<div class="sub">Requesting $2.8M for CRM and Deal Management Modernization</div>
<div class="meta">Presented to: Sarah Kim, CFO &nbsp;|&nbsp; August 15, 2026 &nbsp;|&nbsp; Submitted by: Michael Torres, CIO</div>

<!-- Presenter notes: This presentation is a formal budget request for the Capital Markets Technology Platform modernization, submitted by the CIO to the CFO for inclusion in the FY 2027 Annual Operating Plan. The request totals $2.8M over two years: $1.8M in FY 2027 (the primary ask today) and $1.0M in FY 2028 for phase two functionality and ongoing licensing. This investment has been in planning since Q1 2026; preliminary discovery and vendor evaluation have been completed. Today's objective is to receive CFO approval to include this item in the FY 2027 budget submission to the board. The presentation follows our standard budget request format: current state → ask → breakdown → ROI → alternatives → risks → phasing → decision. I will walk through each section and invite questions as we go. Decision is requested by August 22 to meet the budget submission deadline. -->

---

# Current State — The Problem We Are Solving

<div class="label">Why We Need to Act Now</div>

- **System fragmentation:** Advisors use 3 separate tools (legacy CRM, Excel pipeline, email) with no integration — 4.2 hours/week lost per advisor on manual reconciliation
- **Pipeline blindness:** Leadership has no real-time view of deal status; reports are produced 3 days after month-end from manual data pulls
- **Revenue leakage:** Post-mortem analysis of 2025 deals identified $1.4M in fees billed late or at reduced rates due to tracking errors
- **Competitive disadvantage:** Peer firms average 14% advisor productivity premium; we are at parity with the market from 3 years ago

Current systems are 6–9 years old with no vendor support path beyond 2027.

<!-- Presenter notes: The current state diagnosis is based on a 90-day internal assessment completed in Q2 2026, conducted by IT in partnership with the Capital Markets division. Key findings: first, the time burden on advisors is material — 4.2 hours per week per advisor (across 22 advisors) represents 4,800 hours annually or approximately 2.3 full-time equivalents of productivity lost to administrative overhead. Second, pipeline reporting relies on a manual consolidation process that takes 3 business days to produce, meaning leadership is always operating on stale data. Third, the revenue leakage finding of $1.4M is particularly alarming — this was identified through a reconciliation of engagement letters against invoices issued, revealing systematic underbilling on amendment fees and success-fee calculations. Fourth, our peer benchmarking shows that competitors using modern deal management platforms achieve 12–16% higher advisor productivity as measured by revenue per advisor — Northwind is currently at $2.15M revenue per advisor, versus a peer median of $2.40M. The legacy systems are on Microsoft Dynamics 2016 (EOL in 2028) and a custom-built pipeline tracker on SharePoint 2019. -->

---

# The Ask — Summary of Request

<div class="label">FY 2027 Budget Request</div>

<div class="ask-box">
  <div class="total">$1.8M — FY 2027 Investment Ask</div>
  <div class="desc">Salesforce Financial Services Cloud + Dealogic Integration + Implementation + Training</div>
</div>

| Component | FY 2027 | FY 2028 | Total |
|---|---|---|---|
| Platform Licenses (Salesforce FSC) | $480K | $480K | $960K |
| Implementation &amp; Configuration | $840K | $280K | $1,120K |
| Integration (Dealogic, Bloomberg) | $320K | $160K | $480K |
| Training &amp; Change Management | $160K | $80K | $240K |
| **Total** | **$1.8M** | **$1.0M** | **$2.8M** |

Full-year benefit begins Q2 2027 following Q1 2027 go-live.

<!-- Presenter notes: The $1.8M FY 2027 ask breaks down into four components. Platform licenses represent the Salesforce Financial Services Cloud enterprise agreement — we have negotiated a 3-year term at $480K per year (list price is $620K; we achieved a 23% discount through our existing Salesforce relationship for the Wealth Management CRM). Implementation and configuration is the largest line: $840K in FY 2027 covers the Salesforce implementation partner (we have received three competitive bids; the recommended vendor is Accenture at $840K, versus Deloitte at $920K and a boutique firm at $710K — we recommend Accenture for implementation quality despite the premium). Integration costs cover the Dealogic deal database and Bloomberg terminal feeds, which will provide real-time market data within the deal management workflow. Training and change management is essential — peer implementations have shown that inadequate training is the primary cause of adoption failures. We have budgeted 40 hours per advisor plus management dashboards training. FY 2028 costs represent year-two licensing and phase two functionality (advanced analytics, AI-assisted pipeline forecasting). -->

---

# ROI Justification

<div class="label">Return on Investment Analysis</div>

| Benefit Category | Annual Value | Confidence | Notes |
|---|---|---|---|
| Advisor productivity recovery | $880K | High | 4.2 hrs/week &#215; 22 advisors &#215; $190/hr blended rate |
| Revenue leakage prevention | $1.4M | Medium-High | Based on 2025 post-mortem; assumes 90% prevention |
| Faster pipeline reporting | $120K | Medium | Value of 3-day reporting lead time (management time saved) |
| **Total Annual Benefit** | **$2.4M** | | |

- **Payback period:** 14 months from go-live (Q2 2027 → Q4 2028)
- **3-year NPV** (10% discount rate): **+$3.2M**
- **IRR:** 68%

Comparable Salesforce FSC implementations at peer firms have delivered 15–25% advisor productivity lift within 12 months of go-live.

<!-- Presenter notes: The ROI analysis is conservative by design. We have only included benefits where we have quantitative evidence, and we have applied a confidence discount to each category. Advisor productivity: the 4.2 hour/week figure comes from time studies conducted in April 2026 — 18 of 22 advisors participated. We have valued this time at the blended advisor rate of $190/hour, which is conservative relative to revenue-per-hour of approximately $310/hour. If advisors redirect this time to revenue-generating activities (as peer implementations show they do), the upside is substantially larger. Revenue leakage prevention: the $1.4M identified in 2025 represents our baseline assumption for prevention. We have applied a 10% haircut to account for the possibility that some leakage recurs despite the new system. Faster reporting: the $120K represents CFO and COO time currently spent in monthly reconciliation sessions that will be eliminated. We have not included the value of better decisions from faster data, which is real but unquantifiable. The 14-month payback is from Q2 2027 (first full month of go-live) to Q4 2028 when cumulative benefits exceed cumulative costs. NPV calculated on net incremental cash flows including implementation costs, annual licenses, and annual benefits. The 68% IRR is substantially above our 10% WACC, making this among the highest-returning IT investments in our portfolio. -->

---

# Alternatives Considered

<div class="label">Options Analysis</div>

| Option | Cost | Pros | Cons | Recommendation |
|---|---|---|---|---|
| Do nothing | $0 upfront | No change management | Revenue leakage continues; EOL risk 2028 | <span class="pill pill-red">Rejected</span> |
| Upgrade legacy (Dynamics 2024) | $0.9M total | Lower cost | Does not solve integration or reporting gaps; short runway | <span class="pill pill-red">Rejected</span> |
| Build in-house | $1.2M est. | Customizable | 18-month build; ongoing maintenance burden; execution risk | <span class="pill pill-red">Rejected</span> |
| Salesforce FSC (recommended) | $2.8M total | Full integration; proven at peers; vendor-supported | Highest upfront cost | <span class="pill pill-green">Recommended</span> |

<!-- Presenter notes: We evaluated four options before settling on Salesforce FSC as the recommendation. Do nothing was analyzed first as the baseline — it has zero upfront cost but perpetuates $1.4M annual revenue leakage and creates a hard deadline risk in 2028 when Microsoft ends support for Dynamics 2016. The cost of do-nothing over a 3-year horizon is actually higher than the investment when leakage and forced migration costs are included. Upgrading to Dynamics 2024 was the next option — it would resolve the EOL issue but does not solve pipeline integration (Dealogic integration for Dynamics is not supported) and would require another migration in 3–4 years. Build in-house was seriously considered by our IT team; the attraction is full customization. We rejected it for three reasons: 18-month timeline is too long given our 2028 EOL pressure, we do not have in-house Salesforce/CRM engineering expertise and would need to hire, and ongoing maintenance burden is significant. Salesforce FSC was selected because it is the proven platform in our competitive set (4 of our 7 closest competitors are on FSC), it has native integration with Dealogic and Bloomberg, and the vendor relationship with Salesforce is already established through our Wealth Management CRM. -->

---

# Risks If Not Funded

<div class="label">Cost of Inaction</div>

- **Revenue leakage continues:** $1.4M/year in systematic underbilling — identifiable, preventable, directly bottom-line
- **System EOL — hard deadline:** Microsoft Dynamics 2016 support ends December 2027; migration will be required regardless, but unplanned is 40–60% more costly
- **Advisor attrition risk:** In Q1 2026 exit interviews, 3 of 4 departing senior advisors cited "poor tools" as a dissatisfier; replacing one senior advisor costs $180K–$240K in recruiting and onboarding
- **Competitive gap widens:** Peers are investing; every year of delay is compounding technology debt and productivity disadvantage

<!-- Presenter notes: The risks of inaction are concrete and quantifiable, which distinguishes this from a typical technology investment. The revenue leakage is the most important risk — $1.4M annually is not a projection, it is a historical fact from 2025. We expect similar leakage in 2026 and 2027 if we do nothing. On the EOL deadline: regardless of the CFO's decision today, we will be forced to migrate off Dynamics 2016 by December 2027. An unplanned emergency migration typically costs 40–60% more than a planned one and carries significant business disruption risk. The advisor attrition risk is newer intelligence from our Head of Talent — the exit interview data suggests that tooling quality is a material factor in retention of senior advisors. Replacing a senior advisor with 10+ years of client relationships is extremely expensive and often results in permanent relationship loss. The competitive gap point is difficult to quantify but real — if our peers are 14% more productive per advisor and we continue to fall further behind, it will eventually manifest in market share loss on competitive mandates. This investment is not optional in the medium term; the question is only whether to do it on our timeline or be forced into it. -->

---

# Phasing Plan

<div class="label">Implementation Timeline</div>

| Phase | Period | Scope | Investment |
|---|---|---|---|
| Phase 0 — Foundation | Q4 2026 | Vendor contracting, data migration planning, project team | $120K (FY 2026) |
| Phase 1 — Core Platform | Q1 2027 | CRM configuration, Salesforce FSC go-live, basic pipeline module | $980K |
| Phase 2 — Integration | Q2 2027 | Dealogic + Bloomberg feeds, automated reporting, dashboards | $700K |
| Phase 3 — Advanced | Q3–Q4 2027 | AI forecasting, mobile app, full reporting suite | $0 (FY 2027 included) |
| Phase 4 — Optimization | FY 2028 | Advanced analytics, Phase 2 enhancements | $1.0M |

- Go-live Q1 2027; first full month of benefit: February 2027
- Phase 0 funded from FY 2026 IT budget reserve ($120K available)

<!-- Presenter notes: The phasing plan is designed to deliver value quickly while managing implementation risk. Phase 0 begins in Q4 2026 and is funded from existing IT budget reserves — this does not require new budget approval and allows us to begin vendor contracting, data migration planning, and project team formation before the FY 2027 budget year starts. This is critical: if we wait until January 2027 to start, we push go-live to Q2 2027 and lose one full quarter of benefits. Phase 1 is the core platform go-live: Salesforce FSC configured for our business and the basic pipeline module operational. At this point, advisors have a single system and leadership has real-time pipeline visibility. Phase 2 adds the integrations that drive the revenue leakage prevention — automated fee calculations from Dealogic deal data and Bloomberg market data will eliminate the manual reconciliation that caused 2025 underbilling. Phase 3 completes the advanced functionality including the AI-assisted pipeline forecasting module. The FY 2027 ask of $1.8M covers Phases 1, 2, and 3. The phasing approach also allows us to pause after Phase 1 if implementation challenges arise, which provides a natural risk gate. We recommend a Phase 1 go/no-go review with the CFO in March 2027 before proceeding to Phase 2. -->

---

<!-- _class: decision -->

# Decision Requested by August 22

<div class="label">Requested Actions</div>

- **Approve** inclusion of $1.8M in FY 2027 Capital IT budget for Salesforce FSC platform
- **Authorize** Phase 0 spend of $120K from FY 2026 IT reserve (existing budget — no new approval needed)
- **Designate** executive sponsor from CFO or CRO office for steering committee

**Decision timeline:** August 22 to meet budget submission deadline for October board review.

<!-- Presenter notes: We are requesting three specific actions. First, CFO approval to include the $1.8M in the FY 2027 capital IT budget. This will go into the AOP submission to the board in October 2026. If approved by the CFO, it does not require a separate board approval as it falls within management's delegated capital authorization threshold of $5M per project. Second, authorization for Phase 0 spend of $120K from the FY 2026 IT reserve. This reserve exists precisely for pre-approved project initiation activities and does not require additional CFO approval — we are flagging it for transparency. Third, we need an executive sponsor for the steering committee. The implementation will span three divisions (IT, Capital Markets, Finance) and requires executive-level decision-making authority on scope trade-offs. The CIO is requesting that either the CFO or CRO serve as executive sponsor. The August 22 deadline is firm — missing it means the project is deferred to the FY 2028 budget cycle and we incur one additional year of revenue leakage ($1.4M) and move closer to the Dynamics EOL emergency. Are there questions before we discuss the decision? -->

---

# Appendix — Vendor Scorecard

<div class="label">Competitive Evaluation</div>

| Criterion | Weight | Salesforce FSC | Dynamics 2024 | In-House |
|---|---|---|---|---|
| Integration capability | 30% | 95 | 62 | 75 |
| Implementation timeline | 20% | 85 | 88 | 40 |
| Total cost of ownership | 20% | 70 | 85 | 72 |
| Peer adoption / references | 15% | 92 | 58 | N/A |
| Vendor support quality | 15% | 88 | 74 | N/A |
| **Weighted Score** | | **86.1** | **72.3** | **N/A** |

Salesforce FSC evaluation included three reference calls with peer firms; full evaluation report available upon request.

<!-- Presenter notes: The vendor scorecard summarizes the formal evaluation process conducted over 8 weeks in Q2 2026. Salesforce FSC scored highest overall with a weighted score of 86.1 out of 100, driven by its superior integration capability (particularly the native Dealogic connector, which saves approximately $120K in custom development) and strong peer adoption in our competitive set. The integration capability criterion carries the highest weight at 30% because it is the primary driver of the revenue leakage prevention benefit. If we cannot integrate deal data from Dealogic in real time, we cannot automate fee calculations and the revenue leakage risk remains. Dynamics 2024 scored better on implementation timeline (slightly faster given our existing Dynamics familiarity) and total cost of ownership (lower 3-year cost before benefits), but significantly worse on integration and peer adoption. The in-house option was not fully scored because the in-house build timeline and maintenance burden made it non-competitive after Phase 1 analysis. Full reference call notes, vendor proposals, and the evaluation committee's detailed report are available to the CFO upon request. We are confident in the Salesforce FSC recommendation. -->
