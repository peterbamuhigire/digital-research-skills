from __future__ import annotations

from .base import Finding, GateResult
from ..workspace import Workspace


REASONING_MARKERS = (
    "argument map",
    "governing thesis",
    "load-bearing conclusion",
    "reasoning",
    "logic",
    "claim",
)
EVIDENCE_MARKERS = ("evidence", "source", "data", "citation", "provenance")
ASSUMPTION_MARKERS = ("assumption", "premise", "warrant", "depends on")
COUNTERCASE_MARKERS = (
    "countercase",
    "counter-case",
    "objection",
    "alternative explanation",
    "rival",
    "limitation",
)
IMPLICATION_MARKERS = ("implication", "recommendation", "decision", "next action", "so what")


class Gate04AnalysisTradecraft:
    gate_id = "GATE-04"
    title = "analysis tradecraft"

    def run(self, workspace: Workspace) -> GateResult:
        findings = []
        analysis_files = list(workspace.root.glob("03-analysis/**/*.md"))
        if not analysis_files:
            findings.append(Finding(self.gate_id, "warning", workspace.root / "03-analysis", "no analysis markdown found"))
            return GateResult(self.gate_id, self.title, tuple(findings))

        substantive_files = [path for path in analysis_files if _substantive(path)]
        if not substantive_files:
            findings.append(
                Finding(
                    self.gate_id,
                    "warning",
                    workspace.root / "03-analysis",
                    "analysis files exist but none contain enough substantive text for tradecraft review",
                )
            )
            return GateResult(self.gate_id, self.title, tuple(findings))

        for path in substantive_files:
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
            missing = []
            if not _contains_any(text, REASONING_MARKERS):
                missing.append("reasoning/argument map")
            if not _contains_any(text, EVIDENCE_MARKERS):
                missing.append("evidence trail")
            if not _contains_any(text, ASSUMPTION_MARKERS):
                missing.append("assumptions or warrants")
            if not _contains_any(text, COUNTERCASE_MARKERS):
                missing.append("countercase or limitations")
            if not _contains_any(text, IMPLICATION_MARKERS):
                missing.append("implications or next actions")
            if missing:
                findings.append(
                    Finding(
                        self.gate_id,
                        "warning",
                        path,
                        "analysis does not visibly show: " + ", ".join(missing),
                    )
                )
        return GateResult(self.gate_id, self.title, tuple(findings))


def _substantive(path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore").strip()
    return len(text) >= 400 and "TODO" not in text


def _contains_any(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker in text for marker in markers)
