<!-- TEMPLATE: pricing-negotiation
     CATEGORY: Sales
     USE WHEN: internal deal-desk review for a pricing exception or discount request
     SLIDE COUNT: 8
     PALETTE: Corporate
     RENDER: marp --pptx 75-pricing-negotiation.md -->
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
    font-size: 2.0em;
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

## Deal Desk Review — Confidential

# Meridian Health — Pricing Exception Request

*AE: James Whitfield &nbsp;|&nbsp; Deal Desk: [Approver Name] &nbsp;|&nbsp; April 28, 2026*

**Deal stage:** Verbal yes — pending legal and pricing approval

<!-- Speaker notes:
This is an internal deck — it never goes to the customer. The tone should be analytical and recommendation-oriented. The AE is presenting facts and asking for a decision. Avoid advocacy language that sounds like you are lobbying for the customer instead of presenting an honest case. The deal desk exists to protect margin and prevent precedent-setting discounts. Your job is to make a clean case for why this situation justifies an exception — or to accept that it does not. "Verbal yes pending legal and pricing" is an important context setter: the customer wants to buy. The question is whether the deal can be structured at the right economics for SponAI. Come to this meeting with a recommendation already formed. "I am requesting approval for Option B at the concession levels listed, with the conditions I will walk through." Deal desks do not like presenting AEs who are undecided — they want a position to react to.
-->

---

## Deal Context

# What Meridian Is Asking For — and Why

- **Customer:** Meridian Health — 4-hospital IDN, 2,800 staff, $1.2B annual revenue
- **Proposed deal:** $335,000 Year 1 (implementation + managed service) + $135,000/yr ongoing
- **Customer ask:** 15% discount on Year 1 implementation + 2-year price lock on managed service
- **Reason given:** Healthcare budget cycle requires Q1 approval to land before May 31 procurement freeze

*Customer's procurement team provided written confirmation of the budget freeze deadline*

<!-- Speaker notes:
The context slide answers the deal desk's first three questions: who is the customer, what are the economics, and what is the ask. The budget freeze deadline with written confirmation is a legitimate urgency trigger — not a manufactured one. Verify it before presenting. If the customer gave you a verbal deadline without documentation, note that: "We have a verbal on the freeze date — we are seeking written confirmation before relying on it as a close condition." The customer's revenue — $1.2B — is relevant because it establishes their ability to pay at standard rate. A $335K deal to a $1.2B revenue organization is 0.03% of revenue. This is not a budget-constrained customer; this is a procurement-constrained customer. The distinction matters for the concession analysis: a price concession based on inability to pay is different from a price concession based on procurement timing. The latter is a conversion lever, not a structural discount.
-->

---

## Customer Ask — The Three Options

# Paths to Close This Deal

| Option | Year 1 Revenue | Year 2 Revenue | Gross Margin Impact | AE Recommendation |
|---|---|---|---|---|
| A — Walk away / hold standard | $335,000 | $135,000 | 0% | No — deal at risk |
| B — 10% Y1 discount + 2-yr lock | $301,500 | $135,000/yr | -$33,500 Y1 | **Yes — recommended** |
| C — 15% Y1 discount + 2-yr lock | $284,750 | $135,000/yr | -$50,250 Y1 | No — margin risk |

*Option B recovers the Y1 discount in 2.4 months of Y2 managed service*

<!-- Speaker notes:
Three options with explicit financials. The deal desk should never be in the position of doing the math themselves — you should do it for them. Option A — no concession — is included to show you considered it. It should be presented honestly: the AE believes the deal is at risk if we hold standard pricing. Why? Customer has a competing offer (even if you do not know the details, a procurement freeze without a signed contract means a natural competitor engagement in the next cycle). Option C is presented as a cautionary boundary — you are showing where the margin impact becomes structurally unacceptable. Option B is the recommendation. The math backing it up: $33,500 Y1 discount divided by $135,000/yr managed service = 0.25 years = 3 months. The discount recovers in less than one quarter of Year 2 managed service revenue. That is a clear argument for the business case. The 2-year price lock actually protects revenue against future discount pressure at Year 2 renewal.
-->

---

## Revenue Impact Analysis

# What This Deal Means Over 3 Years

| Scenario | Y1 Revenue | Y2 Revenue | Y3 Revenue | 3-Yr Total |
|---|---|---|---|---|
| Standard (no deal) | $0 | $0 | $0 | $0 |
| Option A (close, no discount) | $335,000 | $135,000 | $135,000 | $605,000 |
| Option B (recommended) | $301,500 | $135,000 | $135,000 | $571,500 |
| Option C (maximum ask) | $284,750 | $135,000 | $135,000 | $554,750 |

*Standard scenario = deal lost in Q1, possible re-engagement in Q3 at unknown pricing pressure*

<!-- Speaker notes:
The 3-year revenue analysis puts the discount in context. A $33,500 Y1 concession on a $571,500 3-year deal is a 5.9% discount on total contract value — not 10%. Framing the concession as a percentage of total contract value (not just Year 1) is a legitimate and often persuasive reframe for deal desks that are focused on margin protection. The "standard scenario = $0" row is the most important row in this table. If we do not close the deal, we get nothing. A 5.9% discount on $571,500 is better than 100% of $0. That is the argument. The Q3 re-engagement risk is real: if Meridian goes through their May procurement freeze without signing, the next window is likely September or October. That is 5 months of no revenue and 5 months of competitor exposure. Healthcare procurement cycles are annual — missing a procurement window often means losing the deal to whoever was in position at the next cycle.
-->

---

## Strategic Value

# Why This Deal Is Worth the Exception

- **Reference account:** Meridian Health is a named IDN — first deployment in a 4-hospital system; enables template for 7 comparable IDNs in our pipeline
- **Product feedback:** Meridian's team has agreed to a formal feedback cycle for the Revenue Integrity Suite — product roadmap value of $150K+ in engineering direction
- **Competitive displacement:** displaces Veradigm at 2 of 4 hospitals — closes a competitive reference gap in the regional market

*Meridian as a reference accelerates 3 pipeline deals estimated at $825,000 combined ARR*

<!-- Speaker notes:
Strategic value is the argument the AE makes when the numbers alone do not close the deal desk. Three points: reference value, product value, and competitive value. Reference value is the hardest to quantify but often the most persuasive. If Meridian saying yes accelerates three other IDN deals, the $33,500 discount is not just a Y1 cost — it is a customer acquisition investment with a multiplier. The product feedback agreement is rare and should be named explicitly: a healthcare IDN providing structured feedback on your Revenue Integrity Suite roadmap is worth real engineering dollars. Put a number on it: "At our current eng billing rate, that feedback cycle is worth approximately $150K in product research." The competitive displacement of Veradigm is important to name even though the customer did not ask about it. The deal desk needs to know that closing this deal removes an incumbent from part of the Meridian footprint — that is a competitive objective beyond the revenue line.
-->

---

## Risk Assessment

# What Could Go Wrong — and Our Mitigation

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Precedent discount for similar deals | <span class="amber">Medium</span> | High | Document as IDN-specific, volume-based — not replicable at smaller accounts |
| Customer does not renew at Year 2 | <span class="amber">Low</span> | Medium | 2-yr price lock is mutual — they are committing to 2 years as condition of discount |
| Deal slips past May 31 anyway | <span class="amber">Low</span> | High | Customer procurement team has confirmed freeze date in writing |
| Margin compression in competitive situations | <span class="red">Ongoing</span> | High | Require deal-desk review for all discounts exceeding 8% — this is a one-time IDN exception |

<!-- Speaker notes:
The risk table shows the deal desk that the AE has thought beyond the immediate close. The precedent risk is the most important risk to address: every deal desk fears that a discount for one customer creates an expectation for all customers. The mitigation — "document as IDN-specific, volume-based" — is the contractual language that makes the exception non-replicable. The conditions for this exception are specific: IDN size (4+ hospitals), multi-year commitment, procurement freeze documentation. A small group practice cannot claim the same exception because they do not meet the conditions. The "requiring deal-desk review for all discounts exceeding 8%" note is a concession to the deal desk's oversight function — you are acknowledging their role and proposing a control mechanism that makes the exception sustainable.
-->

---

## Recommendation

# AE Recommendation — Option B

- **Grant:** 10% Year 1 discount ($301,500) with mandatory 2-year managed service commitment
- **Conditions:** Customer provides written procurement deadline confirmation; contract signed by May 24, 2026
- **Do not grant:** Any discount on managed service rate ($135K/yr is the floor) &nbsp;|&nbsp; Any Y3 price lock
- **Expiry:** This approval expires May 31, 2026 — if deal does not close, standard pricing applies

*Requesting deal-desk approval by April 30, 2026 — verbal approval sufficient to proceed to legal*

<!-- Speaker notes:
The recommendation slide should be the clearest slide in the deck. One option, specific conditions, explicit boundaries, and an expiry. The deal desk does not want to think — they want to react to a specific proposal. "Verbal approval sufficient to proceed to legal" is an efficiency request: you are not asking for a signed form before you can move. A verbal "yes" from the deal desk lead allows the AE to proceed to legal review in parallel with any internal documentation. The May 24 contract signature condition is 7 days before the May 31 approval expiry. That buffer handles minor delays without requiring a second approval. The "do not grant" line is as important as the "grant" line. You are proactively drawing the boundary around managed service pricing. If the customer comes back asking for a discount on the $135K/yr rate, the AE has a clear internal backstop: "That was not part of the approved exception." Boundaries protect the AE as much as the company.
-->

---

## Decision

# Deal Desk — What We Need

**Approvals needed:**
1. Option B pricing exception — 10% Y1 discount, standard Y2/Y3 managed service
2. 2-year managed service commitment as condition precedent
3. IDN-specific exception classification — not a replicable standard

**Decision owner:** [VP Revenue / Chief Revenue Officer]

**Deadline:** April 30, 2026 — customer legal review starts May 1

*If additional review is needed, please advise within 24 hours so timeline can be adjusted.*

<!-- Speaker notes:
The decision slide closes the internal review with a specific ask and a clear owner. "Decision owner" should be a name, not a title — whoever approves pricing exceptions in your organization should be named on this slide. If you are uncertain, confirm before the meeting. The 24-hour advisory request is a professional courtesy that also creates internal urgency without being pushy. If the decision owner needs additional information or a second review, you want to know that now — not on April 30. After presenting this slide, distribute the deck as a PDF to the deal desk attendees and follow up within 4 hours with a brief email summary: "Per our meeting, I am requesting Option B approval by April 30. Happy to answer any follow-up questions via email or a 15-minute call." Written records of internal approval conversations protect the AE if the approved deal is later scrutinized.
-->
