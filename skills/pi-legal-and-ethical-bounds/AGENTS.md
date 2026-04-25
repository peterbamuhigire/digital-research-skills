# Codex / generic-agent — pi-legal-and-ethical-bounds

```yaml
gate:
  activity: "..."
  state: <ISO US state>
  recording: {audio: bool, two_party_consent_state: bool}
  gps: {used: bool, vehicle_owner_consent: bool}
  pretexting: {target_class: financial|medical|telephone|none}
  protected_data: [fcra_credit, dppa_dmv, hipaa, glba]
  permissible_purpose: "..."
  decision: lawful | refuse | counsel_required
  documentation_required: [...]
```

See `SKILL.md`.
