<!-- TEMPLATE: market-overview
     CATEGORY: Business / Strategy
     USE WHEN: briefing leadership or investors on a market landscape before entering it
     SLIDE COUNT: 9
     PALETTE: Corporate hybrid (cream bg, navy headings, gold accent)
     RENDER: marp --pptx 30-market-overview.md -->
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
  section.title { justify-content: center; background: #0e1b2e; }
  section.title h1 { color: #f7f4ef; border-bottom-color: #1a2e48; font-size: 2.2em; }
  section.title h2 { color: #b8965a; font-weight: 400; font-size: 1.1em; }
  section.title p { color: #8899ac; font-size: 0.9em; }
---
<!-- _class: title -->

# Healthcare Claims Processing
## Market Overview — US Payer Technology Segment

**Analyst:** [Name] &nbsp;|&nbsp; **Date:** [YYYY-MM-DD]
**Sources:** KLAS Research, IDC Health Insights, CMS open data

<!-- SPEAKER NOTES — Slide 1: Title
A market overview is a foundational brief — it provides shared context before a strategy, investment, or partnership discussion. State your sources on the title slide: a market overview without attributed data sources is an opinion, not an analysis. The three sources listed (KLAS Research, IDC Health Insights, CMS open data) give this the credibility of independent research. If any data comes from customer interviews or primary research, note the sample size. For investor or board audiences, the methodology note is especially important.
-->

---

# 1 — Market Size

## How Big Is This Market

**US Healthcare Claims Processing Market:**

| Metric | 2024 | 2027 (Forecast) | CAGR |
|---|---|---|---|
| Total market size | $14.8 B | $18.7 B | 8.2% |
| Software and platforms | $6.1 B | $8.4 B | 11.2% |
| Services and BPO | $8.7 B | $10.3 B | 5.8% |

**Volume context:**
- **3.8 B** medical claims submitted annually in the US (CMS, 2023)
- **90%** submitted electronically (EDI); 10% paper (declining 3% YoY)
- **4.2%** claim denial rate — $267 B in denied claims annually (CAQH, 2023)

> The software segment is growing 2× faster than the services segment — digitization is displacing BPO.

<!-- SPEAKER NOTES — Slide 2: Market Size
Market size slides need precise sourcing. The CAGR numbers come from IDC Health Insights — cite the specific report and year. The CMS volume data is public — reference the specific CMS data release. The "4.2% claim denial rate" with a dollar figure ($267 B) is a particularly compelling statistic because it frames the problem size in business terms: denials represent revenue at risk for providers, creating strong buyer motivation for better adjudication platforms. The pull-quote is the strategic implication: software is outgrowing services, which means the addressable market for platform companies is expanding faster than the overall market. This is a favorable trend for a technology-first entrant.
-->

---

# 2 — Market Segments

## Who Buys and Why

| Segment | Size | Key Buyers | Primary Need |
|---|---|---|---|
| Commercial payers (large) | $4.1 B | BCBS plans, Aetna, Cigna | Scale, compliance, cost per claim |
| Commercial payers (mid-market) | $2.8 B | Regional plans (50–500k members) | Modern API, speed to market |
| Medicaid MCOs | $1.9 B | State-contracted plans | CMS compliance, audit trail |
| Medicare Advantage plans | $1.6 B | MA-only and hybrid plans | Risk adjustment integration |
| Hospital / provider (self-processing) | $0.5 B | IDNs, large health systems | Revenue cycle integration |

**Our addressable segment:** Commercial payers (mid-market) + Medicaid MCOs = **$4.7 B TAM**
**Our serviceable addressable market (SAM):** Mid-market plans with > 200k claims/month = **$1.2 B**

<!-- SPEAKER NOTES — Slide 3: Market Segments
Segmentation is the most important slide for investment or strategy discussions — it translates a large market number into a specific, credible addressable market. The TAM/SAM calculation should be documented in detail: how did you arrive at $4.7 B TAM? (Sum of mid-market commercial + Medicaid MCO segments.) How did you arrive at $1.2 B SAM? (200k claims/month threshold filters to plans large enough to justify a platform investment but small enough that they are not locked into a Tier-1 vendor.) Be prepared to defend both numbers. The "Our serviceable addressable market" note should be consistent with the sales qualification criteria the sales team uses — align with them before presenting.
-->

---

# 3 — Market Trends

## What Is Changing and Why It Matters

**Trend 1 — Value-Based Care Contracting**
Payers moving from fee-for-service to value-based models require claims systems that attribute costs to episodes of care, not individual claims. Drives demand for analytics-integrated claims platforms.

**Trend 2 — Real-Time Claims Adjudication**
CMS Transparency Rule (effective 2026) requires payers to provide real-time eligibility and cost estimates. Forces upgrade of legacy batch-processing systems that cannot meet < 1 second SLA.

**Trend 3 — AI-Assisted Denial Management**
AI models predicting denial risk before submission are reducing denial rates by 15–23% in early adopter deployments (Optum, 2023). Becoming a differentiator, not a feature.

> The CMS Transparency Rule is a forcing function — it creates a mandatory upgrade cycle regardless of buyer preference.

<!-- SPEAKER NOTES — Slide 4: Market Trends
Three trends is the right number for a market overview — more than three and the audience loses the thread. Each trend should be connected to a buyer behavior change: Trend 1 changes what features buyers evaluate, Trend 2 creates a mandatory upgrade cycle, Trend 3 changes the evaluation criteria (AI capability now on the shortlist). The CMS Transparency Rule (Trend 2) is the most important for near-term market timing: it creates urgency that does not depend on a buyer's budget cycle. Reference the specific CMS rule number in your speaker notes (CMS-9915-F, effective January 1, 2026). The AI denial management data should be attributed to the specific source (Optum internal study, published where?).
-->

---

# 4 — Key Players

## Who Dominates the Market Today

| Player | Segment Focus | Estimated Revenue | Key Strength |
|---|---|---|---|
| [Vendor A] | Large commercial, Medicare Advantage | $1.2 B | Scale, compliance pedigree |
| [Vendor B] | Mid-market commercial | $480 M | Real-time adjudication engine |
| [Vendor C] | Multi-payer, national | $890 M | Payer network breadth (200+) |
| [Vendor D] | Medicaid-focused | $340 M | State compliance expertise |
| [Vendor E] | Provider-side self-processing | $210 M | EHR integration |
| Emerging | API-first, developer-centric | < $100 M | Modern stack, speed |

**Market concentration:** Top 3 players hold ~55% of software segment revenue.
**Entry pattern:** Mid-market and Medicaid segments underserved by incumbents — primary entry vector.

<!-- SPEAKER NOTES — Slide 5: Key Players
The key players table should use estimated revenues from analyst reports, not from company-reported figures (private companies do not disclose). If estimates are not available, note "estimated" in the table header. The market concentration calculation (55% for top 3) signals that this is a competitive but not monopolized market — there is room for entrants. The entry pattern note at the bottom is the strategic conclusion from the player analysis: mid-market and Medicaid are underserved because large incumbents optimize for their largest accounts. This is a classic innovation theory wedge — start where the incumbents are weakest. Align this with the target segment from Slide 3.
-->

---

# 5 — Growth Drivers

## What Is Accelerating Market Expansion

**Driver 1 — Regulatory mandates (non-discretionary spend):**
CMS interoperability rules, No Surprises Act price transparency requirements, and Medicaid managed care reporting rules drive mandatory platform upgrades. Estimated $1.4 B in compliance-driven IT spend over 2024–2026.

**Driver 2 — Healthcare digitization backlog:**
40% of mid-market payers still running claims systems from the 2000s. Modernization budgets unlocked by COVID-era digital acceleration — now converting to platform purchases.

**Driver 3 — Provider revenue cycle pressure:**
Hospital margins under pressure from labor costs and payer contract renegotiations. Providers self-processing claims (IDNs) are upgrading to reduce the 4.2% denial rate drag.

<!-- SPEAKER NOTES — Slide 6: Growth Drivers
The three-driver structure mirrors the three-trend structure from Slide 4 — this is intentional. Trends describe market direction; drivers explain why those trends translate to revenue. The $1.4 B compliance-driven IT spend estimate should come from a healthcare IT analyst projection — cite it. The "40% of mid-market payers on 2000s systems" statistic is a commonly quoted industry figure — attribute it to HIMSS or KLAS. The provider revenue cycle driver is often overlooked in payer technology analyses but represents a meaningful adjacent market (the $0.5 B provider-side segment from Slide 3). Flag this as a long-term expansion opportunity, not a primary market for initial entry.
-->

---

# 6 — Barriers to Entry

## What Makes This Market Hard to Enter

| Barrier | Severity | Implication |
|---|---|---|
| HIPAA/hitrust compliance certification | High | 9–12 months; non-negotiable for enterprise sales |
| Payer integration complexity | High | 40+ clearing houses, 200+ payers, proprietary EDI variants |
| Incumbent switching costs | High | Average contract length 5–7 years; migration projects 12–18 months |
| Regulatory expertise | Medium | CMS rule interpretation requires dedicated compliance staff |
| Sales cycle length | Medium | 9–18 month enterprise sales cycle; high customer acquisition cost |
| Capital intensity | Medium | Cloud infrastructure + compliance + implementation staff before revenue |

**Implication:** These barriers protect incumbents but also mean a credible entrant takes 18–24 months to establish — budget accordingly.

<!-- SPEAKER NOTES — Slide 7: Barriers to Entry
Barriers to entry are often presented defensively — "these are the reasons we might fail." Reframe them: they are also the moat that protects a successful entrant once established. The high switching cost barrier (5–7 year contracts, 12–18 month migrations) means that once you win an account, you keep it for a long time. The hitrust certification is the most commonly underestimated barrier: it is a 9–12 month process that cannot be shortcut, and without it, enterprise sales cycles will not advance past procurement. Start this process before the first enterprise sales conversation. The sales cycle length (9–18 months) has direct cash flow implications — model this into the runway calculation.
-->

---

# 7 — 5-Year Market Forecast

## Where the Market Is Heading

```
Market Size ($B)
20 │                                              [18.7]
18 │                                    [17.2]
16 │                         [15.8]
14 │          [14.8]
12 │
10 │──────────────────────────────────────────────────
   2024       2025       2026       2027       2028
```

**Key inflection point — 2026:**
- CMS Transparency Rule effective Jan 1, 2026 → forced upgrade cycle begins
- AI denial management reaches mainstream adoption (est. 40% of mid-market plans)
- Next Medicaid managed care contract renewal cycle (every 5 years)

**Forecast confidence:** Medium — regulatory timing is certain; adoption rate is modeled.

<!-- SPEAKER NOTES — Slide 8: 5-Year Forecast
The forecast chart uses an ASCII line graph — for a more polished output, replace with a proper chart if your presentation tool supports it. The key inflection in 2026 is the most important element: it creates a time-bound entry window. If your platform is not ready by early 2026, you miss the first wave of forced upgrades. The "forecast confidence" note is important for credibility — distinguishing between what is certain (regulatory timing) and what is modeled (adoption rate) shows analytical rigor. Leadership will ask about the assumptions behind the adoption rate model — have the sensitivity analysis ready: "If adoption is 10% slower, the market reaches $18.7 B in 2029 instead of 2028."
-->

---

# 8 — Strategic Implications

## What This Means for Our Path

**For timing:**
- The 2026 CMS Transparency Rule creates a 24-month entry window (2024–2026)
- Entering after 2026 means competing for second-mover positions, not greenfield opportunities

**For product:**
- Real-time adjudication (< 800 ms) is becoming table stakes, not a differentiator
- AI denial management will be a buyer evaluation criterion by 2025 — needs roadmap priority
- Developer-friendly API is an under-served differentiator — incumbents are not investing here

**For go-to-market:**
- Mid-market commercial payers are the highest-opportunity entry segment (underserved, active buyers)
- hitrust certification is a sales prerequisite — start the process in [Month]
- Partner with a system integrator that has Medicaid state relationships for that segment

<!-- SPEAKER NOTES — Slide 9: Strategic Implications
The strategic implications slide converts market data into decisions. Each bullet should map directly to a slide earlier in the deck: timing comes from the 2026 inflection point (Slide 8), product priorities come from the trends and barriers analysis (Slides 4 and 7), go-to-market comes from the segments and players analysis (Slides 3 and 5). This slide is the "so what?" of the entire deck. If leadership only reads one slide, it should be this one. The hitrust certification note ("start the process in [Month]") should have a specific month — it is an 18-month lead time item if you have not started, which means it is urgent regardless of the final strategy decision.
-->

---

# 9 — Next Steps

## Recommended Actions

| Action | Owner | Due | Priority |
|---|---|---|---|
| ▲ Align on target segment (mid-market commercial vs. Medicaid first) | Leadership | This week | Critical |
| → Begin hitrust certification process | Compliance + CTO | [Date] | Critical |
| → Commission KLAS buyer survey for mid-market segment (50 respondents) | Strategy | [Date + 4 wk] | High |
| → Build AI denial management POC for roadmap evaluation | Product + Engineering | [Date + 8 wk] | High |
| ○ Brief sales team on CMS Transparency Rule opportunity | Sales + Marketing | [Date + 2 wk] | Medium |
| ○ Identify 3 target system integrators for Medicaid partnership | Business Development | [Date + 6 wk] | Medium |

**Decision needed today:** Which segment do we enter first? The build vs. buy analysis (see companion deck) depends on this choice.

<!-- SPEAKER NOTES — Slide 10 (final): Next Steps
The market overview closes by handing off to action. The "decision needed today" note at the bottom is deliberate: a market overview without a pending decision is a research report, not a strategy session. The segment choice (mid-market commercial vs. Medicaid) drives the build vs. buy recommendation in the competitive analysis deck — make sure that connection is clear. The hitrust certification start date is the most time-sensitive action: it takes 9–12 months minimum and blocks enterprise sales. If the room cannot agree on everything else, they must at minimum agree to start hitrust now. The KLAS buyer survey is a 4–6 week investment that will validate or challenge the segment prioritization — it is a high-ROI research investment before committing to a 18-month build plan.
-->
