---
name: html-generation
description: Generate self-contained, polished HTML documents — executive briefings, board reports, one-pagers, research dashboards, and shareable standalone pages — styled with the Executive Advisor OS cream-navy-gold palette. Use when the user asks for a boardroom-ready HTML brief, a research dashboard, a status page, a board report, or any standalone .html artifact that must open offline in any browser with zero external dependencies. Ships with 80+ production-quality starter templates in `templates/` — prefer cloning a template over generating from scratch. Large artifacts MUST follow `.claude/rules/large-artifact-generation.md` (plan-in-MD → chunk → merge → review).
version: 1.3.0
---

## Template library (use this first)

This skill ships with **80+ production-quality templates** in `templates/` covering executive briefings, board reports, dashboards, long-form analyses, and research artifacts. **Prefer cloning a template over generating from scratch** — they use the Executive Advisor OS cream-navy-gold palette, are accessibility-tested, print-safe, and fully offline.

Browse the catalog: [`templates/INDEX.md`](templates/INDEX.md)

**Workflow:**
1. Read `templates/INDEX.md` and match the user's need to the closest template
2. Copy the file to the output path
3. Replace `{{VERSION}}`, `{{DATE}}`, and fictional placeholder content ("Northwind Capital" / "Meridian Health" / "Helix") with real content
4. Verify the edited file still opens offline (no new external references were introduced)
5. Report which template was used as the base

If no template matches (rare), fall back to the process below.


# HTML Generation

## When to Use

- User wants a boardroom-ready HTML briefing
- Generating an executive summary, detailed report, or one-pager in HTML
- Creating a project documentation page (module docs, API reference, architecture overview)
- Producing a dashboard or status tracker HTML
- Converting Markdown research outputs into polished, emailable HTML

Do NOT use for generating slide decks — use `deck-generation` instead.

## Large artifact contract (read before generating)

If the output crosses ANY of these thresholds → **MUST follow `.claude/rules/large-artifact-generation.md`** (plan-in-Markdown first → chunked build → merge → Step-4 review checklist):

- HTML file > 300 lines OR > 40 KB expected
- Research dashboard or briefing with > 6 content sections
- User said "comprehensive", "detailed", "full", "board-ready", or supplied long source content

Announce the chunking plan to the user in one short paragraph before writing the first chunk. Write the `<output>.plan.md` companion file alongside the artifact.

## Process

1. **Clarify audience + purpose** — board, client, internal team, or end user. The visual weight and tone follow the audience.
2. **Select the template** — briefing, dashboard, or doc-page (see §Templates).
3. **Inline all assets** — CSS, fonts (Google Fonts link OR inline fallback), tiny SVGs. No external JS frameworks, no CDN images.
4. **Apply the executive palette** — follow `.claude/rules/brand/visual-identity.md` (cream-navy-gold; no dark-theme sections in exec-facing outputs).
5. **Write the HTML** — semantic tags, accessible headings, print-safe layout.
6. **Verify offline** — grep the output for `http://`, `https://`, and `cdn.` — none should appear except optional Google Fonts (which degrades gracefully via fallback stack).
7. **Add metadata footer** — version, date, author/context at the bottom.

## Templates

### 1. Briefing HTML (exec-facing)
- Single column, 760–820px max width
- Header: title + date + version
- Body: sections with subtle gold/navy dividers
- Footer: context block (audience, goal, version)
- Palette: cream `#f7f4ef` / navy `#0e1b2e` / gold `#b8965a` (only palette used in this OS)
- Typography: `'Cormorant Garamond'` (headings) + `'DM Sans'` (body) + `'DM Mono'` (meta) with Georgia / system-ui / system-mono graceful fallback
- Print stylesheet: A4 portrait, margins 2cm

### 2. Research dashboard HTML
- Top bar: brand + last-updated timestamp
- Stats row: 3–4 stat cards with large numbers
- Main grid: research cards with status badges (active / completed / needs-review)
- Cards have border-left gold accent; status badges use the status-indicator colors from `visual-identity.md`
- Empty state when no research exists yet
- Regenerated after every completed research session per the `CLAUDE.md` dashboard contract

### 3. Long-form analysis / report page
- Single column content flow with section dividers
- Callout boxes for risks, counter-arguments, and "INFERRED" notes
- Anchor links for every heading (auto-scroll targets)
- Collapsible "How we got here" appendix for Strategic-deep first-principles outputs

## Standards

### Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{descriptive title}}</title>
  <style>/* all CSS inline */</style>
</head>
<body>
  <!-- semantic content -->
  <footer>{{version, date, context}}</footer>
</body>
</html>
```

### CSS Rules
- Use CSS custom properties (`--navy`, `--gold`, etc.) for theming
- Box-sizing: `border-box` universally
- No `!important` unless overriding print styles
- Minimum body font size: 14px
- Line-height: 1.5–1.7 for body, 1.2–1.3 for headings
- Use `rem` / `em` for typography, `px` for borders

### Accessibility
- Every image has `alt` (or `alt=""` if decorative)
- Color contrast ≥ 4.5:1 for body text (WCAG AA)
- Keyboard-navigable if interactive
- Use `<main>`, `<nav>`, `<section>`, `<article>`, `<footer>` — not `<div>` for everything

### Brand Alignment
Every exec-facing output uses the cream-navy-gold executive palette. There is no second palette in this OS — do not mix in dark-theme sections.

```
--cream: #f7f4ef; --cream2: #ede9e2;
--navy: #0e1b2e; --navy2: #152440;
--gold: #b8965a; --gold2: #d4ab72;
--ink: #1c1a18; --muted: #6b6560;
--border: rgba(184,150,90,0.18);
```

Status indicators on dashboards use the reserved status palette: active `#f0a050`, completed `#2dd4a0`, needs-review `#f06070`, archived `#8899ac`.

## Must Do

- Inline ALL CSS — no `<link rel="stylesheet">` to external files except Google Fonts
- Use semantic HTML5 tags
- Include a version + date footer
- Include a `<meta name="viewport">` for mobile
- Test that the file opens with zero network access (file://)
- Keep to a single file — no separate .css/.js siblings
- **For any artifact crossing the thresholds in §"Large artifact contract":** follow `.claude/rules/large-artifact-generation.md` end-to-end — plan MD, chunked build, Step-4 review checklist before claiming "done"

## Must Not Do

- Never use CDN JavaScript (jQuery, React, Tailwind CDN, etc.)
- Never reference external images by URL — inline SVG or base64 only for tiny assets; reference local asset paths only if explicitly allowed
- Never use inline `style="..."` on every element — use `<style>` block with classes
- Never ship HTML >100KB — if it's larger, break into sections or use a different format
- Never use generic frameworks (Bootstrap, Tailwind classes) — the OS uses custom CSS only
- Never use emojis in headings or titles unless the user explicitly requested it

## Common Mistakes

1. **External CDN links** — breaks offline use. Always inline.
2. **Palette drift** — reaching for any color outside cream/navy/gold + the reserved status indicators. Stay on palette.
3. **Missing viewport meta** — looks broken on mobile.
4. **No print styles** — briefings get printed; add a `@media print` block.
5. **Over-designed** — adding gradients, animations, decorative elements the user didn't ask for. Restraint = boardroom-ready.
6. **Forgotten footer** — always include version + date + context so the doc is self-describing weeks later.

## Output

Write the final HTML to the path the user specifies (or the caller's convention — e.g., `output/briefing_v{N}.html` for Executive Advisor OS). Report the file path and byte size when done.
