<!-- TEMPLATE: yc-style-pitch
     CATEGORY: Pitch / Investor
     USE WHEN: YC application, demo day, or any ultra-concise seed pitch
     SLIDE COUNT: 10
     PALETTE: Dark premium (minimalist)
     RENDER: marp --pptx 12-yc-style-pitch.md -->
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
    padding: 56px 72px;
  }
  h1 {
    font-family: 'DM Serif Display', 'Georgia', serif;
    color: #ffffff;
    letter-spacing: -0.5px;
    font-size: 2.6em;
    line-height: 1.1;
    margin-bottom: 0.25em;
  }
  h2 {
    color: #556677;
    font-size: 0.95em;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 1.2em;
  }
  strong { color: #3b9eff; }
  em { color: #a78bfa; font-style: normal; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "— "; color: #3b9eff; }
  ul li { margin-bottom: 0.7em; font-size: 1.1em; line-height: 1.5; }
  .big-stat {
    font-size: 3.2em;
    font-weight: 800;
    color: #3b9eff;
    letter-spacing: -1px;
    line-height: 1;
  }
  .big-label {
    font-size: 1em;
    color: #8899ac;
    margin-top: 0.2em;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.92em;
  }
  th {
    background: #0e1620;
    color: #556677;
    padding: 10px 16px;
    text-align: left;
    font-weight: 600;
    letter-spacing: 0.06em;
    font-size: 0.8em;
    text-transform: uppercase;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #161e28; }
  tr:last-child td { border-bottom: none; }
  section::after { color: #2a3545; font-size: 0.75em; }
---

## Company

# Helix — Prior Auth in Under a Minute

**We automate the process that kills 250,000 patient-days per year.**

Helix connects to any EHR, reads the clinical record, and submits a compliant prior-authorization request — in 22 seconds.

<!-- Speaker notes:
YC pitches move fast. You have 10 minutes and 10 slides. This slide is 45 seconds max. Lead with the one-liner, then the one concrete proof point — "22 seconds." Everything else is elaboration. The best YC openers give the audience a crisp mental model before they have a chance to get confused. Helix: prior auth, fast, automated. That's the model. Do not explain what prior authorization is — if you are pitching YC, your audience has done diligence on healthcare. If you are adapting this for a non-healthcare audience, add one sentence: "Prior authorization is the insurance approval step required before 40% of all medical procedures — it currently takes 11 days." Advance quickly.
-->

---

## Problem

# Physicians Spend 3 Hours Daily Filling Out Forms

- Insurance requires approval for **40% of all procedures**
- Approval takes **11 days** on average — care is delayed
- **17% of claims** denied on first submission; most are overturned on appeal

The system is broken by design. Physicians lose. Patients lose. Payers pay more on appeals than they save on denials.

<!-- Speaker notes:
Two things this slide must achieve: make the investor feel the pain viscerally, and confirm that the problem is large and structural. The physician time stat (3 hours daily) creates an emotional anchor. The 11-day average is the rational case. The denial-overturn statistic is the systemic indictment: "The system denies claims not because they should be denied, but because the process is too painful to fight. We end that." Don't spend more than 60 seconds here. YC investors read ahead; many have already nodded at this slide. Your job is to confirm their intuition and move to the solution. Avoid the word "healthcare" as a vague bucket — be specific about the workflow (prior authorization) and the actor (physicians).
-->

---

## Solution

# Helix Submits, Tracks, and Wins Appeals — Automatically

- **Connect:** integrates with Epic, Cerner, Athena via FHIR R4
- **Reason:** AI maps patient record to payer criteria in real time
- **Close:** auto-appeals denials — **73% win rate**, no human involvement

<!-- Speaker notes:
Three bullets, three verbs, one outcome. This is the YC formula. Connect-Reason-Close maps cleanly to the physician workflow: we integrate into the existing tool, we do the thinking, we win the appeal. The 73% win rate is the number that makes investors pause. Emphasize it: "When the system wrongly denies a claim — and it does 17% of the time — we fight it and win 73% of those fights. Automatically. While the physician has already moved on to the next patient." The competitive moat is in that loop: most competitors do step one or two; nobody has closed the loop through appeals. If pressed on AI risk or clinical liability: "The physician reviews and approves every submission in 22 seconds. We generate; they decide. We are not autonomous clinical AI — we are administrative AI."
-->

---

## Market

# $3.2B Prior Auth Software Market — Growing at 22% CAGR

- **5,600** hospitals in the US &nbsp;▸&nbsp; **2,100** are our addressable target
- Average contract: **$210K ARR** &nbsp;▸&nbsp; SAM = **$441M**
- Adjacent expansion: revenue cycle management ($6.1B), payer decisioning ($4.7B)

<!-- Speaker notes:
YC wants to see that the market is big enough to build a billion-dollar company. $3.2B prior auth software market is not enormous on its own — that is why you name the adjacent markets. The $441M SAM is what your sales motion can actually address in the next 3–5 years. Be honest about this: "We are not claiming the $14B total healthcare admin market. We are claiming the $441M we can actually close with our current motion." Founders who overstate TAM lose credibility in Q&A. The CAGR matters because it means the market is moving toward you, not away — regulatory pressure is accelerating digital adoption in PA specifically. If asked about international: "US-only for the Series A. European payer systems are structurally different. That's a Series B decision."
-->

---

## Traction

# $2.3M ARR &nbsp;▸&nbsp; 18% MoM &nbsp;▸&nbsp; Zero Churn

- **11 health systems** live as of March 2026
- **3 additional** signed, deploying Q2 2026
- NPS **71** — driven by physician adoption, not just IT buyers

<!-- Speaker notes:
This is your credibility slide. Know every number cold. YC partners will probe: "What was MoM three months ago?" Answer: "16%, 17%, 18% — accelerating." "What is the oldest customer?" "Mercy Health System, 18 months live, just upsold from $150K to $380K." "Any churn?" "Zero net churn." Zero net churn in enterprise health IT is extraordinary — most products lose 1–2 customers per year in the first two years just from hospital consolidations and budget freezes. The NPS 71 is the proof that physicians — not just IT buyers — love this. That matters because physician advocacy is how you survive the annual IT budget review: the CMO goes to bat for you because the doctors are demanding it. Spend 90 seconds here, maximum.
-->

---

## Business Model

# Transaction Fee &nbsp;▸&nbsp; Platform &nbsp;▸&nbsp; Payer API

- **$4.80 per PA request** (replaces $14 manual cost — 66% savings to health system)
- **$18K/year** platform fee per department at 12-month upsell
- **$28 per decision** for payer-side API (2027 roadmap)

*Gross margin: 74% &nbsp;|&nbsp; CAC payback: 7 months*

<!-- Speaker notes:
YC loves simple business models with obvious expansion paths. Transaction fee is the wedge — low friction, immediate ROI for the customer. Platform fee is the retain-and-grow motion — we convert at 68% of customers at month 12. Payer API is the long-term value creation story: payers will pay more per decision than health systems, and our denial pattern dataset is the competitive moat that grows with every transaction. On unit economics: 74% gross margin is current, not projected. CAC payback of 7 months is fully-loaded including onboarding engineering time. If asked about pricing pressure: "We've tested lower. Demand does not increase below $3.50 because the ROI story is so clear — the question is never price, it is deployment bandwidth." That is a good problem to have and worth naming.
-->

---

## Team

# We Have Run This Problem From Both Sides

- **Sarah Chen, CEO** — VP Clinical Informatics at Sutter Health for 6 years; Stanford CS
- **James Okafor, CTO** — built prior auth API at Change Healthcare before its $14B acquisition
- **Dr. Priya Mehta, Clinical Lead** — practicing hospitalist + 12 published papers on PA reform

<!-- Speaker notes:
YC cares about founder-market fit more than almost any other metric at seed and Series A. Each bullet answers "why is this person uniquely able to solve this problem?" Sarah bought this product — she knows the buyer's psychology from the inside. James built the infrastructure layer that Helix integrates with — he has the technical credibility and the payer relationships. Priya is rare: a practicing clinician who codes. She ensures the product is clinically coherent, not just technically clever. Keep this slide under 60 seconds — do not recite CVs. One sentence per person, then move on. If pressed on gaps in Q&A: "VP Sales is our next hire — we have two finalists. We are specifically recruiting someone with EHR go-to-market experience from Veeva or Health Catalyst."
-->

---

## Progress

# 14 Months of Compounding — On Plan

| Milestone | Target | Actual |
|---|---|---|
| First health system live | Q2 2025 | Q1 2025 (early) |
| $1M ARR | Q4 2025 | Q3 2025 (early) |
| 10 systems live | Q1 2026 | Q1 2026 (on) |
| CMS compliance certification | Q2 2026 | In progress |

*Next milestone: 30 systems live by Q4 2026*

<!-- Speaker notes:
This slide is the founder integrity signal. Many founders only show accomplishments; showing a plan-versus-actual table — including "in progress" items — signals operational discipline and transparency. The fact that you hit two milestones early demonstrates execution velocity, not just vision. The CMS certification "in progress" is honest: don't claim it's done if it isn't. Investors will call your references and verify. The "next milestone" at the bottom anchors the conversation about what the Series A funding actually buys. If asked why CMS certification is taking longer: "The certification process was extended due to the new interoperability rule updates in January — we had to refactor the API surface. We expect Q3 2026." Specific, factual, no blame.
-->

---

## Vision

# Every Clinical Decision Supported by Complete Information

Prior auth is the first workflow. The same engine extends to:
- **Utilization management** — real-time appropriateness scoring
- **Benefits navigation** — patients understand coverage before the appointment
- **Clinical documentation** — reduce note burden, not just admin burden

*In 10 years: the AI layer between EHR data and every payer decision.*

<!-- Speaker notes:
Vision is where you give investors permission to dream about the Series B and beyond. Don't overpromise on the near term — keep the roadmap grounded. But the vision statement "the AI layer between EHR data and every payer decision" is worth saying slowly and letting it land. That is a platform, not a product. The three adjacencies are each independently large markets — utilization management is $8B, benefits navigation is underserved and growing. The point of this slide is not to promise all three in 24 months; it is to show that you are building toward a platform moat, not a single-workflow tool. YC investors think in 7–10-year arcs. Give them the arc. Then return to earth: "Today, we are executing on prior auth. That is the wedge that earns us the right to build the rest."
-->

---

## Ask

# $3M SAFE &nbsp;|&nbsp; $18M Cap &nbsp;|&nbsp; Closing May 2026

- **Use:** 12 months runway to $9M ARR and 30 health systems live
- **Lead investor:** seeking YC + one strategic co-investor (health system or payer)
- **Data room:** available immediately upon NDA

**Book a 30-minute call this week. Link: helix.health/investor**

<!-- Speaker notes:
The ask slide is where many founders get vague. Don't. Name the instrument (SAFE), the cap ($18M), and the close date (May 2026). Give the use of funds in one line — it signals financial discipline. The "lead investor + strategic co-investor" structure is deliberate: a health system or payer co-investor gives you distribution access and clinical validation that financial-only VCs cannot provide. The data room availability signals that you are prepared and serious. The CTA is specific: "Book a 30-minute call this week" with a URL. Not "let's stay in touch." Not "reach out when you're ready." A specific ask with a specific next action and a specific URL. If this is a YC application, replace the URL with "We will be on-site during YC interview week. We'd welcome a conversation." Follow up within 48 hours of the pitch with the data room link.
-->
