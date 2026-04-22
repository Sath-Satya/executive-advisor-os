<!-- TEMPLATE: knowledge-transfer
     CATEGORY: Training / Knowledge Transfer
     USE WHEN: a team member is departing or transitioning and needs to hand off domain knowledge
     SLIDE COUNT: 12
     PALETTE: Corporate hybrid (cream bg, navy headings, electric blue for current/open states)
     RENDER: marp --pptx 38-knowledge-transfer.md -->
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
  h3 { color: #3b9eff; font-size: 1.0em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.87em; }
  ul { margin-top: 0.4em; }
  li { margin-bottom: 0.4em; line-height: 1.6; }
  code { font-family: 'DM Mono', monospace; background: #ede8df; color: #0e1b2e; padding: 0.15em 0.45em; border-radius: 3px; font-size: 0.88em; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #6b6560; }
  section.lead h1 { font-size: 2.7em; }
  section.lead p { font-size: 1.1em; color: #6b6560; margin-top: 0.4em; }
  section.current { border-left: 5px solid #3b9eff; }
  section.open { background: #f0f7ff; border-left: 5px solid #3b9eff; }
  section.risk { background: #fff8f0; border-left: 5px solid #f0a050; }
  .status-open {
    display: inline-block;
    background: #3b9eff;
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 0.75em;
    padding: 0.2em 0.5em;
    border-radius: 3px;
    margin-left: 0.4em;
  }
  .status-done {
    display: inline-block;
    background: #2dd4a0;
    color: #0e1b2e;
    font-family: 'DM Mono', monospace;
    font-size: 0.75em;
    padding: 0.2em 0.5em;
    border-radius: 3px;
    margin-left: 0.4em;
  }
  .checklist li { list-style-type: none; padding-left: 0; }
  .checklist li::before { content: "- [ ] "; font-family: 'DM Mono', monospace; color: #3b9eff; }
---

<!-- _class: lead -->

# Salesforce Domain — Knowledge Transfer

**Meridian Health Engagement** &nbsp;|&nbsp; Prepared by: [Departing Team Member]

*Effective [Last Date] · Successor: [Successor Name] · April 2025*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
This knowledge transfer deck is prepared by the departing team member and reviewed in a session with the successor and the engagement manager. It is designed to be completed over two sessions: Session 1 covers the domain overview, current state, and key systems (slides 1–8). Session 2 covers key people, open issues, handoff documents, and risks (slides 9–12).

Replace all bracketed fields before any session. The deck should feel personal, not generic. A KT deck that reads like a template rather than a real account of what you actually know is not useful.

Timing: this deck should be started at least 2 weeks before the last date. The departing team member should treat the KT as a first-class deliverable — not something assembled in the last 48 hours. A rushed KT is a disservice to the client, the team, and the successor.

Format for the KT sessions: screen sharing with the departing person driving, successor asking questions, engagement manager observing. Record the sessions if both parties consent. The recording supplements but does not replace this deck.

SponAItech policy: a complete KT deck and at least two recorded sessions are required before a team member's last date on any active client engagement. This is a client obligation, not just an internal process.
-->

---

## Context — Why This Transfer Matters

**Engagement:** Meridian Health Salesforce Optimization — active since January 2024

**Scope:** Claims portal LWC components, Apex service layer, Flow automation for enrollment

**Client relationship:** Strong — Priya Nair (IT Director) is the primary sponsor. She values responsiveness over polish. Call her when there is a problem, do not email.

**What the successor inherits:** 14 months of accumulated context, active technical debt in the enrollment flow, and a client who trusts this team.

<!--
SPEAKER NOTES — SLIDE 2 (Context)
This slide sets up why this KT matters. Do not skip it. A successor who does not understand the engagement history will treat every conversation with the client as a blank slate — and the client will notice the discontinuity.

The client relationship note is critical and should be highly specific. The successor needs to know: who is the real decision-maker (Priya Nair, not the procurement contact), what communication style works (direct phone calls for problems, not email), what the client values (responsiveness), and what earned the relationship in the first place (14 months of delivered work).

Technical debt callout: the enrollment flow has known technical debt that has been intentionally deferred. The successor must understand what it is and why it was deferred — otherwise they may either ignore it (continuing the deferral without understanding the risk) or fix it prematurely (disrupting an active client workflow without the context of why it was left alone).

The deck should be written in the first person by the departing team member. "Priya values responsiveness" is more useful than "the client values responsiveness" — it signals direct knowledge, not secondhand information.
-->

---

## Domain Overview — Salesforce Org Structure

**Environment landscape:**

| Org | Purpose | Deploy frequency |
|---|---|---|
| `meridian-prod` | Production — 840 active users | Bi-weekly release train |
| `meridian-uat` | UAT — business stakeholder testing | On demand |
| `meridian-dev` | Developer sandbox | Daily |
| `meridian-scratch-*` | Scratch orgs for feature development | Per feature branch |

**Stack:** Apex (service layer) · LWC (UI layer) · Flows (automation) · Custom metadata (configuration)

*Access credentials and org aliases in the `sfdx-project.json` and `.env.example` — NOT in this deck*

<!--
SPEAKER NOTES — SLIDE 3 (Domain Overview — Org Structure)
The org landscape slide is the first thing the successor needs to understand before touching anything. Four orgs with four different purposes and different deployment frequencies. The most critical constraint: never deploy directly to `meridian-prod` — all production deployments go through the bi-weekly release train via the deployment pipeline.

Scratch org naming convention: `meridian-scratch-{feature-name}`. Scratch orgs expire after 30 days. The successor will find expired scratch orgs in the SFDX alias list — they can be safely ignored.

The credentials note is important: this deck will be stored in the engagement's GitHub repository and possibly shared with the client. No credentials go in this deck. Access credentials are in the `.env.example` file and the team's password manager. The successor's first action should be to generate their own credentials for all four orgs — do not share credentials, even during a transition.

Deployment pipeline: the bi-weekly release train uses GitHub Actions. The workflow file is at `.github/workflows/deploy-prod.yml`. The pipeline requires the `security-reviewer` agent to pass before production deployment. Successor should review the pipeline configuration in Week 1.
-->

---

<!-- _class: current -->

## Current State — What Is Active

**Active work items as of [last date]:**

- **MERH-0147** — Enrollment Flow v3 refactor <span class="status-open">IN PROGRESS</span>
  - 60% complete · tests written · G3 Build gate · estimated 2 weeks remaining
- **MERH-0151** — Claims portal LWC mobile responsiveness <span class="status-open">IN PROGRESS</span>
  - Design approved · G3 Build starting next sprint
- **MERH-0138** — Custom metadata type for rate tables <span class="status-done">COMPLETE</span>
  - Deployed to production April 10 · monitoring period ends April 24

**Sprint velocity:** 8–10 story points per sprint · Current sprint ends April 25

<!--
SPEAKER NOTES — SLIDE 4 (Current State)
This is the most operationally critical slide in the deck. The successor needs to know exactly where each work item is in the pipeline on the handoff date.

MERH-0147 (Enrollment Flow v3): this is the highest-risk active item. The flow touches 4 custom objects and 2 external system integrations. The test suite covers 91% of the Apex service layer but the Flow tests are manual — this is the technical debt mentioned in the Context slide. The successor must read the G3 build gate output for this work item before making any changes.

MERH-0151 (Mobile responsiveness): this is the lower-risk item. The design was approved by Priya in the April 15 session (recording in the engagement Slack channel). The LWC components affected are `claimsPortalHeader`, `claimsListView`, and `claimDetailPanel`. All three have existing test coverage.

MERH-0138 (Complete): this item is in a 2-week monitoring period. The rate table metadata type is used by the pricing calculation flow. If the successor sees any pricing anomalies in the first two weeks, this deployment is the first thing to investigate. The monitoring SLA ends April 24.

Sprint cadence: Meridian runs 2-week sprints aligned to their IT release calendar. Sprint planning is every other Monday at 10 AM PST. The successor should attend the next sprint planning (April 28) even if they are still in KT mode.
-->

---

## Key Systems — Apex Service Layer

<!-- _class: current -->

**Three primary service classes:**

- `ClaimsProcessingService` — orchestrates the full claims lifecycle; 1,240 lines; test class `ClaimsProcessingServiceTest` (94% coverage)
- `EnrollmentService` — handles plan enrollment logic; 680 lines; currently being refactored in MERH-0147
- `MemberDataService` — read-only member data access; wraps external API callouts; 420 lines

**Governor limit watch:** `ClaimsProcessingService.processBatch()` is approaching the 150 SOQL limit per transaction in edge cases with more than 40 dependent claims. This is logged in `memory/projects/salesforce/meridian-health/blockers.md`.

<!--
SPEAKER NOTES — SLIDE 5 (Key Systems — Apex)
The three service classes are the core of the Salesforce implementation. The successor should spend at least 2 hours reading through each class before the handoff session ends. Not writing code — reading. Understanding the pattern before changing anything.

The ClaimsProcessingService governor limit issue is the most immediate technical risk. The 150 SOQL limit is approached in edge cases — specifically, when a batch contains more than 40 claims that each have 4+ dependent adjustments. This is rare in production but has happened twice in the last 6 months. The fix requires restructuring the SOQL queries to use relationship queries rather than sequential lookups. This is tracked in the blockers.md file.

EnrollmentService refactor: the successor is inheriting a partially refactored service class. The refactored version is in a feature branch (`feature/enrollment-v3`) — the main branch still has the old version. Do not merge the feature branch without completing the test suite for the new enrollment flow logic. The merge is gated on the G3 build being complete.

MemberDataService: this class is stable and should not be modified without specific client sign-off. The external API it wraps is provided by Meridian's data warehouse team and has an SLA of 99.5% uptime. Any changes to callout structure must be coordinated with the data warehouse team lead (contact in key people slide).
-->

---

## Key Systems — LWC Components

<!-- _class: current -->

**Component inventory (active):**

| Component | Purpose | Complexity |
|---|---|---|
| `claimsPortalHeader` | Navigation + user context | Low |
| `claimsListView` | Paginated claims list with filters | Medium |
| `claimDetailPanel` | Full claim detail + action buttons | High |
| `enrollmentWizard` | Multi-step enrollment flow | High |
| `memberDashboard` | Summary view for member self-service | Medium |

**`claimDetailPanel` note:** contains a custom `lightning-datatable` extension that the client's UX team built in-house. Do not replace it with a standard component — Priya signed off on the custom version and the client team maintains it.

<!--
SPEAKER NOTES — SLIDE 6 (Key Systems — LWC)
The component inventory gives the successor a map of the UI layer. The complexity rating is a rough guide — High means "read this carefully before touching anything," not "avoid."

The `claimDetailPanel` callout is the most important note on this slide. The client's UX team built a custom `lightning-datatable` extension that handles multi-level sorting and row expansion — capabilities that the standard LWC component does not support. It is not perfect code, but replacing it would break the client team's ability to maintain their own UI extension. This decision was made jointly with Priya in February 2024 and is documented in the engagement decisions log.

`enrollmentWizard`: this component is directly connected to the `EnrollmentService` that is being refactored in MERH-0147. Any changes to the wizard during the refactor period must be coordinated with the Apex changes — they cannot be deployed independently without regression risk.

The mobile responsiveness work (MERH-0151) affects `claimsPortalHeader`, `claimsListView`, and `claimDetailPanel`. The design spec is in the engagement Figma file, linked from the MERH-0151 work item manifest.
-->

---

## Key People — Who to Know

**Meridian Health:**

- **Priya Nair** — IT Director, primary sponsor · Direct line preferred · Responds fastest before 9 AM PST
- **Marcus Webb** — Claims Operations Lead · Subject matter expert for business logic questions
- **Dani Ochoa** — Data Warehouse Lead · Point of contact for MemberDataService API changes

**SponAItech:**

- **[Engagement Manager]** — overall account relationship · CC on all client communications
- **[New Successor Name]** — taking over technical lead from [last date]

*Meeting preferences and working hours in the engagement contact sheet: [link]*

<!--
SPEAKER NOTES — SLIDE 7 (Key People)
The key people slide is the relationship map. Every name here represents context that cannot be easily reconstructed from documentation.

Priya Nair: she is the reason this engagement exists. She championed the Salesforce optimization initiative internally after being frustrated with the vendor that preceded SponAItech. She is detail-oriented and will notice if the new contact does not know the history. Recommended first action for the successor: schedule a 30-minute introduction call with Priya in Week 1. Do not show up to the first team meeting as if you already know everything — she will appreciate the humility of "I am getting up to speed and want to hear your perspective."

Marcus Webb: the business logic expert. When a requirement seems inconsistent with the data model, ask Marcus. He knows the claims business domain better than anyone on the Meridian side and has saved this engagement from two significant misimplementations by catching business rule edge cases in review.

Dani Ochoa: she controls the MemberDataService API. Any changes to the API — new fields, changed response structure, rate limit adjustments — go through Dani. She is technically strong and prefers written specifications before meetings. Do not cold-call her with an API change request — send a written spec first.

The engagement contact sheet: this should be a living document in the project memory directory. If it does not exist yet, the departing team member should create it as part of the KT process.
-->

---

## Open Issues — What Is Unresolved

<!-- _class: open -->

**Active blockers:**

- **Governor limit risk** in `ClaimsProcessingService.processBatch()` <span class="status-open">OPEN</span> — tracked in blockers.md; no immediate mitigation; watch if batch sizes increase
- **Enrollment Flow v3** — test coverage below 80% floor for Flow components <span class="status-open">OPEN</span> — MERH-0147 cannot close until this is resolved
- **Rate table cache invalidation** — no automated cache clear when rate tables change via metadata deployment <span class="status-open">OPEN</span> — manual clear required after each deployment; documented in runbook

**Pending client decisions:**

- Priya has not signed off on the mobile breakpoints for MERH-0151 (scheduled for April 28 sprint review)
- Annual contract renewal discussion scheduled for May 15 — engagement manager leads

<!--
SPEAKER NOTES — SLIDE 8 (Open Issues)
Open issues are the things that the departing team member would be working on next if they were staying. This slide is the most important section for immediate risk management.

The governor limit risk: this has been known since February and has been intentionally deferred because the edge case is rare and the fix requires a significant refactor of the batch processing logic. The risk level is low for now but will increase if Meridian onboards additional health plan clients (which would increase average batch sizes). The successor should monitor batch size trends in the Application Insights dashboard and escalate to the engagement manager if the average crosses 30 dependent claims per batch.

Enrollment Flow v3 test coverage: the Apex coverage is above 90% but the Flow automation tests are manual and not counted toward the coverage floor. This is a process gap — the engagement needs a plan to add automated Flow testing. Salesforce introduced Robot Framework integration for Flow testing in Spring 2024. This is worth evaluating as a path to automated coverage.

Rate table cache: this is a known and documented workaround. The procedure is in the runbook. It takes 5 minutes. The risk is that a rate table deployment is done without clearing the cache, causing pricing calculations to use stale rates. The mitigation is to make cache clearing a mandatory step in the deployment checklist — add it if it is not already there.
-->

---

## Handoff Documents — What to Read First

**Read in this order:**

1. `memory/projects/salesforce/meridian-health/session_handover.md` — last session state
2. `memory/projects/salesforce/meridian-health/decisions.md` — all architecture decisions with rationale
3. `memory/projects/salesforce/meridian-health/blockers.md` — current blockers with history
4. `MERH-0147` manifest and G3 build log — active high-risk work item
5. Engagement contract and SLAs — `[SharePoint link]`

**Recorded KT sessions:**
- Session 1 — Apex and org structure — `[recording link]`
- Session 2 — Client relationships and open issues — `[recording link]`

<!-- CHECKLIST FORMAT — print and use as a physical checklist -->

<!--
SPEAKER NOTES — SLIDE 9 (Handoff Documents)
The reading order is intentional. Session handover first — it gives the successor a precise starting point without requiring them to synthesize 14 months of history. Decisions second — the architectural decisions explain why things are the way they are, which prevents the successor from "improving" something that was deliberately designed a certain way. Blockers third — knowing the active risks before touching anything.

The MERH-0147 manifest: this is the G3 build gate document for the highest-risk active work item. The successor should not advance this work item to G4 Test until they have read the manifest and understand the full scope of the refactor.

The engagement contract: the successor needs to know the SLAs they are inheriting. Response time SLAs, deployment frequency commitments, and escalation paths are all in the contract. If the successor does not know the SLAs, they cannot manage to them.

Physical checklist: the bulleted list on this slide is designed to be printed and physically checked as each item is completed. The successor should not claim the KT is complete until all five reading items are done and both session recordings have been watched.

The recordings are supplements, not replacements. If there is a conflict between what was said in a recording and what is written in this deck, the deck is the authoritative record. The recordings capture nuance, tone, and spontaneous Q&A that the deck cannot.
-->

---

<!-- _class: risk -->

## Risks — What Could Go Wrong

**Technical risks:**

- **Governor limit breach** — if `ClaimsProcessingService` is called with a batch > 50 items, transaction will fail. Short-term mitigation: batch size cap at 40 in the scheduler config.
- **Enrollment Flow data integrity** — the v3 refactor introduces a new enrollment status state machine. Incorrect state transitions could create orphaned enrollment records. Rollback plan: disable v3 feature flag and revert to v2 in one deployment.

**Relationship risks:**

- Priya is currently very positive about SponAItech. Any visible discontinuity (missed SLAs, slow response, "who are you?") during the transition period could damage the relationship.
- The annual renewal in May is not guaranteed — the relationship quality during this transition period is the determining factor.

<!--
SPEAKER NOTES — SLIDE 10 (Risks)
This slide is the honest assessment that many KT decks omit. Write it even when the risks are uncomfortable. The successor deserves to know what they are walking into.

The governor limit short-term mitigation: the batch size cap at 40 is configured in `BatchSchedulerConfig__mdt` under the `MaxBatchSize` field. Do not raise this number without first completing the SOQL refactor for `processBatch()`. The cap is a risk control, not a preference.

The enrollment flow rollback plan: the feature flag is `EnrollmentV3Enabled__c` on the `MeridianSettings__c` custom setting. Setting it to `false` instantly disables the v3 logic and routes all enrollment requests to the v2 service. This was tested as part of the G2 design gate and is confirmed to work without a deployment.

The relationship risk is real and should not be understated. The successor will be evaluated by Priya against the bar set by the predecessor. The first 60 days of the transition are the highest-risk period for the client relationship. The engagement manager should be on at least two of the first four client calls with the successor.

The annual renewal: the contract renews May 15. If the transition is rocky, Priya may use the renewal as an opportunity to reassess. The engagement manager is the lead on the renewal conversation — but the successor's technical performance is the evidence base.
-->

---

## Questions — Ask Before the Last Day

**Questions to answer during KT sessions:**

- ● Where is the Meridian org's production deploy credentials stored?
- ● What is the on-call rotation for production incidents on this engagement?
- ● Who approves Apex code reviews — internal or Meridian IT?
- ● What is the current status of the May 15 renewal conversation?
- ● Are there any verbal commitments to Priya not captured in the written spec?

*If a question cannot be answered in this deck — it must be answered in a session before the last date*

<!--
SPEAKER NOTES — SLIDE 11 (Questions)
This slide is a forcing function. It identifies five questions that the KT is not complete until they are answered. The departing team member should review these questions against the deck before the first KT session and fill in any answers that belong in earlier slides.

Production credentials: the answer is "in the team password manager and provisioned per-person." The successor must have their own Salesforce login with the appropriate permission set before the departing team member's last date. Shared credentials are a security violation.

On-call rotation: for a lean engagement, "on-call" may mean "the founder is always reachable." But this needs to be explicit — the successor needs to know who they call at 2 AM if the claims API goes down.

Code review approvals: the engagement agreement specifies that Apex code is reviewed internally (G5 Review gate) before submission to Meridian. Meridian IT does a final smoke test in UAT but does not review Apex code. The successor should not ask Meridian to review code — it violates the division of responsibilities.

Verbal commitments: this is the most commonly missed KT question. Over 14 months, there have likely been informal commitments made in passing that were never captured in writing. "We said we would add the audit trail feature next quarter" — things like that. The departing team member should ask themselves: "What did I promise that is not in the spec?" These commitments must be captured before the last date.
-->

---

<!-- _class: lead -->

# Thank You — and Good Luck

*[Departing team member name] — [last date]*

**The team is in good hands.**

*Questions after the last date: [departing person's personal contact, if willing to provide]*

<!--
SPEAKER NOTES — SLIDE 12 (Close)
End on a human note. The KT deck is a professional document, but it is also a personal one — it represents everything a team member has built and is now entrusting to someone else.

The "team is in good hands" statement is a vote of confidence in the successor. It should be genuine — say it only if you mean it. If there are concerns about the successor's readiness, those concerns should have been raised with the engagement manager during the KT process, not left unsaid on the closing slide.

The personal contact offer is optional. Not every departing team member is comfortable providing ongoing support after their last date. Do not pressure anyone to include it. If it is included, it should be used sparingly and briefly — the successor should be building their own understanding of the engagement, not relying on the predecessor.

For the engagement manager: after the KT is complete, send a brief note to Priya Nair acknowledging the transition, introducing the successor by name, and confirming that continuity is the top priority during the transition period. Keep it short — two paragraphs. This communication signals that SponAItech takes relationship continuity seriously.
-->
