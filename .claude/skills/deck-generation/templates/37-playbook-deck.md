<!-- TEMPLATE: playbook-deck
     CATEGORY: Training / Operations
     USE WHEN: walking a team through an operational playbook or runbook
     SLIDE COUNT: 11
     PALETTE: Corporate (cream, navy, gold)
     RENDER: marp --pptx 37-playbook-deck.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&family=DM+Serif+Display&family=DM+Mono&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #f7f4ef;
    color: #1c1a18;
    padding: 52px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', serif;
    color: #0e1b2e;
    font-size: 2.1em;
    letter-spacing: -0.4px;
    margin-bottom: 0.2em;
  }
  h2 { color: #0e1b2e; font-size: 1.35em; font-weight: 600; margin-bottom: 0.5em; }
  h3 { color: #b8965a; font-size: 1.0em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.87em; }
  ul { margin-top: 0.4em; }
  li { margin-bottom: 0.4em; line-height: 1.6; }
  code { font-family: 'DM Mono', monospace; background: #ede8df; color: #0e1b2e; padding: 0.15em 0.45em; border-radius: 3px; font-size: 0.88em; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #6b6560; }
  section.lead h1 { font-size: 2.7em; }
  section.lead p { font-size: 1.1em; color: #6b6560; margin-top: 0.4em; }
  section.step1 { border-left: 6px solid #b8965a; }
  section.step2 { border-left: 6px solid #8a6f3e; }
  section.escalation { background: #fff8ed; border-left: 6px solid #f0a050; }
  section.post-action { background: #f7f4ef; border-top: 4px solid #0e1b2e; }
  .step-number {
    font-family: 'DM Serif Display', serif;
    font-size: 3em;
    color: #b8965a;
    line-height: 1;
    margin-bottom: 0.1em;
  }
  .role-badge {
    display: inline-block;
    background: #0e1b2e;
    color: #f7f4ef;
    font-family: 'DM Mono', monospace;
    font-size: 0.78em;
    padding: 0.2em 0.6em;
    border-radius: 3px;
    margin-right: 0.4em;
  }
  .trigger-box { background: #ffffff; border: 1.5px solid #b8965a; border-radius: 6px; padding: 0.8em 1.2em; margin-top: 0.7em; }
---

<!-- _class: lead -->

# Production Incident Playbook

**SponAItech Operations** &nbsp;|&nbsp; Severity 1 Response

*v2.1 · Effective April 2025 · Reviewed quarterly*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
This playbook governs the SponAItech response to Severity 1 production incidents — events where a client-facing system is fully unavailable, data integrity is compromised, or a critical security breach is detected. The playbook is delivered as a deck so it can be used both as a training tool and as a live reference during an incident.

Who should know this playbook: everyone who deploys to production or who is on call. For a lean operation like SponAItech, that means every technical team member.

Delivery context: review this playbook annually as a team and whenever a new team member joins who has production access. During an actual incident, the playbook is used in real-time — slides are not advanced linearly; the responder jumps to the relevant step.

Version history: the playbook was last updated in April 2025 following a post-incident review of a Meridian Health claims API outage. The key changes from v2.0 to v2.1 are: added the 15-minute escalation trigger (Slide 8), clarified the communication cadence for clients (Slide 7 notes), and added the post-action review SLA of 48 hours (Slide 10).
-->

---

## Scenario — What This Playbook Covers

**Severity 1 — Critical:**
- Client-facing system fully unavailable (API down, UI inaccessible)
- Data integrity breach or unauthorized data access
- Service degradation affecting more than 20% of users for more than 15 minutes

**Severity 2 and below** → use the standard incident process (link in resources)

<div class="trigger-box">
<strong>Playbook activates</strong> when the on-call engineer confirms Severity 1 criteria are met — not when the alert fires.
</div>

<!--
SPEAKER NOTES — SLIDE 2 (Scenario)
The severity classification is the most important decision at the start of an incident. The temptation is to escalate everything to Severity 1 — this creates alarm fatigue and over-mobilizes the team for minor issues. The temptation is also to under-classify to avoid disruption — this delays response to real crises.

The criteria are deliberately specific. "Fully unavailable" means zero successful requests — not slow, not intermittent. "Affecting more than 20% of users for more than 15 minutes" is measurable from the observability dashboard.

The trigger box note is critical: the playbook activates on human confirmation, not on alert. Automated alerts fire frequently — on-call engineers learn to filter noise. The Severity 1 classification requires a human judgment call based on evidence, not just an alert firing.

If there is doubt about whether an event meets Severity 1 criteria: err on the side of activation. It is cheaper to stand down a mobilized team after 10 minutes than to delay response on a real Severity 1 by 30 minutes while trying to classify it precisely.

For the Meridian Health engagement specifically: Severity 1 for the claims API is defined as any period where claims cannot be processed for more than 10 minutes during business hours (7 AM – 7 PM PST). This is more restrictive than the general SponAItech definition.
-->

---

## Roles — Who Does What

<span class="role-badge">INCIDENT COMMANDER</span> — owns the response; all decisions route through them

<span class="role-badge">TECH LEAD</span> — drives the technical investigation and resolution

<span class="role-badge">CLIENT COMMS</span> — manages client communication; no technical detail without IC approval

<span class="role-badge">SCRIBE</span> — logs all decisions, timestamps, and actions in the incident log

**In a lean team:** Incident Commander and Client Comms may be the same person. Tech Lead and Scribe may be the same person. Never combine Incident Commander and Tech Lead — split focus creates missed decisions.

<!--
SPEAKER NOTES — SLIDE 3 (Roles)
The role structure is designed for a team of two to four people, which is the SponAItech operating model. The critical constraint is the last line: never combine Incident Commander and Tech Lead.

Why: the Tech Lead is in a problem-solving mode — heads down in logs, code, and dashboards. The Incident Commander is in a coordination mode — tracking time, managing communication, making calls about rollback vs. patch. These two modes are cognitively incompatible. When one person tries to do both, they either miss a critical log entry or fail to communicate a client update on time.

The scribe role is often the first to be skipped in small teams because it "feels" low priority during a crisis. This is wrong. The incident log is the primary input to the post-action review and the evidence for any client SLA discussion. Without it, the team will spend hours reconstructing what happened and when.

For remote teams: the incident channel (Slack or Teams) effectively serves as the scribe log if everyone posts decisions and timestamps there. Assign one person to consolidate the channel thread into the formal incident log within 24 hours.

On-call rotation: SponAItech uses a manual on-call schedule managed in the Shared calendar. The Incident Commander role defaults to the on-call engineer unless explicitly reassigned.
-->

---

<!-- _class: step1 -->

## Step 1 — Detect and Triage

<div class="step-number">01</div>

**Detect:** Alert fires or client reports an issue

**Triage (within 5 minutes of detection):**

- ● Confirm the system is actually down (not just the alert)
- ● Check the observability dashboard for error rate and affected services
- ● Classify: Severity 1 / 2 / 3 — activate this playbook only if Severity 1
- ● Open the incident channel: `#incident-YYYY-MM-DD-[brief-description]`

*Do not page anyone until Severity 1 is confirmed*

<!--
SPEAKER NOTES — SLIDE 4 (Step 1 — Detect and Triage)
The 5-minute triage window is aggressive and intentional. A 5-minute window forces the on-call engineer to make a classification decision quickly rather than spending 20 minutes investigating before telling anyone.

Confirming the system is actually down: check the health endpoint directly (`GET /health`) rather than relying on the alert tool. Alert tools have false positive rates. A 200 response from the health endpoint when the alert is firing means the monitoring threshold is wrong, not that the system is down.

Observability dashboard: the SponAItech standard is Azure Monitor + Application Insights. Error rate above 50% for more than 3 minutes on the primary API surface is the automated Severity 1 trigger.

The incident channel naming convention: `#incident-YYYY-MM-DD-[brief-description]` creates a searchable archive. Example: `#incident-2025-04-15-claims-api-timeout`. Brief description should be the symptom, not the cause — you do not know the cause yet.

"Do not page anyone until Severity 1 is confirmed": this prevents alert fatigue. The on-call engineer's first job is to confirm the severity before mobilizing the team. A false alarm that pages three people at 2 AM erodes trust in the alert system.
-->

---

<!-- _class: step1 -->

## Step 1 — Notify and Mobilize

<div class="step-number">01b</div>

**Notify (within 10 minutes of Severity 1 confirmation):**

- ● Page the Incident Commander (if not already the on-call engineer)
- ● Page the Tech Lead for the affected system
- ● Post initial client update: *"We are aware of an issue with [system]. Our team is investigating. Next update in 30 minutes."*

**Do not post:** cause, estimated fix time, or blame in the initial client update

*The first client communication buys you 30 minutes — use them*

<!--
SPEAKER NOTES — SLIDE 5 (Step 1b — Notify and Mobilize)
The 10-minute notification window runs concurrently with the triage phase. The on-call engineer starts triage and simultaneously pages the IC and Tech Lead — do not wait for triage to complete before paging.

The initial client update template is deliberately minimal. Clients need to know three things at the start of an incident: you are aware, you are working on it, and you will update them. They do not need cause, timeline, or technical detail at this stage — that information will be wrong at the start of the incident and will create confusion.

"Next update in 30 minutes" is a commitment. Set a timer. Do not let the 30 minutes pass without an update, even if the update is "we are still investigating, next update in 30 minutes." Silence is the worst client communication — it creates the impression that no one is working on the problem.

The "do not post cause or estimated fix time" instruction: cause is unknown at this stage. Estimated fix times given in the first 10 minutes of an incident are wrong more than 90% of the time and will be held against you. Better to say "we do not have an ETA yet" than to miss an ETA you committed to.

For Meridian Health: the client contact for incident notifications is the Meridian IT Operations team, not the business stakeholders. The SLAs in the Meridian contract specify a 15-minute notification SLA from detection to client contact.
-->

---

<!-- _class: step2 -->

## Step 2 — Investigate and Contain

<div class="step-number">02</div>

**Investigate:** Tech Lead leads; Scribe logs every action and timestamp

- ● Check recent deployments in the last 4 hours — most Severity 1s are deployment-related
- ● Review error logs for the first occurrence of the error pattern
- ● Check downstream dependencies: database, external APIs, cloud services

**Contain (as soon as cause is identified):**

- ● If deployment-related: initiate rollback immediately — do not attempt a patch first
- ● If data issue: isolate affected records; do not attempt cleanup under incident conditions
- ● If security breach: disconnect affected services; engage security protocol

<!--
SPEAKER NOTES — SLIDE 6 (Step 2 — Investigate and Contain)
The "check recent deployments first" heuristic is based on empirical observation: the majority of Severity 1 incidents in software systems are caused by changes made in the preceding 4 hours. This is not a guess — it is the Accelerate research finding (Forsgren, Humble, Kim, 2018) confirmed across thousands of teams. Check deployments first.

Error log investigation: look for the first occurrence of the new error pattern, not the most recent. The first occurrence tells you when the problem started — which narrows the deployment window. Compare first occurrence timestamp against the deployment log.

The rollback vs. patch decision is the most consequential call in an incident. The guidance is clear: if the cause is a deployment, roll back first. Do not attempt to patch under incident conditions. Patches introduce new code changes in a high-pressure environment with reduced testing — the failure rate is high. A rollback restores the last known good state. Patch after the incident, during normal conditions, with full testing.

The data issue protocol: containment means not making the problem worse. Under incident conditions, a cleanup script run incorrectly can corrupt more records than the original issue. Isolate, do not clean. The cleanup happens post-incident with full attention and proper testing.

The security breach protocol is a hard stop: disconnect first, investigate second. Every minute a compromised service remains connected is a minute of additional exposure.
-->

---

<!-- _class: step2 -->

## Step 2 — Resolve and Communicate

<div class="step-number">02b</div>

**30-minute client update cadence (until resolved):**

Template: *"Update [HH:MM]: We have identified [brief description of cause]. We are [action in progress]. We expect to have an update on resolution by [time]."*

**Resolve:**
- ● Rollback or patch is deployed and verified (health check returns 200)
- ● Error rate returns to baseline for 10 consecutive minutes
- ● Affected data verified intact or remediation plan confirmed

**Declare resolved:** Incident Commander calls "all clear" — not Tech Lead

<!--
SPEAKER NOTES — SLIDE 7 (Step 2b — Resolve and Communicate)
The 30-minute update cadence is non-negotiable. Set a recurring 30-minute timer when the incident starts. The Client Comms role owns sending the update — the Tech Lead should not be pulled away from investigation to write communications.

The update template includes a cause description because clients deserve to know what happened, not just that something happened. Keep it brief and non-technical: "We identified a configuration error in the API gateway" not "The nginx proxy timeout was set to 30 seconds instead of 90 seconds due to a missed environment variable in the deployment manifest."

Resolution criteria: the 10-minute baseline window prevents premature all-clear declarations. Error rates sometimes spike, drop, then spike again during resolution. A 10-minute clean window provides confidence that the fix is holding.

The Incident Commander declares resolution — not the Tech Lead. This separation exists because the Tech Lead's perspective is technical (the fix is deployed) while the Incident Commander's perspective is operational (the client is informed, the system is verified, the incident log is current). The all-clear requires both.

Post-resolution client communication: the all-clear message should include: confirmation that the system is restored, a brief plain-language description of what happened, and the promise of a post-incident report within 48 hours. Do not include the post-incident report in the all-clear — it takes time to write well.
-->

---

<!-- _class: escalation -->

## Escalation — When to Call for Help

**Escalate within 15 minutes of Severity 1 confirmation if:**

- ● The Tech Lead cannot identify the root cause
- ● The rollback fails or makes the situation worse
- ● A data breach is confirmed or suspected
- ● The incident affects a regulated system (HIPAA-covered data at Meridian)

**Who to call:**
- Platform / cloud issues → Azure Support (Priority support, case number in runbook)
- Security breach → [Security contact name and number]
- Client relationship at risk → Founder / Principal Consultant immediately

*Escalating is not failing — waiting too long to escalate is*

<!--
SPEAKER NOTES — SLIDE 8 (Escalation)
The 15-minute escalation trigger was the key change in v2.1. The previous version had a 30-minute trigger — post-incident review showed that every time escalation was delayed beyond 15 minutes, resolution time increased by at least an hour. The 15-minute gate forces the team to escalate before they are certain they need to, which is the right threshold.

"Escalating is not failing" is a cultural statement that must be made explicitly because the default human instinct is to avoid asking for help. In high-stakes environments, the ability to escalate quickly and clearly is a sign of professional maturity, not weakness.

The HIPAA note for Meridian: any incident involving the Meridian claims system that involves potential unauthorized access to patient data must be escalated immediately to the founder AND the Meridian compliance team. The HIPAA breach notification clock starts from when a breach is "discovered" — which in a legal context means when SponAItech had reason to believe a breach occurred. Delayed escalation creates legal liability.

Azure Support: the current SponAItech Azure support tier and the process for opening a P1 support case should be in the incident runbook linked in the Resources slide. Do not rely on team members knowing this from memory — it changes and needs to be documented.
-->

---

<!-- _class: post-action -->

## Post-Action Review — Within 48 Hours

**Mandatory within 48 hours of incident close:**

- ● Timeline reconstruction (Scribe's log → formal timeline)
- ● Root cause analysis (5-Whys or fishbone — no blame, only causes)
- ● Impact assessment: duration, users affected, client SLA status
- ● Action items: preventive controls, monitoring improvements, playbook updates

**Who attends:** everyone who was active in the incident response

**Output:** post-incident report shared with the client and stored in the incident archive

<!--
SPEAKER NOTES — SLIDE 9 (Post-Action Review)
The 48-hour window is firm. Beyond 48 hours, memory degrades, context switches to new work, and the urgency to improve dissipates. The post-action review is where the team gets the most value from the incident — use it.

The no-blame norm is the most important cultural element of the post-action review. Root cause analysis is about systems and processes, not people. If the analysis surfaces "engineer X made a mistake," the root cause is not the mistake — it is the process that allowed the mistake to reach production without detection. What was the test gap? What was the review gap? What was the deployment verification gap?

The 5-Whys technique: ask "why did this happen?" five times, each time answering the previous question. Example: Why was the API down? → Because the database connection pool was exhausted. Why was the pool exhausted? → Because connection limits were not set in the deployment config. Why were limits not set? → Because the deployment config template did not include the connection limit parameter. Why was it not in the template? → Because connection limits were added to the infra spec after the template was written. Why was the template not updated? → Because there was no process to update templates when the spec changes. Root cause: no spec-to-template update process.

The client post-incident report: write it clearly and honestly. Clients who receive a transparent, well-written post-incident report from a vendor trust that vendor more after the incident than before. Clients who receive silence or vague explanations lose confidence.
-->

---

## Resources — Playbook Reference

**Runbook and contact list:**
- Full runbook with system architecture: `[internal wiki / runbook link]`
- On-call schedule and rotation: `[shared calendar link]`
- Azure Support case creation: `portal.azure.com` → Help + Support → Create support request

**Incident log template:**
- `memory/projects/[domain]/[project]/incidents/YYYY-MM-DD-description.md`

**Related playbooks:**
- Severity 2 — Degradation Response Playbook
- Security Breach Response Playbook
- Data Recovery Playbook

*Playbook owner: [name] · Last reviewed: April 2025 · Next review: July 2025*

<!--
SPEAKER NOTES — SLIDE 10 (Resources)
The resources slide is the permanent reference for items that change over time — contact lists, runbook links, schedule links. These must be updated every time the playbook is reviewed.

The incident log path convention: every incident gets its own Markdown file in the project's memory directory. The filename is the date and a brief description. Example: `2025-04-15-claims-api-timeout.md`. The file contains the full timeline from the Scribe's log, all communications sent, the root cause, and action items.

The related playbooks section acknowledges that this playbook is one in a set. A real operations team needs playbooks for the full spectrum of incident types. The Severity 2 playbook follows the same structure but with relaxed time thresholds. The Security Breach and Data Recovery playbooks have their own escalation trees and specialized steps.

Playbook owner accountability: the named owner is responsible for: scheduling quarterly reviews, incorporating post-incident learnings, keeping contact information current, and communicating updates to the team. An unmaintained playbook is worse than no playbook — it gives responders false confidence in stale information.
-->

---

<!-- _class: lead -->

# Appendix — Quick Reference Card

*Print and post at workstation for on-call engineers*

**Severity 1 Checklist:**

- [ ] Confirm Severity 1 criteria met
- [ ] Open incident channel `#incident-YYYY-MM-DD`
- [ ] Page IC and Tech Lead within 10 min
- [ ] Send initial client update within 10 min
- [ ] 30-min client update cadence
- [ ] Escalate at 15 min if no root cause
- [ ] IC declares all clear
- [ ] Post-action review within 48 hours

<!--
SPEAKER NOTES — SLIDE 11 (Appendix — Quick Reference)
This appendix is designed to be printed as a half-page reference card and posted at the on-call engineer's workstation. During an actual Severity 1 incident, the last thing a responder should have to do is navigate a 11-slide deck to find the checklist.

The checklist format is deliberate: checkboxes instead of bullets. During an incident, the responder physically checks each box. This prevents the "we did everything right" post-incident claim when critical steps were skipped.

For remote teams: the quick reference card can be pinned in the incident channel as a message at the start of every incident. The Scribe's first action when the channel opens is to paste this checklist and check items off as they are completed.

The checkboxes should be evaluated at the post-action review: which items were completed on time? Which were delayed? Which were skipped? The checklist is both a real-time tool and a retrospective audit log.

Production of this card: export this slide as a PNG at 300 DPI, print at 50% size on card stock, laminate if possible. Low-tech but durable. Every on-call engineer should have one at their desk and one near their home workstation.
-->
