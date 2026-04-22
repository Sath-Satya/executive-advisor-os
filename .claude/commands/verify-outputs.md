# /verify-outputs — Audit research outputs against the completeness contract

> **Tool:** Claude Code slash command
> **Skill:** `output-verification`

Run the pre-completion output audit on an existing research folder on demand. Useful when (a) you want to confirm all deliverables landed before presenting to the executive, (b) you suspect a missing `.pptx` or HTML briefing, or (c) a prior session claimed "complete" and you want to re-check.

## What to do

### Step 1 — Resolve the research folder
If `$ARGUMENTS` names a slug (e.g. `cms-0057-payer-implementation`), use it. Otherwise list every directory under `research/` (excluding `dashboard.html`, `dashboard.plan.md`, hidden files) and ask which to audit.

### Step 2 — Run the output-verification skill
Invoke `.claude/skills/output-verification/SKILL.md`. Load the research folder's `.memory/handover.md` → extract the "Outputs Generated" or "Requested outputs" section → build the expected file manifest per `.claude/rules/output-completeness-mandate.md` → enumerate what exists in `research/{slug}/output/` → produce the PASS/FAIL audit report.

### Step 3 — Report to the exec
Print the audit report in the chat:
- PASS → *"All mandatory artifacts present. `<slug>` is complete."*
- FAIL → list missing artifacts and the exact command to produce each (e.g. `python .claude/scripts/md_to_pptx.py <path>`)

### Step 4 — Remediate (optional)
If the audit fails AND the user approves remediation, regenerate missing artifacts per the remediation recipes in the `output-verification` SKILL.md. Re-run the audit before claiming complete.

### Step 5 — Log
Append the audit result (PASS or FAIL + remediation steps, if any) to `research/{slug}/.memory/session-log.md`.

## Important
- **Read-only by default.** Do not regenerate missing artifacts unless the user explicitly says "fix them" or "remediate".
- **Never lie about completeness.** If a `.pptx` is missing, report it — do not substitute the `.md` source.
- **PPTX size check:** a zero-byte `.pptx` is a failed conversion, not a pass. Treat it as missing.
- Works in Claude Code, VS Code + Claude extension, and Claude.ai. Claude.ai users should use this command any time they want to confirm a prior session actually closed cleanly.

$ARGUMENTS
