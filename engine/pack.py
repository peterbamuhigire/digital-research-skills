"""Evidence-pack export."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from .gates import run_all_gates
from .workspace import Workspace


@dataclass(frozen=True)
class PackResult:
    path: Path
    files: int
    blockers: int


def build_pack(workspace: Workspace, out: str | Path) -> PackResult:
    out_path = Path(out)
    if not out_path.is_absolute():
        out_path = workspace.root / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    validation_report = workspace.export_dir / "validation-report.md"
    blockers = _write_validation_report(workspace, validation_report)

    files = _pack_files(workspace)
    with ZipFile(out_path, "w", compression=ZIP_DEFLATED) as archive:
        for path in files:
            if path.exists() and path.is_file():
                archive.write(path, path.relative_to(workspace.root).as_posix())
        archive.write(validation_report, validation_report.relative_to(workspace.root).as_posix())

    _append_release_ledger(workspace, out_path, validation_report)
    return PackResult(out_path, len(files) + 1, blockers)


def _pack_files(workspace: Workspace) -> list[Path]:
    candidates: list[Path] = []
    candidates.extend(workspace.output_dir.glob("**/*.md"))
    candidates.extend(workspace.output_dir.glob("**/*.docx"))
    candidates.extend(workspace.output_dir.glob("**/*.pdf"))
    candidates.extend(workspace.registry_dir.glob("*.yaml"))
    candidates.append(workspace.root / "EVIDENCE-AUDIT.md")
    candidates.append(workspace.root / "PROJECT-STATUS.md")
    candidates.extend(workspace.context_dir.glob("*.md"))
    return sorted({path.resolve() for path in candidates})


def _write_validation_report(workspace: Workspace, path: Path) -> int:
    results = run_all_gates(workspace)
    blockers = 0
    lines = [f"# Validation Report", "", f"Project: `{workspace.project_id}`", ""]
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        lines.append(f"## {result.gate_id} - {result.title} - {status}")
        if not result.findings:
            lines.append("- No findings.")
        for finding in result.findings:
            lines.append(f"- `{finding.severity}` `{finding.path.relative_to(workspace.root)}` - {finding.message}")
            if finding.severity == "blocker":
                blockers += 1
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return blockers


def _append_release_ledger(workspace: Workspace, pack_path: Path, validation_report: Path) -> None:
    ledger = workspace.registry_path("release-ledger.yaml")
    if not ledger.exists():
        ledger.write_text("releases: []\n", encoding="utf-8")
    content = ledger.read_text(encoding="utf-8", errors="ignore")
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    entry = "\n".join(
        [
            f"- id: REL-{timestamp}",
            f'  version: "{timestamp}"',
            f'  date: "{datetime.now(timezone.utc).date().isoformat()}"',
            "  artifacts:",
            f'    - "{pack_path.relative_to(workspace.root).as_posix()}"',
            f'  validation_report: "{validation_report.relative_to(workspace.root).as_posix()}"',
        ]
    )
    if content.strip() == "releases: []":
        ledger.write_text("releases:\n" + entry + "\n", encoding="utf-8")
    else:
        ledger.write_text(content.rstrip() + "\n" + entry + "\n", encoding="utf-8")
