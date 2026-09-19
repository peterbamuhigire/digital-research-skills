# Objection-response release gate

Every material finding, recommendation, comparison, or causal conclusion must
carry a countercase record before release:

```yaml
conclusion: the bounded finding or recommendation
strongest_objection: the most knowledgeable dissenting challenge
alternative: an alternative explanation, option, or rival hypothesis
response:
  outcome: defeats | limits | open
  text: evidence-based response, with uncertainty visible
source_ids: [registered source IDs]
objection_source_ids: [registered source IDs, when applicable]
response_source_ids: [registered source IDs, when applicable]
```

The objection must be represented accurately and the alternative must be
material enough for a fresh reviewer to recognise it as a genuine countercase.
`open` preserves an unresolved objection and lowers confidence; it does not
silently disappear from the product. Missing objection, alternative, or
response is a release blocker. An unknown, fabricated, or misreported source
reference is a release blocker under evidence discipline.

This gate is a reasoning and release boundary, not an automated truth claim.
The response outcome says how the analyst handled the countercase; it does not
make the underlying evidence stronger. The reviewer must still confirm source
identity, locator, support state, scope, and currentness.

The deterministic shape checks are in
`tools/verification/kaizen_contracts.py`. Synthetic normal, unresolved,
missing-objection, and fabricated-source cases are in
`tests/fixtures/kaizen-contracts.json` and
`engine/tests/test_kaizen_contracts.py`.
