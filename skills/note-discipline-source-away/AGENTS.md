# Codex / generic-agent — note-discipline-source-away

```yaml
note_card:
  id: "..."
  project_id: "..."
  heading: "..."        # short topic
  point: "..."          # FRAGMENT — not a sentence
  source_id: "..."
  source_page: "..."    # required for quotes
  is_quote: bool
  quote_marks_required: bool
  personal_comment: "..."  # required for paraphrases
  tags: [...]

source_away_gate:
  source_text_removed: bool   # required before composition
  composition_reads_only_cards: bool   # required
```

See `SKILL.md`.
