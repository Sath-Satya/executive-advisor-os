<!-- TEMPLATE: automation-roi
     CATEGORY: ROI / Business Case
     USE WHEN: automation initiative ROI pitch for process automation investment approval
     SLIDE COUNT: 10
     PALETTE: Dark dev
     RENDER: marp --pptx 70-automation-roi.md -->

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
    border-bottom: 2px solid var(--color-green);
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
    background: var(--color-green);
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
  .process-card {
    background: var(--color-surface);
    border-left: 3px solid var(--color-accent);
    padding: 12px 16px;
    border-radius: 4px;
    margin-bottom: 12px;
  }
  .process-metric { font-size: 1.2rem; font-weight: 700; color: var(--color-negative); }
  .stat-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 16px;
  }
  .stat-card {
    background: var(--color-surface);
    border-top: 3px solid var(--color-green);
    padding: 12px 14px;
    border-radius: 4px;
  }
  .stat-val { font-size: 1.6rem; font-weight: 700; }
  .stat-lbl { font-size: 0.78rem; color: var(--color-muted); margin-top: 4px; }
  .footer-note { font-size: 0.76rem; color: var(--color-muted); margin-top: 14px; }
---

<!-- _paginate: false -->
# Meridian Health — Prior Authorisation<br>Automation ROI Pitch

<div class="cover-sub">Process Automation Investment Case — Operations Committee</div>
<div class="cover-sub">April 2026 &nbsp;|&nbsp; Prepared by: SponAItech LLC &nbsp;|&nbsp; Confidential</div>

<!--
PRESENTER NOTES — Slide 1: Title

This deck makes the case for automating Meridian Health's prior authorisation (PA) process — the workflow through which providers request approval for specific procedures, medications, or referrals before delivering care. Meridian processes 38,000 PA requests per month. Today, 94% require a human clinical reviewer or administrative staff member to touch the request at least once. The automation case is based on three value drivers: labor savings from reduced manual review, quality improvements from faster turnaround (reducing member complaints and provider abrasion), and regulatory compliance (CMS's PA rule requires electronic processing by January 2027). This is both a financial ROI case and a compliance obligation. The committee needs to approve a $2.1M automation investment.
-->

---

# The Process Today — 38,000 Requests, 94% Manual

<div class="label">Current Process</div>

<div class="process-card">
  <strong>Step 1 — Receipt:</strong> Provider submits PA via fax (62%), portal (31%), or phone (7%)
  <div class="process-metric">14 staff FTEs handle receipt and triage. Average: 18 minutes per request</div>
</div>

<div class="process-card">
  <strong>Step 2 — Clinical Review:</strong> 54% of requests require clinical reviewer assessment against coverage criteria
  <div class="process-metric">28 clinical reviewer FTEs. Average: 47 minutes per reviewed request</div>
</div>

<div class="process-card">
  <strong>Step 3 — Decision and Communication:</strong> Decision communicated to provider via fax, phone, or portal
  <div class="process-metric">Average end-to-end cycle time: 3.8 days. CMS target: same day</div>
</div>

<!--
PRESENTER NOTES — Slide 2: Current Process

Map the process step by step before proposing changes. This makes the automation opportunity concrete. The 62% fax intake is particularly striking to modern audiences — fax is the dominant PA intake channel in US healthcare despite being a 40-year-old technology. The 18-minute per-request receipt and triage time reflects the manual work required to extract data from unstructured fax documents: provider NPI, member ID, procedure code, supporting clinical documentation. The 47-minute clinical review time per reviewed request reflects the complexity of matching procedure criteria against coverage policy. The 3.8-day average cycle time is the most damaging metric: CMS's new PA rule requires same-day or next-day decisions for urgent requests and 7-day decisions for non-urgent — Meridian's current 3.8-day average fails the urgent threshold.
-->

---

# Pain Points — Four Reasons This Must Change

<div class="label">Pain Points</div>

- **Member harm risk:** 3.8-day PA cycle delays care. CMS studies link PA delays to 12% higher hospitalization rates for deferred care — a clinical and liability exposure
- **Provider abrasion:** 71% of providers rated Meridian's PA process as "difficult or very difficult" in the Q4 2025 provider satisfaction survey — a key factor in network attrition
- **Regulatory exposure:** CMS PA Interoperability Rule (effective January 1, 2027) requires electronic PA processing. Meridian's current fax-dominant process is non-compliant — potential CMS penalty: $10K per violation per day
- **Staff burnout:** PA staff voluntary turnover reached 34% in 2025 — nearly double the healthcare industry average of 18%. Replacement cost per PA staff member: $42K

<!--
PRESENTER NOTES — Slide 3: Pain Points

The four pain points are arranged in order of stakeholder impact: clinical (member harm), commercial (provider network), regulatory (CMS compliance), and operational (staff turnover). Present the clinical risk first — it is the most important in a healthcare context. The 12% higher hospitalisation rate from deferred care is a published CMS finding, not a Meridian estimate. The provider satisfaction score of 71% rating Meridian's PA as "difficult" is from Meridian's own survey — it is already known to leadership, but naming it in this context connects provider abrasion to a solvable process problem. The CMS compliance deadline is the hardest urgency driver: January 1, 2027 is 9 months away. A $10K per-violation-per-day penalty is real — and with 38,000 PA requests per month, the potential penalty exposure is enormous. The staff turnover cost at $42K per hire × 34% turnover = approximately $600K per year in replacement costs for the 42-person PA team.
-->

---

# Proposed Automation — Three Automation Layers

<div class="label">Solution Design</div>

- **Layer 1 — Intelligent Document Intake:** AI-powered OCR and NLP converts fax documents to structured data in <30 seconds. Eliminates 14 FTE receipt and triage role over 12 months
- **Layer 2 — Rules-Based Auto-Decision:** 58% of PA requests meet straightforward coverage criteria (standard procedures, in-network providers, no contraindications). Auto-approve in <2 minutes with zero clinical reviewer involvement
- **Layer 3 — AI-Assisted Clinical Review:** For the remaining 42% requiring clinical judgment, an AI assistant pre-populates the review form, flags relevant coverage criteria, and suggests a decision with evidence links — reducing review time from 47 to 18 minutes per request

**Post-automation cycle time target: <span class="positive">4 hours</span> (from 3.8 days)**

<!--
PRESENTER NOTES — Slide 4: Solution Design

The three-layer architecture is important to present clearly because different stakeholders have different concerns about automation in healthcare. Emphasise that Layer 2 (auto-decision) applies only to "straightforward" requests — defined as: standard CPT code, in-network provider, member has active coverage, no prior denials for same procedure in last 12 months, no high-alert drug interaction flag. These are the PA equivalent of rubber-stamp approvals that currently consume significant clinical reviewer time because the criteria are checked manually, one by one. The AI-assisted clinical review in Layer 3 is not replacing the clinical reviewer — it is eliminating the data preparation work that currently consumes 20 of the 47 minutes per review. Clinical judgment for medically complex requests is preserved. The 4-hour cycle time target reflects: Layer 1 real-time, Layer 2 2-minute auto-decision, Layer 3 18-minute assisted review with same-day routing.
-->

---

# Cost of Automation — $2.1M Investment

<div class="label">Investment Required</div>

| Component | Cost | Description |
|---|---|---|
| Intelligent document intake (OCR/NLP) | $480K | Azure AI Document Intelligence, NLP pipeline, fax-to-API gateway |
| Rules engine (auto-decision layer) | $360K | Coverage criteria DSL, PA decision workflow, audit trail |
| AI clinical review assistant | $520K | Clinical AI model integration, UI, HITL approval workflow |
| Integration (CMS PA API, EMR) | $380K | HL7 FHIR PA API, Epic and Cerner integration |
| Testing, validation, UAT | $180K | Clinical staff UAT, regulatory compliance testing |
| Training and change management | $100K | 42 PA staff + 28 clinical reviewers |
| Contingency (10%) | $80K | |
| **Total** | **<span class="negative">$2,100K</span>** | |

<!--
PRESENTER NOTES — Slide 5: Investment Required

The $2.1M investment is structured across six components. The largest single item is the AI clinical review assistant at $520K — this is the highest-value component because it serves 28 clinical reviewers who each handle the most complex and time-intensive PA requests. The integration cost of $380K reflects the complexity of connecting to both the CMS FHIR PA API (required for regulatory compliance) and Meridian's EMR vendors (Epic and Cerner). This integration work must be completed regardless of the automation scope — it is the compliance obligation. The OCR/NLP intake component at $480K uses Azure AI Document Intelligence for the fax conversion — SponAItech has a pre-built connector for this that reduces the custom development scope significantly. The rules engine at $360K uses the same DSL framework as the ClaimsAI platform, reducing licensing and development costs through reuse.
-->

---

# Labor Savings — $5.8M Annual Benefit

<div class="label">Labor Savings</div>

| Role Group | Current FTEs | Post-Automation FTEs | Reduction | Annual Saving |
|---|---|---|---|---|
| PA receipt and triage (Layer 1) | 14 | 4 | 10 FTE | <span class="positive">$1.12M</span> |
| Clinical reviewers (Layer 2+3) | 28 | 16 | 12 FTE | <span class="positive">$2.16M</span> |
| PA communication / follow-up | 8 | 3 | 5 FTE | <span class="positive">$0.56M</span> |
| Staff turnover cost reduction | — | — | (-34% to -12%) | <span class="positive">$0.63M</span> |
| Overtime elimination | — | — | — | <span class="positive">$0.38M</span> |
| **Total Annual Labor Saving** | | | **27 FTE** | **<span class="positive">$4.85M</span>** |

<div class="footer-note">FTE reductions achieved through attrition over 18 months — no forced layoffs. Loaded FTE cost = $112K average (clinical: $155K, admin: $72K). Staff turnover cost reduction based on turnover falling from 34% to 12% target.</div>

<!--
PRESENTER NOTES — Slide 6: Labor Savings

The labor savings are the largest financial benefit at $4.85M per year. The 27 FTE reduction is achieved through attrition — the 34% voluntary turnover rate means that 14 of the 42 PA staff will naturally depart in the next 12 months. The automation replaces the need to backfill those departures, rather than eliminating existing employees. The clinical reviewer reduction from 28 to 16 FTEs is more gradual — over 18 months as the auto-decision layer proves its accuracy (currently targeting 97%+ decision accuracy, monitored by the HITL audit layer). The staff turnover cost reduction from 34% to 12% is a projection based on comparable PA automation implementations: staff satisfaction improves significantly when manual data-entry work is replaced by higher-value clinical judgment tasks. The $0.63M saving reflects 6 fewer replacement hires per year at $42K each plus training ramp-up costs.
-->

---

# Quality and Speed Gains — Beyond Labor

<div class="label">Non-Labor Benefits</div>

<div class="stat-row">
  <div class="stat-card">
    <div class="stat-val positive">4 hrs</div>
    <div class="stat-lbl">PA cycle time (from 3.8 days)</div>
  </div>
  <div class="stat-card">
    <div class="stat-val positive">-68%</div>
    <div class="stat-lbl">Provider complaint rate</div>
  </div>
  <div class="stat-card">
    <div class="stat-val positive">$0</div>
    <div class="stat-lbl">CMS compliance penalty exposure</div>
  </div>
</div>

**Quantified non-labor benefits:**

- CMS penalty avoidance (non-compliance risk): <span class="positive">$0.62M/yr</span> (estimated avoided fines)
- Provider network retention (reduced PA friction): <span class="positive">$0.33M/yr</span> (modelled from churn reduction)
- **Total non-labor annual benefit: <span class="positive">$0.95M</span>**

**Total annual benefit (labor + quality): <span class="positive">$5.8M</span>**

<!--
PRESENTER NOTES — Slide 7: Non-Labor Benefits

Quality and speed gains are often under-quantified in automation ROI cases. This slide assigns dollar values to three non-labor benefits. The CMS compliance penalty avoidance is the most concrete: the PA Interoperability Rule carries a $10K per violation per day penalty. With 38,000 PA requests per month and assuming 40% non-compliant (those currently processed by fax without FHIR API routing), the potential daily penalty exposure is $3.8M. We model only 5 violations per month ($50K) as the realistic enforcement scenario — giving $0.62M per year in avoided fines. This is a conservative estimate; CMS enforcement has been increasingly aggressive. The provider network retention benefit is modelled from the relationship between PA friction scores and provider panel departure rates — a 10-point improvement in provider satisfaction score (from the current 71% "difficult" rating to a target 80% "easy" rating) is correlated with a 0.8% reduction in annual panel attrition, valued at $330K in retained provider relationships.
-->

---

# Payback — Investment Recovered in 5 Months

<div class="label">Payback Analysis</div>

| Metric | Value |
|---|---|
| Total investment | <span class="negative">$2.1M</span> |
| Annual benefit (steady state) | <span class="positive">$5.8M</span> |
| Monthly benefit (steady state) | <span class="positive">$483K</span> |
| Go-live month | Month 8 (November 2026) |
| Payback from go-live | <span class="positive">4.3 months</span> |
| Payback from project start | <span class="positive">12 months</span> |
| 3-year cumulative net return | <span class="positive">$12.1M</span> |
| 5-year NPV (8% discount) | <span class="positive">$15.4M</span> |
| Benefit-cost ratio | <span class="positive">7.3x</span> |

<!--
PRESENTER NOTES — Slide 8: Payback

The payback numbers are exceptional because the investment is modest relative to the benefit. At $483K per month in steady-state savings, the $2.1M investment is recovered in 4.3 months after go-live. From project start (including the 8-month implementation period), total payback is 12 months. The 3-year cumulative net return of $12.1M represents a 5.8x return on the $2.1M investment. The 5-year NPV of $15.4M is calculated at 8% discount rate using the annual benefit of $5.8M less $0.2M annual support cost. The 7.3x benefit-cost ratio means that for every dollar invested in this automation programme, $7.30 of value is returned — one of the strongest ROI ratios in any healthcare IT investment category. The compliance driver (CMS January 2027 deadline) means this analysis understates the true ROI: without the investment, penalty risk alone could consume the equivalent of 35% of the annual benefit.
-->

---

# Risks — Addressed and Mitigated

<div class="label">Risk Register</div>

| Risk | Assessment | Mitigation |
|---|---|---|
| Clinical decision accuracy below 97% | Medium likelihood, High impact | HITL oversight maintained for 90 days; rollback to manual if <95% |
| CMS FHIR API integration delay | Low likelihood, Medium impact | API spec finalized; Epic/Cerner have pre-certified connectors |
| Provider adoption of digital PA channel | Medium likelihood, Low impact | Fax gateway remains; digital portal is additive, not replacement |
| Regulatory interpretation changes | Low likelihood, Medium impact | Rules engine updateable in <24 hours; compliance team on retainer |
| Clinical staff resistance | Medium likelihood, Medium impact | Change management workstream; clinical champions identified |

<!--
PRESENTER NOTES — Slide 9: Risks

The most significant risk is clinical decision accuracy — if the auto-decision layer makes incorrect determinations, the consequences are clinical (members denied appropriate care) and regulatory (CMS compliance risk from incorrect denials). The mitigation is rigorous: a 90-day HITL oversight period where every auto-decision is independently reviewed by a clinical reviewer before being communicated to the provider. Only once 30 consecutive days show 97%+ accuracy does the system advance to unsupervised operation. A 95% accuracy threshold triggers a return to supervised mode. This conservative approach adds cost (the 28 clinical reviewers are not reduced until the supervised period completes) but eliminates the clinical risk. The Epic/Cerner pre-certified connector point is important: Epic and Cerner both offer CMS FHIR PA API connectors that are already certified. SponAItech is not building this integration from scratch — it is configuring existing certified connectors, reducing integration risk significantly.
-->

---

# Rollout — Eight-Month Path to Live

<div class="label">Rollout Plan and Ask</div>

| Month | Milestone | Deliverable |
|---|---|---|
| 1–2 | Foundation | Azure environment, FHIR API connection, fax-to-API gateway live |
| 3–4 | Rules engine | Auto-decision layer deployed; clinical champion review begins |
| 5–6 | AI review assistant | Clinical reviewer UI deployed; staff training complete |
| 7 | Parallel run | All three layers operating with HITL oversight; accuracy monitoring |
| 8 | Go-live | Supervised production mode; CMS compliance achieved |

**The ask:**
- Approve $2.1M automation investment — Operations Committee
- Appoint Clinical Champion (VP Medical Management) as steering sponsor
- Commit to January 2027 CMS FHIR compliance deadline — automation is the only path

<!--
PRESENTER NOTES — Slide 10: Rollout and Ask

The 8-month rollout is ambitious but achievable because the technology components are proven — Azure AI Document Intelligence, the ClaimsAI rules DSL, and the FHIR PA API connectors are all production-ready. The custom work is integration and configuration, not invention. The CMS compliance point is the strongest closing argument: by January 1, 2027, electronic PA processing is mandatory. Without this investment, Meridian has no compliant path. The only alternative is a manual workaround that adds staff and still risks CMS penalties. The automation investment simultaneously solves the compliance obligation and delivers $5.8M in annual ROI. The three specific asks are clean: money, a named sponsor, and a deadline commitment. Ask for all three today. Note that the January 2027 CMS deadline is 9 months from April 2026 — the 8-month rollout fits with zero buffer. Approving today means Meridian hits the deadline. Waiting 30 days means Meridian is 30 days late.
-->
