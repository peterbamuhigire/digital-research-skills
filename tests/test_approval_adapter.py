import json
import unittest
from pathlib import Path


class ApprovalAdapterTests(unittest.TestCase):
    def test_claim_release_requires_human_evidence_gate(self):
        payload = json.loads((Path(__file__).parents[1] / "docs" / "approval-adapter.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["engine"], "digital-research")
        actions = {item["action_type"]: item for item in payload["actions"]}
        for action_type in ("research.claim.publish", "research.sensitive-profile.release", "research.high-impact.recommendation.release"):
            action = actions[action_type]
            self.assertEqual(action["class"], "L3")
            self.assertTrue(action["preview_required"] and action["verification"])


if __name__ == "__main__":
    unittest.main()
