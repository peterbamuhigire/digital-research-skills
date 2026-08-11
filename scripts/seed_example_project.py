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
    registry_payloads = {
        "sources.yaml": """sources:
- id: SRC-0001
  title: "TEST ONLY: fixture source"
  ref: "TEST ONLY: local fixture"
  tier: "4"
  accessed: "2026-04-26"
  verification: "TEST ONLY: local-test-fixture"
  confidence: "low"
""",
        "claims.yaml": """claims:
- id: CLM-0001
  claim: "TEST ONLY: the example workspace exercises the project kernel."
  source_ids:
    - SRC-0001
  confidence: "low"
  status: "supported"
""",
        "quotes.yaml": """quotes:
- id: QTE-0001
  quote: "TEST ONLY: fixture quote"
  source_id: SRC-0001
  locator: "TEST ONLY: local fixture"
  verified: true
""",
        "synthesis-map.yaml": """synthesis_map:
- id: SYN-0001
  synthesis: "TEST ONLY: the kernel supports scaffold, validate, assemble, and pack flows."
  claim_ids:
    - CLM-0001
  status: "verified"
""",
        "tradecraft.yaml": """tradecraft_records:
- id: TRD-FIXTURE-0001
  judgment: "TEST ONLY: fixture judgment; not a research conclusion."
  hypothesis_set:
    - "TEST ONLY: the workspace preserves its registry contract."
  evidence:
    - "SRC-0001"
  biases_considered:
    - "TEST ONLY: confirmation-bias check."
  confidence_judgment: low
  confidence_source: low
  indicators:
    - "TEST ONLY: registry row is present."
  status: fixture
""",
        "report-shapes.yaml": """report_shapes:
- id: RSH-FIXTURE-0001
  output_family: "TEST ONLY: fixture-report"
  shape: "TEST ONLY: fixture-manifest"
  audience: "TEST ONLY: repository maintainer"
  action: "TEST ONLY: verify registry-backed output wiring"
  citation_regime: "TEST ONLY: local fixture only"
  verification_status: "TEST ONLY: not assessed for production output"
  status: fixture
""",
        "productization-manifest.yaml": """productization_assets:
- id: PDM-FIXTURE-0001
  asset: "TEST ONLY: registry-wiring record"
  audience: "TEST ONLY: repository maintainer"
  reuse_status: "TEST ONLY: fixture-only"
  provenance: "TEST ONLY: repository fixture"
  sensitivity: "TEST ONLY: none"
  commercial_claim_bounds: "TEST ONLY: no commercial claim"
  status: fixture
""",
        "calibration-log.yaml": """forecasts:
- id: CAL-FIXTURE-0001
  question: "TEST ONLY: does the workspace preserve its fixture registry?"
  horizon: "TEST ONLY: one validation run"
  probability: 0.5
  resolution_source: "TEST ONLY: no external resolution source"
  source_confidence: low
  status: open
""",
        "osint-tool-index.yaml": """osint_tools:
- id: OSINT-FIXTURE-0001
  name: "TEST ONLY: OSINT tool placeholder"
  url: "test-fixture://osint-tool"
  category: "TEST ONLY: fixture"
  geography: "TEST ONLY: fixture"
  source_ids:
    - SRC-0001
  access_model: unverified
  legal_notes: "TEST ONLY: do not use for an investigation."
  verification: "TEST ONLY: unverified"
  confidence: low
  status: candidate
  last_checked: "2026-04-26"
""",
        "release-ledger.yaml": """releases:
- id: REL-FIXTURE-0001
  version: "fixture"
  date: "2026-04-26"
  artifacts:
    - "05-output"
  validation_report: "fixture"
""",
    }
    for name, content in registry_payloads.items():
        workspace.registry_path(name).write_text(content, encoding="utf-8")


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
