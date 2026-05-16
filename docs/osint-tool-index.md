# OSINT Tool Index

The engine can ingest public OSINT toolkit pages into a project-level candidate
registry:

```powershell
python -m engine index-osint-tools <project-id> "https://example.com/toolkit" --geography "Nicaragua"
```

The command writes two registry layers:

- `_registry/sources.yaml` gets the source page as tier 5, low confidence.
- `_registry/osint-tool-index.yaml` gets each extracted external link as a
  candidate OSINT tool/source.

This is deliberately conservative. A blog post, newsletter, or Substack page is
a lead source, not proof that the linked tool is official, current, lawful,
complete, or useful. Every imported record starts with:

- `status: candidate`
- `confidence: low`
- `access_model: unverified`
- `verification: primary-site verification pending`

Before a candidate can support a research claim, verify the primary site,
record terms-of-use or access constraints, capture an archive snapshot where
appropriate, and promote the record to `status: verified`.

## Example Source Class

Country-specific public OSINT toolkit posts are a useful discovery source. For
example, UNISHKA Research Service published an "OSINT of Nicaragua" Substack
post on May 06, 2026 that lists categories such as open data portals, company
registries, sanctions sources, WHOIS/domain intelligence, media sources, and
maps/satellite intelligence:

https://unishka.substack.com/p/osint-of-nicaragua?triedRedirect=true

The source page itself remains tier 5 unless independently verified. The linked
primary portals should be verified one by one before use.

## Verification Promotion

Candidate promotion should record:

- whether the linked URL is live and resolves to the expected organisation;
- the source tier and verification method from `source-evaluation`;
- legal and terms-of-use constraints;
- whether account creation, payment, API keys, or rate limits apply;
- access date and archive reference, where available;
- confidence after primary-site inspection.

Rejected tools stay in the registry with `status: rejected` and a short
verification note so they are not rediscovered as fresh leads in later waves.
