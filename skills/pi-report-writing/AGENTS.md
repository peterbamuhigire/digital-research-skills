# Codex / generic-agent — pi-report-writing

```yaml
report:
  case_type: background | matrimonial | dd | fraud | insurance | process | skip
  sections:
    1_header: {file_id, date, case_type, client, fee, investigator_creds}
    2_subject_block: {name, aliases, dob, ssn_last4, dl, distinguishing_features}
    3_purpose: "..."
    4_steps: [{date, source, method}]
    5_findings: [{topic, content}]
    6_credibility: per_finding
    7_photo_log: exhibit_link
    8_statements: [exhibit_links]
    9_recommendations: [...]
    10_signature: bool
  exhibits:
    - type: photo_log | statement | coc | surveillance
      docx_path: "..."
  court_ready: bool
```

See `SKILL.md`.
