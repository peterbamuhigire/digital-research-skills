# Claude-specific — google-search-api-operator

- Use `tools/google/search_api.py` not direct SERP scrapes.
- Cache aggressively — quota is finite.
- Combine with `google-stakeholder-recon` for fan-out queries.
- Combine 2+ engines (CSE + SerpAPI or Brave) for breadth on important questions.

See `SKILL.md`.
