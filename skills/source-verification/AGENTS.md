# Codex / generic-agent guidance — source-verification

## Capability requirements

- HTTP GET capability for URL-liveness checks
- File-read for auditing existing draft reports
- Optional: archive.org lookup for dead-link recovery

## Output shape

Verification reports a structured object per source:

```yaml
url: <string>
tier: 1|2|3|4|5
date_accessed: YYYY-MM-DD
liveness: live | redirected | dead
attribution_quality: primary | secondary | paraphrased
covers_claims: [<list of claims this source backs>]
```

See `SKILL.md` for canonical instructions.
