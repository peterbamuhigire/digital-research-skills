# Codex / generic-agent — business-report-typology

```yaml
business_report:
  type: informational | analytical | recommendation | progress | feasibility | justification | audit | research | business_plan
  formality: formal | informal
  preliminaries: [cover, title_page, transmittal, toc, list_of_figures, executive_summary]
  body: [introduction, methodology, findings, analysis, conclusions, recommendations]
  supplementaries: [references, appendices, index]
  three_way_discipline:
    findings_descriptive_only: bool
    conclusions_no_new_evidence: bool
    recommendations_owned_dated_costed: bool
  visuals: [{number, title_takeaway, caption, source}]
```

See `SKILL.md`.
