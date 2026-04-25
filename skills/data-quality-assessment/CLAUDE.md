# Claude-specific — data-quality-assessment

- Profile + score every dataset before analysis. No exceptions.
- Pass research_topic + required_columns + expected_scope to score relevance properly.
- Composite < 0.7 → escalate to operator; do NOT proceed silently.
- Save provenance packet (parquet + profile.json + dq.json + manifest.json).

See `SKILL.md`.
