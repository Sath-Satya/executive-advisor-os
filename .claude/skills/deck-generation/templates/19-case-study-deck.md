<!-- TEMPLATE: case-study-deck
     CATEGORY: Sales / Proof
     USE WHEN: single customer case study for sales use, conference presentation, or website download
     SLIDE COUNT: 9
     PALETTE: Clean light
     RENDER: marp --pptx 19-case-study-deck.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'DM Sans', 'Segoe UI', system-ui, sans-serif;
    background: #ffffff;
    color: #1c1a18;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', 'Georgia', serif;
    color: #1c1a18;
    letter-spacing: -0.4px;
    font-size: 2.2em;
    line-height: 1.15;
    margin-bottom: 0.3em;
  }
  h2 {
    color: #3b9eff;
    font-size: 0.88em;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 { color: #1c1a18; font-size: 1.05em; font-weight: 700; }
  strong { color: #3b9eff; }
  em { color: #8899ac; font-style: normal; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "• "; color: #3b9eff; }
  ul li { margin-bottom: 0.6em; font-size: 1.02em; line-height: 1.55; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9em;
  }
  th {
    background: #f4f6f8;
    color: #8899ac;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.06em;
    font-size: 0.82em;
    text-transform: uppercase;
    border-bottom: 2px solid #e0e6ed;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #f0f2f5; }
  tr:last-child td { border-bottom: none; }
  blockquote {
    border-left: 4px solid #3b9eff;
    padding: 14px 24px;
    margin: 1em 0;
    background: #f4f9ff;
    border-radius: 0 8px 8px 0;
    font-style: italic;
    color: #1c1a18;
    font-size: 1.08em;
    line-height: 1.6;
  }
  .big-metric {
    font-size: 3.4em;
    font-weight: 800;
    color: #3b9eff;
    letter-spacing: -1px;
    line-height: 1;
    display: block;
  }
  .big-label {
    font-size: 0.95em;
    color: #8899ac;
    margin-top: 0.2em;
    display: block;
  }
  section::after { color: #c0cad4; font-size: 0.75em; }
---

## Case Study

# How Mercy Health Recovered 2.5 FTE and Cut Denials by 76%

**Client:** Mercy Health System &nbsp;|&nbsp; **Industry:** Healthcare / Integrated Delivery Network
**Size:** 1,200 beds, Epic EHR &nbsp;|&nbsp; **Location:** Chicago, IL &nbsp;|&nbsp; **Deployment:** November 2024

<!-- Speaker notes:
Case study decks serve two audiences: the salesperson who uses them in a meeting and the prospect who downloads them as a PDF. Both audiences need the same thing on slide 1: enough context to know if this story is relevant to them. The client profile on the subtitle line — size, EHR, city — answers "is this comparable to my organization?" within 5 seconds. If you have secured permission to use the client's logo, place it in the top right corner — the visual recognition builds immediate credibility. If the client requested anonymity, use "A 1,200-bed integrated delivery network, Chicago, IL" — do not fabricate names. The deployment date (November 2024) sets the timeline: this is 16 months of production data, not a 30-day pilot. That duration matters for credibility — it rules out novelty effects and early-adopter bias.
-->

---

## The Client

# Mercy Health System — At a Glance

- **12 hospitals** across the greater Chicago metro area
- **$2.1B annual revenue** — primarily fee-for-service reimbursement
- **EHR:** Epic (fully implemented 2021)
- **PA volume:** 28,000 prior authorization requests per year
- **Pre-Helix PA team:** 3 full-time revenue cycle analysts, 1 supervisor

*Mercy's operational model relies on efficient revenue cycle performance. Administrative overhead is a direct margin risk.*

<!-- Speaker notes:
The client profile slide establishes comparability for the prospect reading this case study. Lead with size (12 hospitals, $2.1B revenue) and PA volume (28,000 per year) — these are the numbers a prospect uses to calibrate "is this like us?" The "3 FTE + 1 supervisor" staffing model is important context for the results slide: Mercy had dedicated PA staff, which means the Helix impact represents redeployment of real people, not just process savings. The final line — "Administrative overhead is a direct margin risk" — is the framing that connects the client's business context to why they were motivated to act. Every case study should answer three questions: who was the client, what was their situation, and why did they need to change? This slide answers the first two; the challenge slide answers the third.
-->

---

## The Challenge

# Three Problems — All Rooted in Manual Process

- **Denial rate:** 19% first-pass denial rate (vs. 17% national average) — above benchmark
- **Cycle time:** 12-day average PA approval cycle — delaying elective procedures
- **Staff burden:** 3 FTE spending 85% of their time on repetitive form-filling, not exceptions

*Root cause identified: no automation at the submission stage — every request built manually from chart notes*

<!-- Speaker notes:
The challenge slide is written from the client's perspective, not Helix's. Do not use product language here. The three problems are operational facts: Mercy's denial rate was above benchmark, their cycle time was longer than peers, and their staff was under-utilized on low-value work. The root cause line — "no automation at the submission stage" — is the diagnosis that leads naturally to the solution. If you did a discovery call with Mercy before deployment, quote from it if you have permission: "The VP of Revenue Cycle told us, 'Our team is spending most of their time on the obvious approvals that should never require human involvement.'" That kind of quote is more persuasive than analyst data because it is specific to this client. The challenge slide should make the prospect nod: "That sounds exactly like us." If they do not nod, this case study is not the right one for this prospect.
-->

---

## The Approach

# Phased Deployment — Low Risk, Fast Value

| Phase | Activity | Timeline |
|---|---|---|
| 1 — Configure | FHIR R4 Epic connection, payer credential setup | Weeks 1–3 |
| 2 — Pilot | Cardiology department live — 200 PA/month | Weeks 4–6 |
| 3 — Measure | 6-week pilot results, physician feedback | Weeks 7–9 |
| 4 — Scale | Expand to all 12 departments — 2,300 PA/month | Weeks 10–16 |
| 5 — Optimize | Denial pattern tuning, appeals model refinement | Ongoing |

*Total deployment timeline: 16 weeks from contract to full production*

<!-- Speaker notes:
The approach slide tells the prospect "what the deployment felt like from the inside." This is where you address the unstated fear: "Will this be a painful, multi-year IT project?" The answer is no — 16 weeks from contract to full production. Phase 1 (FHIR configuration) is the only IT-intensive phase; Mercy's Epic admin handled it in 3 days. Phase 2 (cardiology pilot) is the risk-mitigation phase — starting with one department means any issues are contained. Phase 3 (measure) is the decision gate: Mercy's leadership reviewed 6-week pilot results before committing to the full rollout. The 6-week checkpoint is a risk-reduction mechanism that every health system should understand before they sign. If your deployment at Mercy hit any unexpected issues during phases 1–4, describe them and how you resolved them — it builds more trust than a frictionless story.
-->

---

## The Solution

# Helix Prior Authorization Platform — How It Works at Mercy

- **EHR integration:** Helix sidebar inside Epic — visible when a PA-required order is placed
- **AI submission:** reads clinical note, maps to Aetna/BCBS/United criteria, submits in 22 seconds
- **Auto-appeals:** denial triggers evidence assembly and appeal submission in under 4 minutes
- **Analytics:** real-time dashboard showing department-level denial rates, cycle times, and FTE hours

*Configuration: 8 payers connected, 4 specialties, 2,300 PA requests per month processed*

<!-- Speaker notes:
The solution slide is where you connect Mercy's specific setup to the Helix product. Use Mercy's actual payer mix (Aetna, BCBS, United) and their actual volume (2,300 PA/month) — specificity is credibility. The four bullets map directly to the four problems identified in the challenge slide: the EHR integration addresses the "manual form-filling" problem; AI submission addresses the cycle time problem; auto-appeals addresses the denial problem; analytics enables the root cause monitoring that was missing before. If you have a screenshot of the Helix dashboard from Mercy's actual deployment (de-identified), include it on this slide or the next one. Visual evidence — even a cropped dashboard screenshot — is more persuasive than any number of descriptive bullets.
-->

---

## The Results — 90 Days

# Three Metrics That Changed Everything

| Metric | Before Helix | After 90 Days | Change |
|---|---|---|---|
| First-pass denial rate | 19% | **4.7%** | **-75%** |
| Average PA cycle time | 12 days | **2.8 days** | **-77%** |
| Staff time on PA (weekly) | 126 hours | **19 hours** | **-85%** |
| Appeal win rate | 38% (manual) | 73% (Helix) | **+92%** |
| Physician NPS | 18 | **71** | **+295%** |

*Measured at 90-day mark (February 2025). 16-month data available in extended case study.*

<!-- Speaker notes:
The results slide is the payoff for everything that came before it. Every number should be exact and verifiable — these are Mercy's actual numbers, not rounded approximations. The percentage changes are calculated from the exact figures, not estimated. Walk through the table top to bottom with a brief narrative for each row: "Denial rate from 19% to 4.7% — that's 3,400 fewer denied claims per year at Mercy's volume. Cycle time from 12 days to 2.8 days — procedures that were waiting almost two weeks are now approved in under 3 days. Staff time from 126 hours to 19 hours — that's 107 hours per week freed from form-filling." The physician NPS number deserves emphasis: "From 18 to 71 in 90 days. Physicians went from frustrated to advocates. That NPS score is what drives internal expansion." The footnote about 16-month data available positions the extended case study as a deeper resource for serious prospects.
-->

---

## In Their Words

> "Prior authorization used to be a daily source of frustration for our entire cardiology team. Within six weeks of going live with Helix, I had a cardiologist stop me in the hallway to ask if we could expand it to orthopedics. That has never happened with a software rollout in my 12 years here."
>
> — Lisa Park, VP Revenue Cycle, Mercy Health System

*Reference available: Lisa Park is available for 15-minute peer reference calls on request.*

<!-- Speaker notes:
The customer quote is the single most persuasive element in a case study deck. It must be verbatim, attributed, and permission-granted. The quote works on multiple levels: it is specific ("six weeks"), it shows unsolicited advocacy from physicians (not just from the buyer), and it contextualizes the impact for a healthcare audience ("12 years here" — this is not a junior manager who gets excited about every new tool). The reference availability line is extremely valuable: "Lisa Park takes reference calls" converts a slide into a sales tool. Before publishing this case study, confirm with Lisa that she is willing to take calls and what her preferred contact method is. A reference who agrees in principle but does not respond to prospect inquiries is worse than no reference at all. Coach references on the two or three things to emphasize: the physician adoption story and the appeal win rate.
-->

---

## Lessons and Transferability

# What Mercy's Experience Tells Us About Deployment

- **Start with cardiology or orthopedics** — highest PA volume, fastest ROI, physician advocates
- **Get the VP of Revenue Cycle as champion** — they own the business case; IT follows
- **Pilot for 6 weeks before scaling** — creates internal confidence and generates proof points
- **The analytics dashboard accelerates expansion** — leadership can see the ROI in real time

*Mercy's playbook is now used as the standard deployment guide across all Helix customers.*

<!-- Speaker notes:
The lessons slide transforms a single case study into actionable guidance for the next customer. This slide is especially valuable for prospects who are in the early stages of evaluation — it tells them what to do to succeed. The "start with cardiology or orthopedics" recommendation is specific and practical. The "get the VP of Revenue Cycle as champion" point is a soft ask: if your prospect contact is not the VP of Revenue Cycle, this slide is a signal that you need that stakeholder in the room. The "Mercy's playbook" line signals operational maturity: you have a repeatable deployment process, not a one-off success. If you have a one-page deployment guide derived from Mercy's experience, offer it as a leave-behind: "We have a 4-page deployment guide based on what worked at Mercy — I'll send it over after this meeting."
-->

---

## Next Steps

# Ready to Write Your Own Case Study?

- **See it live:** 20-minute demo using your EHR and a sample from your payer mix
- **Model your ROI:** provide your PA volume and denial rate &nbsp;▸&nbsp; we build a custom projection
- **Talk to Mercy:** reference call with Lisa Park — 15 minutes, no sales rep on the call

*Reference organizations at comparable size: Mercy Health (1,200 beds), St. Catherine's (800 beds), Riverside Regional (600 beds)*

**Contact: sarah.chen@helix.health &nbsp;|&nbsp; (415) 555-0192 &nbsp;|&nbsp; helix.health/meet**

<!-- Speaker notes:
The closing slide of a case study should convert interest into a next action. Three options with increasing commitment level: the demo is the lowest bar; the ROI model requires them to share data but produces a specific, personalized output; the reference call is the highest-trust option and the most persuasive for a late-stage skeptic. The "no sales rep on the call" offer for the reference call is important: it removes the fear that the reference call will be a sales conversation. Prospects value unmediated peer conversations. The three reference organizations at the bottom give prospects a choice: "Which of these is most comparable to your organization?" That question starts a needs-discovery conversation naturally. Follow up after distributing this case study with a specific offer: "Which of the three next steps makes most sense given where you are in your evaluation?" Asking for a choice is more productive than asking for a meeting.
-->
