# Codex / generic-agent — plagiarism-prevention

```yaml
gate:
  overlap_check:
    n_gram_lengths: [5, 7, 10, 15]
    critical_threshold: 12
    high_threshold: 7
    max_critical_hits: 0
    max_high_hits: 2
  citation_density:
    min_per_1000_words: 8
    target_per_1000_words: 15
    max_per_1000_words: 30
  quote_density:
    max_ratio: 0.05
  paraphrase_distance:
    required_verdict: true_paraphrase
    forbidden_verdicts: [verbatim, synonym_swap]
  hedging_audit:
    target_rate_per_1000: 8
    fail_if: under_hedged | over_hedged
```

See `SKILL.md`.
