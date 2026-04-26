# OSINT methodology

Open-source intelligence is research with **operational consequence**. The findings may be used to make security decisions, journalism, or investigation. The standards differ from market or pain-point research.

## What OSINT covers

- **Person profiling** — identification, employment history, online footprint, contact details, associates
- **Organisation profiling** — corporate structure, key personnel, operational footprint, public claims vs reality
- **Domain / infrastructure** — DNS, hosting, certificates, registrar, related domains, IP neighbourhoods
- **Geolocation** — image, video, and text-based location identification
- **Network mapping** — relationships between any of the above

## Legal & ethical guardrails

- **Open source only.** No purchased / leaked / breached / hacked data.
- **No social engineering.** Even if technically open, manipulating a target into revealing information is out of scope.
- **No active interaction with the target.** Passive collection only.
- **No PII publication unprovoked.** Findings are research outputs, not exposés.
- **Respect platform ToS.** Reddit, X, LinkedIn, Facebook all have ToS limits — note them.
- **Deconfliction.** If multiple researchers / orgs may be working a target, surface this in the brief.

## Standard sources

- **Person:** LinkedIn, GitHub, Twitter/X, Mastodon, archived blogs, conference attendance lists, paper authorship, court records, professional registries, alumni directories
- **Org:** Companies House (UK), corporateaffairs (KE), URSB (UG), BRELA (TZ), SEC filings, regulator registers, news archives, NGO disclosures
- **Domain:** WHOIS, DNS records, certificate-transparency logs (crt.sh), Wayback Machine, archive.today, BuiltWith
- **Geolocation:** Google Earth historical, Sentinel Hub, Yandex reverse-image, OSM, Mapillary, Bellingcat tooling
- **Network:** Maltego, Shodan, Censys

## Verification rigour

- **Identification first.** A misidentified target is the most common OSINT failure. Never proceed past this step on weak ID.
- **Triangulate every claim.** Cross-reference any single-source finding before promoting it past "indicative".
- **Confidence ratings per finding.** High (multi-source verified), Medium (single tier-1/2 source), Low (single tier-3+ source).
- **Document temporal context.** Information dates fast in OSINT — every finding gets a timestamp.
- **Distinguish association from causation.** "X follows Y on Twitter" ≠ "X works for Y".

## Output structure

- `<project>/research/osint-targets.md` — target list with disambiguation
- `<project>/research/footprint.md` — per-target online footprint
- `<project>/research/network.md` — relationships
- `<project>/research/infrastructure.md` — technical (where applicable)
- `<project>/research/confidence-log.md` — per-finding confidence + sources
- Final Word doc uses Schema G

## Operational security caveats

- **Note any tool used that may reveal researcher identity** — Shodan / Censys queries leave logs
- **Pivoting via VPN / Tor** is the researcher's choice, not the engine's; document the chosen posture
- **Some sources require log-in** — don't use personal accounts for sensitive lookups

## Anti-patterns

- Passing OSINT off as due diligence (different rigour, different liability)
- Publishing PII without operational necessity
- Assuming a username connects across platforms without proof
- Using leaked data to verify claims (out of scope)
- Single-source identification

## See also

- `evidence-discipline` — non-negotiable
- `source-verification` — tier discipline
- `due-diligence-framework` — overlapping but stricter on liability
- `social-source-extraction` — feeds the social-platform layer
- `research-report-builder` — Schema G
