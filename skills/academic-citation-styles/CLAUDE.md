# Claude-specific guidance — academic-citation-styles

- Pick the style **before** writing — don't switch mid-document.
- For pandoc-driven .docx, store citations in a `.bib` file + use `--citeproc` with the appropriate `.csl`.
- Verify DOI liveness with `WebFetch` before final export — broken DOIs are caught by reviewers.
- Never cite ChatGPT / Claude / other LLMs as a source. Cite the underlying source.

See `SKILL.md`.
