# Codex / generic-agent — source-evaluation

```yaml
source_audit:
  ref: "URL or document ID"
  tier: 1 | 2 | 3 | 4 | 5
  verification:
    evidence_discipline_passed: bool
    burke_pentad: {author, provenance, production, mechanics, aims}      # primary documents
    tudor_twelve_points: {recency, relevancy, authority, completeness, accuracy, clarity, verifiability, statistical_validity, internal_consistency, external_consistency, context, comparative_quality}  # media
    silverman_forensics: {exif, reverse_image_search, geolocation, archive, provenance_chain, tampering_check}  # media-forensics
  confidence: high | medium | low
  accessed_utc: "YYYY-MM-DDTHH:MM:SSZ"
  archive_snapshot: "URL"
triangulation:
  required_for_tier_5: 2_to_3_independent_sources
  performed: [source_ref_a, source_ref_b]
```

See `SKILL.md`.
