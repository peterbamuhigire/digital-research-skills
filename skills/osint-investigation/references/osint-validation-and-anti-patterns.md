# Reference — OSINT Validation and Anti-Patterns

**Canonical source:** Bean, Hamilton. *No More Secrets: Open Source Information and the Reshaping of U.S. Intelligence*. Praeger Security International / ABC-CLIO, 2011. Tier 1. Local extract: `extracted-books/no-more-secrets.txt`.

This reference is the **operating discipline** companion to `references/osint-doctrine-and-history.md`. It encodes the validation cycle, the named tensions (speed vs. verification, volume vs. signal, secret vs. open, commercial vs. analytic), the case studies that show OSINT working and failing, and the anti-patterns Bean catalogs.

---

## The validation cycle

Bean reports the OSC's standard cycle (Ch 4 + Appendix). The engine adopts and adapts:

1. **Requirement** — the intelligence question, originated by a named customer (decision-maker, examiner, principal). No requirement → no OSINT product. ("Research that happens to use public sources" is not OSINT.)
2. **Collection plan** — what sources, in what languages, on what timebox, with what budget. The plan is documented and revisable.
3. **Source vetting** — every source rated for reliability and credibility (apply NATO Admiralty Code from `analytic-tradecraft/references/sourcing-and-deception.md` + the engine's 5-tier ladder from `source-evaluation/SKILL.md`).
4. **Discovery** — sweep the named source streams; capture URLs and timestamps; archive snapshots at capture time.
5. **Discrimination** — strip the noise; identify the signal-bearing material.
6. **Distillation** — synthesise across discriminated material; flag confidence per claim.
7. **Dissemination** — produce the product (report, brief, profile, chronology) with provenance per claim and customer-specific framing.
8. **Feedback** — customer's reaction informs the next cycle's requirements.

The Steele formula ("*deliberately discovered, discriminated, distilled, and disseminated*") corresponds to steps 4–7. The engine adds steps 1, 2, 3, 8 to make the cycle complete.

---

## The four named tensions

Bean treats these as live, unresolved tensions in IC OSINT. The engine inherits them and must navigate each consciously.

### Tension 1 — Speed vs. verification

Aspin-Brown noted open-source product "*took longer to produce, required validation, and failed to cover many key aspects critical to policymakers*" (Ch 2). Speed and verification trade off; both customers and analysts undervalue the trade-off.

**Engine discipline.** Verification is non-negotiable; speed is the variable. If the customer's deadline does not allow verification, the product ships as a **HYPOTHESIS** at LOW confidence, with explicit indicators of what would corroborate (per `analytic-tradecraft/references/kent-estimative-probability.md`). The engine refuses to ship "verified" outputs that have not been verified.

### Tension 2 — Volume vs. signal

OSC produces ~2,300 products/day; Bean asks whether any agency "*can effectively analyze it.*" (Ch 4.) The volume of public material exceeds the analyst's capacity to read it; signal extraction at scale is the binding constraint.

**Engine discipline.** Cohort-based dispatch (one sub-agent per cohort) is the engine's volume strategy. Signal extraction is enforced via gap-analysis (`research-techniques/references/gap-analysis.md`) — the analyst names what is missing, not what is present. Volume without signal is busy-work.

### Tension 3 — OSINT vs. classified streams

Institutional bias inside the IC: "*if it ain't secret, it ain't real*" (Fingar, paraphrasing the culture he is trying to change; Bean Appendix, p. 156). Analysts ignored by policymakers who do their own searching.

**Engine discipline.** The engine is civilian and has no classified streams. It treats this tension inside-out: the engine's discipline is to **cite the public source** even where a classified analogue exists in the customer's world. The engine's value is in surfacing what is already public but not yet known.

### Tension 4 — Openness vs. secrecy (over-classification)

OSC routinely classifies analyses built on public inputs. Aftergood / FAS critique: this is driven by "*habit, the cultivation of the mystique of secret intelligence, the protection of copyrighted information, and the preservation of 'decision advantage'*" (Ch 1, p. 5).

**Engine discipline.** The engine treats classification as the customer's choice, not the analyst's. The engine produces unclassified deliverables by default; the customer may classify after delivery if they choose. The engine refuses to classify its own analytic process — methodology and source manifest ship with every product.

### Tension 5 — Commercial vs. analytic imperatives

Outsourcing (Intellibridge, STRATFOR, Oxford Analytica, Jane's, IntelCenter) creates "*a tradeoff between low-cost tradecraft and high-cost technology*"; piecework analyst incentives create factory-line production that jettisons novel lines of inquiry.

**Engine discipline.** The engine charges for tradecraft (depth, verification, calibration), not for word-count. The engine refuses piecework framing.

### Tension 6 — Privacy / legal limits

Domestic homeland-security application collides with civil-liberties limits. The WikiLeaks moment (2010) surfaced unresolved boundaries.

**Engine discipline.** The engine refuses doxxing, harassment, surveillance of private individuals without authority, identification of minors outside safeguarding, and TOS-violating scrapes of authenticated content. See `osint-investigation/SKILL.md` "lawful / unlawful boundary" section. Defers to user counsel on jurisdiction-specific limits.

---

## Source vetting standards (from Bean + engine adoption)

Bean reports the OSC's source vetting (Appendix; OSA Provost Kraus): "*basic tradecraft, Internet exploitation, and reviewing finished intelligence products*" — including media-ownership and political-leaning analysis and "*very precise search and research strategies… not intuitive.*"

Engine adoption (binding):

- **Source ownership** — who owns / funds / publishes the source? Is there a named editorial standard?
- **Political leaning** — is the source aligned with a faction? Does the alignment shape the framing?
- **Track record** — has the source been right before? (NATO Admiralty Code A–F.)
- **Information credibility** — is this specific item independently corroborated? (NATO Admiralty Code 1–6.)
- **Acquisition story** — how did the engine obtain the source? Bruce Ch 12 ("The Missing Link") on the analyst-collector relationship: analysts who don't understand acquisition routinely overweight some streams.
- **Archive snapshot** — every URL captured at access time, archived (Wayback / archive.today) before the product ships.

---

## Tradecraft vs. scientific method — Bean's reported tension

Bean describes a live debate (Ch 4):

- **Tradecraft camp** (analyst self-perception): "*more art and experience than anything else*"; idiosyncratic, novelty-promoting; recorded by Rob Johnston's ethnography.
- **Scientific / systematized camp** (Johnston, WMD Commission): push for machine translation, advanced search, knowledge extraction, structured methods.

**Engine adoption.** Both. The engine encodes structured methods (the Heuer/Pherson SATs from `analytic-tradecraft/references/heuer-pherson-sats.md`) **and** preserves the tradecraft of novel-hypothesis generation (the Pre-Mortem and What-If techniques from the same reference). The choice is not method *vs.* art; it is method *enabling* art.

---

## Case studies — positive

### SARS early warning (2003)

Intellibridge analyst Dan Silver flagged an unusual *Ming Pao* (Hong Kong) report on atypical pneumonia, alerted JICPAC and U.S. health officials; later honoured by ProMED-mail for contribution to containment.

**Lesson.** Open-source signal can lead the classified system, when the analyst has the requirement framing right and the language coverage to read source-language material.

### Aspin-Brown "Burundi battle" (1995)

Steele's open-source team out-delivered CIA's classified product on a 4-day deadline — top-10 journalists / academics, executive summaries, order-of-battle to tribal level, 1:50 maps and recent cloud-free imagery — vs. CIA's "*PowerPoint chart of nominal value.*"

**Lesson.** OSINT, run as a discipline (not as Googling), can match or exceed classified production on timely policy questions.

---

## Case studies — negative (anti-patterns)

### Over-classification

Classifying analyses built entirely from public inputs ("phone-book classification"). Driven by habit, mystique, copyright-protection, and decision-advantage rationales. Erodes democratic value.

### "If it ain't secret, it ain't real"

Cultural reflex among classified-side analysts that systematically devalues OSINT product. Self-fulfilling: undervalued OSINT receives less investment, produces lower-quality work, justifies further undervaluation.

### Factory-line outsourcing

Word-count quotas and individual incentive wages suppress novel hypotheses. Piecework is the wrong incentive structure for analysis. Bean: contractors paid per product produce more product, not better product.

### "Googlification"

Equating OSINT with Google search. Bean's Hulnick critique: "*relentless used-car salesman*" framing of Steele substitutes persuasion for evidence; Wettering's critique: conclusions without proofs. **OSINT is not Googling; Googling without discipline is not OSINT.**

### Single-advocate evidence gap

Letting a charismatic advocate substitute persuasion for evidence. The engine's structural defence: every product ships with the source manifest; persuasion without sources does not pass the ship-gate.

### Technology-substitution-for-people

Procuring technology (machine translation, knowledge extraction) in lieu of investing in skilled analysts. Gannon's caution (Bean Appendix). Tools amplify analyst skill; they do not replace it.

### Reusable-commodity OSINT

Treating OSINT as a commodity reusable across clients dampens client-specific rigor. The engine's discipline: every product is requirement-specific; reusable artefacts are knowledge-base material (`docs/analysis/initial-evaluation/04-recommendations.md` A6 `knowledge-base` skill), not finished products.

---

## Bean's recommendations (engine adoption)

For institutions:

- Treat OSINT as a legitimate discipline with funded infrastructure.
- Locate vetting of external experts inside the OSINT function.
- Declassify and disseminate unclassified products to citizens by default.
- Build oversight of contractors.

For analysts:

- Combine tradecraft (novelty, judgment) with systematic methods.
- Cultivate standing relationships with outside experts before crises (Fingar's standing-expert recommendation).
- Explicitly assess source ownership and political leanings.

For policy / democracy:

- Use open source to "*challenge taken-for-granted assumptions, engage a wide array of stakeholders, improve planning and decision making, and adequately assess the actual and potential consequences of policy decisions.*"
- Expand citizen access to OSINT products to support deliberation.

---

## Companion references

- `references/osint-doctrine-and-history.md` — institutional lineage and competing definitions.
- `references/osint-methodology.md` — engine's own OSINT cycle (Plan → Collect → Analyse → Disseminate).
- `references/macleod-investigative-search.md` — government-records / FOIA / public-records workflow.
- `analytic-tradecraft/references/sourcing-and-deception.md` — single-source rule, Admiralty Code, D&D framework. Bean's Johnston / WMD-Commission discussion bears directly on this.
- `analytic-tradecraft/references/cognitive-bias-checklist.md` — bias mitigation in analysis.

## Source

Bean, Hamilton. *No More Secrets: Open Source Information and the Reshaping of U.S. Intelligence*. Praeger Security International / ABC-CLIO, 2011. Tier 1.
