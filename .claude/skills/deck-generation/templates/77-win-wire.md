<!-- TEMPLATE: win-wire
     CATEGORY: Sales
     USE WHEN: internal win announcement after closing a significant deal
     SLIDE COUNT: 7
     PALETTE: Warm light
     RENDER: marp --pptx 77-win-wire.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', 'DM Sans', system-ui, sans-serif;
    background: #faf7f2;
    color: #1c1a18;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'Georgia', 'DM Serif Display', serif;
    color: #0e1b2e;
    letter-spacing: -0.4px;
    font-size: 2.2em;
    line-height: 1.15;
    margin-bottom: 0.3em;
  }
  h2 {
    color: #f0a050;
    font-size: 0.85em;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 { color: #0e1b2e; font-size: 1.05em; font-weight: 700; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; font-weight: 700; }
  em { color: #f0a050; font-style: normal; font-weight: 600; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "▸ "; color: #f0a050; }
  ul li { margin-bottom: 0.6em; font-size: 1em; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
  th {
    background: #f2ede4;
    color: #556677;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.06em;
    font-size: 0.8em;
    text-transform: uppercase;
    border-bottom: 2px solid #e0d9ce;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #f2ede4; }
  tr:last-child td { border-bottom: none; }
  blockquote {
    border-left: 4px solid #f0a050;
    padding: 12px 24px;
    margin: 1em 0;
    background: #f2ede4;
    border-radius: 0 8px 8px 0;
    color: #0e1b2e;
    font-size: 1.05em;
  }
  .green { color: #2dd4a0; font-weight: 700; }
  section::after { color: #b0a898; font-size: 0.75em; }
---

## Win Wire — Confidential Internal

# We Won Meridian Health — $335,000 ARR

*SponAI Consulting &nbsp;|&nbsp; Closed: April 28, 2026*

*Deal Owner: James Whitfield &nbsp;|&nbsp; Announced to: Sales, Product, Leadership*

<!-- Speaker notes:
The win wire is an internal celebration and knowledge transfer document. The tone should be warm and specific — this is the sales equivalent of a post-mortem, but for a win. The goal is not just to celebrate but to extract learnings that can be replicated. "Win wires" from companies like Gong, Salesforce, and HubSpot are shared weekly and are one of the primary mechanisms by which sales teams improve their craft. Keep this meeting to 20–30 minutes. The AE presents; the team asks questions; lessons are captured. Before distributing this deck, confirm that no customer-confidential information is included that should not be shared internally. Deal economics (ARR, contract value) are generally safe for internal distribution. Competitor names and specific customer pain data should be treated with discretion. The warmth in this opening acknowledges the team — not just the AE. Enterprise deals are won by teams, not individuals.
-->

---

## Deal Summary

# The Numbers That Matter

| Field | Value |
|---|---|
| Customer | Meridian Health (4-hospital IDN, regional) |
| Deal type | New logo — displacement of Veradigm |
| ACV (Annual Contract Value) | $335,000 Year 1 / $135,000 ongoing |
| Contract length | 2 years (auto-renew) |
| Close date | April 28, 2026 |
| Sales cycle | 87 days (first meeting: February 1, 2026) |
| Forecast stage when called | Verbal — called 14 days before close |

*Identified whitespace at contract signature: $480,000 additional ARR opportunity*

<!-- Speaker notes:
The deal summary table is the factual record of what happened. Each field should be filled from Salesforce before the meeting — not from memory. The sales cycle length (87 days) is a reference point for similar opportunities: how long should the team expect a healthcare IDN displacement to take? 87 days is the data point you now have. The "forecast stage when called" field is an honesty check: did the AE call the close accurately? If a deal was in "Discovery" when it was called as Verbal with 14 days to close, that is either a very fast acceleration or a forecasting discipline issue worth discussing. The whitespace figure at the bottom signals that the relationship does not end at close — Meridian is a $905,000 total account potential. The team that celebrated the close should also be aware that $480,000 is still on the table for the next 12–24 months.
-->

---

## The Customer

# Who Bought — and Why They Trusted Us

- **Primary champion:** Dr. Lisa Chandra, SVP Operations — drove internal consensus; personally called our CEO reference
- **Economic buyer:** Brian Holt, CFO — approved based on 7-month payback model
- **Pivotal stakeholder:** Marcus Webb, Director PA Operations — became internal advocate after the shadow-mode demo
- *Priya Nair (VP IT) started neutral and ended supportive — her ticket #4471 resolution was the turning point*

<!-- Speaker notes:
The stakeholder story is the most valuable learning in any win wire. Understanding who the champions were, who was neutral, and who was a risk — and what moved each person — is directly applicable to the next healthcare IDN deal. Dr. Chandra personally calling the CEO reference is significant: she was not just interested, she was doing due diligence on the relationship. That behavior signals a buyer who takes vendor relationships seriously — a strong predictor of a healthy, expanding account post-sale. Marcus Webb becoming an advocate after the shadow-mode demo is a repeatable tactic. In future similar deals, prioritize getting the operations team into a shadow-mode demonstration early. They are the daily users; if they love it, they become internal champions. The Priya Nair story — started neutral, ended supportive, turned on a ticket resolution — is the most instructive detail in this slide. The lesson: do not neglect skeptical stakeholders. Resolving a single open ticket in a timely, professional manner converted a potential blocker into a supporter.
-->

---

## Who We Beat

# Competitive Win — and What Made the Difference

**Competitor:** Veradigm (incumbent, 7-year relationship)

- *Why they lost:* Product in maintenance mode; 14-month release gap; batch Epic integration; no denial prediction capability
- *Why we won:* Native FHIR R4 real-time integration + pre-submission completeness check + outcome guarantee

**Competitive intelligence for future deals:**
- Veradigm's renewal conversations begin 6 months before contract end — get in 8–9 months out
- Their support team response time is 48–72 hours — our 4-hour SLA is a direct differentiator
- They cannot match our performance guarantee — no competitors in this segment offer one

<!-- Speaker notes:
The competitive section is the intelligence goldmine of the win wire. Every field team member should read this and know it. Veradigm's 14-month release gap is public knowledge — it can be verified from their product release notes and customer reviews on G2 or KLAS. The 48–72 hour support response time is competitive intelligence you should be careful about citing by name externally — but internally it is fair game for preparing the team. The strategic timing insight — "get in 8–9 months before contract end" — is based on this specific win. Veradigm started their renewal at 6 months; SponAI engaged at month 4 (February) for an October contract end. That 4-month head start created the relationship and the demonstration opportunity that ultimately won the deal. Codify this as a prospecting trigger: set alerts for Veradigm customers whose contracts end in 9–12 months. The competitive displacement playbook that worked here should be shared with the broader team as a template.
-->

---

## The Team

# Everyone Who Made This Happen

| Name | Role | Contribution |
|---|---|---|
| James Whitfield | Account Executive | Deal strategy, executive relationships, close |
| Dr. Ana Reyes | Clinical AI Architect | Technical credibility with clinical operations team |
| Kevin Park | Integration Engineer | FHIR demo — closed the VP IT concern |
| Tamara Ellis | Customer Success | CSM commitment signal — Dr. Chandra asked for Tamara by name |
| Leadership | CEO reference call | Brian Holt called our CEO — response within the same day |

*Support team: 3 tickets resolved during the evaluation phase — all within 4 hours*

<!-- Speaker notes:
The team slide is about giving credit — specifically and publicly. Do not leave anyone out. The integration engineer who gave a 30-minute FHIR demo to a skeptical VP of IT deserves the same recognition as the AE who ran the board-level executive meeting. "Dr. Chandra asked for Tamara by name" is a remarkable signal: the customer had enough confidence in the CSM relationship before contract signature that she named her in the procurement conversation. That is the gold standard of customer success pre-sale engagement. The CEO reference call story — Holt called and got a same-day response from our CEO — should be told in every onboarding of new sales team members. Executive responsiveness is a competitive differentiator that does not show up in product comparison tables but wins deals. The support team acknowledgment is intentional: three tickets resolved during evaluation means the support team was part of the sales process whether they knew it or not. Recognize that.
-->

---

## Lessons Learned

# What to Replicate on the Next IDN Displacement

- **The shadow-mode demo converted Marcus Webb** — build it into every healthcare operations evaluation; book it at week 3, not week 8
- **Ticket resolution won over Priya Nair** — assign an SE to monitor any open tickets for evaluation-phase accounts; 4-hour response is a sales tool, not just a support metric
- **CEO letter preceded CFO engagement** — the executive-to-executive letter 3 weeks before the final meeting warmed the CFO relationship; replicate for all Tier 1 accounts
- **Performance guarantee closed the risk conversation** — prospects who might otherwise slow down for "more evaluation" ran out of objections when the guarantee was on the table

<!-- Speaker notes:
The lessons slide is the most important slide in the win wire for the sales team. These four lessons should be turned into concrete playbook updates within 2 weeks of this meeting. Specifically: (1) the shadow-mode demo should be added to the standard healthcare displacement playbook at week 3. Document what it takes to prepare one. (2) The ticket monitoring process should be a formal account escalation protocol for evaluation-phase accounts — assign an SE owner with a 4-hour response commitment. (3) The CEO letter template should be created and added to the account review toolkit for Tier 1 strategic accounts. (4) The performance guarantee response training should be updated to include this objection scenario: "How do we bring up the guarantee when a prospect is stalling?" The answer, based on this deal: introduce it at the third executive meeting, not the first. Trust has to be established before the guarantee is credible.
-->

---

## Celebrate

# What This Win Means

> "Meridian Health is a four-hospital IDN with $1.2 billion in annual revenue, a 7-year incumbent relationship to displace, and a CFO who had not bought new enterprise software in 18 months. This team went in, earned trust methodically, solved real problems in the evaluation, and closed on time. This is what great work looks like."
> — [Sales Leadership Name], April 29, 2026

**The next stop: close the $480,000 whitespace before December 31, 2026.**

*James, Ana, Kevin, Tamara — well done.*

<!-- Speaker notes:
The closing slide is the emotional note the win wire should end on. A quote from leadership — genuine, specific, naming what was hard about the deal — lands very differently than a generic "great job." The detail in the quote — "$1.2 billion in revenue, 7-year incumbent, CFO who had not bought in 18 months" — shows that leadership actually understood the difficulty of the win. That specificity is what motivates. The final line — "the next stop: close the $480,000 whitespace" — is a bridge between celebration and the next mission. Teams that celebrate and immediately re-energize are the highest-performing teams. Naming the $480K whitespace target converts the win into a foundation rather than a finish line. End the meeting on time. Win wires should be 20–30 minutes, no longer. After the meeting, the AE sends a brief email to the customer thanking them for the partnership — a single, warm sentence that starts the post-sale relationship on the right tone.
-->
