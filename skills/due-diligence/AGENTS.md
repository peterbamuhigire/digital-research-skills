# Codex / generic-agent — due-diligence

```yaml
dd_engagement:
  scope: "..."
  jurisdictions: [...]
  cutoff_date: "YYYY-MM-DD"
  crawl:
    collect: [...]
    review: [...]
    analyse: [...]
    weigh: [...]
    log: [...]
  sanctions_screen:
    lists: [OFAC, UN, EU, UK_HMT, ...]
    algorithm: fuzzy_match
    name: "...", dob: "...", nationality: "...", aliases: [...]
    run_at: "YYYY-MM-DDTHH:MMZ"
    hits: [...]
  ubo_trace:
    target_entity: "..."
    chain: [...]
    natural_person_reached: bool | flagged_opacity_barrier
  cara:
    context: "..."
    allegations:
      - {text, source_refs, tier, verdict: refuted|partial|substantiated|unresolved}
    resolutions: [...]
    actions: proceed | proceed_with_conditions | decline | escalate
```

See `SKILL.md`.
