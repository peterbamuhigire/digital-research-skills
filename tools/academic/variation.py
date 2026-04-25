"""Run-to-run variation knobs.

The user requirement: same prompt → 3 runs → 3 distinct but authentic outputs.
Plagiarism detection between runs is also a real risk if this engine is used
to write similar reports for similar clients.

This module produces a *deterministic seed* per run that other components
read to choose:
- Opening hook style
- Argument-ordering rotation
- Sentence-length distribution preference
- Reporting-verb subset preference
- Section-header phrasing
- Paragraph-architecture pattern

The seed comes from (project-id, run-number, optional-user-salt). Same
seed → same output; different seed → genuinely different output.
"""
from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class RunVariationKnobs:
    seed: int
    opening_hook_style: str
    argument_order: str
    sentence_length_preference: str
    reporting_verb_subset: str
    paragraph_pattern: str
    section_header_style: str


_OPENING_HOOK_STYLES = [
    "anchor_statistic",       # Lead with a quantified finding
    "scene_setting",           # Lead with context / setting
    "puzzle_framing",          # Lead with the question / paradox
    "stake_framing",           # Lead with what's at stake
    "historical_anchor",       # Lead with a historical comparison
    "definitional",            # Lead with a definitional claim
    "contradiction",           # Lead with two opposing positions
]


_ARGUMENT_ORDERS = [
    "general_to_specific",     # Bailey's standard funnel
    "problem_to_solution",     # IMRAD-friendly
    "thesis_then_evidence",    # MLA-friendly
    "comparison_first",        # Comparative-essay-friendly
    "chronological",           # Historical / case-study
    "causal_chain",            # Cause → effect → implication
    "concentric",              # Inner concept outward to context
]


_SENTENCE_LENGTH_PREFERENCES = [
    "varied_with_short_punctuation",   # mix; periodic short emphatic
    "longer_complex_dominant",          # academic-formal, periodic short
    "balanced",                         # average ~22 words
    "shorter_punchier",                 # journalism-leaning
]


_REPORTING_VERB_SUBSETS = [
    "argues_contends_maintains",        # argumentative-leaning
    "suggests_implies_indicates",       # tentative-leaning
    "demonstrates_shows_establishes",   # evaluative-positive
    "questions_problematises_complicates",  # critical
    "neutral_descriptive",              # states/notes/describes
]


_PARAGRAPH_PATTERNS = [
    "claim_evidence_commentary",         # Bailey's standard
    "evidence_first_then_claim",         # Inductive
    "comparison_within_paragraph",        # X but Y
    "concession_then_assertion",          # Although X, nonetheless Y
    "definition_application_implication", # what / how / so what
]


_SECTION_HEADER_STYLES = [
    "noun_phrase",         # "The Tenant Pain Stack"
    "interrogative",       # "Why Do Tenants Lose Deposits?"
    "thesis_assertion",    # "Tenants Lose Deposits Because…"
    "imperative",          # "Consider The Tenant"
    "minimal",             # "Tenants" (single noun)
]


def seed_from_run(
    project_id: str, *,
    run_number: int = 1,
    user_salt: Optional[str] = None,
) -> RunVariationKnobs:
    """Compute deterministic variation knobs for a given (project, run).

    Same project + run + salt → identical knobs.
    Different run number → different knobs guaranteed.
    """
    base = f"{project_id}::{run_number}::{user_salt or ''}"
    digest = hashlib.sha256(base.encode("utf-8")).digest()
    seed = int.from_bytes(digest[:8], byteorder="big")
    rng = random.Random(seed)

    return RunVariationKnobs(
        seed=seed,
        opening_hook_style=rng.choice(_OPENING_HOOK_STYLES),
        argument_order=rng.choice(_ARGUMENT_ORDERS),
        sentence_length_preference=rng.choice(_SENTENCE_LENGTH_PREFERENCES),
        reporting_verb_subset=rng.choice(_REPORTING_VERB_SUBSETS),
        paragraph_pattern=rng.choice(_PARAGRAPH_PATTERNS),
        section_header_style=rng.choice(_SECTION_HEADER_STYLES),
    )
