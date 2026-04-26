# Codex / generic-agent — pi-investigation

```yaml
pi_engagement:
  jurisdiction: "..."
  licence_id: "..."
  scope: "..."
  lawful_posture_attested: bool
  artefacts:
    - id: "..."
      capture: {timestamp_utc, capturer, location, method}
      hash_sha256: "..."
      custody_log: [{from, to, at, reason}]
      lawfulness_attestation: bool
  mcmahon_report:
    sections: {1_title, 2_investigator, 3_client_authorization, 4_scope_methodology, 5_chronology, 6_findings, 7_evidence_index, 8_limitations, 9_conclusions, 10_attestation}
  refusal_check:
    no_unlawful_surveillance: true
    no_pretexting_credentials: true
    no_consent_violation: true
    no_third_party_doxxing: true
```

See `SKILL.md`.
