from __future__ import annotations

from .base import Finding, GateResult
from ..workspace import Workspace


class Gate06OutputReadiness:
    gate_id = "GATE-06"
    title = "output readiness"

    def run(self, workspace: Workspace) -> GateResult:
        manifests = list(workspace.output_dir.glob("**/manifest.md"))
        findings = []
        if not manifests:
            findings.append(Finding(self.gate_id, "blocker", workspace.output_dir, "no output manifest found"))
        return GateResult(self.gate_id, self.title, tuple(findings))
