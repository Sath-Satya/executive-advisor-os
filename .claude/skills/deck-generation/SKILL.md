---
name: deck-generation
description: Generate presentation decks as Marp-compatible Markdown slide outlines (renderable to PPTX, PDF, or HTML via the Marp CLI) — summary decks (≤3 slides), standard (7–10), detailed (10–12), or workshop (15–20, only on explicit request). Use when the user asks for a slide deck, presentation, board deck, pitch outline, executive briefing deck, or any structured slide-by-slide artifact. Enforces sizing bands, presenter notes on every slide, and boardroom-ready narrative flow. Ships with 80+ production-quality starter templates in `templates/` — prefer cloning a template over generating from scratch. Decks > 3 slides MUST follow `.claude/rules/large-artifact-generation.md` (plan.md + per-slide MD files, chunked build, full review).
version: 1.2.0
---

## Template library (use this first)

This skill ships with **80+ production-quality Marp slide deck templates** in `templates/` covering board and executive decks, strategic reviews, pitch/sales, briefings, and research-output decks. **Prefer cloning a template over generating from scratch** — each template uses the Executive Advisor OS cream-navy-gold palette, has presenter notes on every slide, strictly respects sizing bands, and renders cleanly to PPTX/PDF/HTML via the Marp CLI.

Browse the catalog: [`templates/INDEX.md`](templates/INDEX.md)

**Workflow:**
1. Ask the user what deck type + purpose + audience
2. Read `templates/INDEX.md` and match to the closest template
3. Copy the template file to the output path
4. Replace placeholder content with the user's real material, keeping frontmatter + slide separators + presenter notes intact
5. Render hint: `marp --pptx {file}.md`
6. Report which template was used

If no template matches (rare), fall back to the process below.


# Deck Generation

## When to Use

- User asks for a slide deck, presentation, board deck, pitch, or briefing deck
- Exec-assistant `/new-research` asks for `deck_summary` or `deck_detailed`
- Converting research output into a slide narrative
- Creating a client-facing pitch or demo outline
- Building a technical architecture walkthrough as slides

Do NOT use for generating plain HTML briefings — use `html-generation` instead.

## Sizing Bands (NON-NEGOTIABLE)

| Deck type | Slide count | Use case |
|---|---|---|
| **Summary** | ≤3 slides | Elevator pitch, single-topic briefing, CTA deck |
| **Standard** | 7–10 slides | Most business presentations, client updates |
| **Detailed** | 10–12 slides | Board decks, strategic reviews, deep architecture walkthroughs |
| **Workshop** | 15–20 slides | Training, onboarding (only with explicit user request) |

If content overflows, prioritize ruthlessly — do NOT expand the slide count.

## Output Formats

### 1. Markdown slide outline (default)
```markdown
# Slide 1 — Title
**Framing statement:** one line setting up the narrative.

**Speaker notes:** what the presenter says when this slide is up.

---

# Slide 2 — Key point heading
- Point 1 (≤12 words)
- Point 2 (≤12 words)
- Point 3 (≤12 words)

**Speaker notes:** expanded narrative, data sources, objection handling.

---
```

- `---` separator between slides
- Each slide has: title, body, speaker notes
- Body: bullets, image callouts (as `[IMAGE: description]`), or a quote block
- Keep bullets tight — no paragraphs in bullets

### 2. HTML reveal slides (when requested)
- Self-contained HTML with inline CSS (follow `html-generation` rules)
- Use `<section class="slide">` per slide
- Keyboard navigation (← →) with a tiny inline JS handler
- Presenter notes in `<aside class="notes">` (hidden by default; toggleable with `N` key)
- Executive cream-navy-gold palette throughout — no dark-theme variant in this OS

### 3. PowerPoint / Keynote instructions (outline-only)
When the user will manually build the deck in PowerPoint/Keynote, produce a Markdown outline that includes:
- Title for each slide
- Body content bullets
- Speaker notes block
- Layout suggestion (`Title + 3 bullets`, `Quote`, `Two columns`, `Full-bleed image + caption`, `Comparison table`)

## Process

1. **Clarify the deck type** — summary / standard / detailed / workshop. If unclear, ask.
2. **Clarify the audience + venue** — board, investors, team, external client. Venue affects tone and visual density.
3. **Clarify the call to action** — what decision or action does this deck drive? The final slide must land there.
4. **Outline the narrative** — a one-line arc per slide BEFORE drafting any slide body.
5. **Draft slide-by-slide** — respect the sizing band.
6. **Add presenter notes on EVERY slide** — non-negotiable.
7. **Validate sizing** — count slides. If out of band, cut — don't expand.

## Slide Structures by Deck Type

### Summary deck (≤3 slides)
| # | Purpose | Content |
|---|---|---|
| 1 | Framing | Title + one-line problem statement |
| 2 | Evidence | 3 key points, max |
| 3 | CTA | Recommendation + specific next action |

### Standard deck (7–10 slides)
| # | Purpose |
|---|---|
| 1 | Title |
| 2 | Context / problem |
| 3 | Stakes — why this matters now |
| 4–6 | Core findings or approach |
| 7 | Options with trade-offs |
| 8 | Recommendation |
| 9 | Next steps |
| 10 | (Optional) Appendix / Q&A anchor |

### Detailed deck (10–12 slides)
| # | Purpose |
|---|---|
| 1 | Title |
| 2 | Opening hook |
| 3 | Context / background |
| 4–5 | Key findings |
| 6 | Risks & objections |
| 7 | Supporting data |
| 8–9 | Options / trade-offs |
| 10 | Recommendation |
| 11 | Next steps / timeline |
| 12 | Appendix (optional) |

## Standards

### Content
- Max 3 bullets per slide (exception: comparison table or ≤6-row data)
- Each bullet ≤12 words
- No paragraphs — decks are scaffolds for spoken narrative
- Numbers and dates are anchors — include them
- Every deck ends with a **specific**, **named** next action (not "consider options")

### Speaker notes
- Required on every slide, no exceptions
- Write in the presenter's voice ("I'll open by showing…")
- 80–200 words per slide
- Include source links, data caveats, likely objections

### Titles
- Title case, not sentence case
- No punctuation at end unless it's a question mark
- No colons separating topic from point — use a dash `—` instead
- ≤8 words per title

### Narrative flow
- Every deck has a single narrative spine — problem → evidence → recommendation
- Slides progress the argument; no "just for completeness" slides
- The detailed deck's appendix is for data, not extra argument

## Must Do

- Enforce sizing bands — cut content, don't expand the deck
- Presenter notes on EVERY slide
- End with a specific CTA naming the decision or next action
- Include date + version in slide 1 footer or bottom-right of each slide
- Use a `---` Markdown separator between slides (for outline format)
- Keep titles ≤8 words
- **For any deck > 3 slides:** follow `.claude/rules/large-artifact-generation.md` end-to-end — write `<deck>.plan.md` first, produce one `slides/NN-*.md` file per slide with presenter notes, then assemble the final Marp MD, then run the Step-4 review checklist before claiming "done"

## Must Not Do

- Never exceed the deck's sizing band
- Never skip presenter notes
- Never end on a "Thank you" or "Questions?" slide — always end on the CTA
- Never use emojis in slide titles unless user explicitly asks
- Never produce a deck without a clear narrative arc
- Never cram a full paragraph into a bullet

## Common Mistakes

1. **Over-stuffed slides** — 8 bullets crammed in. Cut to 3. If you can't, split the slide or cut content.
2. **No CTA** — the deck ends on "findings" with no ask. Every deck needs a specific next action.
3. **Missing speaker notes** — especially on title and section-break slides. Always include them.
4. **Sizing violation** — 4 slides for a "summary deck" or 14 for "detailed". Enforce the band.
5. **Buzzword titles** — "Strategic Considerations for Key Stakeholders". Rewrite as concrete statements.
6. **Decorative slides** — agendas, thank-yous, section dividers that add no content. Kill them in small decks.

## Output

- Default: Markdown outline at the path the caller specifies (e.g., `output/deck_summary_v{N}.md` or `output/deck_detailed_v{N}.md`)
- If HTML requested: follow `html-generation` skill's offline-safe rules
- Report: slide count, deck type, file path

## Coordination With html-generation

- If the user wants an HTML slide deck, this skill owns the structure; `html-generation` owns the visual styling and offline-safe constraints
- Presenter notes in HTML decks must be hidden by default, toggleable
