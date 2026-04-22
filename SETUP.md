# Setup — Executive Advisor OS

Five steps. Ten minutes. Then you're running board-grade research from first principles.

---

## Prerequisites — one-time, ~60 seconds

Whatever tool you use (Claude Code, VS Code + Claude, Claude.ai), Python + one package must be on your machine so deck (`.pptx`) generation works. There are two paths — pick whichever fits you.

### Path A — Self-install via Claude Code *(recommended for non-developers)*

Open the repo in Claude Code (Step 1 and Step 2 below), then paste this as your first message. Claude runs every step, installs what's missing, and verifies the deck pipeline is wired up:

```
Please set up Executive Advisor OS. Run each step and report progress:

1. Verify Python 3.9 or newer is available — run `python --version` (try `python3 --version` on Mac/Linux if the first fails). If missing or older than 3.9, stop and tell me the exact install instructions for my OS.
2. Check whether python-pptx is importable — run `python -c "import pptx; print('pptx', pptx.__version__)"`. If it errors, install every Python dependency this repo needs by running `pip install -r requirements.txt`.
3. Re-run the import check to confirm the install worked.
4. Confirm the deck converter and its auto-convert hook are on disk — verify these three files exist: `.claude/scripts/md_to_pptx.py`, `.claude/hooks/auto_convert_deck.py`, `.claude/settings.json`.
5. Print "Setup complete — ready for /new-research" or list exactly what is still missing and how to fix it.
```

**Why this path is the recommended one:**
- **No command-line literacy required.** Claude reads each step and runs it for you, reporting what happened. You don't need to know pip, shell commands, or which Python you have installed.
- **Pinned versions.** `requirements.txt` fixes the package versions the OS was built against — no guessing which release to install.
- **Accurate error messages.** If a step fails (Python missing, no pip, corporate firewall, permissions), Claude explains exactly what went wrong in plain English rather than showing a raw terminal error.
- **Verified before first use.** The deck converter AND the auto-convert hook are both checked in place, so the first deck you generate actually produces a `.pptx` — you never hit a "missing dependency" surprise mid-research.
- **Reusable.** Paste the same block any time later if you suspect something has drifted or if you rebuild your machine.

### Path B — Manual install *(for developers who prefer terminal)*

1. **Python 3.9 or newer** — already on most Macs / Linux. Windows users: install from [python.org](https://www.python.org/downloads/) and check "Add Python to PATH".
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
   (One command covers both deck generation AND the optional non-Claude Python CLI.)

**Verify:**
```
python --version            # should print 3.9+
python -c "import pptx; print(pptx.__version__)"   # should print 1.0.0 or later
```

If both commands succeed, the converter at `.claude/scripts/md_to_pptx.py` can turn deck Markdown into PowerPoint on demand.

### Why this step exists at all

Decks are a mandatory output per `.claude/rules/output-completeness-mandate.md`. Claude Code runs the converter using **your local Python**, not a bundled runtime. The `python-pptx` package must be on your machine, not just in the repo.

**If you skip the install:** the advisor still generates `deck_*.md` (Marp source) but cannot produce the `.pptx` deliverable. The converter prints a clear "missing dependency" message pointing you to the fix; the `output-verification` skill also catches this at session end and blocks the "complete" claim until the `.pptx` is materialized.

**Claude.ai browser users:** Path A's paste block won't run for you — Claude.ai cannot execute shell commands on your machine. Use Path B once, then run `/verify-outputs <slug>` at session end to confirm each deck's `.pptx` landed.

---

## Step 1 — Download the repo

**Option A — ZIP (no Git needed):**
Go to the GitHub page and click **Code → Download ZIP**, then unzip it anywhere on your machine.

**Option B — Git:**
```
git clone https://github.com/Sath-Satya/executive-advisor-os.git
cd executive-advisor-os
```

---

## Step 2 — Open it in your AI tool

Pick one — you only need one.

### Claude Code *(recommended — best experience)*
From the repo folder:
```
claude
```
Inside Claude Code, the full orchestration works out of the box — slash commands, memory reconciliation, dashboard regeneration, and first-principles auto-invocation. Claude Code gives the model the file-system tool-use it needs to perform these actions directly. (The Python CLI in this repo is a prompt router only — see §Python CLI below.)

### VS Code with the Claude extension
1. Open the folder in VS Code: `File → Open Folder… → executive-advisor-os`
2. Make sure the official Claude extension is installed and signed in (search "Claude" in Extensions)
3. Open the Claude chat panel (`Ctrl+Shift+L` on Windows, `Cmd+Shift+L` on Mac)
4. Slash commands work in the chat panel

### Claude.ai *(browser or desktop app)*
1. Open [claude.ai](https://claude.ai)
2. Start a new conversation
3. Drag the file `CLAUDE.md` into the chat window to load the advisor
4. Optionally drag `.claude/commands/new-research.md` to load the command definition
5. Type `/new-research` to start

> **Tip:** Claude.ai has the lightest setup but the weakest memory between sessions. For ongoing research that you'll continue for weeks, Claude Code or VS Code are stronger.

---

## Step 3 — Pick the right model

The advisor works with any large language model, but **first-principles reasoning accuracy depends on model quality**.

| Model | Recommended for |
|---|---|
| **Claude Opus 4.7** | Strategic-deep topics, board decisions — **best pick** |
| **Claude Opus 4.6** | Same tier — also excellent |
| **Claude Sonnet 4.6** | Simple / Standard complexity — good, fast, cheaper |

**In Claude Code / VS Code:**
```
claude --model claude-opus-4-7
```
Or set it via your settings: `model: claude-opus-4-7`.

**In Claude.ai:** pick Opus from the model selector at the top of the chat.

---

## Step 4 — Run your first research

From inside your AI tool, type:
```
/new-research
```

The advisor will:
1. Ask what you're working on (one sentence is fine)
2. Create a research folder named from your topic
3. Ask your end goal + audience + any documents you want reviewed
4. **If you have documents, drop them into the new folder** — the advisor reads them before asking anything else
5. Classify the complexity (Simple / Standard / Complex / Strategic-deep)
6. Run structured multiple-choice clarification rounds (as many as the stakes deserve)
7. For Strategic-deep topics: auto-invoke first-principles reasoning (4 phases, named transparently to you)
8. Ask what outputs you want — executive summary (always), detailed analysis, summary deck, detailed deck, HTML briefing
9. Generate everything to `research/<your-topic>/output/`, versioned `v1`

---

## Step 5 — Open the dashboard

After your first session, open this in any browser:
```
research/dashboard.html
```

One page, every research topic, current status, **expandable file tree** with click-to-open links to every output. Updates after every step (not just session end). Has a `↻ Refresh` button and a 30-second auto-refresh toggle in the topbar. **Bookmark it.** This is your master view.

---

## You're done.

Research lives under `research/<topic>/`. Memory is automatic. Versions never overwrite. Pick up any topic weeks later with:
```
/continue <topic-slug>
```

Forgot to include a document? Drop it in and run:
```
/recalibrate <filename>
```

See everything you've researched:
```
/status
```

Apply first-principles reasoning directly to any topic (standalone, outside `/new-research`):
```
/first-principles <topic>
```

Audit a research folder's deliverables on demand (checks every `.pptx`, HTML, MD is on disk):
```
/verify-outputs <topic-slug>
```

Clean up a deleted research folder from the dashboard:
```
/dismiss <topic-slug>
```

For command and output reference, see `CHEATSHEET.md`.
For the full illustrated walkthrough, open `HELP.html` in your browser.

---

## Optional — Python CLI for non-Claude environments

If you want to run the advisor against another LLM (OpenAI, Gemini, Mistral, Azure OpenAI, etc.) via [LiteLLM](https://github.com/BerriAI/litellm):

```
pip install -r requirements.txt
cp .env.example .env       # then edit .env with your model + API key
python run.py              # interactive mode
```

Or one-shot:
```
python run.py /new-research
python run.py /continue cms-2026-prior-auth
```

### What the Python CLI does and does not do

The included `run.py` is a **thin prompt router** — it loads `CLAUDE.md` and the relevant command definition as a system prompt, sends your messages through LiteLLM, and maintains chat history. That is all it is.

**It does NOT itself do:**
- Folder creation or file writes
- Versioning `v1 → v2` of output files
- Memory reconciliation (writing `handover.md` / `session-log.md`)
- Dashboard regeneration
- Reading PDFs from disk into the model context
- Executing slash commands as discrete workflows

**Why that matters:** the intelligence of Executive Advisor OS depends on the LLM having tool-use for file operations — creating folders, writing outputs, reading documents you drop in. Claude Code, VS Code (with the Claude extension), and Claude.ai all provide this. LiteLLM by itself does not.

**Recommended use of the Python CLI:**
- Advisory conversations and draft outputs with a non-Claude LLM
- Testing prompt logic without tool overhead
- When you're comfortable copying outputs into files yourself
- When you're behind a corporate firewall that blocks Claude but allows your approved LLM

**For the full orchestrated experience** (folder creation, auto-versioning, memory, dashboard, `/continue` resumption) → use Claude Code, VS Code + Claude extension, or Claude.ai. This is the recommended path.

---

## Need help?

- See `CHEATSHEET.md` for commands + outputs
- Open `HELP.html` in your browser for the illustrated walkthrough
- Check the `README.md` for the full feature overview
- Issues / questions: open a GitHub issue
