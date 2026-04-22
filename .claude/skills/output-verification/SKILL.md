---
name: output-verification
description: Pre-completion audit for Executive Advisor OS research sessions. Verifies every requested deliverable exists in its final user-consumable form — PPTX for decks, HTML for briefings, MD for summaries/analyses — before any "complete" claim can be made. Blocks completion if any artifact is missing. Also checks file sizes and Step-4 large-artifact rule compliance.
when_to_use: Run automatically at the end of every `/new-research`, `/continue`, or `/recalibrate` session before regenerating the dashboard and writing the session handover. Also run on demand via `/verify-outputs [slug]`.
version: 1.0.0
---

# Output Verification

## When to Use

Invoke this skill **before** claiming any of: *complete / ready / done / shipped / delivered* on an Executive Advisor OS research session. The skill enumerates what the executive asked for, checks what is actually on disk, and produces a pass/fail report. Failure blocks the completion claim.

Trigger points:
- End of `/new-research` workflow Step 6 (before Step 7 memory + dashboard update)
- End of `/continue` session after outputs are regenerated
- End of `/recalibrate` after v{N+1} is produced
- On demand: `/verify-outputs <slug>` to audit an existing research folder

## The Verification Protocol

### Step 1 — Read the output contract
Load the research folder's `.memory/handover.md` and find the "Outputs Generated" section (or "Requested outputs" during /new-research clarification). This is the **contract** — the binding list of what the executive asked for.

If the contract is unclear, re-read the most recent AskUserQuestion answers in `.memory/session-log.md` for the outputs question.

### Step 2 — Build the expected file manifest
For each requested output, compute the expected file set per `output-completeness-mandate.md`:

| Requested output | Expected files |
|---|---|
| Executive summary | `output/executive_summary_v{N}.md` |
| Detailed analysis | `output/detailed_analysis_v{N}.md` (plus `.plan.md` if expected >300 lines) |
| HTML briefing | `output/briefing_v{N}.html` (plus `briefing.plan.md` if >300 lines) |
| Deck — summary | `output/deck_summary_v{N}.md` **AND** `output/deck_summary_v{N}.pptx` |
| Deck — detailed | `output/deck_detailed_v{N}.md` **AND** `output/deck_detailed_v{N}.pptx` **AND** `deck_detailed.plan.md` **AND** `output/slides/*.md` (one per slide) |
| First-principles (auto for Strategic-deep) | `output/first-principles-analysis_v{N}.md` (plus `.plan.md` if >300 lines) |

### Step 3 — Enumerate what exists on disk
Use `Glob` or `Bash ls` against `research/{slug}/output/` and `research/{slug}/output/slides/` (if applicable).

### Step 4 — Produce the audit report
Format:

```
Output verification — research/{slug}
=====================================
Contract (from .memory/handover.md):
  - executive_summary
  - detailed_analysis
  - briefing_html
  - deck_summary
  - deck_detailed

Audit:
  ✓ executive_summary_v1.md        (4.7 KB)
  ✓ detailed_analysis_v1.md        (40 KB, 830 lines)
  ✓ briefing_v1.html               (46 KB)
  ✓ deck_summary_v1.md             (6.6 KB, 3 slides)
  ✗ deck_summary_v1.pptx           MISSING — blocks completion
  ✓ deck_detailed_v1.md            (18 KB, 12 slides)
  ✗ deck_detailed_v1.pptx          MISSING — blocks completion

Result: FAIL (2 mandatory artifacts missing)
Fix: run `python .claude/scripts/md_to_pptx.py <deck_md_path>` for each missing PPTX
```

### Step 5 — Remediation
If the audit fails:
1. Identify each missing artifact
2. Regenerate it:
   - Missing MD → follow the relevant skill (`html-generation`, `deck-generation`, or direct write)
   - Missing PPTX → `python .claude/scripts/md_to_pptx.py <md_path> [<pptx_path>]`
   - Missing `.plan.md` for large artifact → write the plan (per `large-artifact-generation.md`)
3. Re-run the audit
4. Only claim "complete" when audit result = PASS

### Step 6 — Record the verification
Append the audit report to `.memory/session-log.md`. Include timestamp, result (PASS or FAIL), and list of any remediation steps executed.

## Must Do

- Run this check **before** any completion claim, every session, no exceptions
- Use the exact mandatory file inventory from `output-completeness-mandate.md` — do not relax the list
- Verify PPTX files actually exist on disk AND have non-zero file size (a zero-byte `.pptx` is a failed conversion, not a success)
- When outputs are regenerated during remediation, re-audit — do not trust a first-pass claim

## Must Not Do

- Never claim "complete" when any mandatory artifact is missing
- Never treat a Marp `.md` file as sufficient for a deck output — PPTX is the deliverable
- Never skip verification because "I just generated everything" — generation and persistence are different
- Never silently substitute (e.g., claiming a briefing HTML exists when only a `.md` draft is on disk)

## Remediation Recipes (ready-to-run)

### Missing deck PPTX
```bash
python .claude/scripts/md_to_pptx.py \
  research/{slug}/output/deck_summary_v{N}.md
# Produces deck_summary_v{N}.pptx in same folder
```

### Missing detailed deck with per-slide MDs
If `deck_detailed_v{N}.md` exists but per-slide MDs are missing:
1. Split the main MD on `---` separators
2. Write each slide as `slides/NN-<kebab-title>.md`
3. Keep per-slide presenter notes intact

If PPTX is missing, run the converter — it reads the consolidated MD, not the per-slide MDs.

### Missing briefing HTML
The `html-generation` skill produces the briefing. If only a plan MD exists, write the HTML per the plan using the cream-navy-gold palette per `.claude/rules/brand/visual-identity.md`. Chunk if >300 lines per `large-artifact-generation.md`.

## Integration Points

| Trigger | Verification runs before |
|---|---|
| `/new-research` Step 7 | Dashboard regeneration + handover write |
| `/continue` end | v{N+1} dashboard update |
| `/recalibrate` end | v{N+1} dashboard update |
| `/verify-outputs <slug>` | Read-only audit (no remediation unless exec approves) |

## Exit States

- **PASS** — All mandatory artifacts present and non-empty; session may claim complete
- **FAIL (remediate)** — Missing artifacts; run remediation recipes and re-audit
- **FAIL (blocked)** — Missing artifacts cannot be auto-remediated (e.g., content requires exec input); escalate to exec, pause session, document in blockers

## Why This Skill Exists

Precedent: 2026-04-21 `cms-0057-payer-implementation` session produced 5 MD outputs + 1 HTML briefing, and claimed completion. But the two decks were Marp `.md` source — not PPTX — making them unusable as presentation deliverables for a payer leadership team. Exec caught the gap. Root cause: no pre-completion audit step. This skill institutionalizes the audit so the gap cannot recur.
