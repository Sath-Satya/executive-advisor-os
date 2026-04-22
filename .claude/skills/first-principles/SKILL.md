---
name: first-principles
description: Rigorous first-principles reasoning for strategic research, architectural decisions, and high-stakes planning. Runs a 4-phase pipeline — Deconstruct → Challenge Assumptions → Reconstruct from axioms → Stress-test via pre-mortem — using Aristotelian, Cartesian, Feynman, and Musk/5-Whys decomposition plus Munger, systems-thinking, Bezos, and Bayesian mental models. Surfaces buried assumptions with confidence scores, enumerates 3 alternatives, runs counter-arguments, and flags frozen (unchallengeable) constraints. Auto-triggers when the user says "challenge my assumptions", "go back to basics", "rethink this from scratch", "what are we really solving", "is this the right question", "first principles", or "why do we believe this". Auto-runs inside Executive Advisor OS /new-research for Strategic-deep complexity tier. Opus-tier accuracy-critical skill. Produces a versioned first-principles-analysis_v{N}.md plus Mermaid decomposition tree. Large artifacts follow `.claude/rules/large-artifact-generation.md`.
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep, AskUserQuestion]
---

# First-Principles Thinking

## When to Use

Invoke this skill when the user needs to break a problem down to its fundamental truths and rebuild a defensible answer, rather than reasoning by analogy or convention. Strong fits:

- **Executive research** — board-level, regulatory, multi-stakeholder, or financially material topics. Auto-runs inside `/new-research` when Executive Advisor OS classifies the research as **Strategic-deep** tier.
- **Architecture decisions** — when the team's default is "we've always done it this way" and the cost of being wrong is high.
- **Strategic choices** — build vs buy, enter/exit market, M&A, major policy shift, multi-year bets.
- **Contested internal views** — when stakeholders disagree and the disagreement is traceable to different unstated assumptions.
- **"Why do we believe this?"** — when the user or exec asks a question that implies the current framing may itself be wrong.

## When NOT to Use (decline cases)

The skill MUST recognize these non-fit cases and explicitly decline, offering a better path:

| Case | Signal | Redirect |
|---|---|---|
| **Urgent / hotfix** | Minutes or hours to decide; production down | "First-principles takes time. Want a fast-path recommendation and we book first-principles for the post-mortem?" |
| **Well-solved problem** | The answer is widely documented and not in dispute | "This is a solved problem — standard answer is X. Want first-principles anyway, or use the standard?" |
| **Taste / preference** | Decision is primarily aesthetic or values-based | "First-principles doesn't decide taste. Want a frameworks-based comparison instead?" |
| **Insufficient evidence** | All inputs are speculation; no grounded data | "This is scenario territory. A structured scenario analysis will serve better than first-principles from speculation." |

If the user insists after a decline, honor the request and proceed — but note in the output that the skill flagged the fit mismatch.

## The 4-Phase Pipeline

Every invocation runs exactly these four phases, in order. Each phase has an explicit exit and an **escape hatch** letting the user stop or skip to output.

```mermaid
flowchart LR
    A[Phase 1<br/>Deconstruct] --> B[Phase 2<br/>Challenge<br/>Assumptions]
    B --> C[Phase 3<br/>Reconstruct<br/>3 Alternatives]
    C --> D[Phase 4<br/>Pre-mortem<br/>Stress-test]
    D --> E[Output<br/>first-principles-analysis_v{N}.md]
```

**Depth is topic-driven.** The skill auto-calibrates depth based on complexity signals (financial magnitude, regulatory exposure, multi-stakeholder contestation, multi-year horizon). Default cap: **5 decomposition layers**. Only go deeper on explicit user request.

**Escape hatches** at each phase boundary: `proceed / stop here and write what we have / skip to output`.

---

## Phase 1 — Deconstruct

**Goal:** Identify the REAL question, not the surface question. Strip it down to named components using four lenses, applied in sequence.

### 1.1 Re-frame the question (Feynman)
Re-state the user's problem in plain language, as if explaining it to someone with no domain context. Gaps in the re-statement reveal hidden scope. Ask the user to confirm the re-framing before proceeding.

### 1.2 Categorical decomposition (Aristotelian)
Break the re-framed question across six categories:
- **Substance** — what is the thing itself?
- **Quality** — what attributes define it?
- **Quantity** — what magnitudes matter? (dollars, users, time, risk)
- **Relation** — what does it depend on, what depends on it?
- **Time** — what is the horizon? reversibility?
- **Place** — what is the scope boundary? (geography, market, org unit)

Drop categories that don't apply to the topic. Do not force every bucket to be populated.

### 1.3 Constraint drill (Musk / 5-Whys)
For each material component from 1.2, ask "why does this constrain us?" repeatedly until the answer is:
- A law of physics / math
- A regulatory or contractual requirement
- A specific stated executive preference
- A grounded empirical fact with evidence

Tag each terminal answer as an **axiom candidate**. Stop at 5 layers deep unless the user approves going deeper (paralysis guardrail).

### 1.4 Cartesian doubt pass
For every axiom candidate from 1.3, explicitly ask: "Is this actually self-evident, or am I assuming it?" Anything that fails this test drops back into the assumption pool for Phase 2.

### Phase 1 exit
Summarize the decomposition to the user as a Mermaid left-to-right tree. Offer the escape hatch: **proceed / stop / skip to output**.

---

## Phase 2 — Challenge Assumptions

**Goal:** Inventory every assumption (explicit and implicit), score its defensibility, and challenge the soft ones.

### 2.1 Build the assumption inventory
Extract assumptions from:
- User's problem statement
- Documents provided (if any)
- Industry defaults Claude inferred (tag these **INFERRED** with a note)
- Axiom candidates that failed Cartesian doubt in Phase 1

Format:

| # | Assumption | Source | Frozen? | Confidence | Evidence |
|---|---|---|---|---|---|
| 1 | Example: "Members won't switch plans mid-year" | User statement | No | Medium | Historical churn data ~3%/yr |
| 2 | Example: "Regulatory deadline is 2026-12-31" | CMS final rule | YES | High | CMS-2026-XXXX-F §12.3 |

**Confidence rubric (qualitative with evidence links):**
- **High** — grounded in law, regulation, contract, or robust data
- **Medium** — industry convention, reasonable empirical backing
- **Low** — inferred, conventional, or single-source
- **Speculative** — no evidence, Claude or user inference only

### 2.2 Frozen-assumption confirmation gate
Before running Cartesian challenge, ask the user (via **AskUserQuestion**) to confirm which assumptions are FROZEN (regulatory, contractual, political, ethical, or explicit executive preference). Frozen assumptions are NOT challenged — they are boundaries.

Produce two tables in the output: **Frozen (work within)** and **Challengeable (tested below)**.

### 2.3 Challenge every non-frozen assumption
For each challengeable assumption, answer: **"What if this is wrong — what changes?"** Add a what-if-wrong column to the inventory. Assumptions whose reversal materially changes the recommendation are flagged as **load-bearing**.

### 2.4 Frozen-thaw sidebar
For the top 2–3 frozen assumptions, add a sidebar note: *"If this later thaws, the recommendation shifts toward X."* Useful for multi-year horizons and policy-sensitive topics.

### Phase 2 exit
Present the full assumption inventory + frozen confirmation to the user. Flag load-bearing assumptions explicitly. Escape hatch offered.

---

## Phase 3 — Reconstruct

**Goal:** Build three distinct paths forward from axioms + frozen boundaries, compare them, and recommend one.

### 3.1 Generate three alternatives
Pick the axis that best fits the topic:

- **Temperament axis** — Conservative / Balanced / Aggressive
- **Change axis** — Status-quo / Incremental / Transformative
- **Horizon axis** — Short-term / Medium-term / Long-term

For each alternative, construct the path: what is done, in what order, under what conditions, at what cost.

### 3.2 Apply mental models during construction
- **Munger's latticework** — check each alternative against inversion ("what would guarantee failure?"), opportunity cost, circle of competence, incentive alignment. Flag Lollapalooza risks.
- **Systems thinking** — map feedback loops and delays. Identify leverage points and unintended second-order effects.
- **Bezos** — tag each alternative: reversible (two-way door) or irreversible (one-way door). For one-way doors, raise the evidence bar.
- **Bayesian** — state the prior probability of each alternative succeeding; identify the evidence that would update the prior.

### 3.3 Comparison table
Mandatory output table:

| Dimension | Alt A | Alt B | Alt C |
|---|---|---|---|
| Cost / effort | | | |
| Time to value | | | |
| Reversibility (one-way / two-way) | | | |
| Load-bearing assumptions | | | |
| Prior success probability | | | |
| Key risk | | | |
| Delta vs status quo | | | |

### 3.4 Recommend + justify
Select one alternative. Justify the selection **only** in terms of the axioms, frozen boundaries, and load-bearing assumptions established in Phases 1–2. No new premises introduced here.

### Phase 3 exit
Present the 3 alternatives, comparison table, and recommendation. Escape hatch offered before stress-testing.

---

## Phase 4 — Pre-mortem Stress-test

**Goal:** Assume the recommendation FAILED two years from now. Work backward to discover why.

### 4.1 The pre-mortem prompt
*"It is two years from now. The recommendation was executed. It has spectacularly failed. Write the autopsy — what went wrong, and when was it already inevitable?"*

Produce 5–7 distinct failure modes, ranked by plausibility.

### 4.2 Counter-arguments section (mandatory)
For each top failure mode, write the strongest version of the objection against the recommendation — steel-manned. Show how the analysis survives it, or flag that it doesn't.

Every output MUST have a dedicated **Counter-arguments** section. No exceptions.

### 4.3 Cognitive-bias sweep
Before finalizing, check for the four named biases:
- **Anchoring / availability** — is the recommendation anchored to a vivid recent example or a first-mentioned number?
- **Sunk cost / status quo** — is "we already invested" or "we've always done it" load-bearing?
- **Confirmation / motivated reasoning** — did I select evidence to support a pre-existing view?
- **Planning fallacy / overconfidence** — are the timelines, costs, or impact estimates realistic?

Flag every detected bias in the output with the mitigation applied.

### Phase 4 exit
Pre-mortem + counter-arguments + bias sweep complete. Proceed to output generation.

---

## Output Format

### Primary artifact
`first-principles-analysis_v{N}.md` — written to the caller's working folder (e.g., `research/{slug}/output/` for Executive Advisor OS, `memory/projects/{domain}/{project}/features/{WORK-ITEM-ID}/` for dev-domain work items).

Structure (use the template at `templates/first-principles-analysis-template.md`):

1. Topic + re-framing
2. Mermaid decomposition tree (left-to-right)
3. Assumption inventory — **Frozen** + **Challengeable** tables
4. Three alternatives + comparison table
5. Recommendation + justification tied to axioms
6. Pre-mortem — 5–7 failure modes
7. **Counter-arguments** (dedicated section, always present)
8. Cognitive-bias sweep results
9. Reasoning trace (which framework applied where)
10. Frozen-thaw sidebar (if applicable)

### Versioning
Never overwrite. Every new session increments v{N}.

### Large artifact compliance
Whenever this output exceeds 300 lines or expected size > 40 KB, the caller MUST follow `.claude/rules/large-artifact-generation.md` — plan-in-MD first → chunked build → Step-4 review checklist.

---

## Executive Advisor OS Integration

### Auto-trigger
When Executive Advisor OS's `/new-research` classifies the research as **Strategic-deep** tier, this skill auto-runs **after** Executive Advisor OS's clarification rounds complete and **before** output generation. The exec is told explicitly:

> *"This is a Strategic-deep topic. I'm going to apply first-principles thinking — deconstruct the question, challenge assumptions, build three alternatives, and stress-test the recommendation. Here's the decomposition tree for the first phase…"*

Transparency is mandatory. Never run this skill silently inside Executive Advisor OS.

### Extra AskUserQuestion rounds
First-principles adds its own AskUserQuestion rounds beyond Executive Advisor OS's standard clarification:

- **Phase 1 exit:** confirm the re-framed question; approve the decomposition tree
- **Phase 2 gate:** confirm the frozen-assumption list
- **Phase 3 exit:** any alternative should be excluded? any axis override?
- **Phase 4 review:** any failure mode feels missing?

Same AskUserQuestion UX as Executive Advisor OS's clarification rounds (multiple-choice + "Other").

### Exec-friendly question language (MANDATORY inside EA OS)

When this skill runs inside Executive Advisor OS, every AskUserQuestion round MUST follow `.claude/rules/exec-friendly-clarification.md`. The framework vocabulary stays in the analyst's working notes and the `first-principles-analysis_v{N}.md` artifact — it does NOT appear in the question pane the executive sees.

**Rewrites required on the four phase-exit questions:**

| Phase | ❌ Framework-jargon version | ✅ Exec-friendly version |
|---|---|---|
| Phase 1 exit | "Does the Feynman re-framing capture your real ask?" | "Does this re-statement of the research question capture what you actually want answered?" |
| Phase 2 gate | "Which assumptions are FROZEN (not challenged)?" | "Which of these are hard boundaries we can't change (regulation / contract / explicit exec preference)?" |
| Phase 2 gate | "Which assumptions are load-bearing?" | "Which of these beliefs would materially change the recommendation if they turned out to be wrong?" |
| Phase 3 exit | "Is any alternative strawman-thin?" | "Are any of the three options weak or unrealistic — if so, which should I replace?" |
| Phase 3 exit | "Any axis override?" | "Should we compare the three paths along a different dimension — e.g., by speed, by spend level, or by build-vs-buy posture?" |
| Phase 4 review | "Any counter-argument not steel-manned strongly enough?" | "Any likely board or leadership objection that isn't addressed strongly enough in the analysis?" |
| Phase 4 review | "Any failure mode missing from the pre-mortem?" | "Any way this path could realistically fail that we haven't named yet? *(A pre-mortem imagines it's 2 years out and the path failed — what went wrong?)*" |

**Inline references when a mental model is named:**

When Phase 3 or Phase 4 question phrasing genuinely benefits from naming a mental model, attach a brief parenthetical definition on first use in that message:
- pre-mortem *(imagining failure 2 years from now to surface risks now)*
- inversion *(instead of asking 'how do we succeed?', ask 'how would we most guarantee failure?')*
- one-way door *(a decision that's hard or impossible to reverse once made)*
- two-way door *(a decision you can walk back from)*
- steel-man *(the strongest possible version of the objection — opposite of a strawman)*
- 5-Whys *(drill down by asking 'why?' five times until you hit a root cause)*
- systems feedback loop *(a reinforcing or balancing cycle where output feeds back into input)*
- prior *(your rough estimate of a path's success probability before seeing evidence)*

The analyst's full artifact (`first-principles-analysis_v{N}.md`) continues to use the framework vocabulary directly — that artifact is for audit, not for the executive's primary reading surface.

### Output enrichment — four touch points
1. **New standalone artifact** — `first-principles-analysis_v{N}.md` alongside `executive_summary_v{N}.md`, `briefing_v{N}.html`, etc.
2. **Executive summary enrichment** — the top-of-summary paragraph cites the key axioms, the chosen alternative, and the top counter-argument. Does not duplicate the full analysis — references it.
3. **HTML briefing appendix** — `briefing_v{N}.html` gains a collapsed "How we got here" section at the end containing the Mermaid tree, assumption tables, 3-alternative comparison, and counter-arguments. Styled in exec palette (cream / navy / gold). Expandable on click.
4. **Detailed deck slide** — `deck_detailed_v{N}.md` gains one "Decision rationale" slide showing the reasoning structure in condensed form. Presenter notes link to the full MD artifact.

### Visual styling
All first-principles visual elements inside Executive Advisor OS outputs match the executive palette:
```
--cream: #f7f4ef  --navy: #0e1b2e  --gold: #b8965a
--ink: #1c1a18  --muted: #6b6560  --border: #ddd8ce
```

Mermaid trees render left-to-right with subtle gold edge-color on load-bearing paths.

### Executive Advisor OS scope compliance (overrides all)
This skill MUST respect Executive Advisor OS's research-scope rule. When running inside Executive Advisor OS:
- Never propose building systems, tools, dashboards, workflows, code, or procurement
- If a decomposition branch surfaces an implementation option, acknowledge it as a research angle and redirect — do NOT draft specs, architectures, or project plans
- Inherits `domains/executive-advisor-os/CLAUDE.md` Rules 6 and 11 (stay in scope; never fold when pressed)

---

## Paralysis Guardrails

Four simultaneous guards prevent the skill from spiraling into over-analysis:

1. **Max-depth cap** — decomposition stops at 5 layers deep. User must explicitly request more to override.
2. **Time-box signal** — after significant token burn on one phase, the skill asks "more depth here, or move on?" — gives an escape without forcing one.
3. **Signal-to-noise check** — before going deeper on any branch, ask: *"Does this change the recommendation?"* If no, prune the branch.
4. **Exec escape hatch** — at the end of every phase: `proceed / stop here and write what we have / skip to output`.

If the user says "that's enough" at any point, stop immediately and write what we have. Note the early stop in the output.

---

## Cost & Model Routing

- **Default tier:** Opus for all four phases. This skill is accuracy-critical reasoning per `.claude/rules/model-routing-policy.md` Tier 3.
- **Budget override:** If monthly spend approaches the `$500/mo` ceiling, the caller may route Phase 1 and Phase 4 to Sonnet. Phases 2 and 3 (Challenge and Reconstruct) must stay at Opus. Log every downgrade in the reasoning trace.
- **Never downgrade to Haiku.** The skill's value collapses at Haiku-tier reasoning.

---

## Must Do

- Apply all **4 decomposition frameworks** (Aristotelian, Cartesian, Feynman, Musk/5-Whys) in Phase 1
- Apply all **4 mental models** (Munger, Systems, Bezos, Bayesian) during Phase 3 reconstruction
- Run all **4 bias checks** (anchoring, sunk-cost, confirmation, planning-fallacy) in Phase 4
- Produce the **Frozen** and **Challengeable** assumption tables separately
- Produce exactly **3 alternatives** with the full comparison table
- Always include a dedicated **Counter-arguments** section in the output
- Tag **INFERRED** on any axiom Claude constructed without user/document evidence
- Record a **reasoning trace** in the output showing which framework was applied where
- Respect `.claude/rules/large-artifact-generation.md` when output crosses thresholds
- Inside Executive Advisor OS: respect Executive Advisor OS's research-scope rule (Rule 6 + Rule 11)

## Must Not Do

- Never skip phases. All 4 run in order.
- Never overwrite prior versions (v1 is never touched once v2 exists)
- Never re-derive FROZEN assumptions — work within them
- Never propose more than 3 alternatives in Phase 3 (forces prioritization)
- Never claim an assumption is "self-evident" without passing Cartesian doubt
- Never treat Claude-inferred axioms as ground truth — always tag INFERRED
- Inside Executive Advisor OS: never propose building, designing, or implementing anything
- Never run this skill silently inside Executive Advisor OS — always name the method to the exec
- Never downgrade to Haiku-tier reasoning

---

## Common Failure Modes

1. **Over-decomposition** — drilling past the 5-layer cap without user approval. Mitigation: hard cap + signal-to-noise check.
2. **Assumption blindness** — missing an assumption because it's "obvious". Mitigation: INFERRED tagging + documents-first read.
3. **Fake alternatives** — producing 3 options where 2 are strawmen. Mitigation: each alternative must pass Bezos reversibility + Bayesian prior check.
4. **Motivated reconstruction** — reaching for a pre-determined recommendation. Mitigation: Cartesian doubt in Phase 1 + bias sweep in Phase 4.
5. **Pre-mortem theater** — listing 5 failure modes that all trace to the same root cause. Mitigation: require distinct failure mechanisms.
6. **Scope creep in Executive Advisor OS** — drifting into "should we build a tool to track this?" Mitigation: Executive Advisor OS scope rule hard-override; delete and return to research.

## Reference

Deep-dive reference on every framework is in `reference/frameworks.md` — **loaded only when this skill is actively running**, not at session discovery. Covers:
- Full Aristotelian categories and usage patterns
- Cartesian doubt applied to modern business premises
- Feynman technique worked examples
- Musk/5-Whys in aerospace, healthcare, and software
- The 7 most-used Munger mental models (inversion, opportunity cost, circle of competence, incentive alignment, social proof, loss aversion, Lollapalooza) — the working subset of his ~30-model latticework; expand via `_learnings.md` as sessions accumulate
- Systems-thinking leverage points (Meadows)
- Bezos two-way door decision framework
- Bayesian priors for executive decisions
- Cognitive bias countermeasures in depth

## Output Template

A fillable skeleton is at `templates/first-principles-analysis-template.md`. Copy it to the target path and populate section by section as each phase completes.
