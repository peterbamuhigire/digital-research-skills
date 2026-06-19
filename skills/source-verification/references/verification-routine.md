# Verification Routine

## Registry Checks

- [ ] `sources` root exists and has entries.
- [ ] Every source has `id`, `title`, `ref`, `tier`, `accessed`, `verification`, and `confidence`.
- [ ] Every claim has `id`, `claim`, `source_ids`, `confidence`, and `status`.
- [ ] Every quote has `source_id`, `locator`, `verified`, and exact-match status.
- [ ] Every synthesis item references valid claim IDs.
- [ ] Placeholder values are not treated as release-ready.

## Quote And Statistic Checks

| Item | Check |
|---|---|
| Direct quote | Text matches source exactly and locator is present |
| Numeric claim | Number, unit, date, and population match source |
| Paraphrase | Meaning has not drifted from source |
| URL | Link resolves or archive reference exists |

## Verification Manifest

| Field | Requirement |
|---|---|
| verifier | Person or agent |
| checked_at | UTC date/time |
| sources_checked | Source IDs |
| claims_checked | Claim IDs |
| quotes_checked | Quote IDs |
| failures | Rejected or quarantined items |
| release_status | pass, conditional, fail |
