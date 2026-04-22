<!-- TEMPLATE: savings-deck
     CATEGORY: ROI / Business Case
     USE WHEN: pitching a cost savings initiative with phased implementation
     SLIDE COUNT: 9
     PALETTE: Corporate (cream bg, gold accent)
     RENDER: marp --pptx 66-savings-deck.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --color-bg: #f7f4ef;
    --color-fg: #0e1b2e;
    --color-accent: #b8965a;
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
    margin-top: 12px;
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
  .savings-box {
    background: #ede8e0;
    border-left: 5px solid var(--color-accent);
    padding: 14px 20px;
    margin-top: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .savings-val { font-size: 2rem; font-weight: 700; color: var(--color-positive); }
  .footer-note { font-size: 0.78rem; color: var(--color-muted); margin-top: 14px; }
---

<!-- _paginate: false -->
# Meridian Finance — IR Consolidation<br>Cost Savings Initiative

<div class="cover-sub">Finance Operations Efficiency Programme — FY 2026–2028</div>
<div class="cover-sub">Prepared for: CFO and Finance Leadership &nbsp;|&nbsp; April 2026</div>
<div class="cover-sub">Presented by: SponAItech LLC &nbsp;|&nbsp; Confidential</div>

<!--
PRESENTER NOTES — Slide 1: Title

This deck presents the Meridian Finance IR Consolidation cost savings initiative. Meridian Finance currently operates three investor relations platforms — institutional reporting, retail shareholder communications, and SEC filing management — at a combined annual spend of $4.8M. This programme proposes consolidating to a single platform, redesigning the IR operations team structure, and automating high-volume reporting tasks. The expected result is $3.1M in annual savings by FY 2028, achieved through a phased programme requiring $1.4M in investment. This is a high-confidence savings case because 65% of the saving comes from contractual changes (platform consolidation) rather than behavioural change.
-->

---

# Current Baseline — $4.8M Annual IR Operations Cost

<div class="label">Cost Baseline</div>

| Cost Category | Annual Spend | % of Total |
|---|---|---|
| Platform licences (3 systems) | <span class="negative">$2.1M</span> | 44% |
| IR staff (22 FTEs, loaded cost) | <span class="negative">$1.8M</span> | 38% |
| External printing and mailing | <span class="negative">$0.4M</span> | 8% |
| Data vendor subscriptions (Bloomberg, Refinitiv) | <span class="negative">$0.3M</span> | 6% |
| Compliance and legal review (manual) | <span class="negative">$0.2M</span> | 4% |
| **Total** | **<span class="negative">$4.8M</span>** | 100% |

<div class="footer-note">Baseline sourced from Meridian Finance cost centre report FY 2025. Loaded FTE rate = $81,800 (salary + benefits + overhead at 1.38x).</div>

<!--
PRESENTER NOTES — Slide 2: Baseline

The baseline establishes what we are working with. $4.8M per year is the total cost of Meridian's IR operations function. The largest single component is the $2.1M in platform licences — three separate systems, each with their own support contract, user licences, and upgrade fees. This is the most straightforward savings opportunity: consolidating to one platform eliminates two licence agreements. The $1.8M staff cost covers 22 FTEs; the consolidation and automation programme will reduce this to 16 FTEs through natural attrition over 18 months, saving $490K per year. The printing and mailing cost of $400K is almost entirely eliminable — digital-first investor communications will replace physical mail for 94% of the shareholder base. Present this baseline as a diagnostic, not a criticism of the current team.
-->

---

# Savings Target — $3.1M per Year by FY 2028

<div class="label">Savings Target</div>

<div class="savings-box">
  <div>
    <strong>Annual Savings Target (FY 2028)</strong><br>
    <span style="color:#5a6677; font-size:0.9rem;">64% reduction from $4.8M baseline to $1.7M steady state</span>
  </div>
  <div class="savings-val">$3.1M / year</div>
</div>

**Savings decomposed:**

- Platform consolidation (contract eliminations): <span class="positive">$1.55M/yr</span>
- Staff restructuring (6 FTE attrition): <span class="positive">$0.49M/yr</span>
- Print-to-digital transition: <span class="positive">$0.37M/yr</span>
- Automated reporting (compliance, Board packs): <span class="positive">$0.38M/yr</span>
- Data vendor renegotiation: <span class="positive">$0.31M/yr</span>

<!--
PRESENTER NOTES — Slide 3: Savings Target

The $3.1M savings target represents a 64% reduction from the $4.8M baseline — from $4.8M to $1.7M in ongoing annual cost. This is not a marginal improvement; it is a fundamental redesign of the cost structure. Walk through the five savings streams. Platform consolidation at $1.55M is the largest and most certain — it is a contractual change, not a process change. The two legacy platform contracts can be terminated on their renewal dates in Q2 and Q4 2026. Staff restructuring of $490K reflects 6 FTEs over 18 months through attrition and voluntary redundancy — no forced layoffs are required. Print-to-digital is a quick win implementable in 90 days. Automated reporting using the new consolidated platform's native automation tools eliminates 40% of the manual report production labour. Data vendor renegotiation uses the platform consolidation as leverage for a rebundling negotiation with Bloomberg and Refinitiv.
-->

---

# Initiatives — Five Savings Streams

<div class="label">Initiative Portfolio</div>

| Initiative | FY 2026 Saving | FY 2027 Saving | FY 2028+ Saving | Investment |
|---|---|---|---|---|
| 1. Platform consolidation | <span class="neutral">$0.7M</span> | <span class="positive">$1.55M</span> | <span class="positive">$1.55M</span> | <span class="negative">$0.6M</span> |
| 2. Staff restructuring | — | <span class="positive">$0.25M</span> | <span class="positive">$0.49M</span> | <span class="negative">$0.1M</span> |
| 3. Print-to-digital | <span class="positive">$0.2M</span> | <span class="positive">$0.37M</span> | <span class="positive">$0.37M</span> | <span class="negative">$0.05M</span> |
| 4. Automated reporting | — | <span class="positive">$0.19M</span> | <span class="positive">$0.38M</span> | <span class="negative">$0.4M</span> |
| 5. Vendor renegotiation | — | <span class="positive">$0.31M</span> | <span class="positive">$0.31M</span> | — |
| **Total** | **$0.9M** | **$2.67M** | **$3.1M** | **$1.15M** |

<!--
PRESENTER NOTES — Slide 4: Initiatives

This is the detail behind the savings target. Five initiatives, each with its own savings ramp and investment requirement. Initiative 1 (platform consolidation) delivers $700K in FY 2026 because only one of the two legacy contracts renews in 2026 — the second renews in early 2027, delivering the full $1.55M from FY 2027. Initiative 3 (print-to-digital) starts delivering in FY 2026 because it requires only a process change and a digital communication platform module — 90-day implementation. Initiative 4 (automated reporting) requires platform configuration work and template development — the $400K investment funds a SponAItech configuration project in H2 2026. Initiative 5 (vendor renegotiation) requires no investment but has a 9-month lead time — commencing renegotiation now, with new contracts effective from Q1 2027.
-->

---

# Quick Wins — $0.9M Available in FY 2026

<div class="label">Quick Wins</div>

**Three actions to capture $0.9M savings within 12 months:**

1. **Terminate Legacy Platform B** (renewal September 2026) — $700K annual licence saving effective October 2026. Zero implementation risk — data migration to new platform is contractually supported.

2. **Launch Digital Investor Portal** (90-day implementation, $50K investment) — eliminates $200K annual print-and-mail spend. Shareholder survey shows 91% prefer digital; remaining 9% receive physical copy at $18K/yr residual cost.

3. **Begin data vendor renegotiation** (zero investment, Procurement-led) — targeting $310K in combined Bloomberg/Refinitiv savings through rebundling, effective Q1 2027.

<!--
PRESENTER NOTES — Slide 5: Quick Wins

Quick wins serve two purposes: they generate early savings that offset investment costs, and they build organisational confidence. The Legacy Platform B termination is the most important quick win — $700K starting October 2026. The contract renewal is in September 2026; the notice period is 90 days, meaning the decision must be made by June 2026. This is a forcing event that creates urgency for programme approval today. The digital investor portal quick win is deceptively easy — the new consolidated platform includes a portal module. The $50K investment is for configuration and testing. The data vendor renegotiation is entirely handled by Procurement with SponAItech providing benchmarking data — zero additional implementation cost. These three quick wins are the programme's "funded start" — they cover the $150K initial investment cost within 90 days.
-->

---

# Long-Term — $3.1M Steady State by FY 2028

<div class="label">Long-Term Savings</div>

- Platform consolidation delivers **full $1.55M** from Q1 2027 (second legacy contract terminated)
- Staff restructuring reaches full **$490K** by Q2 2027 (6 FTE attrition complete)
- Automated reporting delivers **$380K** from H1 2027 (configuration complete, templates deployed)
- Total programme delivers **$3.1M annually** from FY 2028 — a sustained reduction in IR operations cost

**Beyond FY 2028:**
- Savings grow at approximately 3% per year with headcount inflation offsets
- Platform consolidation savings are locked via 5-year contract — no re-procurement risk
- Digital portal cost continues to decline as shareholder base ages toward digital-only preference

<!--
PRESENTER NOTES — Slide 6: Long-Term Savings

The long-term picture is compelling: $3.1M per year in perpetuity from FY 2028. The savings are durable because they are predominantly structural — platform contract eliminations and permanent headcount reductions — rather than one-time or behavioural. The 3% annual growth in savings value reflects the fact that headcount costs inflate, so the labour savings grow in absolute terms each year. The platform contract savings are fixed for 5 years per the InvestorFlow agreement. Beyond Year 5, the consolidation savings depend on the renewal negotiation — but with 5 years of demonstrated value, Meridian will be in a strong negotiating position. Contrast this with the status quo: the legacy platform costs grow 5–7% annually under standard SaaS escalation clauses.
-->

---

# Phasing — Three Stages Over 24 Months

<div class="label">Implementation Roadmap</div>

| Stage | Timeline | Key Actions | Cumulative Savings |
|---|---|---|---|
| Stage 1 — Quick Wins | Months 1–3 | Digital portal launch, Legacy B termination notice, vendor renegotiation start | <span class="positive">$0.2M</span> |
| Stage 2 — Platform Migration | Months 4–9 | InvestorFlow deployment, data migration, Legacy B go-live termination | <span class="positive">$0.9M</span> |
| Stage 3 — Automation | Months 10–18 | Automated reporting, Legacy A termination, staff restructuring complete | <span class="positive">$2.1M</span> |
| FY 2028 Steady State | Month 19+ | Full run-rate, programme complete | <span class="positive">$3.1M/yr</span> |

Total programme investment: **$1.15M** | Payback: **15 months from programme start**

<!--
PRESENTER NOTES — Slide 7: Phasing

The phasing is designed to front-load savings and back-load complexity. Stage 1 is entirely no-risk: quick wins that require no platform change. Stage 2 is the highest-complexity stage — migrating to InvestorFlow and terminating Legacy Platform B. This is where the $600K platform investment is spent. Stage 3 adds the automation layer on top of the new platform; by this point the platform is stable and the team is trained. The 15-month payback from programme start is calculated as: $1.15M investment recovered by cumulative savings reaching $1.15M, which occurs at Month 15 based on the savings ramp. This is a strong payback for a transformation programme of this scope.
-->

---

# Investment Needed — $1.15M to Unlock $3.1M/Year

<div class="label">Investment Summary</div>

| Investment Item | Amount | Timing |
|---|---|---|
| InvestorFlow platform licence (Year 1) | <span class="negative">$420K</span> | Month 1 |
| Data migration and integration | <span class="negative">$280K</span> | Months 2–6 |
| Automated reporting configuration (SponAItech) | <span class="negative">$200K</span> | Months 8–12 |
| Digital investor portal (module config) | <span class="negative">$50K</span> | Months 1–3 |
| Staff transition support | <span class="negative">$100K</span> | Months 6–18 |
| Contingency (8%) | <span class="negative">$100K</span> | As needed |
| **Total** | **<span class="negative">$1,150K</span>** | |

3-year ROI: **($3.1M × 3) − $1.15M = $8.15M net** &nbsp;|&nbsp; **7.1x return** on investment

<!--
PRESENTER NOTES — Slide 8: Investment Needed

The investment is modest relative to the savings: $1.15M to unlock $3.1M per year. The 3-year net return of $8.15M represents a 7.1x ROI — exceptional for an efficiency programme. The investment breakdown shows that the largest single item is the InvestorFlow Year 1 licence ($420K). Note that this is a Year 1 figure; the ongoing licence cost from Year 2 is $240K per year, which is $140K per year less than Legacy Platform B alone. The data migration cost of $280K is based on InvestorFlow's fixed-fee migration proposal. The automated reporting configuration of $200K is a SponAItech fixed-fee engagement. The 8% contingency is conservative given the programme's reliance on established platforms rather than custom development.
-->

---

# Governance — Accountability Framework

<div class="label">Governance</div>

- **Programme Sponsor:** Chief Financial Officer
- **Programme Manager:** Director of Finance Operations
- **Technical Lead:** VP, Financial Systems (InvestorFlow relationship owner)
- **Steering reviews:** Monthly for Stages 1–2; quarterly from Stage 3
- **Savings verification:** CFO confirms savings in monthly cost centre report (no self-certification)
- **The ask:** CFO sign-off on $1.15M programme budget and appointment of Programme Manager by May 1, 2026

**Value at stake if deferred 6 months:** Approximately $1.4M in Stage 1 and 2 savings foregone (Legacy B termination window closes).

<!--
PRESENTER NOTES — Slide 9: Governance and Ask

The governance structure is deliberately lean for a programme of this size — CFO sponsor, one programme manager, monthly steering until the platform migration is complete. The savings verification mechanism is important: savings are confirmed in the monthly cost centre report by the CFO, not self-reported by the implementation team. This creates independent accountability. The most critical urgency point: Legacy Platform B's contract renewal is in September 2026. The 90-day notice period means the termination decision must be made by June 2026. If programme approval is deferred beyond April 30, 2026, the termination window closes and $700K in Stage 2 savings are delayed by 12 months. That is the single most important reason to decide today. Ask the CFO: "Is there a reason to wait that is worth $700K?"
-->
