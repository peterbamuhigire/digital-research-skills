# Codex / generic-agent — due-diligence-report-architecture

```yaml
report:
  privileged: true
  attorney_work_product: bool
  subject_type: person | company
  flags: [{flag: red|amber|green, title, summary, sources}]
  cara: {C, A, R, A}            # if person
  swot: {S, W, O, T}            # if company
  body_sections: [{title, content}]
  sources_cited: [...]
  disclaimer: included          # always
```

See `SKILL.md`.
