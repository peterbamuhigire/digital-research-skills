# Index-layer evidence contract

Use this contract when a source is represented in an index, taxonomy, search
record, or evidence graph. It keeps the source layer, the derived index layer,
and analyst interpretation separate.

## Required record

```yaml
subject_unit: claim | document | person | event | relationship
representation_method: human-readable method and vocabulary/version
context:
  scope: bounded population, corpus, or jurisdiction
  as_of: YYYY-MM-DD or source snapshot
index_version: immutable index release identifier
blind_spots:
  - description: excluded language, source type, actor, granularity, or stale category
    owner: named reviewer or team
source:
  source_id: registered source ID
  source_hash: SHA-256 of immutable source material
interpretations:
  - id: interpretation ID
    text: indexed interpretation
    source_id: same registered source ID
    source_hash: same immutable hash
    locator:
      kind: line | page | paragraph | offset | section | uri
      value: exact locator in the source
```

`subject_unit`, `representation_method`, `context`, `index_version`, and
`blind_spots` are part of the representation contract. A missing context is
`NOT_ASSESSED`, because a reviewer cannot establish scope or reconstruct the
interpretation. An unsupported or missing locator is also `NOT_ASSESSED`.
Unknown source IDs and hash mismatches are blockers. Re-indexing may change
the index version or interpretation text, but it must preserve the immutable
source hash.

The contract proves traceability and exposes limits. It does not prove that an
index label is semantically correct, complete, unbiased, or current. Those
questions require source verification and human review.

The deterministic shape checks are in
`tools/verification/kaizen_contracts.py`; synthetic normal and failure cases
are in `tests/fixtures/kaizen-contracts.json` and
`engine/tests/test_kaizen_contracts.py`.
