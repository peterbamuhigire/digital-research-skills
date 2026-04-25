# Codex / generic-agent guidance — quote-extraction

Output structure for each extracted quote:

```yaml
text: "Verbatim text"
class: primary | secondary | paraphrased | inferred
speaker: "Name or descriptor"
role: "Role / context"
outlet: "Source outlet"
date: YYYY-MM-DD
url: "https://..."
language_original: "en | sw | lg | fr | ..."
translation_status: "original | translated | both"
```

See `SKILL.md` for the canonical rules.
