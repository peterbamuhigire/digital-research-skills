"""Base classes and runner for validation gates."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from ..workspace import Workspace


Severity = str


@dataclass(frozen=True)
class Finding:
    gate_id: str
    severity: Severity
    path: Path
    message: str


@dataclass(frozen=True)
class GateResult:
    gate_id: str
    title: str
    findings: tuple[Finding, ...]

    @property
    def passed(self) -> bool:
        return not any(f.severity == "blocker" for f in self.findings)


class Gate(Protocol):
    gate_id: str
    title: str

    def run(self, workspace: Workspace) -> GateResult:
        ...


def text_has_substance(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore").strip()
    return bool(text) and "TODO" not in text


def registry_has_items(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    return "\n-" in text


def root_key_present(path: Path, root_key: str) -> bool:
    if not path.exists():
        return False
    return any(line.startswith(f"{root_key}:") for line in path.read_text(encoding="utf-8", errors="ignore").splitlines())


def run_all_gates(workspace: Workspace) -> tuple[GateResult, ...]:
    from .gate01_init_context import Gate01InitContext
    from .gate02_research_coverage import Gate02ResearchCoverage
    from .gate03_evidence_integrity import Gate03EvidenceIntegrity
    from .gate04_analysis_tradecraft import Gate04AnalysisTradecraft
    from .gate05_synthesis_traceability import Gate05SynthesisTraceability
    from .gate06_output_readiness import Gate06OutputReadiness
    from .gate07_audience_fit import Gate07AudienceFit
    from .gate08_productization_readiness import Gate08ProductizationReadiness
    from .gate09_release_pack import Gate09ReleasePack

    gates: tuple[Gate, ...] = (
        Gate01InitContext(),
        Gate02ResearchCoverage(),
        Gate03EvidenceIntegrity(),
        Gate04AnalysisTradecraft(),
        Gate05SynthesisTraceability(),
        Gate06OutputReadiness(),
        Gate07AudienceFit(),
        Gate08ProductizationReadiness(),
        Gate09ReleasePack(),
    )
    return tuple(gate.run(workspace) for gate in gates)
