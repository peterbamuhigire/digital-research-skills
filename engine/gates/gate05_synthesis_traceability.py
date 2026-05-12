from __future__ import annotations

from .base import Finding, GateResult
from ..registry.schemas import schema_for
from ..registry.validation import as_id_list, has_items, registry_ids, validate_rows
from ..workspace import Workspace


class Gate05SynthesisTraceability:
    gate_id = "GATE-05"
    title = "synthesis traceability"

    def run(self, workspace: Workspace) -> GateResult:
        findings = []
        sources_path = workspace.registry_path("sources.yaml")
        claims_path = workspace.registry_path("claims.yaml")
        synthesis_path = workspace.registry_path("synthesis-map.yaml")

        sources, source_issues = validate_rows(sources_path, schema_for("sources.yaml"))
        claims, claim_issues = validate_rows(claims_path, schema_for("claims.yaml"))
        synthesis_rows, synthesis_issues = validate_rows(synthesis_path, schema_for("synthesis-map.yaml"))
        for issue in source_issues + claim_issues + synthesis_issues:
            findings.append(Finding(self.gate_id, "blocker", issue.path, issue.message))

        if not has_items(claims_path, "claims"):
            findings.append(Finding(self.gate_id, "blocker", claims_path, "claim registry has no entries"))
        if not has_items(synthesis_path, "synthesis_map"):
            findings.append(Finding(self.gate_id, "blocker", synthesis_path, "synthesis map has no entries"))

        source_ids = registry_ids(sources)
        claim_ids = registry_ids(claims)
        for claim in claims:
            claim_id = str(claim.get("id", "claim row"))
            for source_id in as_id_list(claim.get("source_ids")):
                if source_id not in source_ids:
                    findings.append(Finding(self.gate_id, "blocker", claims_path, f"{claim_id}: unknown source id `{source_id}`"))
        for item in synthesis_rows:
            synthesis_id = str(item.get("id", "synthesis row"))
            for claim_id in as_id_list(item.get("claim_ids")):
                if claim_id not in claim_ids:
                    findings.append(Finding(self.gate_id, "blocker", synthesis_path, f"{synthesis_id}: unknown claim id `{claim_id}`"))
        return GateResult(self.gate_id, self.title, tuple(findings))
