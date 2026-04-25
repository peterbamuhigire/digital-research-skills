# Claude-specific guidance — social-source-extraction

- Without Reddit OAuth credentials, **don't try real-time Reddit scraping in-conversation** — flag as a "next-pass" item.
- For inline social findings, use search-engine-indexed snippets and explicitly mark them "theme-level only, not verbatim".
- Brief sub-agents to use the methods in `SKILL.md` and to flag when constraints prevent verbatim extraction.

See `SKILL.md`.
