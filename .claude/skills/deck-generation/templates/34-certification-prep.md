<!-- TEMPLATE: certification-prep
     CATEGORY: Training / Certification
     USE WHEN: preparing a cohort or individual for a certification exam
     SLIDE COUNT: 14
     PALETTE: Clean dev
     RENDER: marp --pptx 34-certification-prep.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&family=DM+Serif+Display&family=DM+Mono&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #ffffff;
    color: #1c1a18;
    padding: 48px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', serif;
    color: #0e1b2e;
    font-size: 2.2em;
    letter-spacing: -0.4px;
    margin-bottom: 0.2em;
  }
  h2 { color: #0e1b2e; font-size: 1.35em; font-weight: 600; margin-bottom: 0.5em; }
  h3 { color: #3b9eff; font-size: 1em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; }
  em { color: #556677; font-style: normal; font-size: 0.87em; }
  code { font-family: 'DM Mono', monospace; background: #f0f4f8; color: #0e1b2e; padding: 0.15em 0.45em; border-radius: 3px; font-size: 0.88em; }
  ul { margin-top: 0.5em; }
  li { margin-bottom: 0.4em; line-height: 1.55; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #8899ac; }
  section.lead h1 { font-size: 2.8em; }
  section.lead p { font-size: 1.1em; color: #556677; }
  section.domain-slide { border-left: 5px solid #3b9eff; padding-left: 44px; }
  section.practice { background: #f0f7ff; border-top: 4px solid #3b9eff; }
  .domain-bar { display: flex; gap: 1em; margin-top: 1em; flex-wrap: wrap; }
  .domain-tag {
    background: #0e1b2e;
    color: #ffffff;
    font-family: 'DM Mono', monospace;
    font-size: 0.8em;
    padding: 0.3em 0.8em;
    border-radius: 3px;
    white-space: nowrap;
  }
  .domain-tag.highlight { background: #3b9eff; }
  .exam-meta { font-family: 'DM Mono', monospace; font-size: 0.82em; color: #556677; margin-top: 0.4em; }
---

<!-- _class: lead -->

# Salesforce Administrator Cert — Prep Guide

**Salesforce ADM 201** &nbsp;|&nbsp; SponAItech Internal Prep Program

*4-Week Study Plan · v2.0 · April 2025*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
This deck is the companion to the 4-week study plan. Learners should work through the full deck in a single 90-minute session, then return to the domain slides repeatedly during study. The deck is designed for both self-study and cohort delivery.

Exam context: the Salesforce Administrator certification (ADM 201) is required for all SponAItech consultants working in the Salesforce domain. The exam consists of 60 multiple-choice questions plus 5 unscored pilot questions. Passing score is 65%. Exam time: 105 minutes. Proctored online via Webassessor.

This prep guide is scoped to the six highest-weight exam domains. The full exam guide from Salesforce is the authoritative source — this guide is a study accelerator, not a replacement. Download the latest exam guide from trailhead.salesforce.com/credentials/administrator before your first study session and compare the domain weights to this deck.

Average preparation time for someone with 6+ months of Salesforce admin experience: 40–60 hours of study. For someone new to Salesforce: 80–120 hours. Calibrate the 4-week plan accordingly.
-->

---

## Exam Overview

**Certification:** Salesforce Certified Administrator (ADM 201)

<div class="exam-meta">
Format: 60 questions + 5 unscored pilot &nbsp;|&nbsp; Time: 105 min &nbsp;|&nbsp; Pass: 65% (39/60) &nbsp;|&nbsp; Cost: $200 USD
</div>

**Six exam domains:**

<div class="domain-bar">
  <span class="domain-tag highlight">Organization Setup 7%</span>
  <span class="domain-tag highlight">User Management 7%</span>
  <span class="domain-tag">Security & Access 14%</span>
  <span class="domain-tag highlight">Object Manager 8%</span>
  <span class="domain-tag">Sales & Marketing 14%</span>
  <span class="domain-tag">Service & Support 13%</span>
  <span class="domain-tag">Productivity 7%</span>
  <span class="domain-tag">Data Management 10%</span>
  <span class="domain-tag">Analytics 10%</span>
  <span class="domain-tag">Workflow 10%</span>
</div>

*Highlighted domains covered in depth in this deck — others in supplemental modules*

<!--
SPEAKER NOTES — SLIDE 2 (Exam Overview)
The exam weight distribution is the most important strategic input to your study plan. Do not study all domains equally — allocate time proportional to weight.

The three highest-weight domains are Security and Access (14%), Sales and Marketing Apps (14%), and Service and Support Apps (13%). Together they represent 41% of the exam. A candidate who masters only these three domains — and gets everything else right at 50% — will still pass.

The $200 exam cost creates a real financial stake. Remind learners: the retake policy is one free retake within 30 days of a failed attempt, then $200 per retake thereafter. The first attempt is the cheapest — prepare accordingly.

The 5 unscored pilot questions: you cannot tell which questions are pilot questions during the exam. Answer all 65 questions with the same care. Do not try to guess which ones do not count.

For cohort delivery: ask the group what their current experience level is before moving to the domain slides. Adjust your pacing based on the distribution of experience.
-->

---

## Domain 1 — Security and Access (14%)

<!-- _class: domain-slide -->

**Three security layers every admin must know:**

- **Org-level** — IP restrictions, login hours, trusted networks, MFA enforcement
- **Object-level** — profiles and permission sets control CRUD access per object
- **Field-level** — field-level security (FLS) controls read/edit access per field per profile

**Common exam traps:**
- Profiles set baseline; permission sets can only grant, never restrict
- FLS does not affect visibility via reports — reports bypass FLS for summary fields

<!--
SPEAKER NOTES — SLIDE 3 (Domain 1 — Security and Access, Part 1)
Security and Access is the single highest-weight domain on the exam. Every question in this domain is about understanding the layered security model. The key mental model: think of access control as nested containers. The org is the outer container (login restrictions). Objects are the middle containers (who can read, create, edit, delete records). Fields are the inner containers (who can see or modify specific data within a record).

The most frequently tested concept: the relationship between profiles and permission sets. Profiles set the minimum baseline — a user cannot exceed their profile. Permission sets can only expand what the profile allows, never restrict it. If an exam question asks "Which of the following can restrict a user's access to a field?" — the answer is always the profile, never a permission set.

The FLS and reports trap: candidates who have real admin experience sometimes get this wrong because they know from practice that reports can show field values that should theoretically be restricted. The exam answer follows the documented behavior: FLS applies in record detail pages and list views. Reports and dashboards may bypass FLS for summary/aggregate values. Know the documented behavior, not just your org's actual behavior.

Study resource: Trailhead module "Data Security" — 2 hours, directly maps to this domain.
-->

---

<!-- _class: domain-slide -->

## Domain 1 — Security and Access (14%)

**Record-level access — four mechanisms:**

| Mechanism | Controls |
|---|---|
| **Organization-wide defaults (OWD)** | Baseline sharing for all users |
| **Role hierarchy** | Managers see subordinates' records |
| **Sharing rules** | Extend access to groups or roles |
| **Manual sharing** | Record owner shares with specific user |

*OWD sets the floor — everything above it can only expand, never restrict*

<!--
SPEAKER NOTES — SLIDE 4 (Domain 1 — Security and Access, Part 2)
Record-level access is the second major concept in this domain. The four mechanisms operate in sequence. Start with OWD, then role hierarchy, then sharing rules, then manual sharing.

The "floor" concept: if OWD for Accounts is set to "Private," only the account owner can see the record by default. Everything else — role hierarchy, sharing rules, manual sharing — can only add people who can see that record. You cannot use sharing rules to hide a record from someone who can already see it via the role hierarchy.

High-frequency exam question pattern: "A user in Role A cannot see records owned by users in Role B. Both roles report to Role C. What must be true?" Answer: Role A and Role B are peer branches in the hierarchy, and OWD is set to a restrictive level. The manager in Role C can see records owned by either subordinate, but peers cannot see each other's records without a sharing rule.

Manual sharing: often overlooked by candidates. Manual sharing is done by the record owner (or admin) on a per-record basis. It does not survive record transfer — when an account is reassigned to a new owner, manual shares set by the previous owner are removed.

Practice: build a simple sharing scenario in a dev org and test each mechanism. Hands-on memory is durable memory.
-->

---

<!-- _class: domain-slide -->

## Domain 2 — Sales and Marketing Apps (14%)

**Leads and opportunities — the conversion model:**

- **Lead** — unqualified prospect; lives outside the standard sales objects
- **Convert** — creates Contact, Account, and optionally Opportunity in one action
- **Opportunity** — qualified deal with stage, amount, and close date

**What does NOT convert automatically:**
- Lead custom field values (must map via lead field mapping before conversion)
- Activities (converted separately via the activity timeline)

<!--
SPEAKER NOTES — SLIDE 5 (Domain 2 — Sales and Marketing, Part 1)
Sales and Marketing Apps is the joint highest-weight domain. The lead conversion model is the most tested concept.

The conversion flow is a one-way door: once a lead is converted, you cannot convert it again. The lead record is marked converted and is no longer visible in the standard leads list view. The data moves to the Contact, Account, and Opportunity objects.

Lead field mapping is the most frequently missed detail: if you have a custom field on the Lead object called "Campaign Source" and you want that value to appear on the converted Contact record, you must create a field mapping in the Lead Field Mapping setup page before conversion. If the mapping does not exist, the value is lost at conversion. This is a very testable detail.

The activities distinction: tasks and events on the lead record are not automatically reassigned to the new Contact/Account/Opportunity at conversion. They appear on the lead record, which is now marked converted. Admins who have done real conversions know this — but it surprises candidates who have only read about it.

Study exercise: in a developer org, create a lead with a custom field, convert it without field mapping, observe the loss, then add the field mapping and repeat. The hands-on experience will anchor the concept.
-->

---

<!-- _class: domain-slide -->

## Domain 2 — Sales and Marketing Apps (14%)

**Forecasting and territories — key distinctions:**

- **Collaborative Forecasting** — based on opportunity amounts and stage; managers see roll-ups
- **Territory Management** — assigns accounts and opportunities to reps by geography or criteria
- **Quota** — set on the user record; forecasting measures actual vs. quota

**Exam pattern:** questions test whether you know which feature solves which business need

<!--
SPEAKER NOTES — SLIDE 6 (Domain 2 — Sales and Marketing, Part 2)
Forecasting and territories are tested together in scenario questions. The scenario gives you a business requirement and asks which Salesforce feature addresses it.

Collaborative Forecasting scenario: "A VP of Sales wants to see the total expected revenue for their team, broken down by rep, for the current quarter, based on opportunity stage." Answer: Collaborative Forecasting. The VP sees a roll-up of all direct and indirect reports' opportunities, categorized by their forecast category.

Territory Management scenario: "A company has sales reps who cover accounts across multiple states. Each account should automatically be assigned to the correct rep based on the account's billing state." Answer: Enterprise Territory Management with territory rules. Rules can be based on account fields — billing state is the classic example.

Quota is frequently tested as a distractor. Quota does not affect which records a rep sees — it is only used for performance comparison in forecasting. A candidate who thinks territory assignment is quota-based will get these questions wrong.

The integration between features: Territory Management integrates with Collaborative Forecasting. If both are enabled, opportunities can contribute to both the user's personal forecast and the territory's forecast. This dual contribution is a common exam scenario.
-->

---

<!-- _class: practice -->

## Practice Questions — Domains 1 and 2

**Q1.** A user can edit an Account but not a specific field on it. What is the most likely cause?
*(A) OWD set to Private &nbsp; (B) Profile FLS set to Read-Only &nbsp; (C) Role hierarchy exclusion &nbsp; (D) Manual share missing)*

**Q2.** A lead is converted. The rep notices the custom field "Lead Source Detail" is blank on the new Contact. What is the fix?
*(A) Re-convert the lead &nbsp; (B) Add a lead field mapping &nbsp; (C) Update the Contact manually — no fix possible &nbsp; (D) Enable field history tracking)*

**Q3.** Which statement about permission sets is correct?
*(A) They can restrict profile access &nbsp; (B) They can grant additional access beyond the profile &nbsp; (C) They replace profiles &nbsp; (D) They control OWD)*

<!--
SPEAKER NOTES — SLIDE 7 (Practice Questions)
Answers: Q1-B, Q2-B, Q3-B.

Q1 explanation: OWD controls record-level access, not field-level access. Role hierarchy exclusion controls record visibility, not field editing. Manual share grants record-level access. Only field-level security (FLS) on the profile controls whether a user can edit a specific field on a record they can already access. Answer: B.

Q2 explanation: re-converting is not possible — leads can only be converted once. Updating the Contact manually loses the data for future reporting. Field history tracking captures changes, not missing conversions. The correct fix is to add a lead field mapping in setup before the next conversion. Answer: B. Note: for the already-converted lead, the data is lost — the mapping only helps future conversions.

Q3 explanation: permission sets can only grant additional access (extend the profile). They cannot restrict profile access — that would require changing the profile itself. They do not replace profiles — every user must have exactly one profile. They have no effect on OWD. Answer: B.

For cohort delivery: give participants 90 seconds to answer individually before discussing. Research on exam preparation shows that attempting retrieval before seeing the answer significantly improves long-term retention — even when the first attempt is wrong.
-->

---

## Tips — Exam Strategy

**Before you sit:**
- ● Spend 15 minutes in Salesforce Setup on the day before the exam — refresh your mental map
- ● Review your weakest domain one more time — not your strongest
- ● Sleep — memory consolidation happens during sleep, not during all-night review

**During the exam:**
- ● Flag questions you are unsure about and return at the end
- ● Eliminate obvious wrong answers first — get to a 50/50 and make a call
- ● If two answers look right, the one that uses official Salesforce terminology is almost always correct

*The exam tests documented behavior — not what your org does in practice*

<!--
SPEAKER NOTES — SLIDE 8 (Exam Tips)
The day-before Salesforce Setup tip is practical and evidence-based. Candidates who spend 15 minutes navigating Setup on exam eve report that the UI feels familiar during the exam — reducing cognitive load for scenario questions that ask "where would you configure this?"

The weakest domain tip runs counter to what most candidates do (review what they know best for confidence). Research on deliberate practice (Ericsson, 1993) consistently shows that time spent at the edge of competence produces more learning than time spent in the comfort zone. Review the domain you fear most.

Sleep: this sounds obvious but candidates in the final week routinely sacrifice sleep for study time. Memory consolidation research (Walker, Why We Sleep, 2017) is clear: a review session followed by 7–8 hours of sleep produces significantly better retention than the same content reviewed twice without sleep between sessions.

The flag-and-return strategy: the Webassessor platform allows flagging. Use it. Do not spend 5 minutes on a question you are unsure about — flag it, move on, and return with 15 minutes remaining.

Official terminology: if a question asks about "restricting field visibility" and one answer says "Field-Level Security" and another says "field permissions on the profile," choose the answer with the official Salesforce term. The exam is written by Salesforce — they use their own terminology.
-->

---

## Resources — Study Materials

**Trailhead (free, official):**
- Admin Beginner trail — 30 hours
- Prepare for Your Salesforce Administrator Credential — 8 hours
- Trailhead Superbadge: Process Automation Specialist

**Practice exams:**
- Focus on Force — paid, 700+ questions — focusonforce.com
- Salesforce Ben free practice exam — salesforceben.com
- ExamTopics community dumps — use with caution (verify against official guide)

**Reference:**
- Salesforce Administrator Exam Guide — trailhead.salesforce.com/credentials/administrator
- Salesforce Help documentation — help.salesforce.com

<!--
SPEAKER NOTES — SLIDE 9 (Resources)
The Trailhead resources are free and maintained by Salesforce — always current with the latest exam release. Start here. The Admin Beginner trail is not beginner-level material — it is the official conceptual foundation for the exam.

Focus on Force is the most highly recommended paid resource in the Salesforce certification community. The question bank is large and frequently updated to reflect exam changes. The explanations for wrong answers are as valuable as the correct answers.

ExamTopics caution: community-sourced dumps can contain outdated questions or incorrect answer explanations. They are useful for exposure to question patterns but should never be the primary study source. Cross-reference any answer from a community dump against the official Salesforce Help documentation.

The exam guide is the single most important document. Read it before you begin studying to understand the exact scope. Read it again at the midpoint of your study plan to verify you are covering the right material. Read it once more the week before the exam.

For SponAItech employees: Trailhead is connected to your Salesforce Trailblazer profile. Complete trails and superbadges and they appear on your public profile — visible to clients. This is a business development asset, not just a learning artifact.
-->

---

## Study Plan — 4 Weeks

| Week | Focus | Hours | Milestone |
|---|---|---|---|
| **1** | Org setup · User management · Security/Access | 12 | Trailhead Admin Beginner complete |
| **2** | Sales apps · Service apps · OWD deep dive | 12 | First practice exam attempt (target 50%) |
| **3** | Automation · Analytics · Data management | 10 | Second practice exam (target 60%) |
| **4** | Weak domain review · Full mock exam · Setup tour | 8 | Full mock at 70%+ → schedule exam |

*Total: ~42 hours · Schedule exam after Week 4 milestone*

<!--
SPEAKER NOTES — SLIDE 10 (Study Plan)
The 4-week plan assumes a candidate with 6+ months of Salesforce admin experience and 10–12 hours per week of study time. Adjust both axes if the learner's profile differs.

Week 1 milestone: Trailhead Admin Beginner complete. This is achievable in 12 hours if the learner moves at a moderate pace. Do not skip the hands-on challenges — they are exam practice in disguise.

First practice exam at 50% target: this is deliberately modest. The first attempt surfaces knowledge gaps, not knowledge mastery. A score below 50% is useful diagnostic data, not cause for alarm. A score above 65% on the first attempt suggests the learner may be ready earlier than 4 weeks.

Week 4 milestone gate: schedule the actual exam only after a full mock exam at 70% or above. The 5-point buffer above the passing score (65%) accounts for exam-day nerves and unfamiliar question phrasing. A candidate scoring 70% on a rigorous practice exam will typically score 65–68% on the actual exam.

For SponAItech: the company covers the $200 exam fee for the first attempt upon successful completion of the 4-week study plan. Retake fees are the employee's responsibility — a policy that aligns incentives toward adequate preparation.
-->

---

## Close — You Are Ready to Pass This

**Three things that separate passing candidates:**

1. They study the documented behavior — not just their org's behavior
2. They practice retrieval — quizzes, not re-reading
3. They schedule the exam before they feel ready

*A scheduled exam date makes everything else real.*

**Your next action:** complete the Week 1 Trailhead trail by [date] and send your completion badge to [manager/buddy].

<!--
SPEAKER NOTES — SLIDE 11 (Close)
The three differentiators are research-backed and practitioner-observed.

Documented behavior: Salesforce orgs diverge from documented behavior through years of customization, permission exceptions, and configuration debt. Candidates who have been admins for years are sometimes disadvantaged because their mental model reflects their org, not Salesforce's documentation. The exam tests the documentation.

Retrieval practice: re-reading notes and slides is the least effective study method for certification exams (Roediger & Karpicke, 2006). Retrieval practice — taking practice quizzes, explaining concepts aloud, writing from memory — is significantly more effective. Every study session should end with a retrieval exercise, not another round of reading.

Schedule the exam: this sounds like motivational talk but it is behavioral science. A scheduled exam date creates a commitment device — a concrete deadline that makes the abstract goal of "getting certified" into a specific, time-bound task. The registration fee is a small financial commitment that reinforces the behavioral commitment.

The named next action: replace [date] and [manager/buddy] before delivering. The action must be specific to be effective. "Complete Week 1 by Friday, April 25, and send your Trailhead completion email to your domain lead" is a real commitment. "Study more" is not.
-->

---

<!-- _class: lead -->

# Appendix — Exam Domain Reference

*Full domain weightings · Official exam guide link · Trailhead trail URLs*

*Facilitator guide and answer key: [shared drive path]*

<!--
SPEAKER NOTES — SLIDE 12 (Appendix header — reference only)
This appendix slide is a reference anchor. The full domain reference table, official links, and answer key for the practice questions in this deck should be stored in the facilitator guide at the linked location.

Do not present this slide in sequence — it is the last item in the deck and serves as a navigation aid for self-study learners who want to jump to a specific domain or resource.

For SponAItech internal use: the facilitator guide is stored in the SponAItech GitHub repo under `domains/salesforce-agentic-os/_templates/certification-prep/`. It includes: all practice question answer keys, domain weight breakdown by exam release, Trailhead trail completion timestamps for cohort tracking, and the mock exam scoring rubric.

If you are delivering this deck to an external client team, replace the shared drive link with the client's preferred document management system.
-->

---

## Appendix — All Six Domain Weights

| Domain | Weight | Priority |
|---|---|---|
| Security and Access | 14% | ◆ High |
| Sales and Marketing Apps | 14% | ◆ High |
| Service and Support Apps | 13% | ◆ High |
| Data Management | 10% | ● Medium |
| Analytics and Reporting | 10% | ● Medium |
| Workflow/Process Automation | 10% | ● Medium |
| Object Manager and Lightning App Builder | 8% | ○ Standard |
| Productivity and Collaboration | 7% | ○ Standard |
| User Management | 7% | ○ Standard |
| Organization Setup | 7% | ○ Standard |

*Total: 100% · Source: Salesforce Administrator Exam Guide, Spring 2025 release*

<!--
SPEAKER NOTES — SLIDE 13 (Domain Weight Reference)
This table is the study allocation reference. Share it as a printed card if delivering live.

The three high-priority domains (41% combined) should receive proportionally more study time. A candidate with 42 hours of total study time should allocate approximately 17 hours (41%) to Security, Sales, and Service.

Note on exam guide versions: Salesforce releases a new exam guide with each seasonal product release (Spring, Summer, Winter). The weights above reflect Spring 2025. Verify against the current guide before each use of this deck. If weights shift, update this table and the Week 1–4 study plan accordingly.

For the SponAItech certification program: this table is the input to the domain skill assessment that new Salesforce domain hires complete in their first week. The assessment identifies which domains each hire is weakest in, and the study plan is personalized based on the results.
-->

---

## Appendix — Practice Question Answer Key

| Question | Answer | Domain |
|---|---|---|
| Q1 — Field not editable despite record access | **B — Profile FLS** | Security and Access |
| Q2 — Custom field blank after lead conversion | **B — Add field mapping** | Sales and Marketing |
| Q3 — Permission sets vs. profiles | **B — Grant only, never restrict** | Security and Access |

*Additional practice questions: Focus on Force · Salesforce Ben · Trailhead Exam Prep module*

<!--
SPEAKER NOTES — SLIDE 14 (Answer Key)
This slide is the answer key for the three practice questions on Slide 7. It is formatted as an appendix so that self-study learners do not see the answers before attempting the questions.

For cohort delivery: do not show this slide until all participants have attempted the three questions independently. The retrieval attempt before seeing the answer is the learning event — showing the answer first eliminates most of the value.

The domain column helps learners identify which domain each question tests. If a learner misses Q1, they should spend additional time on Security and Access. If they miss Q2, Sales and Marketing Apps needs more attention.

Building a personal error log: encourage candidates to keep a running list of every practice question they get wrong, noting: the question topic, why they chose the wrong answer, and what the correct answer explains. This error log becomes the most targeted study resource in the final week — reviewing the log is more efficient than re-reading full domain modules.
-->
