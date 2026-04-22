<!-- TEMPLATE: tco-deck
     CATEGORY: ROI / Business Case
     USE WHEN: comparing total cost of ownership across vendor or technology options
     SLIDE COUNT: 9
     PALETTE: Corporate hybrid (cream bg, gold/blue accents)
     RENDER: marp --pptx 62-tco-deck.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --color-bg: #f7f4ef;
    --color-fg: #0e1b2e;
    --color-accent: #3b9eff;
    --color-gold: #b8965a;
    --color-positive: #2d6a4f;
    --color-negative: #b91c1c;
    --color-neutral: #b8965a;
    --color-muted: #5a6677;
  }
  section {
    background: var(--color-bg);
    color: var(--color-fg);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 64px;
  }
  h1 {
    color: var(--color-fg);
    font-size: 1.9rem;
    font-weight: 700;
    letter-spacing: -0.4px;
    border-bottom: 3px solid var(--color-accent);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  h2 {
    color: var(--color-accent);
    font-size: 1rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 10px;
  }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 10px; font-size: 1.0rem; line-height: 1.5; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
    margin-top: 10px;
  }
  th {
    background: var(--color-fg);
    color: var(--color-bg);
    padding: 8px 12px;
    text-align: left;
  }
  td { padding: 7px 12px; border-bottom: 1px solid #d8d2c8; }
  tr:nth-child(even) td { background: #ede8e0; }
  .positive { color: var(--color-positive); font-weight: 700; }
  .negative { color: var(--color-negative); font-weight: 700; }
  .neutral  { color: var(--color-neutral);  font-weight: 700; }
  .label {
    display: inline-block;
    background: var(--color-accent);
    color: #fff;
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 4px;
    margin-bottom: 14px;
  }
  .cover-sub { font-size: 1.05rem; color: var(--color-muted); margin-top: 10px; }
  .winner {
    background: #e6f4ea;
    border-left: 4px solid var(--color-positive);
    padding: 10px 16px;
    margin-top: 14px;
    font-size: 0.95rem;
  }
  .footer-note { font-size: 0.78rem; color: var(--color-muted); margin-top: 16px; }
---

<!-- _paginate: false -->
# SponAI Consulting Client — Platform TCO Comparison

<div class="cover-sub">Total Cost of Ownership Analysis — 5-Year Horizon</div>
<div class="cover-sub">Evaluation Period: FY 2026–2030 &nbsp;|&nbsp; Prepared by: SponAItech LLC</div>
<div class="cover-sub">Confidential — For Procurement Committee Use Only</div>

<!--
PRESENTER NOTES — Slide 1: Title

This TCO deck is built for procurement committees and technology steering groups evaluating competing platform options. The scenario is a SponAI consulting engagement helping a mid-market client select among three software-as-a-service CRM/service platforms. Total cost of ownership goes well beyond license fees — it must capture implementation, integration, training, ongoing support, customisation, and exit costs. A 5-year horizon is standard for enterprise platform decisions; shorter periods favour high-implementation-cost solutions unfairly. Set this expectation at the outset. The committee should leave this session with a clear, data-supported recommendation — not a recommendation to "do more analysis."
-->

---

# Scope — What This TCO Covers

<div class="label">Methodology</div>

**Three options evaluated:**
- **Option A** — Salesforce Sales Cloud (Enterprise Edition)
- **Option B** — Microsoft Dynamics 365 Sales (Premium)
- **Option C** — HubSpot CRM (Enterprise)

**TCO components included in all options:**

- Software licensing (per-seat or usage-based)
- Implementation and configuration services
- Data migration from legacy CRM (Goldmine)
- Integration development (ERP, support portal, marketing automation)
- Training and change management
- Ongoing administration and customisation
- Annual support and maintenance contracts
- Estimated exit / migration cost at Year 5

<!--
PRESENTER NOTES — Slide 2: Scope

TCO comparisons only have meaning when the scope is identical across all options. This slide establishes that contract. If one option has a lower license cost but requires three times the integration effort, the raw license comparison is misleading. The eight cost components listed here are the standard TCO framework for enterprise software. Note that "exit cost" is included — a platform with aggressive data-lock-in or complex de-commissioning should carry that liability in the TCO. All three vendors were asked to provide implementation estimates using SponAItech's standardised scoping questionnaire. Vendor-provided estimates were adjusted using SponAItech's independent benchmark database of 47 comparable deployments.
-->

---

# Option A — Salesforce Sales Cloud TCO

<div class="label">Option A</div>

| Cost Component | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-Year Total |
|---|---|---|---|---|---|---|
| Licensing (150 seats) | $540K | $567K | $595K | $625K | $656K | $2,983K |
| Implementation | $820K | — | — | — | — | $820K |
| Integration (ERP + portal) | $340K | $40K | $40K | $40K | $40K | $500K |
| Training | $95K | $20K | $20K | $20K | $20K | $175K |
| Admin / customisation | $120K | $150K | $150K | $150K | $150K | $720K |
| Support contract | $54K | $57K | $60K | $63K | $66K | $300K |
| Exit cost (est.) | — | — | — | — | $180K | $180K |
| **Total** | **<span class="negative">$1,969K</span>** | **$834K** | **$865K** | **$898K** | **$1,112K** | **<span class="negative">$5,678K</span>** |

<!--
PRESENTER NOTES — Slide 3: Option A — Salesforce

Salesforce carries the highest licensing cost of the three options — $540K in Year 1 for 150 Enterprise Edition seats at $3,600 per seat per year, with 5% annual escalation per the standard MSA. The $820K implementation cost is based on SponAItech's own Salesforce delivery benchmark: 4,100 hours at a blended rate of $200/hr. The integration cost reflects two major integration points — the client's SAP ERP and their Zendesk support portal. The $180K exit cost is an estimate for data export, de-commissioning custom code, and migration assistance — Salesforce data portability is contractually available but operationally expensive. The 5-year total of $5.678M is the fully-loaded number.
-->

---

# Option B — Microsoft Dynamics 365 TCO

<parameter name="content"><!-- TEMPLATE: tco-deck
     CATEGORY: ROI / Business Case
     USE WHEN: comparing total cost of ownership across vendor or technology options
     SLIDE COUNT: 9
     PALETTE: Corporate hybrid (cream bg, gold/blue accents)
     RENDER: marp --pptx 62-tco-deck.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --color-bg: #f7f4ef;
    --color-fg: #0e1b2e;
    --color-accent: #3b9eff;
    --color-gold: #b8965a;
    --color-positive: #2d6a4f;
    --color-negative: #b91c1c;
    --color-neutral: #b8965a;
    --color-muted: #5a6677;
  }
  section {
    background: var(--color-bg);
    color: var(--color-fg);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 64px;
  }
  h1 {
    color: var(--color-fg);
    font-size: 1.9rem;
    font-weight: 700;
    letter-spacing: -0.4px;
    border-bottom: 3px solid var(--color-accent);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  h2 {
    color: var(--color-accent);
    font-size: 1rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 10px;
  }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 10px; font-size: 1.0rem; line-height: 1.5; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
    margin-top: 10px;
  }
  th {
    background: var(--color-fg);
    color: var(--color-bg);
    padding: 8px 12px;
    text-align: left;
  }
  td { padding: 7px 12px; border-bottom: 1px solid #d8d2c8; }
  tr:nth-child(even) td { background: #ede8e0; }
  .positive { color: var(--color-positive); font-weight: 700; }
  .negative { color: var(--color-negative); font-weight: 700; }
  .neutral  { color: var(--color-neutral);  font-weight: 700; }
  .label {
    display: inline-block;
    background: var(--color-accent);
    color: #fff;
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 4px;
    margin-bottom: 14px;
  }
  .cover-sub { font-size: 1.05rem; color: var(--color-muted); margin-top: 10px; }
  .winner {
    background: #e6f4ea;
    border-left: 4px solid var(--color-positive);
    padding: 10px 16px;
    margin-top: 14px;
    font-size: 0.95rem;
  }
  .footer-note { font-size: 0.78rem; color: var(--color-muted); margin-top: 16px; }
---

<!-- _paginate: false -->
# SponAI Consulting Client — Platform TCO Comparison

<div class="cover-sub">Total Cost of Ownership Analysis — 5-Year Horizon</div>
<div class="cover-sub">Evaluation Period: FY 2026–2030 &nbsp;|&nbsp; Prepared by: SponAItech LLC</div>
<div class="cover-sub">Confidential — For Procurement Committee Use Only</div>

<!--
PRESENTER NOTES — Slide 1: Title

This TCO deck is built for procurement committees and technology steering groups evaluating competing platform options. The scenario is a SponAI consulting engagement helping a mid-market client select among three software-as-a-service CRM/service platforms. Total cost of ownership goes well beyond license fees — it must capture implementation, integration, training, ongoing support, customisation, and exit costs. A 5-year horizon is standard for enterprise platform decisions; shorter periods favour high-implementation-cost solutions unfairly. Set this expectation at the outset. The committee should leave this session with a clear, data-supported recommendation — not a recommendation to "do more analysis."
-->

---

# Scope — What This TCO Covers

<div class="label">Methodology</div>

**Three options evaluated:**
- **Option A** — Salesforce Sales Cloud (Enterprise Edition)
- **Option B** — Microsoft Dynamics 365 Sales (Premium)
- **Option C** — HubSpot CRM (Enterprise)

**TCO components included in all options:**

- Software licensing (per-seat or usage-based)
- Implementation and configuration services
- Data migration from legacy CRM (Goldmine)
- Integration development (ERP, support portal, marketing automation)
- Training and change management
- Ongoing administration and customisation
- Annual support and maintenance contracts
- Estimated exit / migration cost at Year 5

<!--
PRESENTER NOTES — Slide 2: Scope

TCO comparisons only have meaning when the scope is identical across all options. This slide establishes that contract. If one option has a lower license cost but requires three times the integration effort, the raw license comparison is misleading. The eight cost components listed here are the standard TCO framework for enterprise software. Note that "exit cost" is included — a platform with aggressive data-lock-in or complex de-commissioning should carry that liability in the TCO. All three vendors were asked to provide implementation estimates using SponAItech's standardised scoping questionnaire. Vendor-provided estimates were adjusted using SponAItech's independent benchmark database of 47 comparable deployments.
-->

---

# Option A — Salesforce Sales Cloud TCO

<div class="label">Option A</div>

| Cost Component | Year 1 | Year 2–4 (avg) | Year 5 | 5-Year Total |
|---|---|---|---|---|
| Licensing (150 seats) | $540K | $596K | $656K | $2,983K |
| Implementation | $820K | — | — | $820K |
| Integration (ERP + portal) | $340K | $40K | $40K | $500K |
| Training | $95K | $20K | $20K | $175K |
| Admin / customisation | $120K | $150K | $150K | $720K |
| Support contract | $54K | $60K | $66K | $300K |
| Exit cost (est.) | — | — | $180K | $180K |
| **5-Year Total** | | | | **<span class="negative">$5,678K</span>** |

<!--
PRESENTER NOTES — Slide 3: Option A — Salesforce

Salesforce carries the highest licensing cost of the three options — $540K in Year 1 for 150 Enterprise Edition seats at $3,600 per seat per year, with 5% annual escalation per the standard MSA. The $820K implementation cost is based on SponAItech's own Salesforce delivery benchmark: 4,100 hours at a blended rate of $200/hr. The integration cost reflects two major integration points — the client's SAP ERP and their Zendesk support portal. The $180K exit cost is an estimate for data export, de-commissioning custom code, and migration assistance — Salesforce data portability is contractually available but operationally expensive. The 5-year total of $5.678M is the fully-loaded number.
-->

---

# Option B — Microsoft Dynamics 365 TCO

<div class="label">Option B</div>

| Cost Component | Year 1 | Year 2–4 (avg) | Year 5 | 5-Year Total |
|---|---|---|---|---|
| Licensing (150 seats) | $405K | $432K | $460K | $2,164K |
| Implementation | $1,050K | — | — | $1,050K |
| Integration (ERP + portal) | $280K | $35K | $35K | $420K |
| Training | $110K | $25K | $25K | $210K |
| Admin / customisation | $100K | $140K | $140K | $660K |
| Support (Microsoft Premier) | $80K | $80K | $80K | $400K |
| Exit cost (est.) | — | — | $90K | $90K |
| **5-Year Total** | | | | **<span class="neutral">$4,994K</span>** |

<!--
PRESENTER NOTES — Slide 4: Option B — Dynamics 365

Dynamics 365 has a lower per-seat licensing cost than Salesforce — approximately $2,700 per seat per year for Sales Premium — but a meaningfully higher implementation cost. The $1.05M implementation reflects the complexity of deploying Dynamics in a non-Microsoft-native environment: the client runs SAP ERP, not Microsoft F&O, which requires a custom integration layer. The Microsoft Premier support cost is also higher than Salesforce's standard contract. The exit cost is lower at $90K because Dynamics data is stored in Dataverse with standard export APIs. Net result: Dynamics is $684K cheaper than Salesforce over 5 years, primarily driven by lower licensing. But it requires a larger upfront investment and carries higher integration risk.
-->

---

# Option C — HubSpot CRM TCO

<div class="label">Option C — Recommended</div>

| Cost Component | Year 1 | Year 2–4 (avg) | Year 5 | 5-Year Total |
|---|---|---|---|---|
| Licensing (150 seats) | $270K | $283K | $297K | $1,389K |
| Implementation | $420K | — | — | $420K |
| Integration (ERP + portal) | $180K | $25K | $25K | $305K |
| Training | $60K | $15K | $15K | $120K |
| Admin / customisation | $80K | $100K | $100K | $500K |
| Support (HubSpot Enterprise) | $36K | $38K | $40K | $190K |
| Exit cost (est.) | — | — | $60K | $60K |
| **5-Year Total** | | | | **<span class="positive">$2,984K</span>** |

<!--
PRESENTER NOTES — Slide 5: Option C — HubSpot

HubSpot delivers the lowest 5-year TCO at $2.984M — approximately 47% cheaper than Salesforce and 40% cheaper than Dynamics. The lower licensing reflects HubSpot's consumption-based pricing model rather than per-seat fees. The $420K implementation is the most affordable because HubSpot's native integration hub (HubSpot Operations Hub) includes pre-built connectors for SAP and Zendesk, eliminating custom development. The lower support cost reflects HubSpot's self-service-first model. The trade-off: HubSpot has less configurability for complex B2B enterprise workflows. The client's use case — 150 sales reps managing mid-market accounts with standard pipeline stages — is well within HubSpot's capability ceiling. This is a key assumption to validate with the sales operations team.
-->

---

# Side-by-Side — Total Cost Comparison

<div class="label">Comparison Summary</div>

| Category | Option A — Salesforce | Option B — Dynamics | Option C — HubSpot |
|---|---|---|---|
| 5-Year TCO | <span class="negative">$5,678K</span> | <span class="neutral">$4,994K</span> | <span class="positive">$2,984K</span> |
| Year 1 cash requirement | <span class="negative">$2,009K</span> | <span class="negative">$2,025K</span> | <span class="positive">$1,046K</span> |
| Implementation risk | Low–Medium | High | Low |
| Feature fit (scored /10) | 9.1 | 8.4 | 7.8 |
| Integration complexity | Medium | High | Low |
| Vendor stability | High | High | Medium |

<div class="winner">Recommendation: Option C (HubSpot) delivers the lowest TCO ($2.984M) with acceptable feature fit (7.8/10) and the lowest implementation risk. The $2.694M saving vs. Salesforce funds two additional strategic technology initiatives within the 5-year plan.</div>

<!--
PRESENTER NOTES — Slide 6: Side-by-Side

This is the decision slide. HubSpot wins on cost by a wide margin. The feature-fit scores (rated by the sales operations team during a 3-week pilot) show that HubSpot meets 78% of the client's stated requirements out of the box — compared to 91% for Salesforce and 84% for Dynamics. The question the committee must answer is whether the 13-point feature gap justifies a $2.7M premium over five years. SponAItech's recommendation is no — the unmet features are workflow edge cases that can be addressed through process redesign at negligible cost. The $2.694M saving is real capital that can fund other priorities. Vendor stability for HubSpot is rated "Medium" because they are a public company with solid fundamentals but less market presence than Salesforce/Microsoft in the enterprise segment.
-->

---

# Sensitivity — What Changes the Decision

<div class="label">Sensitivity Analysis</div>

| Scenario | HubSpot TCO | Salesforce TCO | Delta |
|---|---|---|---|
| Base case | <span class="positive">$2,984K</span> | $5,678K | <span class="positive">$2,694K</span> in favour of HubSpot |
| HubSpot raises prices 20%/yr | <span class="neutral">$3,642K</span> | $5,678K | <span class="positive">$2,036K</span> in favour of HubSpot |
| HubSpot migration at Year 3 | <span class="negative">$4,810K</span> | $5,678K | <span class="positive">$868K</span> in favour of HubSpot |
| Full Salesforce discount (30%) | $2,984K | <span class="neutral">$3,975K</span> | <span class="positive">$991K</span> in favour of HubSpot |
| Dynamics discount (25%) | $2,984K | — | <span class="positive">$763K</span> vs. Dynamics |

HubSpot remains the lowest-TCO option in all scenarios except a forced mid-contract migration before Year 3.

<!--
PRESENTER NOTES — Slide 7: Sensitivity

Sensitivity analysis answers the objection: "What if something changes?" The most aggressive scenario for HubSpot is a forced migration at Year 3 — for example, if HubSpot's enterprise capabilities prove insufficient and the client must switch to Salesforce mid-contract. Even in this extreme scenario, HubSpot is still $868K cheaper than Salesforce would have been. The full Salesforce 30% discount scenario reflects what Salesforce account executives typically offer under competitive pressure. Even with a 30% discount, Salesforce is $991K more expensive than HubSpot. The committee can use this table to probe the Salesforce sales team: "What discount do you need to offer to match HubSpot TCO?" — the answer is approximately 47%, which is not a discount Salesforce will provide.
-->

---

# Recommendation — Select HubSpot Enterprise

<div class="label">Decision</div>

- Select **HubSpot CRM Enterprise** for 150 seats, 5-year term
- Negotiate annual payment terms to preserve cash flow
- Engage SponAItech for fixed-fee implementation ($420K) beginning Q3 2026
- Retain Salesforce and Dynamics as qualified alternates for 90 days (until contract signature)

**The ask:** Procurement committee approval to issue Letter of Intent to HubSpot within 10 business days.

<div class="footer-note">Savings of $2.694M vs. Salesforce | $2.010M vs. Dynamics — recommend ring-fencing $1.0M of savings for Year 2 digital transformation fund.</div>

<!--
PRESENTER NOTES — Slide 9: Recommendation and Ask

Close with a clear, time-bounded action. A Letter of Intent commits nothing financially — it signals selection intent to HubSpot, enabling contract negotiations to begin. The 90-day hold on alternates protects the committee in case HubSpot's contract terms are unacceptable. The ring-fencing suggestion is a value-add from SponAItech — recommend that the committee formally earmark $1.0M of the $2.694M saving for a digital transformation fund in Year 2. This creates a positive narrative: "HubSpot selection funds our next initiative." Anticipated objection: "We have a relationship with Salesforce." Response: relationships are valuable, but they are worth $2.694M only if Salesforce matches TCO — invite them to do so before the LoI deadline.
-->
