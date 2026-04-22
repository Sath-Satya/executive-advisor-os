<!-- TEMPLATE: proposal-deck
     CATEGORY: Sales
     USE WHEN: formal proposal presentation to an executive buyer or committee
     SLIDE COUNT: 11
     PALETTE: Executive cream
     RENDER: marp --pptx 73-proposal-deck.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', 'DM Sans', system-ui, sans-serif;
    background: #f7f4ef;
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
    color: #b8965a;
    font-size: 0.85em;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 { color: #0e1b2e; font-size: 1.05em; font-weight: 700; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; font-weight: 700; }
  em { color: #b8965a; font-style: normal; font-weight: 600; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "▸ "; color: #b8965a; }
  ul li { margin-bottom: 0.6em; font-size: 1em; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
  th {
    background: #ede9e1;
    color: #8899ac;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.06em;
    font-size: 0.8em;
    text-transform: uppercase;
    border-bottom: 2px solid #d6cfc3;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #ede9e1; }
  tr:last-child td { border-bottom: none; }
  blockquote {
    border-left: 4px solid #b8965a;
    padding: 12px 24px;
    margin: 1em 0;
    background: #ede9e1;
    border-radius: 0 8px 8px 0;
    font-style: italic;
    color: #0e1b2e;
    font-size: 1.05em;
  }
  section::after { color: #c4bdb3; font-size: 0.75em; }
---

## Proposal — Meridian Health

# AI-Powered Claims Operations Transformation

*Presented by SponAI Consulting &nbsp;|&nbsp; April 28, 2026*

*Prepared for: Dr. Lisa Chandra, SVP Operations &nbsp;|&nbsp; Brian Holt, CFO*

<!-- Speaker notes:
The proposal cover slide should be sent as a PDF 24 hours before the meeting, so the economic buyers arrive having read it. In the meeting, do not read the cover — acknowledge it and transition: "You have had time to review the document. I want to use our time today to walk through the parts that matter most to your decision, answer your questions, and discuss terms." That framing respects their time and signals that you are not going to read slides at them. The dual addressees — Dr. Chandra as champion and Brian Holt as CFO — signal that this proposal was written for both audiences. Dr. Chandra cares about operational outcomes; Brian Holt cares about financial return. Both perspectives are represented in this deck. Confirm attendees before the meeting: if additional stakeholders are joining (VP IT, Legal), ensure you are prepared for their specific concerns. Proposals presented to a larger audience than expected often fail because the seller was not prepared for questions from new voices.
-->

---

## Our Understanding

# The Problem We Are Here to Solve

- **Claims processing backlog:** 2,400+ pended claims per week; average 14-day clearance cycle
- **Authorization denial rate:** 18% — 4 points above national average; $3.1M in avoidable rework
- **Staff utilization:** 6 FTE spending 70% of their time on tasks that have no clinical judgment component
- *Root cause: three disconnected systems with no common data layer and no automated routing*

<!-- Speaker notes:
The "understanding" slide is the highest-stakes slide in the proposal deck. If you get this wrong — if the customer says "that is not quite our problem" — you lose credibility that is very difficult to rebuild. Validate this slide with your champion before the meeting: send it to Dr. Chandra 48 hours in advance and ask: "Does this accurately capture the situation?" If she corrects you, update the slide. A corrected slide that the champion helped you write is more persuasive than a perfect slide you wrote alone. The root cause line at the bottom is where you differentiate yourself from competitors. Most proposals describe the symptoms — the backlog, the denial rate, the FTE time. The root cause — three disconnected systems — is the insight that justifies the solution you are about to propose. If competitors are proposing point solutions for each symptom, your proposal addresses the structural cause. That is a fundamentally different and more defensible position.
-->

---

## Objectives

# What Success Looks Like at 12 Months

- **Reduce pended claims cycle from 14 days to 4 days** — targeting top-quartile national performance
- **Lower authorization denial rate from 18% to below 8%** through AI-driven completeness checks
- **Redeploy 4 FTE** from manual routing to clinical coordination and member advocacy
- *Financial target: $2.8M net annual benefit &nbsp;|&nbsp; Payback: 7 months on proposed investment*

<!-- Speaker notes:
The objectives slide converts discovery findings into specific, measurable commitments. Every number should be traceable to either the customer's own data or a named industry benchmark. "Top-quartile national performance" is not vague — KLAS and MGMA publish this data annually, and you should be able to cite the specific benchmark. The 4 FTE redeployment number should be conservative: if you calculate 5 FTE and commit to 4, you deliver upside at the 12-month review. If you commit to 5 and deliver 4, you are explaining a miss. The financial target of $2.8M should be built line by line and available as a supporting document. Economic buyers scrutinize ROI models — have the spreadsheet ready. The payback of 7 months is the number that closes. Most CFOs have an informal payback threshold for discretionary IT investment: anything under 12 months gets approved without a committee; anything over 18 months requires a board-level case. You are comfortably inside the threshold.
-->

---

## Our Approach

# How We Deliver — Without Disrupting Operations

- **Phase 1 (Weeks 1–4):** Integration mapping — FHIR R4 connector to your Epic instance; no workflow changes
- **Phase 2 (Weeks 5–10):** AI engine deployment — claims triage, authorization completeness, denial pattern detection
- **Phase 3 (Weeks 11–16):** Staff transition — retraining program, dashboard go-live, FTE redeployment plan

*All three phases run in parallel with live operations. Zero planned downtime. Weekly status reports.*

<!-- Speaker notes:
"Without disrupting operations" is the headline that every COO and SVP Operations wants to hear. The fear in any large-scale IT deployment is that the transition will cause more disruption than the problem it was solving. Your three-phase approach directly addresses this fear. Phase 1 is integration only — no workflow changes. Staff do not know anything has changed. Phase 2 deploys the AI engine in shadow mode: it runs alongside existing processes before taking over routing. This builds confidence in the model's accuracy before it handles live cases. Phase 3 is the hardest phase: retraining staff who have done the same work for years. Be specific about what "retraining program" means. A 4-hour workshop per department? A dedicated change management resource? Specify it. The weekly status report commitment is a small thing that matters enormously. Customers who feel informed do not escalate. Customers who feel surprised escalate immediately. Over-communicate during deployment.
-->

---

## Scope

# What Is Included — and What Is Not

**In scope:**
- Claims AI triage module (Epic-connected)
- Prior authorization completeness engine
- Denial pattern analytics dashboard
- 12-month managed service and support tier

**Out of scope:**
- EMR system changes or upgrades
- Payer connectivity (Availity integration handled by your IT team)
- Staffing decisions — redeployment plan is advisory only

<!-- Speaker notes:
The scope slide is the most important risk-management slide in the proposal. Scope creep is the primary cause of project overruns, and in enterprise consulting, scope creep is often caused by ambiguity at proposal time — not bad-faith customers. By explicitly naming what is out of scope, you are protecting yourself and setting clear expectations for both teams. The "EMR system changes" out-of-scope line is critical: if Meridian's Epic installation requires any custom development to support your integration, that is their IT team's scope, not yours. Confirm this with Priya Nair before the meeting. The "staffing decisions are advisory only" line is a legal and relationship boundary: you are providing a redeployment plan, but you cannot make Meridian's HR decisions. This protects you from being blamed if the redeployment is handled differently than your recommendation. After presenting this slide, ask: "Are there any items in the out-of-scope list that you expected to be included? Better to address that now than after signature."
-->

---

## Deliverables

# What You Will Receive

| Deliverable | Format | Milestone |
|---|---|---|
| Integration specification | Technical document | End of Week 2 |
| AI engine — shadow mode live | Working system | End of Week 8 |
| Staff retraining program | Workshop + playbook | Week 12 |
| Analytics dashboard | Live web app | Week 14 |
| 90-day performance report | Executive PDF | Week 16 |
| 12-month managed service | Ongoing | Post go-live |

*Every deliverable has a written acceptance criteria — approved by you before we begin*

<!-- Speaker notes:
The deliverables table transforms the proposal from a promise into a contract. Each row names a specific output with a format and a milestone. The last row — "every deliverable has written acceptance criteria" — is the quality gate that protects both parties. Before you write a single line of integration code, Meridian's team reviews and approves the criteria for what "done" looks like for that deliverable. This eliminates the most common source of delivery disputes: "we thought it would do X, you delivered Y." After presenting this slide, offer to walk through the acceptance criteria process: "We have a template for this — would it be useful to review it with your IT lead before contract signature? It typically takes 90 minutes and saves weeks of rework." That offer signals maturity and builds confidence that you have done this before.
-->

---

## Timeline

# 16 Weeks to Full Production

| Phase | Weeks | Key Milestone |
|---|---|---|
| Integration & setup | 1–4 | FHIR connector approved by Meridian IT |
| AI engine deployment | 5–10 | Shadow mode validation — 95% routing accuracy |
| Staff transition | 11–14 | First department fully redeployed |
| Go-live & stabilization | 15–16 | All departments live, 90-day clock starts |

*Project start date: May 12, 2026 &nbsp;|&nbsp; Production go-live: September 8, 2026*

<!-- Speaker notes:
Sixteen weeks is a compressed timeline for an enterprise deployment of this scale. The key enabler is the FHIR R4 native integration — there is no custom middleware to build. If Meridian's IT team has concerns about the timeline, address them directly: "The 16-week commitment assumes standard FHIR R4 Epic connectivity. If there are non-standard configurations in your environment, we can assess in Week 1 and provide a revised plan by Week 2 — before any timeline commitment is locked in." The shadow mode validation milestone in Weeks 5–10 is the riskiest phase from an engineering perspective. Building in validation gates — "95% routing accuracy before production" — means that if the AI engine underperforms, you catch it before it affects operations. The 90-day performance clock starts at go-live, not at contract signature. This is important for ROI measurement: the clock starts when the system is running, not when the project begins.
-->

---

## Team

# The People Accountable to Your Success

| Name | Role | Background |
|---|---|---|
| James Whitfield | Engagement Lead | 14yr enterprise healthcare IT |
| Dr. Ana Reyes | Clinical AI Architect | MD + 8yr health informatics |
| Kevin Park | Integration Engineer | Epic-certified, FHIR specialist |
| Tamara Ellis | Customer Success Manager | 200+ enterprise deployments |

*Executive sponsor: Sathish T., Founder — available for escalation within 4 business hours*

<!-- Speaker notes:
The team slide is often underutilized in enterprise proposals. Buyers are not just buying a product — they are buying the people who will deliver it. Each row should show domain credibility relevant to the customer. Dr. Ana Reyes has an MD — that signals clinical credibility to a healthcare system that is skeptical of "tech people who do not understand care workflows." Kevin Park is Epic-certified — that is a specific, verifiable credential that reduces the integration risk in the customer's mind. Tamara Ellis's stat — 200+ enterprise deployments — signals operational scale. The executive sponsor line is a relationship signal: the founder is available for escalation. In large enterprise deals, knowing that the relationship goes to the top of the vendor organization matters to CFOs and SVPs who have been burned by "enterprise" vendors who disappear after signature. Before presenting this slide, confirm that every team member named is actually available for this engagement on the proposed timeline.
-->

---

## Investment

# Total Investment — Year 1

| Component | Investment |
|---|---|
| Phase 1–3 Implementation | $185,000 |
| Year 1 Managed Service | $115,000 |
| Staff Retraining Program | $35,000 |
| **Total Year 1 Investment** | **$335,000** |
| Year 2+ Annual Service (renewal) | $135,000/yr |

> **Net Year 1 benefit: $2,465,000 &nbsp;|&nbsp; ROI: 636% &nbsp;|&nbsp; Payback: 7 months**

<!-- Speaker notes:
Price presentation is a skill. Never apologize for the number. Never say "I know this is a lot." Present the investment table and then move directly to the ROI. The blockquote at the bottom is the most important number in the deck: $2,465,000 net Year 1 benefit. That is the return after paying you. For a CFO evaluating a $335,000 investment, a $2.8M gross benefit and $2.5M net benefit at 7-month payback is not a difficult decision — it is a prioritization decision. The risk is that the investment is split across three line items, which makes it look large. You can simplify if needed: "Think of it as $335K in Year 1, then $135K per year to maintain the platform. Year 1 is the investment year. Year 2 forward is pure margin." Year 2 economics are important for multi-year contract negotiations — at $135K annual service on a $2.8M annual benefit, the ongoing ROI is extraordinary. Use that math in renewal conversations.
-->

---

## Terms and Conditions

# Contract Structure

- **Term:** 1-year initial + auto-renewing annually with 90-day cancellation notice
- **Payment:** 40% on contract signature, 40% at Phase 2 go-live, 20% at 90-day review
- **Performance guarantee:** If denial rate does not reach below 12% by Day 90, pro-rata credit applied
- **Data handling:** HIPAA BAA included; SOC 2 Type II certified; data deletion within 30 days of contract end

*Standard MSA available for legal review — redline turnaround within 5 business days*

<!-- Speaker notes:
The terms slide should be presented matter-of-factly — it is not a confrontation, it is a plan. The payment structure is designed to align incentives: 40% at signature means you are funded to start; 40% at Phase 2 go-live means you do not collect the bulk until you have delivered something working; 20% at the 90-day review means the final payment is tied to demonstrated performance. The performance guarantee — "if denial rate does not reach below 12% by Day 90" — is a risk reversal that removes the biggest objection from risk-averse buyers. Twelve percent is significantly better than their current 18% but below the committed 8% target — it is a floor, not the ceiling. The data handling terms matter enormously to healthcare buyers. HIPAA BAA is non-negotiable for any PHI touching system. SOC 2 Type II is the enterprise security minimum. Have both documents ready to share in the data room on the same day as this meeting. Legal teams that have to wait two weeks for a BAA will slow your entire close.
-->

---

## Why SponAI Consulting

# What Makes This Proposal Different

- **Healthcare-native:** Every consultant on your team has healthcare IT experience — no learning curve at your expense
- **AI that integrates, not replaces:** Our platform runs inside your existing Epic environment, not beside it
- **Performance-backed:** We put a guarantee in writing. Most competitors do not.
- *Meridian Health would be our fourth IDN on Epic — reference calls available with all three*

<!-- Speaker notes:
The "why us" slide is your chance to make the competitive differentiation explicit without naming competitors. Each bullet is a genuine differentiator: healthcare-native means that the consultants who will be in Meridian's building have seen Epic before. "AI that integrates, not replaces" is a direct counter to competitors who require replacing the EHR workflow — that is a 12–18 month project, not a 16-week implementation. The performance guarantee is rare in enterprise software consulting. Most competitors offer SLAs around uptime, not business outcomes. Offering an outcome guarantee signals confidence and shifts the risk calculation for the buyer. The reference offer at the bottom — three IDN clients, all on Epic — is a closing device. Before you leave this meeting, offer to connect Dr. Chandra with her peer at one of the three reference sites. A peer conversation between two SVP Operations at comparable health systems is worth more than anything you can say in this room.
-->

---

## The Ask

# Three Decisions — This Month

1. **Approve the proposal** — legal review complete by May 5, contract signed by May 9
2. **Identify the IT lead** — Priya Nair or designee confirmed as integration owner by May 9
3. **Confirm May 12 kickoff** — first joint team meeting, 2 hours, on-site at Meridian

*James Whitfield &nbsp;|&nbsp; james.whitfield@sponai.com &nbsp;|&nbsp; (415) 555-0147*

*SponAI Consulting &nbsp;|&nbsp; sponaitech.com*

<!-- Speaker notes:
Three decisions with hard dates. This is the close. Do not soften it with "whenever you are ready" or "take the time you need." Specific dates drive specific actions. The May 9 contract signature target is 11 days from the proposal date — aggressive but achievable for a well-prepared legal team with a standard MSA. If they push back on timing, ask: "What would you need from us to meet that date?" That question turns a delay into a project plan. The IT lead identification is a low-stakes ask that signals momentum: asking them to confirm Priya Nair's role costs them nothing and creates internal accountability on their side. The kickoff confirmation is the highest-value commitment because once internal calendars are blocked, the project feels real — and real projects close. After presenting this slide, be quiet. Give the room time to respond. The first person to speak after the close loses the negotiating position. If Brian Holt asks about price flexibility, you have slides 8 and 9 as your anchor — point back to the ROI math before any concession conversation.
-->
