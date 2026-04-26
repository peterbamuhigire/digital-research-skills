"""Manifest-driven output assembly."""

from __future__ import annotations

from pathlib import Path

from .workspace import Workspace


DEFAULT_OUTPUT_FAMILIES = ("executive-report", "proposal", "academic-paper")


def seed_output_family(workspace: Workspace, family: str) -> Path:
    output_dir = workspace.output_dir / family
    sections_dir = output_dir / "sections"
    sections_dir.mkdir(parents=True, exist_ok=True)
    intro = sections_dir / "01-introduction.md"
    if not intro.exists():
        intro.write_text(f"# {family.replace('-', ' ').title()}\n\nTODO: Draft this section.\n", encoding="utf-8")
    manifest = output_dir / "manifest.md"
    if not manifest.exists():
        manifest.write_text("# Manifest\n\n- sections/01-introduction.md\n", encoding="utf-8")
    return manifest


def assemble_output(workspace: Workspace, family: str, out: str | Path | None = None) -> Path:
    output_dir = workspace.output_dir / family
    manifest = output_dir / "manifest.md"
    if not manifest.exists():
        raise FileNotFoundError(f"output manifest not found: {manifest}")

    parts = _manifest_parts(manifest)
    if not parts:
        raise ValueError(f"manifest has no section entries: {manifest}")

    rendered: list[str] = []
    for rel in parts:
        path = (output_dir / rel).resolve()
        if output_dir.resolve() not in path.parents and path != output_dir.resolve():
            raise ValueError(f"manifest entry escapes output directory: {rel}")
        if not path.exists():
            raise FileNotFoundError(f"manifest section not found: {path}")
        rendered.append(path.read_text(encoding="utf-8"))

    out_path = Path(out) if out else output_dir / "assembled.md"
    if not out_path.is_absolute():
        out_path = workspace.root / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n\n".join(rendered).strip() + "\n", encoding="utf-8")
    return out_path


def _manifest_parts(manifest: Path) -> list[Path]:
    parts: list[Path] = []
    for line in manifest.read_text(encoding="utf-8", errors="ignore").splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            parts.append(Path(stripped[2:].strip()))
    return parts
