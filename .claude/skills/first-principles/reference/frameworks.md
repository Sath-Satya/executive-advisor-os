# First-Principles — Frameworks Deep Reference

Loaded ON DEMAND when the `first-principles` skill is actively running. Not in session-discovery tier 1.

This file is the canonical explainer for every framework SKILL.md references. When in doubt during analysis, come here.

---

## Part A — Decomposition Frameworks

### A.1 Aristotelian (categorical)

The 10 categories of being from Aristotle's *Categories* — we use the 6 that matter for business reasoning. Use this FIRST in Phase 1 because it prevents missing a dimension.

| Category | Question it forces | Business translation |
|---|---|---|
| Substance | What is the thing itself? | What are we actually deciding about — a product? a policy? a relationship? a contract? |
| Quality | What attributes define it? | Price, speed, quality, brand position, compliance posture |
| Quantity | What magnitudes matter? | Revenue, cost, users, members, hours, risk exposure in $ |
| Relation | What does it depend on, what depends on it? | Upstream suppliers, downstream consumers, partnerships, regulatory dependencies |
| Time | What is the horizon? What is reversible? | Short-term / medium / long-term; one-way or two-way door |
| Place | What is the scope boundary? | Geography, market segment, organizational unit, product line |

**Usage rule:** prune categories that don't apply. Don't force "Place" into a decision that has no geographic dimension. Keeping empty branches produces noise.

**Worked example — "Should we migrate to vendor B from vendor A?"**
- Substance: contract + implementation + change-management package, not just technology
- Quality: uptime, support responsiveness, feature parity, data portability
- Quantity: $12M/yr license delta; 18 months of engineer time to migrate; 47 integrations
- Relation: 3 downstream products depend on vendor A's API shape; 2 regulators have audit trails
- Time: 18-month project; extremely hard to reverse once data is migrated (one-way door)
- Place: decision is US-scoped; EU entity is on vendor C entirely

---

### A.2 Cartesian doubt

From Descartes' *Meditations* — reject every accepted premise until only what is self-evidently true remains. Used in Phase 1 to stress-test axiom candidates, and in Phase 2 to find assumptions hiding as facts.

**The four rules (adapted for business):**

1. **Accept nothing as true that you have not clearly and distinctly perceived to be so.** Industry convention is not truth. "That's how it's done" is not evidence.
2. **Divide each difficulty into as many parts as are necessary.** If a claim bundles multiple sub-claims, split them and test each.
3. **Order your thoughts from simplest to most complex.** Build up from the unquestionable before adding complexity.
4. **Make enumerations so complete and reviews so general you are sure nothing is omitted.** Did we list every assumption? Did we check every dependency?

**Usage rule:** the question Claude asks at every axiom candidate is:
> *"If I take this away, does the argument fall apart? If so — is this actually self-evident, or am I assuming it?"*

A real axiom survives the removal. An assumption doesn't.

**Anti-pattern:** treating "because the org has always done it this way" as self-evident. It's the opposite — it's a signal that the premise has never been tested.

---

### A.3 Feynman technique

From Richard Feynman's pedagogy — if you can't explain it simply, you don't understand it. Used in Phase 1 step 1.1 to re-frame the question.

**The four steps:**

1. Pick the concept (the user's question).
2. Re-explain it in plain language, as if to a smart 12-year-old who has no domain context.
3. Identify the gaps — places where you had to reach for jargon or hand-wave.
4. Refine — go back to sources, fill the gap, re-explain.

**Usage rule for this skill:** write the re-framing in no more than 3 sentences. If it takes more, the question itself is probably composite — split it before proceeding.

**Worked example — re-framing drift:**
- User says: "We need to optimize our member engagement KPIs for Q3."
- Feynman re-frame (attempt 1): "The member team wants engagement numbers to go up in the next 3 months."
- Gap detected: "engagement" isn't defined; "optimize" isn't a specific action.
- Feynman re-frame (attempt 2): "Between July and September, the member team wants more members to do {specific action} more often, and needs a plan for making that happen."
- Now the real question becomes visible: it's not an analytics question, it's a behavior-change question.

---

### A.4 Musk / 5-Whys (constraint drill)

From both Toyota's 5-Whys root-cause method and Elon Musk's reasoning style. Used in Phase 1 step 1.3.

**The drill:**
Repeat "why does this constrain us?" on every material component until the terminal answer is one of:

1. **A law of physics or math** — unchallengeable; stop.
2. **A regulation or contract** — may be challengeable (lobbying, renegotiation) but expensive; tag as Frozen unless executive has authority to pursue.
3. **A stated executive preference** — challengeable in conversation; ask exec if still held.
4. **A grounded empirical fact with evidence** — challengeable by better data; note the source.
5. **"Because we've always done it that way"** — NOT a terminal answer. This is an assumption, not a constraint. Drop back into the assumption pool.

**Guardrail:** stop at 5 layers deep. Past that, cognitive load per layer exceeds insight return. Only go deeper on explicit user approval.

**Worked example — why does this project take 18 months?**
- Why 18 months? → Because the vendor requires a 6-month implementation + 12 months of data migration.
- Why 12 months of data migration? → Because we have 47 legacy integrations to re-map.
- Why 47 integrations? → Because over 8 years we integrated every new system with vendor A directly.
- Why direct integrations? → Because we didn't build an integration layer. (← this is the actual constraint — a past architectural decision)
- Why didn't we build a layer? → Because it wasn't prioritized. (← we hit a soft constraint; drop back to assumption pool)

**Terminal insight:** the 18-month timeline is a function of past architectural debt, not of the vendor migration itself. That changes the entire analysis — the real decision may be whether to build an integration layer first.

---

## Part B — Mental Models (applied in Phase 3 Reconstruction)

### B.1 Munger's latticework (core 30)

Charlie Munger's multi-disciplinary mental models. Not all 30 apply to every problem — pick the ones that fit. The skill uses these seven most often in exec reasoning:

1. **Inversion** — "What would guarantee this fails?" Often easier than asking what guarantees success.
2. **Opportunity cost** — every "yes" is a "no" to something else. What is the next-best use of these resources?
3. **Circle of competence** — are we playing inside our expertise, or outside it?
4. **Incentive alignment** — how is everyone involved compensated? What does that compensation drive them to do?
5. **Social proof** — are we following this path because it's right, or because everyone else is?
6. **Loss aversion** — are we over-weighting the downside of change versus the downside of inaction?
7. **Lollapalooza effect** — when multiple mental models point the same direction at once, effects compound. Check if the alternative has a Lollapalooza for OR against it.

**Usage rule in Phase 3:** for each of the 3 alternatives, run at minimum Inversion, Opportunity cost, and Incentive alignment. Add others as the topic demands.

**Worked snippet — Inversion applied to a "should we acquire X?":**
- What would guarantee this acquisition fails? Integration costs run 2x; key talent leaves in year 1; cultural mismatch breaks product velocity; regulator blocks the deal.
- Are any of these signals already present? If yes — they're not tail risks, they're base-rate risks.

---

### B.2 Systems thinking (Meadows)

From Donella Meadows' *Thinking in Systems*. Used in Phase 3 to identify leverage points and second-order effects.

**Core concepts used:**

- **Stock and flow** — what accumulates (stock) and what changes it (flow)? Example: member count is a stock; new joins and churn are flows.
- **Feedback loops** — reinforcing (R) loops accelerate; balancing (B) loops self-correct. Most failures come from ignored balancing loops.
- **Delays** — the gap between cause and effect. Long delays cause over-correction and oscillation.
- **Leverage points** (Meadows' 12, in rough order of power):
  1. Paradigm (lowest leverage)
  2. Goals
  3. Power to change paradigms
  4. Self-organization
  5. Rules
  6. Information flows
  7. Reinforcing loops
  8. Balancing loops
  9. Delays
  10. Stock / buffer sizes
  11. Subsystem structure
  12. Numbers / parameters (highest leverage per unit effort, often)

**Usage rule in Phase 3:** for each alternative, ask: where does it intervene? If it's at the "numbers / parameters" layer, expect quick wins. If it's at "paradigm", expect slow, deep change — and resistance.

---

### B.3 Bezos — regret minimization + 2-way doors

Two Amazon leadership principles applied to executive decisions:

**Regret minimization framework (for one-way decisions):**
> "When I'm 80, will I regret NOT doing this?"

Used when the decision is irreversible (hiring someone senior, selling a business, exiting a market). Forces the decision into a long-horizon frame where tactical concerns matter less.

**Two-way door vs one-way door:**

- **Two-way door** (reversible) — make fast. Cheap to correct. Don't over-analyze; ship and iterate.
- **One-way door** (irreversible) — make slowly. Raise the evidence bar. Require deeper first-principles work.

**Usage rule in Phase 3:** every alternative gets tagged `two-way` or `one-way`. One-way alternatives require a higher Bayesian prior to be recommended. Two-way alternatives favor speed over certainty.

**Worked snippet:**
- Alt A: pilot with 500 members for 90 days. **Two-way door** — we can stop at any point.
- Alt B: rebuild the authentication layer. **One-way door** at scale — reverse would cost ~8 months.
- → Alt A needs less evidence to justify; Alt B needs materially more.

---

### B.4 Bayesian / probabilistic reasoning

Not statistical wizardry — the discipline of stating priors and updating on evidence.

**Usage rule in Phase 3:** for each alternative, answer three questions:

1. **Prior** — before any analysis, what's your gut probability this alternative succeeds? State a range (e.g., 40–60%).
2. **Evidence update** — what evidence would move the prior up? What would move it down? Has that evidence arrived?
3. **Posterior** — after the evidence, what's the updated probability? Has the recommendation order changed?

**Crucial check:** if the posterior is inside the prior range even after evidence, your evidence isn't actually moving the needle — which means you might be anchored to the prior (bias check in Phase 4).

**Audience calibration:** Bayesian language lands well with quant-literate audiences; for non-quant executives, translate to "confidence" (high / medium / low) — but keep the discipline internally.

---

## Part C — Cognitive Bias Countermeasures (Phase 4)

The four bias families the skill sweeps for before output. Each has a detection heuristic and a mitigation.

### C.1 Anchoring / availability

- **Detection:** Does the recommendation follow suspiciously closely to the first number or first example mentioned? Is a vivid recent event (e.g., a competitor's move, a public incident) driving the weighting?
- **Mitigation:** Reset — state the recommendation without reference to the anchor. Does it still hold? If not, the anchor was doing the work.

### C.2 Sunk cost / status quo

- **Detection:** Phrases like "we've already invested", "we can't throw away", "this is how we've always done it" in the decomposition or alternatives.
- **Mitigation:** Run the analysis from a zero-base — "if we were starting fresh today, would we pick this path?" If the answer is no, sunk cost is driving the recommendation.

### C.3 Confirmation / motivated reasoning

- **Detection:** Every piece of evidence points toward the same conclusion. Counter-evidence was noted but dismissed without detailed engagement. The exec walked in with a position and the analysis matches it.
- **Mitigation:** Steel-man the opposing view (Phase 4 counter-arguments section). If the steel-man is thin, the analysis is probably confirmation-biased. Ask a colleague to attack the recommendation.

### C.4 Planning fallacy / overconfidence

- **Detection:** Timelines, costs, and impact estimates are suspiciously round and optimistic. Failure modes in pre-mortem are all "unlikely edge cases", not plausible base-rate failures.
- **Mitigation:** Reference class forecasting — what happened to the last N projects like this? Use the outside view, not the inside view. For estimates, apply a +50% contingency unless evidence supports tighter bounds.

---

## Part D — Integration Cheatsheet

### D.1 Executive Advisor OS Strategic-deep auto-invocation flow

```
Executive Advisor OS /new-research
  → Step 1-3 Core + docs
  → Step 4 Complexity classification
    → If Strategic-deep → first-principles auto-runs HERE
      → Phase 1 Deconstruct + AskUserQuestion confirm
      → Phase 2 Challenge + AskUserQuestion frozen gate
      → Phase 3 Reconstruct + AskUserQuestion axis check
      → Phase 4 Pre-mortem + AskUserQuestion failure review
    → Continue with EA Step 6 output generation
    → Executive Advisor OS outputs enriched from first-principles-analysis_v{N}.md
```

### D.2 Dev-domain invocation

Use with `brainstorm-to-plan` for architecture decisions where the team's defaults might be wrong:
```
brainstorm-to-plan Phase 1 Socratic → detect "we've always..." → invoke /first-principles → resume brainstorm-to-plan Phase 2 with outputs
```

### D.3 Interaction with large-artifact-generation.md

If the output MD (including Mermaid tree + 3 alternatives + pre-mortem + counter-arguments) crosses 300 lines → this skill MUST follow the large-artifact-generation rule — plan file + chunked build + Step-4 review before claiming complete.
