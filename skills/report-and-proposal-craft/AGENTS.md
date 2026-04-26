# Codex / generic-agent — report-and-proposal-craft

```yaml
report_or_proposal:
  artifact: informational | analytical | recommendation | progress | feasibility | audit | research | business_plan | internal_proposal | external_proposal | rfp_bid | wp_backgrounder | wp_numbered_list | wp_problem_solution
  audience_grid: {decider, influencer, blocker, user, gatekeeper}
  purpose_xyz: {reader, decision, because_document_shows, next_action, deadline}
  scqa: {situation, complication, question, answer}
  three_way_discipline:
    findings_descriptive_only: bool
    conclusions_no_new_evidence: bool
    recommendations_owned_dated_costed: bool
  white_paper_specific:
    flavor: backgrounder | numbered_list | problem_solution | null
    mantra_pass_per_section: bool
    vendor_named_only_after_allowed_page: bool
    single_cta: bool
  references_loaded: [...]
```

See `SKILL.md`.
