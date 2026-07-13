---
name: osint-investigation
description: Use when lawful public-source investigation needs stakeholder reconnaissance, adverse-media review, chronology, source capture, or case-vault discipline; use pi-investigation only for authorised licensed-PI work and refuse surveillance, harassment, stalking, or doxxing.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# OSINT Investigation

Single entry skill for open-source intelligence work — civilian, lawful, defensible. The engine refuses state-intelligence, surveillance, harassment, doxxing, and stalking-adjacent uses. Load `pi-investigation` for licensed-PI workflows; load `due-diligence` for corporate-vetting work.

## Investigation-type router

| Investigation goal | Load |
|---|---|
| Map a person's public footprint and stakeholder relationships | `references/google-stakeholder-recon.md` + `references/social-source-extraction.md` |
| Trace someone whose contact details are stale | `references/skip-tracing-craft.md` |
| Profile an individual or entity for adverse media | `references/adverse-media-investigation.md` |
| General OSINT methodology (planning, collection, analysis, dissemination) | `references/osint-methodology.md` |
| Build a chronology of events from heterogeneous sources | `references/chronology-construction.md` |
| Verify images / videos / documents | load `source-evaluation` skill, `references/silverman-media-forensics.md` |
| Run a phased investigation with client-facing cost / consent gates | `references/osint-methodology.md` § Hetherington Phased Approach |
| Build a repeatable case notebook / graph / evidence vault | `references/osint-case-vaults.md` |
| Reach for a technique not covered by the standard references (deep / dark web, geospatial, email tracing, metadata, crypto, IoT, ML, disinformation) | `references/advanced-osint-techniques.md` |
| Use automated source or claim reliability scoring for high-volume triage | `source-evaluation/references/automated-reliability-triage.md` |

## The OSINT cycle (universal)

`references/osint-methodology.md` carries the full cycle. Quick reference:

1. **Plan** — define the question, the deliverable, the legal/ethical bounds, the timebox.
2. **Collect** — open-source channels only; archive snapshots at capture time.
3. **Analyse** — synthesize across sources; flag confidence per claim.
4. **Disseminate** — produce the artifact (report, brief, chronology, profile) with provenance per claim.

## Source posture (mandatory pairing with `source-evaluation`)

OSINT lives or dies on source vetting. Every claim drawn from an open-source channel must pass through `source-evaluation`:

- Tier the source (1–5 credibility ladder).
- Apply Burke pentad to primary documents.
- Apply Tudor twelve points to media / journalism.
- Apply Silverman media-forensics to images / videos.
- Triangulate tier-5 claims against ≥2 tier-1–3 sources.

A single-tier-5 OSINT report is not an OSINT report; it is a rumour log.

## Reference index

| Reference | Load when |
|---|---|
| `references/osint-methodology.md` | Always — the cycle and the operating posture |
| `references/google-stakeholder-recon.md` | Mapping a target's public footprint via search-engine mastery (the "three Googles" + TLD atlas + stakeholder recon patterns) |
| `references/social-source-extraction.md` | Pulling structured signal from social platforms — what's lawful, what's not, how to preserve provenance |
| `references/adverse-media-investigation.md` | Building an adverse-media file on an individual or entity (allegations, prosecutions, lawsuits, sanctions, regulator actions, scandals) |
| `references/skip-tracing-craft.md` | Locating a person whose last-known contact details are stale — civilian/lawful skip tracing only |
| `references/chronology-construction.md` | Building a timeline from heterogeneous sources, with confidence per event and gaps named explicitly |
| `references/macleod-investigative-search.md` | Government-records / FOIA / court-docket / public-records-aggregator workflow + people-finding with legal sensitivities (DPPA, FCRA, GLBA, HIPAA flags). MacLeod, *How to Find Out Anything* (Tier 1). |
| `references/osint-doctrine-and-history.md` | Institutional lineage (FBIS → OSC), four competing definitions of OSINT (OSC / Congress-Simmons / NATO-Steele / historical), distinctions vs. clandestine INTs / journalism / SOCMINT, the engine's adopted definition. Bean, *No More Secrets* (Tier 1). |
| `references/osint-validation-and-anti-patterns.md` | OSINT validation cycle, six named tensions (speed/verification, volume/signal, secret/open, commercial/analytic, privacy, tradecraft/scientific), source-vetting standards, positive cases (SARS / Burundi), anti-patterns (over-classification, "Googlification", factory-line outsourcing, single-advocate evidence gaps). Bean, *No More Secrets* (Tier 1). |
| `references/advanced-osint-techniques.md` | Topic atlas for techniques beyond the standard references — deep/dark web, geospatial intelligence, email tracing, metadata/forensics, cryptocurrency / blockchain, IoT, ML-augmented OSINT, disinformation analysis, big-data sources. Botwright, *Advanced OSINT Strategies* (4-volume bundle), with engine guardrails. |
| `references/osint-case-vaults.md` | Markdown-first case vaults, Obsidian-style templates, entity/source/case note separation, activity logs, asset custody, graph/canvas use, and local-first storage posture. |
| `source-evaluation/references/automated-reliability-triage.md` | Automated source / claim scoring for high-volume triage only; requires axis-level signals, source-independence checks, calibration, and human-review flags. |

## Lawful / unlawful boundary (engine refuses)

The engine **refuses**:

- State-intelligence collection or surveillance.
- Doxxing or harassment-enabling output.
- Pretexting for credentials / accounts (impersonation).
- Bypassing access controls (TOS-violating scrape of authenticated content).
- Information about minors except in narrow safeguarding contexts with explicit authorisation.
- Output that would identify a private individual's home address, schedule, or family without a verified safeguarding or legal authority.
- Operational targeting of specific living people in jurisdictions where such targeting is illegal or risks violence.

The engine **permits**, with discipline:

- Public-record research (court filings, regulator publications, registries).
- Map-of-public-footprint reporting on public figures, executives, and entities.
- Adverse-media collation tied to a defensible diligence purpose.
- Chronology of public events.
- Skip-tracing for legitimate civilian purposes (debt collection by licensed parties, journalism, family reconnection — never for stalking).

## Universal output rule

Every claim in any OSINT artifact carries:

- Source URL or document ID (with archive snapshot).
- Source tier (1–5).
- Capture timestamp (UTC).
- Confidence (high / medium / low).
- Verification notes (Burke / Tudor / Silverman if applicable).

Claims that fail the rule do not ship.

## Universal anti-patterns

- Single-tier-5 sourcing for a load-bearing claim.
- "Public record" cited without the actual record (URL, case number, registry hit).
- Screenshot of a social-media post with no archive and no posting timestamp.
- Profile of a private individual built without a defensible diligence purpose.
- Chronology with mixed-confidence events not flagged as such.
- Image used as evidence without a reverse-image-search trail.
- Mixing OSINT outputs with PI workflow steps that require licensure (load `pi-investigation` for those).
- "It was on Reddit" treated as evidence of fact rather than evidence of a claim being made.
- Scraping authenticated content to build the file (TOS violation; tier-5 evidence at best).
- Skip-tracing for purposes outside the lawful list above.

## Universal ship gate

- [ ] Investigation goal stated in writing; deliverable named; legal/ethical bound stated.
- [ ] OSINT cycle (plan / collect / analyse / disseminate) followed.
- [ ] Every claim has source ref + tier + capture timestamp + confidence.
- [ ] Tier-5 claims triangulated against ≥2 tier-1–3 sources.
- [ ] Archive snapshots captured for every URL.
- [ ] Images / videos checked via Silverman workflow.
- [ ] Chronology gaps named, not papered over.
- [ ] Refusal-list checked: no doxxing, no minors, no state-intel, no pretexting, no TOS-violating scrape.
- [ ] Engine-level guardrail (`source-evaluation/references/evidence-discipline.md`) audit run.

## Companion skills

- `source-evaluation` — universal source vetting (mandatory pairing).
- `due-diligence` — when the investigation is corporate/financial vetting.
- `pi-investigation` — when licensed-PI workflows apply (chain-of-custody, formal report).
- `web-scraping-foundations` — when collection requires automation.
- `report-and-proposal-craft` — for the artifact form.

<!-- dual-compat-start -->
## Use When

- Use for a lawful civilian investigation based on publicly available sources.

## Do Not Use When

- Refuse surveillance, stalking, harassment, doxxing, credential theft, impersonation, or targeting that could expose a private person to harm.

## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Lawful purpose, subject scope, jurisdiction, risk boundary, and collection plan | Requester and investigation lead | required | Stop and request scope; do not begin collection |

## Workflow

1. Confirm purpose, legality, proportionality, subject risk, and stop conditions.
2. Define questions and collect the minimum necessary public material with provenance.
3. Corroborate identity and claims; stop on private-data exposure, unlawful access, or material misidentification risk.
4. Build chronology and findings; recover from blocked access by recording no source found and narrowing conclusions.

## Capability Contract

Default to read-only public-source research. Network collection must stay within authorised lawful scope; contact, bypass, surveillance, or publication of personal data requires separate lawful authority and may be refused.

## Degraded Mode

Without source access or identity corroboration, return a collection plan and explicit gaps, not a speculative profile.

## Decision Rules

| Choice | Action | Failure avoided |
|---|---|---|
| Collection creates a credible harm or misidentification risk | Stop, minimise, and escalate | Harm to a private person |
| Public claim has independent corroboration | Include with provenance and confidence | Single-source allegation treated as fact |

## Outputs

| Artefact | Consumer | Acceptance |
|---|---|---|
| Case log, source register, chronology, and qualified findings | Investigation lead or authorised client | Every item has provenance, collection time, confidence, and lawful-purpose link |


## Osint Investigation Evidence Notes
- Preserve URLs, lawful captures, identity-resolution notes, contradictions, and no-source-found results.

## Quality Standards

Minimise personal data, separate allegation from verified fact, and make confidence and limitations visible.

## Anti-Patterns

- Treating a matching name as identity proof. Fix: corroborate independent identifiers.
- Republishing unnecessary personal data. Fix: redact and minimise.
- Using one adverse-media item as fact. Fix: verify and label allegation status.
- Bypassing an access control. Fix: stop and use lawful public routes.
- Hiding a failed search. Fix: report no source found and the search scope.

## Worked Example

For an authorised stakeholder review, corroborate public organisational roles across independent sources, log dates and URLs, and omit unrelated private details.

## References

- [OSINT methodology](references/osint-methodology.md)
- [Validation and anti-patterns](references/osint-validation-and-anti-patterns.md)
- [Chronology construction](references/chronology-construction.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Consumer | Acceptance |
|---|---|---|
| Source and collection register | Investigation lead | Provenance, collection time, confidence, and gaps are recorded |

## Reference Index

- [Advanced techniques](references/advanced-osint-techniques.md); [adverse media](references/adverse-media-investigation.md); [stakeholder reconnaissance](references/google-stakeholder-recon.md)
- [Investigative search](references/macleod-investigative-search.md); [case vaults](references/osint-case-vaults.md); [doctrine and history](references/osint-doctrine-and-history.md)
- [Skip tracing](references/skip-tracing-craft.md); [social-source extraction](references/social-source-extraction.md)
