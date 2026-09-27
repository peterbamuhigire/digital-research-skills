import json
from pathlib import Path
import unittest

from tools.evaluation.replay_gate import evaluate


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals/seek-research/replay-gate/synthetic_historical_regression.json"


def load_record():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class ReplayGateTests(unittest.TestCase):
    def test_historical_regression_rejects_despite_emerging_improvement(self):
        result = evaluate(load_record())
        self.assertEqual("rejected", result["status"])
        self.assertTrue(any("historical replay regression" in reason for reason in result["reasons"]))
        self.assertFalse(result["promotion_performed"])
        self.assertFalse(result["canonical_guidance_written"])

    def test_synthetic_no_regression_still_cannot_be_promoted(self):
        record = load_record()
        record["replay"]["regressions"] = 0
        result = evaluate(record)
        self.assertEqual("not_assessed", result["status"])
        self.assertTrue(any("synthetic" in reason for reason in result["reasons"]))

    def test_changed_routing_description_rejects_guidance_only_candidate(self):
        record = load_record()
        record["controls"]["routing_description_unchanged"] = False
        result = evaluate(record)
        self.assertEqual("rejected", result["status"])
        self.assertTrue(any("routing description changed" in reason for reason in result["reasons"]))

    def test_mixed_cause_cannot_enter_revision_gate(self):
        record = load_record()
        record["candidate"]["primary_cause"] = "mixed"
        record["replay"]["regressions"] = 0
        result = evaluate(record)
        self.assertEqual("not_assessed", result["status"])
        self.assertTrue(any("cause is unresolved" in reason for reason in result["reasons"]))

    def test_passing_evidence_only_yields_human_review_handoff(self):
        record = load_record()
        record["synthetic"] = False
        record["candidate"]["synthetic"] = False
        record["replay"]["regressions"] = 0
        record["controls"].update({"reviewed_labels_verified": True, "independent_review": True, "semantic_review_complete": True, "uncertainty_reported": True, "evaluation_contract_unchanged": True, "authorized_maintainer_decision": True})
        record["ambiguous"] = {"cases": 1, "critical_false_ready": 0, "noninferiority_pass": True}
        result = evaluate(record)
        self.assertEqual("eligible_for_authorized_review", result["status"])
        self.assertFalse(result["promotion_performed"])

    def test_malformed_count_rejects_instead_of_crashing(self):
        record = load_record()
        record["replay"]["regressions"] = "one"
        result = evaluate(record)
        self.assertEqual("rejected", result["status"])
        self.assertTrue(any("non-negative integer" in reason for reason in result["reasons"]))


if __name__ == "__main__":
    unittest.main()
