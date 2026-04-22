<!-- TEMPLATE: grant-pitch
     CATEGORY: Grant / Funding Application
     USE WHEN: applying for federal, state, or foundation grants; SBIR/STTR; philanthropic funding
     SLIDE COUNT: 10
     PALETTE: Executive cream (warm academic — cream/navy)
     RENDER: marp --pptx 16-grant-pitch.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Georgia', 'Segoe UI', serif;
    background: #f7f4ef;
    color: #1c1a18;
    padding: 52px 68px;
  }
  h1 {
    font-family: 'Georgia', serif;
    color: #0e1b2e;
    letter-spacing: -0.3px;
    font-size: 2em;
    line-height: 1.2;
    margin-bottom: 0.35em;
  }
  h2 {
    color: #b8965a;
    font-size: 0.85em;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 { color: #0e1b2e; font-size: 1em; font-weight: 700; }
  strong { color: #0e1b2e; font-weight: 700; }
  em { color: #b8965a; font-style: normal; font-weight: 600; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "• "; color: #b8965a; }
  ul li { margin-bottom: 0.6em; font-size: 0.98em; line-height: 1.6; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88em;
  }
  th {
    background: #ede9e1;
    color: #0e1b2e;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.05em;
    font-size: 0.82em;
    text-transform: uppercase;
    border-bottom: 2px solid #c8c2b8;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #ede9e1; }
  tr:last-child td { border-bottom: none; }
  blockquote {
    border-left: 3px solid #b8965a;
    padding: 10px 20px;
    margin: 1em 0;
    background: #ede9e1;
    color: #0e1b2e;
    font-size: 0.95em;
    font-style: italic;
    border-radius: 0 6px 6px 0;
  }
  section::after { color: #c4bdb3; font-size: 0.75em; }
---

## SBIR Phase II Application

# Reducing Prior Authorization Burden Through Federated Clinical AI

**Helix Health Technologies, Inc.**
*Principal Investigator: Dr. Priya Mehta, MD, MS*
*Submitted to: AHRQ Program Announcement PA-26-014 &nbsp;|&nbsp; April 2026*

<!-- Speaker notes:
Grant applications have a distinct audience from commercial pitches: program officers and review panels evaluate scientific merit, feasibility, significance, and innovation — in that order. This first slide establishes four things immediately: the problem domain (prior authorization burden), the approach (federated clinical AI — a specific technical term that signals your awareness of privacy constraints), the organization (Helix, not just the PI), and the regulatory framing (AHRQ PA number signals you have read the program announcement). If this is a foundation grant rather than SBIR, replace the AHRQ reference with the foundation name and program area. Federated learning is an intentional technical choice that resonates with AHRQ reviewers because it enables learning from multiple hospital datasets without centralizing patient data — it directly addresses the privacy concerns that kill most clinical AI grant applications. Be prepared to explain federated vs. centralized learning in the Q&A.
-->

---

## Mission

# Eliminating Administrative Friction That Harms Patient Access

**Organizational mission:** Develop and deploy AI systems that reduce administrative burden in clinical settings, with a specific focus on populations facing access barriers due to process delays.

- Helix is an **SBIR Phase I awardee** (AHRQ, 2025) — Phase I validated technical feasibility
- **3 health systems** participated in Phase I; **8 additional** committed for Phase II
- 100% of Phase I milestones delivered on schedule

<!-- Speaker notes:
Mission statements in grant applications must align with the funder's mission. AHRQ focuses on healthcare quality, safety, effectiveness, and access. Your mission statement should use their language — "administrative burden," "patient access," "access barriers" — because reviewers are trained to match application language to program goals. The three proof points (Phase I award, health systems committed, milestones delivered) establish credibility for reviewers who are wondering "can this team actually execute?" Phase II reviewers are skeptical of Phase I awardees who overstated their initial progress. Counter this by being precise: "100% of Phase I milestones delivered on schedule" — list them if you have room. The 8 additional health systems committed for Phase II is a strong signal of market pull, which reviewers weight heavily because it suggests the technology will survive beyond grant funding.
-->

---

## The Problem — Evidence Base

# Prior Authorization Delays Are a Measurable Access Crisis

- **94 million** PA requests processed annually in the US (AMA, 2025)
- **34%** of physicians report a patient experienced a serious adverse event due to PA delay
- **Disproportionate impact:** patients in rural areas wait **40% longer** for PA approvals
- **Cost:** $14B in annual administrative spending — $13.30 per transaction, manually

> "Prior authorization is the single most significant administrative burden I face as a practicing physician — and it directly harms my patients."
> — Survey respondent, AMA Physician Practice Survey 2025

<!-- Speaker notes:
Evidence-based problem framing is non-negotiable in grant applications. Every statistic must have a citation — add them to the slide notes or a reference appendix. The AMA 2025 survey data is real and current; use the actual citation in your formal application. The rural access disparity point is particularly important for AHRQ applications — AHRQ has an explicit focus on health disparities. If your Phase II design includes a rural health system, name it here. The quote from a physician is powerful, but in a formal grant submission, use it in the significance section of your narrative rather than as a primary data source. In the pitch version (for a review panel presentation), the quote humanizes the statistics and reminds reviewers that behind the numbers are patients who are not getting care. Keep this slide evidence-heavy — grant reviewers want to see that you know the literature, not just the pain.
-->

---

## Proposed Project

# Phase II — Federated Learning Across 11 Health Systems

**Core innovation:** A federated AI system that learns denial patterns from multiple health systems without centralizing patient data — trained on each site's local EHR, aggregated via differential privacy.

- **Primary aim:** Reduce first-pass PA denial rate by 50% across all study sites
- **Secondary aim:** Reduce time-to-approval by 60% for CMS-mandated PA procedures
- **Exploratory aim:** Identify disparities in PA approval rates by race, geography, and payer

<!-- Speaker notes:
The proposed project slide is where your technical innovation is established. Federated learning is the key differentiator from both a scientific and a regulatory standpoint: you are not asking health systems to share patient data, only model gradients. Differential privacy provides a formal mathematical guarantee against patient re-identification. If reviewers are not familiar with federated learning, be ready to explain it: "Each site trains a local model on their own patient data. We aggregate the model weights — not the data — and send updates back. No patient record ever leaves the site." The three-aim structure mirrors NIH/AHRQ grant conventions — primary, secondary, exploratory. Even if this is a pitch slide rather than a full application, using this structure signals familiarity with the grant process. Specific percentage targets (50% denial reduction, 60% time-to-approval reduction) are based on your Phase I results — do not overpromise beyond what your data supports.
-->

---

## Evidence — Phase I Results

| Metric | Baseline | Phase I Result | Change |
|---|---|---|---|
| First-pass denial rate | 17.4% | 8.1% | **-53%** |
| Time to approval (days) | 11.2 | 4.3 | **-62%** |
| Appeal win rate | 41% (manual) | 73% (AI) | **+78%** |
| Physician time per PA (min) | 14.2 | 0.37 | **-97%** |
| Patient adverse events (attributed) | 8 | 1 | **-88%** |

*N=3 health systems, 18 months, 340,000+ PA transactions*

<!-- Speaker notes:
Phase I results are the single most important element of a Phase II application. They demonstrate feasibility — which is the primary evaluation criterion for Phase II. These numbers need to be exactly what your Phase I report states; any discrepancy between the pitch and the formal application will be flagged by the program officer. The patient adverse events row is the most powerful: from 8 attributed cases to 1. That is not a statistic — that is a person who received care they would not have received without this technology. Name it in your presentation: "In our Phase I study, we tracked patient adverse events that were directly attributed to PA delays. We went from 8 to 1 across three sites in 18 months. That is the impact we are scaling in Phase II." The sample size (340,000+ transactions) is sufficient for statistical significance claims — be ready to provide confidence intervals if asked by biostatistics reviewers.
-->

---

## Outcomes and Impact

# Measurable Targets — Phase II (36 Months)

- **Primary:** 50% reduction in first-pass denial rate across all 11 sites
- **50,000 patients** avoid PA-related delays annually post-deployment
- **$4.1M** saved in administrative costs across participating health systems
- **Disparities:** measurable reduction in rural-urban PA approval gap (target: 20% reduction)
- All models and anonymized benchmarks **published open access** under CC BY 4.0

<!-- Speaker notes:
Outcomes must be SMART: specific, measurable, achievable, relevant, time-bound. The 50,000 patients figure is calculated: 11 sites x average 4,545 patients affected by PA delays annually. Show the math in the full application narrative. The $4.1M savings figure should reconcile with your cost model — $13.30 per transaction x 340,000 transactions x 53% denial reduction = $2.4M in direct denial savings, plus FTE time savings. Be precise about which savings are included. The open access publication commitment is important for AHRQ: they fund research for public benefit and expect dissemination. Committing to CC BY 4.0 publication signals you understand the federal open access mandate. The disparities target (20% rural-urban reduction) is quantified rather than aspirational — reviewers will evaluate whether it is achievable given your study design.
-->

---

## Timeline

# 36-Month Phase II Plan

| Period | Milestone |
|---|---|
| Months 1–6 | IRB approvals (8 sites), FHIR integration at 5 new sites |
| Months 7–12 | Federated model baseline training, first longitudinal cohort enrolled |
| Months 13–18 | Interim analysis, disparities report, peer review submission |
| Months 19–24 | Scale to all 11 sites, A/B testing of model vs. standard care |
| Months 25–30 | Final cohort data, outcomes analysis, health economic model |
| Months 31–36 | Final reporting, open-access publication, dissemination conference |

<!-- Speaker notes:
A credible timeline demonstrates project management maturity. IRB approvals in months 1–6 is honest — multi-site IRB review takes 3–5 months even with a coordinating IRB. Do not show a timeline where everything starts in month 1; reviewers with clinical research experience will flag it. The interim analysis at month 13–18 is important: AHRQ program officers conduct site visits and expect progress reports at 12 and 18 months. The A/B testing in months 19–24 is your primary endpoint: you are comparing outcomes between patients whose PA goes through Helix versus the standard care arm. This is the controlled study design that will withstand peer review. The final publication commitment in months 31–36 is not a throw-away — name the target journals: JAMIA, NEJM Catalyst, or Health Affairs depending on the framing. Reviewers respect specificity about dissemination plans.
-->

---

## Budget Summary

# $1.8M Phase II Request — 3-Year Period

| Category | Amount | % |
|---|---|---|
| Personnel (PI, postdoc x2, data engineer, PM) | $890,000 | 49% |
| Subaward — site coordination (11 systems) | $420,000 | 23% |
| Computing infrastructure (federated nodes) | $185,000 | 10% |
| Patient engagement and dissemination | $95,000 | 5% |
| Indirect costs (44% MTDC) | $210,000 | 12% |
| **Total** | **$1,800,000** | **100%** |

*Cost per PA transaction analyzed: $0.018 &nbsp;|&nbsp; Cost per adverse event prevented: $1,800*

<!-- Speaker notes:
Budget slides in grant applications are scrutinized for reasonableness and justification. The 49% personnel rate is appropriate for an SBIR application — it is not inflated. Two postdocs are justified for an 11-site study with a disparities component. The subaward rate ($420K across 11 sites = $38K per site) covers IRB fees, data manager time, and site coordinator effort — this is below-market and signifies cost efficiency. Indirect costs at 44% MTDC is your organization's negotiated rate with the federal government — include your rate agreement in the appendix. The two cost-effectiveness metrics at the bottom — $0.018 per transaction and $1,800 per adverse event prevented — frame the investment in comparative effectiveness terms. Compare to the $13.30 manual processing cost: Helix costs 1.4 cents per transaction to run and prevent adverse events at $1,800 each. That is a compelling cost-effectiveness argument for both the grant reviewer and the policy argument for scale.
-->

---

## Team

# Research Team with Complementary Expertise

- **PI: Dr. Priya Mehta, MD, MS** — Health informatics, UCSF; 12 publications on PA reform; PCORI award 2023
- **Co-I: Dr. James Okafor, PhD** — Machine learning and federated systems; Change Healthcare ex-CTO
- **Co-I: Dr. Sarah Chen, MS** — Clinical informatics implementation; 6 years VP at Sutter Health
- **Biostatistician: Dr. Anika Ramos, PhD** — Health services research; expertise in disparities analysis

*Advisory board includes former CMS Deputy Administrator and Chief Medical Officer, Anthem.*

<!-- Speaker notes:
NIH and AHRQ score teams heavily. Each person needs to demonstrate specific, relevant expertise — not just impressive credentials. Dr. Mehta's PCORI award signals she can manage a multi-site federal grant. Dr. Okafor's federated systems expertise is directly relevant to the technical innovation. Dr. Chen's implementation experience at a large health system is what will make the 11-site scale actually happen — this is where most academic research fails. Dr. Ramos is specifically named for disparities analysis because your exploratory aim has a disparities component — reviewers will look for a biostatistician with that background. The advisory board names (former CMS and Anthem) are credibility anchors that signal regulatory and payer-side access. In the formal application, each person needs a 4-page biosketch. For the pitch slide, one bullet each is sufficient. If asked about any team member's availability: come with specific effort percentages — "Dr. Mehta is at 25% effort, consistent with her Phase I commitment."
-->

---

## Sustainability

# Post-Grant Revenue Path — No Dependency on Continued Funding

- **Commercial deployment:** Helix commercial product reaches 30+ health systems by grant end
- **Subscription revenue:** $9M ARR projected by Q4 2026 — self-sustaining operational model
- **Open-source components:** federated learning framework released to research community
- **Policy impact:** findings submitted to CMS for consideration in 2027 interoperability rulemaking

*This grant accelerates a commercially-viable product — it does not create dependency on future grants.*

<!-- Speaker notes:
Sustainability is evaluated by AHRQ reviewers because federal agencies do not want to fund technology that disappears when the grant ends. Your sustainability argument is unusually strong because Helix is a commercial product: grant funding subsidizes the research study design and the disparities analysis; the underlying technology is funded by commercial revenue. Be explicit about this: "Helix will continue to operate and improve regardless of whether grant funding continues. The grant funds the rigorous controlled study that generates the evidence base for policy and broader adoption." The open-source commitment for the federated learning framework is important for academic credibility and will be cited in peer-reviewed papers. The CMS rulemaking mention is the policy impact pathway — AHRQ explicitly values research that influences federal policy. If you have already submitted comments to CMS or testified before an advisory committee, mention it here.
-->
