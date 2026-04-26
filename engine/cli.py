"""CLI surface for the project kernel."""

from __future__ import annotations

import argparse
from pathlib import Path

from .workspace import Workspace, WorkspaceError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m engine")
    subcommands = parser.add_subparsers(dest="command")

    doctor = subcommands.add_parser("doctor", help="check the engine runtime")
    doctor.add_argument("--project", help="optional project id or path to validate")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "doctor":
        return _doctor(args.project)

    parser.print_help()
    return 0


def _doctor(project: str | None) -> int:
    repo_root = Path.cwd()
    required = ["README.md", "AGENTS.md", "CLAUDE.md", "skills/source-evaluation/SKILL.md"]
    missing = [item for item in required if not (repo_root / item).exists()]
    if missing:
        print("Engine doctor failed.")
        for item in missing:
            print(f"- missing {item}")
        return 1

    if project:
        try:
            workspace = Workspace.load(project, base=repo_root)
        except WorkspaceError as exc:
            print(f"Workspace invalid: {exc}")
            return 1
        print(f"Workspace OK: {workspace.root}")
    else:
        print("Engine doctor OK.")
    return 0
