# /continue — Resume an Existing Research

> **Tool:** Claude Code slash command

Pick up an existing research exactly where it was left. Load the handover, summarize in 3 sentences, ask what changed, and regenerate at the next version.

## What to do

### Step 1 — Resolve the target folder
If `$ARGUMENTS` names a folder, use it. Otherwise list folders under `research/` (excluding `.memory`, `dashboard.html`) and ask which one.

### Step 2 — Load context
Read `research/{slug}/.memory/handover.md` in full. Read the most recent entries from `session-log.md`.

### Step 3 — Summarize back to the executive (≤3 sentences)
Mention: topic, last action taken, current version, and anything flagged as unresolved.

### Step 4 — Ask what's changed (use AskUserQuestion)
Run one `AskUserQuestion` call with these questions (multiple-choice options + "Other"):
- New documents to merge? (Yes, dropped in the folder | Yes, will paste inline | None new | Other)
- Audience or purpose shift? (Same | Narrower | Broader | Different audience | Other)
- New deadline or driving event? (No | Yes — board/exec meeting | Yes — decision date | Yes — other | Other)
- Depth change? (Go deeper on current findings | Broaden scope | Sharpen the recommendation | No change | Other)

If the executive signals the research has grown more complex (e.g. "much bigger now", "board-level now", "regulatory added"), re-classify complexity per CLAUDE.md Step 3 and run additional AskUserQuestion rounds before generating. No question cap.

### Step 5 — Execute and bump version
Every output regenerates as v{N+1}. Never overwrite prior versions.

### Step 6 — Reconcile memory + regenerate dashboard
Append a new `session-log.md` entry. Update `handover.md`. Regenerate `research/dashboard.html`.

## Important
- Always bump the version, even if only one output changed.
- Do NOT re-ask the 3 core questions — they are already in handover.md.
- If the folder does not exist or has no handover.md, tell the user and offer to `/new-research`.
- **Stay strictly in research scope.** Never propose building tools, systems, or workflows. Research and reports only. See CLAUDE.md Rule 6 + Rule 11.

$ARGUMENTS
