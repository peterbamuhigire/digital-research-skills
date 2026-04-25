# Codex / generic-agent guidance — academic-citation-styles

Use BibTeX or CSL-JSON to store citations. For pandoc:

```bash
pandoc input.md -o output.docx \
  --citeproc \
  --bibliography=refs.bib \
  --csl=<style>.csl
```

Style files at https://citationstyles.org/styles/

See `SKILL.md`.
