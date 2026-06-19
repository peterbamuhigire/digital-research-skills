"""Asserts the enriched §0–§9 .docx structure for healthcare-app-clinical-data cohorts.

Per docs/plans/2026-05-04-automated-onboarding-plan.md task A2.1.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import generate_healthcare_app_clinical_data_outputs as gen  # noqa: E402


REQUIRED_HEADINGS = (
    "Executive summary",
    "Standards",
    "Dataset summary",
    "Per-entity reference",
    "Cross-cohort dependencies",
    "Onboarding workflow",
    "Acceptance criteria",
    "Open gaps",
    "Critical reasoning",
    "Change log",
)


@pytest.fixture
def fixture_cohort():
    """Three-row fixture for the conditions cohort.

    Cohort spec is reused from the script; rows are inline so the test is
    independent of corpus state.
    """
    cohort = next(c for c in gen.COHORTS if c.slug == "conditions")
    rows = [
        {
            "icd10_code": "B50.0",
            "icd10_chapter": "I — Infectious",
            "preferred_name_en": "Plasmodium falciparum malaria with cerebral complications",
            "snomed_ct_concept_id": "186741000",
            "ranking_rationale": "GBD top-10 Uganda",
            "level_of_care_min": "HC III",
            "cadre_min": "Clinical officer",
        },
        {
            "icd10_code": "A15.0",
            "icd10_chapter": "I — Infectious",
            "preferred_name_en": "Tuberculosis of lung, confirmed",
            "snomed_ct_concept_id": "154283005",
            "ranking_rationale": "NTLP priority",
            "level_of_care_min": "HC IV",
            "cadre_min": "Clinical officer",
        },
        {
            "icd10_code": "E11.9",
            "icd10_chapter": "IV — Endocrine",
            "preferred_name_en": "Type 2 diabetes mellitus without complications",
            "snomed_ct_concept_id": "44054006",
            "ranking_rationale": "PEN protocol primary",
            "level_of_care_min": "HC III",
            "cadre_min": "Medical officer",
        },
    ]
    return cohort, rows


def _heading_texts(doc) -> list[str]:
    return [p.text for p in doc.paragraphs if p.style.name.startswith("Heading")]


def test_enriched_report_has_required_sections(fixture_cohort):
    cohort, rows = fixture_cohort
    doc = gen.build_enriched_docx(cohort, rows)
    headings = _heading_texts(doc)
    missing = [h for h in REQUIRED_HEADINGS if not any(h in actual for actual in headings)]
    assert not missing, f"Missing headings: {missing}\nActual: {headings}"


def test_enriched_report_section_order(fixture_cohort):
    """§0 must precede §1, §1 must precede §2, etc."""
    cohort, rows = fixture_cohort
    doc = gen.build_enriched_docx(cohort, rows)
    headings = _heading_texts(doc)

    def position(needle: str) -> int:
        for i, h in enumerate(headings):
            if needle in h:
                return i
        return -1

    expected_order = [
        "Executive summary",
        "Standards",
        "Dataset summary",
        "Per-entity reference",
        "Cross-cohort dependencies",
        "Onboarding workflow",
        "Acceptance criteria",
        "Open gaps",
        "Critical reasoning",
        "Change log",
    ]
    positions = [position(h) for h in expected_order]
    assert all(p >= 0 for p in positions), f"Some headings missing: {list(zip(expected_order, positions))}"
    assert positions == sorted(positions), f"Out of order: {list(zip(expected_order, positions))}"


def test_enriched_report_carries_cohort_title(fixture_cohort):
    cohort, rows = fixture_cohort
    doc = gen.build_enriched_docx(cohort, rows)
    all_text = "\n".join(p.text for p in doc.paragraphs)
    assert cohort.title in all_text
