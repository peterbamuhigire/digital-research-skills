# Codex / generic-agent — academic-writing

```yaml
academic_artifact:
  type: paper | essay | thesis | dissertation
  variant: academic | popular
  discipline: sciences | social_sciences | humanities
  citation_style: APA | Chicago | MLA | Harvard | Vancouver
  source_away_workflow:
    notes_extracted: bool
    sources_removed_from_context: bool
    composition_done_from_notes: bool
    originality_check_passed: bool
    n_seven_gram_overlaps: <int>   # must be 0
  voice_audit:
    hedges_per_1000_words: <int>   # target 6..12
    reporting_verb_diversity: <int>
  references_loaded: [...]
  ship_gate: {...}
```

See `SKILL.md`.
