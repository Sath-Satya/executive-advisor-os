# Exec-Friendly Clarification — Question Language Rule (NON-NEGOTIABLE)

## Purpose
Every `AskUserQuestion` round surfaced to a non-technical executive must be phrased in **business and research terms** — not methodology or framework jargon. Most executives do not know (and do not need to know) terms like "strawman alternative," "steel-man," "frozen-thaw," "Aristotelian categories," "Bayesian prior," "Bezos two-way door," or "load-bearing assumption." These are analyst constructs. They belong in the analyst's working notes, not in the clarification pane the executive sees.

## Scope
Applies to every `AskUserQuestion` call made inside Executive Advisor OS across all commands — `/new-research`, `/continue`, `/recalibrate`, `/first-principles`, and any skill invoked from within EA OS (including `first-principles`).

Does NOT apply to artifacts generated for audit (e.g. `first-principles-analysis_v{N}.md`), where methodology vocabulary is appropriate and expected.

## Non-Negotiable Rules

### 1. Prefer research-relevant phrasing over method-relevant phrasing
Reword every question from "what analysis step should I take" to "what business input should I use."

| ❌ Method-jargon phrasing | ✅ Exec-friendly phrasing |
|---|---|
| "Is any alternative strawman-thin?" | "Is any of the three options weak or unrealistic — if so, which should I replace?" |
| "Any counter-argument I didn't steel-man strongly?" | "Is there an objection from leadership / the board that we haven't addressed strongly enough?" |
| "Which of these assumptions is load-bearing?" | "Which of these beliefs would materially change the recommendation if it turned out to be wrong?" |
| "Should we treat this as FROZEN?" | "Is this a hard boundary we can't change (regulation / CEO preference / contract)?" |
| "Apply inversion on Alt A?" | "What would most likely cause this path to fail?" |
| "What is the Bayesian prior?" | "How likely is this path to succeed — our rough confidence level today?" |

### 2. Inline reference when a mental model is invoked
If a question or a bullet explicitly names a mental model (pre-mortem, inversion, two-way door, systems thinking, 5-Whys, etc.), add a **brief parenthetical definition** inline on first use within that message. The executive should never have to ask "what does that mean."

| ❌ Bare invocation | ✅ With inline reference |
|---|---|
| "Run a pre-mortem on Alt A." | "Run a pre-mortem on Alt A *(imagine it's 2 years from now and this path failed — why)*." |
| "Is Alt C a one-way door?" | "Is Alt C a one-way door *(an irreversible commitment that's hard to undo once made)*?" |
| "Apply inversion." | "Invert the problem *(instead of asking 'how do we succeed?', ask 'how would we most guarantee failure?')*." |
| "What's the Bayesian prior?" | "What's the prior *(our best rough estimate of the success probability before we run the test)*?" |
| "Steel-man the counter-argument." | "State the strongest possible version of the objection *(the 'steel-man' — opposite of a strawman)*." |

### 3. Use the exec's own vocabulary
When the exec's clarification answers include terms from their domain (e.g. payer, MLR, MA, PA, prior auth, USCDI, FHIR, formulary, HEDIS, Star Ratings, CMS), mirror those terms in subsequent questions. Do not default to generic business terms when a domain term has been used.

### 4. Keep option copy inside AskUserQuestion short + concrete
Options inside AskUserQuestion should be 1–5 word labels + a one-line concrete description. Never use a method-named option label (e.g., "Strawman Alt B"). If you must reference the method, put the method name in the description body after the plain-language lead.

### 5. Analyst notes stay in artifacts
All framework vocabulary (frozen, challengeable, load-bearing, counter-argument, steel-man, Cartesian doubt, etc.) is still used in the analyst-facing artifacts (`first-principles-analysis_v{N}.md`, `.memory/handover.md`, `.memory/session-log.md`). Those artifacts are for audit and continuity — and also for a future Claude session resuming the work. Framework language in those files is a feature, not a bug.

### 6. Transparency still required
When the `first-principles` skill runs inside EA OS, the executive is still told "I'm applying first-principles thinking" (per `first-principles` SKILL.md integration contract). But the individual questions asked along the way use exec-friendly phrasing — the method name is the header, not every question.

## How to Apply

Before every `AskUserQuestion` call in EA OS:
1. Draft the questions in whatever internal phrasing comes naturally
2. Scan for jargon terms (list below)
3. Rewrite each flagged term into business/research language per the table above
4. If a mental model is genuinely needed in the question, add the inline parenthetical

**Jargon terms to flag and rewrite:**
strawman · steel-man · frozen · challengeable · load-bearing · axiom · Aristotelian · Cartesian · Feynman · Musk/5-Whys · Munger · Bayesian · Bezos door · pre-mortem · inversion · Lollapalooza · systems-thinking leverage point · circle of competence · planning fallacy · anchoring bias · confirmation bias · confidence interval · prior probability

## Enforcement

- `first-principles` SKILL.md references this rule in its EA OS integration section — questions follow this rule when the skill runs inside EA OS
- `output-verification` skill does not block on language style, but an optional self-audit pass may flag obvious jargon leaks
- `skill-evolution` scans `_learnings.md` for user feedback about confusing questions → adds to the jargon term list

## Example — Before and After

### ❌ Before (from an actual session)
> **Question:** "Is any alternative strawman-thin, or does a 4th alternative need surfacing before Phase 4?"
> Options include: *"Alt B is strawman" / "Add 4th alt: Ecosystem Leader"*

### ✅ After (this rule applied)
> **Question:** "Are any of the three options weak or unrealistic — should I replace one?"
> Options: *"All three are solid" / "Option B is weak — replace it with something stronger" / "Add a fourth option: Payer-as-Platform ecosystem play (requires removing one of the current three since we cap at three to force prioritization)"*

### ❌ Before
> **Question:** "Any counter-argument I didn't steel-man strongly enough?"

### ✅ After
> **Question:** "Any likely board or leadership objection that isn't addressed strongly enough in the analysis?"

## Related rules

- **`.claude/rules/output-completeness-mandate.md`** — governs the *artifacts* produced at session end (PPTX, HTML, MD inventories). This rule governs the *language* of the clarification interview leading up to those artifacts. Together they cover the full exec-facing surface: plain language during the interview, complete deliverables at the end.
- **`.claude/skills/output-verification/SKILL.md`** — enforces the completeness contract at session close. Does not check clarification language (that is this rule's job) but runs a self-audit pass that may flag obvious jargon leaks in handover/session-log.

## Why This Rule Exists

Precedent: 2026-04-21 `cms-0057-payer-implementation` session. Phase 3 and Phase 4 AskUserQuestion rounds used terms including "strawman" and "steel-man." Exec flagged confusion — "most people may not be well-known with these gates and principles." Research-relevant phrasing would have been clearer and still captured the same signal.

The cost of using jargon is measured in two ways:
1. **Exec cognitive load** — they have to either infer the term's meaning or stop and ask
2. **Answer quality** — a confused exec picks defensively or skips the question, not optimally

Plain-language rewriting has zero downside. The analyst's working vocabulary is preserved in artifacts; the exec-facing surface speaks the exec's language.
