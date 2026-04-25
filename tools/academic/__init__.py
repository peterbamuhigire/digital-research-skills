"""Academic-writing utilities — originality, paraphrase, citation, voice.

Public API:
    detect_overlap          — N-gram overlap against a source corpus
    paraphrase_distance     — semantic-vs-surface similarity score
    citation_density        — citations-per-paragraph audit
    reporting_verb_variety  — varies "argues / suggests / posits" across a draft
    hedging_audit           — checks for sufficient modality / qualification
    canonicalize_quote      — formats direct quotes with proper attribution
    seed_from_run           — produces a per-run seed for controlled variation
"""
from .originality import detect_overlap, OverlapReport, NGramHit
from .paraphrase import paraphrase_distance, ParaphraseScore
from .citation_density import citation_density, CitationDensityReport
from .reporting_verbs import reporting_verb_variety, REPORTING_VERBS
from .hedging import hedging_audit, HedgingReport, HEDGING_MARKERS
from .quotes import canonicalize_quote, format_block_quote
from .variation import seed_from_run, RunVariationKnobs

__all__ = [
    "detect_overlap", "OverlapReport", "NGramHit",
    "paraphrase_distance", "ParaphraseScore",
    "citation_density", "CitationDensityReport",
    "reporting_verb_variety", "REPORTING_VERBS",
    "hedging_audit", "HedgingReport", "HEDGING_MARKERS",
    "canonicalize_quote", "format_block_quote",
    "seed_from_run", "RunVariationKnobs",
]
