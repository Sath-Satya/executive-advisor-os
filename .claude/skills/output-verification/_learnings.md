# output-verification — Learnings

## Seed entry — 2026-04-21
**Origin:** Framework gap flagged by exec during `cms-0057-payer-implementation` session.

**What happened:** Session delivered 5 Markdown outputs + 1 HTML briefing and declared "session complete," but the two Marp deck sources (`deck_summary_v1.md`, `deck_detailed_v1.md`) were never converted to PPTX. An exec cannot present a Marp MD to a payer leadership team. The "complete" claim was false.

**Root cause:** No mandatory pre-completion audit existed. The deck-generation skill produces the Marp MD; nothing verified that the PPTX deliverable was materialized.

**Fix:** Created this skill + `output-completeness-mandate.md` rule + `md_to_pptx.py` converter. All three must be used together — the rule sets the contract, the converter does the conversion, this skill enforces the audit before completion.

**Watch for:**
- Similar gaps if new output types are introduced (PDF briefings, XLSX appendices, etc.) — the mandatory file inventory in the rule must be updated in lockstep.
- Deck workflow where Marp MD is valid and PPTX is not required (e.g., Marp-rendered HTML slideshow). If exec requests Marp-native, document that explicitly in the output contract and relax the PPTX requirement for that specific session.
