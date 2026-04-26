from __future__ import annotations

from .base import Finding, GateResult, registry_has_items
from ..workspace import Workspace


class Gate05SynthesisTraceability:
    gate_id = "GATE-05"
    title = "synthesis traceability"

    def run(self, workspace: Workspace) -> GateResult:
        findings = []
        if not registry_has_items(workspace.registry_path("claims.yaml")):
            findings.append(Finding(self.gate_id, "blocker", workspace.registry_path("claims.yaml"), "claim registry has no entries"))
        if not registry_has_items(workspace.registry_path("synthesis-map.yaml")):
            findings.append(Finding(self.gate_id, "blocker", workspace.registry_path("synthesis-map.yaml"), "synthesis map has no entries"))
        return GateResult(self.gate_id, self.title, tuple(findings))
