# Book-driven source admission and currentness

This reference turns the supplied books into research questions and admission rules without treating them as current authorities.

## Source classes

Classify a book or practitioner work as durable concept input, contextual evidence, or time-sensitive claim. Books can inform hypotheses about systems, markets, narratives, finance, learning, and operating behaviour. They cannot by themselves establish current law, policy, standard, software version, platform capability, security control, or command syntax.

## Claim discipline

For each material claim, record claim text, source ID, source tier, exact support or paraphrase, scope, publication or version date, access date, freshness class, review date, confidence, and whether the statement is fact, synthesis, inference, or unresolved gap. A recommendation must not be stronger than its evidence.

## Currentness admission

Use authoritative current sources for time-sensitive claims: standards bodies, regulators, official vendor or project documentation, and primary technical specifications. Verify that the source is live, in scope, and current enough for the claim. If support is missing, stale, ambiguous, or contradicted, quarantine the claim and state what would resolve it.

## Portfolio register

The 2026-09 book wave is controlled by the portfolio currentness register at `C:\wamp64\www\skills-web-dev\docs\source-registers\skills-engine-currentness-2026-09.json`. Validate it with `validate_source_currency.py` before release and refresh time-sensitive entries at or before their review dates.

## Research output

Separate source-backed findings, cross-source synthesis, inference, recommendation, uncertainty, and gaps. Preserve provenance and do not copy raw books or OCR into a skill engine.
