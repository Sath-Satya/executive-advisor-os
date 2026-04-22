<h1 align="center">Executive Advisor OS</h1>

<p align="center"><strong>Think again. From first principles.</strong></p>

<p align="center"><em>An open-source executive research operating system — structured, auditable, and built for decisions that need to stand up in front of a board, a CFO, an investor, or a regulator.</em></p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-b8965a.svg?style=flat-square"></a>
  <img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-0e1b2e?style=flat-square">
  <img alt="Claude Opus 4.7" src="https://img.shields.io/badge/tuned%20for-Claude%20Opus%204.7-b8965a?style=flat-square">
  <img alt="Any LLM via LiteLLM" src="https://img.shields.io/badge/works%20with-any%20LLM-0e1b2e?style=flat-square">
  <img alt="Offline-capable" src="https://img.shields.io/badge/outputs-offline--capable-b8965a?style=flat-square">
</p>

<p align="center">
  <img src="executive_advisor_os_v2.gif" alt="Executive Advisor OS in action — structured interview, first-principles pipeline, boardroom-ready outputs" width="860">
</p>

---

## Why this exists

Most AI research tools give executives a fast answer. Very few give them a **defensible** answer.

You prompt. The LLM assumes what you meant, reaches for what it already knows, produces a polished one-shot response. Fast. Smooth. Authoritative.

**One answer. One path of reasoning. Zero audit trail. Every assumption invisible.**

Then your Boss asks *"how did you get there?"* — and a chat log isn't an answer.

That's the gap I built **Executive Advisor OS** to close. It's not another AI chatbot. It's a structured operating system that treats every strategic question like boardroom preparation — step by step, method first, with every decision documented and every assumption visible.

If you've ever been burned by an AI output that sounded great in the moment but fell apart under scrutiny — this is built to survive that scrutiny.

---

## Who it's for

- **Founders and operators** making consequential bets
- **C-suite leaders** preparing for board, investor, or strategic reviews
- **Healthcare, finance, legal, and regulated-industry executives** working with sensitive or compliance-heavy material
- **Strategy, transformation, operations, and finance teams** that need research to survive audit
- **Board members and advisors** who want AI-assisted preparation that is credible under scrutiny
- **Anyone** tired of AI that sounds confident but can't explain itself

---

## Business outcomes this delivers

| Outcome | How the OS produces it |
|---|---|
| **Faster board preparation** | Structured interview + templates + auto-versioned outputs cut multi-day prep to hours |
| **Better decision defensibility** | Every assumption visible, every framework logged, counter-arguments steel-manned |
| **Less executive ambiguity** | Three alternatives with an explicit comparison table — not a single overconfident recommendation |
| **Reusable strategic memory** | Persistent handover + session log — pick up months-old research in 3 sentences |
| **Lower AI risk exposure** | INFERRED tagging separates model guesses from your ground truth; no hidden hallucinations |
| **Portable research archive** | Each topic is a self-contained folder. Zip it, email it, move it — no database lock-in |

---

## Fit for regulated industries

This has particularly strong fit where decisions need to survive external scrutiny:

- **Healthcare / payer-provider** — CMS rule changes, Medicare Advantage strategy, prior-authorization redesign, clinical policy, network strategy
- **Financial services** — Basel compliance, regulator prep, treasury strategy, capital allocation, enterprise risk reviews
- **Private equity** — target diligence, thesis testing, portfolio-company strategy reviews, exit scenarios
- **Legal and compliance** — policy impact analysis, regulatory change briefings, contract-dependency maps
- **Board and investor prep** — quarterly narratives, capital raises, acquisition memos, board-committee materials

Two properties matter here: **(1)** every output is a self-contained artifact that can be shared, printed, or archived; **(2)** with an enterprise-approved Claude deployment, your sensitive documents never leave your approved boundary. No cloud hop this OS adds. No telemetry. No server.

---

## How it differs from just prompting an LLM

| Generic AI "deep research" | Executive Advisor OS |
|---|---|
| You prompt; it reasons in one shot | Structured 4-phase pipeline, step by step |
| Single answer | **Three alternatives** with explicit comparison on cost, reversibility, priors, key risk |
| Reasoning hidden inside the output | Full audit trail — which framework, which source, which decision, why |
| Every assumption invisible | **Frozen vs Challengeable** assumption tables, confidence-scored with evidence |
| Claude's guesses treated as facts | **INFERRED tagging** — model guesses flagged separately from your ground truth |
| Free-form chat | Structured multiple-choice interviews, depth calibrated to stakes |
| Optimistic by default | **Mandatory pre-mortem + steel-manned counter-arguments + cognitive-bias sweep** |
| Runs even on unfit problems | **Declines hotfixes, well-solved problems, taste decisions, pure speculation** — suggests a better tool |
| Forgets between sessions | Persistent memory — `/continue` resumes exactly where you left, 3-sentence catch-up |
| Drifts into "should we build this?" | Research-scope is a non-negotiable rule — never proposes tools/systems/code |
| Output looks like a chat log | Boardroom-polished HTML, Marp decks (PPTX/PDF/HTML export), audit-grade MD — print-safe, email-safe |
| One-off | Live dashboard tracking every topic, every version, every output |
| Locked to one provider | Works with **any LLM** (Claude, GPT-4, Gemini, Azure, Mistral) via Python CLI |

---

## How it actually works

### Step 1 — You drop your documents first
Company reports, compliance filings, competitor decks, process memos, briefing notes, transcripts, financial exports — anything that matters. Drop them into the research folder. The system reads them all, fully, **before** asking a single follow-up question.

### Step 2 — It classifies the stakes
Every topic is auto-classified into one of four complexity tiers:

| Tier | Triggers | Depth |
|---|---|---|
| **Simple** | Single topic, internal audience, short memo | 1 round of questions |
| **Standard** | Multi-angle, one audience, one deadline | 2 rounds |
| **Complex** | Board-level, multi-stakeholder, regulatory/financial exposure | 3–5 rounds |
| **Strategic-deep** | M&A, market entry, major policy shift, multi-year bets | 5+ rounds, no ceiling |

### Step 3 — It interviews you with structured multiple-choice questions
Four per round, each with concrete options plus *"Other — I'll type it."* Simple topics complete in one round. Strategic-deep topics keep going until the research picture is genuinely clear. Your time is worth more picking from well-framed options than composing prose.

### Step 4 — It goes to the internet for what documents don't cover
Market sizing, competitor signals, regulatory context, industry benchmarks, press coverage. Then it loops back and asks for more if anything is still missing.

### Step 5 — It knows when NOT to run
The system auto-declines four kinds of problems:

| Case | Signal | Redirect it offers |
|---|---|---|
| **Urgent / hotfix** | Minutes to decide; production down | *"Use a fast-path recommendation; we'll do first-principles in the post-mortem."* |
| **Well-solved** | Answer is widely documented and uncontested | *"Standard answer is X. Want first-principles anyway, or use the standard?"* |
| **Taste / preference** | Decision is aesthetic or values-based | *"First-principles doesn't decide taste. Want a frameworks comparison instead?"* |
| **Insufficient evidence** | All inputs are speculation | *"This is scenario territory. A structured scenario analysis will serve better."* |

Rigor isn't the right tool for every job. The system tells you when it's the wrong fit.

### Step 6 — For Strategic-deep topics, a 4-phase first-principles pipeline auto-invokes inside `/new-research`
After classification, before output generation, the first-principles skill runs as an explicit phase of the research workflow — transparently, named in conversation, no black box. It is not a separate autonomous engine; it is a skill the `/new-research` workflow invokes once the complexity classifier tags the topic Strategic-deep.

- **Phase 1 — Deconstruct.** Feynman re-frame ("explain the real question in plain language") → Aristotelian decomposition across Substance / Quality / Quantity / Relation / Time / Place → Musk / 5-Whys drill until a law of physics, a regulation, a contract, or grounded evidence → Cartesian doubt tests every candidate axiom.
- **Phase 2 — Challenge assumptions.** Every assumption is inventoried with a confidence score and evidence link. **Frozen** (regulatory, contractual, political, ethical) are separated from **Challengeable**. Load-bearing assumptions are flagged. **Frozen-thaw sidebar:** the top 2–3 frozen assumptions get a *"if this later thaws, the recommendation shifts toward X"* note — critical for multi-year horizons.
- **Phase 3 — Reconstruct from axioms.** Exactly three alternatives — stress-tested through Munger's mental-model latticework, Meadows' systems-thinking leverage points, Bezos two-way vs one-way doors, and Bayesian priors.
- **Phase 4 — Pre-mortem stress-test.** Mandatory: *"It's two years from now. This recommendation was executed. It failed spectacularly. What happened?"* Plus steel-manned counter-arguments. Plus a cognitive-bias sweep (anchoring, sunk cost, confirmation, planning fallacy).

None of these are mine. The discipline is borrowed from people I admire. The engineering is stitching them into a pipeline that runs every time, on every decision that matters, without asking you to remember the frameworks.

- **Charlie Munger** — mental-model latticework (inversion, opportunity cost, circle of competence, incentive alignment, social proof, loss aversion, Lollapalooza effects)
- **Warren Buffett** — circle of competence as a decision gate
- **Jeff Bezos** — two-way vs one-way doors, regret minimization
- **Richard Feynman** — "if you can't explain it simply, you don't understand it" re-framing
- **Donella Meadows** — systems-thinking leverage points (*Thinking in Systems*)
- **Elon Musk** — constraint-drill reasoning to the terminal "why?"
- **René Descartes** — doubt as a discipline (reject anything not clearly and distinctly true)
- **Aristotle** — categorical decomposition (six categories of being applied to decisions)
- **Thomas Bayes** — priors and updating on evidence

### Step 7 — Paralysis guardrails (4 protections)
Rigor without over-analysis:

1. **Max-depth cap** — decomposition stops at 5 layers unless you explicitly ask for more
2. **Signal-to-noise pruning** — before going deeper on any branch, the system asks *"does this change the recommendation? If no, prune."*
3. **Time-box signal** — after heavy token burn in one phase, it prompts *"more depth here, or move on?"*
4. **Escape hatches every phase** — `proceed / stop here and write what we have / skip to output`

Say *"that's enough"* anytime and it writes what it has. No fighting the tool.

### Step 8 — INFERRED tagging: you always know what Claude made up
When the model has to infer an axiom without your document evidence, it tags it **INFERRED** in the assumption inventory. You see — at a glance — what came from your documents, what came from the internet, and what Claude inferred itself. Your ground truth stays separated from the model's best guesses.

### Step 9 — Confidence rubric with evidence links
Every assumption carries one of four confidence labels plus a one-line citation:

| Label | Means |
|---|---|
| **High** | Grounded in law, regulation, contract, or robust data |
| **Medium** | Industry convention, reasonable empirical backing |
| **Low** | Inferred, conventional, or single-source |
| **Speculative** | No evidence; Claude or user inference only |

No hand-waving. Every claim cite-able.

### Step 10 — Large-artifact protection (no truncation)
A non-negotiable rule prevents the "response hit length limit" failure mode: for any output > 300 lines, the system **plans in Markdown first → builds in chunks → merges → reviews** against a checklist before claiming complete. No half-written briefings. No broken decks.

### Step 11 — Three output formats, ready to share
| Output | What it is | When |
|---|---|---|
| **Executive summary** (MD) | 400–550 words, decision-ready | Always generated |
| **Detailed analysis** (MD) | Full depth, evidence, objections | Internal deep-dives |
| **HTML briefing** | Self-contained, 10–20 pages, print-safe, email-safe, runs offline with graceful font fallback | Board prep, external share |
| **Summary deck** (Marp, 3 slides) | Elevator: framing + 3 points + CTA, presenter notes on every slide | Opens a conversation |
| **Detailed deck** (Marp, 10–12 slides) | Full narrative with presenter notes on every slide | Board presentations |
| **First-principles analysis** (MD) | Mermaid decomposition tree + frozen/challengeable assumption tables + 3-alternative comparison + pre-mortem + counter-arguments + bias sweep + reasoning trace | Audit-grade (Strategic-deep) |

Pick any combination. Executive summary always ships. Every deck has presenter notes on every slide — not optional.

### Step 12 — Decks export to PPTX, PDF, or HTML in one line
All decks are Marp-compatible Markdown. To convert:
```bash
marp --pptx research/cms-2026/output/deck_detailed_v1.pptx
marp --html research/cms-2026/output/deck_detailed_v1.html
```
No vendor lock-in. No paid converter. One CLI.

### Step 13 — Mermaid decomposition tree, rendered inline
Phase 1 of every Strategic-deep analysis renders a left-to-right Mermaid tree showing the decomposition. Load-bearing paths highlighted. Renders natively in VS Code, GitHub, modern browsers, and any Markdown viewer that speaks Mermaid. No image pipeline needed.

### Step 14 — Auto-versioning — v1 never overwritten once v2 exists
Every run bumps the version. Want to see how your thinking evolved? Every previous version is preserved. Ask *"what if X changes?"*, re-run, get v2 alongside v1. Compare side by side.

### Step 15 — Memory + context managed automatically
- Warns you at **70% context utilization**
- Auto-writes `handover.md` + `session-log.md` at session end
- Type `/continue your-topic-slug` two weeks later — 3-sentence catch-up, resume exactly where you left
- Separate handover (current state) from session-log (chronological audit)

### Step 16 — Run multiple research projects in parallel, they never collide
Every topic lives in its own folder. Zip one and email it — handover, session log, and all outputs travel together. No database, no export dance. Research is portable.

### Step 17 — A live dashboard, one place for everything
`research/dashboard.html` auto-regenerates after **every step** of every command — not just at session end — when run inside Claude Code, Claude.ai, or VS Code + Claude extension (these give the model the file-system tool-use it needs to rewrite the page; the Python CLI via LiteLLM does not itself regenerate the dashboard — it's a prompt router, see Requirements).

The dashboard carries:
- A sticky topbar with a `↻ Refresh` button, a `◷ Auto-refresh` toggle (30-second polling, persisted in localStorage), and a live `Last updated` timestamp
- A persistent left sidebar listing every topic with a status dot — click to jump to that topic's card
- A 4-stat header: Topics / Active / Completed / Removed
- One card per topic with an **expandable file tree** showing every file under `output/` and `.memory/` — click any file to open it in a new tab
- Status indicators: Active / Completed / Needs Review / **Removed**
- Removed-detection: delete a research folder from your file explorer and the next regeneration marks it `Removed`; `/dismiss <slug>` drops it from the dashboard permanently

---

## 160+ boardroom-ready templates, invisible to you

The system ships with **80 HTML briefing templates + 80 Marp-compatible deck templates** covering:

- Executive briefings and one-pagers
- Board reports and board packs
- Pitch decks and sales strategy
- ROI / business case presentations
- Dashboards and status trackers
- Compliance and regulatory memos
- Market analysis and competitor deep-dives
- M&A fit assessments
- Crisis communications
- Training and workshop decks

All SponAItech-branded, print-safe, email-safe. The system picks the right starting point for your topic — you never touch CSS or a template gallery.

---

## Design principles

This project is grounded in a few core beliefs that shape every feature:

- **Strategic AI should improve judgment, not just accelerate output.**
- **Executive workflows need structure, not just conversation.**
- **Research should be explainable, reviewable, and portable.**
- **First-principles thinking should be operationalized, not merely admired.**
- **Outputs should be polished enough for real executive use** — no chat logs, no screenshots of markdown.
- **Your assumptions belong on the table, not hidden in the answer.**
- **Three alternatives is a minimum discipline; one answer is laziness.**
- **Counter-arguments are not optional.** If you can't steel-man the opposing view, you haven't done the work.

---

## The frameworks it runs on

Most AI tools namedrop "first-principles thinking" as a prompt. This OS operationalizes it — ten distinct mental models wired into a four-phase pipeline that runs the same way on every Strategic-deep topic. You never have to remember the frameworks; the pipeline applies them in sequence and surfaces the output in plain executive language.

**Phase 1 — Deconstruct.** The question gets re-framed in plain language (**Feynman**: if you can't explain it simply, you don't understand it), then broken across six categories of being — substance, quality, quantity, relation, time, place (**Aristotle**). Each material piece is drilled with "why?" until the answer hits a law, regulation, contract, or grounded fact (**Musk / 5-Whys**). Every candidate axiom is then tested for self-evidence (**Descartes**: reject anything not clearly and distinctly true).

**Phase 2 — Challenge Assumptions.** Every explicit and implicit assumption is inventoried, split into **Frozen** (regulatory, contractual, ethical — boundaries, not debates) vs **Challengeable**, and scored for confidence with evidence. Anything whose reversal would materially change the recommendation gets tagged **load-bearing**.

**Phase 3 — Reconstruct three alternatives.** Each path is built from axioms up, then cross-checked with **Munger's latticework** (inversion, opportunity cost, circle of competence, incentive alignment, Lollapalooza risk), **Meadows' systems-thinking** (feedback loops, leverage points, second-order effects), **Bezos' two-way vs one-way door** test, and **Bayesian priors** with the evidence that would update them. **Buffett's circle of competence** serves as the go/no-go gate.

**Phase 4 — Pre-mortem.** Assume the recommendation failed two years out; write the autopsy. Steel-man every counter-argument. Sweep for anchoring, sunk-cost, confirmation, and planning-fallacy biases — flag each with the mitigation applied.

That sequence — ten models, four phases, one audit trail — is the unique engineering.

---

## Requirements

**One of these environments:**

- **Claude Code** *(recommended — best experience; full tool-use for folder ops, memory, and dashboard regeneration)*
- **Claude.ai** — browser or desktop; drag `CLAUDE.md` into a new conversation
- **VS Code** with the official Claude extension

**Model:**
**Tuned for Claude Opus 4.6 and Opus 4.7** — first-principles accuracy depends on a top-tier model. Opus 4.7 is the sweet spot. Sonnet works for Simple / Standard tiers. Haiku is not recommended for Strategic-deep research.

**Works with any LLM:** Claude, GPT-4, Gemini, Azure OpenAI, Mistral — via the included Python CLI (LiteLLM). Not locked to Anthropic.

**Important — what the Python CLI does and does not do:**
The included `run.py` routes prompts through LiteLLM and maintains a chat history. It is *not* a standalone execution engine — it does not itself perform file creation, memory reconciliation, or dashboard regeneration. For full orchestration (folder creation, output versioning, auto-dashboard, `/continue` resumption), use **Claude Code, VS Code with Claude extension, or Claude.ai** — those environments give the model the tool-use it needs. Use the Python CLI for advisory conversations with non-Claude LLMs and when you're comfortable running the file operations yourself.

**Runs fully locally** on Mac or Windows. No server. No telemetry.

**Offline behavior:**
Every HTML output is self-contained and opens in any browser with no external JS or CSS dependencies. Typography uses Google Fonts with a graceful system-font fallback (Georgia / system-ui / system mono) — if Wi-Fi is off or you're in an air-gapped environment, the document remains fully readable and print-safe; fonts simply degrade.

### Privacy and enterprise use

If your company has approved Claude enterprise (via Anthropic, AWS Bedrock, Google Vertex, or Azure AI), your documents and prompts stay inside that enterprise boundary. This operating system adds no external data hop.

For regulated industries (healthcare, finance, legal), this matters: you can run compliance analysis, M&A due diligence, or clinical strategy research on sensitive documents without them leaving your approved environment.

---

## Quick start (5 minutes)

### Step 1 — Download
```bash
git clone https://github.com/Sath-Satya/executive-advisor-os.git
cd executive-advisor-os
```
Or click **Code → Download ZIP** on GitHub, unzip anywhere.

### Step 2 — Open in your AI tool

**Claude Code** *(recommended):*
```bash
claude
```

**VS Code:** `File → Open Folder`, then open the Claude chat panel.

**Claude.ai:** New conversation, drag `CLAUDE.md` into the chat, type `/new-research`.

### Step 2.5 — One-time setup (paste into Claude Code)

Copy the block below and paste it as your first message in Claude Code (or VS Code's Claude chat). Claude will check Python, install the one dependency needed for PowerPoint deck generation, and verify the deck converter + hook are in place — all in about 60 seconds.

```
Please set up Executive Advisor OS. Run each step and report progress:

1. Verify Python 3.9 or newer is available — run `python --version` (try `python3 --version` on Mac/Linux if the first fails). If missing or older than 3.9, stop and tell me the exact install instructions for my OS.
2. Check whether python-pptx is importable — run `python -c "import pptx; print('pptx', pptx.__version__)"`. If it errors, install every Python dependency this repo needs by running `pip install -r requirements.txt`.
3. Re-run the import check to confirm the install worked.
4. Confirm the deck converter and its auto-convert hook are on disk — verify these three files exist: `.claude/scripts/md_to_pptx.py`, `.claude/hooks/auto_convert_deck.py`, `.claude/settings.json`.
5. Print "Setup complete — ready for /new-research" or list exactly what is still missing and how to fix it.
```

**Why use this instead of typing `pip install` yourself:**
- You do not need to know pip, terminal commands, or which Python version you have — Claude runs each check and shows the result
- `requirements.txt` pins the versions — no guessing which package release to use
- If something fails (wrong Python, no pip, corporate firewall), Claude reports exactly what went wrong instead of a cryptic shell error
- The deck converter and `PostToolUse:Write` hook are verified in place before your first research session — so the first deck you generate actually produces a PowerPoint file without any "missing dependency" surprise mid-run
- For Claude.ai browser users: skip this block — Claude.ai cannot execute shell commands on your machine. Install `python-pptx` manually once (`pip install python-pptx`) and run `/verify-outputs <slug>` at session end to confirm PPTX files were produced

### Step 3 — Pick Opus 4.6 or 4.7
Set model to `claude-opus-4-7` (Claude Code/VS Code) or pick Opus from the Claude.ai model selector.

### Step 4 — Run your first research
```
/new-research
```

### Step 5 — Open the dashboard
After your first session completes:
```
research/dashboard.html
```
Bookmark it.

### Using a non-Claude LLM?
```bash
pip install -r requirements.txt
cp .env.example .env       # edit with your model + API key
python run.py              # interactive mode
```
Any LiteLLM-supported provider works for the model calls. See Python CLI note in Requirements above for scope. Full setup details: `SETUP.md`.

---

## Commands

| Command | Purpose |
|---|---|
| `/new-research` | Start a new topic. Classifies complexity, asks structured questions, delivers outputs. Auto-invokes first-principles on Strategic-deep. |
| `/continue [topic-slug]` | Resume any existing research. Loads the handover, bumps the version, regenerates. |
| `/recalibrate [file]` | Dropped in a document you forgot? Add it — outputs regenerate at next version, no questions asked. |
| `/status` | See every research topic, current version, what outputs exist. |
| `/first-principles [topic]` | Invoke the 4-phase reasoning pipeline directly, standalone. |
| `/dismiss [slug]` | Permanently drop a removed research slug from the dashboard (only once the folder is actually deleted from disk). |

---

## Folder structure

```
executive-advisor-os/
├── README.md                        ← This file
├── CLAUDE.md                        ← The advisor's system prompt
├── SETUP.md                         ← Full setup (3 environments + Python CLI)
├── CHEATSHEET.md                    ← Command + output reference
├── HELP.html                        ← Illustrated walkthrough (open in any browser)
├── LINKEDIN_POST.md                 ← Ready-to-post launch copy
├── QUALITY_RUBRIC.md                ← How to judge output quality
├── CHANGELOG.md                     ← Version history
├── LICENSE                          ← MIT
├── run.py                           ← Python CLI (LiteLLM prompt router)
├── .env.example                     ← API key template for LiteLLM
├── requirements.txt                 ← Python deps (only if using run.py)
├── .claude/
│   ├── commands/                    ← 7 slash commands
│   ├── rules/                       ← Operational rules (visual identity, model routing, large-artifact)
│   └── skills/
│       ├── html-generation/         ← 80 HTML briefing templates
│       ├── deck-generation/         ← 80 Marp deck templates (PPTX/PDF/HTML export)
│       └── first-principles/        ← 4-phase reasoning pipeline
└── research/
    ├── dashboard.html               ← Auto-updating master view
    └── <your-topic-slug>/
        ├── .memory/
        │   ├── handover.md          ← Current state — loads on /continue
        │   └── session-log.md       ← Chronological audit log
        └── output/
            ├── executive_summary_v1.pptx
            ├── detailed_analysis_v1.md
            ├── deck_summary_v1.md
            ├── deck_detailed_v1.pptx
            ├── briefing_v1.html
            └── first-principles-analysis_v1.md   ← Strategic-deep only
```

Each research topic is a self-contained folder. Zip it, email it, move it between machines — handover, session log, and outputs travel together. No database, no export dance.

---

## How to judge a good output

See `QUALITY_RUBRIC.md` for the four-check rubric:

1. Are assumptions explicit and confidence-scored?
2. Are the three alternatives genuinely distinct?
3. Is the recommendation tied to axioms and evidence?
4. Are counter-arguments steel-manned?

---

## Non-negotiable rules the advisor follows

1. **Memory is always reconciled** — handover + session log updated after every session
2. **Dashboard always refreshes** — part of task completion, not optional
3. **End goal always clarified** before any analysis begins
4. **Versions never overwrite** — v1 is preserved when v2 is generated
5. **Deck sizes enforced** — summary ≤3 slides, detailed 10–12 slides
6. **Research scope is absolute** — never proposes building systems, tools, code, or procurement
7. **Clarification depth matches stakes** — Simple: 1 round. Strategic-deep: no cap.
8. **Structured interviews over free-form prompts** — your time is worth more picking from options
9. **First-principles auto-invokes inside `/new-research` on Strategic-deep topics** — after classification, before output generation, transparently named to you in conversation
10. **Presenter notes on every deck slide** — not optional
11. **Every HTML output is self-contained** — opens offline with graceful font fallback
12. **Every step documented** — which framework, which source, which decision, why
13. **Three alternatives, not one** — forces prioritization and comparison
14. **INFERRED gets tagged** — Claude's guesses never masquerade as ground truth
15. **Large artifacts are planned + chunked** — no "response hit length limit" truncation

---

## What this is not

- Not a chatbot layer
- Not a tool that generates marketing copy or SEO posts
- Not a productivity assistant for scheduling or email
- Not a general knowledge search
- Not something that pretends every question needs first-principles depth — it declines when a topic is a better fit for a different tool

It is specifically: **a practical executive reasoning system for people who want AI to support better decisions, clearer narratives, and stronger strategic preparation.**

---

## Who built this, and why

I spent 24 years in enterprise IT and 18 in healthcare. I kept watching the same pattern: strategic decisions drift on inherited assumptions nobody has tested in years. AI should raise the floor on executive reasoning — not drown it in more content.

The methodology here is borrowed from people I admire — Munger, Buffett, Bezos, Feynman, Meadows, Musk, Descartes, Aristotle, Bayes. None of it is mine. The engineering is — stitching their disciplines into an operating system that runs every time, on every decision that matters, without asking you to remember the frameworks.

Built in the open. MIT licensed. Shared because the idea is worth more in the world than locked in a vault.

— Sathiyaraj Thangavel (Satya). · https://www.linkedin.com/in/tsatya/

---

## License

MIT. Use it. Fork it. Share it. If it changes how you decide — or strengthens a decision you were already leaning into — I want to hear about it.

---

**Think again. From first principles.**

A true executive thinking partner, 24/7. Five-minute setup. MIT-licensed. Free forever.

If this direction is useful to your work — strategy, leadership, healthcare, operations, enterprise transformation, board preparation — I would genuinely value your feedback. [Star the repo](https://github.com/Sath-Satya/executive-advisor-os) · [Open an issue](https://github.com/Sath-Satya/executive-advisor-os/issues)


