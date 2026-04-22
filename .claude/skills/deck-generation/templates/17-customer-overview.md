<!-- TEMPLATE: customer-overview
     CATEGORY: Sales / Customer-Facing
     USE WHEN: introductory meeting with a new customer, conference booth follow-up, or leave-behind
     SLIDE COUNT: 7
     PALETTE: Clean light
     RENDER: marp --pptx 17-customer-overview.md -->
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
    font-size: 0.82em;
    text-transform: uppercase;
    border-bottom: 2px solid #e0e6ed;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #f0f2f5; }
  tr:last-child td { border-bottom: none; }
  blockquote {
    border-left: 4px solid #3b9eff;
    padding: 12px 24px;
    margin: 1em 0;
    background: #f4f9ff;
    border-radius: 0 8px 8px 0;
    font-style: italic;
    color: #1c1a18;
    font-size: 1.02em;
  }
  section::after { color: #c0cad4; font-size: 0.75em; }
---

## Who We Are

# Helix — We Make Prior Authorization Disappear

**Founded:** 2024 &nbsp;|&nbsp; **HQ:** San Francisco, CA &nbsp;|&nbsp; **Team:** 38 employees

Helix is an AI platform that automates the prior-authorization workflow — from first submission through appeals — inside the EHR systems your physicians already use.

*11 health systems. 340,000 PA requests automated. Zero patient data moved.*

<!-- Speaker notes:
This deck is designed for an introductory meeting — the audience may not know Helix at all. The one-liner "we make prior authorization disappear" is deliberately bold. It creates a mental model before any explanation is needed. The three stats in the footer — 11 systems, 340,000 requests, zero data moved — address scale, proof, and the privacy concern that health system buyers will raise within 60 seconds. Keep this slide under 60 seconds. You are setting context, not making the case. If you are at a conference and the person across from you found you at a booth, they have 5 minutes before their next meeting. Every slide in this deck is designed to be scannable in under 90 seconds. The leave-behind version of this deck should be emailable as a PDF — make sure no proprietary information (investor pipeline, unreleased products) is included.
-->

---

## What We Do

# One Platform — Three Workflows

- **Prior authorization:** AI submits complete, compliant PA requests from the EHR in 22 seconds
- **Denial management:** automatic appeal generation with supporting evidence — 73% win rate
- **Analytics:** real-time dashboard showing approval rates, denial patterns, and staff workload

*Works inside Epic, Cerner, and Athena — no new login, no new tab, no training required*

<!-- Speaker notes:
The "what we do" slide should be clear enough that a non-technical executive can explain it to a colleague. Three workflows, each expressed as a verb phrase describing an outcome, not a feature. The "no new login, no new tab, no training required" line is the adoption unlock — it directly addresses the "our physicians won't use a new tool" objection before it is raised. If the person across from you is clinical (CMO, chief nursing officer), emphasize the 22 seconds and the physician experience. If they are operational (VP Ops, CFO), emphasize the denial rate and the analytics dashboard. If they are IT (CIO, CISO), pivot to the FHIR architecture and the SOC 2 certification — and stay on the "no new infrastructure" message. Tailor the emphasis based on what you know about the audience before you advance to this slide.
-->

---

## How We Help

# From 14 Minutes to 22 Seconds — Measurable Impact

| Metric | Before Helix | After Helix |
|---|---|---|
| Time per PA request | 14 minutes | **22 seconds** |
| First-pass denial rate | 17% industry avg | **6%** with Helix |
| Appeals win rate | 42% manual | **73%** with Helix |
| Staff time on PA (weekly) | 120 hours/dept | **18 hours/dept** |
| Days to approval | 11 days | **3 days** |

*Data from 11 live deployments, March 2026*

<!-- Speaker notes:
The before/after table is the core value proposition in one slide. In an introductory meeting, this table often generates the most questions — which is exactly what you want. The number that lands hardest varies by audience: physicians care about "14 minutes to 22 seconds," CFOs care about "120 hours to 18 hours per department," and quality officers care about "17% to 6% denial rate." Do not try to cover all of them — ask the room: "Which of these metrics is most important to your organization right now?" The answer tells you which slides to emphasize in the rest of the deck and which use case to feature in the next meeting. The source footnote — "11 live deployments, March 2026" — is important. When someone sees dramatic numbers, their first reaction is skepticism. Naming a date and a specific sample makes it verifiable.
-->

---

## Who We Help

# Purpose-Built for Health Systems — 200 to 2,000 Beds

- **Academic medical centers:** complex procedures, high PA volume, research documentation needs
- **Community hospitals:** resource-constrained — every FTE redeployment matters
- **Integrated delivery networks:** multi-site deployment with consolidated analytics

*We are not a fit for: solo practices, payer-side utilization management, or non-US systems.*

<!-- Speaker notes:
The "who we help" slide is as much about disqualifying poor fits as it is about qualifying good ones. The final bullet — "we are not a fit for" — is unusual in an overview deck, but it builds trust. It signals that you are not going to waste their time trying to shove a misfit deal through. If the person you are talking to is a solo practice manager, you can close gracefully: "Based on what you've told me, Helix isn't the right fit today — but I'd like to reconnect when you're at a network level. Here's the overview deck for your reference." That conversation earns more goodwill than trying to sell to the wrong buyer. For IDN buyers, emphasize the multi-site analytics: "If you have 6 hospitals in your network, you can see denial patterns across all six in one dashboard — and identify which sites have the most improvement opportunity."
-->

---

## Case Study — Mercy Health System

# From 19% Denials to 4% in 90 Days

**Mercy Health System** (1,200 beds, Epic EHR, Chicago, IL)

- **Challenge:** 3 FTE dedicated full-time to PA management; 19% denial rate; physician complaints
- **Deployment:** Helix live in cardiology department in 5 weeks
- **Results at 90 days:**
  - Denial rate: 19% &nbsp;▸&nbsp; **4%** &nbsp;|&nbsp; Time-to-approval: 12 days &nbsp;▸&nbsp; **2.8 days**
  - Staff redeployed: **2 of 3 FTE** to patient care coordination
  - Physician NPS: **+68** (from baseline of 18)

<!-- Speaker notes:
Case studies are the most persuasive element of any customer overview deck. Lead with the customer's challenge, not Helix's features. "3 FTE dedicated full-time to PA" is a peer recognizing their own situation — health system buyers have almost identical problems, and seeing a comparable organization resolve it creates credibility. The deployment time — 5 weeks — is a key objection handler: "We hear 'we're too busy to implement new software.' Mercy deployed in 5 weeks, and the first-week benefit already offset the implementation time." The physician NPS number deserves special attention: "The most important thing about this result isn't the efficiency gain. It's that physicians went from skeptical to advocates. An NPS of 68 means your physicians are telling colleagues to demand this." If you have a reference willing to take calls, offer it: "I can arrange a 15-minute call with Mercy's VP of Operations if that would be useful."
-->

---

## Case Study — St. Catherine's Medical

# Cardiology Denials Dropped 76% — One Department, 60 Days

**St. Catherine's Medical Center** (800 beds, Cerner EHR, Dallas, TX)

- **Challenge:** Cardiology prior auth was a 22-day average cycle; 2 RAs working full-time
- **Deployment:** 7-week Cerner integration; live in cardiology November 2025
- **Results at 60 days:**
  - Cardiology PA cycle time: 22 days &nbsp;▸&nbsp; **4.1 days**
  - Denial rate: 21% &nbsp;▸&nbsp; **5%**
  - RA time freed: **1.6 FTE** redeployed to care coordination
  - Zero implementation issues; go-live ahead of schedule

<!-- Speaker notes:
The second case study should differ from the first in size, EHR, and use-case emphasis. Mercy was an Epic shop; St. Catherine's is Cerner — this addresses the objection "does it work with our EHR?" Cardiology is a consistently high-PA-volume specialty; using it as a reference case means the numbers are dramatic because cardiology PA is complex and high-stakes. The "go-live ahead of schedule" line is important for risk-conscious buyers: it signals that Helix's implementation team does not create project management nightmares. The 1.6 FTE number is precise, not rounded — precision builds credibility. When you leave this deck with a prospect, tell them the reference is available: "I'll introduce you to the VP of Cardiology at St. Catherine's if you want to hear it directly from them." A warm reference introduction from you is worth more than a cold name on a slide.
-->

---

## Next Steps

# Three Ways to Start a Conversation

1. **30-minute discovery call** — we learn your PA volume and workflow; you see the ROI model
2. **Live product demo** — 20 minutes, sandbox environment, your team's questions answered live
3. **Site visit** — join us at a live Helix deployment at a peer institution

*No commitment required. We will have a custom ROI estimate ready before the first call.*

**Request a meeting: helix.health/meet &nbsp;|&nbsp; sarah.chen@helix.health &nbsp;|&nbsp; (415) 555-0192**

<!-- Speaker notes:
Three options with decreasing commitment level — discovery call is the lowest bar. Always give prospects a choice rather than one next step; it puts them in control and increases the conversion rate from "thinking about it" to "scheduled." The custom ROI estimate offer is a strong incentive: "Before you even spend 30 minutes with us, we'll prepare a model based on your organization's size and PA volume — just tell me the EHR you use and your bed count." That commitment of effort before the call signals confidence and respect. The site visit option is the highest-value offer: seeing Helix in a live health system with a peer organization is more persuasive than any demo. If you have a willing customer who is a geographic peer of this prospect, offer the introduction: "Mercy Health in Chicago is open to peer visits on Wednesdays." Leave-behind note: if emailing this deck, add a calendar link directly in the email body rather than making them navigate to a website.
-->
