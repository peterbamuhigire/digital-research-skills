from __future__ import annotations

from .base import Finding, GateResult, registry_has_items, root_key_present
from ..registry.schemas import SCHEMAS
from ..workspace import Workspace


class Gate03EvidenceIntegrity:
    gate_id = "GATE-03"
    title = "evidence integrity"

    def run(self, workspace: Workspace) -> GateResult:
        findings = []
        for schema in SCHEMAS:
            path = workspace.registry_path(schema.filename)
            if not root_key_present(path, schema.root_key):
                findings.append(Finding(self.gate_id, "blocker", path, f"registry root key missing: {schema.root_key}"))
        if not registry_has_items(workspace.registry_path("sources.yaml")):
            findings.append(Finding(self.gate_id, "blocker", workspace.registry_path("sources.yaml"), "source registry has no entries"))
        return GateResult(self.gate_id, self.title, tuple(findings))
