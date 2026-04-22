# Executive Advisor OS — Visual Identity

All executive-facing outputs (HTML briefings, decks, dashboards) share a single cream-navy-gold palette. This is the boardroom palette — calm, deliberate, print-safe, email-safe.

## Colors

### Primary palette (exec-facing outputs)
- **Cream:** `#f7f4ef` — background
- **Cream2:** `#ede9e2` — subtle surface variant
- **Navy:** `#0e1b2e` — headings, accents
- **Navy2:** `#152440` — deep accent
- **Gold:** `#b8965a` — emphasis, load-bearing highlights, section dividers
- **Gold2:** `#d4ab72` — hover / secondary gold
- **Ink:** `#1c1a18` — body text
- **Muted:** `#6b6560` — secondary text
- **Border:** `rgba(184,150,90,0.18)` — soft gold dividers

### Status indicators (dashboards)
- **Active (amber):** `#f0a050`
- **Completed (green):** `#2dd4a0`
- **Needs review (coral):** `#f06070`
- **Archived (muted):** `#8899ac`

## Typography

**Heading font:** `'Cormorant Garamond'`, Georgia, serif — reads as boardroom-grade, print-safe
**Body font:** `'DM Sans'`, system-ui, -apple-system, sans-serif
**Code/meta font:** `'DM Mono'`, monospace

**Offline fallback:** If Google Fonts are unavailable (air-gapped or Wi-Fi off), the system falls back gracefully to Georgia (heading), system-ui (body), and system monospace. Typography degrades but the document remains fully readable and print-safe.

**Never use:** Arial, Comic Sans, Papyrus, Impact, decorative display fonts.

## Design principles

- Cream/navy/gold always — never mix with other palettes in a single document
- Single-column briefings (760–820px max width) for readability
- Rounded corners: 8–12px for cards, 4–6px for badges
- Subtle gold dividers (1px solid `border`) — never heavy lines
- Hover states: slight lift (translateY −1 to −2px), no glow
- Consistent 8px spacing grid
- Print stylesheet: A4 portrait, 2cm margins

## Anti-patterns (NEVER)

- No generic AI-purple gradients
- No stock photo heroes
- No animated backgrounds or particles
- No more than 3 colors in any single component
- No drop shadows heavier than `0 8px 24px rgba(0,0,0,0.3)`
- No dark-theme sections in exec-facing outputs
- No external CDN assets except Google Fonts (which gracefully degrade — see Typography)
