from __future__ import annotations

from .base import Finding, GateResult, text_has_substance
from ..workspace import Workspace


class Gate08ProductizationReadiness:
    gate_id = "GATE-08"
    title = "productization readiness"

    def run(self, workspace: Workspace) -> GateResult:
        path = workspace.context_path("monetization.md")
        findings = []
        if not text_has_substance(path):
            findings.append(Finding(self.gate_id, "warning", path, "monetization or reuse intent is not resolved"))
        return GateResult(self.gate_id, self.title, tuple(findings))
