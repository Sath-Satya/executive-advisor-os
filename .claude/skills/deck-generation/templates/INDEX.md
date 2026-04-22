# Deck Template Catalog

80 production-quality Marp slide deck templates. Each renders to PPTX, PDF, or HTML via the Marp CLI:
```bash
marp --pptx 01-board-deck-summary.md    # → .pptx
marp --pdf  01-board-deck-summary.md    # → .pdf
marp        01-board-deck-summary.md    # → .html
```

Every template has presenter notes on EVERY slide (80–200 words, 60 words for Pecha Kucha). Sizing bands strictly enforced.

## Executive Advisor OS palette lock

**For any Executive Advisor OS deck (summary or detailed, used inside `/new-research` outputs) use only the Executive cream palette templates.** The other palettes are shipped as reference-only starting points for non-exec audiences — do NOT use them for executive research output decks. See `.claude/rules/brand/visual-identity.md`.

## Usage

1. Pick the Executive cream template that matches your presentation type
2. Copy the file (`cp templates/{N}-{name}.md output/your-deck.md`)
3. Replace placeholder content with your real material
4. Keep the Marp frontmatter and slide separators intact
5. Render: `marp --pptx your-deck.md`

## Palettes

- **Executive cream** *(EA default — use this)* — `#f7f4ef` bg, navy `#0e1b2e` heads, gold `#b8965a`. Formal business decks.
- **Dark premium** *(reference-only — do NOT use for EA outputs)* — `#0a0e14` bg, white heads, electric blue or purple.
- **Clean light** *(reference-only — do NOT use for EA outputs)* — `#ffffff` bg, navy heads.
- **Dark dev** *(reference-only — do NOT use for EA outputs)* — `#0a0e14` bg, blue heads, mint accent.
- **Corporate hybrid** *(reference-only — do NOT use for EA outputs)* — cream bg, navy heads, blue or gold accent.

---

## Executive (10)
| # | File | Slides | Palette | Use when |
|---|------|:---:|---------|----------|
| 01 | `01-board-deck-summary.md` | 3 | Executive cream | 3-slide board summary for quarterly touch-point |
| 02 | `02-board-deck-detailed.md` | 12 | Executive cream | Full board deck with context/findings/recommendation |
| 03 | `03-ceo-keynote.md` | 10 | Dark premium | CEO annual address style (Bezos/Nadella tone) |
| 04 | `04-exec-briefing.md` | 7 | Executive cream | Executive briefing on a specific decision |
| 05 | `05-qbr.md` | 11 | Executive cream | Quarterly business review with commitments |
| 06 | `06-strategic-plan-deck.md` | 12 | Executive cream | Strategic plan (mission/vision/pillars/KPIs) |
| 07 | `07-annual-plan-deck.md` | 12 | Executive cream | Annual planning deck with budget + team |
| 08 | `08-investor-update-deck.md` | 9 | Executive cream | Monthly investor update with asks |
| 09 | `09-sequoia-memo.md` | 10 | Dark premium | Classic Sequoia pitch format |
| 10 | `10-seed-pitch.md` | 10 | Dark premium (purple) | Early-stage seed pitch with insight slide |

## Pitch & Sales (10)
| # | File | Slides | Palette | Use when |
|---|------|:---:|---------|----------|
| 11 | `11-series-a-pitch.md` | 12 | Dark premium | Series A raise with traction focus |
| 12 | `12-yc-style-pitch.md` | 10 | Dark premium | YC application / demo day format |
| 13 | `13-product-demo.md` | 8 | Clean light | Product demo with screen placeholders |
| 14 | `14-sales-pitch.md` | 9 | Executive cream | Enterprise sales pitch (pain→future→proof) |
| 15 | `15-partnership-pitch.md` | 8 | Corporate hybrid | Partnership proposal (us + you + joint value) |
| 16 | `16-grant-pitch.md` | 10 | Executive cream | Grant application (AHRQ SBIR structure) |
| 17 | `17-customer-overview.md` | 7 | Clean light | Customer-facing intro deck |
| 18 | `18-product-launch.md` | 11 | Executive cream | Internal launch readiness review |
| 19 | `19-case-study-deck.md` | 9 | Clean light | Single case study presentation |
| 20 | `20-roi-deck.md` | 8 | Executive cream | ROI / business case deck |

## Technical (10)
| # | File | Slides | Palette | Use when |
|---|------|:---:|---------|----------|
| 21 | `21-architecture-review.md` | 12 | Dark dev | Architecture review (current→proposed→trade-offs) |
| 22 | `22-design-review.md` | 10 | Dark dev | Design review with goals/non-goals |
| 23 | `23-postmortem-deck.md` | 9 | Dark dev (red/amber) | Incident postmortem with timeline |
| 24 | `24-tech-talk.md` | 10 | Dark premium | Conference tech talk |
| 25 | `25-brown-bag.md` | 8 | Clean light dev | Internal brown-bag session |
| 26 | `26-rfc-presentation.md` | 10 | Dark dev | RFC pitch asking for feedback |
| 27 | `27-launch-readiness.md` | 11 | Corporate hybrid | Feature launch readiness + go/no-go |
| 28 | `28-system-design.md` | 12 | Dark dev | System design deck (interview-style depth) |
| 29 | `29-competitive-analysis.md` | 10 | Corporate | Competitive landscape + positioning |
| 30 | `30-market-overview.md` | 9 | Corporate | Market size, trends, players, forecast |

## Training & Workshop (10)
| # | File | Slides | Palette | Use when |
|---|------|:---:|---------|----------|
| 31 | `31-workshop-deck.md` | 18 | Warm light | Full-day / half-day workshop facilitator deck |
| 32 | `32-training-module.md` | 12 | Light clean | Self-paced training module with practice |
| 33 | `33-onboarding-deck.md` | 15 | Executive cream | New hire week-1 onboarding |
| 34 | `34-certification-prep.md` | 14 | Clean dev | Exam/cert prep with domain breakdown |
| 35 | `35-bootcamp-lesson.md` | 10 | Light clean dev | Single bootcamp lesson |
| 36 | `36-faq-deck.md` | 10 | Clean light | FAQ explainer deck |
| 37 | `37-playbook-deck.md` | 11 | Corporate cream+gold | Operations playbook walkthrough |
| 38 | `38-knowledge-transfer.md` | 12 | Corporate hybrid | Departing-person knowledge transfer |
| 39 | `39-campaign-deck.md` | 11 | Bold creative | Marketing campaign pitch |
| 40 | `40-brand-deck.md` | 12 | SponAItech full | Brand guidelines with live examples |

## Finance (10)
| # | File | Slides | Palette | Use when |
|---|------|:---:|---------|----------|
| 51 | `51-earnings-call-deck.md` | 11 | Executive cream | Public earnings call for analysts |
| 52 | `52-fpa-review.md` | 10 | Executive cream | Monthly FP&A review (MTD/YTD/variance) |
| 53 | `53-budget-pitch.md` | 9 | Corporate hybrid | Budget request pitch to CFO |
| 54 | `54-annual-budget-deck.md` | 12 | Executive cream | Annual budget presentation to board |
| 55 | `55-cfo-briefing.md` | 8 | Executive cream | CFO briefing to board |
| 56 | `56-finance-kickoff.md` | 10 | Warm corporate | Finance team annual kickoff |
| 57 | `57-audit-committee.md` | 11 | Cream + dark navy | Audit committee update (SEC proxy grade) |
| 58 | `58-investor-earnings-deck.md` | 12 | Dark premium | Full quarterly investor deck |
| 59 | `59-ma-financing.md` | 10 | Corporate cream/gold | M&A financing options pitch |
| 60 | `60-treasury-review.md` | 9 | Dark developer | Treasury operations review |

## ROI & Business Case (10)
| # | File | Slides | Palette | Use when |
|---|------|:---:|---------|----------|
| 61 | `61-business-case-deck.md` | 12 | Executive cream | Full business case presentation |
| 62 | `62-tco-deck.md` | 9 | Corporate hybrid | TCO comparison deck |
| 63 | `63-npv-irr-deck.md` | 8 | Executive cream | NPV/IRR analysis deck |
| 64 | `64-payback-deck.md` | 7 | Clean light | Payback-focused pitch |
| 65 | `65-value-realization-deck.md` | 10 | Corporate blue | Post-implementation value deck |
| 66 | `66-savings-deck.md` | 9 | Corporate gold | Cost savings initiative pitch |
| 67 | `67-investment-committee.md` | 12 | Dark premium | IC-style investment memo deck |
| 68 | `68-vendor-roi-deck.md` | 9 | Corporate hybrid | Vendor selection ROI deck |
| 69 | `69-migration-roi.md` | 10 | Dark dev | Legacy-to-new migration ROI |
| 70 | `70-automation-roi.md` | 10 | Dark dev | Process automation ROI pitch |

## Sales (10)
| # | File | Slides | Palette | Use when |
|---|------|:---:|---------|----------|
| 71 | `71-account-review-deck.md` | 10 | Corporate | Internal strategic account review |
| 72 | `72-discovery-deck.md` | 8 | Clean light | Early-stage discovery meeting |
| 73 | `73-proposal-deck.md` | 11 | Executive cream | Full proposal presentation |
| 74 | `74-renewal-deck.md` | 9 | Clean light | Renewal presentation to customer |
| 75 | `75-pricing-negotiation.md` | 8 | Corporate | Internal pricing / deal-desk review |
| 76 | `76-competitive-displacement.md` | 10 | Dark premium | Competitor displacement pitch |
| 77 | `77-win-wire.md` | 7 | Warm light | Internal win announcement |
| 78 | `78-pipeline-review.md` | 9 | Dark dev | Sales pipeline review |
| 79 | `79-kickoff-deck.md` | 10 | Clean light | Customer kickoff deck (post-sale) |
| 80 | `80-qbr-customer-deck.md` | 11 | Executive cream | Customer-facing QBR |

## Creative & Minimal (10)
| # | File | Slides | Palette | Use when |
|---|------|:---:|---------|----------|
| 41 | `41-minimalist-dark.md` | 10 | Pure black/white | Radical minimalism, one idea per slide |
| 42 | `42-minimalist-light.md` | 10 | Pure white, red accent | Swiss-style grid minimalism |
| 43 | `43-typographic.md` | 10 | Cream + serif hero | Typography-led presentation |
| 44 | `44-data-story.md` | 11 | Clean light + signal color | Data storytelling (Knaflic method) |
| 45 | `45-visual-narrative.md` | 12 | Dark premium + SVGs | Visual-first storytelling |
| 46 | `46-keynote-inspired.md` | 10 | Pure black, white Helvetica | Apple keynote style (Jobs era) |
| 47 | `47-google-slides.md` | 10 | White + color strips | Modern Google Slides aesthetic |
| 48 | `48-duarte-style.md` | 12 | Cream + oscillation | Nancy Duarte Resonate method |
| 49 | `49-takahashi-method.md` | 20 | White + massive black type | Rapid-fire single-word slides |
| 50 | `50-pecha-kucha.md` | 20 | Dark + SVG per slide | 20×20 format (20 slides × 20 sec) |

---

## Sizing bands recap (non-negotiable per `SKILL.md`)
- **Summary:** ≤3 slides
- **Standard:** 7–10 slides
- **Detailed:** 10–12 slides
- **Workshop:** 15–20 slides (special — used by 31, 33, 34, 49, 50)

If the content overflows, CUT — do not expand the deck.

## How the skill uses this catalog

When the `deck-generation` skill runs, it should:
1. Ask the user what kind of deck (summary / standard / detailed / workshop) and the purpose
2. Match against this catalog — prefer the closest template
3. Copy the template file, replace placeholder content with the user's
4. Keep Marp frontmatter, slide separators, and presenter notes intact
5. Render hint: `marp --pptx {file}.md`
6. Report which template was used
