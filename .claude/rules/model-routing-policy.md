# Model Routing Policy — Executive Advisor OS

Tuned for Claude Opus 4.6 / 4.7. Works with any LLM via LiteLLM. This policy describes which model tier fits which research task, and when to downgrade under budget pressure.

## Tier definitions

| Tier | Models (Claude + equivalents) | Approx. cost | Fit for |
|---|---|---|---|
| **1 — Fast** | Haiku 4.5, GPT-4o-mini, Gemini Flash | ~$0.25/M tokens | Formatting, summarization, tag extraction |
| **2 — Balanced** | Sonnet 4.6, GPT-4o, Gemini Pro | ~$3/M tokens | Simple / Standard research, routine briefings |
| **3 — Power** | Opus 4.6, Opus 4.7, GPT-4 Turbo | ~$15/M tokens | Complex research, Strategic-deep first-principles |

## Routing by task

### Tier 3 — Power (default for Executive Advisor OS)
- First-principles 4-phase pipeline (any phase)
- Strategic-deep complexity tier research
- Counter-arguments + pre-mortem generation
- Assumption challenge + Bayesian prior setting
- Three-alternatives reconstruction
- Board-level / M&A / regulatory research

### Tier 2 — Balanced
- Simple / Standard tier research
- Document ingestion and summarization
- Clarification question generation
- Executive summary drafting
- Deck slide composition
- HTML briefing assembly (non-Strategic-deep)

### Tier 1 — Fast
- Slug generation for research folder naming
- Handover file formatting
- Dashboard regeneration
- Session-log entry writing
- Tag and keyword extraction
- Output file naming

## Override rules

1. **Budget pressure** — if monthly spend approaches ceiling, downgrade Tier 3 → Tier 2 on Phase 1 (Deconstruct) and Phase 4 (Pre-mortem) only. Phases 2 (Challenge) and 3 (Reconstruct) must stay at Tier 3 — they are accuracy-critical.
2. **Accuracy-critical** — regulatory, compliance, clinical, M&A, or financial topics always stay at Tier 3 regardless of budget.
3. **Batch operations** — re-running identical research with parameter changes can use Tier 2 if the analysis structure doesn't materially change.
4. **First attempt / retry** — first attempt at the recommended tier; if the output is incomplete or hallucinated, retry at Tier N+1.

## Model selection by environment

- **Claude Code / Claude.ai / VS Code:** native Opus 4.6 / 4.7 recommended. Sonnet 4.6 acceptable for Simple / Standard tiers.
- **Python CLI via LiteLLM:** any Tier 3 model from any provider — Opus 4.6/4.7, GPT-4 Turbo, or Gemini Pro / Ultra.
- **Never** use Haiku-class models for Strategic-deep research. Reasoning depth collapses; counter-arguments become shallow; bias sweeps miss detectable biases.

## How to apply

Claude automatically picks the right tier based on complexity classification. You don't need to set anything. If your account lets you choose models, pick Opus 4.7 for best results on high-stakes research. If budget matters, Sonnet 4.6 works fine for Simple and Standard tiers — keep Opus for the Complex and Strategic-deep topics where it earns its cost.
