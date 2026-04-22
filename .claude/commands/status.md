# /status — List All Research and Open Dashboard

> **Tool:** Claude Code slash command

Show every research topic, its version, last-updated date, and what outputs exist. Point the user to `research/dashboard.html` for the visual view.

## What to do

### Step 1 — Enumerate research folders
List every directory under `research/` (excluding `dashboard.html`). For each:
- Folder name (slug)
- Topic name (from `handover.md` — read only the header)
- Current version
- Last updated date
- List of output files that exist

### Step 2 — Print a compact table to chat
```
SLUG                       TOPIC                               VERSION   UPDATED      OUTPUTS
cms-2026-prior-auth        CMS 2026 Prior Auth Impacts         v3        2026-04-15   summary, analysis, briefing, deck_detailed
board-capital-plan         2026 Capital Plan Review            v1        2026-03-22   summary, analysis, briefing
```

### Step 3 — Regenerate dashboard
Regenerate `research/dashboard.html` with current state so the user has a fresh view to open.

### Step 4 — Tell the user where to look
*"Open `research/dashboard.html` in your browser for the visual view."*

## Important
- Read-only listing — do not modify any research output.
- If `research/` is empty, say so and suggest `/new-research`.
- If any folder lacks `handover.md`, show it as "In Progress" and suggest `/continue {slug}` to complete it.

$ARGUMENTS
