# Claude-specific guidance — research-report-builder

- Use the `professional-word-output` skill (in this repo) for high-fidelity rendering.
- Use `python-document-generation` if pure-Python `python-docx` flow is preferred.
- Read each cohort's `research/`, `analysis/`, `opportunities/` files into context before assembling — schema-driven order matters.
- After assembling the master markdown, lint with `markdown-lint-cleanup` before render.
- Save versioned outputs to `projects/<project-id>/report-v<N>-<date>.docx`.

See `SKILL.md`.
