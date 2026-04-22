<!-- TEMPLATE: vendor-roi-deck
     CATEGORY: ROI / Business Case
     USE WHEN: vendor selection decision with ROI and risk comparison across options
     SLIDE COUNT: 9
     PALETTE: Corporate hybrid (cream bg, blue accent)
     RENDER: marp --pptx 68-vendor-roi-deck.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --color-bg: #f7f4ef;
    --color-fg: #0e1b2e;
    --color-accent: #3b9eff;
    --color-gold: #b8965a;
    --color-positive: #2d6a4f;
    --color-negative: #b91c1c;
    --color-neutral: #b8965a;
    --color-muted: #5a6677;
  }
  section {
    background: var(--color-bg);
    color: var(--color-fg);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 64px;
  }
  h1 {
    color: var(--color-fg);
    font-size: 1.9rem;
    font-weight: 700;
    letter-spacing: -0.4px;
    border-bottom: 3px solid var(--color-accent);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  h2 {
    color: var(--color-accent);
    font-size: 1rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 10px;
  }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 10px; font-size: 1.0rem; line-height: 1.5; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    margin-top: 12px;
  }
  th {
    background: var(--color-fg);
    color: var(--color-bg);
    padding: 8px 12px;
    text-align: left;
  }
  td { padding: 7px 12px; border-bottom: 1px solid #d8d2c8; }
  tr:nth-child(even) td { background: #ede8e0; }
  .positive { color: var(--color-positive); font-weight: 700; }
  .negative { color: var(--color-negative); font-weight: 700; }
  .neutral  { color: var(--color-neutral);  font-weight: 700; }
  .label {
    display: inline-block;
    background: var(--color-accent);
    color: #fff;
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 4px;
    margin-bottom: 14px;
  }
  .cover-sub { font-size: 1.05rem; color: var(--color-muted); margin-top: 10px; }
  .winner-banner {
    background: #e6f4ea;
    border: 2px solid var(--color-positive);
    border-radius: 6px;
    padding: 12px 20px;
    margin-top: 14px;
    font-size: 0.95rem;
  }
  .score-cell-high { color: var(--color-positive); font-weight: 700; }
  .score-cell-mid  { color: var(--color-neutral);  font-weight: 700; }
  .score-cell-low  { color: var(--color-negative); font-weight: 700; }
  .footer-note { font-size: 0.78rem; color: var(--color-muted); margin-top: 14px; }
---

<!-- _paginate: false -->
# SponAI Consulting Client — AI Platform<br>Vendor Selection ROI Analysis

<div class="cover-sub">Procurement Decision Support — AI/ML Infrastructure Vendor Selection</div>
<div class="cover-sub">Evaluation completed: April 2026 &nbsp;|&nbsp; Prepared by: SponAItech LLC</div>
<div class="cover-sub">Confidential — For Technology Steering Committee</div>

<!--
PRESENTER NOTES — Slide 1: Title

This deck presents the vendor selection analysis for a SponAI consulting client evaluating three AI/ML infrastructure platforms. The client is a mid-market financial services firm seeking to deploy production AI workloads — including document intelligence, risk scoring, and customer service automation — on a managed platform rather than building infrastructure in-house. Three vendors were evaluated through a structured 10-week RFP process: Microsoft Azure AI Services, AWS Bedrock, and a specialist AI platform provider. The analysis covers feature fit, TCO, implementation risk, vendor stability, and long-term strategic fit. The committee needs a single, binding selection decision today.
-->

---

# The Problem — Current AI Approach Is Not Scalable

<div class="label">Problem Statement</div>

- The client currently runs **14 isolated AI proof-of-concepts** across 6 departments — each on different infrastructure, built by different vendors
- **No shared model management, no unified data pipeline, no enterprise observability** — each PoC is a silo
- Annual spend on fragmented AI tooling: **$1.4M** — for infrastructure that serves fewer than 200 users
- Time to deploy a new AI use case: **4–6 months** average due to repeated infrastructure setup
- Security and compliance review must be repeated for every new tool — **$120K per review** on average

> "We have 14 pilots and zero production AI. We need a platform, not more pilots."
> — CTO, Q1 2026 technology review

<!--
PRESENTER NOTES — Slide 2: Problem Statement

The problem is familiar to any enterprise that adopted AI opportunistically: fragmentation. Each department found its own tool, built its own infrastructure, and the result is 14 isolated experiments that collectively cost $1.4M per year while serving fewer than 200 people. The most damaging metric is the 4–6 month deployment cycle — not because building AI is slow, but because repeated infrastructure setup, security review, and data pipeline work consumes all the time. A unified platform eliminates this overhead. The $120K per-review compliance cost is a real number: the client's CISO requires a full security and data governance review for each new AI tool procurement. One platform means one review per year, not 14. The CTO quote is real — it sets the standard against which every vendor option must be measured: production-ready, not more pilots.
-->

---

# Vendor Options — Three Finalists

<div class="label">Vendor Landscape</div>

| Criterion | Vendor A — Azure AI Services | Vendor B — AWS Bedrock | Vendor C — Specialist Platform |
|---|---|---|---|
| Model access | 15+ models (OpenAI, MSFT, Meta) | 12+ models (Anthropic, Meta, Cohere) | 8 models (curated enterprise) |
| Enterprise compliance | HIPAA, SOC 2, ISO 27001 | HIPAA, SOC 2, ISO 27001 | SOC 2 only |
| Existing client infrastructure | Azure cloud (primary) | AWS (secondary) | None |
| Implementation time | 8 weeks | 10 weeks | 6 weeks |
| Vendor maturity | High (MSFT backing) | High (AWS backing) | Medium (Series C, $180M raised) |
| Reference customers (client segment) | 12 comparable | 8 comparable | 4 comparable |

<!--
PRESENTER NOTES — Slide 3: Vendor Options

The three finalists were selected from an initial 11 vendors evaluated at the RFI stage. Two factors eliminated the other eight: insufficient enterprise compliance coverage and lack of comparable customer references in the financial services segment. Vendor A (Azure) has the strategic advantage of aligning with the client's primary cloud infrastructure — single-vendor billing, unified identity management via Entra, and existing Azure support contracts. Vendor B (AWS Bedrock) is technically comparable but requires operating in a secondary cloud environment, adding complexity. Vendor C is a specialist — its 8 curated models are specifically tuned for financial services use cases, but the SOC 2-only compliance posture is a gap: the client's CISO requires ISO 27001 certification for any platform handling customer financial data.
-->

---

# Feature Comparison — Scored Against Requirements

<div class="label">Feature Assessment</div>

| Feature Category | Weight | Azure AI | AWS Bedrock | Specialist |
|---|---|---|---|---|
| Model variety and quality | 25% | <span class="score-cell-high">9.2</span> | <span class="score-cell-high">8.8</span> | <span class="score-cell-mid">7.1</span> |
| Enterprise security and compliance | 20% | <span class="score-cell-high">9.6</span> | <span class="score-cell-high">9.1</span> | <span class="score-cell-low">5.8</span> |
| Integration with existing stack | 20% | <span class="score-cell-high">9.4</span> | <span class="score-cell-mid">6.2</span> | <span class="score-cell-mid">5.5</span> |
| Observability and audit | 15% | <span class="score-cell-high">8.7</span> | <span class="score-cell-high">8.5</span> | <span class="score-cell-mid">6.9</span> |
| Developer experience / tooling | 10% | <span class="score-cell-mid">8.1</span> | <span class="score-cell-high">8.9</span> | <span class="score-cell-high">9.2</span> |
| Cost management tools | 10% | <span class="score-cell-high">8.4</span> | <span class="score-cell-mid">7.8</span> | <span class="score-cell-mid">7.2</span> |
| **Weighted Score** | | **<span class="positive">9.0</span>** | **<span class="neutral">8.0</span>** | **<span class="negative">6.4</span>** |

<!--
PRESENTER NOTES — Slide 4: Feature Comparison

The scoring methodology was agreed with the client's technology steering committee before the evaluation began — this prevents post-hoc weight adjustment to favour a preferred vendor. The weights reflect the committee's stated priorities: model quality and security are the two largest categories at 25% and 20% respectively. Azure's highest score is the security and compliance category — 9.6 reflects the full ISO 27001, HIPAA, FedRAMP, and SOC 2 Type II coverage, plus native Entra identity integration. The Specialist vendor's 5.8 in security is a genuine red flag — it would require the CISO to accept a compliance gap or conduct a custom audit engagement ($180K). AWS's 6.2 in existing stack integration reflects the multi-cloud complexity cost. Azure's 9.4 integration score reflects native connectivity with the client's existing Azure DevOps, Entra, and Azure Monitor infrastructure.
-->

---

# TCO Comparison — 3-Year Cost Analysis

<div class="label">Total Cost of Ownership</div>

| Cost Component | Azure AI Services | AWS Bedrock | Specialist Platform |
|---|---|---|---|
| Platform licence / usage (Year 1) | $280K | $310K | $220K |
| Implementation (one-time) | $420K | $520K | $380K |
| Integration with existing stack | $80K | $240K | $320K |
| Training and adoption | $60K | $75K | $90K |
| Annual support (Year 2+) | $140K/yr | $155K/yr | $130K/yr |
| Compliance audit (one-time for specialist) | — | — | $180K |
| **3-Year TCO** | **<span class="positive">$1,420K</span>** | **<span class="neutral">$1,825K</span>** | **<span class="negative">$1,890K</span>** |

<div class="footer-note">Azure integration cost advantage ($80K vs $240K–$320K) reflects existing Azure infrastructure — no additional cloud connectors required.</div>

<!--
PRESENTER NOTES — Slide 5: TCO Comparison

Azure AI Services delivers the lowest 3-year TCO at $1.42M — $405K less than AWS and $470K less than the Specialist platform. The key driver is the integration cost: $80K for Azure versus $240K for AWS (multi-cloud connector development) and $320K for the Specialist (requires building Azure-to-specialist API bridge from scratch). The Specialist platform's compliance audit is a one-time cost unique to that option — without it, the CISO will not approve deployment to production. Azure's platform usage cost of $280K in Year 1 is based on projected token consumption and compute allocation for the 14 planned use cases — SponAItech modelled this using the client's pilot usage data scaled to production estimates. The $140K annual support cost from Year 2 replaces the $1.4M current fragmented tooling spend — a net saving of $1.26M per year.
-->

---

# Risk Comparison — Three Dimensions

<div class="label">Risk Assessment</div>

| Risk Dimension | Azure AI | AWS Bedrock | Specialist |
|---|---|---|---|
| Vendor lock-in | Medium (Azure ecosystem) | Medium (AWS ecosystem) | High (proprietary models) |
| Compliance gap risk | None | None | High (ISO 27001 gap) |
| Implementation risk | Low | Medium (multi-cloud) | Medium-High |
| Model quality degradation | Low (MSFT/OpenAI backing) | Low (Anthropic partnership) | Medium (8 models, smaller roadmap) |
| Price escalation risk | Low (enterprise MSA) | Low (enterprise MSA) | Medium (Series C — pricing pressure post-Series D) |
| Support quality risk | Low (Microsoft Premier) | Low (AWS Enterprise) | Medium (smaller support team) |
| **Overall Risk Score** | **<span class="positive">Low</span>** | **<span class="neutral">Low–Medium</span>** | **<span class="negative">Medium–High</span>** |

<!--
PRESENTER NOTES — Slide 6: Risk Comparison

Risk is the dimension that eliminates the Specialist platform as a viable option despite its lower base price. The ISO 27001 compliance gap is a binary blocker for the CISO — production deployment is not permitted without it. The Specialist vendor was asked directly whether they plan to pursue ISO 27001 certification; the answer was "within 18 months, subject to funding." That is not an acceptable compliance commitment. The vendor lock-in risk for Azure and AWS is acknowledged — but it exists for any enterprise cloud platform. The mitigation is the model abstraction layer (a SponAItech design principle) that wraps model calls in a client-owned API layer, enabling future migration if needed. The price escalation risk for the Specialist is genuine: they are Series C with aggressive growth targets, and the enterprise pricing model will likely change post-Series D.
-->

---

# Recommendation — Select Azure AI Services

<div class="label">Recommendation</div>

<div class="winner-banner">
  <strong>Recommendation: Azure AI Services</strong><br>
  Highest feature score (9.0), lowest 3-year TCO ($1.42M), lowest risk profile, and best alignment with existing infrastructure. Net saving vs. current fragmented approach: $1.26M per year from Year 2.
</div>

**Commercial terms recommended:**
- 3-year Enterprise Agreement with Microsoft — lock in current pricing
- Include Azure AI Content Safety and Azure AI Document Intelligence in scope
- Negotiate SponAItech as preferred implementation partner on Azure marketplace

<!--
PRESENTER NOTES — Slide 7: Recommendation

The recommendation is clear and multi-dimensional: Azure AI Services wins on feature score, TCO, risk, and strategic alignment simultaneously. This is not a trade-off decision — Azure is the dominant choice on all four dimensions. The commercial terms recommendation is important: a 3-year Enterprise Agreement locks in current pricing before Microsoft's anticipated 2027 AI pricing adjustments. The Azure AI Content Safety module is specifically recommended because the client's CISO required evidence of content filtering capabilities for customer-facing AI applications. The SponAItech marketplace listing allows the implementation contract to be executed on the client's existing Azure Marketplace MPSA — simplifying procurement and enabling immediate contract activation.
-->

---

# Contract Terms — Key Negotiation Points

<div class="label">Contract Terms</div>

| Term | Target | Rationale |
|---|---|---|
| Contract length | 3 years | Locks current pricing; EA discount tier |
| Annual spend commitment | $280K Year 1, $200K Year 2–3 | Year 1 higher due to onboarding; Year 2+ at lower run-rate |
| Price escalation cap | 5% per year maximum | Protects against AI pricing volatility |
| SLA uptime | 99.9% for production workloads | Required for customer-facing applications |
| Data residency | US-East and US-West only | Compliance with client's data sovereignty policy |
| Exit clause | 90-day notice, data portability guaranteed | Contractual portability mitigates lock-in risk |
| Microsoft Premier Support | Included in EA pricing | Dedicated TAM and 24x7 critical incident response |

<!--
PRESENTER NOTES — Slide 8: Contract Terms

The contract terms are negotiation targets, not the starting position. The 5% price escalation cap is the most important clause — AI infrastructure pricing has been volatile, and locking the escalation rate protects the client's budget model. Microsoft will negotiate this; the opening position should be 3%, with 5% as the walk-away. The exit clause and data portability guarantee are standard Azure EA clauses but must be explicitly included — do not assume they are default. The US-East/US-West data residency restriction aligns with the client's existing data sovereignty policy; ensure this is written into the service addendum, not just referenced in the order form. Microsoft Premier Support at the EA pricing level includes a designated Technical Account Manager — this resource is valuable for architecture guidance during the 14 use-case deployment.
-->

---

# Phasing and Ask — Deploy in Three Waves

<div class="label">Deployment Plan and Ask</div>

| Wave | Timeline | Use Cases | Investment |
|---|---|---|---|
| Wave 1 — Foundation | Months 1–3 | Platform setup, identity integration, 2 pilot use cases migrated | $420K (implementation) |
| Wave 2 — Core Deployment | Months 4–9 | 8 priority use cases deployed; observability dashboard live | $280K (Year 1 licence) |
| Wave 3 — Scale | Months 10–18 | Remaining 4 use cases + 6 new use cases; automation roadmap | $200K/yr ongoing |

**The ask:** Technology Steering Committee approval to:
1. Select Azure AI Services as the enterprise AI platform
2. Authorize SponAItech to execute the 3-year EA negotiation
3. Allocate $700K (Year 1 budget) from the Technology Capital Fund

<!--
PRESENTER NOTES — Slide 9: Phasing and Ask

The three-wave deployment plan converts the vendor selection into an execution plan. Wave 1 is the foundation — it deploys the platform and migrates two of the easiest existing pilots to validate the approach. This is a 3-month confidence-building phase. Wave 2 deploys the 8 priority use cases selected by the steering committee — these are the highest-value applications, including document intelligence and risk scoring. Wave 3 scales to the full portfolio and adds new use cases identified during Waves 1 and 2. The $700K Year 1 budget covers both the implementation fee ($420K) and the first year of platform licence ($280K). This compares favourably to the current $1.4M annual spend on fragmented tooling — Year 1 is a net saving of $700K, and Year 2 onwards is a net saving of $1.2M. Ask for the three approvals explicitly and request the committee to confirm the SponAItech engagement scope.
-->
