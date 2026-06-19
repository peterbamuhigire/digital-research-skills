from __future__ import annotations

from .base import Finding, GateResult
from ..registry.schemas import SCHEMAS
from ..registry.validation import has_items, validate_rows
from ..workspace import Workspace


class Gate03EvidenceIntegrity:
    gate_id = "GATE-03"
    title = "evidence integrity"

    def run(self, workspace: Workspace) -> GateResult:
        findings = []
        for schema in SCHEMAS:
            path = workspace.registry_path(schema.filename)
            _, issues = validate_rows(path, schema)
            for issue in issues:
                findings.append(Finding(self.gate_id, "blocker", issue.path, issue.message))
        if not has_items(workspace.registry_path("sources.yaml"), "sources"):
            findings.append(Finding(self.gate_id, "blocker", workspace.registry_path("sources.yaml"), "source registry has no entries"))
        return GateResult(self.gate_id, self.title, tuple(findings))
