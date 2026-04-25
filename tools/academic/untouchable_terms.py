"""Untouchable-terms registry — terms paraphrasers must NOT substitute.

Per Bailey: "Do not attempt to paraphrase every word, since some have no
true synonym (e.g. demand, economy)."

These are technical / canonical / proper-noun terms that lose accuracy if
paraphrased. The paraphrase validator should preserve these verbatim.
"""
from __future__ import annotations


# Categorised list — extend per project / per discipline.
UNTOUCHABLE_TERMS: dict[str, list[str]] = {
    "historical_events": [
        "Industrial Revolution",
        "World War I", "World War II",
        "Great Depression",
        "Cold War",
        "French Revolution",
        "American Civil War",
        "Renaissance",
        "Enlightenment",
    ],
    "economic_indicators": [
        "GDP", "GNP", "GNI", "CPI", "PPI", "PPP",
        "purchasing power parity",
        "balance of payments",
        "current account",
        "inflation rate",
    ],
    "international_organisations": [
        "World Bank", "International Monetary Fund", "IMF",
        "United Nations", "UN", "WHO", "World Health Organization",
        "OECD", "WTO", "World Trade Organization",
        "OPEC", "ASEAN", "African Union", "European Union", "EU",
        "ECOWAS", "EAC", "East African Community",
        "African Development Bank", "AfDB",
        "ICIJ", "OCCRP", "Transparency International",
    ],
    "scientific_canonical": [
        "DNA", "RNA", "mRNA", "ATP",
        "general theory of relativity", "special theory of relativity",
        "natural selection",
        "scientific method",
        "germ theory",
        "thermodynamics",
        "quantum mechanics",
        "evolution",
    ],
    "named_theories": [
        "social contract",
        "invisible hand",
        "tragedy of the commons",
        "broken windows theory",
        "rational choice theory",
        "bounded rationality",
        "comparative advantage",
        "Marxism", "Keynesian", "neoliberalism",
        "post-colonial theory",
    ],
    "legal_canonical": [
        "due process",
        "habeas corpus",
        "common law",
        "civil law",
        "stare decisis",
        "rule of law",
        "presumption of innocence",
        "right to silence",
        # Specific statute names — never substitute
        "Landlord and Tenant Act 2022",
        "Rent Restriction Act 1982",
        "Fair Credit Reporting Act",
        "Gramm-Leach-Bliley Act",
        "GDPR",
    ],
    "stat_methods": [
        "regression analysis",
        "p-value",
        "standard deviation",
        "confidence interval",
        "null hypothesis",
        "type I error", "type II error",
        "machine learning",
        "neural network",
    ],
    "ea_specific": [
        "Mau Mau",
        "Buganda",
        "EAC",
        "common market",
        # Place names that should never be transliterated
        "Nairobi", "Kampala", "Dar es Salaam", "Kigali",
        "Bujumbura", "Juba",
    ],
}


def all_untouchable() -> set[str]:
    """Flat set of all untouchable terms for fast lookup."""
    out: set[str] = set()
    for terms in UNTOUCHABLE_TERMS.values():
        for t in terms:
            out.add(t.lower())
    return out


def is_untouchable(term: str) -> bool:
    return term.lower().strip() in all_untouchable()


def find_untouchables_in(text: str) -> list[str]:
    """Return untouchable terms found in the text (case-insensitive)."""
    text_lower = text.lower()
    found: list[str] = []
    for term in all_untouchable():
        if term in text_lower:
            found.append(term)
    return sorted(set(found))
