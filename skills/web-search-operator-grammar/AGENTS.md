# Codex / generic-agent guidance — web-search-operator-grammar

Wrap every search query in the four-layer build:

```yaml
phrase: "<core multi-word concept>"
synonyms: [a, b, c]      # OR-joined
excludes: [x, y]          # -term
site: <domain or TLD>
filetype: <pdf|xlsx|...>
intitle: <required>
```

See `SKILL.md`.
