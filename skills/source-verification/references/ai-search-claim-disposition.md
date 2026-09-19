# AI-search claim disposition

AI-search observations must be recorded as bounded evidence. A claim record
uses one disposition:

| Disposition | Meaning | Release boundary |
|---|---|---|
| `durable_synthesis` | A stable method or concept assembled from named sources | Do not turn it into a current platform guarantee |
| `current_supported` | A current claim supported within a recorded source scope and review window | Requires source IDs, scope, access date, review date, and limitation |
| `inference` | Analyst reasoning beyond directly observed source text | Keep the inference label and warrant visible |
| `partial` | Evidence supports only part of the proposed wording | Narrow the wording and preserve the gap |
| `NOT_ASSESSED` | Evidence is missing, stale, inaccessible, or ambiguous | Quarantine until a qualifying review exists |

Use a separate `observation_type` for `mention`, `citation`, `referral`, or
`conversion`. These are different events and must not be renamed as rank,
recommendation, visibility, or demand without evidence for that exact claim.
Each observation carries `source_ids`, scope, date, and limitation. Weak
evidence remains `NOT_ASSESSED`; metadata cannot upgrade it.

Guarantees fail closed. A record that promises ranking, inclusion,
recommendation, citation, traffic, or conversion is blocked even when it has a
source. A `current_supported` record whose `review_after` date has passed is
stale and becomes `NOT_ASSESSED` until reverified. Durable book-derived ideas
are useful hypotheses, not current platform evidence.

The deterministic checks are in `tools/verification/kaizen_contracts.py`.
Synthetic valid, weak-evidence, and stale-currentness cases are in
`tests/fixtures/kaizen-contracts.json` and
`engine/tests/test_kaizen_contracts.py`.
