<!-- TEMPLATE: training-module
     CATEGORY: Training / Self-Paced
     USE WHEN: delivering a self-paced or instructor-led training module on a single concept
     SLIDE COUNT: 12
     PALETTE: Light clean
     RENDER: marp --pptx 32-training-module.md -->
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
    margin-bottom: 0.25em;
  }
  h2 { color: #0e1b2e; font-size: 1.4em; font-weight: 600; margin-bottom: 0.5em; }
  h3 { color: #3b9eff; font-size: 1.05em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; }
  em { color: #556677; font-style: normal; font-size: 0.88em; }
  ul { margin-top: 0.5em; }
  li { margin-bottom: 0.45em; line-height: 1.6; }
  code { font-family: 'DM Mono', monospace; background: #f4f6f8; color: #0e1b2e; padding: 0.15em 0.4em; border-radius: 3px; font-size: 0.9em; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #8899ac; }
  section.lead h1 { font-size: 2.8em; }
  section.lead p { font-size: 1.1em; color: #556677; margin-top: 0.4em; }
  section.practice { background: #f0f7ff; border-left: 5px solid #3b9eff; }
  section.quiz { background: #f6fff9; border-left: 5px solid #2dd4a0; }
  .objective-list li::before { content: "→ "; color: #3b9eff; font-weight: 600; }
  .answer-reveal { background: #e8f4ff; border: 1px solid #3b9eff; border-radius: 4px; padding: 0.6em 1em; margin-top: 0.8em; font-size: 0.9em; }
---

<!-- _class: lead -->

# AI-Assisted Claims Triage — Module 3

**Meridian Health** &nbsp;|&nbsp; Clinical Operations Training

*Self-Paced Module · v1.2 · April 2025 · Est. 45 min*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
This is a self-paced module. The learner will advance through slides at their own pace. If you are delivering this in a live session, introduce yourself and give a 60-second orientation: this module covers AI-assisted claims triage from the perspective of the claims examiner, not the AI engineer. No technical background is required.

Estimated completion time is 45 minutes for a self-paced learner reading at a moderate pace, completing the practice questions, and reviewing the resources list. In a live session with discussion, budget 60–75 minutes.

This is Module 3 in the series. Modules 1 and 2 (Claims Fundamentals and Intake Form Standards) are prerequisites. If learners have not completed those modules, direct them there first. The concepts in this module assume familiarity with Meridian's claims workflow and standard intake fields.

Learning objectives appear on the next slide. By the end of this module, learners will be able to apply the triage decision criteria in their daily review queue.
-->

---

## Learning Objectives

By the end of this module, you will be able to:

- ● Describe how the AI triage engine classifies incoming claims
- ● Apply the three-tier review queue to your daily workflow
- ● Identify the five claim flags that require human escalation
- ● Evaluate an AI triage decision for accuracy and override when needed

*Prerequisites: Module 1 (Claims Fundamentals) · Module 2 (Intake Form Standards)*

<!--
SPEAKER NOTES — SLIDE 2 (Learning Objectives)
Read the objectives aloud if delivering live. For self-paced, these objectives serve as a learning contract — the learner should be able to do all four things by the end of the module.

Each objective maps to a specific section of the module: Objective 1 → Concept 1 slides; Objective 2 → Concept 2 slides; Objective 3 → both Concept slides; Objective 4 → the Application slide and Quiz.

If a learner is short on time and can only read part of the module, the priority order is: Objectives 4, 3, 2, 1. The override skill (Objective 4) is the most operationally critical.

Assessment: the Quiz slide (Slide 11) covers all four objectives. A learner who passes the quiz with 3 out of 4 correct is considered proficient for this module. A score of 2 or lower requires a conversation with their supervisor before they are cleared to process the AI triage queue independently.
-->

---

## Concept 1 — How the AI Triage Engine Works

The AI triage engine reads four fields from the intake form:

- **Claim type** — inpatient, outpatient, pharmacy, durable medical equipment
- **Diagnosis code** — ICD-10 primary + secondary
- **Provider NPI** — verified against the Meridian credentialing database
- **Amount requested** — compared against historical benchmark for the code

It assigns one of three classifications: **Auto-Approve** · **Review** · **Escalate**

<!--
SPEAKER NOTES — SLIDE 3 (Concept 1)
This slide gives learners a mental model of what the AI is actually doing — not the engineering details, but the decision logic from a user's perspective. It is important that learners understand the AI is not reading the full clinical narrative. It reads exactly these four fields.

Common misconception to address: some learners believe the AI reads the clinical notes and reasons about them the way a senior examiner would. It does not. It classifies based on structured fields. This means: if the intake form is incomplete, the classification will be wrong. Module 2 (Intake Form Standards) is the upstream fix for this.

The three classifications map directly to the three-tier queue covered in Concept 2. Do not jump ahead — let this slide settle first.

If delivering live, ask: "Has anyone seen a claim get Auto-Approved that they thought should have been escalated?" Take one or two responses. This grounds the concept in the learner's real experience before you explain why it can happen.
-->

---

## Concept 1 — Classification Logic

| Classification | Criteria | Examiner Action |
|---|---|---|
| **Auto-Approve** | Clean code match · NPI verified · Amount ≤ benchmark | Queue cleared automatically |
| **Review** | Minor code mismatch or amount 1–1.5× benchmark | Examiner reviews within 2 business days |
| **Escalate** | NPI unverified · Amount > 1.5× benchmark · Any flag | Senior examiner within 4 hours |

*Auto-Approve does not mean no review — it means no manual action required today*

<!--
SPEAKER NOTES — SLIDE 4 (Concept 1 continued — Classification Table)
The table is the operational heart of this module. Learners will refer back to this in their daily work. Encourage them to screenshot it or print the module PDF.

Clarify the Auto-Approve footnote carefully. "No manual action required today" does not mean these claims are never reviewed. Monthly audits sample 5% of Auto-Approved claims against the original clinical records. The audit is what catches systematic drift in the AI's classification accuracy. If you hear a colleague say "the AI approved it, so it's fine," that is a red flag — report it to your supervisor.

The Escalate row: the 4-hour SLA is binding. If a senior examiner is not available within 4 hours, the claim routes to the on-call escalation queue. The on-call contact list is in the Meridian Claims SharePoint under Escalation Resources.

Practice question follows on the next slide.
-->

---

<!-- _class: practice -->

## Practice Question 1

A claim arrives with:
- Claim type: outpatient
- Diagnosis code: Z00.00 (routine exam) — verified
- Provider NPI: not found in credentialing database
- Amount: $280 — benchmark $310

**How does the AI classify this claim?**

A) Auto-Approve &nbsp;&nbsp; B) Review &nbsp;&nbsp; **C) Escalate** &nbsp;&nbsp; D) Reject

<!--
SPEAKER NOTES — SLIDE 5 (Practice Question 1)
Answer: C — Escalate. The NPI is unverified, which is an automatic Escalate trigger regardless of the other field values.

Give learners 30 seconds to answer before revealing. If delivering live, ask for a show of hands before explaining.

Common wrong answer: B (Review), because the amount is below benchmark and the code is clean. Learners who answer B have over-indexed on the amount field and missed the NPI check. Use this to reinforce: the classification is based on the most serious flag, not an average of all fields. One Escalate trigger = Escalate.

If a learner answers D (Reject): the AI triage engine does not reject claims — that decision requires human authorization. Rejections are a G5 Review gate output, not an AI output. Clarify this distinction.

After explaining the answer, transition: "Now let's look at what happens once a claim reaches your review queue."
-->

---

## Concept 2 — The Three-Tier Review Queue

Your daily queue displays three lanes:

- **Auto-Approve lane** — monitoring only; no action required
- **Review lane** — claims awaiting your 2-business-day evaluation
- **Escalate lane** — claims requiring senior examiner; do not hold

**Your daily habit:** clear the Escalate lane before 10:00 AM · process the Review lane by EOD

<!--
SPEAKER NOTES — SLIDE 6 (Concept 2)
The daily habit instruction is operationally critical. The 10:00 AM Escalate clearing is a team SLA — not a personal preference. If an escalated claim sits in your queue past 10:00 AM without action, the SLA dashboard flags it and your supervisor receives an alert.

The Review lane 2-business-day SLA starts from when the claim enters your queue — not from when it was submitted. If a claim entered your queue Monday at 3 PM, it is due by Wednesday at 3 PM.

The Auto-Approve lane monitoring: once a week, spend 10 minutes scanning the Auto-Approve lane for any pattern that looks unusual. You are not reviewing individual claims — you are doing a visual scan. If a specific provider's claims are all Auto-Approving at the top of the benchmark, that is worth flagging. Your judgment is the long feedback loop that the AI cannot provide.

Ask learners: "If you come in on Wednesday and see 14 items in your Escalate lane from the last two days, what does that tell you?" Answer: the SLA was missed. This is a system or staffing issue to escalate — do not silently work through the backlog as if nothing happened.
-->

---

## Concept 2 — The Five Escalation Flags

A claim must be manually escalated when any flag is present:

1. **NPI not in credentialing database** — provider verification required
2. **ICD-10 code mismatch** — diagnosis does not match procedure code
3. **Amount exceeds 1.5× benchmark** — high-dollar review required
4. **Duplicate claim indicator** — same patient, same date, same code within 30 days
5. **Patient complaint on file** — any open complaint linked to this claim

*You may see claims in your Review lane that develop a flag mid-review — escalate immediately*

<!--
SPEAKER NOTES — SLIDE 7 (Concept 2 continued — Five Flags)
These five flags are exhaustive — if a claim does not have any of these, it is eligible for the Review lane. If it has one or more, it belongs in the Escalate lane.

Flag 4 (duplicate) is the one most often missed by new examiners because the AI catches most duplicates automatically, but not all. The AI checks the current claim against the last 30 days of history. If a claim is a re-submission from 45 days ago, the AI may not flag it. Human review catches this when you notice the patient name and procedure code look familiar.

Flag 5 (patient complaint) is in the claims system under the patient record — check it before completing any Review lane claim. It takes 10 seconds. Missing an open complaint and approving a disputed claim creates a compliance risk.

Encourage learners to print or save this list. It is the single most actionable reference in this module.
-->

---

## Application — Override Decision Framework

When you disagree with an AI classification:

**Step 1:** Verify you have reviewed all five escalation flags against the claim  
**Step 2:** If your conclusion differs from the AI, document your reasoning in the notes field  
**Step 3:** Apply your classification — your judgment takes precedence  
**Step 4:** If overriding an Auto-Approve to Escalate, notify your supervisor same day

*Override rate target: 3–7% of Review lane claims. Higher signals AI drift; lower signals under-review.*

<!--
SPEAKER NOTES — SLIDE 8 (Application)
This slide is the most important for building examiner confidence. Many new examiners are reluctant to override the AI because they assume the AI is right and they are wrong. Correct this directly: the AI is a first-pass classifier. You are the decision-maker.

The override rate target is a health metric for the team, not a performance target for individuals. If the team's override rate goes to 15%, that is a signal that the AI model has drifted and needs retraining — report it to the AI Operations team (contact in the Resources slide). If the team's override rate is 0.5%, that is a signal that examiners are rubber-stamping AI decisions — a quality and compliance risk.

The same-day supervisor notification for Auto-Approve overrides: this is not punitive. It creates a feedback loop so the AI team can investigate whether the claim represents a new pattern they should add to the training data.

Step 2 (documenting reasoning) is auditable. In the monthly compliance audit, 100% of overrides are reviewed. Clear documentation protects you. "Looked wrong to me" is not sufficient — "ICD-10 code Z00.00 does not match outpatient surgery procedure — possible coding error" is.
-->

---

## Recap — Module 3 Summary

**What you learned:**

- ✓ AI classifies on four fields: claim type, ICD-10, NPI, amount
- ✓ Three classifications: Auto-Approve · Review · Escalate
- ✓ Five flags that always require escalation
- ✓ Your judgment overrides the AI — document your reasoning

**Your daily habit:**
- Clear Escalate lane by 10:00 AM
- Process Review lane by EOD
- Override when your assessment differs — always document

<!--
SPEAKER NOTES — SLIDE 9 (Recap)
Read through the recap at a measured pace. This is a memory-consolidation slide — the learner is hearing the key points for the second time, which improves retention.

For self-paced learners: invite them to pause the module and write down the three things they want to remember most before moving to the quiz. Research on learning transfer (Roediger & Karpicke, 2006) shows that retrieval practice — even brief — significantly outperforms re-reading for retention.

For live delivery: ask the group to close their slides for 60 seconds and write down everything they remember from the module. Then have them check their notes against the recap. This is a simple retrieval exercise that doubles as an engagement technique.

Transition to the quiz: "Let's see how well this is landing before you leave the module."
-->

---

<!-- _class: quiz -->

## Quiz — Module 3

**1.** Which field alone can trigger an Escalate classification?  
*(A) Amount at benchmark &nbsp; (B) Unverified NPI &nbsp; (C) Outpatient claim type &nbsp; (D) Primary ICD-10 match)*

**2.** Your override rate this month is 12%. What does this most likely signal?  
*(A) You are a thorough examiner &nbsp; (B) AI model drift &nbsp; (C) Understaffing &nbsp; (D) Normal variance)*

**3.** A Review lane claim develops Flag 4 (duplicate) mid-review. What do you do?  
*(A) Complete Review lane processing &nbsp; (B) Escalate immediately &nbsp; (C) Auto-Approve &nbsp; (D) Close without action)*

**4.** What is the Escalate lane SLA?  
*(A) Same day &nbsp; (B) 4 hours &nbsp; (C) 2 business days &nbsp; (D) End of week)*

<!--
SPEAKER NOTES — SLIDE 10 (Quiz)
Answers: 1-B, 2-B, 3-B, 4-B.

Scoring: 4/4 = Proficient; 3/4 = Review the missed concept and retest; 2/4 or below = Required supervisor review before independent queue processing.

Question 1 answer explanation: Unverified NPI is an automatic Escalate trigger regardless of all other fields. This was covered on the Classification Logic slide.

Question 2 answer explanation: 12% override rate is above the 3–7% target band. This is not a reflection of the examiner's thoroughness — it means the AI is mis-classifying at a rate that warrants model review.

Question 3 answer explanation: "Escalate immediately" means the moment you discover the flag, you move the claim to the Escalate lane. You do not finish your Review analysis first.

Question 4 answer explanation: 4 hours from when the claim enters the Escalate lane, not from when it was submitted. This was covered in the Concept 2 slides.

For self-paced learners: answers are in the module facilitator guide linked on the Resources slide. Do not put answers on this slide — the quiz is a retrieval exercise.
-->

---

## Resources — Module 3

**References:**
- Meridian Claims Processing Policy v4.2 — [SharePoint: Claims Operations]
- AI Triage Engine Technical Overview — [SharePoint: AI Operations]
- Escalation Contact List — [SharePoint: Claims Escalation Resources]
- ICD-10 Code Lookup — [cms.gov/medicare/coding-billing/icd-10-codes]

**Support:**
- Questions about this module → your direct supervisor
- AI triage errors or unexpected behavior → AI Operations team
- Policy questions → Claims Operations inbox

*Module series: 1 Claims Fundamentals · 2 Intake Form Standards · **3 AI Triage** · 4 Appeals Process*

<!--
SPEAKER NOTES — SLIDE 11 (Resources)
This slide is a permanent reference. Learners should bookmark or save it. All SharePoint links should be verified before the module is published — broken links undermine trust in the training materials.

The module series map at the bottom gives learners a sense of where they are in the full training path. Module 4 (Appeals Process) follows this module and is a prerequisite for independent queue processing on complex cases.

The AI Operations contact is important. Most examiners have never contacted this team and do not know the channel exists. Name them specifically in live delivery: "This is the Meridian AI Operations team — they are not engineers in the abstract. They are Priya, Marcus, and Dani. You can reach them at [contact]." Humanizing the feedback channel increases the likelihood that examiners report AI errors.

If this is self-paced: learners should complete the quiz before accessing the Resources slide. In a live session, distribute the resources list as a printed reference card.
-->

---

<!-- _class: lead -->

## Next Module — Module 4 — Appeals Process

**What you will learn:**
- How to initiate a formal appeal on a denied claim
- The documentation standard for appeals packets
- SLAs and escalation paths for contested decisions

*Available in: Meridian Health Learning Management System — Claims Track*

<!--
SPEAKER NOTES — SLIDE 12 (Next Module)
End on a forward-looking slide, not a generic "thank you." The next module prompt creates continuity and motivation to complete the training series.

For self-paced learners: the transition to the LMS should be a direct link if technically possible. Every extra click reduces completion rates.

For live delivery: confirm the next session date and tell learners exactly what to bring — "In Module 4, you will need two real claims from your queue that were denied in the last 30 days. Bring them anonymized. We will use them as case studies."

Module completion tracking: this slide's appearance in the LMS marks the module as complete. If delivering in person, have learners sign the attendance log before leaving. Attendance is required for certification credit under Meridian's annual training compliance requirements.
-->
