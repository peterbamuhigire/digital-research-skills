# Codex / generic-agent — academic-voice-and-register

```yaml
audit:
  hedging:
    rate_per_1000: <float>
    target: 6-12
    verdict: under_hedged | over_hedged | within_norm
    overclaims_found: [...]
  reporting_verbs:
    overused: [{verb, count}]
    underused_categories: [...]
  ai_template_phrases_found: [...]
  register: first_person | passive_impersonal | active_third
  tense_consistency: bool
```

See `SKILL.md`.
