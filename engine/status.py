"""Project status reporting."""

from __future__ import annotations

from dataclasses import dataclass

from .gates import run_all_gates
from .workspace import Workspace


@dataclass(frozen=True)
class ProjectStatus:
    project_id: str
    current_phase: str
    source_count: int
    source_tiers: dict[str, int]
    blockers: int
    warnings: int
    open_markers: int
    output_manifests: int
    release_entries: int


def inspect_status(workspace: Workspace) -> ProjectStatus:
    results = run_all_gates(workspace)
    blockers = sum(1 for result in results for finding in result.findings if finding.severity == "blocker")
    warnings = sum(1 for result in results for finding in result.findings if finding.severity == "warning")
    source_tiers = _source_tiers(workspace)
    return ProjectStatus(
        project_id=workspace.project_id,
        current_phase=_current_phase(workspace),
        source_count=sum(source_tiers.values()),
        source_tiers=source_tiers,
        blockers=blockers,
        warnings=warnings,
        open_markers=_open_markers(workspace),
        output_manifests=len(list(workspace.output_dir.glob("**/manifest.md"))),
        release_entries=_release_entries(workspace),
    )


def format_status(status: ProjectStatus) -> str:
    tiers = ", ".join(f"{tier}: {count}" for tier, count in sorted(status.source_tiers.items())) or "none"
    validation = "pass" if status.blockers == 0 else "blocked"
    return "\n".join(
        [
            f"Project: {status.project_id}",
            f"Current phase: {status.current_phase}",
            f"Validation: {validation} ({status.blockers} blockers, {status.warnings} warnings)",
            f"Sources: {status.source_count} ({tiers})",
            f"Open TODO/gap markers: {status.open_markers}",
            f"Output manifests: {status.output_manifests}",
            f"Release entries: {status.release_entries}",
        ]
    )


def _current_phase(workspace: Workspace) -> str:
    status_path = workspace.root / "PROJECT-STATUS.md"
    if not status_path.exists():
        return "unknown"
    for line in status_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if "Current phase" in line and "|" in line:
            parts = [part.strip() for part in line.split("|") if part.strip()]
            if len(parts) >= 2:
                return parts[-1]
    return "unknown"


def _source_tiers(workspace: Workspace) -> dict[str, int]:
    path = workspace.registry_path("sources.yaml")
    if not path.exists():
        return {}
    tiers: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        stripped = line.strip()
        if stripped.startswith("tier:"):
            tier = stripped.split(":", 1)[1].strip().strip('"')
            tiers[tier] = tiers.get(tier, 0) + 1
    return tiers


def _open_markers(workspace: Workspace) -> int:
    count = 0
    for path in workspace.root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        count += text.count("TODO")
        count += text.count("(gap)")
    return count


def _release_entries(workspace: Workspace) -> int:
    path = workspace.registry_path("release-ledger.yaml")
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8", errors="ignore").splitlines() if line.startswith("- id:"))
