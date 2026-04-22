<!-- TEMPLATE: kickoff-deck
     CATEGORY: Sales
     USE WHEN: customer kickoff meeting after contract signature (post-sale)
     SLIDE COUNT: 10
     PALETTE: Clean light
     RENDER: marp --pptx 79-kickoff-deck.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', 'DM Sans', system-ui, sans-serif;
    background: #ffffff;
    color: #1c2b3a;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'Segoe UI', system-ui, sans-serif;
    color: #0e1b2e;
    letter-spacing: -0.3px;
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
  h3 { color: #0e1b2e; font-size: 1.05em; font-weight: 700; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; font-weight: 700; }
  em { color: #3b9eff; font-style: normal; font-weight: 600; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "▸ "; color: #3b9eff; }
  ul li { margin-bottom: 0.6em; font-size: 1em; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
  th {
    background: #f0f6ff;
    color: #556677;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.06em;
    font-size: 0.8em;
    text-transform: uppercase;
    border-bottom: 2px solid #dde8f5;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #f0f6ff; }
  tr:last-child td { border-bottom: none; }
  blockquote {
    border-left: 4px solid #3b9eff;
    padding: 12px 24px;
    margin: 1em 0;
    background: #f0f6ff;
    border-radius: 0 8px 8px 0;
    color: #0e1b2e;
    font-size: 1.05em;
  }
  .green { color: #2dd4a0; font-weight: 700; }
  .amber { color: #f0a050; font-weight: 700; }
  section::after { color: #8899ac; font-size: 0.75em; }
---

## Project Kickoff — Meridian Health

# Welcome to the Team — Let's Build Something Great

*SponAI Consulting &nbsp;|&nbsp; May 12, 2026*

*Project: Claims AI Transformation &nbsp;|&nbsp; Contract Signed: April 28, 2026*

<!-- Speaker notes:
The kickoff meeting is the first impression of how SponAI delivers — not sells. The tone shift from sales to delivery is important. The people in this room may or may not have been part of the procurement decision. You will likely meet new faces: IT administrators, integration engineers, department managers, and analysts. Set the tone in your opening: "Thank you for trusting us with this project. Our job from today forward is to deliver exactly what we committed to in the contract — on time and with transparency at every step." Two things matter most in a kickoff: establishing trust with the delivery team (not just the executive sponsors) and creating clarity about how decisions will be made. Before this meeting, confirm the attendance list with Dr. Chandra. The kickoff should include: your engagement lead, integration engineer, CSM, and clinical architect — and from Meridian: operations lead, IT lead, and at least one department representative from the first phase.
-->

---

## Team Introductions

# The People Behind the Project

| SponAI Consulting | Role | Contact |
|---|---|---|
| James Whitfield | Engagement Lead | james.whitfield@sponaitech.com |
| Dr. Ana Reyes | Clinical AI Architect | ana.reyes@sponaitech.com |
| Kevin Park | Integration Engineer | kevin.park@sponaitech.com |
| Tamara Ellis | Customer Success Manager | tamara.ellis@sponaitech.com |

*Executive escalation: Sathish T., Founder — available within 4 business hours*

**Your Meridian Project Contacts:**
- Primary: Dr. Lisa Chandra (SVP Operations)
- IT Lead: Priya Nair (VP IT)
- Day-to-day: Marcus Webb (Director, PA Operations)

<!-- Speaker notes:
The team slide establishes the human side of the engagement. Take 30–45 seconds to introduce each SponAI team member with one sentence about their specific role on this project — not their job title. "Ana is our clinical AI architect — she will be the person you call when the system is doing something you do not understand and you need a clinical explanation for why." That specificity makes the introduction memorable. Ask the Meridian team to introduce themselves as well. Note who is new to the project that was not in the sales process — these are the people you need to earn trust with from scratch. The executive escalation path should be treated seriously. If Dr. Chandra says "I hope I never have to call him," your response is: "I hope so too. But knowing the path exists means you never have to navigate an unresolved issue alone." Customers who feel they have escalation access are more tolerant of the normal turbulence of project delivery.
-->

---

## Project Goals

# What We Are Here to Achieve Together

- **Primary:** Reduce claims processing cycle from 14 days to 4 days average
- **Secondary:** Lower prior authorization denial rate from 18% to below 8%
- **Tertiary:** Redeploy 4 FTE from manual routing to higher-value clinical coordination work
- *Financial target: $2.8M net benefit in the first 12 months of full production*

> "These are not our goals — they are your goals. We are here to help you achieve them."

<!-- Speaker notes:
The goals slide is read from the contract — not from a new document. Show the Meridian team that you have internalized what they committed to. The quote at the bottom is important: "These are not our goals — they are your goals." That framing shifts the relationship from vendor-customer to partnership. You are not delivering a product; you are helping them achieve outcomes they have already committed to internally. After presenting this slide, ask the room: "Before we go further, is there anyone here who has not seen these goals before, or who would like to discuss whether they are realistic given the current state of operations?" That question surfaces concerns early. A team member who thinks the 4-day cycle is impossible will tell you now — which is infinitely better than telling you after six weeks of deployment. If someone raises a concern, thank them: "That is exactly the kind of thing I want to know in Week 1. Let's put it in the risk register and address it in our first status call."
-->

---

## Success Criteria

# How We Will Know This Project Worked

| Metric | Baseline | Target | Measurement Method |
|---|---|---|---|
| Claims cycle time | 14 days | 4 days | Claims data extract — weekly |
| Authorization denial rate | 18% | Below 8% | Payer remittance report |
| FTE hours on manual routing | 65% of 6 FTE | Below 20% | Time-tracking logs (Marcus Webb's team) |
| Platform uptime | N/A | 99.5% minimum | SponAI monitoring dashboard |
| Staff satisfaction | N/A | Above 70 NPS | 30-day and 90-day surveys |

*Success criteria are locked as of this meeting. Changes require written agreement from both parties.*

<!-- Speaker notes:
Success criteria should be immovable after this meeting. The "locked as of this meeting" language is important: it prevents scope creep and protects both parties from measurement disputes at the 90-day review. Before this meeting, confirm that the baseline data — 14-day cycle, 18% denial rate, 65% FTE hours — has been verified against Meridian's actual operational data, not the estimate from the discovery call. If the baseline is different from what was assumed in the proposal, surface it now: "We had estimated 14-day average cycle time. Your February data shows 16 days. Should we update the baseline?" A higher baseline means the target improvement is larger, which may strengthen the ROI case. The staff NPS measurement at 30 and 90 days is a leading indicator of adoption. If the 30-day NPS is below 50, schedule an intervention before the 90-day review. Low early NPS almost always predicts low adoption at production scale.
-->

---

## Project Timeline

# 16 Weeks — Week by Week

| Week | Phase | Key Deliverable |
|---|---|---|
| 1–2 | Integration setup | FHIR connector configuration |
| 3–4 | Data validation | Epic data quality report |
| 5–8 | AI engine deployment | Shadow mode — 10,000 claim sample |
| 9–10 | Shadow mode validation | Accuracy report — target 95% |
| 11–12 | Staff training | PA Operations team certified |
| 13 | Department 1 cutover | PA Operations live |
| 14–15 | Full deployment | All departments live |
| 16 | Go-live stabilization | 90-day clock starts |

*Production go-live: September 8, 2026 &nbsp;|&nbsp; 90-day review: December 8, 2026*

<!-- Speaker notes:
Walk through this timeline at a pace that lets the Meridian team absorb each phase. At the end, ask: "Is there anything in this timeline that conflicts with your organization's schedule?" Healthcare organizations have predictable busy periods: year-end financial close, JCAHO surveys, open enrollment cycles. If any phase conflicts with a Meridian-specific operational event, flag it now and adjust. The shadow mode validation in Weeks 9–10 is a decision gate: if the accuracy report comes back below 95%, the cutover plan needs to be revised. Build that conditional into the conversation: "At Week 10, we will sit down and review the accuracy report together. If we are above 95%, we proceed to Department 1 cutover on schedule. If we are below, we have a conversation about what needs to be adjusted before we go live." That transparency about decision gates builds trust — it shows that you are not going to push through a deployment that is not ready.
-->

---

## Milestones

# Checkpoints That Require Your Sign-Off

| Milestone | Date | Owner (SponAI) | Owner (Meridian) |
|---|---|---|---|
| FHIR connector approved | May 26 | Kevin Park | Priya Nair |
| Data quality report accepted | June 9 | Dr. Ana Reyes | Marcus Webb |
| Shadow mode accuracy approved | July 28 | Dr. Ana Reyes | Marcus Webb |
| Department 1 cutover approved | August 11 | James Whitfield | Dr. Chandra |
| Full production approved | August 25 | James Whitfield | Dr. Chandra |
| 90-day review completed | December 8 | Tamara Ellis | Brian Holt |

<!-- Speaker notes:
The milestones table is the project governance structure in one slide. Every milestone requires approval from both parties — this is intentional. It prevents SponAI from unilaterally advancing a project phase without customer sign-off, and it prevents Meridian from being surprised by phase transitions. The joint ownership model is also a partnership signal: both organizations are accountable for progress. After presenting this slide, confirm each Meridian owner verbally: "Priya, you are listed as the approver for the FHIR connector — are you comfortable with that?" If Priya says she would prefer to delegate to a team member, update the table now. Wrong names on a governance document cause confusion and delay at every milestone. The 90-day review with Brian Holt is the financial accountability checkpoint. The CFO being listed as the Meridian owner sends a signal to the entire project team: this is not just an IT project, it is a business outcome project.
-->

---

## Meeting Cadence

# How We Stay Aligned Throughout the Project

| Meeting | Frequency | Attendees | Format |
|---|---|---|---|
| Weekly status call | Every Monday, 10am PST | AE + CSM + Meridian ops lead | 30 min, standing agenda |
| Technical sync | Every Wednesday, 2pm PST | Kevin Park + Priya Nair team | 45 min, issue resolution |
| Monthly executive update | First Friday of month | Engagement Lead + Dr. Chandra | 20 min, dashboard review |
| Milestone review | Per milestone table | Full team | 60 min, formal sign-off |
| 90-day review | December 8 | Full teams + Brian Holt | 90 min, formal presentation |

*All meetings have a written agenda 24 hours in advance. Decisions are documented in the meeting notes.*

<!-- Speaker notes:
The meeting cadence slide is often skipped in kickoff decks. It should not be. Consistent meeting structure is the single most effective tool for preventing project drift and building the relationship between delivery teams. The standing Monday status call keeps both teams accountable week-over-week. The Wednesday technical sync keeps Kevin Park and Priya Nair's team aligned on integration issues before they become escalations. The monthly executive update is specifically short — 20 minutes — because Dr. Chandra is busy. A tight monthly check-in that shows progress against the success criteria table is all she needs. If something requires more than 20 minutes, it should be a separate meeting. "Decisions are documented in the meeting notes" is a discipline that prevents "I thought we agreed on X" conversations. The CSM owns meeting notes distribution within 2 hours of each meeting. Send them even when nothing new happened — the discipline of regular communication is itself a value signal.
-->

---

## Escalation Path

# What to Do When Something Goes Wrong

**Level 1 — Day-to-day issues:** Marcus Webb (Meridian) + Tamara Ellis (SponAI)
*Resolution target: 24 hours*

**Level 2 — Project risk or delay:** Dr. Lisa Chandra (Meridian) + James Whitfield (SponAI)
*Resolution target: 48 hours*

**Level 3 — Contract or critical issue:** Brian Holt (Meridian) + Sathish T. (SponAI)
*Resolution target: 24 hours (critical path)*

*Escalation is not a failure — it is a feature. Use it early and often.*

<!-- Speaker notes:
The escalation path slide is about psychological safety. When teams know how to escalate, they escalate earlier — when problems are small. Teams that do not have a clear escalation path wait until problems are large, at which point they require executive attention and create relationship risk. "Escalation is not a failure — it is a feature" is a phrase worth saying out loud in the meeting. In enterprise consulting, the culture around escalation determines whether small problems stay small. The 24-hour response target for Level 1 and Level 3 issues may surprise the Meridian team — most vendors respond in 48–72 hours. Setting a 24-hour commitment and meeting it in the first real escalation will earn more trust than any marketing material. Before closing this slide, ask: "Is there any situation you can imagine that is not covered by these three levels?" That question pre-wires the team to think about edge cases — and often surfaces a concern that the Meridian team was hesitant to raise directly.
-->

---

## Risks

# What We Are Watching — Starting Today

| Risk | Owner | Status | Mitigation |
|---|---|---|---|
| FHIR configuration complexity | Kevin Park | <span class="amber">Open</span> | Discovery call with Epic team, Week 1 |
| Staff change resistance | Marcus Webb | <span class="amber">Open</span> | Change management workshop, Week 3 |
| Data quality issues in claims history | Dr. Ana Reyes | <span class="amber">Open</span> | Data audit, Week 2 |
| Timeline dependencies on Meridian IT | Priya Nair | <span class="amber">Open</span> | Resource commitment confirmed in kickoff |

*All risks are Open until resolved. No risks are Red at kickoff — earliest Red flag triggers an escalation.*

<!-- Speaker notes:
A risk register with all items "Open" at kickoff is normal and healthy. Every item on this list was identified during the sales process or the week before kickoff. "Open" does not mean "problematic" — it means "we are watching it." The change management risk is often the one that surprises healthcare organizations. Staff who have run the same process for years sometimes resist new tools, especially when those tools are described as AI. The Week 3 change management workshop should be designed in Week 2 with Marcus Webb's input — understanding the team's concerns before the workshop makes the workshop far more effective. The data quality risk is universal in healthcare IT: claims history data in older systems often has coding inconsistencies, legacy fields, and missing values. Finding these issues in Week 2 during the data audit is far better than finding them in Week 8 when the AI engine is running on live data. Priya Nair's commitment on IT resource availability should be documented: "We need your FHIR team available for 4–6 hours in Week 1. Priya, can you confirm that commitment?" Get a verbal yes in the room.
-->

---

## Next Steps

# What Happens in the Next 7 Days

- **May 13:** Kevin Park schedules FHIR discovery call with Meridian IT — Kevin + Priya Nair
- **May 14:** Tamara Ellis sends kickoff notes and standing meeting invites to full project team
- **May 15:** Dr. Ana Reyes delivers data access request list to Marcus Webb
- **May 19:** First weekly status call — 10am PST

*If any of these dates need to change, contact Tamara Ellis within 24 hours.*

*Thank you for trusting SponAI Consulting with this project. We will earn it every week.*

<!-- Speaker notes:
The final slide of a kickoff deck is the handoff from meeting to momentum. Four actions, four dates, four owners. The 7-day window creates immediate accountability — if Week 1 actions happen on time, it signals to the customer that SponAI's delivery culture matches the sales team's promises. The contact instruction — "if any of these dates need to change, contact Tamara Ellis within 24 hours" — establishes the CSM as the single point of contact for logistics. This prevents multiple threads of communication from creating confusion. The closing line — "Thank you for trusting SponAI Consulting with this project. We will earn it every week." — is the most important sentence in the deck. It sets the expectation that trust is earned through execution, not assumed from contract signature. In a room full of people who may be nervous about a new vendor and a new system, that sentence lands with genuine resonance. Say it slowly and mean it.
-->
