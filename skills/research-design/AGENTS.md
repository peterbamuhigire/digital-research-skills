# Codex / generic-agent — research-design

```yaml
research_design:
  design_document:
    empirical_puzzle: "..."
    theoretical_puzzle: "..."
    research_questions: [...]
    action_list: [...]
  layers_loaded: [historical | trend | mroc | knowledge_lifecycle | design_document | report_builder]
  knowledge_lifecycle_stage: discovery | capture | curation | storage | retrieval | application | reuse | retirement
  report_builder:
    pulls_from: [research/, analysis/, opportunities/]
    schema: "..."
    output_path: "...docx"
```

See `SKILL.md`.
