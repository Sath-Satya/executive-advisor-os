<!-- TEMPLATE: migration-roi
     CATEGORY: ROI / Business Case
     USE WHEN: legacy-to-modern migration investment with ROI justification
     SLIDE COUNT: 10
     PALETTE: Dark dev
     RENDER: marp --pptx 69-migration-roi.md -->

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
    --color-green: #2dd4a0;
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
    font-size: 1.9rem;
    font-weight: 700;
    letter-spacing: -0.4px;
    border-bottom: 2px solid var(--color-accent);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  h2 {
    color: var(--color-green);
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
    font-size: 0.87rem;
    margin-top: 12px;
  }
  th {
    background: var(--color-surface);
    color: var(--color-green);
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
  .cover-sub { font-size: 1.0rem; color: var(--color-muted); margin-top: 10px; }
  .cost-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-top: 16px;
  }
  .cost-card {
    background: var(--color-surface);
    border-left: 3px solid var(--color-negative);
    padding: 12px 16px;
    border-radius: 4px;
  }
  .cost-card-pos {
    background: var(--color-surface);
    border-left: 3px solid var(--color-positive);
    padding: 12px 16px;
    border-radius: 4px;
  }
  .cost-val { font-size: 1.4rem; font-weight: 700; }
  .cost-lbl { font-size: 0.82rem; color: var(--color-muted); margin-top: 4px; }
  .footer-note { font-size: 0.76rem; color: var(--color-muted); margin-top: 14px; }
---

<!-- _paginate: false -->
# Meridian Health — Claims Platform<br>Legacy Migration ROI

<div class="cover-sub">Mainframe-to-Cloud Migration — Investment Case</div>
<div class="cover-sub">Technology Capital Committee — April 2026 &nbsp;|&nbsp; SponAItech LLC</div>

<!--
PRESENTER NOTES — Slide 1: Title

This deck presents the ROI case for migrating Meridian Health's claims processing infrastructure from a 22-year-old mainframe system (IBM zSeries running COBOL-based claims adjudication) to a modern cloud-native platform on Azure. The business context: Meridian's claims mainframe is at end-of-support from IBM in December 2027 — a hard deadline that makes this a mandatory investment, not a discretionary one. The ROI analysis therefore focuses not on whether to migrate, but on the financial benefit of migrating now versus waiting to the hard deadline. Migrating in 2026 rather than 2027 captures 14 months of additional operating cost savings. This deck is for the Technology Capital Committee which must approve the $6.8M migration investment.
-->

---

# Current Cost — The Mainframe Burden

<div class="label">Current State</div>

<div class="cost-grid">
  <div class="cost-card">
    <div class="cost-val negative">$4.2M</div>
    <div class="cost-lbl">Annual IBM mainframe support and maintenance</div>
  </div>
  <div class="cost-card">
    <div class="cost-val negative">$1.8M</div>
    <div class="cost-lbl">COBOL developer costs (6 FTEs, scarce talent)</div>
  </div>
  <div class="cost-card">
    <div class="cost-val negative">$0.9M</div>
    <div class="cost-lbl">Third-party MIPS licensing and capacity fees</div>
  </div>
  <div class="cost-card">
    <div class="cost-val negative">$0.6M</div>
    <div class="cost-lbl">DR/BCP infrastructure (separate IBM DR site)</div>
  </div>
</div>

**Total annual legacy cost: <span class="negative">$7.5M</span>**<br>
<div class="footer-note">IBM end-of-support deadline: December 31, 2027. Post-deadline support requires extended support contract at 2.5x current annual fee ($10.5M/yr).</div>

<!--
PRESENTER NOTES — Slide 2: Current Cost

The $7.5M annual mainframe cost is the baseline from which migration savings are calculated. Walk through each component. The $4.2M IBM support fee is the largest item — this covers hardware maintenance, software support, and the annual mainframe license renewal. The $1.8M COBOL developer cost reflects 6 FTEs at an average loaded rate of $300K — COBOL talent commands a significant premium because fewer than 2% of new computer science graduates have COBOL training. The $0.9M MIPS licensing fee scales with transaction volume; Meridian's 1.4M monthly claims require significant compute capacity. The DR/BCP cost of $0.6M covers a separate IBM DR site in a colocation facility — a cost that disappears when the workload moves to Azure. The critical urgency point: IBM's end-of-support deadline in December 2027 would impose an extended support surcharge of 2.5x — from $4.2M to $10.5M per year. That single cost increase justifies the migration investment on its own.
-->

---

# Limitations — What the Mainframe Cannot Do

<div class="label">Platform Limitations</div>

- **No API-first architecture** — integrating new capabilities (AI adjudication, mobile, provider portal) requires expensive middleware and COBOL batch adapters. Average integration project cost: $380K and 8 months
- **No real-time processing** — batch architecture processes claims in 4-hour windows. Real-time adjudication (required by CMS fast-track mandate by 2028) is not achievable on the current platform
- **No cloud elasticity** — fixed MIPS capacity means Meridian over-provisions for peak periods (January, open enrollment) while paying full cost during low-volume months
- **Skills shortage** — 2 of 6 COBOL developers plan to retire within 18 months. Replacement hiring takes 6–9 months and costs $180K in recruiting fees per hire

<!--
PRESENTER NOTES — Slide 3: Limitations

The mainframe limitation argument is often more persuasive than the pure cost argument, because it connects to strategic capability gaps that leaders can viscerally understand. The API limitation is the most immediately painful — every time Meridian wants to add a new capability (AI adjudication, member portal, provider integration), it requires a costly COBOL adapter project. The real-time processing gap is a regulatory risk: CMS's proposed prior authorisation rule (H.R. 3591) requires real-time adjudication for certain claim types by 2028. The mainframe's batch architecture cannot meet this requirement without a fundamental re-architecture — which is effectively a migration anyway. The COBOL skills shortage is an existential risk: losing two of six COBOL developers would leave Meridian with inadequate capacity to maintain the current system, let alone enhance it.
-->

---

# Proposed Migration — Azure Claims Platform

<div class="label">Target State</div>

- **Target platform:** Azure Kubernetes Service (AKS) with microservices claims architecture
- **Claims engine:** SponAItech ClaimsAI (already approved in Phase 1) — extended to replace COBOL adjudication logic
- **Database:** Azure SQL Managed Instance (replacing IBM Db2) with Azure Cosmos DB for real-time event processing
- **Integration:** Azure API Management — replaces COBOL batch adapters with standard REST APIs
- **DR/BCP:** Azure paired regions (East US + West US) — eliminates dedicated DR site; Azure SLA: 99.99%

**Post-migration annual cost: <span class="positive">$1.9M</span>** (75% reduction from $7.5M)

<!--
PRESENTER NOTES — Slide 4: Proposed Migration

The target state leverages the ClaimsAI platform already approved in the Phase 1 business case — this is not a new vendor relationship. The COBOL adjudication logic is being translated into the ClaimsAI rules engine, not rewritten from scratch. SponAItech has completed a COBOL code analysis: 68% of the 2.2 million lines of COBOL represent adjudication rules that are directly expressible in the ClaimsAI rules DSL. The remaining 32% represents infrastructure code (file I/O, batch job control, error handling) that is replaced by Azure platform services. This significantly reduces migration risk compared to a greenfield rewrite. The $1.9M post-migration annual cost breaks down as: $1.1M Azure infrastructure and licences, $0.6M 4 cloud-native developers (replacing 6 COBOL FTEs through attrition), and $0.2M SponAItech annual support.
-->

---

# Migration Cost — What the Transition Requires

<div class="label">Migration Investment</div>

| Cost Component | Amount | Notes |
|---|---|---|
| COBOL analysis and rules extraction | $0.8M | SponAItech fixed-fee; 2.2M LOC mapped |
| Azure platform setup and configuration | $1.2M | AKS, SQL MI, API Management, monitoring |
| Data migration (28 years of claims history) | $1.4M | Incremental migration over 18 months |
| ClaimsAI extension for COBOL replacement | $0.9M | Rules DSL translation; 68% automated |
| Testing and validation (parallel run) | $0.8M | 6-month parallel operation with mainframe |
| Change management and training | $0.4M | Cloud developers onboarding, team retraining |
| Contingency (15%) | $1.0M | Migration projects warrant higher contingency |
| **Total Migration Investment** | **<span class="negative">$6.5M</span>** | |

<!--
PRESENTER NOTES — Slide 5: Migration Cost

The $6.5M migration investment is substantial but well-justified against the $7.5M annual legacy cost. Walk through each component. The COBOL analysis at $0.8M is the first phase of work — before writing a line of Azure code, the full COBOL codebase must be analysed and the business rules extracted. SponAItech's proprietary COBOL analysis tooling automates 70% of this work, enabling a fixed-fee engagement. The data migration at $1.4M is the longest component — 28 years of claims history (approximately 400 million records) must be migrated to Azure SQL MI. The incremental migration approach moves historical data in batches over 18 months while the production system continues to operate on the mainframe. The parallel run at $0.8M covers 6 months of running both systems simultaneously for validation — this is the highest-confidence approach to zero-risk cutover. The 15% contingency ($1.0M) is higher than the standard 8% because migration projects have historically underestimated scope.
-->

---

# Post-Migration Cost — 75% Reduction

<div class="label">Future State Cost</div>

| Cost Category | Current Annual | Post-Migration Annual | Saving |
|---|---|---|---|
| Infrastructure support (IBM → Azure) | <span class="negative">$4.2M</span> | <span class="positive">$1.1M</span> | <span class="positive">$3.1M</span> |
| Developer costs (COBOL → cloud-native) | <span class="negative">$1.8M</span> | <span class="positive">$0.6M</span> | <span class="positive">$1.2M</span> |
| MIPS licensing | <span class="negative">$0.9M</span> | <span class="positive">$0</span> | <span class="positive">$0.9M</span> |
| DR/BCP infrastructure | <span class="negative">$0.6M</span> | <span class="positive">$0.2M</span> | <span class="positive">$0.4M</span> |
| **Total** | **<span class="negative">$7.5M</span>** | **<span class="positive">$1.9M</span>** | **<span class="positive">$5.6M</span>** |

<div class="footer-note">Azure infrastructure cost includes compute, storage, networking, and Azure Monitor. DR/BCP cost post-migration = Azure paired-region replication at $200K/yr vs. $600K/yr dedicated site.</div>

<!--
PRESENTER NOTES — Slide 6: Post-Migration Cost

The post-migration cost table shows the full financial benefit. The $5.6M annual saving is a 75% reduction in infrastructure operating cost. The most dramatic saving is the IBM infrastructure cost — from $4.2M to $1.1M. This reflects the fundamental economics of cloud-native versus mainframe: Azure AKS scales to zero during low-volume periods, whereas the mainframe requires constant MIPS capacity allocation regardless of utilisation. The developer cost reduction from $1.8M to $0.6M reflects a reduction from 6 COBOL FTEs to 4 cloud-native developers — 2 FTEs are not replaced, achieved through voluntary retirement of the 2 developers already planning to leave. The 4 remaining COBOL developers will be retrained on Azure and Python over 12 months (training cost included in the migration investment). The MIPS licensing elimination is total — Azure charges for actual compute consumed, not reserved capacity.
-->

---

# Net Savings — $5.6M Per Year After Migration

<div class="label">ROI Summary</div>

| Year | Investment | Annual Saving | Net Cash Flow | Cumulative |
|---|---|---|---|---|
| Year 0 | <span class="negative">($6.5M)</span> | — | <span class="negative">($6.5M)</span> | <span class="negative">($6.5M)</span> |
| Year 1 (partial) | <span class="negative">($0.2M)</span> | <span class="positive">$2.8M</span> | <span class="positive">$2.6M</span> | <span class="negative">($3.9M)</span> |
| Year 2 | <span class="negative">($0.2M)</span> | <span class="positive">$5.6M</span> | <span class="positive">$5.4M</span> | <span class="positive">$1.5M</span> |
| Year 3 | <span class="negative">($0.2M)</span> | <span class="positive">$5.8M</span> | <span class="positive">$5.6M</span> | <span class="positive">$7.1M</span> |
| Year 4 | <span class="negative">($0.2M)</span> | <span class="positive">$6.0M</span> | <span class="positive">$5.8M</span> | <span class="positive">$12.9M</span> |
| Year 5 | <span class="negative">($0.2M)</span> | <span class="positive">$6.2M</span> | <span class="positive">$6.0M</span> | <span class="positive">$18.9M</span> |

**NPV (8% discount, 5 years): <span class="positive">$13.6M</span> &nbsp;|&nbsp; Payback: 20 months**

<!--
PRESENTER NOTES — Slide 7: ROI Summary

The cash flow table shows the investment recovery timeline. Year 0 is the $6.5M migration investment. Year 1 shows partial savings of $2.8M — reflecting a mid-year cutover (target: June 2027), so only 6 months of full savings accrue. By Year 2, full $5.6M annual savings are in force. Cumulative cash flow turns positive in Year 2 (Month 20 from project start). The 5-year NPV of $13.6M at an 8% discount rate represents exceptional value for a mandatory infrastructure replacement — this is not a discretionary investment, and even the mandatory version generates a 2.1x present-value return. Savings grow 3% per year post-Year 2 due to COBOL talent inflation: replacing the 2 COBOL developers who retire would cost $600K each in the open market; cloud developers are $200K. The salary differential grows each year.
-->

---

# Risks — Migration-Specific Concerns

<div class="label">Risk Register</div>

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Data migration error (28-year history) | Low | High | Incremental migration with reconciliation gates; parallel run validation |
| COBOL translation incomplete | Medium | High | 70% automated; 30% manual review; parallel run catches gaps |
| Timeline overrun (18-month plan) | Medium | Medium | 15% contingency built in; IBM hard deadline provides external pressure |
| Talent loss (COBOL developers mid-migration) | Medium | High | Retention bonus for 18-month period; SponAItech COBOL SME backup |
| Azure cost overrun | Low | Low | Azure cost management alerts; SponAItech FinOps governance |
| Business disruption at cutover | Low | High | Zero-downtime cutover via blue-green deployment; 90-day rollback window |

<!--
PRESENTER NOTES — Slide 8: Risks

Migration projects fail most often due to three factors: data quality issues, incomplete business logic translation, and talent departure mid-project. All three are addressed in the risk register. The data migration risk is mitigated by the incremental approach — moving claims history in monthly batches with automated reconciliation, rather than a big-bang cutover. The COBOL translation risk is partially automated — SponAItech's tooling handles 70% of the translation, reducing the manual surface area where errors occur. The 30% requiring manual review is the highest-risk work and is sequenced first, before the automated portion, to surface issues early. The talent retention risk is real: COBOL developers know their skills are in demand and may seek other opportunities during the 18-month migration. The $180K retention bonus pool (included in migration budget) is structured as monthly payments through cutover, creating a financial incentive to stay. The blue-green deployment approach means cutover is instantaneous and reversible: both the mainframe and cloud platform run in parallel until the cloud platform is certified, then traffic is switched. A 90-day rollback window is maintained.
-->

---

# Timeline — 18-Month Migration Roadmap

<div class="label">Implementation Timeline</div>

| Phase | Months | Key Milestones |
|---|---|---|
| Phase 0 — Preparation | 1–2 | COBOL analysis complete, Azure environment provisioned, team assembled |
| Phase 1 — Foundation | 3–6 | Data model mapped, first 8 claim types migrated, parallel run begins |
| Phase 2 — Core Migration | 7–12 | All 47 claim types migrated, COBOL rules translated, regression testing |
| Phase 3 — Validation | 13–16 | 4-month parallel run, reconciliation clean, performance benchmarking |
| Phase 4 — Cutover | 17–18 | Blue-green cutover, mainframe decommission, DR validation |

**Hard deadline: December 31, 2027 (IBM end-of-support)**<br>
Target cutover: **June 2027** — provides 6-month buffer before hard deadline

<!--
PRESENTER NOTES — Slide 9: Timeline

The 18-month timeline is designed with a 6-month buffer before the IBM hard deadline. This buffer is intentional — migration projects rarely run exactly to plan, and having 6 months of buffer before the December 2027 deadline means a 3-month delay (not uncommon) still delivers before deadline. Phase 0 is often underestimated: the COBOL analysis and Azure environment setup must be complete before any migration work begins. SponAItech has a dedicated COBOL analysis team that can complete Phase 0 within 8 weeks. Phase 3's 4-month parallel run is the most expensive phase in terms of operational overhead — running two production systems simultaneously — but it is the most important for risk mitigation. The reconciliation clean milestone means that claim counts, financial totals, and adjudication decisions in Azure match the mainframe to within the acceptable variance threshold (0.01% dollar variance).
-->

---

# Phasing and Ask — Approve to Beat the Deadline

<div class="label">Decision Required</div>

- Approve $6.5M migration investment (includes 15% contingency)
- Authorise SponAItech as prime migration vendor — Phase 0 kickoff within 10 business days
- Establish Migration Steering Committee (CIO, CFO, VP Claims, SponAItech PM) — first meeting by May 15

**What happens without approval today:**

- Each month of delay compresses the buffer against the December 2027 IBM deadline
- A 3-month delay pushes cutover to September 2027 — 3-month buffer only; too tight
- If Meridian misses the hard deadline: IBM extended support surcharges $10.5M/yr vs. $4.2M today — a $6.3M annual penalty that exceeds the migration cost in Year 1 alone
- **Net migration saving over 5 years: $18.9M cumulative &nbsp;|&nbsp; NPV: $13.6M**

<!--
PRESENTER NOTES — Slide 10: The Ask

The closing argument is unusually strong because this is a mandatory investment with a hard external deadline. The IBM end-of-support deadline is not negotiable — it is a contractual reality. Framing the migration as "optional" is incorrect; the choice is: migrate now at $6.5M, or migrate under crisis conditions in 2027 at higher cost and risk, while paying $6.3M per year in extended support surcharges. The 10-business-day kickoff window enables SponAItech to start the COBOL analysis before the end of April, completing Phase 0 by June 2026. Each week of delay in Phase 0 directly compresses the buffer. The $13.6M NPV and $18.9M cumulative 5-year saving frame the investment as value creation, not just cost avoidance. Ask for three specific approvals — investment, vendor, and steering committee — and request a decision today.
-->
