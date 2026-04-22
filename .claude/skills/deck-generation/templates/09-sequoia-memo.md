<!-- TEMPLATE: 09-sequoia-memo  CATEGORY: Executive / Pitch  USE WHEN: Series A or B fundraise using classic Sequoia pitch format — purpose, problem, solution, why now, market, competition, product, model, team, financials  SLIDE COUNT: 10  PALETTE: Dark premium (#0a0e14 bg, #d0d8e4 text, #ffffff headings, #3b9eff accent)  RENDER: marp --pptx 09-sequoia-memo.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: 'DM Sans', system-ui, sans-serif; background: #0a0e14; color: #d0d8e4; padding: 60px 80px; }
  h1 { font-family: 'DM Serif Display', Georgia, serif; color: #ffffff; letter-spacing: -0.5px; font-size: 2em; margin-bottom: 0.3em; }
  h2 { color: #3b9eff; font-size: 1em; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1em; }
  strong { color: #ffffff; }
  em { color: #3b9eff; font-style: normal; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
  th { background: #111820; color: #3b9eff; padding: 10px 16px; text-align: left; border-bottom: 2px solid #3b9eff; }
  td { padding: 10px 16px; border-bottom: 1px solid #1e2a38; color: #d0d8e4; }
  .hero { font-size: 2.6em; font-weight: 700; color: #ffffff; display: block; line-height: 1.1; letter-spacing: -0.02em; }
  .sub { font-size: 0.95em; color: #8899ac; margin-top: 8px; display: block; }
  .pill { display: inline-block; background: #111820; border: 1px solid #3b9eff; color: #3b9eff; padding: 4px 14px; border-radius: 100px; font-size: 0.78em; margin-right: 8px; }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 36px; margin-top: 20px; }
  .card { background: #111820; border-left: 4px solid #3b9eff; padding: 20px 24px; border-radius: 4px; }
  .muted { color: #8899ac; font-size: 0.88em; }
---

# Helix
## Company Purpose

**AI that resolves prior authorizations before they delay care.**

Every day, US clinicians spend 13+ hours per week on PA paperwork.
Helix cuts that to under 2 hours — without changing the EHR.

<span class="pill">Healthcare AI</span><span class="pill">Series A</span><span class="pill">April 2026</span>

<!-- Speaker notes:
Open with one sentence that a 10-year-old could understand, because that is the Sequoia standard. Helix exists to remove the administrative tax on clinical care. Prior authorization is the mechanism by which payers approve treatments before they are delivered. It was designed as a cost-control mechanism; it has become a care-delay mechanism. The average PA request takes 11 business days to resolve. For cancer patients, that delay is clinically meaningful. Helix uses AI trained on 18 months of retrospective PA outcomes — approvals, denials, appeal outcomes — to predict, pre-populate, and route PA requests with 94% accuracy. Clinicians spend 87% less time on PA paperwork. Payers process 40% fewer re-submissions. The health system saves $3,200 per physician per year in administrative labor. That is the company in one paragraph. We are raising a Series A to expand from 94 health systems to 500 by the end of 2027, to deepen the Epic integration to cover 80% of PA types, and to launch the first AI-assisted denial appeal workflow in the market. This deck follows the Sequoia Capital pitch structure used by Airbnb, DoorDash, and LinkedIn at Series A. We will move through purpose, problem, solution, why now, market, competition, product, model, team, and financials. Questions after the deck — we have left 20 minutes.
-->

---

# The Problem

## Prior Auth Is Broken at Scale

<div class="grid2">
  <div>
    <p><strong>3.4 billion</strong> PA requests annually in the US<br><span class="muted">AMA 2025 survey</span></p>
    <p><strong>13.4 hours/week</strong> per physician spent on PA<br><span class="muted">Cost: $54B/year in wasted clinical labor</span></p>
    <p><strong>1 in 4</strong> patients abandon treatment when PA is delayed &gt; 2 weeks<br><span class="muted">AHIP outcomes study, 2024</span></p>
  </div>
  <div class="card">
    <p><strong>The workflow today:</strong></p>
    <ol style="margin: 0; padding-left: 1.2em; font-size: 0.9em; line-height: 2;">
      <li>Clinician identifies PA-required treatment</li>
      <li>Staff pulls payer-specific form (avg 14 pages)</li>
      <li>Manual data entry from 3+ source systems</li>
      <li>Fax or portal submission (92% still use fax)</li>
      <li>Wait 11 business days for decision</li>
      <li>Appeal if denied (47% denial rate for complex cases)</li>
    </ol>
  </div>
</div>

<!-- Speaker notes:
The problem slide must be visceral. $54 billion in clinical labor wasted on paperwork that should not exist is visceral. But the human cost is more compelling than the dollar cost for this audience: 1 in 4 patients abandoning treatment because an insurance form took too long. We are not solving a workflow inconvenience — we are solving a patient-outcome problem that has a regulatory and political headwind behind it. The No Surprises Act, the CMS interoperability final rule, and the bipartisan Improving Seniors' Timely Access to Care Act all target prior authorization specifically. Sequoia pitches perform best when the problem slide generates a visceral "of course" moment in the investor's mind. The six-step workflow on the right side is designed to do that — most investors who have had a personal healthcare experience in the last five years have encountered this exact sequence from the patient side. They have seen a doctor say "I need to get authorization for this" and watched nothing happen for two weeks. That is our opening.
-->

---

# The Solution

## Helix — AI Clinical Workflow Platform

<div class="grid2">
  <div>
    <strong>What it does:</strong>
    <ul style="margin-top: 12px; line-height: 2.2;">
      <li>Reads the EHR — no new data entry</li>
      <li>Predicts approval probability in &lt; 2 seconds</li>
      <li>Pre-populates the correct payer form</li>
      <li>Submits via API or auto-fax</li>
      <li>Tracks status and flags denials for appeal</li>
    </ul>
  </div>
  <div>
    <strong>What changes for clinicians:</strong>
    <ul style="margin-top: 12px; line-height: 2.2;">
      <li>PA time: 13.4 hrs/week &#8594; <em>1.9 hrs/week</em></li>
      <li>Approval cycle: 11 days &#8594; <em>2.1 days</em></li>
      <li>Denial rate: 47% &#8594; <em>18%</em> (better first submission)</li>
      <li>Staff cost savings: <em>$3,200/physician/year</em></li>
    </ul>
  </div>
</div>

**Integration:** Works inside Epic, Cerner, and Meditech — zero new login, zero new training.

<!-- Speaker notes:
The solution slide answers the problem slide directly. Every bullet on the left maps to a step in the broken workflow we showed on slide 2. Reads the EHR eliminates step 3 (manual data entry from 3 source systems). Submits via API or auto-fax eliminates the fax machine. Flags denials for appeal eliminates step 6 as a manual process. The right side shows the before-and-after in the clinician's actual experience: time, cycle, denial rate, and dollars. These are not projections — they are averages from our 94 active health systems over the past 12 months. The zero-new-login point is critical for the enterprise buyer: the number-one reason clinical AI tools fail at adoption is that they require behavior change from overloaded clinicians. Helix surfaces inside the native EHR workflow as an embedded panel. The clinician sees a recommendation with a confidence score, approves with one click, and the system handles the rest. We built the Epic integration first because Epic runs 38% of US hospitals. Cerner is in beta with 4 sites; Meditech integration ships Q3.
-->

---

# Why Now

## Three Forces That Did Not Exist 24 Months Ago

<div class="grid2">
  <div class="card">
    <strong>1. CMS Mandate (Jan 2026)</strong><br>
    <span style="font-size:0.88em; color:#d0d8e4; line-height:1.6; display:block; margin-top:8px;">All payers must support FHIR-based PA APIs by Jan 1, 2026. Creates the data infrastructure Helix requires. First time in history payers are legally required to expose real-time PA status via API.</span>
  </div>
  <div class="card">
    <strong>2. Clinical LLM Maturity</strong><br>
    <span style="font-size:0.88em; color:#d0d8e4; line-height:1.6; display:block; margin-top:8px;">GPT-4-class models now pass USMLE Step 3 (90th percentile). Helix's proprietary fine-tune on 18M PA decisions outperforms general models by 31 points on clinical reasoning accuracy.</span>
  </div>
</div>

<div class="card" style="margin-top: 24px;">
  <strong>3. Health System CFO Pain</strong> — Post-pandemic margin compression averaging -4.3% (AHA 2025). Administrative cost reduction is the #1 CFO priority; Helix has a 6-month ROI proof point from 94 live customers.
</div>

<!-- Speaker notes:
Why now is the slide that separates fundable ideas from fundable companies. Three structural shifts happened in the 24-month window before our founding that make Helix possible today but not five years ago. The CMS FHIR mandate is the most important: before January 2026, payers were not required to expose PA data via API. That meant any AI system had to scrape web portals or rely on fax OCR — noisy, fragile, and not HIPAA-compliant at scale. The mandate flipped that overnight. Helix was architecturally designed around FHIR API access; our competitors who built on portal-scraping are now scrambling to retool. The clinical LLM maturity point answers the "why not Google or Epic?" question preemptively. General-purpose LLMs have the reasoning capability, but not the PA-specific training. Our 18-month retrospective dataset — 18 million PA decisions across 7 payers and 22 states — is the moat. No one else has this dataset at this specificity. Health system CFO pain closes the loop on urgency: a solution that delivers 6-month ROI is not a nice-to-have in a -4.3% margin environment. It is a budget item that approves itself.
-->

---

# Market Size

## $54B Addressable — Not Counting the Appeal Layer

| Segment | TAM | SAM | SOM (3yr) |
|---|---|---|---|
| Health system PA workflow | $54B | $18B | $420M |
| Payer-side PA processing | $12B | $4B | $80M |
| Denial appeal automation | $8B | $3B | $60M |
| **Total** | **$74B** | **$25B** | **$560M** |

**Bottoms-up:** 6,090 US hospitals &#215; avg $340K ACV = $2.1B reachable market in hospitals alone.
Add 250,000 physician practices (smaller ACV) &#8594; $4.8B total reachable.

<!-- Speaker notes:
Sequoia explicitly warns against top-down TAM slides — "the global healthcare market is $4 trillion" is meaningless. This slide builds from first principles. The $54B figure is not an estimate; it is the AMA's own calculation of physician labor cost attributable to PA paperwork, published in their 2025 administrative burden report. We own the health system segment. Payer-side PA processing and denial appeal automation are expansion markets we enter in 2027 and 2028 respectively — they are on this slide to show that Helix is not a point solution. The bottoms-up calculation is the one investors should internalize: 6,090 hospitals at $340K average ACV gives us a $2.1B hospital-only reachable market. We are currently capturing $1.7M of that, which is 0.08% penetration. Our 3-year SOM of $420M requires 8.7% penetration of the hospital segment — achievable via our current sales motion with Series A capital. We do not need a new distribution channel to reach that number. We scale the existing channel.
-->

---

# Competition

## No One Has the Full Stack

| Competitor | Approach | Gap |
|---|---|---|
| Waystar / Availity | Rules-based PA routing | No AI prediction; 11-day cycle unchanged |
| Cohere Health | Payer-side clinical review AI | Serves payers, not health systems; no EHR integration |
| Epic native PA module | PA tracking inside Epic | No AI; no cross-payer intelligence; no denial prediction |
| General-purpose LLMs | Custom GPT wrappers | No PA-specific training; no FHIR integration; HIPAA risk |
| **Helix** | **End-to-end AI PA platform** | **Only solution combining EHR integration + payer FHIR API + proprietary model** |

**Defensibility:** 18M labeled PA decisions. Each new customer adds ~200K labeled samples/year. The moat widens with scale.

<!-- Speaker notes:
The competitive landscape slide must be honest or sophisticated investors will catch the gaps and question your judgment. Waystar is the incumbent in PA routing — they process more PA requests than anyone else in the US. But they are a workflow router, not an AI predictor. They tell you where to send a request; they do not tell you whether it will be approved or how to optimize it for approval. Cohere Health is the most technically sophisticated competitor but they are on the payer side of the table, which means health systems view them as the adversary's tool, not their tool. Epic is the biggest structural risk — if Epic adds AI-powered PA natively, they have the distribution. But Epic has 18 months of AI development lag and has historically not moved fast in clinical AI. Our Epic App Orchard partnership is partly a hedge: we want to be the preferred Epic AI layer for PA before Epic builds it. The moat statement at the bottom is the most important sentence on this slide: 18 million labeled PA outcomes is a dataset that takes 5-7 years to accumulate at the pace of a health system's natural volume. A new entrant cannot shortcut it.
-->

---

# Product

## What Ships in 2026

<div class="grid2">
  <div>
    <strong>Live (Apr 2026)</strong>
    <ul style="margin-top: 8px; line-height: 2;">
      <li>Epic FHIR bi-directional sync</li>
      <li>PA prediction engine v2 (94% accuracy)</li>
      <li>HIPAA audit log + SOC 2 prep</li>
      <li>CMS interoperability compliance</li>
    </ul>
  </div>
  <div>
    <strong>Roadmap (2026)</strong>
    <ul style="margin-top: 8px; line-height: 2;">
      <li>Denial appeal AI (Q2) — automates 80% of standard appeals</li>
      <li>Bulk batch API (Q2) — for large IDN processing</li>
      <li>Cerner integration (Q3)</li>
      <li>Payer portal for real-time response (Q4)</li>
    </ul>
  </div>
</div>

**Architecture:** HIPAA-compliant, SOC 2 Type 2 (audit July 2026), multi-tenant, deployed in customer VPC on request.

<!-- Speaker notes:
Product credibility at Series A comes from showing that what is live works, and that the roadmap is grounded in customer demand rather than engineering ambition. Everything in the Live column has been shipped, is used by active customers, and is generating the outcome metrics we showed on slide 3. The roadmap is sequenced by customer request volume: denial appeal was the number-one feature request across all Q1 customer interviews; bulk batch API came directly from Dignity Health; Cerner integration opens a new segment; the payer portal is a 2027 revenue opportunity. Architecture matters to the CTO-level buyer we need to close enterprise deals. HIPAA-compliant is table stakes. SOC 2 Type 2 differentiates us from competitors who are still SOC 2 Type 1. Multi-tenant deployment is our default; we offer customer-VPC deployment for health systems with strict data residency requirements — typically academic medical centers with IRB constraints. We currently have three customers on VPC-isolated deployments. The architecture is built on Azure Container Apps with Azure Health Data Services for FHIR storage — a stack that Azure's healthcare team has endorsed as their reference architecture for clinical AI.
-->

---

# Business Model

## Land-Expand in Health Systems

<div class="grid2">
  <div class="card">
    <strong>Land</strong>
    <p style="font-size:0.88em; line-height:1.8; margin-top:8px;">$18K–$45K ACV per department (avg 3 departments/hospital at signing)<br>Average contract: $72K ACV, 2-year term<br>Implementation fee: $12K one-time</p>
  </div>
  <div class="card">
    <strong>Expand</strong>
    <p style="font-size:0.88em; line-height:1.8; margin-top:8px;">112% NRR — existing customers growing 12%/year through seat adds and new department rollouts<br>Upsell: denial appeal module adds $28K ACV avg</p>
  </div>
</div>

| Metric | Value |
|---|---|
| Gross Margin | 73% |
| LTV / CAC | 6.8x |
| CAC Payback | 8.7 months |
| Average Contract Length | 24 months |

<!-- Speaker notes:
The business model slide answers: how do you make money, and is the unit economics attractive? The land-expand motion works in health systems because every hospital has 20–30 departments and the PA workflow problem exists in all of them. We land in the highest-volume department — typically oncology or cardiology — where the PA burden is most severe and the ROI is most measurable. From there, the CMIO or VP of Operations expands us to adjacent departments on a standard addendum; no new procurement cycle. The 112% NRR is the proof that this expansion motion works in practice, not just in theory. Gross margin at 73% is sustainable because our cost structure is primarily model inference (declining with scale) and implementation labor (declining as we build self-serve onboarding). LTV/CAC at 6.8x is above the SaaS benchmark of 3x for enterprise software. CAC payback at 8.7 months means we recover our sales cost before the average contract is 40% complete. The 24-month average contract length gives us 15+ months of contracted recurring revenue per customer at signing — important for modeling the Series A deployment timeline.
-->

---

# Team

## Built for This Specific Problem

| Name | Role | Background |
|---|---|---|
| **Priya Nair, MD** | CEO | Former CMIO, UCSF Medical Center; Stanford GSB MBA; 14yr clinical + ops |
| **Daniel Cho** | CTO | Led ML platform at Optum (50M patient records); MIT EECS PhD |
| **Rachel Torres** | VP Sales | Scaled Olive AI from $0 &#8594; $80M ARR; enterprise health system motion |
| **James Wu, MD** | Chief Medical Officer | Former CMS prior-auth policy lead; wrote the 2024 interoperability rules |
| **Fatima Al-Hassan** | VP Engineering | Azure Health Data Services engineering lead (5yr); FHIR standards committee |

**Advisors:** Former CEO of Availity (distribution), Chief Strategy Officer of Epic (integration pathway), Partner at CMS Innovation Center (regulatory navigation).

<!-- Speaker notes:
The team slide at Series A must answer one question: why is this the team that wins? Each person on this slide has a specific, non-replaceable credential for this specific problem. Priya was a CMIO — she managed PA workflows from the clinical leadership chair and knows exactly what health system buyers need to hear. Daniel's Optum background means he has trained ML models on population-scale health data under HIPAA; most clinical AI teams have never done this. Rachel's Olive AI experience is the most directly applicable sales motion: enterprise SaaS sold into health system C-suites, beginning with a departmental land and expanding across the system. James Wu literally wrote the CMS rules that created the market we are operating in — he knows every payer compliance officer personally and has turned several into customer references. Fatima built Azure Health Data Services, which is the infrastructure Helix runs on; she has the FHIR standards committee relationships that keep us ahead of compliance changes. The advisor panel addresses the three questions investors ask about risk: can you distribute (Availity CEO), can you integrate (Epic CSO), and can you navigate regulation (CMS Innovation Center). The answer to all three is yes, and we have named proof.
-->

---

# Financials

## Path to $10M ARR by Q4 2027

| | 2025A | 2026E | 2027E |
|---|---|---|---|
| ARR | $0.8M | $3.2M | $10.4M |
| MRR at EOY | $67K | $267K | $867K |
| Gross Margin | 68% | 74% | 78% |
| Headcount | 12 | 21 | 38 |
| Net Burn / mo | $185K | $218K | $290K |

**Series A Ask:** $12M

| Use of Funds | Allocation |
|---|---|
| Sales & marketing (2 AEs, 1 SDR, demand gen) | 42% |
| Engineering (4 engineers — denial appeal, Cerner, payer portal) | 33% |
| Customer implementations (Head of Impl + partner model) | 15% |
| G&A + Series A legal/audit | 10% |

**Runway post-close:** 30+ months to $10M ARR milestone with 6-month buffer.

<!-- Speaker notes:
The financial slide is where many founders lose Sequoia partners because the numbers do not tell a coherent story. Ours does. 2025 actuals are auditable — $0.8M ARR with 12 people and $185K monthly burn. 2026 estimates are based on the 94 customers already under contract and a 22% MoM growth rate that we have sustained for 6 consecutive months. 2027 projections assume growth decelerating to 12% MoM as we exit the early-adopter segment and enter mainstream health systems — a conservative assumption relative to comparable SaaS growth curves at this ARR level. Gross margin expansion from 68% to 78% comes from three drivers: model distillation (lower inference cost), self-serve onboarding (lower implementation labor), and revenue mix shift toward the higher-margin denial appeal module. The $12M ask is sized to reach $10M ARR — the traditional Series B threshold — with 6 months of buffer. We are not asking for more than we need. The use-of-funds breakdown shows that 75% goes to revenue-generating activities (sales, engineering, implementations) and only 10% to overhead. Every dollar in this raise is pointed at the 500-health-system target. Breakeven is modeled at $4.2M ARR — a Q1 2027 event that means the business is self-sustaining before we deploy the full raise.
-->
