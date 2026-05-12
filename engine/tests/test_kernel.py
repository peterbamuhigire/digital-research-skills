from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from engine.gates.gate04_analysis_tradecraft import Gate04AnalysisTradecraft
from engine.gates.gate03_evidence_integrity import Gate03EvidenceIntegrity
from engine.gates.gate05_synthesis_traceability import Gate05SynthesisTraceability
from engine.gates.gate06_output_readiness import Gate06OutputReadiness
from engine.gates import run_all_gates
from engine.pack import build_pack
from engine.registry import sync_workspace
from engine.scaffold import ScaffoldOptions, create_project
from engine.workspace import Workspace


class KernelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="dre-kernel-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def test_scaffold_loads_as_workspace(self) -> None:
        workspace = create_project(ScaffoldOptions("Unit Project", "market", "internal", "standard", self.tmp))
        loaded = Workspace.load(workspace.root)
        self.assertEqual(loaded.project_id, "unit-project")

    def test_sync_repairs_missing_registry(self) -> None:
        workspace = create_project(ScaffoldOptions("Sync Project", "market", "internal", "standard", self.tmp))
        workspace.registry_path("claims.yaml").unlink()
        result = sync_workspace(workspace)
        self.assertEqual(len(result.created), 1)
        self.assertTrue(workspace.registry_path("claims.yaml").exists())

    def test_fresh_project_has_validation_blockers(self) -> None:
        workspace = create_project(ScaffoldOptions("Gate Project", "market", "internal", "standard", self.tmp))
        results = run_all_gates(workspace)
        blockers = [finding for result in results for finding in result.findings if finding.severity == "blocker"]
        self.assertGreater(len(blockers), 0)

    def test_analysis_tradecraft_warns_when_reasoning_is_not_visible(self) -> None:
        workspace = create_project(ScaffoldOptions("Analysis Project", "market", "internal", "standard", self.tmp))
        analysis = workspace.root / "03-analysis" / "market.md"
        analysis.write_text(
            "# Market Notes\n\n"
            + "The market appears attractive because demand is growing and competitors are weak. " * 12,
            encoding="utf-8",
        )

        result = Gate04AnalysisTradecraft().run(workspace)

        self.assertTrue(any("does not visibly show" in finding.message for finding in result.findings))

    def test_analysis_tradecraft_accepts_visible_reasoning_stack(self) -> None:
        workspace = create_project(ScaffoldOptions("Reasoned Analysis Project", "market", "internal", "standard", self.tmp))
        analysis = workspace.root / "03-analysis" / "market.md"
        analysis.write_text(
            "# Market Analysis\n\n"
            "## Argument Map\n"
            "Claim: the opportunity is commercially plausible for the defined segment.\n"
            "Evidence: three cited source groups, current market data, and customer interviews support the claim.\n"
            "Assumption: the channel partner remains available and the price point is accepted.\n"
            "Warrant: the evidence links to the conclusion because willingness to pay, access, and margin are all present.\n"
            "Countercase: an alternative explanation is that short-term demand reflects a subsidy rather than durable need.\n"
            "Limitation: current evidence is stronger on demand than on repeat purchase behaviour.\n"
            "Implication: next action is to validate repeat purchase and revise the revenue model before release.\n",
            encoding="utf-8",
        )

        result = Gate04AnalysisTradecraft().run(workspace)

        self.assertFalse(result.findings)

    def test_evidence_integrity_blocks_missing_required_source_fields(self) -> None:
        workspace = create_project(ScaffoldOptions("Source Schema Project", "market", "internal", "standard", self.tmp))
        workspace.registry_path("sources.yaml").write_text(
            "sources:\n"
            "- id: SRC-0001\n"
            "  title: Example source\n"
            "  tier: \"1\"\n"
            "  accessed: \"2026-05-12\"\n"
            "  verification: checked\n"
            "  confidence: high\n",
            encoding="utf-8",
        )

        result = Gate03EvidenceIntegrity().run(workspace)

        self.assertTrue(any("missing required field `ref`" in finding.message for finding in result.findings))

    def test_synthesis_traceability_blocks_unknown_claim_source_links(self) -> None:
        workspace = create_project(ScaffoldOptions("Trace Project", "market", "internal", "standard", self.tmp))
        workspace.registry_path("sources.yaml").write_text(
            "sources:\n"
            "- id: SRC-0001\n"
            "  title: Example source\n"
            "  ref: https://example.com/source\n"
            "  tier: \"1\"\n"
            "  accessed: \"2026-05-12\"\n"
            "  verification: checked\n"
            "  confidence: high\n",
            encoding="utf-8",
        )
        workspace.registry_path("claims.yaml").write_text(
            "claims:\n"
            "- id: CLM-0001\n"
            "  claim: Example claim\n"
            "  source_ids:\n"
            "    - SRC-9999\n"
            "  confidence: medium\n"
            "  status: supported\n",
            encoding="utf-8",
        )
        workspace.registry_path("synthesis-map.yaml").write_text(
            "synthesis_map:\n"
            "- id: SYN-0001\n"
            "  synthesis: Example synthesis\n"
            "  claim_ids:\n"
            "    - CLM-0001\n"
            "  status: draft\n",
            encoding="utf-8",
        )

        result = Gate05SynthesisTraceability().run(workspace)

        self.assertTrue(any("unknown source id `SRC-9999`" in finding.message for finding in result.findings))

    def test_output_readiness_warns_on_missing_manifest_metadata(self) -> None:
        workspace = create_project(ScaffoldOptions("Manifest Project", "market", "internal", "standard", self.tmp))
        manifest = workspace.output_dir / "executive-report" / "manifest.md"
        manifest.write_text("# Manifest\n\n- sections/01-introduction.md\n", encoding="utf-8")

        result = Gate06OutputReadiness().run(workspace)

        self.assertTrue(any("output manifest missing metadata" in finding.message for finding in result.findings))

    def test_estimative_analysis_warns_without_tradecraft_record(self) -> None:
        workspace = create_project(ScaffoldOptions("Estimative Project", "market", "internal", "standard", self.tmp))
        analysis = workspace.root / "03-analysis" / "warning.md"
        analysis.write_text(
            "# Warning Analysis\n\n"
            "## Argument Map\n"
            "Claim: the risk is likely to increase in the next quarter.\n"
            "Evidence: current source evidence and data support the claim.\n"
            "Assumption: the policy environment remains unchanged.\n"
            "Countercase: an alternative explanation is temporary reporting noise.\n"
            "Implication: next action is additional monitoring.\n"
            + "This analysis is intentionally long enough to trigger the substantive tradecraft gate. " * 6,
            encoding="utf-8",
        )

        result = Gate04AnalysisTradecraft().run(workspace)

        self.assertTrue(any("tradecraft registry has no records" in finding.message for finding in result.findings))

    def test_pack_writes_zip(self) -> None:
        workspace = create_project(ScaffoldOptions("Pack Project", "market", "internal", "standard", self.tmp))
        result = build_pack(workspace, "export/test.zip")
        self.assertTrue(result.path.exists())
        self.assertGreater(result.files, 0)


if __name__ == "__main__":
    unittest.main()
