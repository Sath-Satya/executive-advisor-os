# /dismiss — Remove a research slug from the dashboard

> **Tool:** Claude Code slash command

Permanently drop a slug from the dashboard. Use when a research folder was deleted from disk and the user is ready to stop seeing it as `Removed` on the dashboard.

## What to do

### Step 1 — Parse the slug
`$ARGUMENTS` is the slug to dismiss (e.g. `old-board-memo`). If missing, list the current `REMOVED_SLUGS` from `research/dashboard.html` and ask which one to dismiss.

### Step 2 — Safety check
Confirm the folder is actually gone from disk. If `research/<slug>/` still exists, do NOT dismiss — tell the user the research is still live and ask whether they want to delete the folder first.

### Step 3 — Update dashboard state
Edit `research/dashboard.html`:
- Remove `<slug>` from the `<!-- REMOVED_SLUGS: ... -->` comment near the top of `<head>`
- Remove the card with `id="<slug>"` and `.removed` class from `#research-grid`
- Remove the sidebar `<li>` entry pointing to `#<slug>`
- Decrement the `Removed` stat counter
- Update the `Last updated` timestamp

### Step 4 — Confirm
Report: *"Dismissed `<slug>` from the dashboard. It won't reappear unless a folder with that name is recreated under `research/`."*

## Important
- Never dismiss a slug whose folder still exists on disk — that would hide live research
- Never edit anything outside `research/dashboard.html` — this command is dashboard-state only
- No memory or handover updates — those files already vanished with the folder

$ARGUMENTS
