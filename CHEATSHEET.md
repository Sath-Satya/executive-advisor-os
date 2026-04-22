# Cheatsheet — Executive Advisor OS

---

## Commands

| Command | What it does |
|---|---|
| `/new-research` | Start a new topic. Classifies complexity, asks structured questions, delivers outputs. Auto-invokes first-principles on Strategic-deep topics. |
| `/continue [name]` | Pick up an existing research exactly where you left off. No re-explaining needed. |
| `/recalibrate [filename]` | Add a file you forgot to include. Regenerates everything with the new document merged in. |
| `/status` | See all your research topics, versions, and what's been produced. |
| `/first-principles [topic]` | Apply the 4-phase reasoning pipeline directly to any topic — Deconstruct → Challenge → Reconstruct → Pre-mortem. |
| `/dismiss [slug]` | Permanently drop a removed research slug from the dashboard (only works once the folder is actually deleted from disk). |
| `/verify-outputs [slug]` | Audit a research folder against the output-completeness contract — checks every requested deliverable exists on disk (including deck `.pptx` files, not just Marp `.md`). Prints PASS/FAIL. |

---

## What gets produced

| Output | What it is |
|---|---|
| `executive_summary_v[N].md` | 400–550 words. Core message, key findings, recommendation. Always generated. |
| `detailed_analysis_v[N].md` | Full depth. Background, evidence, objections, strategic recommendations. |
| `deck_summary_v[N].md` | Up to 3 slides. Title + key points + CTA. With presenter notes. |
| `deck_detailed_v[N].md` | 10–12 slides. Full narrative deck with presenter notes. |
| `briefing_v[N].html` | Standalone HTML. Open in any browser. Safe to email or share. |
| `first-principles-analysis_v[N].md` | *(Strategic-deep only)* Full 4-phase reasoning trace — Mermaid decomposition tree, assumption inventory (frozen + challengeable), 3 alternatives, pre-mortem, counter-arguments, cognitive-bias sweep. |

Ask for any combination. The executive summary is always produced. For Strategic-deep topics, the first-principles analysis is also produced automatically.

---

## Folder structure

```
research/
├── dashboard.html              ← Open in browser. Auto-updated after every session.
└── your-research-topic/
    ├── .memory/
    │   ├── handover.md         ← Full context. Loads when you /continue.
    │   └── session-log.md      ← History of every session.
    └── output/
        ├── executive_summary_v1.md
        ├── detailed_analysis_v1.md
        ├── deck_summary_v1.md
        ├── deck_detailed_v1.md
        └── briefing_v1.html
```

---

## Examples

**Starting fresh:**
```
/new-research
→ "I need to understand the impact of CMS 2026 rule changes on prior auth before my board call."
```

**Coming back after two weeks:**
```
/continue cms-2026-prior-auth
```

**You forgot to include a document:**
```
/recalibrate cms-final-rule-2026.pdf
```

**Check what you have:**
```
/status
```

---

## Rules to know

- **Versions never overwrite.** Every run creates v2, v3, etc. Nothing is lost.
- **Memory is always saved.** You can always `/continue` from exactly where you left.
- **Dashboard auto-updates** after every STEP of every command — not just at session end. It carries a refresh button, a 30-second auto-refresh toggle, a left nav of every topic, and an expandable file tree per topic. (Dashboard regeneration works inside Claude Code, Claude.ai, or VS Code + Claude extension — these give the model file-system tool-use.)
- **Questions scale with stakes.** Simple topics: 1 round of clarification. Strategic-deep: as many as needed — no cap.
- **First-principles runs automatically on Strategic-deep topics.** You'll see the method named explicitly ("here's the decomposition tree…") — it's transparent, not silent.
- **Research scope is absolute.** The advisor never proposes building systems, tools, code, or procurement. Research and reports only.
- **Deck summary = max 3 slides. Deck detailed = 10–12 slides.** Always.
- **Model matters.** Tuned for Claude Opus 4.6 / 4.7. Sonnet works for Simple / Standard tiers. Haiku is not recommended for Strategic-deep.

---

*Open `HELP.html` in your browser for the full illustrated guide.*
