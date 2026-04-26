from __future__ import annotations

from .base import Finding, GateResult, registry_has_items
from ..workspace import Workspace


class Gate02ResearchCoverage:
    gate_id = "GATE-02"
    title = "research coverage"

    def run(self, workspace: Workspace) -> GateResult:
        findings = []
        if not registry_has_items(workspace.registry_path("sources.yaml")):
            findings.append(Finding(self.gate_id, "warning", workspace.registry_path("sources.yaml"), "no source entries found"))
        if not any(workspace.root.glob("02-research/**/*")) and not workspace.legacy_cohort_dirs():
            findings.append(Finding(self.gate_id, "warning", workspace.root / "02-research", "no research files found"))
        return GateResult(self.gate_id, self.title, tuple(findings))
