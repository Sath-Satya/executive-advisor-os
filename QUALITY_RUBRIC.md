# Output Quality Rubric

How to judge whether an Executive Advisor OS output is actually good — or whether it's AI-polished filler.

Use this rubric before you stake a decision on any analysis the system produced. Four checks. If the output fails any of them, re-run with `/continue` and specify what's missing, or open `_learnings.md` to refine your ask.

---

## The four checks

### 1. Are assumptions explicit and confidence-scored?

**Open the output. Find the assumption inventory.**

- Is there a **Frozen** table and a **Challengeable** table, separately?
- Does every row carry a confidence label — **High / Medium / Low / Speculative**?
- Does every row have an **evidence link** or a one-line citation?
- Are Claude's own inferences tagged **INFERRED**?

**Red flags:**
- No assumption inventory at all
- All assumptions rated "High" (suspicious uniformity)
- No INFERRED rows when the topic clearly required Claude to reason beyond your documents
- Same assumption appears in both Frozen and Challengeable tables

**If this check fails:** the analysis is a narrative, not a reasoning trace. Don't present it to a board.

---

### 2. Are the three alternatives genuinely distinct?

**Look at the three alternatives in Phase 3.**

- Do they differ on the **axis** (Temperament / Change / Horizon)?
- Is each tagged **two-way door** or **one-way door** (Bezos)?
- Does each carry a different **Bayesian prior** on success?
- Are the **load-bearing assumptions** different for each?
- Does the comparison table show meaningful deltas, not cosmetic ones?

**Red flags:**
- Two alternatives are essentially the same with minor phrasing changes (strawmen)
- All three share the same load-bearing assumptions (they're not really alternatives)
- One alternative is obviously a "throwaway option" included only to make the chosen one look good
- Comparison table has the same values across multiple dimensions

**If this check fails:** the analysis is single-answer-in-disguise. Ask the system to rebuild the alternatives on a different axis.

---

### 3. Is the recommendation tied to axioms and evidence?

**Read the recommendation paragraph.**

- Does the justification reference the **axioms** established in Phase 1?
- Does it cite the **frozen boundaries** from Phase 2?
- Does it name the **load-bearing assumptions** from Phase 2?
- Does it introduce any NEW premises not established earlier? *(this is a fail)*

**Red flags:**
- Recommendation uses generic reasoning that could apply to any topic
- New facts or opinions appear in the recommendation that weren't in the earlier phases
- Justification is emotional or rhetorical, not structural
- Recommendation hand-waves on the load-bearing assumptions ("we can figure that out later")

**If this check fails:** the analysis is disconnected from its own foundation. The recommendation could be wrong for reasons the analysis ignored.

---

### 4. Are counter-arguments steel-manned?

**Open the Counter-arguments section.**

- Is there at least one counter-argument per top failure mode in the pre-mortem?
- Is each counter-argument **strong** — the best version of the objection, not a weak strawman?
- For each, does the analysis **show how it survives** the objection, OR honestly flag that it doesn't?
- Are any gaps or unresolved tensions named explicitly?

**Red flags:**
- Counter-arguments are one-liners
- Every counter-argument is "successfully refuted" without detailed engagement
- The counter-argument reads as written by someone who wanted the recommendation to win
- No "Gap flagged" notes anywhere — implying the analysis thinks it's bulletproof

**If this check fails:** the analysis hasn't earned its conclusion. A smart board member or reviewer will find the hole in five minutes.

---

## How to use this rubric

**Before you present the output externally:**
1. Run all four checks yourself (takes ~10 minutes)
2. If any fail, type `/continue <topic-slug>` and explicitly name what's missing — *"The assumption inventory is uniform on confidence. Re-do it with evidence links per row."*
3. Bump to v2. Re-check.
4. Only then take it to the board / CFO / investor / regulator.

**Before you act on the recommendation yourself:**
1. Apply the same four checks
2. Specifically look for **confirmation bias** — are the Frozen assumptions suspiciously aligned with what you already wanted?
3. If so, explicitly challenge one frozen assumption in a re-run to see what shifts

---

## The meta-rule

**If the output is too polished and too confident too fast** — be suspicious. Real first-principles analysis has friction. Real reasoning surfaces uncomfortable tradeoffs. Real pre-mortems uncover failure modes you didn't see before you started.

A perfectly clean output with a confident recommendation and no gaps is a signal, not a result.

The system has a bias-sweep phase for a reason. Use the rubric. Trust the friction.
