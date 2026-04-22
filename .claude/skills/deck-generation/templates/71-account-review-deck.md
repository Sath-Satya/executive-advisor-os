<!-- TEMPLATE: account-review-deck
     CATEGORY: Sales
     USE WHEN: presenting a strategic account plan to internal leadership
     SLIDE COUNT: 10
     PALETTE: Corporate
     RENDER: marp --pptx 71-account-review-deck.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', 'DM Sans', system-ui, sans-serif;
    background: #faf8f3;
    color: #1c1a18;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'Georgia', 'DM Serif Display', serif;
    color: #0e1b2e;
    letter-spacing: -0.4px;
    font-size: 2.1em;
    line-height: 1.15;
    margin-bottom: 0.3em;
  }
  h2 {
    color: #1a6bb5;
    font-size: 0.85em;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 { color: #0e1b2e; font-size: 1.05em; font-weight: 700; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; font-weight: 700; }
  em { color: #1a6bb5; font-style: normal; font-weight: 600; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "▸ "; color: #1a6bb5; }
  ul li { margin-bottom: 0.6em; font-size: 1em; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
  th {
    background: #eceae4;
    color: #556677;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.06em;
    font-size: 0.8em;
    text-transform: uppercase;
    border-bottom: 2px solid #d4d0c8;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #eceae4; }
  tr:last-child td { border-bottom: none; }
  blockquote {
    border-left: 4px solid #1a6bb5;
    padding: 12px 24px;
    margin: 1em 0;
    background: #eceae4;
    border-radius: 0 8px 8px 0;
    color: #0e1b2e;
    font-size: 1.05em;
  }
  .green { color: #2dd4a0; font-weight: 700; }
  .amber { color: #f0a050; font-weight: 700; }
  .red { color: #f06070; font-weight: 700; }
  section::after { color: #aaa8a0; font-size: 0.75em; }
---

## Strategic Account Review — Internal

# Meridian Health — Q2 2026 Account Plan

*Account Executive: James Whitfield &nbsp;|&nbsp; SponAI Consulting &nbsp;|&nbsp; April 2026*

**ARR:** $425,000 &nbsp;|&nbsp; **Tier:** Enterprise Strategic &nbsp;|&nbsp; **Health:** <span class="green">Green</span>

<!-- Speaker notes:
This is an internal account review — every data point on this slide should be verified against Salesforce before the meeting. The ARR figure should match the contract value visible to finance. The health status (Green / Amber / Red) should be your honest assessment based on engagement, support tickets, executive access, and renewal probability — not the number you wish it were. Meridian Health is one of SponAI's top five accounts by ARR, which is why it receives strategic-tier treatment. The purpose of this deck is to ensure that everyone in the room — sales leadership, CSM, solutions engineers, and finance — leaves with the same picture of the account. Before presenting, confirm that the CSM and AE are aligned on the health score and the whitespace numbers. Disagreements in the room are fine; contradictions to customers are not. Set the tone in your first 30 seconds: "I want to walk you through where we are, where we could go, and what we need from this room to get there."
-->

---

## Account Snapshot

# The Relationship at a Glance

| Metric | Value |
|---|---|
| Relationship start | March 2022 |
| Current ARR | $425,000 |
| Modules live | 3 of 5 (Claims AI, Auth Engine, Analytics) |
| Primary contact | Dr. Lisa Chandra, SVP Operations |
| Economic buyer | Brian Holt, CFO |
| Contract expiry | February 28, 2027 |
| NPS (last survey, Q1 2026) | 72 |

*Last executive engagement: March 14, 2026 — QBR with CFO and CMO*

<!-- Speaker notes:
The account snapshot is the foundation of the entire review. Every leader in the room should be able to read this slide in 20 seconds and understand who Meridian Health is as a customer. The "modules live" row is critical — 3 of 5 tells you that there is meaningful whitespace remaining. The primary contact and economic buyer distinction matters: Dr. Chandra is the champion; Brian Holt is the person who signs checks. Your strategy must work for both of them. The NPS of 72 is a strong signal — anything above 50 is considered excellent in enterprise software. Use it in renewal conversations. The last executive engagement date tells you how recently you had C-level access. If that date is more than 90 days ago, it is a risk regardless of other green signals. For this account, March 14 is recent. Contract expiry in February 2027 means you have an 8-month runway before the renewal window — enough time to expand before locking in the renewal price.
-->

---

## Stakeholder Map

# Who Owns the Relationship — and Who Could Kill It

| Name | Title | Sentiment | Role |
|---|---|---|---|
| Dr. Lisa Chandra | SVP Operations | <span class="green">Champion</span> | Primary sponsor, daily user |
| Brian Holt | CFO | <span class="green">Supportive</span> | Economic buyer |
| Priya Nair | VP IT | <span class="amber">Neutral</span> | Integration owner, risk flag |
| Marcus Webb | Director, PA Operations | <span class="green">Champion</span> | Power user, internal advocate |
| Janet Flores | VP Compliance | <span class="amber">Uninformed</span> | Needs engagement before renewal |

*Detractor risk: Priya Nair — recent support escalation re: FHIR latency (open ticket #4471)*

<!-- Speaker notes:
Stakeholder maps are the single most important slide in any strategic account review. Two champions (Chandra and Webb) and one supportive CFO is a strong position. The risks are Priya Nair and Janet Flores. Priya's neutrality is not passive — she had a support escalation last quarter. If that ticket is still open when renewal negotiations start, she has the standing to block or delay the contract. Action item from this meeting: assign a solutions engineer to close ticket #4471 within 10 business days. Janet Flores in Compliance is "uninformed" — she has not been briefed on how the system handles audit trails and data governance. Before renewal, the CSM should schedule a 30-minute briefing for her. Do not wait for her to ask questions during renewal; answer them proactively before she asks. Stakeholders who are uninformed at renewal time default to risk aversion. The goal of this slide is to assign owners and actions, not just to name stakeholders.
-->

---

## Current ARR Breakdown

# What They Are Paying For Today

| Module | ARR | Status | Renewal Risk |
|---|---|---|---|
| Claims AI Automation | $195,000 | <span class="green">Live — full adoption</span> | Low |
| Prior Auth Engine | $145,000 | <span class="green">Live — 87% utilization</span> | Low |
| Analytics Dashboard | $85,000 | <span class="amber">Live — 42% utilization</span> | Medium |
| **Total** | **$425,000** | | |

*Analytics underutilization is the primary renewal risk — addressed in expansion plan*

<!-- Speaker notes:
Two of three modules are performing well. The analytics dashboard at 42% utilization is the problem you need to solve before renewal. In renewal negotiations, the customer's procurement team will look at usage data. If they see a module they are barely using, they will ask to remove it or discount it. Your job between now and February 2027 is to either drive analytics adoption above 70% or reframe what "value" looks like for that module. The CSM should schedule a working session with Marcus Webb's team to identify why adoption is low. Likely causes: the dashboard is not showing the metrics they care about, the interface requires training, or the module was purchased for a use case that has since changed. Each cause has a different fix. Do not assume — ask. If adoption cannot be improved, have a contingency plan: can you replace the analytics module with a higher-value module they would use? Protect the $425K floor before reaching for whitespace expansion.
-->

---

## Whitespace Analysis

# Where the $850K Opportunity Lives

- **Revenue Integrity Suite** — not deployed; 4 hospitals in the IDN not yet on platform; *est. $210,000 ARR*
- **Member Engagement AI** — CEO publicly committed to digital-first member communication in Q1 earnings call; *est. $175,000 ARR*
- **Population Health Module** — 2026 strategic initiative; RFP expected Q3; *est. $95,000 ARR*

*Total identified whitespace: $480,000 ARR &nbsp;|&nbsp; Total account potential: $905,000 ARR*

<!-- Speaker notes:
Whitespace analysis is where this meeting earns its time. The $480,000 in whitespace is not a wish list — each line should be backed by a trigger. The Revenue Integrity Suite trigger: 4 hospitals in the IDN are not on platform. That is an expansion into existing logos, the easiest motion in enterprise sales. The Member Engagement AI trigger: the CEO said it in an earnings call. That is a publicly stated strategic priority — your proposal should quote it back to them. The Population Health Module trigger: an RFP is expected. That means there is a budget and a process already forming. Your job is to get on the shortlist before the RFP is issued, not after. The $905,000 total account potential is a target ARR, not a guarantee. Set expectations with leadership: "Realistically, I expect to close $210K-$310K in new ARR at renewal. The remaining whitespace is 12-24 months out." Overclaiming whitespace destroys trust in internal forecasts.
-->

---

## Strategic Initiatives

# Aligning to Meridian's 2026 Priorities

- **"Digital Front Door" Program** — Meridian's board-level initiative to reduce member friction; our Member Engagement AI is a direct fit
- **IDN consolidation** — 2 hospital acquisitions planned in 2026; we must be the platform they standardize on, not the platform they swap out
- **CMS compliance deadline** — interoperability rule takes effect October 2026; our FHIR R4 native layer is already compliant; competitors are not

*Executive sponsor for Digital Front Door: Dr. Lisa Chandra — our primary champion*

<!-- Speaker notes:
This slide elevates the account review from an internal sales exercise to a strategic alignment document. Each bullet connects a Meridian priority to a SponAI capability. "Digital Front Door" is not a SponAI term — it is their term. Using their language signals that your team has done its homework. The IDN consolidation item is both an opportunity and a risk: if Meridian acquires two hospitals that run a competing platform, and you are not positioned as the standard, you could lose share even in a healthy account. Schedule a conversation with Dr. Chandra about the acquisition timeline. "We want to make sure the integration plan includes our platform from day one, not as an afterthought." The CMS interoperability deadline is the clearest competitive lever: if a competitor is not FHIR R4 compliant by October, they face regulatory risk. You are not — and you should say so directly, with documentation.
-->

---

## Risk Register

# What Could Derail This Account

| Risk | Severity | Probability | Mitigation |
|---|---|---|---|
| Analytics underutilization at renewal | <span class="amber">Medium</span> | High | Adoption sprint — 90 days |
| Priya Nair escalation unresolved | <span class="amber">Medium</span> | Medium | Close ticket #4471 by May 9 |
| Competitor evaluation during IDN expansion | <span class="red">High</span> | Medium | Executive briefing on FHIR compliance gap |
| Budget freeze — healthcare sector pressure | <span class="amber">Medium</span> | Low | CFO alignment letter from our CEO |

*No critical risks today — maintain green status with proactive mitigation*

<!-- Speaker notes:
A risk register without owners and due dates is theater. Every risk on this slide needs an owner assigned before this meeting ends. The analytics underutilization risk has the highest probability of impacting the renewal — it is a high-frequency concern. The competitor evaluation risk has the highest severity if it materializes — losing the IDN expansion to a competitor could mean being displaced across all four unconverted hospitals eventually. The budget freeze risk is currently low probability but worth watching. Healthcare systems are under reimbursement pressure from CMS, and a sudden budget freeze could pause expansion conversations without warning. The mitigating signal is Brian Holt's active engagement — a CFO who comes to QBRs is not a CFO who is about to freeze discretionary IT spend. Revisit this risk assessment at each monthly account review between now and renewal.
-->

---

## Revenue Plan

# FY2026 Expansion Target: +$275,000 ARR

| Initiative | Target ARR | Close Quarter | Confidence |
|---|---|---|---|
| Revenue Integrity Suite — 2 hospitals | $105,000 | Q3 2026 | <span class="green">High (75%)</span> |
| Member Engagement AI | $120,000 | Q4 2026 | <span class="amber">Medium (50%)</span> |
| Analytics upsell / right-size | $50,000 | Q2 2026 | <span class="amber">Medium (55%)</span> |
| **Total expansion target** | **$275,000** | | |

*Renewal at current ARR: February 2027 &nbsp;|&nbsp; Target ARR at renewal: $700,000*

<!-- Speaker notes:
The revenue plan is where internal credibility is built or lost. Each line should have a confidence percentage that reflects pipeline reality, not aspiration. High confidence (above 65%) means the champion has confirmed budget, the economic buyer has been briefed, and there is an active conversation. Medium confidence (40–60%) means there is interest but no budget confirmation. Low confidence (below 40%) should not be in the Q-level forecast — move it to pipeline or next year. The $700,000 target ARR at renewal is a 65% increase over current ARR. That is aggressive but achievable given the whitespace analysis. If leadership pushes back, the defensible number is $625,000 — that assumes the Revenue Integrity Suite expansion and the renewal of all three current modules. The $120,000 Member Engagement AI is the variable. Focus Q2 executive conversations on building the business case for that module with Dr. Chandra as internal sponsor.
-->

---

## Blockers and Asks

# What This Room Needs to Do

- **Product:** Analytics dashboard — two missing report types requested in Q1. Required for adoption sprint. *Ask: commit to Q3 roadmap*
- **Leadership:** Executive-to-executive letter from our CEO to Meridian CFO Brian Holt ahead of IDN expansion conversations. *Ask: CEO signs and sends by April 30*
- **Legal:** MSA amendment for multi-hospital expansion pricing — standard terms need hospital count clause. *Ask: draft ready by May 15*

*All three blockers are in-team dependencies — no customer action required*

<!-- Speaker notes:
This is the slide where the AE asks the room for something. The three asks are calibrated to the audience: a product commitment, a leadership action, and a legal task. None of them require the customer to do anything — they are internal unblocks. Be direct when presenting this slide: "I cannot close the Revenue Integrity Suite expansion without the MSA amendment because Meridian's legal team will not sign an addendum that does not have explicit multi-hospital pricing language." That specificity earns credibility. For the CEO letter: this is a relationship signal, not a legal document. A short note from CEO to CFO saying "we are committed to growing with Meridian" costs nothing and has outsized impact in a renewal conversation where the CFO is comparing us to a challenger. If any of these asks are denied, document the decision and its impact on the revenue plan. A sales leader who asks for something and gets a no should immediately quantify the consequence: "Without the analytics roadmap commitment, I lower Q3 Revenue Integrity confidence from 75% to 45%."
-->

---

## Next Quarter Plan

# 90-Day Priorities — Q2 2026

- **April:** Close ticket #4471 &nbsp;|&nbsp; Compliance briefing for Janet Flores &nbsp;|&nbsp; CEO letter to Brian Holt
- **May:** Analytics adoption sprint with Marcus Webb's team &nbsp;|&nbsp; Revenue Integrity Suite scoping call
- **June:** Executive QBR — present expansion business case to Dr. Chandra and CFO &nbsp;|&nbsp; MSA amendment signed

*Target outcome by June 30: $105,000 Revenue Integrity Suite — verbal commitment from Meridian*

<!-- Speaker notes:
The 90-day plan converts this review from a discussion into a project. Each month has a clear focal point — do not try to do everything in April. Sequencing matters: the Compliance briefing for Janet Flores must happen before the renewal conversation starts, not during it. The CEO letter needs to go out before the Revenue Integrity Suite scoping call so the CFO's temperature has been warmed by an executive peer. The June QBR is the most important event in the quarter. It is the moment where all the groundwork — analytics adoption improvement, compliance briefing, executive relationship — comes together in a single room with decision-makers. The June 30 target is a verbal commitment, not a signed contract. Set that expectation explicitly with leadership: "Verbal by June 30, paper by July 31, booking in Q3." The verbal-to-paper conversion rate on well-prepared strategic accounts at this ARR level is above 80%. Do the groundwork and the close will follow.
-->
