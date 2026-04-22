<!-- TEMPLATE: strategic-plan-deck
CATEGORY: Executive
USE WHEN: Multi-year strategic plan presentation to board, leadership team, or investors covering mission, vision, pillars, initiatives, and investment.
SLIDE COUNT: 12
PALETTE: Executive cream
RENDER: marp --pptx 06-strategic-plan-deck.md   (produces 06-strategic-plan-deck.pptx)
-->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&family=DM+Serif+Display&family=DM+Mono&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #f7f4ef;
    color: #1c1a18;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', serif;
    color: #0e1b2e;
    font-size: 2.2em;
    letter-spacing: -0.5px;
    margin-bottom: 0.2em;
  }
  h2 { color: #b8965a; font-size: 0.92em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5em; }
  h3 { color: #0e1b2e; font-size: 1.1em; margin: 0.8em 0 0.3em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.87em; }
  li { margin-bottom: 0.4em; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.86em; margin-top: 0.7em; }
  th { background: #0e1b2e; color: #f7f4ef; padding: 0.48em 0.78em; text-align: left; }
  td { padding: 0.44em 0.78em; border-bottom: 1px solid #e0dcd4; }
  tr:nth-child(even) td { background: #f0ece4; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.7em; color: #6b6560; }
  section.lead h1 { font-size: 2.8em; }
  section.lead p { font-size: 1.1em; color: #6b6560; }
  section.pillar { background: #0e1b2e; color: #f7f4ef; }
  section.pillar h1 { color: #f7f4ef; font-size: 2.2em; }
  section.pillar h2 { color: #b8965a; }
  section.pillar li { color: #d0c8b8; }
  section.pillar strong { color: #f7f4ef; }
---

<!-- _class: lead -->

# Meridian Health — Strategic Plan 2026–2028

**Executive Leadership Team &nbsp;|&nbsp; Strategy Offsite**

*November 2025 — Three-Year Plan*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
This is a strategy offsite, not a quarterly review. Set the register accordingly: you are here to think big and make binding decisions about where the company is going over the next three years. Day-to-day operational concerns are explicitly out of scope for this session.

Distribute the pre-read (market analysis, competitive landscape, financial model) 48 hours in advance and expect participants to arrive having read it. Do not summarize the pre-read in the session — start from it.

Ground rules for the offsite: decisions made here become commitments. If a pillar or initiative is approved today, it enters the operating plan and gets resourced. If something is not approved, it goes to a parking lot — it is not killed, but it is not funded. This distinction matters for how people engage.
-->

---

## Mission — Why Meridian Exists

**Mission:** Make the administrative burden of healthcare invisible so clinicians and patients can focus on health.

**Vision:** By 2028, every health plan in the United States that covers more than 50,000 members uses AI-assisted administration — and Meridian is the platform that makes it possible.

**Why this matters:** The US healthcare system spends $496 billion annually on administrative overhead. Every dollar saved is a dollar that can go to care. We are not building software — we are redistributing resources back to patients.

<!--
SPEAKER NOTES — SLIDE 2 (Mission/Vision)
Do not rush through this slide. The mission and vision are not wallpaper — they are the strategic filter for every decision in this plan. Every initiative, investment, and trade-off should be evaluated against: does this make administrative burden invisible? Does this help us own the 50,000+ member plan market by 2028?

On the $496 billion figure: this is from CMS administrative cost analysis (2024). The number is defensible and striking. Use it whenever you are asked "how big is the opportunity?" — the answer is that even capturing 1% of the waste is a $4.9 billion market.

On the vision: "every health plan that covers more than 50,000 members" is a deliberate scope constraint. It rules out the small-plan market and focuses our go-to-market on the enterprise and upper mid-market segments. This is a strategic choice, not a limitation. Smaller plans are not our ICP.
-->

---

## Strategic Context — The Three Forces Shaping 2026–2028

**Force 1 — Regulatory acceleration**
CMS mandates, state prior auth rules, and value-based care contracts are creating a compliance imperative that makes AI adoption non-optional for health plans.

**Force 2 — Labor market pressure**
Health plan administrative headcount is down 11% since 2022. Plans cannot hire their way out of backlogs — they must automate or fall behind.

**Force 3 — AI commoditization risk**
Foundational AI is becoming a commodity. The moat is no longer the model — it is the integration depth, training data, and workflow embedding.

*Our plan is built to capitalize on Forces 1-2 and defend against Force 3.*

<!--
SPEAKER NOTES — SLIDE 3 (Strategic Context)
The three forces frame is important because it grounds the strategy in external reality, not internal ambition. We are not building to our strengths in a vacuum — we are responding to a specific market configuration.

On Force 3 (AI commoditization): this is the existential question the board will ask. "What stops a hyperscaler from replicating your product?" The honest answer is: the model cannot be easily replicated, but the integrations and training data can be defended. Our strategy is to deepen integration with the 47 plans already live before competitors have the training data to compete. This is a time-sensitive advantage, which is why speed of execution matters so much in the 2026-2027 window.

Ask the room: "Are there forces we are not seeing?" This generates genuine strategic debate and surfaces blind spots before the plan is set.
-->

---

<!-- _class: pillar -->

## Pillar 1 of 3

# Own the Claims Intelligence Layer

**What it means:** Every health plan on our platform delegates claims intelligence decisions to Meridian's AI — not as a feature, but as a core operational system of record.

**Target by 2028:**
- 100% of active health plans using Claims AI for primary decisioning
- 80% reduction in manual claims review for platform customers
- Claims AI API available to non-Meridian systems (open platform)

*Current state: 47 plans, 51% review reduction. Target: 120 plans, 80% reduction.*

<!--
SPEAKER NOTES — SLIDE 4 (Pillar 1)
Pillar 1 is the core product strategy. "System of record" is the key phrase — we are not a feature in someone else's workflow; we are the platform they build their workflow on. This is the difference between a vendor and a platform company, and it is what justifies the revenue multiple we want to command.

On the open API strategy: this is the most debated element of Pillar 1. The concern is that opening the API allows competitors to build on our infrastructure. The counterargument is that platform businesses win by having the most integrations and the most data — both of which increase as usage increases. The analog is Salesforce opening its AppExchange: third-party apps made Salesforce indispensable, not replaceable.

Surface the open API debate explicitly here and let the room engage. This is the right forum to make that call.
-->

---

<!-- _class: pillar -->

## Pillar 2 of 3

# Expand the Addressable Surface

**What it means:** Move from claims processing into adjacent administrative workflows — member services, prior authorization, care coordination — without leaving our core competency.

**Target by 2028:**
- Prior Authorization AI: launched Q1 2026, 30 plans by year-end
- Member Services AI: launched Q3 2026, 20 plans by year-end
- Care Coordination workflows: design phase 2026, launch 2027

*Revenue contribution from adjacencies: $0 today → $42M by 2028 (17% of plan revenue)*

<!--
SPEAKER NOTES — SLIDE 5 (Pillar 2)
Pillar 2 is the growth strategy. It answers the question: "What do we sell to existing customers after Claims AI?" The three adjacencies are sequenced deliberately — Prior Auth is already in development, Member Services requires new NLP capabilities, and Care Coordination requires a different data model.

On the $42M adjacency revenue target: this assumes 30 plans on Prior Auth at $400K ARR average, 20 plans on Member Services at $500K ARR, and 15 early Care Coordination pilots at $300K. These are conservative estimates based on pricing experiments in Q3.

The risk for Pillar 2 is product focus. Expanding into adjacencies too fast can degrade core product quality. The sequencing — Prior Auth in 2026, Member Services in 2026, Care Coordination in 2027 — is designed to allow each product to reach maturity before the next one is resourced.
-->

---

<!-- _class: pillar -->

## Pillar 3 of 3

# Build the Network — Data as Compounding Moat

**What it means:** Each health plan that joins the platform makes the AI smarter for all other plans. This flywheel is the structural defense against commoditization.

**Target by 2028:**
- 120 plans on platform generating shared, anonymized training signal
- Benchmark dataset: largest in health plan administration (100M+ claims processed)
- Data governance framework: HIPAA-compliant federated learning model in production

*The 47 plans live today have generated 8.7M training examples. At 120 plans, that is 22M+ — a dataset no competitor can acquire without 3+ years of deployment.*

<!--
SPEAKER NOTES — SLIDE 6 (Pillar 3)
Pillar 3 is the moat strategy. The core insight is that our competitive advantage compounds with scale — unlike a traditional software company where all customers get the same product, our customers get a better product as more customers join. This is a network effect, not a scale effect.

On the federated learning model: this is the technical approach that allows us to improve the AI using data from all 47 plans without ever transferring identifiable data between customers. Each plan's data stays in their environment; only model weights and gradient updates are shared. This is the HIPAA-compliant solution that our legal and privacy team approved in Q2.

The $3M investment in data infrastructure in 2026 (see slide 10) is the price of building this moat. At 120 plans, this infrastructure pays for itself in competitive defensibility within 18 months.
-->

---

## Priority Initiatives — 2026 Execution Plan

| Initiative | Pillar | Owner | FY2026 Budget | Launch |
|---|---|---|---|---|
| Prior Authorization AI — GA | 2 | CTO | $3.2M | Q1 2026 |
| Claims AI Open API | 1 | CTO + CPO | $1.8M | Q3 2026 |
| Federated Learning Infrastructure | 3 | CTO | $3.0M | Q2 2026 |
| Pacific Southwest Market Entry | 2 | CRO | $4.2M | Q2 2026 |
| Member Services AI — MVP | 2 | CPO | $2.1M | Q3 2026 |
| Enterprise Data Team (4 hires) | 3 | CPO | $1.6M | Q1 2026 |

**Total 2026 strategic investment: $15.9M**

*All initiatives approved as a package or individually — board discretion on tranche release.*

<!--
SPEAKER NOTES — SLIDE 7 (Initiatives)
Six initiatives, six owners, clear budgets and launch dates. This table is the operating contract between the leadership team and the board.

Walk through each row: Prior Auth is the highest-priority near-term initiative because the CMS mandate window is open now. Claims AI Open API is the strategic bet with the longest payback period. Federated Learning is table stakes for Pillar 3. Pacific Southwest is the only geographic expansion. Member Services AI is the second adjacency. Enterprise Data Team is the people investment that enables all three pillars.

On the package vs. individual approval: if the board wants to fund a subset, the priority order is Prior Auth → Federated Learning → Pacific Southwest → Claims AI Open API → Member Services AI → Data Team. This is explicitly stated so the board can make a partial approval decision cleanly.
-->

---

## Milestones — The 2026–2027 Roadmap

**2026 — Build and launch**
- Q1: Prior Auth AI GA + enterprise data team hired
- Q2: Pacific Southwest market launch + federated learning infrastructure deployed
- Q3: Claims AI Open API beta + Member Services AI MVP to 5 pilot plans
- Q4: Full-year revenue $240M; 90 plans on platform

**2027 — Scale and defend**
- Q1: Member Services AI GA to 20 plans
- Q2: Care Coordination design review + board approval for 2027-2028 tranche
- Q3: Open API partner program launched (10 certified third-party integrations)
- Q4: Full-year revenue $310M; 120 plans on platform; benchmark dataset milestone

<!--
SPEAKER NOTES — SLIDE 8 (Milestones)
The milestone roadmap is a commitment calendar. Every milestone named here will be reviewed at the relevant QBR or board meeting. Name the review mechanism: "Each of these milestones has a corresponding board gate — we will not advance a Q3 initiative without confirming Q2 milestones are green."

On the $310M target for 2027: this is the sum of $183M existing base growing at NRR 118% for two years ($255M) plus $55M from new initiatives at plan close rates. The model is in the data room.

On Care Coordination design review in Q2 2027: we are deliberately not committing to a 2027 launch for Care Coordination. The Q2 design review is a gate — if the market timing is right and the prior initiatives are stable, we proceed. If not, we defer and redeploy the budget. This is intentional optionality, not indecision.
-->

---

## KPIs — How We Measure Strategic Progress

| KPI | 2025 Baseline | 2026 Target | 2027 Target | 2028 Target |
|---|---|---|---|---|
| Health plans on platform | 47 | 90 | 120 | 150 |
| Annual Recurring Revenue | $183M | $240M | $310M | $390M |
| Gross Margin | 63.4% | 64.5% | 66.0% | 68.0% |
| NRR | 118% | 120% | 122% | 125% |
| Claims processed (annual) | 8.7M | 18M | 28M | 40M |
| Prior Auth reviews automated | 0 | 500K | 2.1M | 4.5M |

*KPIs reviewed at each quarterly board meeting. Targets may be revised annually.*

<!--
SPEAKER NOTES — SLIDE 9 (KPIs)
Six KPIs, three-year targets. These are the metrics the board will use to evaluate whether the strategy is working. Walk through the logical chain: plans on platform drives revenue, margin expands as infrastructure costs are amortized, NRR expands as adjacencies deepen retention.

On the gross margin trajectory to 68%: this assumes the Claims AI infrastructure costs are largely fixed and new plan additions are high-margin incremental revenue. The assumptions are in the financial model. If the federated learning infrastructure investment comes in over budget, margin expansion could be 1-2 points slower — still positive but less dramatic.

On Prior Auth reviews automated: this number goes from 0 to 4.5M in three years. That is 4.5 million clinical decisions per year where a health plan employee does not have to manually review a request. At an average of 15 minutes per review, this is 1.1 million hours of clinician and administrator time returned to patient care annually. That is the mission in numbers.
-->

---

## Investments — Three-Year Capital Requirements

| Year | R&D | Sales & Marketing | Infrastructure | G&A | Total OpEx |
|---|---|---|---|---|---|
| 2026 | $28.4M | $18.2M | $12.1M | $19.8M | $78.5M |
| 2027 | $32.1M | $21.4M | $10.8M | $21.2M | $85.5M |
| 2028 | $34.8M | $24.6M | $9.4M | $23.1M | $91.9M |

**Three-year cumulative investment: $255.9M**

**Three-year cumulative revenue: $940M** *(if targets met)*

**Operating margin trajectory:** 15% (2026) → 21% (2027) → 28% (2028)

<!--
SPEAKER NOTES — SLIDE 10 (Investments)
The financial summary. Three years of investment against three years of projected revenue. Operating margin expanding from 15% to 28% — this is the path to profitability without sacrificing growth.

On the R&D investment: growing from $28.4M to $34.8M over three years, but declining as a percentage of revenue (from 11.8% to 8.9%). This is a sign of operating leverage — we are not becoming a mature, slow-growth company; we are scaling efficiently.

On infrastructure costs declining: $12.1M → $10.8M → $9.4M despite significant platform growth. This reflects the Azure cloud architecture providing elastic scaling at lower marginal cost. The federalized learning infrastructure has high setup cost but near-zero marginal cost per additional plan.

If a board member asks about the path to profitability: at 28% operating margin on $390M revenue, operating income in 2028 is $109M. This is the basis for a Series D or IPO conversation in 2028. Do not promise a timeline, but do not avoid the question.
-->

---

## Risks — Three-Year Horizon

**Risk 1 — Competitive response (High likelihood, High impact)**
Mitigation: Federated learning data moat + deep integration lock-in. Window is 2026.

**Risk 2 — Regulatory environment shifts (Medium, High)**
Mitigation: Contract structures hedge 18-24 months; government relations investment in 2026.

**Risk 3 — Product quality under expansion pressure (Medium, Medium)**
Mitigation: Sequential roadmap prevents over-stretch; dedicated QA function added Q1 2026.

**Risk 4 — Key person departure — CTO (Low, High)**
Mitigation: Succession plan approved; retention package in effect through 2028.

<!--
SPEAKER NOTES — SLIDE 11 (Risks)
Strategic plans that do not include risks are plans that have not been honestly evaluated. Present these risks with the same confidence you present the opportunities — the board will trust the plan more if they see you have thought about what can go wrong.

On competitive response: this is the highest-rated risk for good reason. The 2026 window is the critical period. If we execute Pillars 1-3 in 2026, by 2027 we will have a dataset and integration depth that is structurally difficult to replicate. If we do not execute in 2026, we remain vulnerable.

On product quality: the risk of expanding too fast is real. The sequencing mitigation is deliberate, but it requires leadership discipline to resist pressure to launch adjacencies before they are ready. The board should hold management to the sequenced timeline even if market demand creates pressure to accelerate.
-->

---

## Close — The Decision Before This Team

**We are asking this leadership team to commit to three things:**

1. **The pillars are the pillars** — Claims Intelligence, Adjacency Expansion, and the Data Network are the strategy for 2026-2028. All major investment decisions will be evaluated against them.

2. **The sequencing holds** — We will not launch Member Services AI before Prior Auth is stable. We will not pursue acquisitions while organic opportunities remain large.

3. **The KPIs are the contract** — We will report honestly against these targets at every board meeting. We will not rebase targets without explicit board approval and a rationale.

*With these commitments in place, we are ready to build.*

<!--
SPEAKER NOTES — SLIDE 12 (Close / Commitments)
End on the commitment, not the vision. The vision was slide 2. This slide is about what the people in this room are agreeing to do for the next three years.

Read the three commitments clearly and ask for explicit agreement from each executive present. Go around the table. This is not a formality — it is the governance moment. People who agree publicly to commitments follow through at higher rates than people who nod and move on.

If there is disagreement with any of the three commitments, surface it now. Better to spend 30 minutes in a productive debate about pillar prioritization today than to have that debate play out in resource allocation arguments over the next six months.

After the agreement, close the session: "We have a plan. Now we execute."
-->
