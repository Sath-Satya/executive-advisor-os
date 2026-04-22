#!/usr/bin/env python3
"""Executive Advisor OS — Python CLI.

A thin command runner for non-Claude-Code environments. Routes /new-research,
/continue, /recalibrate, and /status to the model of your choice via LiteLLM.

The business logic lives in CLAUDE.md and .claude/commands/*.md — this file
just loads them as system context, ingests user input, and relays model output.

Usage:
    python run.py                       # interactive mode
    python run.py /new-research
    python run.py /continue cms-2026-prior-auth
    python run.py /recalibrate path/to/file.pdf
    python run.py /status

Environment:
    Copy .env.example to .env and fill in your model + key. See SETUP.md.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

try:
    from litellm import completion
except ImportError:
    completion = None


ROOT = Path(__file__).resolve().parent
CLAUDE_MD = ROOT / "CLAUDE.md"
COMMANDS_DIR = ROOT / ".claude" / "commands"


def load_system_prompt(command: str | None) -> str:
    """Assemble the system prompt: CLAUDE.md + the invoked command definition."""
    parts = [CLAUDE_MD.read_text(encoding="utf-8")]
    if command:
        cmd_file = COMMANDS_DIR / f"{command.lstrip('/')}.md"
        if cmd_file.exists():
            parts.append(f"\n\n---\n\n# Active command: /{command.lstrip('/')}\n\n")
            parts.append(cmd_file.read_text(encoding="utf-8"))
    return "\n".join(parts)


def run_once(command: str | None, user_input: str, model: str) -> str:
    if completion is None:
        print(
            "ERROR: litellm is not installed. Run `pip install -r requirements.txt` first.",
            file=sys.stderr,
        )
        sys.exit(2)

    system = load_system_prompt(command)
    resp = completion(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_input},
        ],
        temperature=0.3,
    )
    return resp["choices"][0]["message"]["content"]


def interactive(model: str) -> None:
    print("Executive Advisor OS — interactive mode.")
    print("Type /new-research, /continue, /recalibrate, or /status. Ctrl+C to exit.\n")
    history: list[dict[str, str]] = []
    while True:
        try:
            user = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not user:
            continue
        command = user.split()[0] if user.startswith("/") else None
        system = load_system_prompt(command)
        history.append({"role": "user", "content": user})
        resp = completion(
            model=model,
            messages=[{"role": "system", "content": system}, *history],
            temperature=0.3,
        )
        reply = resp["choices"][0]["message"]["content"]
        history.append({"role": "assistant", "content": reply})
        print(f"\n{reply}\n")


def main() -> None:
    if load_dotenv is not None:
        load_dotenv(ROOT / ".env")
    model = os.getenv("EAOS_MODEL", "claude-opus-4-7")

    args = sys.argv[1:]
    if not args:
        interactive(model)
        return

    first = args[0]
    command = first if first.startswith("/") else None
    user_input = " ".join(args[1:]) if command else " ".join(args)
    if not user_input and command:
        user_input = f"Run {command}"
    print(run_once(command, user_input, model))


if __name__ == "__main__":
    main()
