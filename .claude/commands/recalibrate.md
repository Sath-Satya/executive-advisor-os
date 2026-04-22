# /recalibrate — Add a Missed File and Regenerate

> **Tool:** Claude Code slash command

Add a document that was missed on the first pass. No questions. Read the file, merge it into existing context, regenerate all existing outputs at the next version, update memory + dashboard.

## What to do

### Step 1 — Resolve target research
If only `$ARGUMENTS` is given (e.g. `cms-2026-final-rule.pdf`), locate the active research folder (or ask which one if ambiguous). The file can be inside a specific research folder or at the domain root.

### Step 2 — Read the new file fully
Extract key findings, data points, positions. Add a summary line to `handover.md` under "Documents Reviewed".

### Step 3 — Re-synthesize
Merge the new file's content with existing findings. Flag any contradictions or updates to prior conclusions.

### Step 4 — Regenerate existing outputs at v{N+1}
Only regenerate output types that already exist for this research. Do NOT introduce new output types — that's what /continue is for.

### Step 5 — Reconcile memory + dashboard
Append session-log entry: "Recalibrated with {filename}, regenerated {list of outputs} at v{N+1}."
Regenerate `research/dashboard.html`.

## Important
- NO questions. The user already knows what they want.
- If the new file fundamentally changes the research direction, flag it in the handover's "Open Questions" and let the user decide whether to /continue or /new-research.

$ARGUMENTS
