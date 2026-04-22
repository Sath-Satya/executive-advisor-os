<!-- TEMPLATE: onboarding-deck
     CATEGORY: Training / Onboarding
     USE WHEN: welcoming a new hire through their first week of onboarding
     SLIDE COUNT: 15
     PALETTE: Executive cream
     RENDER: marp --pptx 33-onboarding-deck.md -->
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
    font-size: 2.3em;
    letter-spacing: -0.4px;
    margin-bottom: 0.2em;
  }
  h2 { color: #b8965a; font-size: 1.05em; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.6em; }
  h3 { color: #0e1b2e; font-size: 1.2em; font-weight: 600; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.88em; }
  ul { margin-top: 0.5em; }
  li { margin-bottom: 0.45em; line-height: 1.6; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #6b6560; }
  section.lead h1 { font-size: 2.8em; }
  section.lead p { font-size: 1.15em; color: #6b6560; margin-top: 0.5em; }
  .milestone-row { display: flex; gap: 1.4em; margin-top: 1em; }
  .milestone {
    background: #ffffff;
    border-left: 4px solid #b8965a;
    padding: 0.75em 1.1em;
    border-radius: 4px;
    flex: 1;
  }
  .milestone strong { font-size: 1.05em; }
  .milestone em { display: block; margin-top: 0.2em; font-size: 0.82em; }
  .people-card { background: #ffffff; border-radius: 6px; padding: 0.8em 1em; margin-bottom: 0.5em; border-left: 3px solid #b8965a; }
  .people-card strong { font-size: 1em; }
  .people-card em { font-size: 0.82em; color: #6b6560; }
---

<!-- _class: lead -->

# Welcome to SponAItech

**We are glad you are here.**

*New Hire Onboarding — Week 1 — April 2025*

<!--
SPEAKER NOTES — SLIDE 1 (Welcome)
This is the first slide the new hire sees on Day 1. The tone is warm but not effusive. SponAItech is a professional environment — the welcome should match that register.

Deliver this slide in person if possible. If remote, have video on. The first five minutes of onboarding set the emotional tone for the first 90 days. Make eye contact, speak slowly, and leave space for the new hire to settle in before you launch into content.

If you are the hiring manager delivering this: share a brief personal statement about why you are excited this person joined. One or two sentences. "I hired you because..." is a powerful opening. It tells the new hire they were a deliberate choice, not a backfill.

If HR is delivering this to a group: acknowledge that the group comes from different backgrounds and will be joining different teams. The next few slides will be common ground before they split into team-specific onboarding tracks.

This deck covers Week 1. Week 2 onboarding materials (tools deep dives, client orientation, and project shadowing) are in the New Hire portal under your profile.
-->

---

## Our Story — SponAItech

SponAItech was founded on a single conviction: **enterprise organizations deserve AI-powered development at startup speed.**

- Founded by practitioners — 24 years IT, 18 years healthcare, 6 years Salesforce
- Built for mid-market companies who need production-ready systems, not pilots
- One-person model scaled by AI automation — every person here has leverage

*We do not build prototypes. We build things that ship.*

<!--
SPEAKER NOTES — SLIDE 2 (Company Story)
The company story is a credibility statement, not a marketing slide. New hires need to understand why SponAItech exists and why clients trust us — before they can represent the company to those clients.

The founding story: SponAItech was built by someone who spent 24 years inside the systems that other consultants sell into. That insider perspective is the core differentiator. When we tell a Salesforce admin at a health plan that we understand their constraints, we actually do — because we have lived them.

The "one-person model scaled by AI" point is something new hires will feel immediately. SponAItech operates lean by design. AI automation handles scaffolding, research, and first drafts. Your job is judgment, client relationships, and the things that require enterprise domain expertise. If you are used to large teams with hand-offs, this will feel different. That is intentional.

"We do not build prototypes" is a cultural declaration. If a client asks for a quick POC that will never scale, we redesign the ask before we accept the work. This has cost us some deals. It has kept every delivered project running in production.
-->

---

## Mission and Values

**Mission:** AI-powered consulting that delivers production-ready systems at startup speed with enterprise quality.

**What we value:**

- **Evidence over opinion** — show your work, ship proof
- **Speed without shortcuts** — fast and right, not fast and reckless
- **Client domain respect** — they know their world; we know ours; we learn together
- **Transparency about AI** — we use AI, we say so, we own the output

<!--
SPEAKER NOTES — SLIDE 3 (Mission and Values)
Walk through each value with a brief example or story. These are not posters on a wall — they are the decision rules we apply when the answer is not obvious.

Evidence over opinion: last quarter, a client asked us to recommend a data architecture. We had an opinion but not enough data. We told them. We ran a two-week spike, produced evidence, then made a recommendation. They extended the contract because of that discipline.

Speed without shortcuts: we use AI to move fast. AI generates first drafts of code, test cases, and documentation. A human reviews and approves every output before it ships. The speed comes from AI handling the 80% of work that is mechanical. The quality comes from human judgment on the 20% that requires expertise.

Client domain respect: we work in healthcare, Salesforce, and custom software. These are deep domains with real stakes. A wrong claims configuration can deny a patient's medication. A broken Apex trigger can corrupt 40,000 records. We take the domain seriously even when the technology seems straightforward.

Transparency about AI: we do not hide that we use Claude to accelerate our work. We tell clients. We explain what AI does and what humans review. This builds trust. It also protects us — if something AI-generated is wrong, we own it because a human reviewed it.
-->

---

## Organization Structure

**SponAItech LLC** — single-entity consulting firm

```
Founder / Principal Consultant
     │
     ├── Salesforce Domain
     ├── Custom Applications Domain
     ├── iOS Applications Domain
     └── Trading Systems Domain
```

**Engaged team model:** domain experts brought in as needed per project

*Your hiring letter specifies your primary domain — you may work across domains*

<!--
SPEAKER NOTES — SLIDE 4 (Org Structure)
SponAItech is a lean organization. The structure slide conveys that — there is no sprawling org chart because there is no sprawling organization. This is a feature, not a limitation.

The "engaged team model" means that for larger projects, SponAItech brings in domain specialists under contract. If you are one of those specialists, your engagement terms are in your contract. If you are a full-time team member, you report to the founder.

For new hires from large organizations: the absence of layers is an adjustment. There is no escalation path for most decisions — you make the call, you document the reasoning, you own it. This is what "leverage" means in practice.

Domain ownership: when you are working in your primary domain, you are the technical authority. When you are working across domains, you collaborate with the domain owner. The Agentic OS system (covered in your tools onboarding on Day 3) reflects this structure — each domain has its own operating system with its own standards.

Questions about the structure that often come up: "Who do I report to?" — The founder. "Who approves my work?" — You do, via the verification gates in the Agentic OS. "Who do I call if there's a production incident?" — The founder, immediately, regardless of time.
-->

---

## Your Team

**Direct contact list — save these on Day 1:**

<div class="people-card">
<strong>Sathish T. — Founder and Principal Consultant</strong><br>
<em>Primary contact for all client and business decisions · sathiyaraj.t@gmail.com</em>
</div>

<div class="people-card">
<strong>[Your Hiring Manager Name] — Domain Lead</strong><br>
<em>Day-to-day technical direction · [email]</em>
</div>

<div class="people-card">
<strong>[Buddy / Onboarding Partner Name]</strong><br>
<em>Your first-week guide for tools, process, and "how we actually do things" · [email]</em>
</div>

*Add your own contacts as you meet the team this week*

<!--
SPEAKER NOTES — SLIDE 5 (Your Team)
Replace the bracketed names before delivering this deck to any specific new hire. This is a template — the people cards must be populated with real names.

The onboarding buddy concept: every new hire gets an assigned buddy for Week 1. The buddy is not their manager — they are a peer who has been at SponAItech for at least 3 months and knows where things live. Buddy conversations are informal and off the record. New hires should feel free to ask "dumb questions" to their buddy that they might not want to ask their manager on Day 1.

The founder contact note: this is intentional. At SponAItech's scale, new hires should feel comfortable contacting the founder directly for business decisions. There is no "go through channels" culture here. That said, the domain lead is the right first call for technical questions and project-level decisions.

Encourage new hires to add 3–5 more contacts to this list by the end of Week 1. The goal is that by Friday, they can name the five people they would call first in a crisis. If they cannot, their onboarding buddy has a follow-up task.
-->

---

## Your Role — What Success Looks Like

**Your primary domain:** [Domain — e.g., Salesforce / Custom Apps / iOS / Trading]

**In the first 30 days, success means:**
- ✓ You can navigate the Agentic OS independently
- ✓ You have shipped one production-quality artifact (code, spec, or design doc)
- ✓ You have attended two client calls as an observer

**By Day 90, success means:**
- ✓ You own one active work item end to end
- ✓ You have run one full gate cycle (Plan → Build → Verify) without a prompt from your manager

<!--
SPEAKER NOTES — SLIDE 6 (Your Role)
Replace the bracketed domain before delivery.

The two-tier success definition (30 days / 90 days) sets expectations without overwhelming. New hires often ask "am I doing well?" in the first month. These criteria give them a concrete answer.

The 30-day goal of shipping "one production-quality artifact" is deliberately broad. A new Salesforce developer might ship a tested Apex class. A custom app developer might ship a module with passing tests. What matters is that the artifact meets the quality bar — built with TDD, passed through the verification gate, documented. If it does not meet the bar, the manager's job is to redirect, not to accept sub-par work and say nothing.

The 90-day goal is the independence milestone. Running a full gate cycle without prompting means the new hire has internalized the process. It does not mean they work alone — it means they know what step comes next without being told.

If this is a senior hire who has been doing this type of work for 10 years: adjust the language. "One active work item" may be too small. Scale the 90-day target to match the hire's experience level. This template is a floor, not a ceiling.
-->

---

## First 30 — 60 — 90 Days

<div class="milestone-row">
  <div class="milestone">
    <strong>Days 1–30</strong>
    <em>Orient · Shadow · Ship one artifact</em>
    Orient to tools, process, and one active project. Attend all team calls as observer. Ship one artifact under supervision.
  </div>
  <div class="milestone">
    <strong>Days 31–60</strong>
    <em>Contribute · Own tasks · Build relationships</em>
    Take ownership of discrete tasks. Present one artifact to a client or the team. Identify one process improvement.
  </div>
  <div class="milestone">
    <strong>Days 61–90</strong>
    <em>Lead · Run gates · Operate independently</em>
    Own a work item end to end. Run a full gate cycle. Propose one improvement to the Agentic OS for your domain.
  </div>
</div>

<!--
SPEAKER NOTES — SLIDE 7 (30-60-90)
The 30-60-90 plan is the most referenced slide in any onboarding deck. New hires will screenshot it, share it with their family, and return to it when they feel uncertain about how they are doing. Make it concrete.

The three-phase structure mirrors how expertise develops: Orient (learning the context) → Contribute (applying what you learned) → Lead (generating new value from your unique perspective). Each phase has a different risk tolerance. In the Orient phase, mistakes are expected and safe. In the Lead phase, mistakes are real and must be caught by the gate process.

The "propose one improvement to the Agentic OS" milestone in days 61–90 is an important signal. It tells new hires that the system is not fixed — it is designed to evolve based on what the people using it discover. This invitation to improve the system is a form of psychological ownership that correlates strongly with long-term retention.

For the manager: schedule three structured check-ins — at 30, 60, and 90 days — with a written agenda. The agenda for each check-in should reference the success criteria from the previous slide. These are not performance reviews — they are navigational conversations.
-->

---

## Tools — What You Will Use Daily

- **VS Code** — primary development IDE with Claude Code extension
- **GitHub (SponAItech org)** — all code, documentation, and project artifacts
- **Claude Code CLI** — AI-assisted development via the Agentic OS
- **Azure** — cloud platform (Container Apps, SQL, Storage)
- **Salesforce CLI** (Salesforce domain only) — org deployment and scratch orgs
- **TradeStation** (Trading domain only) — strategy development and backtesting

*Tools access provisioned by EOD Day 1 — IT contact: [IT contact name]*

<!--
SPEAKER NOTES — SLIDE 8 (Tools)
This slide is a preview, not a tutorial. Detailed tools onboarding happens in Day 3 sessions. The purpose here is to make sure new hires can orient themselves before those sessions.

The Claude Code CLI is the tool that will feel most unfamiliar to new hires from traditional development environments. Block 30 minutes on Day 2 for a self-guided tour of the Agentic OS using the onboarding path in the CLAUDE.md file. By Day 3, they should understand what skills, agents, and commands are — even if they have not used them yet.

Access timing: tools access is provisioned in this order: email and Slack on Day 1 AM, GitHub on Day 1 PM, Azure on Day 2 AM, domain-specific tools by Day 3. If any access is missing at the expected time, the new hire should notify their onboarding buddy immediately — not wait and work around it.

For remote hires: video all tool setup sessions. The recording becomes the training artifact for the next new hire. This is an example of how SponAItech uses the "automate what is repeatable" principle internally.
-->

---

## Meetings — The Weekly Rhythm

| Day | Meeting | Duration | Purpose |
|---|---|---|---|
| Monday | Team standup | 15 min | What is in progress, what is blocked |
| Wednesday | Architecture review | 30 min | Design decisions, cross-domain questions |
| Friday | Week close | 20 min | What shipped, what carries to next week |
| As needed | Client calls | 30–60 min | Project updates, discovery, demos |

*Calendar invites sent Day 1 — conflicts escalate to your domain lead*

<!--
SPEAKER NOTES — SLIDE 9 (Meetings)
Fewer meetings is a SponAItech principle. The three standing meetings cover the three things that require synchronous coordination: status (standup), design (architecture review), and closure (week close). Everything else is async or on-demand.

Client calls are not on a fixed schedule — they are triggered by project milestones and client needs. New hires should attend all client calls in their first 30 days as observers. No speaking unless invited. Taking notes is expected and valued.

The architecture review is the most important meeting for new hires in Weeks 2–4. This is where cross-domain design decisions are made. New hires should come with at least one question about a design choice they encountered that week — even if it is a small one. Contributing to architecture review is a signal that the new hire is thinking beyond their immediate task.

For remote teams: all meetings have video on by default. No exceptions for standing meetings. For client calls, confirm the client's video preference in advance.
-->

---

## People to Meet — Week 1

**By end of Day 2:**
- ● Your onboarding buddy — informal tour and Q&A
- ● Your domain lead — context on active projects

**By end of Day 5:**
- ● One peer in a different domain — cross-pollination conversation
- ● Any active client contact your manager introduces

*Introduce yourself before asking for something — always*

<!--
SPEAKER NOTES — SLIDE 10 (People to Meet)
The structured "who to meet by when" list prevents the paralysis that some new hires experience in the first week — not knowing who to talk to or in what order.

The cross-domain peer conversation is intentional. SponAItech works across four domains. A Salesforce developer who has never spoken to the trading systems developer misses the cross-pollination that makes SponAItech's AI-native approach distinctive. "How do you use the Agentic OS in your domain?" is a great opening question for these conversations.

The etiquette note ("introduce yourself before asking for something") sounds obvious but new hires often skip it when they are under pressure to get up to speed fast. A 60-second introduction before a request is the difference between building a relationship and burning a favor.

For the onboarding buddy: send the new hire a calendar invite for a 45-minute informal walk-through before EOD Day 2. The agenda should be: 15 min informal, 15 min tool tour, 15 min "what I wish I had known in Week 1." No slides required.
-->

---

## Key Documents — Where Things Live

- **CLAUDE.md** — the operating system for your domain (start here)
- **README.md** — project-specific context and quickstart
- **session_handover.md** — last session summary for any active project
- **GitHub SponAItech org** — all code and project artifacts
- **.env.example** — environment variables template for every project
- **Brand guidelines** — `.claude/rules/brand/` — visual and voice standards

*When in doubt: read the CLAUDE.md for your domain first*

<!--
SPEAKER NOTES — SLIDE 11 (Key Documents)
This slide solves one of the most common new hire frustrations: not knowing where information lives. The answer at SponAItech is: CLAUDE.md for your domain is the entry point for everything.

The CLAUDE.md convention: every domain has a CLAUDE.md that explains the domain's tech stack, conventions, workflow, and project structure. Reading your domain's CLAUDE.md is the single most valuable 30-minute investment of the first day. It is not glamorous, but it prevents weeks of confusion.

The session_handover.md is the memory artifact that connects sessions. When you pick up work from a previous session — yours or someone else's — read the handover first. It contains what was built, what is blocked, and what comes next. Skipping it is the fastest way to duplicate work or miss a critical context.

The .env.example convention: every project has an .env.example that shows what environment variables are required. Never commit a .env file. Never hardcode credentials. These are not preferences — they are enforced by the pre-commit hook.
-->

---

## Culture — How We Work

- **Async first** — write before you meet; meeting is for decisions, not updates
- **Document as you go** — if you discovered something, write it down for the next person
- **Overcommunicate on blockers** — blocked for more than 2 hours? Tell someone
- **AI output is your output** — you are accountable for everything AI generates under your name

*The goal: everyone on the team should be able to pick up your work at any moment*

<!--
SPEAKER NOTES — SLIDE 12 (Culture)
Each of these cultural norms has a practical reason behind it.

Async first: SponAItech operates across time zones and with varying focus schedules. Async communication by default respects everyone's deep work time. Before scheduling a meeting, ask: can this be resolved in a Slack message or a short document? If yes, do that.

Document as you go: the Agentic OS has a `_learnings.md` file in every skill. When you discover something that works better than the documented approach, add a learning entry. This is how the system improves — not through a quarterly review, but through continuous capture.

Overcommunicate on blockers: a blocked developer is a fully stopped developer. Every hour of blocked time is an hour of zero output. Surfacing blockers early — even when it feels like admitting weakness — is the professional behavior at SponAItech. "I hit a wall on X — here is what I tried — asking for a 15-minute pair" is the right message.

AI output accountability: this is non-negotiable. When Claude generates a code module and you commit it, you are accountable for that code. Review it. Test it. Run the verification gate. "The AI wrote it" is not a defense.
-->

---

## Your Goals — First Week

**By end of Day 5, you should have:**

- ✓ Completed your tools setup and access verification
- ✓ Read your domain's CLAUDE.md end to end
- ✓ Met your onboarding buddy and domain lead
- ✓ Attended at least one standup
- ✓ Started the first module of your domain training track
- ✓ Written your first session_handover.md entry

*These are not performance metrics — they are orientation checkpoints*

<!--
SPEAKER NOTES — SLIDE 13 (Goals — First Week)
Frame this as orientation checkpoints, not performance evaluation. The first week should feel safe and exploratory. If a new hire reaches Friday and has checked three of six items, that is a conversation starter, not a disciplinary trigger.

The last item — writing a session_handover.md entry — is the most important onboarding habit to establish early. The handover format is the primary continuity mechanism at SponAItech. If new hires start writing them in Week 1, it becomes second nature. If they skip it for the first month and try to start later, the habit never forms.

Ask the new hire to share their handover with you at EOD Friday. Review it together in the Day 5 check-in. Give specific feedback: "This is clear" or "This section is too vague — what specifically was blocked?" The quality of the handover reflects the quality of the thinking.

For remote hires: the Week 1 goal list should be sent as a written message on Day 1, not just shown on a slide. It becomes the new hire's personal checklist for the week.
-->

---

## Questions — Ask Early, Ask Often

**No question is too basic in Week 1.**

The fastest path to productivity is understanding — not guessing.

*Your buddy is your first stop for how-we-actually-do-this questions.*  
*Your domain lead is your first stop for technical and project questions.*  
*The founder is always available for business and client questions.*

**Where to ask:**
- Slack: `#onboarding` for general questions · `#[your-domain]` for technical questions
- 1:1 with buddy — no agenda required

<!--
SPEAKER NOTES — SLIDE 14 (Questions)
This slide addresses a real psychological barrier: new hires often do not ask questions in the first week because they fear appearing incompetent. Name the fear directly — "you are not being evaluated on what you already know, you are being evaluated on how fast you learn."

The three-person contact structure gives new hires clarity about who to ask for what. Without this structure, new hires default to one person for everything — usually their manager — which creates bottlenecks and dependency.

Slack channels: create the `#onboarding` and `#[domain]` channels before the new hire starts. An empty channel is better than no channel — it shows that onboarding is a designed experience, not improvised.

The "no agenda required" note for buddy 1:1s: this is permission-giving. Many new hires interpret the absence of a scheduled meeting as "I should not bother this person." Making the informal channel explicit removes that barrier.

Model the question-asking behavior yourself: on Day 1, tell the new hire one thing you are uncertain about in the current project and how you are working to resolve it. This signals that uncertainty is normal at every level.
-->

---

<!-- _class: lead -->

# Welcome — You Belong Here

*Week 2 onboarding begins Monday.*  
*Your buddy will send you the schedule Friday afternoon.*

**SponAItech** &nbsp;|&nbsp; `sponaitech.com`

<!--
SPEAKER NOTES — SLIDE 15 (Welcome Close)
End on belonging, not on logistics. The logistics were covered in the previous slides. This closing slide is a human moment.

The phrase "You belong here" is deliberate. Research on new hire retention (Gallup, 2023) consistently shows that the single strongest predictor of 90-day retention is whether the new hire felt welcomed — not whether their tools were set up on time, not whether their 30-60-90 plan was clear. The emotional signal matters.

Deliver this slide in person if possible. If remote: turn on video, make eye contact with the camera, and pause for a moment before speaking. The pause communicates that you mean it.

What to say here: "That is the formal content. What I want you to leave today knowing is that we chose you specifically for this role, this team, and this moment. We are glad you are here. Now let's go do something that matters."

After the slide: give the new hire the remainder of Day 1 to set up their environment, re-read the CLAUDE.md, and write their first notes. Do not schedule anything else on Day 1 after the onboarding deck. Give them space.
-->
