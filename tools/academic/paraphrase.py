"""Paraphrase quality scorer — true paraphrase vs synonym-swap.

A "synonym swap" paraphrase keeps the same sentence structure and only
changes individual words. Plagiarism detectors that use semantic similarity
(BERT-based) flag this. True paraphrase reorganises the structure.

This tool scores a paraphrase candidate against the original on three axes:
1. Surface similarity (n-gram overlap) — should be LOW
2. Lexical overlap (word-set Jaccard) — should be MODERATE
3. Semantic similarity (sentence-level) — should be HIGH

A good paraphrase: low surface, moderate lexical, high semantic.
A bad paraphrase: high surface, high lexical, high semantic (synonym swap).
"""
from __future__ import annotations

import re
from dataclasses import dataclass


_TOKEN = re.compile(r"\b[\w'-]+\b")


@dataclass(slots=True)
class ParaphraseScore:
    surface_similarity: float       # 0-1; lower is better for true paraphrase
    lexical_overlap: float          # 0-1; moderate is good
    semantic_similarity: float | None  # 0-1; higher is better; None if model unavailable
    verdict: str                    # "true_paraphrase" | "synonym_swap" | "too_distant" | "verbatim"
    rationale: str


def paraphrase_distance(
    original: str, paraphrase: str, *,
    surface_n_gram: int = 5,
    use_semantic: bool = False,
) -> ParaphraseScore:
    """Score a paraphrase candidate.

    use_semantic: if True, lazy-import sentence-transformers for cosine
        similarity. If False, semantic_similarity returns None.
    """
    surface = _ngram_jaccard(original, paraphrase, n=surface_n_gram)
    lexical = _word_jaccard(original, paraphrase)

    semantic: float | None = None
    if use_semantic:
        semantic = _semantic_cosine(original, paraphrase)

    # Verdict heuristic
    if surface >= 0.5:
        verdict = "verbatim"
        rationale = "Too much verbatim overlap — rewrite the structure, not just swap words."
    elif surface < 0.05 and lexical < 0.15:
        verdict = "too_distant"
        rationale = "Almost no shared vocabulary — paraphrase may have drifted from original meaning."
    elif surface < 0.15 and lexical >= 0.3:
        verdict = "true_paraphrase"
        rationale = "Low surface overlap with moderate lexical overlap — structure has been genuinely reorganised."
    elif lexical >= 0.6 and surface >= 0.2:
        verdict = "synonym_swap"
        rationale = "High lexical overlap with moderate surface — looks like word-by-word substitution. Restructure."
    else:
        verdict = "true_paraphrase"
        rationale = "Acceptable paraphrase distance."

    return ParaphraseScore(
        surface_similarity=surface,
        lexical_overlap=lexical,
        semantic_similarity=semantic,
        verdict=verdict,
        rationale=rationale,
    )


def _ngram_jaccard(a: str, b: str, *, n: int = 5) -> float:
    a_grams = _ngrams(_tokens(a), n)
    b_grams = _ngrams(_tokens(b), n)
    if not a_grams and not b_grams:
        return 0.0
    if not a_grams or not b_grams:
        return 0.0
    inter = a_grams & b_grams
    union = a_grams | b_grams
    return len(inter) / len(union)


def _word_jaccard(a: str, b: str) -> float:
    a_words = {t.lower() for t in _tokens(a)}
    b_words = {t.lower() for t in _tokens(b)}
    if not a_words and not b_words:
        return 0.0
    inter = a_words & b_words
    union = a_words | b_words
    return len(inter) / len(union)


def _semantic_cosine(a: str, b: str) -> float:
    """Cosine similarity using sentence-transformers. Lazy-imported."""
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embs = model.encode([a, b], convert_to_tensor=True, show_progress_bar=False)
    return float(util.cos_sim(embs[0], embs[1]).item())


def _tokens(text: str) -> list[str]:
    return _TOKEN.findall(text.lower())


def _ngrams(tokens: list[str], n: int) -> set[str]:
    return {" ".join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}
