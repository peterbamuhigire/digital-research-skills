"""Project scaffold creation."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .workspace import REQUIRED_DIRECTORIES, Workspace


CONTEXT_FILES = {
    "brief.md": "# Project Brief\n\nTODO: State the research question, client need, and decision this project supports.\n",
    "methodology.md": "# Methodology\n\nTODO: Define methods, source classes, verification routines, and limits.\n",
    "project-profile.md": "# Project Profile\n\nTODO: Record research type, domain, geography, audience, and output family.\n",
    "research-roadmap.md": "# Research Roadmap\n\nTODO: Plan waves, cohorts, verification passes, synthesis, and output milestones.\n",
    "audience.md": "# Audience\n\nTODO: Define primary and secondary audiences, tone, citation expectations, and decisions served.\n",
    "output-plan.md": "# Output Plan\n\nTODO: Define deliverables, formats, versions, and release acceptance criteria.\n",
    "audience-output-matrix.md": "# Audience Output Matrix\n\n| Audience | Output | Evidence depth | Status |\n|---|---|---|---|\n| TODO | TODO | TODO | TODO |\n",
    "cohorts.md": "# Cohorts\n\nTODO: List cohorts or state why this is a single-cohort project.\n",
    "scope.md": "# Scope\n\nTODO: Define included geographies, time periods, populations, and source classes.\n",
    "exclusions.md": "# Exclusions\n\nTODO: Record hard exclusions so later waves do not reopen them quietly.\n",
    "hypotheses.md": "# Hypotheses\n\nTODO: List working hypotheses and mark them as untested until supported by evidence.\n",
    "success-criteria.md": "# Success Criteria\n\nTODO: Define what must be true for the project to be release-ready.\n",
    "monetization.md": "# Monetization\n\nTODO: Record whether this project produces reusable, sellable, or internal-only knowledge assets.\n",
}

REGISTRY_FILES = {
    "sources.yaml": "sources: []\n",
    "claims.yaml": "claims: []\n",
    "quotes.yaml": "quotes: []\n",
    "synthesis-map.yaml": "synthesis_map: []\n",
    "sign-offs.yaml": "sign_offs: []\n",
    "waivers.yaml": "waivers: []\n",
    "release-ledger.yaml": "releases: []\n",
}


@dataclass(frozen=True)
class ScaffoldOptions:
    name: str
    research_type: str
    audience: str
    variant: str
    projects_dir: Path = Path("projects")


def slugify_project_id(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.strip().lower()).strip("-")
    if not slug:
        raise ValueError("project name must contain at least one letter or number")
    return slug


def create_project(options: ScaffoldOptions) -> Workspace:
    project_id = slugify_project_id(options.name)
    root = options.projects_dir / project_id
    if root.exists():
        raise FileExistsError(f"project already exists: {root}")

    for directory in REQUIRED_DIRECTORIES:
        (root / directory).mkdir(parents=True, exist_ok=True)

    for name, content in CONTEXT_FILES.items():
        (root / "_context" / name).write_text(content, encoding="utf-8")

    for name, content in REGISTRY_FILES.items():
        (root / "_registry" / name).write_text(content, encoding="utf-8")

    (root / "README.md").write_text(_readme(project_id, options), encoding="utf-8")
    (root / "PROJECT-STATUS.md").write_text(_status(project_id, options), encoding="utf-8")
    (root / "EVIDENCE-AUDIT.md").write_text(_evidence_audit(), encoding="utf-8")
    (root / "CLAUDE.md").write_text(_runtime_notes(project_id), encoding="utf-8")
    (root / "05-output" / "README.md").write_text("# Outputs\n\nDeliverable source and manifests live here.\n", encoding="utf-8")
    (root / "export" / "README.md").write_text("# Export\n\nRelease packs and rendered deliverables live here.\n", encoding="utf-8")

    workspace = Workspace(root.resolve())
    from .output import DEFAULT_OUTPUT_FAMILIES, seed_output_family

    for family in DEFAULT_OUTPUT_FAMILIES:
        seed_output_family(workspace, family)
    workspace.validate()
    return workspace


def _readme(project_id: str, options: ScaffoldOptions) -> str:
    return f"""# {project_id}

Research project workspace.

| Field | Value |
|---|---|
| Project id | `{project_id}` |
| Research type | {options.research_type} |
| Audience | {options.audience} |
| Variant | {options.variant} |

## Golden Path

1. Complete `_context/brief.md` and `_context/project-profile.md`.
2. Run research meta-initialization.
3. Execute research waves.
4. Run `python -m engine sync {project_id}`.
5. Run `python -m engine validate {project_id}`.
6. Build outputs in `05-output/`.
7. Run `python -m engine pack {project_id} --out export/{project_id}.zip`.
"""


def _status(project_id: str, options: ScaffoldOptions) -> str:
    return f"""# Project Status

| Field | Value |
|---|---|
| Project | `{project_id}` |
| Current phase | initiation |
| Research type | {options.research_type} |
| Audience | {options.audience} |
| Variant | {options.variant} |
| Validation state | not run |
| Open gaps | TODO |
| Outputs built | none |
"""


def _evidence_audit() -> str:
    return """# Evidence Audit

No hallucination, citation drift, or verification failure has been logged yet.

## Log Format

- Source agent / wave:
- Fabricated or corrected content:
- Caught by:
- Action:
- Lesson:
"""


def _runtime_notes(project_id: str) -> str:
    return f"""# CLAUDE.md - {project_id}

This project follows the repository-level evidence discipline. Read the root
`CLAUDE.md`, `AGENTS.md`, and `skills/source-evaluation/references/evidence-discipline.md`
before research work.

Canonical workspace root: `projects/{project_id}/`.
"""
