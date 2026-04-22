<!-- TEMPLATE: faq-deck
     CATEGORY: Training / FAQ
     USE WHEN: building an explainer deck around common questions on a tool, process, or product
     SLIDE COUNT: 10
     PALETTE: Light clean
     RENDER: marp --pptx 36-faq-deck.md -->
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
  h2 { color: #0e1b2e; font-size: 1.5em; font-weight: 600; margin-bottom: 0.5em; }
  h3 {
    color: #3b9eff;
    font-size: 1.0em;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin-bottom: 0.4em;
  }
  strong { color: #0e1b2e; }
  em { color: #556677; font-style: normal; font-size: 0.88em; }
  p { line-height: 1.65; margin-top: 0.3em; }
  code { font-family: 'DM Mono', monospace; background: #f0f4f8; color: #0e1b2e; padding: 0.15em 0.45em; border-radius: 3px; font-size: 0.88em; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #8899ac; }
  section.lead h1 { font-size: 2.8em; }
  section.lead p { font-size: 1.1em; color: #556677; margin-top: 0.4em; }
  section.faq { border-top: 4px solid #3b9eff; }
  .q-label {
    display: inline-block;
    background: #3b9eff;
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 0.78em;
    font-weight: 600;
    padding: 0.2em 0.6em;
    border-radius: 3px;
    margin-bottom: 0.6em;
    letter-spacing: 0.04em;
  }
  .answer-text { line-height: 1.7; font-size: 0.97em; margin-top: 0.4em; }
  .callout { background: #f0f7ff; border-left: 4px solid #3b9eff; border-radius: 4px; padding: 0.7em 1em; margin-top: 0.8em; font-size: 0.9em; }
---

<!-- _class: lead -->

# Claude Code — Common Questions

**SponAItech Internal FAQ** &nbsp;|&nbsp; Agentic OS Enablement

*Updated April 2025 · v1.3 · Internal use only*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
This FAQ deck addresses the six most common questions that SponAItech team members ask when they first start working with Claude Code and the Agentic OS. It is designed as a self-service reference — team members can flip through it on their own or it can be delivered as a 20-minute walkthrough in a team meeting.

The questions were collected over three months of internal onboarding sessions. They represent real confusion, not invented scenarios. If you are delivering this live, acknowledge that: "These are real questions from real people on this team. There are no dumb questions in here."

The deck is updated quarterly. If a question is missing or an answer is stale, flag it to [maintainer name] via Slack `#agentic-os`. Do not assume the deck is current — check the version number at the bottom right of each slide.

For new team members: read this deck before your first Claude Code session, not after. The mental models here will save you 2–3 hours of confusion in your first week.
-->

---

<!-- _class: faq -->

<div class="q-label">Q1 — Most Asked</div>

## What Is the Difference Between a Skill and an Agent?

<div class="answer-text">

A **skill** is a set of instructions that guides how Claude approaches a specific type of task — like writing a test suite or designing an API. Claude reads the skill and applies its principles. Skills do not run independently.

An **agent** is a subagent that Claude dispatches to run a specific job in a separate context — with its own tools, model tier, and scope. Agents execute tasks and return results.

**Analogy:** a skill is a recipe; an agent is the chef sent to cook it.

</div>

<div class="callout">Use skills to shape behavior. Use agents to parallelize work.</div>

<!--
SPEAKER NOTES — SLIDE 2 (Q1 — Skills vs. Agents)
This is the most frequently asked question by new Claude Code users. The confusion is understandable — both concepts are stored in `.claude/` and both influence how Claude works. The key distinction is active vs. passive.

Expand on the analogy if the room needs it: a recipe tells a chef how to cook a dish (skill). You send a chef to a separate kitchen to cook a dish while you do something else (agent). The chef has their own tools, their own space, and returns with the finished product.

Practical implications: if you want Claude to always write tests in a specific style, that is a skill (`tdd-workflow`). If you want Claude to spin up a parallel process to review security while the main process continues building, that is an agent (`security-reviewer`).

The overlap that confuses people: some skills reference agents ("use the security-reviewer agent at G5"), and some agents load specific skills ("preload: [api-design-principles]"). They are separate abstractions that work together.

If someone in the room has tried to use a skill "to run a job" or an agent "to change Claude's behavior," gently correct the mental model here rather than during their next blocked task.
-->

---

<!-- _class: faq -->

<div class="q-label">Q2</div>

## Do I Need to Run `/sync-shared` After Every Change?

<div class="answer-text">

No. Run `/sync-shared` only when you modify a **Shared-tier asset** at the master level and want that change to appear in all five domain repos.

Run it in three situations:
- After updating a skill, agent, hook, command, or rule that is in the Shared tier
- After adding a new Shared-tier asset
- At the start of domain-specific work to confirm you are not operating on drift

Always run `--dry-run` first to see what would change before running `--apply`.

</div>

<!--
SPEAKER NOTES — SLIDE 3 (Q2 — sync-shared frequency)
The confusion here is usually about "when is something a Shared-tier asset vs. a domain-specific asset?" Quick reference: any asset in the master's `.claude/` directory is Shared and gets synced. Any asset in `domains/{domain}/.claude/` that is not in the Shared registry is domain-specific and does not sync.

The dry-run habit is important. Running `--apply` on the master without checking `--dry-run` first has caused unexpected overwrites in the past — specifically, a domain team member modified a shared skill locally to experiment, and the next master sync overwrote their changes. Always: dry-run first, review the delta, then apply.

The "start of domain-specific work" check is a good habit for consultants who jump between domains. A 30-second dry-run confirms that the domain is synchronized before you build on top of it.

If someone asks "how do I know which tier an asset is?" — answer: check the arrays at the top of `.claude/scripts/sync-shared.sh`. If the asset name appears in the `SHARED_SKILLS`, `SHARED_AGENTS`, `SHARED_COMMANDS`, `SHARED_RULES`, or `SHARED_HOOKS` arrays, it is Shared. Otherwise, it is domain-specific.
-->

---

<!-- _class: faq -->

<div class="q-label">Q3</div>

## Why Did Claude Ignore My Skill?

<div class="answer-text">

Skills activate based on their `description` field — Claude reads it to decide if the skill is relevant. If the description does not clearly match your task, the skill will not activate.

Three common causes:
1. **Weak description** — "Helps with code" activates for almost nothing; "Processes API design and route structure for FastAPI endpoints" activates reliably
2. **Missing trigger phrase** — your prompt does not contain a word the description is listening for
3. **Context exceeded** — Claude is operating beyond ~40% context and may not fully consider skill metadata

Fix: add a trigger phrase to your prompt, or invoke the skill explicitly: "Use the `api-design-principles` skill to..."

</div>

<!--
SPEAKER NOTES — SLIDE 4 (Q3 — Skill not activating)
This is the most frustrating new-user experience in Claude Code: you set up a skill, you write a prompt, and the skill is ignored. The cause is almost always the description field.

Research on Claude skill activation (from Anthropic's public Claude Code documentation and independent testing): directive descriptions achieve approximately 100% activation rate. Standard descriptions drop to around 37%. The difference is whether the description says what triggers it, not just what it does.

The context size issue is real but often overlooked. At ~40% context, Claude's attention to system prompt content degrades. If you are deep into a long session and skills stop activating, it is time to wrap up and start a new session.

The explicit invocation ("Use the X skill to...") is a reliable workaround for any activation issue. It does not require modifying the skill — it simply tells Claude directly which skill to load and apply. This is especially useful in situations where the task is ambiguous and the skill description cannot be made arbitrarily specific.

Maintenance note: if a skill consistently fails to activate for its intended use case, that is a signal to improve its description. Log it in the skill's `_learnings.md` file so the next `/evolve-skills` run picks it up.
-->

---

<!-- _class: faq -->

<div class="q-label">Q4</div>

## What Happens If I Forget to Write a Session Handover?

<div class="answer-text">

Your work does not disappear — but the next session (yours or someone else's) starts from scratch without context. This creates two risks:

- **Duplicated work** — the next session re-explores decisions already made
- **Lost decisions** — architectural choices and blockers that were in your head are not captured

The `session-wrapup.sh` hook will remind you at session end. If you miss it anyway: write the handover at the start of the next session before doing any new work. Better late than never.

</div>

<div class="callout">Handover quality = your team's ability to continue your work without you.</div>

<!--
SPEAKER NOTES — SLIDE 5 (Q4 — Forgetting the handover)
This question usually comes from someone who has already missed a handover and experienced the consequences. Be empathetic — it happens to everyone. The goal is to make the habit so low-friction that it becomes automatic.

The "write it at the start of the next session" advice is practical. The alternative — "you lose the work" — is overstated. The work is in the repo. What is lost is the decision context: why did you choose this approach? What did you try that did not work? What is the next step? These are the things that are expensive to reconstruct.

The callout at the bottom ("Handover quality = your team's ability to continue your work without you") is a reframe that resonates with people who care about their colleagues. It shifts the handover from "bureaucratic overhead" to "professional courtesy."

For SponAItech specifically: as a lean operation, the handover is not optional. If the person who owns a client project is unavailable for any reason, the handover is the only continuity mechanism. A missing handover on a client project is a business risk, not just a process miss.

The session-wrapup hook: it runs at session end and checks whether a handover has been written. It exits with a warning (exit 1) if the handover is missing — it does not block, but it does surface the reminder. If the hook is not running, check your `.claude/settings.json` configuration.
-->

---

<!-- _class: faq -->

<div class="q-label">Q5</div>

## Can I Use Claude to Generate Client-Deliverable Documents?

<div class="answer-text">

Yes — with three conditions:

1. **Human review required** — every AI-generated deliverable must be reviewed and approved by a team member before it reaches the client
2. **Use the `demo-preparer` agent** — it is calibrated for client-facing tone, SponAItech branding, and non-technical audiences
3. **Disclose appropriately** — SponAItech's policy is transparent AI use; if a client asks whether AI was involved, the answer is yes

What Claude is excellent at: first drafts, structure, formatting, and consistency. What requires human judgment: accuracy of technical claims, tone calibration for the specific client, and content that requires domain expertise to verify.

</div>

<!--
SPEAKER NOTES — SLIDE 6 (Q5 — Client deliverables)
This question reflects a real tension: AI-generated output is fast and often very good, but it carries risks for client-facing work. The three conditions balance speed with accountability.

Condition 1 (human review): the output is only as good as the human who reviews it. If the reviewer does not have enough domain knowledge to catch a factual error in a technical deliverable, the review is theatrical rather than real. Match the reviewer's expertise to the document's technical depth.

Condition 2 (demo-preparer agent): this agent is scoped and calibrated for SponAItech's client-facing voice — professional but approachable, results-first, no jargon. Using it for client deliverables rather than an unguided Claude session ensures brand consistency.

Condition 3 (disclosure): SponAItech's transparency policy is a differentiator. Clients who know we use AI and trust us anyway are more engaged clients. Do not hide AI involvement — own it and explain the review process. "We used AI to draft this and our team reviewed every claim" is a credible answer. "We wrote it ourselves" when you did not is a trust risk.

The distinction between what AI does well and what requires human judgment is the most important thing to internalize. Claude is an accelerator for first drafts, not a replacement for expertise.
-->

---

<!-- _class: faq -->

<div class="q-label">Q6</div>

## How Do I Know When to Use Opus vs. Sonnet vs. Haiku?

<div class="answer-text">

The model-routing-policy rule has the full table. Quick reference:

| Task type | Model | Cost/M input |
|---|---|---|
| Classification, extraction, formatting | **Haiku** | ~$0.25 |
| Code review, research, multi-turn reasoning | **Sonnet** | ~$3 |
| Architecture, security audit, strategy design | **Opus** | ~$15 |

**Default for day-to-day work:** Sonnet.  
**Default for complex design or compliance-critical:** Opus.  
**Default for batch operations and read-only research:** Haiku.

</div>

<!--
SPEAKER NOTES — SLIDE 7 (Q6 — Model selection)
The model-routing-policy rule is the authoritative source. This FAQ slide gives people a quick mental model without requiring them to read the full policy first.

The cost difference is important context. Opus is 60× more expensive per input token than Haiku. For a 10,000-token context window: Haiku costs about $0.003, Sonnet about $0.03, Opus about $0.15. At scale — hundreds of agent calls per day — these differences are meaningful.

The "day-to-day default is Sonnet" guidance prevents both over-spending (routing everything to Opus) and under-performing (routing everything to Haiku). Sonnet is the right balance for most code-related work.

Two common mistakes to call out: using Opus for tasks like "summarize this document" (Haiku does this fine at 1/60th the cost), and using Haiku for architecture decisions (under-performs because the reasoning surface is too complex for a speed-optimized model).

The SponAItech monthly budget is $100–500. If team members default to Opus for everything, the budget will be exhausted before mid-month. Model discipline is a budget responsibility, not just a performance preference.

If anyone wants to verify which model an agent uses: check the `model:` field in the agent's `.md` file in `.claude/agents/`. The absence of a model field means it inherits from the session default.
-->

---

## Still Have Questions?

**Check these first:**

- ● `CLAUDE.md` in your domain — covers conventions and workflow
- ● `_learnings.md` in the relevant skill — covers known issues and workarounds
- ● `memory/project_session_handover.md` — recent session context

**Ask a human:**

- Slack `#agentic-os` — for framework questions (skills, agents, sync)
- Slack `#[your-domain]` — for domain-specific questions (Apex, FastAPI, EasyLanguage)
- Your domain lead — for anything that could affect a client deliverable

*If your question is not in this FAQ, it probably belongs in it — send it to [maintainer]*

<!--
SPEAKER NOTES — SLIDE 8 (Still Have Questions?)
This slide exists to prevent the "I am stuck but do not know where to ask" paralysis. Give people explicit channels for explicit question types.

The "check these first" list is not gatekeeping — it is efficiency. 80% of questions from new team members are answered in the domain's CLAUDE.md or in skill `_learnings.md` files. Encouraging self-service first respects everyone's time, including the asker's.

The "send it to [maintainer]" instruction at the bottom is how this FAQ grows. Replace [maintainer] with the specific person or channel responsible for the FAQ deck before distributing. An unmaintained FAQ is worse than no FAQ — it creates false confidence in stale information.

For live delivery: end this slide by asking the room "What question do you have that is not in this FAQ?" Take 2–3 answers. If they are good candidates for the FAQ, say so and commit to updating it. Then actually update it.

The Slack channel naming convention: `#agentic-os` is for framework-level discussions. Domain channels (`#salesforce`, `#python-apps`, `#trading`, `#ios`) are for domain-specific technical questions. Client-specific channels are created per project. If someone is not in the right channel, invite them — do not just redirect them.
-->

---

## Resources — Learn More

**Official documentation:**
- Claude Code documentation — code.claude.com/docs
- Anthropic platform docs — platform.claude.com/docs

**Internal resources:**
- Claude Code official documentation — code.claude.com/docs
- Anthropic skill-creator reference — platform.claude.com/docs
- Your team's own CLAUDE.md at the repo root
- Your team's internal skill / agent authoring standards (if any)

**Training track:**
- New hire onboarding (this series) — Module 1 → 2 → 3 → 4 → 5
- Certification: Salesforce ADM 201, Azure Fundamentals AZ-900

<!--
SPEAKER NOTES — SLIDE 9 (Resources)
The internal resource paths are absolute paths relative to the master OSofOS directory. Verify they are correct for the local machine or repository structure before distributing this deck.

The Claude Code documentation URL: verify this is current before each use of this deck. Anthropic's documentation structure has changed in the past — a broken link in a FAQ resources slide is a credibility issue.

The training track at the bottom: fill in the actual module names before distributing. The "Module 1 → 2 → 3 → 4 → 5" placeholder should reference the specific modules in the SponAItech new hire training series.

For the certification track: the certifications listed (ADM 201, AZ-900) are the minimum certifications for SponAItech team members in the Salesforce and Custom Apps domains. Trading and iOS domains have domain-specific certifications — reference the appropriate track for those team members.

If this deck is being shared externally (e.g., with a client team learning to use Claude Code): remove the internal resource paths and the certification track. Replace with equivalent external resources. The internal structure of SponAItech's Agentic OS is proprietary.
-->

---

<!-- _class: lead -->

# FAQ Version Log

*v1.0 — Initial release — January 2025*  
*v1.1 — Added Q5 (client deliverables) — February 2025*  
*v1.2 — Updated Q6 with Haiku pricing — March 2025*  
*v1.3 — Added resource links · Updated Q3 context guidance — April 2025*

*Next review: July 2025 · Maintainer: [name]*

<!--
SPEAKER NOTES — SLIDE 10 (Version Log)
The version log is a trust signal. It tells readers that this document is actively maintained, not abandoned. Every time a question is added or an answer is updated, log it here with the month and year.

The version log also helps readers who have seen a previous version understand what changed. If Q3 was updated, a reader who memorized the old answer will know to re-read it.

For the maintainer: schedule a quarterly review calendar event for this deck. The review takes 30 minutes: check each answer against current behavior, verify all links, check if any new questions have come up in Slack that belong in the FAQ, and update the version log.

The "Next review: July 2025" date should be updated every time you publish a new version. If it says a date in the past, update it. A stale review date signals neglected content.

Replace [name] with the actual maintainer before distributing. An FAQ without a named maintainer is an FAQ that no one feels responsible for.
-->
