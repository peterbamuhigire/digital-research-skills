from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.verification.source_verifier import verify_claim, verify_manifest


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "tests" / "fixtures" / "claim-support-review.json"


class SourceVerifierTests(unittest.TestCase):
    def test_claim_support_fixture_keeps_semantic_states_explicit(self) -> None:
        report = verify_manifest(FIXTURE, check_archives=False)
        claims = {result.item_id: result for result in report.results if result.item_type == "claim"}

        self.assertEqual(
            {result.support_state for result in claims.values()},
            {"supported", "unsupported", "synthesis", "inference", "no-source"},
        )
        self.assertEqual(claims["CLM-TEST-SUPPORTED"].status, "warn")
        self.assertEqual(claims["CLM-TEST-UNSUPPORTED"].status, "fail")
        self.assertEqual(claims["CLM-TEST-SYNTHESIS"].status, "warn")
        self.assertEqual(claims["CLM-TEST-INFERENCE"].status, "warn")
        self.assertEqual(claims["CLM-TEST-NO-SOURCE"].status, "fail")
        self.assertFalse(report.release_ready)
        self.assertTrue(
            any("automated semantics are not assessed" in result.evidence for result in claims.values())
        )

    def test_known_source_ids_without_support_review_are_not_passed(self) -> None:
        result = verify_claim(
            {
                "id": "CLM-TEST-MISSING-REVIEW",
                "text": "TEST ONLY: semantic support review is absent.",
                "source_ids": ["SRC-TEST-001"],
            },
            {"SRC-TEST-001": {"id": "SRC-TEST-001", "tier": 4}},
        )

        self.assertEqual(result.status, "warn")
        self.assertEqual(result.confidence, "low")
        self.assertIn("semantic claim support was not assessed", result.evidence)

    def test_non_certifying_states_cannot_be_promoted_by_review_metadata(self) -> None:
        for state in ("unsupported", "no-source", "inference"):
            source_ids = [] if state == "no-source" else ["SRC-TEST-001"]
            manifest = {
                "sources": [{"id": "SRC-TEST-001", "tier": 4}],
                "claims": [
                    {
                        "id": f"CLM-TEST-ONLY-{state.upper()}",
                        "text": f"TEST ONLY: {state} claim with complete review metadata.",
                        "source_ids": source_ids,
                        "support_review": {
                            "state": state,
                            "reviewer": "test-labelled reviewer",
                            "basis": "TEST ONLY: metadata does not certify semantic support.",
                            "reviewed_at": "2026-08-11",
                        },
                    }
                ],
            }
            with self.subTest(state=state), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "manifest.json"
                path.write_text(json.dumps(manifest), encoding="utf-8")
                report = verify_manifest(path, check_archives=False)

            claim = next(result for result in report.results if result.item_type == "claim")
            self.assertFalse(report.release_ready)
            self.assertNotEqual(claim.status, "pass")
            self.assertEqual(claim.confidence, "low")
            self.assertEqual(claim.support_state, state)

    def test_malformed_state_source_combinations_are_rejected(self) -> None:
        cases = (
            ("no-source-with-source-id", "no-source", ["SRC-TEST-001"]),
            ("inference-without-source-id", "inference", []),
            ("supported-without-source-id", "supported", []),
            ("scalar-source-ids", "inference", "SRC-TEST-001"),
            ("non-string-source-id", "inference", [None]),
        )
        for case, state, source_ids in cases:
            with self.subTest(case=case):
                result = verify_claim(
                    {
                        "id": f"CLM-TEST-MALFORMED-{case.upper()}",
                        "text": "TEST ONLY: malformed state/source combination.",
                        "source_ids": source_ids,
                        "support_review": {
                            "state": state,
                            "reviewer": "test-labelled reviewer",
                            "basis": "TEST ONLY: malformed combination must remain blocked.",
                            "reviewed_at": "2026-08-11",
                        },
                    },
                    {"SRC-TEST-001": {"id": "SRC-TEST-001", "tier": 4}},
                )
                self.assertEqual(result.status, "fail")
                self.assertEqual(result.confidence, "low")

    def test_non_list_claim_collection_is_rejected(self) -> None:
        manifest = {
            "sources": [{"id": "SRC-TEST-001", "tier": 4}],
            "claims": {"id": "CLM-TEST-NOT-A-LIST"},
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            report = verify_manifest(path, check_archives=False)

        self.assertFalse(report.release_ready)
        self.assertTrue(any(result.item_type == "manifest" and result.status == "fail" for result in report.results))


if __name__ == "__main__":
    unittest.main()
