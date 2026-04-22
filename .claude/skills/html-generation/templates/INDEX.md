# HTML Template Catalog

80 production-quality, self-contained HTML templates. Each opens offline in any browser and uses only inline CSS (Google Fonts permitted).

## Executive Advisor OS palette lock

**For any Executive Advisor OS output (briefings, board reports, research dashboards, one-pagers) use only the Executive cream palette templates.** The other palettes are shipped as reference-only starting points for users who explicitly want a non-exec look — do NOT use them for executive research outputs. See `.claude/rules/brand/visual-identity.md`.

## Usage

1. Pick the Executive cream template that matches your use case from the catalog below
2. Copy the file (`cp templates/{N}-{name}.html output/your-file.html`)
3. Replace `{{VERSION}}`, `{{DATE}}`, and any other `{{...}}` placeholders
4. Swap the fictional placeholder content ("Northwind Capital", "Meridian Health", "Helix") for your real content
5. Verify it still opens cleanly offline

## Palettes used

- **Executive cream** *(EA default — use this)* — `#f7f4ef` bg, `#0e1b2e` navy, `#b8965a` gold. Boardroom / formal docs.
- **Dark developer** *(reference-only — do NOT use for EA outputs)* — `#0a0e14` bg, `#3b9eff` blue, `#2dd4a0` mint.
- **Light clean** *(reference-only — do NOT use for EA outputs)* — `#ffffff` bg, navy headings, blue accents.
- **Retro warm** *(reference-only — do NOT use for EA outputs)* — cream bg with mint/amber/blue accents.

---

## Executive & Board (10)
| # | File | Palette | Use when |
|---|------|---------|----------|
| 01 | `01-exec-brief-cream.html` | Executive cream | One-page executive briefing for the board or C-suite |
| 02 | `02-exec-brief-dark.html` | Dark developer | Same briefing, technical/internal audience |
| 03 | `03-ceo-memo.html` | Executive cream | CEO-to-company or CEO-to-board memo |
| 04 | `04-strategic-plan.html` | Executive cream | Multi-section strategic plan with pillars + KPIs |
| 05 | `05-quarterly-review.html` | Executive cream | QBR doc with KPI scoreboard + wins/losses |
| 06 | `06-investor-update.html` | Dark developer | Monthly investor update with metrics + asks |
| 07 | `07-annual-report.html` | Executive cream | Long-form annual report with TOC + chapters |
| 08 | `08-shareholder-letter.html` | Executive cream | Buffett-style long-form shareholder letter |
| 09 | `09-board-deck.html` | Executive cream | Scroll-snap HTML slide deck |
| 10 | `10-classified-briefing.html` | Mono/cream | Defense-style classified briefing aesthetic |

## Dashboards & Analytics (10)
| # | File | Palette | Use when |
|---|------|---------|----------|
| 11 | `11-kpi-dashboard.html` | Executive cream | KPI grid with sparklines and trend indicators |
| 12 | `12-project-tracker.html` | Executive cream | Project/module tracker (SponAItech tracker style) |
| 13 | `13-status-page.html` | Dark developer | Service status page with uptime bars |
| 14 | `14-financial-dashboard.html` | Executive cream | Revenue/costs/margin dashboard with donut chart |
| 15 | `15-sales-pipeline.html` | Executive cream | Kanban-style sales pipeline with deal cards |
| 16 | `16-trading-dashboard.html` | Dark developer | Market/trading dashboard with equity curve SVG |
| 17 | `17-system-health.html` | Dark developer | Observability dashboard (latency/errors/throughput) |
| 18 | `18-incident-timeline.html` | Dark developer | Post-incident timeline with event tags |
| 19 | `19-ab-comparison.html` | Executive cream | A/B test side-by-side with verdict |
| 20 | `20-cohort-analysis.html` | Dark developer | Cohort retention heatmap (conic-gradient cells) |

## Reports & Documents (10)
| # | File | Palette | Use when |
|---|------|---------|----------|
| 21 | `21-research-report.html` | Executive cream | Academic / analyst research report |
| 22 | `22-whitepaper.html` | Executive cream | Technical whitepaper with cover + TOC |
| 23 | `23-case-study.html` | Executive cream | Business case study (challenge/solution/results) |
| 24 | `24-market-analysis.html` | Executive cream | Market/industry analysis with forecast SVG |
| 25 | `25-due-diligence.html` | Executive cream | M&A / PE due diligence report with verdict banner |
| 26 | `26-audit-report.html` | Executive cream | Financial/compliance audit with opinion banner |
| 27 | `27-compliance-brief.html` | Executive cream | HIPAA/SOX/GDPR compliance brief + gap analysis |
| 28 | `28-risk-assessment.html` | Executive cream | 5x5 likelihood×impact heatmap + register |
| 29 | `29-post-mortem.html` | Dark developer | Incident post-mortem with timeline + actions |
| 30 | `30-technical-spec.html` | Dark developer | Technical design spec with architecture SVG |

## Docs & Product Communications (10)
| # | File | Palette | Use when |
|---|------|---------|----------|
| 31 | `31-api-docs.html` | Dark developer | API reference (Stripe-inspired) with method badges |
| 32 | `32-getting-started.html` | Light clean | Product onboarding guide with step cards |
| 33 | `33-architecture-doc.html` | Dark developer | System architecture page with SVG diagram |
| 34 | `34-runbook.html` | Dark developer | Operations runbook with diagnosis steps |
| 35 | `35-kb-article.html` | Light clean | Knowledge base article (Zendesk-style) |
| 36 | `36-release-notes.html` | Light clean | Product release notes (Linear changelog style) |
| 37 | `37-landing-hero.html` | Light marketing | Product landing page hero + features |
| 38 | `38-one-pager-sales.html` | Light marketing | Sales one-pager with KPIs + comparison |
| 39 | `39-product-brief.html` | Executive cream | Internal product brief / PRD |
| 40 | `40-pitch-onepager.html` | Light marketing | Startup pitch one-pager with traction metrics |

## Finance (10)
| # | File | Palette | Use when |
|---|------|---------|----------|
| 51 | `51-pnl-statement.html` | Executive cream | Profit & Loss statement with multi-period columns + YoY % |
| 52 | `52-balance-sheet.html` | Executive cream | Balance sheet (Assets = Liab + Equity reconciled) |
| 53 | `53-cash-flow.html` | Executive cream | Cash flow statement with sparkline reconciliation |
| 54 | `54-budget-variance.html` | Executive cream | Budget vs Actual variance with color-coded commentary |
| 55 | `55-expense-report.html` | Executive cream | Employee expense report (itemized + approvals) |
| 56 | `56-forecast-model.html` | Dark developer | 12-month rolling forecast with assumptions + scenarios |
| 57 | `57-scenario-analysis.html` | Dark developer | Base/Upside/Downside scenario comparison + sensitivity heatmap |
| 58 | `58-earnings-summary.html` | Executive cream | Quarterly earnings one-pager with guidance |
| 59 | `59-treasury-dashboard.html` | Dark developer | Treasury ops dashboard (cash/FX/debt/liquidity) |
| 60 | `60-vendor-spend.html` | Executive cream | Vendor spend analysis with category donut + concentration risk |

## ROI & Business Case (10)
| # | File | Palette | Use when |
|---|------|---------|----------|
| 61 | `61-roi-calculator.html` | Executive cream | ROI calculator with verdict banner (ROI 143% reconciled) |
| 62 | `62-payback-analysis.html` | Executive cream | Cumulative cash flow with SVG break-even marker |
| 63 | `63-npv-irr-summary.html` | Executive cream | DCF + NPV/IRR with sensitivity table |
| 64 | `64-tco-comparison.html` | Executive cream | 3-option TCO comparison with winner callout |
| 65 | `65-cost-benefit.html` | Executive cream | Cost-benefit analysis with BCR + qualitative factors |
| 66 | `66-value-realization.html` | Dark developer | Post-implementation value realization report |
| 67 | `67-business-case.html` | Executive cream | Full business case document (7 sections) |
| 68 | `68-savings-tracker.html` | Dark developer | Savings initiatives tracker with SVG bar chart |
| 69 | `69-investment-memo.html` | Executive cream | IC-style investment memo (Sequoia/KKR format) |
| 70 | `70-benefit-realization.html` | Executive cream | Benefit realization plan with dependency matrix |

## Sales (10)
| # | File | Palette | Use when |
|---|------|---------|----------|
| 71 | `71-account-plan.html` | Executive cream | Strategic account plan with whitespace + revenue plan |
| 72 | `72-territory-plan.html` | Light clean | Sales territory plan with tiering + coverage |
| 73 | `73-win-loss-analysis.html` | Dark developer | Win-loss analysis with interview quotes + patterns |
| 74 | `74-customer-qbr.html` | Executive cream | Customer-facing Quarterly Business Review |
| 75 | `75-renewal-summary.html` | Light clean | Renewal risk assessment with probability ring |
| 76 | `76-expansion-proposal.html` | Executive cream | Upsell/expansion proposal with ROI + signatures |
| 77 | `77-pipeline-health.html` | Dark developer | Pipeline health dashboard with funnel + deal heat map |
| 78 | `78-deal-desk-memo.html` | Executive cream | Deal desk approval memo with deviation cards |
| 79 | `79-customer-success-plan.html` | Executive cream | Post-signature customer success plan (30/60/90) |
| 80 | `80-sales-playbook.html` | Light clean | Sales playbook / battlecard (ICP + discovery + objections) |

## Marketing & Admin (10)
| # | File | Palette | Use when |
|---|------|---------|----------|
| 41 | `41-email-newsletter.html` | Light (table-based) | Transactional/marketing email (Gmail/Outlook-safe) |
| 42 | `42-testimonial-wall.html` | Light clean | Client testimonial wall (masonry quote cards) |
| 43 | `43-pricing-page.html` | Light clean | SaaS pricing with 3-4 tiers |
| 44 | `44-event-invite.html` | Light clean | Event/webinar invitation with agenda + speakers |
| 45 | `45-style-guide.html` | SponAItech full | Brand style guide (color, type, do/don't) |
| 46 | `46-glossary.html` | Light clean | A-Z terminology glossary with anchor nav |
| 47 | `47-invoice.html` | Executive cream | Professional invoice (A4 print-ready) |
| 48 | `48-proposal.html` | Executive cream | Consulting proposal with SVG Gantt + signatures |
| 49 | `49-meeting-agenda.html` | Executive cream | Meeting agenda with time-stamped items + actions |
| 50 | `50-retrospective.html` | Retro warm | Sprint retro (went-well / didn't-go / actions) |

---

## How the skill uses this catalog

When the `html-generation` skill runs, it should:
1. Ask the user what they're producing (or infer from context)
2. Match against this catalog — prefer the closest template over generating from scratch
3. Copy the template file, replace placeholders, adapt content
4. Verify output is still self-contained (no new external references)
5. Report which template was used as the base
