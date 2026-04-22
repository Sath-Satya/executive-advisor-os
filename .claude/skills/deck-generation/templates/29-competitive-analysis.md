<!-- TEMPLATE: competitive-analysis
     CATEGORY: Business / Strategy
     USE WHEN: presenting competitive landscape research to product, strategy, or leadership teams
     SLIDE COUNT: 10
     PALETTE: Corporate hybrid (cream bg, navy headings, gold accent)
     RENDER: marp --pptx 29-competitive-analysis.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'DM Sans', 'Segoe UI', system-ui, sans-serif;
    background: #f7f4ef;
    color: #2c3340;
    padding: 48px 60px;
  }
  h1 {
    font-family: 'Segoe UI', system-ui, sans-serif;
    color: #0e1b2e;
    letter-spacing: -0.3px;
    font-size: 1.75em;
    border-bottom: 2px solid #d8d2c6;
    padding-bottom: 12px;
    margin-bottom: 22px;
    font-weight: 700;
  }
  h2 { color: #b8965a; font-size: 1.2em; margin-top: 0; font-weight: 600; }
  h3 { color: #8899ac; font-size: 0.9em; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; }
  p, li { color: #2c3340; line-height: 1.65; }
  strong { color: #0e1b2e; font-weight: 700; }
  em { color: #b8965a; font-style: normal; font-weight: 600; }
  code {
    font-family: 'DM Mono', 'Cascadia Code', monospace;
    background: #e8e2d8;
    padding: 2px 6px;
    border-radius: 3px;
    color: #4a5568;
    font-size: 0.9em;
  }
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
  th { background: #0e1b2e; color: #f7f4ef; padding: 10px 14px; text-align: left; border-bottom: none; font-weight: 600; font-size: 0.85em; }
  td { padding: 9px 14px; border-bottom: 1px solid #d8d2c6; color: #2c3340; }
  tr:nth-child(even) td { background: #f0ece4; }
  blockquote { border-left: 3px solid #b8965a; padding: 10px 16px; background: #eae6de; margin: 16px 0; border-radius: 0 4px 4px 0; }
  blockquote p { color: #0e1b2e; margin: 0; font-weight: 600; }
  .win { color: #2a7d4f; font-weight: 700; }
  .risk { color: #b91c1c; font-weight: 700; }
  .neutral { color: #92400e; }
  section.title { justify-content: center; background: #0e1b2e; }
  section.title h1 { color: #f7f4ef; border-bottom-color: #1a2e48; font-size: 2.2em; }
  section.title h2 { color: #b8965a; font-weight: 400; font-size: 1.1em; }
  section.title p { color: #8899ac; font-size: 0.9em; }
---
<!-- _class: title -->

# Claims Processing Platform
## Competitive Analysis — [Market Segment]

**Analyst:** [Name] &nbsp;|&nbsp; **Date:** [YYYY-MM-DD]
**Audience:** Product Leadership, Strategy Team

<!-- SPEAKER NOTES — Slide 1: Title
A competitive analysis presentation should lead with its intended use: are you making a build-vs-buy decision, evaluating a market entry, or preparing for a sales conversation? State the use case in the first 30 seconds. The audience should know whether this is a strategic brief (leading to a decision) or an informational update (building shared understanding). For leadership audiences, signal that you have been thorough: "We evaluated [N] vendors, ran [N] demos, and interviewed [N] customers." Evidence of rigor builds credibility before the first data slide.
-->

---

# 1 — Market Context

## Why This Analysis Exists

**The question we are answering:** Should we build a claims processing platform or acquire/partner with an existing vendor?

**Market size:**
- US healthcare claims processing market: **$14.8 B** (2024)
- Growing at **8.2% CAGR** — driven by payer digitization and value-based care contracts
- Consolidation underway: 3 major acquisitions in the past 18 months

**Our position today:**
- Self-built adjudication engine (Helix) — 1.2 M claims/day, single payer segment
- Entering multi-payer market requires capabilities beyond current Helix scope
- Decision timeline: board presentation in [Month]

<!-- SPEAKER NOTES — Slide 2: Market Context
Ground the analysis in the business question it is answering. "Should we build or buy?" is more tractable than "who are our competitors?" The market size and CAGR numbers should come from a credible source — cite the research firm (e.g., KLAS Research, IDC Health Insights, or Grand View Research) in your notes. The consolidation trend is important context: if the market is consolidating, waiting to make a build/buy decision means the acquire options are shrinking. The "decision timeline" note anchors urgency — a board presentation in [Month] means this analysis must be complete and defensible by [Month - 2 weeks].
-->

---

# 2 — Competitor A — [Vendor Name]

## Profile and Capabilities

**Overview:** [One-sentence description of who they are and what they do]

**Market position:** [Market segment focus, customer size, geography]

| Capability | Rating | Notes |
|---|---|---|
| Claim ingestion (EDI, REST, SOAP) | ★★★★★ | Native support for all major formats; 40+ clearing house integrations |
| Adjudication rules engine | ★★★★☆ | Strong for standard rules; custom rules require professional services |
| Real-time adjudication (< 1 s) | ★★★☆☆ | Achievable at < 500k claims/day; degrades above that |
| HIPAA compliance and audit | ★★★★★ | SOC 2 Type II, HIPAA BAA, hitrust certified |
| Multi-payer support | ★★★★☆ | 85 payers supported; smaller regional payers require custom work |

**Pricing model:** Per-claim (est. $0.08–$0.15/claim based on public contract filings)

<!-- SPEAKER NOTES — Slide 3: Competitor A
One slide per major competitor keeps the pacing manageable. The rating system (stars) should be defined in an appendix slide — what does "3 stars" mean for adjudication speed? Define it as: 5 = industry-leading, 4 = above average, 3 = meets requirement, 2 = gaps exist, 1 = significant deficiency. The per-claim pricing estimate should be sourced from contract filings, analyst reports, or customer interviews — not guessed. If you have a demo recording or trial environment data, reference it. The "professional services for custom rules" weakness is important: it means your roadmap is dependent on their PS team, which is a risk for a fast-moving product organization.
-->

---

# 3 — Competitor B — [Vendor Name]

## Profile and Capabilities

**Overview:** [One-sentence description]

**Market position:** [Market segment focus, customer size, geography]

| Capability | Rating | Notes |
|---|---|---|
| Claim ingestion (EDI, REST, SOAP) | ★★★☆☆ | Strong EDI; REST API is 2019-era, limited webhooks |
| Adjudication rules engine | ★★★★★ | Best-in-class rules engine; AI-assisted rule recommendations |
| Real-time adjudication (< 1 s) | ★★★★★ | P99 < 200 ms at 2 M claims/day in published benchmarks |
| HIPAA compliance and audit | ★★★★☆ | HIPAA BAA; hitrust in progress (2025 target) |
| Multi-payer support | ★★★☆☆ | 40 payers; heavy Blue Cross / United concentration |

**Pricing model:** Annual license + usage tier (est. $480K/yr base + $0.04/claim above 1 M/mo)

<!-- SPEAKER NOTES — Slide 4: Competitor B
Be objective in the ratings — if a competitor has a genuinely better capability than your current system, say so. Understating competitor strengths leads to poor strategic decisions. The AI-assisted rule recommendations capability is worth discussing: if Competitor B can surface optimization opportunities in the rules engine automatically, that is a real differentiation against a manual rules management approach. The hitrust "in progress" status is a risk for customers with strict compliance requirements — flag it. The concentrated payer support (Blue Cross / United) is a geographic and payer mix risk: customers with heavy regional payer exposure would be underserved.
-->

---

# 4 — Competitor C — [Vendor Name]

## Profile and Capabilities

**Overview:** [One-sentence description]

**Market position:** [Market segment focus, customer size, geography]

| Capability | Rating | Notes |
|---|---|---|
| Claim ingestion (EDI, REST, SOAP) | ★★★★☆ | Strong; missing direct clearing house integrations (customer-managed) |
| Adjudication rules engine | ★★★☆☆ | Rules defined in proprietary DSL; limited portability |
| Real-time adjudication (< 1 s) | ★★★☆☆ | P99 ~1.2 s at rated load; marginal for SLA requirements |
| HIPAA compliance and audit | ★★★★★ | Longest track record; used by 3 of 5 largest US payers |
| Multi-payer support | ★★★★★ | 200+ payers; strongest regional payer coverage |

**Pricing model:** Subscription + implementation fee (est. $200K implementation + $18K/mo)

<!-- SPEAKER NOTES — Slide 5: Competitor C
The proprietary DSL for rules is a significant lock-in risk — flag it prominently. If a customer invests 12 months building rules in Competitor C's DSL, migration to another platform requires rewriting all rules. This is both a competitive moat for Competitor C and a risk for any customer evaluating them. The strong multi-payer coverage (200+ payers) is Competitor C's clearest differentiator against Competitors A and B. If your target market includes heavy regional payer exposure, Competitor C is the strongest incumbent. The high implementation fee ($200K) is a barrier that may work in your favor if your alternative is faster to implement — quantify your implementation time and compare.
-->

---

# 5 — Comparison Matrix

## Head-to-Head Summary

| Capability | Our Platform (Helix) | Vendor A | Vendor B | Vendor C |
|---|---|---|---|---|
| EDI + REST ingestion | ★★★★☆ | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Adjudication rules engine | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| Real-time (< 800 ms P99) | ★★★★☆ | ★★★☆☆ | ★★★★★ | ★★★☆☆ |
| HIPAA / hitrust certified | ★★★☆☆ | ★★★★★ | ★★★★☆ | ★★★★★ |
| Multi-payer support | ★☆☆☆☆ | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| API extensibility | ★★★★★ | ★★★☆☆ | ★★★★☆ | ★★☆☆☆ |
| Total cost (est. 3 yr) | $1.8 M | $3.2 M | $2.6 M | $3.8 M |

**Legend:** ★★★★★ = industry-leading · ★★★☆☆ = meets requirement · ★☆☆☆☆ = significant gap

<!-- SPEAKER NOTES — Slide 6: Comparison Matrix
The comparison matrix is the most referenced slide in a competitive analysis — leadership will photograph this slide. Make sure the ratings are defensible and consistent with the per-vendor slides. The "Our Platform (Helix)" column is critical: be honest about gaps. The multi-payer support gap (★☆☆☆☆) is a significant weakness that the entire analysis is built around. The API extensibility advantage (★★★★★) is your clearest current differentiation — it should feature prominently in the recommendation. The 3-year TCO row should be calculated with a consistent model: include implementation, licensing, and estimated operational overhead. Have the detailed cost model in an appendix. The legend at the bottom defines the scale — read it aloud when presenting.
-->

---

# 6 — Positioning Map

## Where Each Player Sits

```
                    RULES DEPTH
         Low ←─────────────────────→ High
    H │                         [Vendor B]
    i │
    g │  [Our Platform]
    h │        [Vendor A]
      │
M   M │
u   e │
l   d │               [Vendor C]
t   ─ │
i   L │
-   o │
P   w │
a      ─────────────────────────────────
y     Single Payer         Multi-Payer
e                    PAYER BREADTH
r
```

**Strategic implication:** Our platform wins on extensibility and performance. Gap is payer breadth + rules depth. Vendor B is the most direct competitive threat in real-time workloads.

<!-- SPEAKER NOTES — Slide 7: Positioning Map
The positioning map makes the competitive landscape spatial and memorable. The two axes (rules depth and payer breadth) are the two most critical dimensions identified in the requirements analysis — the axes should match the buyer's evaluation criteria, not generic dimensions. Walk through where each player sits: Our Platform is strong on performance but limited on payer breadth (single payer today). Vendor B is strong on rules and performance — it is the most direct competitive threat for real-time workloads. Vendor C owns multi-payer but is slow. Vendor A is the generalist. The strategic implication at the bottom should flow naturally from the positioning: you are looking at different build paths (payer breadth build vs. rules engine acquisition vs. Vendor B partnership).
-->

---

# 7 — Gaps and Opportunities

## What the Competitive Landscape Reveals

**Market gaps (no incumbent owns these):**
- Real-time adjudication + multi-payer support — no vendor does both at scale
- API-first architecture with extensible rules — incumbents are proprietary DSL or professional services
- Mid-market pricing — Vendor A/C pricing excludes orgs below 500k claims/month

**Our addressable gaps (build or buy):**
- Multi-payer coverage: 14-month build estimate vs. Vendor C acquisition or partnership
- Rules engine depth: 8-month build estimate vs. Vendor B partnership (API access to their engine)
- HIPAA hitrust certification: 9-month process (currently in progress — not a build)

**Where incumbents are weakest:**
- API extensibility — all three vendors require professional services for custom integrations
- Developer experience — no competitor offers SDK or webhook-first integration patterns

<!-- SPEAKER NOTES — Slide 8: Gaps and Opportunities
The gaps analysis is where the competitive analysis generates actionable insight. Walk through the three sections in order: what nobody owns (market opportunity), what we are missing (honest self-assessment), and where incumbents are weakest (our attack surface). The "API-first with extensible rules" gap is your most compelling market opportunity: no incumbent does this well, and it aligns directly with your existing strength (★★★★★ on API extensibility). The build vs. buy estimates should be validated with the engineering team before presenting — "14-month build estimate" for multi-payer coverage is a significant commitment. Have the breakdown ready: what does 14 months include? (Payer integrations: 3 months × N payers, plus governance and testing.)
-->

---

# 8 — Strategic Options

## Three Paths Forward

**Option A — Build (18-month plan):**
Accelerate Helix into a multi-payer, full-featured platform. Build rules engine depth and payer integrations internally. Estimated investment: $4.2 M over 18 months.

**Option B — Acquire / Partner (6–12 months):**
Acquire a payer integration specialist or sign a revenue-share partnership with Vendor C for payer coverage, while retaining Helix for the rules engine. Estimated integration cost: $800K.

**Option C — OEM / White-label (3–6 months):**
White-label Vendor B as the rules engine under the Helix brand. Invest in API extensibility and developer experience as differentiation. Estimated cost: $480K/yr + margin compression.

**Recommended direction:** [Option X] — rationale follows in Recommendation slide.

<!-- SPEAKER NOTES — Slide 9: Strategic Options
Presenting three options with estimated costs gives leadership a real choice, not a rubber-stamp. Each option should be evaluated on: time-to-market, cost, strategic control, and risk. Option A (build) maximizes strategic control but is the slowest and most expensive. Option B (partner) is the middle path — faster than building, but introduces a dependency on Vendor C's roadmap and pricing. Option C (OEM) is fastest but introduces margin compression and limits product differentiation. The recommendation should be in the next slide — keep the options slide neutral so leadership can debate on equal footing. If you have a recommended option, state it clearly in the next slide with full rationale, not as a fait accompli in this slide.
-->

---

# 9 — Recommendation

## What We Should Do and Why

**Recommendation: Option B — Partner with Vendor C for payer coverage**

**Rationale:**
- Multi-payer coverage is the largest gap and the slowest to build organically (14 months)
- Vendor C has the strongest payer network (200+ payers) with no competitive threat on our core differentiators (API extensibility, real-time performance)
- Partnership preserves Helix as the rules engine and adjudication brain — strategic IP stays internal
- Estimated 6-month time to market advantage over Option A

**Conditions for this recommendation:**
- Vendor C partnership terms allow API-first integration (not black-box)
- Revenue share does not exceed 18% — model breaks above this threshold
- Exit clause at 24 months if Vendor C is acquired by a direct competitor

> This is a speed-to-market decision, not a permanent architecture decision.

<!-- SPEAKER NOTES — Slide 10: Recommendation (final)
A competitive analysis recommendation should be specific, owned, and conditioned. The three conditions are non-negotiable — if any are violated in negotiation, the recommendation changes (likely to Option A or a different partner). The "speed-to-market decision, not a permanent architecture decision" framing is important: it signals that the recommendation is bounded by current constraints, not a 10-year commitment. This gives leadership confidence that you have thought about reversibility. After this meeting, the next step is a negotiation brief with Vendor C — confirm who owns that and by when. Have a fallback position ready if Vendor C declines: that is when Option A or a different partner becomes the recommendation.
-->

---

# 10 — Next Steps

## Recommended Actions

| Action | Owner | Due | Dependencies |
|---|---|---|---|
| ▲ Approve strategic direction (Option B) | Leadership | Today | This presentation |
| → Begin Vendor C partnership negotiation | Business Development | [Date + 1 week] | Leadership approval |
| → Commission hitrust audit (independent track) | Compliance | [Date + 2 weeks] | None |
| → Scope Option A build estimate (fallback plan) | Engineering | [Date + 3 weeks] | Vendor C NDA signed |
| ○ Board presentation with recommended option | CEO / Strategy | [Board Date] | All above |

**If Option B is approved:** Partnership LOI target signed by [Date].
**If Option B is rejected:** Reconvene with full Option A build plan within 4 weeks.

<!-- SPEAKER NOTES — Slide 11 (final): Next Steps
Close with a crisp action table — every row has an owner, a due date, and a dependency. The Leadership row is the first action because it unblocks everything else. Note that the hitrust audit is on an independent track — it takes 9 months regardless of which strategic option is chosen, so it should start immediately. The "fallback plan" engineering scope (Option A) is listed as contingent on Vendor C NDA — this is intentional: you cannot scope the build plan accurately until you know what the partnership would cover. After the meeting, distribute the action table via email within 24 hours with confirmed owners. Schedule the Board presentation slot before leaving the room.
-->
