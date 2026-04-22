# /first-principles — Apply First-Principles Reasoning

> **Tier:** Shared
> **Skill:** `first-principles`
> **Model tier:** Opus (accuracy-critical)

Invoke the 4-phase first-principles pipeline on a topic: **Deconstruct → Challenge Assumptions → Reconstruct (3 alternatives) → Pre-mortem Stress-test**. Produces a versioned `first-principles-analysis_v{N}.md` with Mermaid decomposition tree, frozen/challengeable assumption tables, 3-alternative comparison, counter-arguments, and cognitive-bias sweep.

**When to use:** strategic decisions, contested internal views, board-level research, architecture where convention may be wrong, any "why do we believe this?" moment.

**When NOT to use (skill will auto-decline):** production hotfixes, well-solved problems, taste/preference decisions, pure speculation with no evidence.

## What to do

### Step 1 — Parse the topic
If `$ARGUMENTS` names a topic, use it directly. Otherwise ask the user: *"What topic should I apply first-principles to?"* — one sentence.

### Step 2 — Decline check
Run the 4-case decline check from `SKILL.md` §"When NOT to Use". If the topic fits a decline case, say so and offer the suggested redirect. Proceed only if the user confirms.

### Step 3 — Classify complexity + set depth
Default depth cap: 5 decomposition layers. Adjust using topic-driven auto-depth per `SKILL.md` Phase 1. Announce the plan to the user in one short paragraph before Phase 1.

### Step 4 — Run the 4-phase pipeline
Per `SKILL.md` Phases 1–4. At each phase exit, offer the user an AskUserQuestion escape hatch: **proceed / stop here / skip to output**. For Executive Advisor OS contexts, add the Executive Advisor OS integration AskUserQuestion rounds per `SKILL.md` §"Executive Advisor OS Integration".

### Step 5 — Produce the artifact
Use `templates/first-principles-analysis-template.md` as the skeleton. Write to:
- Executive Advisor OS context: `research/{slug}/output/first-principles-analysis_v{N}.md`
- Dev-domain work item: `memory/projects/{domain}/{project}/features/{WORK-ITEM-ID}/first-principles-analysis_v{N}.md`
- Ad-hoc: the path the user specifies, or the current working folder

If the output crosses 300 lines, follow `.claude/rules/large-artifact-generation.md` — plan → chunk → merge → review.

### Step 6 — Enrich dependent outputs (Executive Advisor OS only)
When invoked inside Executive Advisor OS Strategic-deep tier, also enrich:
- `executive_summary_v{N}.md` — add axioms + chosen alternative + top counter-argument to the opening paragraph
- `briefing_v{N}.html` — add expandable "How we got here" appendix (exec palette)
- `deck_detailed_v{N}.md` — add "Decision rationale" slide

### Step 7 — Confirm completion
Report: artifact path, byte size, phases completed, bias sweep results, and any phase where the user used the escape hatch.

## Important

- **Never skip phases.** All 4 run in order.
- **Never overwrite versions.** v1 is never touched once v2 exists.
- **Always include a Counter-arguments section** in the output.
- **Inside Executive Advisor OS: respect the research-scope rule.** Never propose building systems, tools, or workflows, even when the decomposition surfaces an implementation option. See `domains/executive-advisor-os/CLAUDE.md` Rules 6 and 11.
- **Name the method to the user** when running inside Executive Advisor OS. Transparency is mandatory.
- **Opus-tier default.** Only downgrade Phases 1 and 4 to Sonnet under explicit budget pressure. Phases 2 and 3 stay at Opus.

$ARGUMENTS
