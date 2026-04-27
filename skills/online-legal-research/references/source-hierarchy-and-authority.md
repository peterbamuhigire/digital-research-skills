# Legal source hierarchy & authority

**Date written:** 2026-04-27
**Drawn from:** Putman & Albright, *Legal Research, Analysis and Writing* (Cengage, 2018), Parts I–II; *Legal Research* (anonymous compendium); Long, *Legal Research Using the Internet* (general framing).

This reference makes one decision easy: **what weight does this source carry, and is it allowed to bind the answer?**

## The two foundational distinctions

### Primary vs secondary authority

| Type | What it is | Examples |
|---|---|---|
| **Primary** | The law itself — what a court can be made to apply | Constitutions, statutes, regulations, judicial opinions, treaties, executive orders, court rules, gazette notices |
| **Secondary** | Commentary about the law — never the law itself | Textbooks, treatises, law-review articles, legal encyclopaedias, restatements, practice manuals, AI summaries, blog posts, LLM output |

**Only primary authority can bind a court.** Secondary authority can interpret, organise, summarise, or persuade — but it is never controlling. If your output rests load-bearing weight on a secondary source where a primary source exists, find the primary source.

### Mandatory vs persuasive authority

A second axis cuts across the first:

| Type | What it is | Effect |
|---|---|---|
| **Mandatory (binding)** | Primary authority that the deciding court is **required** to apply | Court must follow it absent an exception |
| **Persuasive** | Anything else — including primary authority from another jurisdiction, lower-court decisions in a higher court, dicta, or any secondary source | Court *may* be guided by it; not required |

**Putman & Albright's rule:** mandatory authority for a court is (a) the constitution and statutes of the jurisdiction whose law governs the case, in force on the relevant date, and (b) decisions of higher courts in the same court system on the same legal point.

Everything else — Supreme Court decisions of a *different* jurisdiction, lower-court decisions, dicta in higher-court decisions, all secondary authority — is at most **persuasive**.

## Hierarchy of primary authority (federal/state US frame, generalised)

Putman & Albright lay out the classical hierarchy. The names change between jurisdictions; the *structure* is universal:

```
Constitution                           ← supreme; everything else must conform
    ↓
Statute / Act of legislature           ← controls unless unconstitutional
    ↓
Regulation / subsidiary legislation    ← controls unless ultra vires
    ↓
Court rules                             ← procedure within the courts
    ↓
Judicial opinions interpreting any of the above
    ↓
Executive / agency decisions
```

Within judicial opinions, the hierarchy of courts inside a single jurisdiction creates a sub-ladder:

```
Highest court (Supreme Court / Court of Appeal as final court)
    ↓
Intermediate appellate court
    ↓
Trial court / High Court at first instance
```

A trial-court decision binds nobody but the parties. An intermediate appellate decision binds lower courts in its hierarchy. A final-court decision binds everyone in that jurisdiction (subject to the doctrine of stare decisis).

## Stare decisis — and its exceptions

Putman & Albright (Chapter 1) define **stare decisis** as "a basic principle of the case law system that requires a court to follow a previous decision of that court or a higher court when the current decision involves issues and facts similar to those involved in the previous decision."

The doctrine is **not absolute.** A court may decline to follow precedent when:

1. The earlier decision has become outdated because of changed conditions or policies
   *Example: Plessy v. Ferguson, 163 U.S. 537 (1896), overruled by Brown v. Board of Education of Topeka, 347 U.S. 483 (1954).*
2. The legislature has enacted legislation that overrules the decision
3. The earlier decision was poorly reasoned or has produced undesirable results

In practice, citing a case as authority requires not just locating the case but verifying it has not been overruled, distinguished into irrelevance, or superseded by statute — see `online-research-workflow.md` on citators.

## Categories of primary authority (with examples retained from Putman)

### Enacted law

- **Constitutions** — supreme; both written (federal/state) and equivalent in non-federal systems
- **Statutes** — Acts of Parliament / Congress; codified into thematic codes
- **Treaties** — once ratified, often co-equal with statute
- **Regulations / Administrative law** — agency rule-making under statutory authority
- **Court rules** — procedural rules adopted by the courts themselves
- **Local ordinances / by-laws** — municipal-level enacted law

### Case law

- **Reported judgments** — full opinions in official or commercial reporters
- **Unreported judgments** — increasingly authoritative as digital repositories standardise
- **Holding** — the binding rule of a case (load-bearing for stare decisis)
- **Dicta (obiter dicta)** — remarks by the court not necessary to the decision; persuasive only
- **Concurring / dissenting opinions** — never binding even from a final-court bench

## Categories of secondary authority

Putman & Albright (Chapters 5–6) list the major secondary sources. The hierarchy of trust within secondary authority follows the credibility-ladder logic from `source-evaluation`:

| Type | When useful |
|---|---|
| Restatements (e.g., US Restatement of Torts) | High-prestige scholarly synthesis; cited routinely |
| Treatises by leading scholars | Foundation reading for a doctrine |
| Law-review articles | Cutting-edge or contested questions |
| Legal encyclopaedias (Am Jur, CJS) | Orientation; never sole authority |
| Practice manuals | Procedural how-to; check date |
| ALR annotations | Map case-law splits across jurisdictions |
| Legal dictionaries (Black's) | Definitional support only |
| Loose-leaf services | Tracking new statutes/regulations |
| Bar-journal articles | Practical commentary |
| Blogs, AI summaries, news articles | Lead generation only — never cite as authority |

## Universal application rules

1. **Identify the governing jurisdiction first.** Authority is jurisdiction-relative. A binding rule in Kenya is at most persuasive in Uganda, and vice versa.
2. **Date-stamp every authority.** Statutes are amended; judgments are overruled. The version cited must be the version in force on the relevant date.
3. **Know whether you have the holding or dicta.** Quote rules at issue, not stray comments by the bench.
4. **Hierarchy beats eloquence.** A two-paragraph holding from the highest court controls; a hundred-page well-reasoned trial-court opinion does not.
5. **Cite primary first; cite secondary only to support a primary argument** (Putman's "always cite primary authority where it exists").
6. **A case is not authority for what it does not decide.** Issues not before the court are not part of the holding.

## Anti-patterns

- Citing a treatise's summary of a case instead of the case itself
- Treating a US case as binding in an East African brief
- Quoting from headnotes or syllabi as if they were the holding
- Treating concurring or dissenting opinions as authoritative
- Citing an encyclopaedia entry without locating its primary footnote
- Confusing a state/regional decision with a federal/national one
- Treating a regulation as in force without checking the gazette/regulations index
- Treating a constitution as static — amendments often affect cited articles
