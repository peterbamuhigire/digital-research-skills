# Codex / generic-agent — business-writing

```yaml
business_artifact:
  channel: email | memo | letter | plan | blog | web | speech | resume | internal_comms
  language: en | fr | sw
  seven_steps:
    step_1_readers_purpose: bool
    step_2_collect: bool
    step_3_brainstorm: bool
    step_4_organize: bool
    step_5_draft: bool
    step_6_revise: bool
    step_7_proof: bool
  prose_audit:
    avg_sentence_words: <int>
    max_sentence_words: <int>
    latinate_strikes: <int>
    vague_adjective_strikes: <int>
    passive_voice_count: <int>
    first_revision_cut_pct: <float>
  references_loaded: [...]
```

See `SKILL.md`.
