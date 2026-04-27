# Online legal research workflow

**Date written:** 2026-04-27
**Drawn from:** Putman & Albright, *Legal Research, Analysis and Writing*, Chapters 7–8 (computers and internet legal research); Long, *Legal Research Using the Internet*; *Legal Research* (anonymous compendium).

This reference is the operator's manual for actually finding the law online. It teaches **search strategy**, **citator logic**, and the **division of labour between free and paid databases** — without prescribing tools the engine cannot independently verify exist.

## The decision tree before you search

Before issuing a single query:

1. **Stated jurisdiction(s)** — which legislatures, courts, and regulators can possibly bind the answer?
2. **Date window** — what events triggered the question, and what version of the law applied at that time?
3. **Question type** — statutory interpretation? case-law application? regulatory compliance? procedural? constitutional?
4. **Type of authority needed** — primary first, secondary as scaffolding
5. **Search vocabulary** — what *terms of art* are used in this area of law? (Putman: "the wrong word kills the search")

A search begun without these four answers tends to produce noise.

## Search-strategy patterns

### Boolean operators (universal across legal databases)

| Operator | Effect | Example |
|---|---|---|
| `AND` | Both terms must appear | `negligence AND foreseeability` |
| `OR` | Either term | `tenant OR lessee` |
| `NOT` / `AND NOT` / `BUT NOT` | Exclude | `easement NOT prescriptive` |
| `" "` | Phrase search | `"right to be forgotten"` |
| `*` (or `!`) | Truncation / wildcard | `negligen*` → negligent, negligence, negligently |
| Proximity (`/n`, `w/n`) | Within n words of | `landlord /5 negligence` |
| Field/segment | Restrict to part of document | `caption("Roe v. Wade")`, `judge(Mukasa)` |

Different databases use different syntax — but every serious legal database supports the *concepts*. Verify the exact syntax for the database in use before issuing the query.

### Natural-language vs Boolean

Most modern legal databases offer both:

- **Natural language** — type a question; engine ranks results by relevance. Best for first-pass orientation when you don't know the terms of art.
- **Boolean / terms-and-connectors** — explicit operator-driven query. Best for precision once you know the terms of art and want comprehensive recall.

Putman's recommendation: start in natural language to find the vocabulary, then refine with Boolean for precision.

### Field/segment searches

Restrict matching to specific parts of a document — judge name, court, date, jurisdiction, statute section. Field searches are how a researcher filters from "100,000 hits" to "23 hits" without losing the ones that matter.

### Iteration discipline

Save every successful search query. Re-run them after the initial pass to capture new judgments published since.

## Citator logic — validating currency

Putman & Albright (Chapter 5) and the anonymous *Legal Research* devote sustained attention to citators. The two market-leading systems are **Shepard's** (LexisNexis) and **KeyCite** (Westlaw). Other jurisdictions have their own analogues. The *concept* is universal:

> A citator answers the question: **"Has this authority been treated by later courts? If so, how — followed, distinguished, criticised, overruled?"**

### Universal citator workflow

For every cited case:

1. Look up the case in the citator
2. Read the **status flag** — is the case still good law, partly bad, or fully overruled?
3. Read the **subsequent treatment** — list of later cases citing it, classified as *followed*, *distinguished*, *criticised*, *limited*, *overruled in part*, *overruled*
4. Read the **prior history** — was this case appealed up or down?
5. If the case was overruled or substantively criticised, **find the overruling case and read it**
6. Record the currency check in the project manifest with date

For every cited statute:

1. Confirm the section number is current (statutes are renumbered after amendments)
2. Confirm the text quoted matches the in-force version on the relevant date
3. Pull the consolidated/annotated version where possible
4. If amended, locate the amending Act and check the commencement provisions

A claim that survives the citator check is **good law as of the check date.** A claim that hasn't faced the citator is **unverified** and not safe to ship.

## Free vs paid databases — division of labour

Putman acknowledges that not every researcher has Westlaw or Lexis. The discipline doesn't change with the tool — only the convenience.

| Use free repositories for | Use paid databases when available for |
|---|---|
| Locating the text of statutes and reported judgments | Citator services (Shepard's / KeyCite) |
| First-pass case-law searches | Comprehensive subsequent-treatment trails |
| Confirming case names and parties | Editorial annotations, headnotes, key-number digests |
| Reading the judgment in full | Cross-database link integration |
| Triangulating against secondary commentary | Time-of-search snapshots for malpractice trails |

**The methodology floor is the same regardless.** Free repositories like government court websites, gazette archives, and academic open-access repositories contain primary authority. The work of confirming currency, however, may require either a paid citator or manual checking against later judgments and gazette amendment indexes.

## A repeatable seven-step search routine

1. **Frame the issue** in two sentences (Issue from IRAC).
2. **List terms of art** likely to appear in the law of this issue.
3. **Pick the jurisdiction(s)** and date window.
4. **Run a natural-language pass** to discover dominant terms and leading cases.
5. **Refine with Boolean** to capture comprehensive results.
6. **Triangulate** with at least one secondary source (treatise, journal article, encyclopaedia) to confirm you have the leading authorities.
7. **Run citator on every case kept** and check statute/regulation currency.

Document each step in the project's `research/` log so the audit trail is reproducible.

## Anti-patterns

- Searching only on the words the *client* used (legal terms of art often differ from lay vocabulary)
- Stopping at the first relevant case instead of canvassing the field
- Reading headnotes instead of the judgment
- Skipping the citator because "the case looks fresh"
- Relying on AI-generated case names without verification — see `source-evaluation/references/evidence-discipline.md`
- Confusing search-engine rank with legal authority weight
- Treating an open-web hit (blog, summary, AI-rewrite) as a substitute for the judgment text
- Failing to record the search query and date — destroys reproducibility
