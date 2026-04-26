from __future__ import annotations

from .base import Finding, GateResult, registry_has_items
from ..workspace import Workspace


class Gate09ReleasePack:
    gate_id = "GATE-09"
    title = "release pack"

    def run(self, workspace: Workspace) -> GateResult:
        findings = []
        if not registry_has_items(workspace.registry_path("release-ledger.yaml")):
            findings.append(Finding(self.gate_id, "warning", workspace.registry_path("release-ledger.yaml"), "release ledger has no entries"))
        if not workspace.export_dir.exists():
            findings.append(Finding(self.gate_id, "blocker", workspace.export_dir, "export directory is missing"))
        return GateResult(self.gate_id, self.title, tuple(findings))
