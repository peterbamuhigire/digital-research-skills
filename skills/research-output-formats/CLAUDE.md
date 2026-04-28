# Claude-specific — research-output-formats

- Run this skill **before** drafting any deliverable whose format is not already pinned by a template, house style, or statutory form.
- Use the selection router in `SKILL.md` to name the format. Do not draft against a vague label like "report".
- After the format is fixed, load `references/academic-vs-nonacademic-variants.md` and explicitly state which variant you are writing.
- Load only the family reference relevant to the deliverable. Never load all five.
- Embed the chosen format **and** variant verbatim in every sub-agent brief that produces drafted text. A sub-agent without a format defaults to academic-essay voice.
- Do not change format mid-document. If the user later asks for a different format, run this skill again and produce a new draft — do not splice voices.
- Format never excuses fabrication. Even pamphlets, op-eds, and product descriptions carry the `source-evaluation` evidence-discipline clause.
- For terminal rendering, hand off to `professional-word-output` or `python-document-generation` only after the format and variant are locked.

See `SKILL.md`.
