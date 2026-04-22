# First-Principles Analysis — {Topic}

**Version:** v{N}
**Date:** {YYYY-MM-DD}
**Invoked by:** {caller — /first-principles | Executive Advisor OS /new-research Strategic-deep | brainstorm-to-plan | ad-hoc}
**Complexity tier:** {Simple | Standard | Complex | Strategic-deep}

---

## 0. Scope note

Audience: {primary decision-maker / board / exec team / self}
End goal: {the decision or action this analysis serves}
Frozen boundaries declared up front: {regulatory / contractual / political / ethical / executive preference — one-line each}

---

## 1. Re-framed question (Feynman)

**User's stated question:**
> {original framing — quoted verbatim}

**Re-framed in plain language:**
> {plain-language restatement; no jargon; tests whether the question is actually the right question}

**Re-framing confirmation:** {confirmed by user on {date} | pending}

---

## 2. Decomposition tree (Mermaid, left-to-right)

```mermaid
flowchart LR
    Q[{re-framed question}]
    Q --> S[Substance]
    Q --> Qu[Quality]
    Q --> N[Quantity / magnitude]
    Q --> R[Relation / dependencies]
    Q --> T[Time / horizon / reversibility]
    Q --> P[Place / scope boundary]
    S --> S1[...]
    S --> S2[...]
    Qu --> Qu1[...]
```
*(Populate only the categories that apply; prune empty branches.)*

**Depth reached:** {N} layers. Max cap: 5. Deeper requested by user: {yes / no}.

---

## 3. Axiom candidates (Musk/5-Whys terminal layer)

Terminal answers from the "why does this constrain us?" drill. Each must pass Cartesian doubt to become an axiom.

| # | Axiom candidate | Type | Cartesian doubt passed? | Notes |
|---|---|---|---|---|
| A1 | e.g., "CMS regulation X requires Y by 2026-12-31" | Regulatory | Yes | CMS-2026-XXXX-F §12.3 |
| A2 | e.g., "Member switching cost is ~$1,200/yr in admin + rework" | Empirical (grounded) | Yes | Internal ops data 2025 |
| A3 | e.g., "Members prefer fewer plan disruptions" | Industry convention | **No — back to assumption pool** | |

---

## 4. Assumption inventory

### 4a. FROZEN assumptions (work within — not challenged)

| # | Assumption | Frozen-reason | Thaw signal | What changes if it thaws |
|---|---|---|---|---|
| F1 | {} | {regulatory / contractual / political / ethical / exec-preference} | {event/date that would trigger re-evaluation} | {high-level delta in recommendation} |
| F2 | {} | | | |

### 4b. CHALLENGEABLE assumptions (tested)

| # | Assumption | Source | Confidence | Evidence | What-if-wrong | Load-bearing? |
|---|---|---|---|---|---|---|
| C1 | {} | {user / doc / inferred} | {High/Med/Low/Speculative} | {one-line evidence link} | {how recommendation shifts if reversed} | {Yes/No} |
| C2 | {} | | | | | |

**INFERRED tag:** Any row where Source = `inferred` means Claude constructed it without user or document evidence. Treat with extra scrutiny.

---

## 5. Three alternatives

Axis chosen for the alternatives: {Temperament / Change / Horizon}

### 5a. Alternative A — {name}
{one-paragraph description}
- Sequence: {what happens in what order}
- Cost / effort: {}
- Time to value: {}
- Reversibility: {two-way door / one-way door}
- Load-bearing assumptions: {Cx, Cy}
- Bezos test: {reversible = faster, irreversible = higher bar}
- Systems risk: {feedback loops / delays / second-order effects}
- Munger inversion: {what would guarantee this fails?}
- Bayesian prior: {~X% likely to succeed, updated by evidence Y}

### 5b. Alternative B — {name}
{...same template...}

### 5c. Alternative C — {name}
{...same template...}

### 5d. Comparison table

| Dimension | Alt A | Alt B | Alt C |
|---|---|---|---|
| Cost / effort | | | |
| Time to value | | | |
| Reversibility | | | |
| Load-bearing assumptions | | | |
| Prior success probability | | | |
| Key risk | | | |
| Delta vs status quo | | | |

---

## 6. Recommendation

**Selected:** Alternative {A | B | C} — {name}

**Justification** (anchored to axioms + frozen + load-bearing assumptions only — no new premises):
{2–4 paragraphs}

**Conditions under which this recommendation changes:**
- If {load-bearing assumption Cx} is refuted → {pivot to alternative Y}
- If {frozen assumption Fz} thaws → {see thaw-sidebar in §4a}

---

## 7. Pre-mortem (Phase 4)

**Scenario:** It is two years from now. This recommendation was executed. It has spectacularly failed.

### Failure modes (ranked by plausibility)

1. **{Failure mode 1 — distinct mechanism}** — what happened, when was it already inevitable, what evidence would have warned us earlier.
2. **{Failure mode 2}** — …
3. **{Failure mode 3}** — …
4. **{Failure mode 4}** — …
5. **{Failure mode 5}** — …
6. (optional 6–7 for high-stakes topics)

---

## 8. Counter-arguments (MANDATORY section)

For each of the top 3 failure modes, write the **strongest** version of the argument against the recommendation. Steel-man, don't strawman.

### Counter-argument 1 — targeting {failure mode X}
{strongest objection}

**How the analysis survives it:** {defense tied to axioms / evidence}
OR
**Gap flagged:** {this objection is not fully resolved — acceptance rationale}

### Counter-argument 2 — …

### Counter-argument 3 — …

---

## 9. Cognitive-bias sweep

Before signing off, checked the recommendation against four biases:

| Bias | Detected? | Evidence | Mitigation applied |
|---|---|---|---|
| Anchoring / availability | {Yes/No} | | |
| Sunk cost / status quo | {Yes/No} | | |
| Confirmation / motivated reasoning | {Yes/No} | | |
| Planning fallacy / overconfidence | {Yes/No} | | |

---

## 10. Reasoning trace

Chronological log of framework application. Supports post-hoc critique and future learning.

- Phase 1 — Feynman re-framing: {one line on what shifted}
- Phase 1 — Aristotelian decomposition: {categories that mattered; categories pruned}
- Phase 1 — Musk/5-Whys: {depth reached; terminal constraint types}
- Phase 1 — Cartesian doubt: {axioms rejected and why}
- Phase 2 — Assumption extraction sources: {user / docs / inferred count}
- Phase 2 — Frozen gate: {confirmed by user on {date}}
- Phase 3 — Axis selected: {why}
- Phase 3 — Munger checks run: {inversion / opportunity cost / incentives / Lollapalooza}
- Phase 3 — Systems thinking: {feedback loops surfaced}
- Phase 3 — Bezos: {one-way vs two-way classification per alternative}
- Phase 3 — Bayesian: {priors stated; update triggers}
- Phase 4 — Pre-mortem: {failure modes generated before / after steel-man pass}
- Phase 4 — Bias sweep: {results}
- Escape hatches used: {phase N → user action}

---

## 11. Frozen-thaw sidebar

Select 2–3 frozen assumptions with highest "if this thaws" leverage. For each:

- **{Frozen assumption Fx}** — if this later changes, the recommendation shifts toward {Alt B} because {mechanism}. Watch signal: {event / metric / date}.

---

## 12. Output linkage (Executive Advisor OS only)

When this analysis is produced inside an EA research session, it feeds four downstream outputs:

- `executive_summary_v{N}.md` — enriched with key axioms + chosen alternative + top counter-argument
- `briefing_v{N}.html` — gains an expandable "How we got here" appendix (this file, rendered in exec palette)
- `deck_detailed_v{N}.md` — gains a "Decision rationale" slide
- `first-principles-analysis_v{N}.md` — this file, standalone, audit-grade

---

*Generated by `first-principles` skill v1.0.0 · {timestamp} · {model-tier}*
