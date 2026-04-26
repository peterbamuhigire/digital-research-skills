# Reference — MacLeod Search Mastery

**Canonical source:** MacLeod, Don. *How to Find Out Anything: From Extreme Google Searches to Scouring Government Documents, a Guide to Uncovering Anything About Everyone and Everything*. Prentice Hall Press, 2012. Tier 1. Local extract: `extracted-books/macleod-find-anything.txt`.

This reference covers the **general search-craft** layer — operator catalog, search heuristics, the deep web, the reference-interview discipline, and the limits of Google. The **investigative** application of this material (government records, people-finding, company records, FOIA, public records aggregators) lives in `osint-investigation/references/macleod-investigative-search.md`.

## The reference interview — with yourself

MacLeod, Ch 1: "*To become a skilled researcher, step number one is learning how to craft the answerable question.*"

Distil curiosity into a factual, answerable question before touching a search box. The reference interview is a librarian's term for the conversation that converts a vague request into a research-able question. The discipline applies to self-research equally:

1. **What do you already know?** Write it.
2. **What do you not know?** Write it.
3. **What kind of answer would satisfy you?** A number? A name? A date? A document? A judgment?
4. **What category does the question belong to?** Art history, business, legal, scientific. The category points to the right type of source.
5. **What scope are you willing to set?** Finite scope = finite research. Infinite scope = research never ends.

For open-ended questions ("Are CEOs overpaid?"), MacLeod's discipline: convert into 4–6 specific factual questions that, together, build the answer.

## The Google operator catalog (Ch 3)

MacLeod, Ch 3: "*Of all the tools Google provides to help you search the web, none is as powerful or as useful as the site/domain search.*"

| Operator | Syntax | Use case from the book |
|---|---|---|
| Quoted phrase / Verbatim | `"french poodle"`; or use Google Verbatim tool | Disable synonym expansion; force literal match |
| Exclusion | `"avatar" -movie`, `"newt" -gingrich` | Strip ambiguous senses |
| OR / pipe | `"Nikon" \| "Canon" \| "Leica"` | Search alternatives |
| Wildcard | `"King * of Jordan"` | Fill blank in known phrase |
| Brackets (literal) | `[to be or not to be]` | Treat operator-words literally |
| `intitle:` / `inurl:` / `inanchor:` | `intitle:longfellow`, `inurl:chevrolet` | Restrict match location |
| `allintitle:` / `allinurl:` / `allintext:` | `allintitle:Jackson snakes plane` | Multi-term location restriction |
| `site:` (domain or specific URL) | `"diabetes" site:.gov`, `"necklace" site:tiffanys.com` | Most powerful single filter |
| `-site:` | `site:.org -site:.gov` | Exclude domain class |
| `filetype:` | `"Roe v Wade" filetype:pdf`, `filetype:xls`, `filetype:ppt` | Find spreadsheets, decks, court PDFs |
| Numeric range | `"car" "used" $5000..$8000` | Two periods between two numbers |
| Date filter | "More Search Tools" → past hour/day/year/custom | Time-sensitive queries |
| Region / language | Country-code domain or pull-down | Geographic scoping |
| Reading level | Beginner / intermediate / advanced | Filter by sophistication |
| Cache view | "cached" link in result | Retrieve removed/altered pages |
| Similar / linked | "Find pages similar to..." / "links to..." | Lateral expansion |

**Adjacent tool:** Wayback Machine (https://archive.org/) for historical site snapshots back to 1996. Distinct from Google cache (last visit; ~6 months retention).

## The deep web (Ch 2)

MacLeod, Ch 2: "*Searchable databases and their contents are the bread and butter of good research.*"

The deep web — content held inside queryable databases rather than as static pages — is 4–5× larger than the surface (indexable) web. Defaulting to Google for any question structurally excludes most of the deep web.

**Deep-web finders MacLeod recommends:**

- IncyWincy
- INFOMINE — https://infomine.ucr.edu/
- DeepPeep
- Bright Planet

The discipline: when the question is "find me data about X", the right move is often "find the database that holds X" — then go to the database's own search.

## Search heuristics (Ch 1, Ch 2)

- **Categorise the question first** — its category points to the right source type.
- **Never compile information yourself if someone else already has** (Ch 1). Find the existing directory, association, aggregator.
- **Use one fact to find another** — the "detective leverage" principle.
- **Domain-restrict everything** — `site:.gov`, `site:.edu`, `site:.org`, etc.
- **Read internal references, footnotes, blogrolls** — and ask "where else?" of every human source.
- **Double-source every nontrivial claim** — minimum two independent corroborations.
- **Talk to people** — librarians, association staff, bulletin-board experts. Crowdsource via niche forums when web search dries up.
- **Mind the bias of every source** — especially advocacy groups and industry associations.
- **Look in archived/cached versions** when content disappears.
- **Tenacity** — expect dead ends; continue.

## Specialty databases for general research (selected)

For investigative-flavoured databases (government, court, corporate, FOIA, people-finding) see `osint-investigation/references/macleod-investigative-search.md`. The general-research subset:

- **Reference / orientation:** Wikipedia (always footnote-chase, never cite directly), OED.
- **Books:** Google Books, Google Scholar (with caveats — not yet reliable for legal research per MacLeod), HathiTrust, Internet Archive.
- **Scientific:** Google Scholar, PubMed, JSTOR, arXiv, BioRxiv.
- **News archives:** NewspaperArchive, Newspapers.com, ProQuest Historical Newspapers, Google News Archive (where still available).
- **Image archives:** Library of Congress, Smithsonian, Getty Open Content, Wikimedia Commons.
- **Computational reference:** Wolfram|Alpha — for timelines, lifespan charts, computed answers.
- **Time-machine:** Wayback Machine (archive.org).

## Anti-patterns

MacLeod calls these out repeatedly:

- Defaulting to a Google keyword search for any question, including ones Google structurally can't answer.
- Stopping at the top-20 results and treating them as authoritative ("infobesity," James Morris's term, cited Ch 1).
- Treating ranked results as judged content rather than crowd-sourced suggestions.
- Searching open-ended questions ("Are X overpaid?") rather than the factual cascade beneath them.
- Skipping Advanced Search — fewer than 5% of users (including Google staff) use it.
- Trusting Yahoo! Answers, content farms, and Wikipedia uncritically.
- Ignoring the deep web (4–5× larger than surface web).
- Not using `site:` filters to escape SEO-spam clutter.
- Never picking up the phone.
- Not keeping notes — lost URLs become re-search work.
- Confusing Google cache (last visit) with the Wayback Machine (historical archive).
- Assuming a name is unique or correctly spelled.

## Quotable passages

1. "Research is the process of finding out for yourself what somebody else already knows." (Ch 1)
2. "To become a skilled researcher, step number one is learning how to craft the answerable question." (Ch 1)
3. "Never compile information yourself if someone else has already done it." (Ch 1)
4. "Skepticism (not cynicism) is the ally of the researcher." (Ch 1)
5. "Google is the Schrödinger's cat of search engines — it's simultaneously the greatest boon to online research ever invented and the archnemesis of effective information gathering." (Ch 2)
6. "Searchable databases and their contents are the bread and butter of good research." (Ch 2)
7. "Of all the tools Google provides to help you search the web, none is as powerful or as useful as the site/domain search." (Ch 3)

## Companion references

- `references/search-operator-grammar.md` — engine's own operator grammar (the MacLeod material here is the canonical source for it).
- `references/reference-interview.md` — the engine's reference-interview procedure (extends MacLeod's "interview yourself" discipline).
- `references/russell-search-literacy.md` — Daniel Russell's metacognitive layer, complementary to MacLeod's structural layer.
- `osint-investigation/references/macleod-investigative-search.md` — the investigative application of this material.

## Sources

- MacLeod, Don. *How to Find Out Anything*. Prentice Hall Press, 2012. Tier 1.
