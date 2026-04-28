# Claude-specific — osint-investigation

- Always pair with `source-evaluation`; every claim carries ref + tier + timestamp + confidence.
- Refuse the unlawful list: state-intel, doxxing, harassment, pretexting, TOS-violating scrapes of authenticated content, minors outside safeguarding, identifying private individuals' home/schedule/family without authority.
- Run the OSINT cycle in order: plan → collect → analyse → disseminate.
- Archive every URL; never cite a URL without an archive snapshot.
- Triangulate tier-5 claims against 2+ tier-1–3 sources before they appear as fact.
- Name chronology gaps; do not paper them over.
- Redirect licensed-PI workflows to `pi-investigation`; redirect corporate vetting to `due-diligence`.
- For client-facing investigations with cost / consent gates, run the Hetherington Phased Approach (Phase 1 Online / Phase 2 Boots-on-the-Ground / Phase 3 Recommended Next Steps) — see `references/osint-methodology.md` § Hetherington Phased Approach.
- Apply the Hetherington universal investigation scaffold (personal identifiers / financial history / civil-criminal filings) to every Phase-1 person-centric pass; if a line is intentionally skipped for legal / ethical / scope reasons, say so explicitly in the report.
- Every Phase-1 and Phase-2 deliverable ends with a Recommended Next Steps section naming tangent leads, monitoring suggestions, and escalation paths.
- For techniques beyond the standard references (deep/dark web, geospatial, email tracing, metadata, crypto, IoT, ML, disinformation), load `references/advanced-osint-techniques.md`. Default to **decline** on dark-web access, IoT interaction, and face-recognition against private individuals unless documented authority exists.

See `SKILL.md`.
