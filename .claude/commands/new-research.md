# /new-research — Start a New Research Topic

> **Tool:** Claude Code slash command
> **Skills:** html-generation, deck-generation
> **Key dependency:** `AskUserQuestion` tool for structured clarification rounds

Start a fresh research topic. Name the folder, ask the 3 core questions in free text, then run as many structured `AskUserQuestion` rounds as the research complexity warrants. Ingest documents. Deliver versioned outputs. Memory and dashboard are always reconciled at the end.

## What to do

### Step 1 — Get the topic (free text)
Ask: *"What are you working on? One sentence is enough to start."*

### Step 2 — Slug + folder
Generate a 2–4 word kebab-case slug. Create:
```
research/{slug}/
├── .memory/
│   ├── handover.md
│   └── session-log.md
└── output/
```

### Step 3 — Ask the 3 core questions (free text, conversationally)
1. End goal — what decision or action does this serve?
2. Primary audience?
3. Documents to drop in?

If documents are provided → read them FULLY before any structured round.

### Step 4 — Classify complexity
After the core answers (and any documents), classify the research: **Simple | Standard | Complex | Strategic-deep** using the rubric in `CLAUDE.md`. Default to one tier higher when unsure.

### Step 5 — Run structured clarification rounds with AskUserQuestion

- Ask permission once: *"I'd like to run a structured set of clarifying questions so I can sharpen the research. A few quick rounds — okay?"*
- Then run clarification rounds per the complexity tier:
  - **Simple:** 1 round (2–4 questions)
  - **Standard:** 2 rounds (5–8 total)
  - **Complex:** 3–5 rounds (9–16 total)
  - **Strategic-deep:** 5+ rounds, no ceiling — keep going until clarity is real
- **Each round = one `AskUserQuestion` tool call** with up to 4 questions. Each question has 3–5 multiple-choice options plus "Other / I'll type it".
- Group related questions into one round (audience + tone + depth together; stakeholders + champion + pushback together).
- After each round: one-sentence acknowledgement, decide whether another round is needed. Do NOT re-ask permission between rounds.
- Stop immediately if the executive says "enough, let's go".

See `CLAUDE.md` Step 3 for the full question bank (positioning, stakeholders, timing, audience calibration, scope/boundaries).

### Step 6 — Ask what outputs they need
Use AskUserQuestion here too: list each output type as a yes/no question, or one multi-select question listing all formats. Always generate executive summary by default.

Options: executive summary (always), detailed analysis, deck summary (≤3 slides), deck detailed (10–12 slides), HTML briefing.

### Step 6.5 — (Strategic-deep only) Auto-invoke `first-principles`
If the complexity classification from Step 4 was **Strategic-deep**, invoke the `first-principles` skill BEFORE generating any outputs. Name the method to the executive in conversation first — *"This is a Strategic-deep topic. I'm going to apply first-principles thinking…"* — then run its 4-phase pipeline (Deconstruct → Challenge Assumptions → Reconstruct 3 alternatives → Pre-mortem). The skill will add its own AskUserQuestion rounds at each phase boundary (question re-frame confirmation, frozen assumption gate, axis check, failure-review). The analysis is written to `research/{slug}/output/first-principles-analysis_v1.md` and will feed the four enrichment points in Step 7.

Respect every existing guardrail: Executive Advisor OS scope rule (never propose building), large-artifact rule (plan → chunk → review), paralysis guards (max depth 5, escape hatches at each phase). Opus-tier default.

### Step 7 — Research, analyze, generate at v1
- Synthesize across documents + bring in relevant external context
- Map findings to the executive's end goal and audience
- Use `html-generation` skill for `briefing_v1.html` (must follow `.claude/rules/large-artifact-generation.md` — plan-in-MD → chunk → merge → review)
- Use `deck-generation` skill for any deck output (decks > 3 slides also follow the large-artifact rule)
- **Strategic-deep enrichment** — if first-principles ran in Step 6.5:
  - `executive_summary_v1.md` opens with key axioms + chosen alternative + top counter-argument
  - `briefing_v1.html` gains a collapsed "How we got here" appendix at the end (exec palette, Mermaid tree, assumption tables, 3-alternative comparison, counter-arguments)
  - `deck_detailed_v1.md` gains a "Decision rationale" slide
- Write to `research/{slug}/output/`

### Step 8 — Reconcile memory + regenerate dashboard
Non-negotiable per `CLAUDE.md`. Update `.memory/handover.md` + `session-log.md`, then regenerate `research/dashboard.html`.

## Important
- **No question cap on complexity.** Strategic-deep has no ceiling. Keep going until you understand the research picture.
- **Use AskUserQuestion for every clarification round** in Standard+ tiers (not free-form prose questions).
- **Versions never overwrite** — always start at v1.
- **Dashboard regeneration is part of task completion**, not a separate step.
- **Stay strictly in research scope.** Never propose building, designing, implementing, or scoping tools / systems / dashboards / workflows — even if the executive pushes. Research and reports only. If they push to build: *"I'm the research assistant — for implementation you'd want a build workflow. Want me to research what the build would involve?"* See CLAUDE.md Rule 11.

$ARGUMENTS
