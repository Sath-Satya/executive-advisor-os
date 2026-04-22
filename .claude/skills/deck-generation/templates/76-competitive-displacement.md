<!-- TEMPLATE: competitive-displacement
     CATEGORY: Sales
     USE WHEN: pitching to displace a competitor in an existing customer account
     SLIDE COUNT: 10
     PALETTE: Dark premium
     RENDER: marp --pptx 76-competitive-displacement.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', 'DM Sans', system-ui, sans-serif;
    background: #0a0e14;
    color: #d0d8e4;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'Segoe UI', system-ui, sans-serif;
    color: #ffffff;
    letter-spacing: -0.4px;
    font-size: 2.1em;
    line-height: 1.15;
    margin-bottom: 0.3em;
    font-weight: 700;
  }
  h2 {
    color: #3b9eff;
    font-size: 0.85em;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 { color: #ffffff; font-size: 1.05em; font-weight: 700; margin-bottom: 0.4em; }
  strong { color: #ffffff; font-weight: 700; }
  em { color: #3b9eff; font-style: normal; font-weight: 600; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "▸ "; color: #3b9eff; }
  ul li { margin-bottom: 0.6em; font-size: 1em; line-height: 1.55; color: #d0d8e4; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
  th {
    background: #111820;
    color: #8899ac;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.06em;
    font-size: 0.8em;
    text-transform: uppercase;
    border-bottom: 2px solid #1e2a38;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #111820; color: #d0d8e4; }
  tr:last-child td { border-bottom: none; }
  blockquote {
    border-left: 4px solid #3b9eff;
    padding: 12px 24px;
    margin: 1em 0;
    background: #111820;
    border-radius: 0 8px 8px 0;
    color: #d0d8e4;
    font-size: 1.05em;
  }
  .green { color: #2dd4a0; font-weight: 700; }
  .amber { color: #f0a050; font-weight: 700; }
  .red { color: #f06070; font-weight: 700; }
  section::after { color: #556677; font-size: 0.75em; }
---

## Displacement Proposal — Meridian Health

# There Is a Better Way to Run Claims Operations

*SponAI Consulting &nbsp;|&nbsp; Confidential — Prepared for Meridian Health Executive Leadership*

*April 2026*

<!-- Speaker notes:
The competitive displacement deck opens with confidence, not aggression. You are not attacking the incumbent — you are presenting a better future state. The "confidential" label is appropriate because this deck contains competitive positioning that you would not want circulated outside the decision-maker group. Before this meeting, do your homework on the incumbent: how long have they been deployed at Meridian, what contracts are in place, when is the renewal window, and what are the switching costs. The displacement motion is fundamentally different from a new logo motion. The customer already has a solution — they are not convinced they have a problem. Your job is to show them the gap between what they have and what is possible. Start the meeting by asking: "What made you willing to have this conversation?" The answer tells you everything about the internal dynamics that got you in the room. A champion who fought to get you a meeting is more valuable than a meeting that was set up by procurement.
-->

---

## The Current State

# What Operations Look Like Today at Meridian

- **Claims cycle:** 11-day average — 2nd quartile performance nationally; 8% of claims aged beyond 30 days
- **Denial rate:** 18% — $3.1M in annual rework costs for preventable denials
- **Staff experience:** 3 FTE spending 65% of their time on data reconciliation between disconnected systems
- *The platform you are on today was the right choice in 2019. The question is whether it is still the right choice in 2026.*

<!-- Speaker notes:
The current state slide establishes the baseline without attacking the incumbent by name. "The right choice in 2019" is a deliberate framing: it acknowledges that the customer made a reasonable decision when they deployed the current system, while implying that the technology landscape has changed. That framing is important — calling the incumbent a bad choice implies the customer made a bad decision, which creates defensiveness. Instead, you are saying: the world changed, and the tools that were state-of-the-art five years ago are no longer the best available. This is a factual and empathetic position. The "2nd quartile" benchmark should be sourced: KLAS, MGMA, or HFMA benchmarks provide nationally comparable performance data for revenue cycle operations. Verify the benchmark before using it. If your data source is wrong, the customer's finance team will catch it and your credibility drops.
-->

---

## Pain with the Incumbent

# The Friction That Has Become Background Noise

- **Integration overhead:** 4 manual data transfers daily between the platform and Epic; each takes 45–60 minutes of staff time
- **Denial pattern detection:** current platform flags denials after submission — not before. Your team is fighting fires, not preventing them
- **Roadmap stagnation:** the last major feature release was 14 months ago — the platform is in maintenance mode

> "We spend as much time managing the tool as we do managing the claims." — Director, PA Operations (Marcus Webb, internal voice of customer)

<!-- Speaker notes:
The pain slide is where you crystallize what the customer's internal champions have been telling you during discovery. The three bullets should come directly from your discovery conversations — not from your competitive intelligence on the incumbent. If Marcus Webb said "we spend as much time managing the tool as managing claims," use his exact words. Internal voices of customer are the most credible sources in a displacement conversation because they cannot be dismissed as vendor positioning. The denial flagging point — "after submission, not before" — is a technical differentiator that translates to real economics. A system that flags denial risk before submission allows staff to fix the problem before it becomes a denial. A system that flags it after creates a rework cycle. The cost of rework is in your current state slide. The roadmap stagnation point is strategic: a platform in maintenance mode will not close the gap between current performance and best-in-class. The customer is paying for a platform that is standing still while the market moves forward.
-->

---

## Our Differentiators

# What SponAI Brings That the Current Platform Cannot

| Capability | Current Platform | SponAI |
|---|---|---|
| Denial prediction | Post-submission flagging | Pre-submission completeness check |
| Epic integration | Daily batch transfer | Native FHIR R4, real-time |
| AI model updates | Annual release cycle | Continuous learning, monthly retraining |
| Reporting | Static canned reports | Custom dashboard, self-service analytics |
| Customer success | Shared support queue | Dedicated CSM + quarterly executive reviews |

<!-- Speaker notes:
The comparison table is the most scrutinized slide in a displacement deck. Every claim should be verifiable. "Native FHIR R4, real-time" should be supported by your Epic certification documentation. "Continuous learning, monthly retraining" should be backed by your product team's release cadence. If any claim can be challenged and you cannot back it up, remove it. A comparison table with five accurate points is stronger than one with eight points where two are questionable. The temptation is to make the table look as lopsided as possible. Resist this. Customers know that vendors never present balanced comparisons. A table where you are clearly better on 4 of 5 dimensions with an honest acknowledgment of where the incumbent is comparable or better earns more credibility than a table where you win every category. Ask your champion to review this table before the meeting: "Are there any of these comparisons where you would push back or where the current platform is better?" That conversation strengthens the deck and gives your champion talking points for internal conversations.
-->

---

## Proof Points

# Customers Who Made This Switch

| Organization | Previous Platform | Outcome After Switch | Timeline |
|---|---|---|---|
| St. Catherine's Medical | Veradigm | Denial rate 21% → 5% in 90 days | 8-week migration |
| Valley Regional Health | nThrive | Claims cycle 16 days → 4.2 days; $1.4M saved Y1 | 10-week migration |
| Cascade Physicians Group | Experian Health | 3 FTE redeployed; NPS 78 from clinical staff | 6-week migration |

*Migration references available — all three customers displaced the same class of platform*

<!-- Speaker notes:
The proof point slide specifically names displacement scenarios — customers who made the switch from a comparable platform. This is more powerful than generic customer success stories because it answers the unstated question: "Has anyone else done what you are asking us to do, and what happened?" Each reference customer has a different highlight: denial rate, cycle time, and staff satisfaction. This three-dimensional proof covers the buyer personas in the room: the COO cares about cycle time, the CFO cares about savings, and the clinical operations leader cares about staff satisfaction. The "8-week migration" timeline is the critical signal — it shows that switching is not a 12-month project. The customer's fear of switching cost is often larger than the actual switching cost. When you put 6–10 week migration timelines in front of them, that fear begins to dissolve. Offer a reference call with whoever is most similar to Meridian: "The Valley Regional scenario is the closest match to your situation — I can arrange a peer call with their VP Revenue Cycle within the week."
-->

---

## The Switching Path

# How Migration Actually Works

- **Week 1–2:** Parallel run — SponAI ingests Meridian's claim data alongside the current platform; zero workflow change
- **Week 3–4:** Shadow validation — our AI processes claims independently; staff review discrepancies without any impact on live operations
- **Week 5–6:** Cutover — department by department; first department switches; others remain on current platform
- *Full transition complete in 8 weeks. Current platform contract honored until its expiration date.*

<!-- Speaker notes:
The switching path is the slide that converts fear into a plan. The customer's procurement team knows how to evaluate software. Their risk manager knows how to evaluate contract transitions. What they do not have a model for is the operational risk of switching a core administrative platform mid-year. This slide answers that risk question directly. The parallel run in weeks 1–2 means you are processing their real claims before any workflow changes. That is the proof of concept embedded in the migration plan. If the shadow validation in weeks 3–4 reveals any issues, you catch them before any cutover. The department-by-department cutover means that a bad outcome in the first department does not take down the entire organization. You roll back to the current platform and fix the issue before continuing. "Current platform contract honored until its expiration date" is an important legal and financial statement. You are not asking Meridian to break their contract with the incumbent — you are proposing a timeline that respects their existing contractual obligations.
-->

---

## Cost to Switch

# The Real Economics of Transition

| Cost Category | Estimate | Notes |
|---|---|---|
| Migration project (one-time) | Included in Year 1 | No separate migration fee |
| Staff retraining | 4 hours/person, 15 staff | $4,500 estimated at internal cost |
| Parallel run period | 2 weeks | Staff time; estimated $8,000 |
| Early termination penalty (incumbent) | $0–$45,000 | Depends on contract terms |
| **Total switching cost** | **$12,500–$57,500** | Variable based on incumbent contract |

*Switching cost recovered in Year 1 net benefit within 45–90 days of go-live*

<!-- Speaker notes:
Transparency about switching costs is a displacement differentiator. Most displacement conversations avoid this topic — the seller does not want to raise the switching cost; the buyer does not know how to quantify it. By putting numbers on the table first, you control the framing. $12,500–$57,500 is a wide range, but both ends are defined. The $45,000 variable is the incumbent's early termination penalty, which is a customer contract issue — not your cost. Prepare a decision tree: "If your current contract expires within 6 months, your switching cost is under $15,000. If you have 6–18 months remaining, it depends on the termination clause. We can help you model this if you share the relevant terms with our team." That offer is valuable — you are doing financial due diligence for them. The payback statement — switching cost recovered in 45–90 days — requires the Year 1 benefit analysis to be complete and defensible. Never use this line without the math to back it up.
-->

---

## ROI Analysis

# What the Switch Delivers Financially

| Year | Investment (SponAI) | Benefit | Net |
|---|---|---|---|
| Year 1 (incl. switch) | $392,500 | $3,100,000 | $2,707,500 |
| Year 2 | $135,000 | $3,100,000 | $2,965,000 |
| Year 3 | $135,000 | $3,200,000 | $3,065,000 |
| **3-Year Total** | **$662,500** | **$9,400,000** | **$8,737,500** |

*Year 1 includes $57,500 maximum switching cost scenario. Current platform spend not included in investment column — that is replaced by SponAI.*

<!-- Speaker notes:
The 3-year ROI table is the closing argument for the economic buyer. Year 1 includes the switching cost — even in the worst-case scenario of a $45,000 termination penalty plus $12,500 in transition costs. The net benefit of $2.7M in Year 1 still represents an 8x return on investment. Year 3 shows a slight benefit increase — $3.2M versus $3.1M — which reflects the compounding value of the AI model's continuous learning improving denial prediction accuracy over time. Present this table carefully: do not rush through it. Let the CFO process the numbers. If they ask for the methodology: "The $3.1M annual benefit is built bottom-up from three components — staff time savings, denial rate improvement, and cycle time acceleration. I have the breakdown available. Which component would you like to validate first?" Giving them a choice signals confidence in all three components and lets you tailor the conversation to what matters most to them.
-->

---

## Risk Mitigation

# Protecting Meridian Through the Transition

- **Performance guarantee:** Denial rate below 12% by Day 90 — or pro-rata credit applied automatically
- **Data continuity:** Full claims history migrated and accessible from Day 1 in the new system
- **Rollback clause:** If any department has a critical issue during cutover, 24-hour rollback to current platform is contractually guaranteed
- *SponAI has never triggered a rollback clause. We include it because you deserve the protection.*

<!-- Speaker notes:
The risk mitigation slide addresses the question the customer has not asked yet but is thinking about: "What if this goes wrong?" Every enterprise customer has a horror story about a failed migration. Your job is to pre-empt that fear before it surfaces. The rollback clause is a strong risk reversal — you are putting in writing that if the cutover causes critical issues, you restore the previous state within 24 hours. "SponAI has never triggered a rollback clause" is the sentence that makes the clause more credible, not less. You are not offering the protection because you expect to need it — you are offering it because your customer deserves it. The data continuity guarantee is critical for healthcare organizations: claims history is a regulatory and financial asset. Any migration that puts historical data at risk is a non-starter. The guarantee should be backed by a specific data migration protocol: "We migrate 5 years of claims history and provide a validation report showing record-for-record accuracy before cutover."
-->

---

## Timeline

# Displacement and Go-Live Plan

| Week | Milestone |
|---|---|
| 1–2 | Contract signed &nbsp;|&nbsp; parallel run begins &nbsp;|&nbsp; historical data migration starts |
| 3–4 | Shadow mode validation &nbsp;|&nbsp; staff training sessions scheduled |
| 5 | Department 1 cutover (PA Operations) |
| 6–7 | Departments 2–3 cutover &nbsp;|&nbsp; analytics dashboard live |
| 8 | Full production — all departments on SponAI |
| 12 | 90-day review: actual vs. projected outcome |

*Go-live target: July 14, 2026 &nbsp;|&nbsp; Contract signing required by May 31, 2026*

<!-- Speaker notes:
The timeline slide converts the displacement conversation into a project plan. The 8-week migration has a go-live date of July 14, which assumes a May 31 contract signing. If the signing slips, the go-live date slips proportionally — be explicit about this dependency. The department-by-department cutover order is not arbitrary: PA Operations (Department 1) is Marcus Webb's team — your internal champion. Starting with his department ensures you have an advocate in the first production environment. If Department 1 goes well, the momentum for Departments 2 and 3 is much stronger. The 90-day review at Week 12 is the accountability checkpoint for the performance guarantee. Schedule it now, before go-live, so the customer knows you are planning for it. An AE who schedules the performance review before the ink is dry on the contract signals confidence in the outcome.
-->

---

## The Ask

# One Decision — This Month

**What we are asking for:**
- A 30-minute technical call with Priya Nair (VP IT) to confirm FHIR integration requirements
- A contract review meeting with legal by May 15
- Contract signed by May 31 — enabling July 14 go-live

*Every week of delay is approximately $59,600 in recoverable value — the math is on your side to move quickly.*

*James Whitfield &nbsp;|&nbsp; james.whitfield@sponaitech.com &nbsp;|&nbsp; (415) 555-0147*

<!-- Speaker notes:
The displacement close is more specific than a new logo close because the customer already knows what a vendor relationship looks like. They are not afraid of the unknown — they are afraid of the known risk of switching. Your close should address execution risk directly: the technical call with Priya Nair is a low-stakes first commitment that moves the project forward. The "$59,600 per week of delay" calculation should be traceable: $3.1M annual benefit divided by 52 weeks = $59,600. It is a factual number, not a manufactured urgency device. Do not oversell the urgency — state the math and let the customer decide. After presenting the final slide, silence is your ally. The first person to speak after the close is negotiating. If Dr. Chandra or Brian Holt asks a question, answer it directly and return to the ask. If they are silent, wait. Enterprise sales professionals who are comfortable with silence close at higher rates than those who fill the pause with more talking.
-->
