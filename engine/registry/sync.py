"""Synchronise project registries with the workspace baseline."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from ..workspace import Workspace
from .schemas import SCHEMAS, RegistrySchema


@dataclass(frozen=True)
class SyncResult:
    created: tuple[Path, ...]
    repaired: tuple[Path, ...]
    imported_sources: int


def sync_workspace(workspace: Workspace) -> SyncResult:
    created: list[Path] = []
    repaired: list[Path] = []

    workspace.registry_dir.mkdir(exist_ok=True)
    for schema in SCHEMAS:
        path = workspace.registry_path(schema.filename)
        if not path.exists():
            path.write_text(f"{schema.root_key}: []\n", encoding="utf-8")
            created.append(path)
            continue
        if not _has_root_key(path, schema):
            path.write_text(f"{schema.root_key}: []\n", encoding="utf-8")
            repaired.append(path)

    imported = _import_legacy_sources(workspace)
    return SyncResult(tuple(created), tuple(repaired), imported)


def _has_root_key(path: Path, schema: RegistrySchema) -> bool:
    content = path.read_text(encoding="utf-8").splitlines()
    return any(line.strip() == f"{schema.root_key}: []" or line.startswith(f"{schema.root_key}:") for line in content)


def _import_legacy_sources(workspace: Workspace) -> int:
    sources_path = workspace.registry_path("sources.yaml")
    content = sources_path.read_text(encoding="utf-8")
    if "\n-" in content:
        return 0

    source_lines: list[str] = []
    for legacy in sorted(workspace.root.glob("*/research/sources.md")):
        for line in legacy.read_text(encoding="utf-8", errors="ignore").splitlines():
            stripped = line.strip()
            if not stripped.startswith("-"):
                continue
            source_lines.append(stripped.lstrip("-").strip())

    if not source_lines:
        return 0

    today = date.today().isoformat()
    rows = ["sources:"]
    for index, source in enumerate(source_lines, start=1):
        safe_source = source.replace('"', "'")
        rows.extend(
            [
                f"- id: SRC-{index:04d}",
                f'  title: "{safe_source[:120]}"',
                f'  ref: "{safe_source}"',
                '  tier: "TODO"',
                f'  accessed: "{today}"',
                '  verification: "imported-from-legacy-sources-md"',
                '  confidence: "TODO"',
            ]
        )
    sources_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return len(source_lines)
