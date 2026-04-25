# Codex / generic-agent — paraphrase-discipline

```yaml
paraphrase:
  original_passage: "..."
  candidate: "..."
  scoring:
    surface_similarity: 0.0-1.0    # target < 0.15
    lexical_overlap: 0.0-1.0       # target 0.30-0.50
    semantic_similarity: 0.0-1.0   # target > 0.75
    verdict: true_paraphrase | synonym_swap | verbatim | too_distant
  citation_required: true
```

See `SKILL.md`.
