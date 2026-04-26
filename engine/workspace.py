"""Workspace discovery and path contracts for research projects."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


class WorkspaceError(ValueError):
    """Raised when a project workspace cannot be resolved or validated."""


REQUIRED_ROOT_FILES = ("README.md", "EVIDENCE-AUDIT.md")
REQUIRED_DIRECTORIES = (
    "_context",
    "_registry",
    "01-initiation",
    "02-research",
    "03-analysis",
    "04-synthesis",
    "05-output",
    "06-governance",
    "export",
)


@dataclass(frozen=True)
class Workspace:
    """A canonical ``projects/<project-id>/`` workspace."""

    root: Path

    @classmethod
    def load(cls, project: str | Path, *, base: str | Path | None = None) -> "Workspace":
        """Resolve and validate a workspace.

        ``project`` may be a project id under ``projects/`` or an explicit path.
        """

        candidate = Path(project)
        if not candidate.is_absolute():
            repo_root = Path(base) if base is not None else Path.cwd()
            direct = repo_root / candidate
            under_projects = repo_root / "projects" / candidate
            candidate = direct if direct.exists() else under_projects

        workspace = cls(candidate.resolve())
        workspace.validate()
        return workspace

    @property
    def project_id(self) -> str:
        return self.root.name

    @property
    def context_dir(self) -> Path:
        return self.root / "_context"

    @property
    def registry_dir(self) -> Path:
        return self.root / "_registry"

    @property
    def output_dir(self) -> Path:
        return self.root / "05-output"

    @property
    def export_dir(self) -> Path:
        return self.root / "export"

    def context_path(self, name: str) -> Path:
        return self.context_dir / name

    def registry_path(self, name: str) -> Path:
        return self.registry_dir / name

    def validate(self) -> None:
        """Validate the baseline workspace contract."""

        if not self.root.exists():
            raise WorkspaceError(f"workspace does not exist: {self.root}")
        if not self.root.is_dir():
            raise WorkspaceError(f"workspace is not a directory: {self.root}")

        missing_files = [name for name in REQUIRED_ROOT_FILES if not (self.root / name).is_file()]
        missing_dirs = [name for name in REQUIRED_DIRECTORIES if not (self.root / name).is_dir()]
        if missing_files or missing_dirs:
            details: list[str] = []
            if missing_files:
                details.append("missing files: " + ", ".join(missing_files))
            if missing_dirs:
                details.append("missing directories: " + ", ".join(missing_dirs))
            raise WorkspaceError(f"invalid workspace {self.root}: {'; '.join(details)}")

    def legacy_cohort_dirs(self) -> list[Path]:
        """Return legacy cohort directories that still follow the old shape."""

        reserved = {name.lower() for name in REQUIRED_DIRECTORIES}
        reserved.update({"export"})
        cohort_dirs: list[Path] = []
        for child in self.root.iterdir():
            if not child.is_dir() or child.name.lower() in reserved or child.name.startswith("_"):
                continue
            if all((child / name).exists() for name in ("README.md", "research", "analysis", "opportunities")):
                cohort_dirs.append(child)
        return sorted(cohort_dirs)
