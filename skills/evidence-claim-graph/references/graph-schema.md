# Graph Schema

## Node Types

| Node | Meaning | Required fields |
|---|---|---|
| Source | Origin of evidence | id, title, ref, tier, accessed, verification, confidence |
| Evidence | Atomic extracted fact, quote, stat, observation, image, or dataset item | id, source_id, locator, type, content, verification |
| Claim | Statement that can be true, false, supported, contested, or inferred | id, claim, scope, source_ids, confidence, status |
| Warrant | Reason the evidence supports the claim | id, claim_id, warrant, assumption_ids |
| Assumption | Load-bearing unstated or partially evidenced premise | id, assumption, test, status |
| Contradiction | Evidence or claim conflict | id, claim_ids, conflict, resolution_status |
| Gap | Missing evidence or unresolved question | id, gap, decision_impact, next_search |
| Finding | Promoted analytical conclusion | id, finding, claim_ids, confidence, limits |

## Edge Types

| Edge | Direction | Rule |
|---|---|---|
| supports | evidence -> claim | Evidence directly supports the claim |
| weakens | evidence -> claim | Evidence reduces claim strength |
| contradicts | claim -> claim | Claims cannot both be true as scoped |
| warrants | warrant -> claim | Warrant explains evidence-to-claim link |
| assumes | claim -> assumption | Claim depends on assumption |
| synthesizes | finding -> claim | Finding combines claims |
| resolves | source/evidence -> contradiction | Evidence settles a conflict |

## Status Values

- `untested`
- `supported`
- `contested`
- `contradicted`
- `synthesis`
- `inference`
- `retired`
