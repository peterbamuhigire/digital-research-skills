"""CLI surface for the project kernel."""

from __future__ import annotations

import argparse
from pathlib import Path

from .scaffold import ScaffoldOptions, create_project
from .registry import sync_workspace
from .gates import run_all_gates
from .output import assemble_output, seed_output_family
from .pack import build_pack
from .status import format_status, inspect_status
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

    sync = subcommands.add_parser("sync", help="repair or seed project registries")
    sync.add_argument("project", help="project id or path")

    validate = subcommands.add_parser("validate", help="run deterministic project gates")
    validate.add_argument("project", help="project id or path")

    status = subcommands.add_parser("status", help="show project operating status")
    status.add_argument("project", help="project id or path")

    init_output = subcommands.add_parser("init-output", help="create an output family manifest")
    init_output.add_argument("project", help="project id or path")
    init_output.add_argument("family", help="output family name")

    assemble = subcommands.add_parser("assemble", help="assemble markdown from an output manifest")
    assemble.add_argument("project", help="project id or path")
    assemble.add_argument("family", help="output family name")
    assemble.add_argument("--out", help="optional output markdown path")

    pack = subcommands.add_parser("pack", help="build an audit-ready evidence pack")
    pack.add_argument("project", help="project id or path")
    pack.add_argument("--out", required=True, help="zip path to write")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "doctor":
        return _doctor(args.project)
    if args.command == "new-project":
        return _new_project(args)
    if args.command == "sync":
        return _sync(args.project)
    if args.command == "validate":
        return _validate(args.project)
    if args.command == "status":
        return _status(args.project)
    if args.command == "init-output":
        return _init_output(args.project, args.family)
    if args.command == "assemble":
        return _assemble(args.project, args.family, args.out)
    if args.command == "pack":
        return _pack(args.project, args.out)

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


def _sync(project: str) -> int:
    try:
        workspace = Workspace.load(project)
    except WorkspaceError as exc:
        print(f"Workspace invalid: {exc}")
        return 1
    result = sync_workspace(workspace)
    print(f"Registry sync complete: {workspace.project_id}")
    print(f"- created: {len(result.created)}")
    print(f"- repaired: {len(result.repaired)}")
    print(f"- imported sources: {result.imported_sources}")
    return 0


def _validate(project: str) -> int:
    try:
        workspace = Workspace.load(project)
    except WorkspaceError as exc:
        print(f"Workspace invalid: {exc}")
        return 1

    results = run_all_gates(workspace)
    blockers = 0
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{result.gate_id} {status} - {result.title}")
        for finding in result.findings:
            print(f"  [{finding.severity}] {finding.path}: {finding.message}")
            if finding.severity == "blocker":
                blockers += 1
    return 1 if blockers else 0


def _status(project: str) -> int:
    try:
        workspace = Workspace.load(project)
    except WorkspaceError as exc:
        print(f"Workspace invalid: {exc}")
        return 1
    print(format_status(inspect_status(workspace)))
    return 0


def _init_output(project: str, family: str) -> int:
    try:
        workspace = Workspace.load(project)
    except WorkspaceError as exc:
        print(f"Workspace invalid: {exc}")
        return 1
    manifest = seed_output_family(workspace, family)
    print(f"Output manifest ready: {manifest}")
    return 0


def _assemble(project: str, family: str, out: str | None) -> int:
    try:
        workspace = Workspace.load(project)
        out_path = assemble_output(workspace, family, out)
    except (WorkspaceError, FileNotFoundError, ValueError) as exc:
        print(f"Could not assemble output: {exc}")
        return 1
    print(f"Assembled output: {out_path}")
    return 0


def _pack(project: str, out: str) -> int:
    try:
        workspace = Workspace.load(project)
        result = build_pack(workspace, out)
    except (WorkspaceError, OSError, ValueError) as exc:
        print(f"Could not build pack: {exc}")
        return 1
    print(f"Release pack: {result.path}")
    print(f"- files: {result.files}")
    print(f"- validation blockers: {result.blockers}")
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
