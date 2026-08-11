from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ROUTER = ROOT / "skills" / "research-orchestration" / "references" / "research-type-router.md"
ACTIVE_SKILL_NAMES = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}

CANONICAL_TARGETS = {
    "research-techniques",
    "quantitative-modelling",
    "research-design",
    "osint-investigation",
    "due-diligence",
    "calibration-and-forecasting",
    "online-legal-research",
    "academic-writing",
    "academic-reporting-standards",
    "business-writing",
    "research-output-formats",
}

FORMER_DEAD_ROUTE_NAMES = {
    "pain-point-taxonomy",
    "academic-source-mining",
    "cross-cohort-synthesis",
    "social-source-extraction",
    "due-diligence-framework",
    "osint-methodology",
    "historical-research-methods",
    "trend-analysis",
    "regulatory-landscape-mapping",
    "academic-writing-conventions",
    "academic-citation-styles",
    "writing-quality",
    "content-writing",
    "research-report-builder",
    "market",
}


class ResearchTypeRouterTests(unittest.TestCase):
    def test_all_repaired_research_type_rows_have_active_skill_routes(self) -> None:
        text = ROUTER.read_text(encoding="utf-8")
        route_rows = [line for line in text.splitlines() if line.startswith("| **")]

        self.assertEqual(len(route_rows), 19)
        for row in route_rows:
            cells = [cell.strip() for cell in row.split("|")[1:-1]]
            self.assertGreaterEqual(len(cells), 5, row)
            route_tokens = re.findall(r"`([^`]+)`", cells[3])
            skill_tokens = [token for token in route_tokens if "/" not in token]
            self.assertTrue(skill_tokens, row)
            for skill in skill_tokens:
                self.assertIn(skill, ACTIVE_SKILL_NAMES, row)

    def test_canonical_routes_and_references_are_filesystem_backed(self) -> None:
        text = ROUTER.read_text(encoding="utf-8")

        for name in CANONICAL_TARGETS:
            self.assertIn(f"`{name}`", text)
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file(), name)

        for reference in re.findall(r"`(references/[^)`]+\.md)`", text):
            self.assertTrue(
                any((ROOT / "skills" / name / reference).is_file() for name in CANONICAL_TARGETS),
                reference,
            )

        self.assertIn("methodology_references", text)

    def test_former_dead_names_are_not_active_route_targets(self) -> None:
        text = ROUTER.read_text(encoding="utf-8")

        for name in FORMER_DEAD_ROUTE_NAMES:
            self.assertNotIn(f"`{name}`", text, name)

    def test_tools_readme_does_not_advertise_absent_modules(self) -> None:
        text = (ROOT / "tools" / "README.md").read_text(encoding="utf-8")

        for name in (
            "auth.py",
            "storage.py",
            "dedup.py",
            "ethics.py",
            "monitoring.py",
            "reverse_image.py",
            "shadow_time.py",
            "whois_cluster.py",
        ):
            self.assertNotIn(name, text, name)
        self.assertIn("source_verifier.py", text)


if __name__ == "__main__":
    unittest.main()
