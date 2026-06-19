from __future__ import annotations

from .base import Finding, GateResult, text_has_substance
from ..registry.schemas import schema_for
from ..registry.validation import validate_rows
from ..workspace import Workspace


class Gate08ProductizationReadiness:
    gate_id = "GATE-08"
    title = "productization readiness"

    def run(self, workspace: Workspace) -> GateResult:
        path = workspace.context_path("monetization.md")
        findings = []
        if not text_has_substance(path):
            findings.append(Finding(self.gate_id, "warning", path, "monetization or reuse intent is not resolved"))
        manifest_path = workspace.registry_path("productization-manifest.yaml")
        _, issues = validate_rows(manifest_path, schema_for("productization-manifest.yaml"))
        for issue in issues:
            findings.append(Finding(self.gate_id, "blocker", issue.path, issue.message))
        return GateResult(self.gate_id, self.title, tuple(findings))
