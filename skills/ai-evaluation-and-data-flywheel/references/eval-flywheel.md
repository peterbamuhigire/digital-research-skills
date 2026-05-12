# Eval Flywheel

## Eval Case

| Field | Requirement |
|---|---|
| id | Stable case ID |
| task | User-like request |
| inputs | Files, sources, or context |
| expected checks | Observable criteria |
| source integrity checks | Required citation/quote/URL checks |
| known failure | What this case protects against |
| status | active, retired, candidate |

## Failure Tags

- `retrieval-miss`
- `citation-drift`
- `quote-error`
- `unsupported-claim`
- `reasoning-gap`
- `tool-failure`
- `format-mismatch`
- `latency-cost`
- `unsafe-output`

## Flywheel Rule

Only promote a feedback example into the eval set after a human or verifier confirms the expected behavior and source truth.
