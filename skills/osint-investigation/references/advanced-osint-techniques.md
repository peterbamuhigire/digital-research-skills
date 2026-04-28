# Advanced OSINT techniques

Topic-coverage reference for OSINT techniques beyond the engine's defaults in `osint-methodology.md`. Drawn principally from Rob Botwright, *Advanced OSINT Strategies: Online Investigations and Intelligence Gathering* (a four-volume bundle: Foundations, Navigating the Digital Shadows, Advanced Arsenal, Mastering Cutting-Edge Strategies and Tools, 2024). The book is broad rather than deep; this reference uses it as a topic atlas and overlays the engine's lawful-civilian guardrails on every section.

## The non-negotiable guardrail

These techniques sit on top of the engine's existing rules, not beside them. Every technique listed below carries the constraints from `SKILL.md`:

- Open-source only. No purchased / leaked / breached / hacked data.
- Lawful, civilian, defensible. No state-intelligence or surveillance work.
- Refusal list applies: doxxing, harassment, pretexting, TOS-violating scrapes of authenticated content, identifying private individuals' home / schedule / family without authority.
- Source-evaluation tiering and triangulation apply to every claim.

Where a technique below skirts the refusal list (notably social engineering, dark-web access, IoT data collection, cryptocurrency tracing of named individuals), the engine's default is to **decline** unless the engagement has documented authority — corporate security mandate, lawful investigation, sanctioned research, or explicit client authorisation that itself has lawful basis.

## When to load this reference

- The standard `osint-methodology.md` workflow has produced what it can and the question still has gaps.
- The investigation's question is technical (an artifact, an account, an address, a transaction) rather than relational (a person, an organisation).
- The engagement has the authority to pursue more invasive techniques.
- The deliverable is for a security-professional reader who can interpret the technical material.

## Technique atlas

### 1. Advanced search queries (Botwright Bk 2 ch. 1)

- Operator stacking: `site:`, `intitle:`, `inurl:`, `filetype:`, `cache:`, `before:` / `after:`, exact-phrase quotes, `-` exclusion, `OR` boolean.
- Search-engine selection: Google for breadth, Bing for some indexes Google has dropped, Yandex for image search and Russian-language coverage, DuckDuckGo for non-personalised results, Mojeek for an independent index.
- Specialised search: code (GitHub / sourcegraph), academic (Google Scholar, Semantic Scholar), legal (CourtListener, RECAP), patents (Google Patents, Espacenet), business-records (per `due-diligence` jurisdictional atlas).
- "Search-engine archaeology": cached pages and Wayback Machine for content the live site has removed; Google's own cache is largely deprecated, so capture archive snapshots at the moment of finding.

### 2. Deep-web and dark-web investigations (Botwright Bk 2 ch. 2; Bk 3 ch. 1)

**Deep web** is anything not indexed by general search engines: paywalled databases, library catalogues, government records behind login, internal corporate intranets. Most legitimate investigation work happens here.

**Dark web** is overlay networks (Tor, I2P, Freenet) reachable only via specific clients. The engine's default posture:

- **Decline by default.** Dark-web access is justified only where the engagement has explicit authority and the researcher has the operational-security training to attempt it without compromise.
- **Where authorised**, use a dedicated, isolated VM, fresh Tor identity, no personally identifiable persistence, and a documented chain of custody for any artefact captured.
- **Never engage** with offerings on the dark web — buying, selling, recruiting, befriending — even for evidentiary purposes, without a lawful framework and supervisory signoff.
- Honeypot risk is high; many "marketplaces" are state, criminal, or research-team operated.

Specialised search engines for dark-web indexing (Ahmia, OnionSearch, etc.) exist; treat results as unverified until corroborated outside the dark-web context.

### 3. Geospatial intelligence (Botwright Bk 2 ch. 3; Bk 3 ch. 3)

- **Imagery sources:** Google Earth (current and historical), Sentinel Hub (Sentinel-2 free, near-real-time), Planet Labs (commercial, daily revisit), Maxar (high-resolution, paid), USGS EarthExplorer (Landsat archive).
- **Reverse image** for landmarks: Yandex (best for buildings outside the West), Google Lens (best in OECD), TinEye (best for catalogue-style images), Bing.
- **Map overlays:** OpenStreetMap, Mapillary (street-level user uploads), KartaView, Wikimapia.
- **Bellingcat methodology** is the canonical reference for image-based geolocation; pair with `chronology-construction.md` for time-of-day and weather verification.
- **Sun-position verification:** SunCalc.org for solar azimuth and elevation given a date, time, and location — corroborates or refutes claimed timestamps.
- **Shadow-length analysis** to estimate the time of an outdoor photograph; published Bellingcat case studies show worked examples.

Hard rule: never publish a geolocation that puts a private individual's home or daily routine in public view. If the geolocation belongs to a public-facing event or a corporate / state target, it is fair game.

### 4. Email and communication tracing (Botwright Bk 2 ch. 5; Bk 3 ch. 5)

- **Email headers** carry routing data — sender, recipient, intermediate servers, timestamps, message-IDs. The "Received" lines record each hop and read bottom-to-top.
- **Tools to interpret headers:** Microsoft's Message Header Analyzer, MXToolbox, Google's Admin Toolbox header parser. They convert raw headers into a route diagram with IPs and timestamps.
- **Common spoofing tells:** mismatched `Return-Path` and `From`, forged `Received` chains (timestamps that go backwards or pass through implausible relays), missing or invalid SPF / DKIM / DMARC results.
- **Reverse-resolution discipline:** an IP in a header is at best the host that handled the message; rarely the user. Geolocation of an IP gives city-level confidence, not street-level.
- **What this is NOT:** content-recovery from a third party's mailbox, password recovery, mailbox compromise. Email forensics on the engine's terms is header-only on emails the investigator's principal already lawfully holds.

### 5. Metadata analysis and digital forensics (Botwright Bk 3 ch. 4)

- **Image metadata (EXIF):** camera make / model, lens, settings, often GPS (when not stripped by the platform). Tools: ExifTool (canonical), Jeffrey's Image Metadata Viewer, exif.regex.info.
- **Document metadata:** PDF / Office documents carry author, last-saved-by, organisation, software version, creation/modification timestamps. ExifTool reads PDFs; `pdfinfo`, `oletools` for Office.
- **Important caveat:** most major social platforms strip EXIF on upload (Facebook, Instagram, Twitter / X, LinkedIn). Telegram channels and direct downloads from a personal cloud often preserve it. Always note where the file came from.
- **File-system / artefact forensics** is out of scope for OSINT; that is a digital-forensics speciality requiring lawful seizure and proper chain of custody. Do not attempt on the basis of OSINT-only authority.

### 6. Cryptocurrency and blockchain (Botwright Bk 2 ch. 9; Bk 3 ch. 9)

- **Public ledgers** (Bitcoin, Ethereum, most public chains) are open by design. Block explorers: blockchain.com, etherscan.io, blockchair.com, mempool.space.
- **Address clustering** (heuristics: common-input-ownership, change-address detection) attributes multiple addresses to a single entity. Commercial tools: Chainalysis, Elliptic, TRM Labs, CipherTrace; open: Walletexplorer, OXT for Bitcoin.
- **Mixing services / coinjoin** complicate but do not necessarily defeat tracing. Wasabi, Samourai, JoinMarket each have known fingerprints.
- **Privacy chains** (Monero, Zcash with shielded transactions) are deliberately opaque; tracing is research-grade, not evidentiary.
- **Pairing crypto trace with KYC artefacts** is where investigations succeed: subpoena returns, exchange leaks, voluntary disclosure. The crypto pseudonymity is broken at the on/off-ramp.

### 7. Internet-of-things data (Botwright Bk 3 ch. 7)

- **Shodan / Censys / ZoomEye** index internet-exposed devices: webcams, ICS, VOIP, routers, badly-configured databases.
- **Lawful use** is asset-discovery (your own organisation's exposure), threat-intelligence research, and academic study. Engaging with someone else's exposed device — even read-only — is almost always unlawful access.
- **The engine's default:** identify exposure, do not interact. A Shodan result is a finding; a connect attempt is a crime.
- **Default credentials** databases (CIRT.net, Routerpasswords) exist to support red-team and asset-recovery work; the engine does not use them against third-party devices.

### 8. Machine learning and OSINT (Botwright Bk 3 ch. 6; Bk 4 ch. 5, 9)

ML augments the analyst, never replaces evidence discipline. Useful applications:

- **Entity extraction** from large unstructured corpora (court filings, news archives, leaked-document collections that have lawful access). spaCy, Hugging Face NER models.
- **Translation** for foreign-language sources (DeepL, Google Translate, Argos). Always preserve the original; translation is a derived artefact subject to verification.
- **Topic modelling** for large document sets (BERTopic, classical LDA).
- **Image clustering** to group near-duplicate photos across platforms (perceptual hashing, CLIP embeddings).
- **Speaker / face recognition** is high-risk; the engine does not use commercial face-recognition services against private individuals. Use only in very narrow lawful contexts (sanctioned research, internal-asset matching, missing-persons casework with appropriate authority).

ML pipelines do not relax the engine's verification rule: every claim still passes through `source-evaluation` regardless of whether the analyst or a model produced it.

### 9. Disinformation analysis (Botwright Bk 4 ch. 10)

- **Account-network analysis** — coordinated inauthentic behaviour leaves graph-level fingerprints (creation-date clustering, posting-time synchronisation, shared content fingerprints).
- **Content-fingerprinting** — perceptual hashing for images, audio fingerprinting for clips, document-similarity hashing for repurposed text.
- **Provenance tracking** — Hunchly / Webrecorder / archive.today for capturing the state of a piece at the moment of finding; C2PA / Content Credentials for verifying provenance of generative-media claims.
- **Pair with `source-evaluation`** Silverman media-forensics rules; pair with `chronology-construction.md` to defeat dating-confusion attacks.
- **Caveat:** disinformation is a topic where the analyst is also a target. Anti-disinfo workflows operate against actors that monitor and adapt — operate from clean infrastructure and assume your queries may be observed.

### 10. Big-data OSINT (Botwright Bk 4 ch. 1)

- **Public-data warehouses:** Common Crawl (web), GDELT (events / news), OpenStreetMap full planet dumps, Wikidata, OpenCorporates, Companies House full data, USAspending.gov.
- **Search at scale:** Elasticsearch / OpenSearch for indexed corpora; Apache Spark / DuckDB for one-shot analytics on parquet dumps.
- **What changes at scale** is the cost of being wrong: a single bad inference applied to a million records is a much larger reputational risk than a hand-curated mistake. Sampling and statistical confidence become a discipline, not an afterthought.

## Skill cross-references

- `osint-methodology.md` — Phased Approach overlay, four-stage cycle, source-tiering.
- `due-diligence` — CRAWL framework and CARA report architecture; load when investigation work needs corporate / financial / sanctions overlay.
- `pi-investigation` — licensed-PI workflows.
- `source-evaluation` — every artefact above is treated as a candidate claim until tier-and-triangulate is satisfied.
- `chronology-construction.md` — geospatial timestamps, disinformation-dating challenges, email-header timeline reconstruction.

## Tools index (quick links, no endorsement)

| Domain | Open / free | Commercial |
|---|---|---|
| Web archive | Wayback, archive.today, Hunchly (paid feature set) | Page Vault, X1 Social Discovery |
| Search | Google, Bing, Yandex, DuckDuckGo, Mojeek, Marginalia | Maltego, IntelTechniques |
| Image / video forensics | InVID-WeVerify, FotoForensics, ExifTool | Amped Authenticate |
| Domain / DNS | crt.sh, dnsdumpster, viewdns.info | DomainTools, Whoisology |
| Network / device | Shodan (free tier), Censys (free tier) | Shodan paid, Censys Enterprise |
| Maps / imagery | OSM, Sentinel Hub, Google Earth | Planet, Maxar, Earthi |
| Crypto | Blockchain.com, etherscan, blockchair, OXT | Chainalysis, Elliptic, TRM Labs |
| Person-finders | local-jurisdiction registries (per `due-diligence`) | LexisNexis, Accurint, IRBsearch, TLO |
| Social platforms | platform native search; Hunchly capture | Maltego transforms, Echosec, Babel Street |
| Disinformation | Twitter graph tooling (where API is available), Hoaxy, MediaCloud | Graphika, Logically, Blackbird.AI |

The list is not exhaustive and changes faster than this document. Treat it as a starting set, not a recipe.

## Source books

- Botwright, *Advanced OSINT Strategies: Online Investigations and Intelligence Gathering*, 2024 — four-volume bundle.
- Bellingcat, *Online Open Source Investigation Toolkit* (live, open) — methodological canon for image and video work.
- Bazzell, *Open Source Intelligence Techniques*, 11th ed. or current — comprehensive tool reference.
- Hetherington, *The Guide to Online Due Diligence Investigations*, 2nd ed., Facts on Demand Press, 2015 — for the investigation-discipline overlay.
- See also the engine's `due-diligence`, `pi-investigation`, and `source-evaluation` skills for governance.
