import json
from pathlib import Path
import unittest

from tools.evaluation.research_evaluator import evaluate


ROOT = Path(__file__).resolve().parents[1]
BANK = json.loads((ROOT / "skills/ai-evaluation-and-data-flywheel/references/criterion-bank.json").read_text(encoding="utf-8"))
FIXTURES = ROOT / "evals/seek-research/fixtures"


def load_case(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class ResearchEvaluatorContractTests(unittest.TestCase):
    def test_synthetic_packet_preserves_cluster_gap_and_contradiction(self):
        result = evaluate(load_case("synthetic_packet_case.json"), BANK, ROOT)
        self.assertEqual(9, result["source_origin_clusters"][0]["count"])
        self.assertEqual(["target_period_evidence"], result["subquestion_gaps"])
        self.assertEqual(["SYN-X1"], result["unresolved_contradictions"])
        self.assertEqual("blocked", result["status"])
        self.assertFalse(result["certifies_truth"])

    def test_currentness_guard_blocks_when_route_misses_risk_criterion(self):
        result = evaluate(load_case("synthetic_route_miss_case.json"), BANK, ROOT, "dynamic")
        self.assertNotIn("risk_compliance", result["selected_criteria"])
        self.assertEqual(["risk_compliance"], result["routing_misses"])
        self.assertTrue(any("currentness_when_required: failed" in x for x in result["blockers"]))
        self.assertEqual("blocked", result["status"])

    def test_missing_guard_cannot_produce_ready(self):
        case = load_case("synthetic_route_miss_case.json")
        case["mandatory_guards"].pop("currentness_when_required")
        result = evaluate(case, BANK, ROOT)
        self.assertNotEqual("ready", result["status"])

    def test_unknown_source_and_missing_locator_are_reported(self):
        case = load_case("synthetic_route_miss_case.json")
        case["claims"][0]["source_ids"] = ["unknown"]
        case["claims"][0]["locator"] = None
        result = evaluate(case, BANK, ROOT)
        self.assertTrue(any("unknown source" in x for x in result["structural_errors"]))
        self.assertTrue(any("missing locator" in x for x in result["structural_errors"]))
        self.assertNotEqual("ready", result["status"])

    def test_ready_result_is_only_structural_and_non_certifying(self):
        case = load_case("synthetic_route_miss_case.json")
        case["currentness_required"] = False
        case["mandatory_guards"]["currentness_when_required"] = "not_applicable"
        case["diagnostic_expected_criteria"] = []
        result = evaluate(case, BANK, ROOT)
        self.assertEqual("ready", result["status"])
        self.assertFalse(result["certifies_truth"])


if __name__ == "__main__":
    unittest.main()
