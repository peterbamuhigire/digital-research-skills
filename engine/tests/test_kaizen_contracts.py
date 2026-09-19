from __future__ import annotations

import json
from datetime import date
from pathlib import Path
import unittest

from tools.verification.kaizen_contracts import (
    NOT_ASSESSED,
    source_hash_is_stable,
    validate_ai_search_claim,
    validate_index_layer,
    validate_objection_response,
)


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "tests" / "fixtures" / "kaizen-contracts.json"


class KaizenContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.known_source_ids = cls.data["known_source_ids"]

    def test_index_contract_accepts_context_locator_and_hash(self) -> None:
        findings = validate_index_layer(self.data["index_records"]["valid"], known_source_ids=self.known_source_ids)
        self.assertEqual(findings, [])

    def test_missing_context_is_not_assessed(self) -> None:
        findings = validate_index_layer(self.data["index_records"]["missing_context"], known_source_ids=self.known_source_ids)
        self.assertIn("NOT_ASSESSED", {finding.status for finding in findings})
        self.assertTrue(any(finding.code == "index-missing-context" for finding in findings))

    def test_unsupported_locator_is_not_assessed(self) -> None:
        findings = validate_index_layer(self.data["index_records"]["unsupported_locator"], known_source_ids=self.known_source_ids)
        self.assertTrue(any(finding.code == "index-unsupported-locator" and finding.status == NOT_ASSESSED for finding in findings))

    def test_source_hash_remains_stable_after_reindex(self) -> None:
        before = self.data["index_records"]["valid"]
        after = json.loads(json.dumps(before))
        after["index_version"] = "idx-2026-09-19.2"
        after["interpretations"][0]["text"] = "TEST ONLY: re-indexed representation."
        self.assertTrue(source_hash_is_stable(before, after))
        after["source"]["source_hash"] = "b" * 64
        self.assertFalse(source_hash_is_stable(before, after))

    def test_objection_gate_requires_strongest_objection(self) -> None:
        findings = validate_objection_response(self.data["objection_records"]["missing_objection"], known_source_ids=self.known_source_ids)
        self.assertTrue(any(finding.code == "objection-missing" and finding.status == "blocker" for finding in findings))

    def test_unresolved_objection_lowers_confidence_without_erasing_it(self) -> None:
        findings = validate_objection_response(self.data["objection_records"]["unresolved"], known_source_ids=self.known_source_ids)
        self.assertTrue(any(finding.code == "objection-unresolved" and finding.confidence == "low" for finding in findings))

    def test_unknown_objection_source_is_a_blocker(self) -> None:
        findings = validate_objection_response(self.data["objection_records"]["fabricated_source"], known_source_ids=self.known_source_ids)
        self.assertTrue(any(finding.code == "objection-fabricated-source" and finding.status == "blocker" for finding in findings))

    def test_ai_search_claim_keeps_observation_types_and_currentness(self) -> None:
        findings = validate_ai_search_claim(self.data["ai_search_claims"]["valid"], as_of=date(2026, 9, 19))
        self.assertEqual(findings, [])

    def test_weak_ai_search_evidence_is_not_assessed(self) -> None:
        findings = validate_ai_search_claim(self.data["ai_search_claims"]["weak_evidence"], as_of=date(2026, 9, 19))
        self.assertTrue(any(finding.code == "ai-weak-evidence" and finding.status == NOT_ASSESSED for finding in findings))

    def test_stale_ai_search_currentness_is_not_assessed(self) -> None:
        findings = validate_ai_search_claim(self.data["ai_search_claims"]["stale"], as_of=date(2026, 9, 19))
        self.assertTrue(any(finding.code == "ai-currentness-stale" and finding.status == NOT_ASSESSED for finding in findings))

    def test_ai_search_guarantee_fails_closed(self) -> None:
        findings = validate_ai_search_claim(self.data["ai_search_claims"]["guarantee"], as_of=date(2026, 9, 19))
        self.assertTrue(any(finding.code == "ai-guarantee-blocked" and finding.status == "blocker" for finding in findings))


if __name__ == "__main__":
    unittest.main()
