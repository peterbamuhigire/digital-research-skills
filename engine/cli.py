"""CLI surface for the project kernel."""

from __future__ import annotations

import argparse
from pathlib import Path

from .scaffold import ScaffoldOptions, create_project
from .workspace import Workspace, WorkspaceError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m engine")
    subcommands = parser.add_subparsers(dest="command")

    doctor = subcommands.add_parser("doctor", help="check the engine runtime")
    doctor.add_argument("--project", help="optional project id or path to validate")

    new_project = subcommands.add_parser("new-project", help="create a canonical project workspace")
    new_project.add_argument("name", help="project name; converted to a filesystem-safe id")
    new_project.add_argument("--type", required=True, dest="research_type", help="research type")
    new_project.add_argument("--audience", required=True, help="primary audience")
    new_project.add_argument("--variant", default="standard", help="output variant")
    new_project.add_argument("--projects-dir", default="projects", help="target projects directory")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "doctor":
        return _doctor(args.project)
    if args.command == "new-project":
        return _new_project(args)

    parser.print_help()
    return 0


def _new_project(args: argparse.Namespace) -> int:
    options = ScaffoldOptions(
        name=args.name,
        research_type=args.research_type,
        audience=args.audience,
        variant=args.variant,
        projects_dir=Path(args.projects_dir),
    )
    try:
        workspace = create_project(options)
    except (FileExistsError, ValueError) as exc:
        print(f"Could not create project: {exc}")
        return 1

    print(f"Created project workspace: {workspace.root}")
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
