from __future__ import annotations

from .base import Finding, GateResult
from ..registry.schemas import schema_for
from ..registry.validation import has_items, validate_rows
from ..workspace import Workspace


MANIFEST_REQUIRED_FIELDS = (
    "output_family:",
    "report_shape:",
    "audience:",
    "citation_regime:",
    "verification_status:",
)


class Gate06OutputReadiness:
    gate_id = "GATE-06"
    title = "output readiness"

    def run(self, workspace: Workspace) -> GateResult:
        manifests = list(workspace.output_dir.glob("**/manifest.md"))
        findings = []
        if not manifests:
            findings.append(Finding(self.gate_id, "blocker", workspace.output_dir, "no output manifest found"))
        for manifest in manifests:
            text = manifest.read_text(encoding="utf-8", errors="ignore")
            missing = [field.rstrip(":") for field in MANIFEST_REQUIRED_FIELDS if field not in text]
            if missing:
                findings.append(Finding(self.gate_id, "warning", manifest, "output manifest missing metadata: " + ", ".join(missing)))

        report_shapes_path = workspace.registry_path("report-shapes.yaml")
        _, issues = validate_rows(report_shapes_path, schema_for("report-shapes.yaml"))
        for issue in issues:
            findings.append(Finding(self.gate_id, "blocker", issue.path, issue.message))
        if not has_items(report_shapes_path, "report_shapes"):
            findings.append(Finding(self.gate_id, "warning", report_shapes_path, "report shape registry has no entries"))
        return GateResult(self.gate_id, self.title, tuple(findings))
