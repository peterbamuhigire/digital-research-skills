# Codex / generic-agent guidance — osint-methodology

Per-finding output structure:

```yaml
target: "..."
finding_type: identification | footprint | network | infrastructure | geolocation
finding: "..."
sources: [{url, tier, date, platform}]
confidence: high | medium | low
temporal_context: YYYY-MM-DD
verification_limit: "..."
ethics_review: open-source-only | excluded
```

See `SKILL.md`.
