# Claude-specific guidance — quote-extraction

- Use `WebFetch` to retrieve the source page when extracting verbatim text — never rely on search-engine snippets, they truncate.
- When a sub-agent returns a quote, verify it against the source before writing to `quotes.md`.
- For Reddit / X / TikTok, flag the platform inline; never present social posts as authoritative voice.
- Translate Swahili / Luganda / French quotes inline — keep the original visible.

See `SKILL.md`.
