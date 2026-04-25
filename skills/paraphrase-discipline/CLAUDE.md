# Claude-specific — paraphrase-discipline

- Use the four-step technique: read → close source → write from idea → compare back.
- Run `paraphrase_distance` with `use_semantic=True` on every paraphrase.
- Verdict must be `true_paraphrase`. Anything else: rewrite.
- Synthesising from 3+ sources naturally beats single-source paraphrase.

See `SKILL.md`.
