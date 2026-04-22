# Research Dashboard v2 — Build Plan

## Audience / Purpose
Executive Advisor OS users — a single master view of every research topic, auto-updated every regeneration. Must open offline, print cleanly, and survive a browser refresh with no external state loss.

## Template base
Executive cream-navy-gold palette per `.claude/rules/brand/visual-identity.md`. No dark-theme variant.

## Section outline

1. `<head>` — meta, title, inline Google Fonts link, full inline `<style>` block (~140 lines — palette vars, layout grid, topbar, sidebar, stats, card, file-tree, badges, empty state, print media)
2. `<body>` `.topbar` — brand + last-updated timestamp + auto-refresh toggle + refresh button (~15 lines)
3. `<body>` `.layout` — CSS grid 2-column: sidebar + main
4. `.sidebar` — static title + nav list of research topics (anchor links) + "+ New research" hint at bottom (~15 lines)
5. `.main` — stats row (4 cards: total / active / completed / removed) + research grid (~20 lines)
6. `.research-grid` — one `.card` per research topic, populated by regeneration
7. Card template — header (title, slug, version, status badge) + goal line + expandable file tree + dismiss button (for REMOVED only)
8. Empty state — shown when zero topics exist
9. `<script>` inline — (a) set last-updated timestamp, (b) auto-refresh toggle with localStorage, (c) expandable file-tree toggle, (d) dismiss-removed helper
10. Persistence comment block — `<!-- TRACKED_SLUGS: ... --><!-- REMOVED_SLUGS: ... -->` for the regeneration logic to read
11. Regeneration contract comment block — enumeration rules, card template, verification checklist (updated from v1)

## Data sources
- Filesystem scan of `research/*/` (the assistant regenerates this file after every step)
- Per folder: `.memory/handover.md` (name, goal, audience, updated, version) + `output/*` (files + versions)
- Prior dashboard.html's TRACKED_SLUGS comment — compared against current filesystem to detect REMOVED topics

## Chunking plan
Single write — estimated ~280 lines, under the 300 threshold. Keep it tight: no duplicate CSS, terse class names, no decorative animations.

## Total estimated line count
~280 lines
