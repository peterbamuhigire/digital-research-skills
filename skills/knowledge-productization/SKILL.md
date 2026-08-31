---
name: knowledge-productization
description: Use when the engine must turn research into reusable knowledge assets, audience-specific variants, and monetizable offerings rather than a one-off document only. Encodes knowledge audit, asset design, reuse discipline, and commercialization framing.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
  priority: medium
---

# Knowledge Productization

<!-- dual-compat-start -->
## Use When

- Use when research must be reused across multiple outputs, audiences, or offers.
- Use when the owner wants reusable IP and monetizable assets rather than a one-off report only.

## Do Not Use When

- The task is a single deliverable with no reuse path.
- The work is still too early and the evidence base is not yet stable.


## Knowledge Productization Required Context
- The core research corpus or asset inventory.
- Intended audiences or buyers.
- Reuse, sensitivity, and confidentiality constraints.


## Knowledge Productization Method Detail 2
- Read this `SKILL.md` first, then load only the needed reference file.
- Audit the knowledge corpus before choosing wrappers.
- Preserve provenance while creating variants and offers.

## Quality Standards

- Reusable vs client-specific knowledge is explicit.
- Audience variants are intentional.
- Commercial claims stay inside validated evidence.


## Knowledge Productization Existing Failure Notes
- Rewriting from scratch when a reusable core exists.
- Packaging confidential details into reusable IP.
- Monetizing ideas that have not survived verification.


## Knowledge Productization Core Deliverables
- A knowledge audit, audience-variant plan, asset ladder, or monetization-ready packaging plan.

## Book-derived additions

For a dissertation or research corpus that must become reusable, audience-bound
knowledge products, load `dissertation-writing-process` and retain provenance,
originality, and rights checks.

## References

- Use the `references/` files for audit, audience planning, and productization.
## Inputs

| Artefact | Source or provider | Requirement | If absent |
|---|---|---|---|
| Verified knowledge assets and audience need | knowledge-mining and requester | required | Return an asset-gap assessment when either is absent |

## Capability contract

Read access to the verified asset library and audience brief is required. Variant creation, pricing, licensing, publication, or commercial release needs explicit owner authority.

## Degraded mode

Fallback when rights, audience evidence, or asset access is unavailable: return a qualified product concept and gap register; do not label demand, rights, or release readiness as assessed.

## Decision rules

| Choice | Action | Failure avoided |
|---|---|---|
| Same evidence serves a distinct audience decision | Create a controlled variant | Copy proliferation without purpose |


## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Productization plan and audience variants | owner, editor, or commercial team | Each variant retains claim provenance and names its buyer or user decision |


## Knowledge Productization Evidence Notes
- Record source-asset identifiers, audience decision, rights status, variant changes, refresh ownership, and pilot evidence.

## Worked example

Reuse one verified claim library for an executive brief and a training note, changing structure and explanation but retaining the same source identifiers.

<!-- dual-compat-end -->

This skill treats research output as an asset portfolio, not just a finished report. It helps the engine preserve, package, and repurpose insight across clients, sectors, and output forms without breaking provenance.

## When to use

- The same research must feed several deliverables or audiences
- A project should produce reusable IP, not only a single report
- The owner wants offers, products, briefs, dashboards, papers, proposals, or books from the same corpus
- The engine needs a knowledge audit before building a new product line

## Five rules

1. **Audit the knowledge before packaging it.** Know what is explicit, reusable, sensitive, or client-specific.
2. **Separate core insight from wrapper.** Findings stay stable; format, tone, and CTA change by audience.
3. **Reuse with provenance.** Every reusable asset keeps the chain back to the original evidence.
4. **Build an asset ladder.** One research corpus should support multiple value levels, from memo to report to workshop to book.
5. **Monetization never outruns proof.** Product claims must stay inside what the evidence base can support.

## Router

| Situation | Load |
|---|---|
| Auditing what knowledge exists and what can be reused | `references/knowledge-audit.md` |
| Planning variants for different audiences | `references/audience-variant-planning.md` |
| Designing monetizable assets and offers | `references/productization-and-monetization.md` |


## Knowledge Productization Core Method Notes
1. Inventory the corpus: findings, methods, visuals, frameworks, templates, data assets.
2. Classify what is reusable, sensitive, client-specific, or obsolete.
3. Choose the asset ladder: memo, report, white paper, proposal, workshop, dashboard, thesis, book.
4. Map each audience to tone, level of detail, evidence density, and CTA.
5. Publish variants without breaking source traceability.

## Ship gate

- [ ] Core insight and evidence base are defined
- [ ] Reusable vs client-specific boundaries are explicit
- [ ] Audience variants are intentionally differentiated
- [ ] Every asset has a clear use case and buyer / reader
- [ ] Source traceability survives repackaging
- [ ] Commercial claims stay inside validated evidence


## Knowledge Productization Additional Failure Modes 2
- Treating every finished report as a dead end
- Rewriting from scratch when a reusable core exists
- Packaging confidential client specifics into supposedly reusable IP
- Building products around ideas that have not survived research verification

## Companion skills

- `research-design` — knowledge lifecycle and report builder
- `report-and-proposal-craft` — business-facing long-form variants
- `academic-writing` — scholarly variants
- `executive-communication` — executive-facing variants
- `python-document-generation` / `professional-word-output` — final rendering

## Sources for this skill

- Hackos, JoAnn T. *The Complete Guide to Knowledge Management*. Tier 1.
- *Knowledge Management and Business Strategies*. Tier 1.
- *Developments in Information and Knowledge Management Systems for Business Applications*. Tier 1.


## Workflow
1. Audit verified assets, rights, freshness, audience, and decision need.
2. Select the smallest useful product and define its provenance-preserving variant rules.
3. Stop when rights, evidence, or buyer need is unresolved.
4. Pilot and review; recover by returning to the knowledge audit and narrowing scope.

## Evidence Produced

| Evidence | Consumer | Acceptance |
|---|---|---|
| Productization decision and provenance register | Owner and release reviewer | Each variant names its source assets, audience, use, and gaps |


## Anti-Patterns
- Packaging an unverified claim library. Fix: verify or remove unsupported assets.
- Creating variants without a distinct audience decision. Fix: keep one source product.
- Copying content until provenance drifts. Fix: use controlled source identifiers.
- Claiming demand without evidence. Fix: label it as a hypothesis and test it.
- Ignoring refresh cost. Fix: define ownership and cadence before release.

## Reference Index

- [Knowledge audit](references/knowledge-audit.md); [audience-variant planning](references/audience-variant-planning.md); [productization and monetization](references/productization-and-monetization.md)
