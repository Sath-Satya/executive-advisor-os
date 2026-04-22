"""
auto_convert_deck.py — PostToolUse:Write|Edit hook.

Fires after every Write or Edit tool call. If the file written matches a
deck Markdown source in a research output folder, runs the PPTX converter
automatically so the .pptx deliverable exists without Claude having to
remember to invoke it manually.

Hook contract (Claude Code):
- Reads JSON from stdin
- Writes messages to stderr (shown to Claude); stdout is quiet on success
- Exit 0 always (advisory hook, never blocks)

JSON payload shape:
  {
    "tool_name": "Write" | "Edit",
    "tool_input": {"file_path": "..."},
    ...
  }

Trigger pattern:
  <anything>/research/<slug>/output/deck_<name>_v<N>.md

On match:
  python .claude/scripts/md_to_pptx.py <md_path>

Exit codes:
  0 — always (advisory only — output-verification is the gate)
"""

import json
import re
import subprocess
import sys
from pathlib import Path


TRIGGER_RE = re.compile(
    r"(?:^|[/\\])research[/\\][^/\\]+[/\\]output[/\\]deck_[^/\\]+_v\d+\.md$"
)


def main() -> int:
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        # Malformed input — stay quiet, exit clean
        return 0

    tool_name = payload.get("tool_name", "")
    if tool_name not in ("Write", "Edit"):
        return 0

    file_path_str = (payload.get("tool_input") or {}).get("file_path", "")
    if not file_path_str:
        return 0

    if not TRIGGER_RE.search(file_path_str.replace("\\", "/")):
        return 0

    md_path = Path(file_path_str).resolve()
    if not md_path.exists():
        return 0  # Write failed upstream; nothing to do

    # Resolve converter path relative to this hook file
    converter = Path(__file__).resolve().parent.parent / "scripts" / "md_to_pptx.py"
    if not converter.exists():
        print(
            f"[auto-convert-deck] converter not found at {converter} — skipped",
            file=sys.stderr,
        )
        return 0

    pptx_path = md_path.with_suffix(".pptx")
    print(
        f"[auto-convert-deck] {md_path.name} → {pptx_path.name}", file=sys.stderr
    )

    try:
        result = subprocess.run(
            [sys.executable, str(converter), str(md_path), str(pptx_path)],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0:
            print(
                f"[auto-convert-deck] OK ({pptx_path.stat().st_size} bytes)",
                file=sys.stderr,
            )
        else:
            # Report but don't block — output-verification skill is the real gate
            print(
                f"[auto-convert-deck] converter exit {result.returncode}:\n"
                f"{result.stdout}\n{result.stderr}",
                file=sys.stderr,
            )
            print(
                "[auto-convert-deck] install hint: pip install python-pptx",
                file=sys.stderr,
            )
    except subprocess.TimeoutExpired:
        print("[auto-convert-deck] converter timed out after 60s", file=sys.stderr)
    except Exception as e:
        print(f"[auto-convert-deck] error: {e}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
