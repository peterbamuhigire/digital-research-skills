# Adverse-media investigation

Negative-news search for DD reports. Hetherington's discipline: multi-source rule, identifier anchoring, common-name disambiguation.

## The five risk-term categories

The engine queries the subject against curated negative-news terms across:

1. **Financial crime**: fraud, embezzlement, money laundering, ponzi, tax evasion, insider trading, bribery, kickback, corrupt, racketeer
2. **Regulatory**: sanctions, fined, penalty, consent decree, cease and desist, debarred, disqualified, censure, revoked
3. **Criminal**: indicted, convicted, arrested, charged, sentenced, guilty plea, felony
4. **Litigation**: lawsuit, sued, class action, settlement, judgment against
5. **Reputational**: scandal, investigation, probe, exposé, allegation

## Anti-defamation discipline

Common-name false positives are the #1 risk. Apply Hetherington's identifier anchor:

```python
from tools.dd import search_adverse_media

hits = list(search_adverse_media(
    subject_name="John Smith",
    aliases=["J. Smith"],
    subject_identifiers=["1965", "Acme Corp", "Nairobi"],  # DOB year, employer, location
    engines=["google_cse", "serpapi"],
    risk_categories=["financial_crime", "regulatory", "criminal"],
    languages=("en",),
    per_query_limit=10,
))

high_conf = [h for h in hits if h.confidence == "high"]   # ≥50% identifiers matched
medium_conf = [h for h in hits if h.confidence == "medium"]
```

**High-confidence** (≥50% of identifiers matched in snippet) → likely real hit.
**Medium-confidence** (some identifiers matched) → manual triangulation.
**Low-confidence** (no identifiers) → log only — likely common-name confusion.

## Multi-source rule

A single hit on a single source is a **rumour**. Hetherington requires:
- ≥2 outlets reporting the same fact OR
- 1 outlet + 1 court/regulatory primary source

Do not include in the DD report unless the multi-source rule is met.

## Foreign-press necessity

For non-US/UK subjects, you must cover foreign press:
- Hire a local correspondent or use US-embassy directory
- Native-speaker analysts catch nuance machine-translation misses
- Microfilm / microfiche still load-bearing for pre-2000 events
- Engine: query in the target country's language (use `translate-then-search` skill — roadmap)

## Anti-patterns

- Single-source negative finding → reported as fact in DD report
- Common-name match without identifier verification
- Trusting machine-translated foreign-press snippets without native review
- Forum/competitor smear treated as real reporting
- Bot-generated narrative treated as journalism
- Tone confusion: distinguishing complaint forums from legitimate news

## Reporting in the DD report

Per the **due-diligence-report-architecture** skill, adverse-media findings appear in the body section "Media findings (descending date order)" with one of two formats:

- **Paraphrase** (default): summarise the finding with citation
- **Direct quote** (when content is technical or risk-laden): verbatim quote with attribution

Always include the **negative finding** as a separate line: *"A multi-source adverse-media search across [engines] on [date] did not reveal hits against the subject's identifiers."*

## See also

- `tools/dd/adverse_media.py` — implementation
- `due-diligence-report-architecture` — where the findings land
- `evidence-discipline` — citation rules apply
- `provenance-chain` (roadmap) — earliest-known timestamp for each hit
