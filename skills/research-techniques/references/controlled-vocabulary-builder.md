# Controlled vocabulary builder

A controlled vocabulary is a "terminology system unambiguously mapped to concepts" (Bergeron). Every serious research project needs one. Without it, the same concept gets named four ways and the synthesis breaks.

## Why it matters

- **Search precision.** MeSH lets PubMed users find papers about "Crohn's disease" even when the paper says "regional enteritis."
- **Synthesis integrity.** Cross-cohort synthesis fails when "deposit theft" in one cohort and "non-refund" in another aren't linked.
- **Project memory.** Abbott: "my own first book was essentially the writing down in words of a controlled vocabulary that I had developed."
- **Disambiguation.** Bergeron's "fish" example — goldfish, marlin, salmon, fish-sticks — same word, four concepts.

## Three layers

### Layer 1 — Terms list
Flat list of canonical terms. Each entry:
```yaml
term: "Deposit theft"
synonyms: ["non-refund", "deposit non-return", "deposit retention"]
definition: "Failure of landlord to return tenant security deposit at lease end"
first_used: 2026-04-25
project_scope: east-africa-property-hostel
```

### Layer 2 — Taxonomy (hierarchy)
Broader / narrower / related-term relations:
```
Tenant pain
├── Deposit theft (synonyms: non-refund, deposit retention)
│   ├── Outright disappearance
│   ├── Vague-damages deduction
│   └── "Eating-the-deposit" tenant counter-strategy
├── Rent gouging
│   ├── Mid-lease hike
│   ├── Currency-pegged rent
│   └── Election-cycle gouging
└── ...
```

### Layer 3 — Ontology (typed relations)
For knowledge-graph-class projects:
```
Komakech & 7 Ors v Ayaa & Anor (case)
  --HEARD_AT--> Uganda High Court
  --DECIDED_IN--> 2018
  --PRECEDES--> UG Landlord & Tenant Act 2022
  --RULES_ON--> Forcible eviction
```

## Decision rules

- **Build incrementally.** Don't try to fix the vocabulary up front. Add as concepts emerge.
- **Versioned.** Every change is dated; revisions are part of project history.
- **Project-scoped, not global.** A controlled vocabulary for a property-hostel project is different from one for a banking-DD project.
- **Synonym lists are not optional.** Half the synthesis value comes from these.
- **Definitions are not optional.** Bergeron: "words can have different meanings, depending on context."
- **Refresh on phase transition.** When the design document revises, the vocabulary often needs revision too.

## When the source has its own vocabulary

If a source provides a controlled vocabulary (MeSH for medicine, ERIC thesaurus for education, LCSH for general library work, IPC/CPC for patents), **use the source's terms as the canonical layer**. Build your project layer on top, not in conflict with it.

## File location

`projects/<project-id>/VOCABULARY.md` — always visible, always editable.

Pair with `projects/<project-id>/IDEAS.md` (Abbott's "idea notebook"): controlled-vocabulary-tagged append-only ideas log.

## Anti-patterns

- Tag-everything-with-everything filing — Abbott: "you are literally refusing to think"
- No synonyms — synthesis fails silently
- No definitions — terms drift
- Forcing the project's terms onto a domain that has its own controlled vocabulary
- Vocabulary frozen at project start — it must evolve
- Treating vocabulary as a deliverable rather than a working tool — it's both, but primarily working

## Anchors for East African projects

- **Geographic:** Uganda / Kenya / Tanzania / Rwanda / Burundi / South Sudan; cities in canonical spellings
- **Currency:** UGX / KES / TZS / RWF; always with code, not symbol
- **Universities:** Makerere, MUBS, Kyambogo, UoN, Kenyatta U, Strathmore, USIU, JKUAT, UDSM, Mzumbe, UR
- **Regulators:** KRA, URA, KCCA, NEMA, IRA, EARB, AREA Uganda

## See also

- `research-design-document` — design and vocabulary co-evolve
- `crosswalk-matrix` — uses vocabulary terms as row labels
- `reading-mode-router` — meditative reading is the primary feeder of new vocabulary
- `cross-cohort-synthesis` — depends on vocabulary alignment to find shared pains
