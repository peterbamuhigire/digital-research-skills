from __future__ import annotations

from .base import Finding, GateResult, text_has_substance
from ..workspace import Workspace


class Gate01InitContext:
    gate_id = "GATE-01"
    title = "init context"

    required = (
        "brief.md",
        "methodology.md",
        "project-profile.md",
        "research-roadmap.md",
        "audience.md",
        "output-plan.md",
        "scope.md",
        "success-criteria.md",
    )

    def run(self, workspace: Workspace) -> GateResult:
        findings = []
        for name in self.required:
            path = workspace.context_path(name)
            if not text_has_substance(path):
                findings.append(Finding(self.gate_id, "blocker", path, "context file is missing, blank, or still contains TODO"))
        return GateResult(self.gate_id, self.title, tuple(findings))
