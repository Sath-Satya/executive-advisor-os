# Large Artifact Generation — Plan-in-Markdown, Build-in-Chunks (NON-NEGOTIABLE)

## Purpose
Stop "response hit length limit" failures on large HTML documents and slide decks. Every large artifact MUST be planned as Markdown first, then built in chunks and merged, then thoroughly reviewed before being marked complete.

## Scope
Applies to:
- HTML documents (any single file) > **300 lines** OR expected > **40 KB**
- HTML dashboards with > **6 content sections**
- Slide decks (Marp `.md` or PPTX) with > **3 slides**
- Any report/briefing where the user says "comprehensive", "detailed", "full", "workshop", "board-ready", or supplies a long input

If in doubt → treat as large. Plan-first has no downside; truncation does.

---

## The Protocol (MUST follow, in order)

### Step 1 — Plan in Markdown FIRST
Before writing any HTML or slide output, create a planning file in Markdown:

**For HTML:** `<output-name>.plan.md`
```markdown
# <Artifact> — Build Plan
## Audience / Purpose / Template base
## Section outline (numbered)
1. Header / hero — ~N lines of HTML
2. Section A — ~N lines
3. Section B — ~N lines
...
## Data sources (queries, inputs, MD content files)
## Chunking plan (which chunks, in what order)
## Total estimated line count
```

**For decks:** `<deck-name>.plan.md` + per-slide MD files
```
<deck-name>.plan.md         # deck-level outline, sizing band, narrative arc
slides/01-title.md          # one MD file per slide: title, bullets, presenter notes
slides/02-context.md
slides/03-evidence.md
...
```

Share the plan with the user for confirmation ONLY if the user asked for planning; in auto mode proceed once the plan file is written.

### Step 2 — Build Chunks
- Build the HTML or deck in discrete chunks, one per response/tool call cycle.
- Each chunk is a complete, syntactically-valid slice (full section, full slide, full CSS block) — never mid-tag, never mid-rule.
- Use the Write tool to create the file skeleton first (head + style + footer), then `Edit` to append sections one at a time.
- After each chunk, read the file size. If approaching the budget, pause and split the next chunk further.

### Step 3 — Merge + Integrate
- Once all chunks are written, read the full file end-to-end.
- Verify:
  - All opening tags have matching close tags
  - CSS selectors all resolve to real classes/IDs used in markup
  - No placeholder text (`{{TODO}}`, `TBD`, "lorem ipsum")
  - No duplicated sections or stale copy
  - Single palette (executive OR dark, never mixed)

### Step 4 — Review Before Marking Complete
Thorough review is mandatory. The artifact is NOT complete until:
- [ ] File opens offline (no `http://`, `https://`, `cdn.` references except optional Google Fonts)
- [ ] Print layout works (if briefing-style)
- [ ] All sections from the plan are present and ordered correctly
- [ ] Spelling / grammar pass
- [ ] Brand conformance (palette, fonts, footer per `.claude/rules/brand/visual-identity.md`)
- [ ] Decks only: every slide has presenter notes; slide count matches sizing band
- [ ] Evidence block or version footer present
- [ ] For DB-driven HTML: XSS-safe escaping of all DB values

Only after ALL checks pass can the assistant report "done / complete / ready".

---

## Non-Negotiable Rules

1. **NEVER write a large HTML/deck in a single tool call.** Chunk it.
2. **NEVER mark complete on a length-limit-truncated response.** If you see a truncation, re-plan with smaller chunks and restart from the last clean section.
3. **NEVER skip the MD plan file** for anything crossing the Scope thresholds, even if the user didn't explicitly ask for a plan.
4. **NEVER skip per-slide MD files** for decks > 3 slides — one MD per slide is mandatory.
5. **NEVER claim "done" before running the Step 4 checklist.**
6. **ALWAYS keep the plan file and slide MDs alongside the output** (same folder or an adjacent `plan/` subfolder). They are part of the deliverable — they let a future session rebuild or extend the artifact without starting over.
7. **ALWAYS announce the chunking plan** in user-facing text before writing the first chunk, so the user can redirect before tokens are spent.

---

## Integration Points

| Skill | How this rule applies |
|---|---|
| `html-generation` | Applies to any template-based or freshly-generated HTML crossing the Scope thresholds. Templates in `templates/` are themselves examples of "fully-reviewed large artifacts" and may serve as the skeleton without additional planning, but content replacement still follows chunked editing. |
| `deck-generation` | Applies to every deck in the **standard (7–10 slides)** and **detailed (10–12 slides)** bands — i.e., anything larger than the ≤3-slide summary. Per-slide MD files under `slides/` are mandatory for these bands, plus a `<deck>.plan.md` sibling. Summary decks (≤3 slides) are exempt. |
| `first-principles` | Applies whenever the first-principles analysis artifact crosses 300 lines — which is typical for Strategic-deep research. Plan file MUST list all phase sections and expected size before generation. |

---

## Enforcement

- This rule is auto-loaded via `.claude/rules/` directory on every session.
- `html-generation`, `deck-generation`, and `first-principles` SKILL.md files link to this rule and echo its Step-4 checklist in their "Must Do" sections.
- Any session where an HTML/deck output was truncated MUST log a `_learnings.md` entry in the relevant skill.
- Before claiming "done" on any large artifact, the assistant MUST run the Step 4 review checklist against the output and the accompanying plan/slide MD files.

---

## Why This Rule Exists

"Response hit length limit" is the single most expensive failure mode for large HTML and deck generation — it silently truncates output, leaves half-closed tags, breaks offline rendering, and wastes an entire session's tokens. Root cause: trying to emit the whole artifact in one shot instead of planning + chunking. Plan-in-Markdown-first makes the artifact auditable, resumable, and reviewable BEFORE the long-generation phase begins.

## How to Apply

When a request arrives that crosses the Scope thresholds:
1. Announce the chunking plan in one short paragraph to the user
2. Write `<name>.plan.md` (and `slides/NN-*.md` for decks)
3. Write the skeleton file (head + footer only)
4. Edit-append one section/slide at a time
5. Run the Step 4 review checklist
6. Only then report completion — with the plan file path, the final artifact path, and byte count
