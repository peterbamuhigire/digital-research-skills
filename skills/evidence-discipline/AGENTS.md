# Codex / generic-agent guidance — evidence-discipline

## Required behaviour for any agent in this engine

1. Refuse to write a numeric claim, name, statute, or URL without an inline citation.
2. Use explicit markers: `(synthesis)`, `(inference)`, `(paraphrased)`, `(estimated)`, `(gap — no source found)`.
3. If unable to find a source, return `"status": "gap"` rather than fabricating.
4. Verify URLs and cited statistics before returning final output.

## Required output schema for every claim

```yaml
claim: "..."
type: stat | quote | name | case | statute | url | finding
source_url: "https://..." | null
source_outlet: "..."
source_date: YYYY-MM-DD
source_quote: "..." (if applicable)
verification_status: verified | unverified | gap
markers: [synthesis | inference | paraphrased | estimated]
```

Outputs that do not conform are rejected by the orchestrator.

See `SKILL.md`.
