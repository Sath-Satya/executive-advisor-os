<!-- TEMPLATE: brand-deck
     CATEGORY: Brand / Guidelines
     USE WHEN: presenting or distributing SponAItech brand guidelines to partners, contractors, or new team members
     SLIDE COUNT: 12
     PALETTE: SponAItech full — exec cream and dev dark, both palettes shown
     RENDER: marp --pptx 40-brand-deck.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&family=DM+Serif+Display&family=DM+Mono&display=swap');

  /* === BASE — executive cream side === */
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #f7f4ef;
    color: #1c1a18;
    padding: 52px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', serif;
    color: #0e1b2e;
    font-size: 2.1em;
    letter-spacing: -0.4px;
    margin-bottom: 0.2em;
  }
  h2 { color: #0e1b2e; font-size: 1.3em; font-weight: 600; margin-bottom: 0.5em; }
  h3 { color: #b8965a; font-size: 1.0em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.87em; }
  ul { margin-top: 0.4em; }
  li { margin-bottom: 0.4em; line-height: 1.6; }
  code { font-family: 'DM Mono', monospace; background: #ede8df; color: #0e1b2e; padding: 0.15em 0.45em; border-radius: 3px; font-size: 0.88em; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #6b6560; }

  /* === LEAD — dark panel title slide === */
  section.lead {
    background: #0a0e14;
    color: #d0d8e4;
  }
  section.lead h1 { font-size: 2.9em; color: #ffffff; }
  section.lead h2 { color: #3b9eff; font-size: 1.1em; }
  section.lead p { font-size: 1.1em; color: #8899ac; margin-top: 0.4em; }

  /* === DEV DARK — dev/product slides === */
  section.dev {
    background: #111820;
    color: #d0d8e4;
  }
  section.dev h1, section.dev h2 { color: #ffffff; }
  section.dev h3 { color: #3b9eff; }
  section.dev strong { color: #ffffff; }
  section.dev em { color: #8899ac; }
  section.dev footer { color: #556677; }
  section.dev code { background: #1e2a38; color: #d0d8e4; }

  /* === COLOR PALETTE SWATCHES === */
  .swatch-row { display: flex; gap: 0.7em; margin-top: 1em; flex-wrap: wrap; }
  .swatch { border-radius: 6px; padding: 0.8em 1em; min-width: 110px; }
  .swatch strong { display: block; font-family: 'DM Mono', monospace; font-size: 0.75em; margin-top: 0.3em; }
  .swatch em { font-size: 0.7em; }

  /* === TYPOGRAPHY DEMO === */
  .type-row { margin-top: 0.8em; }
  .type-sample { border-left: 3px solid #b8965a; padding-left: 1em; margin-bottom: 0.9em; }
  .type-sample.dev-accent { border-color: #3b9eff; }
  .type-label { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #6b6560; margin-bottom: 0.2em; }

  /* === DO / DON'T COLUMNS === */
  .do-dont { display: flex; gap: 2em; margin-top: 0.8em; }
  .do { flex: 1; border-left: 4px solid #2dd4a0; padding-left: 1em; }
  .dont { flex: 1; border-left: 4px solid #f06070; padding-left: 1em; }
  .do h3 { color: #2dd4a0; }
  .dont h3 { color: #f06070; }

  /* === APPLICATIONS DEMO === */
  .app-card { background: #111820; color: #d0d8e4; border-radius: 8px; padding: 1em 1.2em; margin-top: 0.6em; }
  .app-card strong { color: #3b9eff; font-size: 0.85em; font-family: 'DM Mono', monospace; text-transform: uppercase; }
---

<!-- _class: lead -->

# SponAItech Brand Guidelines

**For Partners, Contractors, and Team Members**

*v2.0 · April 2025 · sponaitech.com*

<!--
SPEAKER NOTES — SLIDE 1 (Title — Dark)
This slide uses the dark dev palette — deep navy background, white headline, electric blue accent. It is the SponAItech "developer aesthetic" that anchors the brand in the tech-forward positioning.

This brand guidelines deck is delivered to: new team members in Week 1 onboarding, contractors and designers before any visual output, and partners who will co-brand or reference SponAItech in their materials.

The deck covers the full SponAItech brand system: story (where the brand comes from), logo rules, color palette (both exec cream and dev dark), typography, voice, imagery, dos and don'ts, and real-world applications. It is not a 200-page brand bible — it is a reference deck that a designer or writer can use in 30 minutes to produce on-brand work.

Two palette philosophy: SponAItech intentionally uses two coordinated palettes — Executive Cream for boardroom-facing materials (board decks, proposals, case studies) and Dev Dark for developer-facing and product materials (API docs, tech blogs, demo UIs). Both are official. Choosing between them depends on the audience, not preference.
-->

---

## Brand Story — Why We Exist

SponAItech was built on a belief that enterprise organizations have been underserved by two extremes: massive consultancies that are slow and expensive, and AI startups that move fast but do not understand the enterprise world.

**The founding conviction:** AI-powered consulting can be both fast and enterprise-grade — if the person building it has actually lived inside the organizations they serve.

**24 years of enterprise IT. 18 years of healthcare. 6 years of Salesforce. AI-native from day one.**

*The brand expresses this paradox: the speed of a startup with the credibility of a veteran.*

<!--
SPEAKER NOTES — SLIDE 2 (Brand Story — Cream)
This slide uses the executive cream palette — warm background, navy headline, gold accent. This is the SponAItech "boardroom aesthetic" used for client-facing and executive-level materials.

The brand story is not marketing copy — it is the reason the visual identity makes the choices it does. Understanding the story helps designers, writers, and partners make better decisions when they face situations the guidelines do not explicitly cover.

The "paradox" framing is intentional and must be maintained across all brand expressions: speed is usually associated with startups (casual, colorful, playful). Credibility is associated with established firms (conservative, serif, slow). SponAItech's visual identity holds both in tension — using DM Serif Display (classic, credible) alongside the electric blue accent (modern, confident) to express this paradox visually.

When delivering this to a designer: tell the story, then show the visual system. Designers who understand the brand story make better decisions on the 20% of cases the guidelines do not cover.
-->

---

## Logo Rules

**The SponAItech wordmark:**

- ● Always use the approved SVG or PNG — never recreate the logo in another typeface
- ● Minimum size: 120px wide on screen; 1.5 inches on print
- ● Clear space: equal to the height of the "S" in SponAItech on all four sides
- ● Approved background colors: `#f7f4ef` (cream), `#0a0e14` (deep navy), `#ffffff` (white)
- ● Never place on a busy photographic background
- ● Never rotate, stretch, or apply effects (shadows, gradients, outlines)

**File locations:** `[brand asset repo link]` — dark version, light version, favicon, social crops

*When in doubt: use the dark version on cream backgrounds, white version on dark backgrounds*

<!--
SPEAKER NOTES — SLIDE 3 (Logo Rules)
The logo rules exist because well-intentioned people make harmful logo decisions. The most common violations: stretching the wordmark to fit a container, placing the logo on a colorful gradient background, and recreating the logo in a similar typeface because the original file is not accessible.

The "never recreate" rule: the DM Serif Display typeface that resembles the wordmark is available on Google Fonts, which means a designer could manually typeset something that looks close but is not the official wordmark. Close is not correct. Always use the approved file.

The clear space rule: clear space is the breathing room around the logo that prevents it from being visually crowded by adjacent elements. The height of the "S" character in the wordmark is the minimum clear space unit — this is a proportional rule that works at any size.

Approved backgrounds: these three backgrounds were tested for contrast compliance (WCAG AA minimum). The cream and white backgrounds with the dark wordmark pass at any size. The navy background with the white wordmark passes at the minimum logo size. Do not place the dark wordmark on dark backgrounds or the white wordmark on light backgrounds.

Asset access: replace the brand asset repo link with the actual location before distributing this deck. All recipients of this guidelines deck should have access to the brand assets within 24 hours of receiving the deck.
-->

---

## Color Palette — Executive Cream Side

<!-- This is a cream palette slide -->

<div class="swatch-row">
  <div class="swatch" style="background:#f7f4ef; border:1px solid #c8c0b0;">
    Background<br><strong>#f7f4ef</strong><em>Warm Cream</em>
  </div>
  <div class="swatch" style="background:#0e1b2e; color:#d0d8e4;">
    Heading<br><strong>#0e1b2e</strong><em>Deep Navy</em>
  </div>
  <div class="swatch" style="background:#b8965a; color:#fff;">
    Accent<br><strong>#b8965a</strong><em>Gold</em>
  </div>
  <div class="swatch" style="background:#6b6560; color:#fff;">
    Muted<br><strong>#6b6560</strong><em>Warm Gray</em>
  </div>
  <div class="swatch" style="background:#ffffff; border:1px solid #e0d8cc;">
    Surface<br><strong>#ffffff</strong><em>White</em>
  </div>
</div>

**Use for:** board decks, proposals, client reports, case studies, printed materials

*Gold accent is used for dividers, kpi borders, and decorative elements — not for body text*

<!--
SPEAKER NOTES — SLIDE 4 (Color Palette — Cream)
The executive cream palette is the primary palette for all client-facing written communications. It conveys credibility, warmth, and professionalism. The choice to use cream rather than white reflects the brand's positioning as experienced and considered — not clinical or sterile.

The gold accent (#b8965a) is derived from the warm undertones of the cream background. It is not a primary color — it is an accent used sparingly. Overuse of gold (for example, highlighting every heading in gold) reads as trying too hard. Use it for: left-border accents on KPI cards, section dividers in printed reports, and decorative graphic elements.

Color accessibility: the deep navy (#0e1b2e) on the cream background (#f7f4ef) passes WCAG AA contrast requirements (contrast ratio: 11.8:1). The gold on cream (3.2:1) passes AA for large text only — do not use gold for body text. This is why the guideline says "not for body text."

Palette consistency: never mix executive cream and dev dark elements on the same slide. The two palettes are designed to coexist within a brand system, not to be blended on individual slides. A cream slide with a dark navy background box is a palette violation.
-->

---

<!-- _class: dev -->

## Color Palette — Dev Dark Side

<div class="swatch-row">
  <div class="swatch" style="background:#0a0e14; color:#d0d8e4; border:1px solid #1e2a38;">
    Background<br><strong>#0a0e14</strong><em>Deep Navy</em>
  </div>
  <div class="swatch" style="background:#111820; color:#d0d8e4;">
    Surface<br><strong>#111820</strong><em>Dark Panel</em>
  </div>
  <div class="swatch" style="background:#3b9eff; color:#0a0e14;">
    Electric Blue<br><strong>#3b9eff</strong><em>Primary Accent</em>
  </div>
  <div class="swatch" style="background:#a78bfa; color:#0a0e14;">
    Soft Purple<br><strong>#a78bfa</strong><em>AI Accent</em>
  </div>
  <div class="swatch" style="background:#2dd4a0; color:#0a0e14;">
    Mint Green<br><strong>#2dd4a0</strong><em>Success</em>
  </div>
</div>

**Use for:** technical docs, developer blogs, product UI, code-heavy presentations, API reference

*Electric blue is the primary accent — purple and mint are used for secondary signals*

<!--
SPEAKER NOTES — SLIDE 5 (Color Palette — Dev Dark)
This slide itself uses the dev dark palette to demonstrate the system in context. Every element on this slide is an example of the dev dark guidelines in use.

The dev dark palette is the SponAItech "product" aesthetic — used wherever SponAItech is communicating in a technical register. The deep navy background conveys focus and professionalism without the corporate formality of the cream palette.

Electric blue (#3b9eff) is the primary action color: links, interactive elements, borders on active states, and section headings in technical content. It is bright enough to read clearly on dark backgrounds and specific enough to feel engineered rather than generic.

Soft purple (#a78bfa) is the AI-specific accent. It is used to call out AI-related features, agent names, or machine-generated content. This signals that SponAItech uses a consistent visual language for AI vs. human-authored content — a transparency principle expressed visually.

Mint green (#2dd4a0) is the success color: completed states, passing tests, go indicators, positive metrics. It is never used for decorative purposes — only for success states. This gives it semantic weight that makes it immediately readable in dashboards and status displays.

The three-color maximum per element: no single component in the dev dark palette should use more than three colors. Background + primary accent + one secondary signal. More than three creates visual noise that undermines the clean, professional aesthetic.
-->

---

## Typography — The Type System

<div class="type-row">
  <div class="type-sample">
    <div class="type-label">Display / Headings — DM Serif Display</div>
    <span style="font-family:'DM Serif Display',serif; font-size:1.6em; color:#0e1b2e; letter-spacing:-0.3px;">Enterprise Experience, Startup Speed</span>
  </div>
  <div class="type-sample">
    <div class="type-label">Body — DM Sans 400 / 600</div>
    <span style="font-family:'DM Sans',sans-serif; font-size:1.1em; color:#1c1a18;">We build production-ready systems that ship and run. AI-powered development without the abstraction.</span>
  </div>
  <div class="type-sample">
    <div class="type-label">Code / Mono — DM Mono</div>
    <code>GET /api/v1/claims → 200 OK · 42ms</code>
  </div>
</div>

*Google Fonts — DM family — free, no licensing required*

<!--
SPEAKER NOTES — SLIDE 6 (Typography)
The DM typeface family (DM Serif Display, DM Sans, DM Mono) is a coordinated type system by Colophon Foundry, distributed free via Google Fonts. The three weights cover every use case: display headlines, body text, and technical/code content.

DM Serif Display: used only for display-size headings — slide titles, report section headers, pull quotes. Never for body text or small-size headings. The serif character of this face communicates credibility and authority — it is the typographic equivalent of a firm handshake.

DM Sans: the workhorse typeface. Used at 400 (regular) for body text and at 600 (semibold) for subheadings, labels, and emphasis. Never use bold (700) in DM Sans for body text — it reads as shouting. Semibold is the appropriate emphasis weight.

DM Mono: reserved for code, file paths, technical identifiers, timestamps, and version numbers. The monospace setting communicates "this is technical content." Using DM Mono for non-technical content (like pull quotes or footnotes) dilutes this signal.

System fallbacks for web: 'DM Sans', system-ui, -apple-system, sans-serif. If DM Sans fails to load, system-ui renders at consistent quality across platforms. Never fall back to Arial or Times — they undermine the brand positioning.

Never use: Comic Sans, Papyrus, Impact, Helvetica Neue (too generic), or any condensed display face. The anti-pattern list exists because these faces have been proposed in the past.
-->

---

## Voice — How SponAItech Speaks

**Professional but approachable.** Enterprise credibility without corporate stiffness.

<div class="do-dont">
  <div class="do">
    <h3>Write This</h3>
    <ul>
      <li>We build claims processing tools that reduce review time by 42%</li>
      <li>The API handles 2,000 requests per minute on a $150/month Azure plan</li>
      <li>Three things went wrong — here is how we fixed them</li>
    </ul>
  </div>
  <div class="dont">
    <h3>Not This</h3>
    <ul>
      <li>We leverage cutting-edge AI to synergize your workflow paradigms</li>
      <li>Our scalable, enterprise-grade platform delivers value at speed</li>
      <li>Everything is going great — excited to share our journey</li>
    </ul>
  </div>
</div>

<!--
SPEAKER NOTES — SLIDE 7 (Voice)
Voice is the hardest brand element to enforce because it lives in writing, not visuals. The do/don't format makes the contrast stark and actionable.

Write This — the three examples share a pattern: specific numbers, concrete outcomes, and honest framing. "42% reduction in review time" is a measurement. "2,000 requests per minute on $150/month" is a cost-performance statement. "Three things went wrong — here is how we fixed them" is transparency.

Not This — the three anti-examples share a pattern: abstract claims, marketing jargon, and positivity without evidence. "Leverage cutting-edge AI" has no specific meaning and can be said by any company. "Scalable, enterprise-grade platform" is pure buzzword assembly. "Everything is going great — excited to share our journey" is emotional manipulation without substance.

The voice rules from the brand identity document:
- Active voice always ("We build X" not "X is built by us")
- No exclamation marks in professional copy
- Numbers are credibility signals — use them
- Prefer: build, solve, automate, streamline, deliver
- Avoid: leverage, synergy, paradigm, cutting-edge, revolutionary, journey

The voice is non-negotiable in client-facing materials. In internal Slack messages and informal team communication, natural conversational tone is fine. The voice guidelines apply to: case studies, proposals, LinkedIn posts, email campaigns, website copy, and any document that reaches a prospect or client.
-->

---

## Imagery Principles

**Photography and illustration philosophy:**

- ● **People over product** — show the humans doing the work, not abstract technology diagrams
- ● **Real environments** — genuine office or remote work settings, not stock photo studios
- ● **Diversity and inclusion** — reflect the range of professionals in the industries we serve
- ● **No decorative AI art** — purple neural networks and glowing circuits are clichéd and undermine credibility

**Approved image treatment:**
- Consistent overlay tint using the palette's primary dark color (opacity 20–40%)
- Desaturation of overly vibrant stock photography (reduce saturation 40–60%)
- Never crop faces awkwardly at the edges — center the person

<!--
SPEAKER NOTES — SLIDE 8 (Imagery)
The imagery guidelines address a specific failure mode common in AI consulting brand materials: defaulting to clichéd "AI imagery" — glowing brains, neural network diagrams, purple circuits, and disembodied hands touching digital screens. This aesthetic signals that the brand is a newcomer trying to look futuristic rather than a practitioner who delivers real results.

"People over product" is the guiding principle. SponAItech's value is human expertise amplified by AI, not AI in the abstract. Photography should show people working — in front of screens, in meetings, writing on whiteboards. The technology is in the background, not the subject.

Real environments: stock photography of perfect-lighting studio setups reads as artificial. Genuine remote work environments (a home office with a second monitor and coffee) or realistic office settings (imperfect lighting, personal items) communicate authenticity.

The AI art prohibition: generative AI imagery (Midjourney, DALL-E) is not banned categorically, but any AI-generated image must be reviewed for: accuracy of depicted environments (AI often generates incorrect or impossible technology setups), potential bias in depicted people, and alignment with the "real environments" principle.

Image sourcing: preferred sources are Unsplash (free) and Getty Images (licensed). When using any stock photography, verify the license allows commercial use. Never use images from a web search without verifying the license.
-->

---

<!-- _class: dev -->

## Do's — On-Brand Examples

**Slide headline:** "Claims Processing — Reduced From 4.2 Days to 6 Hours"

**LinkedIn post opener:** "We just deployed a claims routing model that processes 800 claims per hour. Here is the one architectural decision that made it possible..."

**Email subject:** "How Meridian cut their claims review backlog by 68%"

**UI element naming:** `ClaimsRouter` · `EnrollmentWizard` · `MemberDashboard`

**Error message:** "Claim not found. Check the claim ID or contact support at [email]."

*Every example is: specific, result-oriented, jargon-free*

<!--
SPEAKER NOTES — SLIDE 9 (Do's — Dev Dark)
This slide uses the dev dark palette because the examples skew technical — UI naming, error messages, LinkedIn posts about technical implementations.

The examples are not hypothetical — they are the type of content SponAItech actually produces. Each demonstrates a specific brand voice principle:

"Claims Processing — Reduced From 4.2 Days to 6 Hours": a result-first headline with specific numbers. The unit change (days to hours) is more visceral than a percentage — it conveys a qualitative shift, not just an improvement.

LinkedIn post opener: leads with the metric, then offers the insight. This is the SponAItech content formula: result → explanation → one key decision. The "here is the one architectural decision" hook creates anticipation without clickbait.

Email subject: third-person result ("How Meridian cut...") is often stronger than first-person ("How we helped Meridian...") for cold email because it focuses on the client outcome, not SponAItech's achievement.

UI element naming: PascalCase, noun-focused, domain-specific. Not "ClaimsProcessingSystemControllerV2" — that is internal implementation naming, not brand-aligned component naming.

Error message: specific, actionable, human. Not "Error 404" or "Something went wrong." The contact path is provided. This is brand-voice applied to UX writing.
-->

---

## Don'ts — Off-Brand Examples

<div class="do-dont">
  <div class="dont">
    <h3>Visual Don'ts</h3>
    <ul>
      <li>Purple AI neural network hero images</li>
      <li>More than 3 colors in one component</li>
      <li>Drop shadows heavier than <code>0 8px 24px rgba(0,0,0,0.3)</code></li>
      <li>Animated backgrounds or particle effects</li>
      <li>Mixing cream and dark palettes on one slide</li>
    </ul>
  </div>
  <div class="dont">
    <h3>Voice Don'ts</h3>
    <ul>
      <li>"We leverage synergies to deliver value"</li>
      <li>Exclamation marks in professional copy</li>
      <li>"Cutting-edge" / "revolutionary" / "paradigm-shifting"</li>
      <li>Passive voice in capability statements</li>
      <li>Claims without specific numbers</li>
    </ul>
  </div>
</div>

<!--
SPEAKER NOTES — SLIDE 10 (Don'ts)
The don'ts slide is the most referenced slide in any brand guidelines deck — designers and writers return to it when they are uncertain about a choice. Keep it concrete and specific.

Visual don'ts:

Purple AI neural network hero images: this is the most common AI brand cliché. It signals "we know AI is a trend" rather than "we are practitioners who build real AI systems." If the SponAItech brand ever feels indistinguishable from any other AI startup, this is the first thing to check.

More than 3 colors in one component: the 3-color maximum is a design discipline rule. Background + primary + one accent. Adding a fourth color creates visual complexity that competes with the content.

Drop shadow limit: heavier shadows feel dated and heavy. The specified maximum (`0 8px 24px rgba(0,0,0,0.3)`) produces a subtle depth effect that reads as polished without feeling like a PowerPoint template from 2015.

Animated backgrounds/particles: these reduce accessibility (motion sensitivity) and signal "startup trying to look impressive" rather than "practitioner delivering results."

Palette mixing: cream and dark elements on the same slide create visual incoherence. The exception is a quotation call-out box using a contrasting surface — but even then, the treatment must be intentional and referenced in the guidelines.

Voice don'ts: all covered in the Voice slide but repeated here as a quick reference checklist for writers reviewing their own work.
-->

---

## Applications — Brand in the Wild

**Exec Cream — Client proposal cover:**
<div style="background:#f7f4ef; border:1px solid #c8c0b0; border-radius:6px; padding:0.8em 1.2em; margin-top:0.5em;">
  <span style="font-family:'DM Serif Display',serif; font-size:1.4em; color:#0e1b2e;">Salesforce Optimization Proposal</span><br>
  <span style="font-family:'DM Sans',sans-serif; font-size:0.85em; color:#6b6560;">Meridian Health · April 2025 · Prepared by SponAItech</span>
</div>

**Dev Dark — API documentation header:**
<div class="app-card">
  <strong>GET /api/v1/claims</strong><br>
  <span style="font-size:0.88em; color:#8899ac;">Returns paginated list of claims. Requires Bearer token. Rate limit: 100 req/min.</span>
</div>

**Both palettes in one brand system — not in competition*

<!--
SPEAKER NOTES — SLIDE 11 (Applications)
This slide is the "show, don't tell" payoff. After 10 slides of rules, the audience sees what the brand looks like in real use cases.

The exec cream example (proposal cover): demonstrates how the typeface combination works at a small scale — DM Serif Display for the title, DM Sans for the metadata line. The border provides structure without heavy visual weight. The warm cream background reads as professional and personal.

The dev dark example (API docs): demonstrates the code-first aesthetic. The `GET /api/v1/claims` route is in DM Mono — immediately identifiable as technical content. The description uses DM Sans in the muted text color. No decorative elements. Clean, scannable, functional.

The "both in one system — not in competition" note is important. Partners and contractors sometimes assume they must choose one palette. They do not. A client proposal (cream) can reference the product documentation (dark) and they coexist within the SponAItech brand system because the underlying type choices and spacing systems are shared.

The most common misapplication: using the dev dark palette for a board deck because it "looks more impressive." The board audience expects executive cream — deep navy screens can be harder to read in bright conference rooms, and the aesthetic signals "startup" rather than "enterprise partner."
-->

---

<!-- _class: lead -->

# Brand Assets and Contact

**Asset library:** `[GitHub brand assets repo link]`

*Contains: logo SVG/PNG (dark + light + favicon), brand color hex codes, DM type specimens, PowerPoint template, HTML template*

**Brand questions:** `[brand@sponaitech.com]`

**Guidelines version:** v2.0 · April 2025 · Review cycle: annual

*These guidelines are approved for use by SponAItech employees, approved contractors, and registered partners. Not for public distribution.*

<!--
SPEAKER NOTES — SLIDE 12 (Resources — Dark)
End on the dark palette to bookend the deck — title and close on dark, middle content on cream. This creates a visual rhythm that reinforces the two-palette system.

The asset library link must be active before this deck is distributed. A brand guidelines deck that links to an empty repository is worse than no guidelines — it signals that brand is aspirational, not operational.

The asset library should contain, at minimum: the wordmark in SVG and PNG for both dark and light versions, the color hex codes in a design tokens file (compatible with Figma), the font files or a Google Fonts link, a PowerPoint template (.pptx) using the exec cream palette, and an HTML document template using the dev dark palette.

Brand questions email: this should route to the person responsible for brand decisions — currently the founder. Brand questions are not trivial — a contractor asking whether they can use a different blue "just for this one project" needs a clear no with an explanation. Unanswered brand questions default to "close enough" decisions that accumulate into brand drift.

Distribution restriction: this deck is marked as not for public distribution. The brand guidelines contain specific color codes, typography choices, and visual examples that competitors could use to create confusingly similar brands. Share only with people who have a legitimate need to produce on-brand SponAItech materials.

Annual review: brand guidelines should be reviewed annually against three questions: Does the visual system still reflect the brand's positioning? Have any of the referenced tools or resources changed? Are there new use cases (video, social, physical) that the guidelines do not cover?
-->
