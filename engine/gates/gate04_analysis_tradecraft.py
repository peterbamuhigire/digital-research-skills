from __future__ import annotations

from .base import Finding, GateResult
from ..workspace import Workspace


class Gate04AnalysisTradecraft:
    gate_id = "GATE-04"
    title = "analysis tradecraft"

    def run(self, workspace: Workspace) -> GateResult:
        findings = []
        analysis_files = list(workspace.root.glob("03-analysis/**/*.md"))
        if not analysis_files:
            findings.append(Finding(self.gate_id, "warning", workspace.root / "03-analysis", "no analysis markdown found"))
        return GateResult(self.gate_id, self.title, tuple(findings))
