from __future__ import annotations

from .base import Finding, GateResult, text_has_substance
from ..workspace import Workspace


class Gate07AudienceFit:
    gate_id = "GATE-07"
    title = "audience fit"

    def run(self, workspace: Workspace) -> GateResult:
        path = workspace.context_path("audience-output-matrix.md")
        findings = []
        if not text_has_substance(path):
            findings.append(Finding(self.gate_id, "warning", path, "audience-output matrix is incomplete"))
        return GateResult(self.gate_id, self.title, tuple(findings))
