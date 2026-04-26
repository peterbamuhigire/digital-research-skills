"""Seed small kernel example projects."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.output import assemble_output
from engine.scaffold import ScaffoldOptions, create_project
from engine.workspace import Workspace


EXAMPLES = (
    ("Example Market Landscape", "market landscape", "internal strategy", "executive-report"),
    ("Example Due Diligence Dossier", "due diligence", "investor", "evidence-dossier"),
    ("Example Academic Paper", "paper", "academic reviewers", "academic-paper"),
)


def main() -> int:
    projects_dir = Path("projects")
    for name, research_type, audience, family in EXAMPLES:
        project_id = name.lower().replace(" ", "-")
        root = projects_dir / project_id
        if root.exists():
            shutil.rmtree(root)
        workspace = create_project(
            ScaffoldOptions(
                name=name,
                research_type=research_type,
                audience=audience,
                variant=family,
                projects_dir=projects_dir,
            )
        )
        _complete_context(workspace, research_type, audience, family)
        _complete_registries(workspace)
        _complete_outputs(workspace, family)
        assemble_output(workspace, family)
    return 0


def _complete_context(workspace: Workspace, research_type: str, audience: str, family: str) -> None:
    replacements = {
        "brief.md": f"# Project Brief\n\nThis example demonstrates the kernel workflow for a {research_type} project.\n",
        "methodology.md": "# Methodology\n\nDesk research, registry tracking, validation gates, and manifest-driven output assembly.\n",
        "project-profile.md": f"# Project Profile\n\nResearch type: {research_type}\n\nAudience: {audience}\n",
        "research-roadmap.md": "# Research Roadmap\n\n1. Initiation\n2. Research\n3. Verification\n4. Synthesis\n5. Output\n6. Pack\n",
        "audience.md": f"# Audience\n\nPrimary audience: {audience}.\n",
        "output-plan.md": f"# Output Plan\n\nPrimary deliverable family: {family}.\n",
        "audience-output-matrix.md": f"# Audience Output Matrix\n\n| Audience | Output | Evidence depth | Status |\n|---|---|---|---|\n| {audience} | {family} | registry-backed | ready |\n",
        "cohorts.md": "# Cohorts\n\nSingle example cohort.\n",
        "scope.md": "# Scope\n\nDemonstration scope only; no external factual claims are made.\n",
        "exclusions.md": "# Exclusions\n\nNo live research claims, names, statistics, or URLs are included.\n",
        "hypotheses.md": "# Hypotheses\n\nNo substantive hypothesis is tested in this fixture.\n",
        "success-criteria.md": "# Success Criteria\n\nWorkspace validates with no blocking gate findings.\n",
        "monetization.md": "# Monetization\n\nReusable as a kernel test fixture.\n",
    }
    for name, content in replacements.items():
        workspace.context_path(name).write_text(content, encoding="utf-8")


def _complete_registries(workspace: Workspace) -> None:
    workspace.registry_path("sources.yaml").write_text(
        """sources:
- id: SRC-0001
  title: "Fixture source"
  ref: "local fixture"
  tier: "fixture"
  accessed: "2026-04-26"
  verification: "local-test-fixture"
  confidence: "high"
""",
        encoding="utf-8",
    )
    workspace.registry_path("claims.yaml").write_text(
        """claims:
- id: CLM-0001
  claim: "The example workspace exercises the project kernel."
  source_ids:
    - SRC-0001
  confidence: "high"
  status: "fixture"
""",
        encoding="utf-8",
    )
    workspace.registry_path("quotes.yaml").write_text(
        """quotes:
- id: QTE-0001
  quote: "Fixture quote"
  source_id: SRC-0001
  locator: "local fixture"
  verified: true
""",
        encoding="utf-8",
    )
    workspace.registry_path("synthesis-map.yaml").write_text(
        """synthesis_map:
- id: SYN-0001
  synthesis: "The kernel supports scaffold, validate, assemble, and pack flows."
  claim_ids:
    - CLM-0001
  status: "fixture"
""",
        encoding="utf-8",
    )
    workspace.registry_path("release-ledger.yaml").write_text(
        """releases:
- id: REL-FIXTURE-0001
  version: "fixture"
  date: "2026-04-26"
  artifacts:
    - "05-output"
  validation_report: "fixture"
""",
        encoding="utf-8",
    )


def _complete_outputs(workspace: Workspace, family: str) -> None:
    output_dir = workspace.output_dir / family
    sections = output_dir / "sections"
    sections.mkdir(parents=True, exist_ok=True)
    (sections / "01-introduction.md").write_text(
        f"# {family.replace('-', ' ').title()}\n\nThis fixture output is assembled from a manifest.\n",
        encoding="utf-8",
    )
    (output_dir / "manifest.md").write_text("# Manifest\n\n- sections/01-introduction.md\n", encoding="utf-8")
    (workspace.root / "03-analysis" / "fixture-analysis.md").write_text("# Analysis\n\nFixture analysis note.\n", encoding="utf-8")
    (workspace.root / "02-research" / "fixture-research.md").write_text("# Research\n\nFixture research note.\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
