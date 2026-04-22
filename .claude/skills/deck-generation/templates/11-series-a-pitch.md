<!-- TEMPLATE: series-a-pitch
     CATEGORY: Pitch / Investor
     USE WHEN: raising Series A, want investor-ready narrative scaffold
     SLIDE COUNT: 12
     PALETTE: Dark premium
     RENDER: marp --pptx 11-series-a-pitch.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'DM Sans', 'Segoe UI', system-ui, sans-serif;
    background: #0a0e14;
    color: #d0d8e4;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', 'Georgia', serif;
    color: #ffffff;
    letter-spacing: -0.5px;
    font-size: 2.4em;
    line-height: 1.15;
    margin-bottom: 0.3em;
  }
  h2 {
    color: #a78bfa;
    font-size: 1.1em;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 {
    color: #3b9eff;
    font-size: 1em;
    font-weight: 600;
    margin-bottom: 0.4em;
  }
  strong { color: #3b9eff; }
  em { color: #a78bfa; font-style: normal; font-weight: 600; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "▸ "; color: #3b9eff; font-size: 0.9em; }
  ul li { margin-bottom: 0.6em; font-size: 1.05em; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9em;
  }
  th {
    background: #111820;
    color: #a78bfa;
    padding: 10px 14px;
    text-align: left;
    font-weight: 600;
    letter-spacing: 0.05em;
    font-size: 0.85em;
    text-transform: uppercase;
  }
  td { padding: 10px 14px; border-bottom: 1px solid #1e2a38; }
  tr:last-child td { border-bottom: none; }
  .metric-row { display: flex; gap: 48px; margin-top: 1.5em; }
  footer {
    font-size: 0.7em;
    color: #556677;
    position: absolute;
    bottom: 28px;
    right: 64px;
  }
  section::after {
    color: #556677;
    font-size: 0.75em;
  }
---

# Helix
## AI for Clinical Workflows

**The infrastructure layer that replaces manual prior-authorization.**

*Series A — April 2026 &nbsp;|&nbsp; Confidential*

<!-- Speaker notes:
Open with energy and brevity. "We are Helix. We eliminate the single most hated process in healthcare — prior authorization." Don't belabor the company name; everyone in the room has already seen the one-pager. Your goal on slide 1 is to set the emotional register: this is a large, solvable problem with a technically credible team standing in front of them. Pause after the tagline. Let it breathe. If you have a quick proof point — "Last month we processed 140,000 prior-auth requests across 11 health systems" — drop it here before advancing. Keep this slide under 30 seconds. The investor already knows your name; your job is to make them lean forward for slide 2.
-->

---

## The Problem

# Prior Auth Kills 250,000 Patient-Days Per Year

- Physicians spend **3 hours daily** on administrative approvals
- **17% of claims** denied on first submission — 90% are overturned on appeal
- Average approval cycle: **11 days** &nbsp;▸&nbsp; optimal: under 4 hours

<!-- Speaker notes:
This is your credibility slide. Investors have heard "healthcare is broken" a thousand times. You need to be specific and sourced. The 250,000 patient-days figure comes from the AMA's 2024 Prior Authorization Impact Survey — cite it if asked. The 3-hours-daily stat is from the same source. The 17% denial / 90% overturn pairing is the emotional gut-punch: most denials are wrong, they just get upheld because no one has time to fight them. Pause on the third bullet. "Eleven days. The test takes 20 minutes. The approval takes 11 days." That contrast is your hook into the next slide. Anticipate the "how big is this" question; that's slide 4 — tease it here: "This is a $14B administrative waste problem."
-->

---

## Why Now

# The Regulatory Window Is Open — For 18 Months

- CMS Interoperability Rule (Jan 2026): mandates **real-time PA API** by 2027
- AI reasoning models hit **clinical-grade accuracy** in Q3 2025
- EHR vendors racing to add PA — but **none own the workflow layer**

<!-- Speaker notes:
"Why now" is the slide many founders forget to make compelling. Your three points each represent a distinct forcing function. First, the regulatory deadline is real: hospitals that aren't compliant by Jan 2027 face Medicare reimbursement penalties. That creates urgency that has nothing to do with sales cycles. Second, the AI accuracy point matters because prior auth is a liability-sensitive domain — until GPT-4o-class reasoning hit 94% clinical accuracy on CMS criteria sets, this product couldn't exist responsibly. Third, the EHR gap is your market entry point: Epic, Cerner, Athena are all adding PA features but they're bolting them on. None of them will own the cross-payer, cross-system orchestration layer. That's us. If an investor pushes back on the window, be direct: "If we're wrong and the window closes, it's a headwind, not a wall. The efficiency case stands on its own."
-->

---

## Market

# $14B TAM — and the Mandate Accelerates Capture

| Segment | Size | Our Entry |
|---|---|---|
| Prior auth workflow software | $3.2B | Direct — health systems |
| Revenue cycle management | $6.1B | Adjacent — expand via billing |
| Payer-side decisioning | $4.7B | Future — API licensing |

*SAM (health systems 200+ beds, US): $1.1B*

<!-- Speaker notes:
Walk through the table top to bottom, but spend the most time on the SAM. The TAM is for credibility; the SAM is where your sales motion actually operates. $1.1B SAM against a $2.3M ARR starting point means you are at 0.2% penetration — that's not a ceiling story, that's a land-and-expand story. The payer-side row is important: don't oversell it as a current product, but do name it as a strategic expansion. Payer-side decisioning is where the real margin is — payers pay $25–40 per PA decision; health systems pay $8–12. If an investor asks about downmarket (smaller hospitals, clinics), acknowledge it: "We'll open a self-serve tier in 2027 once the API-first motion is proven." Don't let the market discussion drag past 90 seconds — get to traction.
-->

---

## Traction

# $2.3M ARR — 18% Month-over-Month

- **11 health systems** live &nbsp;▸&nbsp; **3 signed, deploying Q2 2026**
- Average contract: **$210K ARR**, 3-year terms
- **NPS 71** — physicians, not IT buyers, are the advocates

<!-- Speaker notes:
This is the slide investors will photograph. Rehearse the exact numbers cold. "Two point three million ARR, growing eighteen percent month over month. That's not a spike — we have been at 14% or above for 14 consecutive months." The three-bullets structure gives you three proof vectors: scale (11 systems), pipeline (3 deploying), and quality (NPS 71). The NPS point is differentiated — most enterprise health IT scores 20–40. 71 means physicians are evangelizing you internally, which dramatically reduces your CAC on expansion. If asked about churn: zero net churn to date; one customer upsold from $150K to $380K in year two. Anticipate "what happens when EHRs add this natively?" — answer on the next slide.
-->

---

## Product — Core Engine

# Helix Reasons, Negotiates, and Learns

- **Ingestion:** pulls clinical notes, labs, imaging directly from EHR via FHIR R4
- **Reasoning:** maps patient record to payer criteria; generates compliant PA request
- **Negotiation:** auto-appeals denials with supporting evidence; win rate **73%**

<!-- Speaker notes:
The product needs to be described functionally, not technically. Avoid "large language model" and "transformer" — say "clinical reasoning engine" if pressed. The three-step arc is your differentiator versus point solutions: most competitors do ingestion OR generation, not the full loop including appeals. The 73% appeal win rate is your moat claim — that number comes from 14 months of denial pattern data across 7 payers. Over time, the model gets better at each payer's specific criteria quirks. That's defensibility. If you have a live demo, offer it: "I can show the full 90-second PA cycle live — who wants to see it?" Don't show the demo unless you've rehearsed it cold on this specific laptop. Technical failures on this slide destroy credibility.
-->

---

## Product — Workflow Layer

# Built Into the Physician's Existing Screen

- **Zero new UI:** integrates as sidebar inside Epic, Cerner, Athena
- **One-click submit:** physician reviews, approves, submits — average **22 seconds**
- **Audit trail:** every decision logged, explainable, retrievable for compliance

<!-- Speaker notes:
The "zero new UI" point is the biggest adoption unlock in healthcare IT. Physicians have tool fatigue. Every new window, every new login, every new workflow step costs you adoption. We render inside their existing screen as a native extension — they never leave Epic. This is architecturally harder, but commercially it means our deployment cycle is 6 weeks, not 6 months. The 22-second stat is real, measured across 50,000 submissions. Contrast it with the current state: physicians describe the current PA workflow as "10–15 minutes of hunt, copy, paste, fax." From 15 minutes to 22 seconds. That's not an improvement, it's elimination. The audit trail bullet matters for compliance-minded buyers (and for investors thinking about liability) — every AI decision is explainable and reversible by a human. We are not replacing clinical judgment; we are eliminating administrative overhead.
-->

---

## Competition

# We Win on Completeness — Not Just Speed

| | Helix | Cohere Health | Olive AI | Epic Prio |
|---|---|---|---|---|
| EHR-native UI | Yes | No | No | Partial |
| Cross-payer appeals | Yes | No | Yes | No |
| Real-time FHIR R4 | Yes | Partial | No | Yes |
| Appeal win rate | 73% | 41% | N/A | N/A |
| Avg deploy time | 6 wk | 18 wk | 24 wk | 12 wk |

<!-- Speaker notes:
Name your competitors honestly. Investors hate evasiveness here more than competition. Cohere Health is well-funded and legitimate — acknowledge it: "Cohere is the most direct competitor. They are strong on the payer side; we are stronger on the health system side and on the appeals loop." Olive AI has had well-publicized struggles and has pivoted away from PA — don't gloat, just let the table speak. Epic Prio is the "free with Epic" objection you will face in every health system sales cycle. Your answer: "Epic Prio covers 40% of their own criteria mapping. We cover 100%, plus cross-payer, plus appeals, plus non-Epic EHRs. We integrate with Epic Prio rather than replacing it." The deploy-time row is a business-model advantage, not just a product advantage — 6 weeks to first revenue beats 18 weeks in any sales math.
-->

---

## Business Model

# Land on Workflow, Expand to Data Intelligence

- **Land:** per-PA transaction fee — **$4.80 per request** (vs $14 manual cost)
- **Retain:** platform fee — **$18K/year** per department for analytics + audit
- **Expand:** payer API — **$28 per decision** sold to payer's utilization management

*Gross margin: 74% at scale &nbsp;|&nbsp; CAC payback: 7 months*

<!-- Speaker notes:
Walk through the three tiers as an expansion motion, not three separate products. Every customer starts on the transaction fee. At 12 months, we pitch the analytics platform — it sells itself because the compliance team has already been pulling the audit logs manually. At 24 months, we approach the payer side as a data product — our denial pattern data is worth more to a payer than to the health system, and the payer margin is 3x. The 74% gross margin is current — not projected. We are already at scale on the infrastructure cost side. CAC payback of 7 months is calculated on fully-loaded sales and onboarding costs. If asked about pricing sensitivity: "We've tested $3.50 to $6.00. Price elasticity is low because we are replacing a $14 cost. The question customers ask is not whether to buy — it is how fast they can deploy."
-->

---

## Team

# Operators Who Have Run This Problem From Both Sides

- **CEO: Sarah Chen** — former VP Clinical Informatics, Sutter Health &nbsp;|&nbsp; Stanford CS
- **CTO: James Okafor** — led prior auth API at Change Healthcare before exit
- **Head of Clinical: Dr. Priya Mehta** — practicing hospitalist, UCSF &nbsp;|&nbsp; 12 published papers on PA reform
- **Advisors:** Former CMS Deputy Administrator; Chief Medical Officer, Anthem

<!-- Speaker notes:
Team slide is where founder-market fit gets proven or disproven. Sarah's Sutter background means she has bought this product — she knows exactly what the procurement committee is going to ask because she was on it. James built the Change Healthcare API that Helix now integrates with — he has the technical credibility and the existing relationships with payer IT teams. Dr. Mehta is unusual: a practicing clinician who also codes. She runs physician focus groups monthly and directly informs product prioritization. The advisor names are credibility anchors — don't dwell on them, but do name them. Former CMS deputy administrator means we know how the regulatory clock works before it's published. Anticipate the "what's missing" question: "We are hiring a VP of Sales with EHR ecosystem experience. We have two finalists under offer." Show you know your own gaps.
-->

---

## The Ask

# Raising $18M Series A — Closing June 2026

- **Lead:** $12M for product, compliance infrastructure, and enterprise sales team
- **Use of funds:** 60% sales + CS &nbsp;|&nbsp; 25% R&D &nbsp;|&nbsp; 15% G&A
- **Target:** $9M ARR by Q4 2026 &nbsp;|&nbsp; 30+ health systems live

*We have term sheets from two strategic investors. Seeking a lead who accelerates the payer expansion.*

**Next step: 45-minute deep-dive. We will share live data room access today.**

<!-- Speaker notes:
Be crisp and confident on the ask. Do not apologize for the number. $18M Series A in clinical AI infrastructure is below-market for the traction level — frame it that way if challenged: "We are being capital-efficient. Our Series B will be the larger check, and we want to arrive there with proven unit economics." The use-of-funds breakdown signals financial maturity — you have a model, not just ambition. The "two term sheets" line creates social proof without being arrogant. Use it only if true. The CTA is specific: "45-minute deep-dive + data room." Never end with "let us know if you have questions" — end with a named next action and a timeline. Follow up within 24 hours with a calendar invite. If they don't take the meeting, ask for the specific objection — it is more useful than silence.
-->

---

## Appendix — Key Metrics

| Metric | Value | Period |
|---|---|---|
| ARR | $2.3M | March 2026 |
| MoM growth | 18% | 14-month average |
| Customers | 11 live, 3 deploying | |
| NPS | 71 | Q1 2026 |
| Gross margin | 74% | Q1 2026 |
| CAC payback | 7 months | |
| Appeal win rate | 73% | all-time |
| Avg contract | $210K ARR | |
| Runway (pre-raise) | 14 months | |

<!-- Speaker notes:
This slide belongs in the appendix — do not advance to it during the main pitch. It exists for the data room and for the Q&A session where an investor wants to verify a number you cited. Have this slide loaded and ready to navigate to instantly. If you are asked a metric and it's on this table, say "let me pull the appendix" — it signals you know your numbers precisely. If a number has changed since you last rehearsed, update this table before the meeting. Nothing destroys credibility faster than a discrepancy between a cited number and the slide behind it. This table should reconcile exactly with your data room model. Treat it as a contract, not a summary.
-->
