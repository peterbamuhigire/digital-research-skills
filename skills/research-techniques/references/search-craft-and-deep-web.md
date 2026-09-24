# Search Craft and the Deep Web

Use this guide when a research question must be turned into searches: framing an answerable
question, choosing between a web search engine and a database, composing operators, and
recovering content that has moved. The metacognitive layer (when to reframe, when to stop, how
to verify) is in `search-metacognition-and-verification.md`; the operator grammar is in
`search-operator-grammar.md`; the investigative application (registries, courts, people,
companies) is in `../../osint-investigation/references/public-records-investigative-search.md`.

## Inputs

- The request as the user phrased it.
- What is already known and what form of answer would satisfy (number, name, date, document,
  judgment).
- Jurisdiction, language and time window.
- Access: subscriptions, library credentials, budget for paid databases.

## Decision rules

1. **Make the question answerable before searching.** Write down what you know, what you do not,
   what answer would satisfy, which domain the question belongs to (law, finance, health,
   history), and the scope. An open-ended question ("Are Kenyan bank CEOs overpaid?") becomes four
   to six factual questions (pay disclosed in annual reports, peer pay, performance, pay
   regulation) whose answers build the judgment. Run `reference-interview.md` when the request
   comes from someone else.
2. **Find the compiler before compiling.** Someone has often already built the list, directory,
   dataset or index: an association, regulator, statistics office, library guide. Search for the
   compilation first.
3. **Database questions go to databases.** Much valuable content sits inside searchable
   databases (registries, catalogues, court systems, statistical portals, journal indexes) that
   general search engines index poorly or not at all. When the question is "find data about X",
   first find the database that holds X, then use its own search.
4. **Restrict by source class.** Domain and site restriction (government, academic, a named
   regulator) cuts spam and raises source tier faster than adding keywords.
5. **Use one fact to find the next.** A registration number, a director's name or an old address
   unlocks the next source.
6. **Double-source every non-trivial claim** with two independent sources; see
   `../../source-evaluation/SKILL.md`.
7. **Talk to people when the web runs dry.** Librarians, association staff, registry clerks and
   specialist forums often answer in minutes what searching cannot.

## Procedure

1. Frame the answerable question and its sub-questions (rule 1).
2. Classify each sub-question: open web, specialist database, archive, or human source.
3. For open-web sub-questions, compose queries with operators (below) and restrict by domain.
4. For database sub-questions, identify the database, read its search help, and use its fields
   (author, date, jurisdiction, document type).
5. Harvest vocabulary from good early hits (technical terms, official names, document types) and
   re-query with it (`../../academic-writing/references/pearl-growing.md`).
6. Record every query, source, date accessed and result in the research log so the search can be
   repeated.
7. Stop when the original written question is answered or the stop rule in
   `search-metacognition-and-verification.md` triggers.

## Operators and tools (check at task time)

Google Search Central's operator documentation (accessed 2026-09-24) documents `site:`,
`filetype:`, and, for image search, `imagesize:` and `src:`. Other widely used forms (quoted
phrases, `-` exclusion, `OR`, `intitle:`, `inurl:`, `before:` and `after:`) work but are not
formally documented and may change; test them before relying on them in a repeatable protocol.

| Need | Pattern | Note |
|---|---|---|
| Exact phrase | `"land registry backlog"` | Also switch results to verbatim where the engine offers it |
| Exclude a sense | `jaguar -car` | |
| Alternatives | `"URSB" OR "Registration Services Bureau"` | |
| Domain class or site | `site:go.ug`, `site:ac.ke`, `site:bou.or.ug` | The single most effective filter |
| Exclude a domain | `site:.org -site:wikipedia.org` | |
| File type | `"annual report" filetype:pdf site:co.ke` | Finds reports, spreadsheets, slide decks |
| Title or URL | `intitle:tender`, `inurl:gazette` | Undocumented; verify behaviour |
| Date window | Tools menu date filter, or `before:` / `after:` | Essential for time-sensitive facts |

**Retired features.** Google's cached-page link and the `cache:` operator were retired in 2024;
use the Internet Archive's Wayback Machine (web.archive.org) or archive.today for earlier
versions of a page, and record the snapshot URL and timestamp. Do not cite a live page for a
claim about its past content.

**Beyond general search.** Discipline databases (PubMed, JSTOR, Scopus, African Journals Online),
Google Scholar and Google Books for literature; national statistics offices and central banks
for data; Wikipedia only as a map to its cited sources, never as the citation; Wolfram|Alpha for
computed facts. Old "deep-web finder" directories named in older manuals have largely gone
offline; do not recommend a finder service without checking it is live.

## Failure modes

Keyword-searching a question a database would answer · treating the top ten results as the
authoritative set · searching the open-ended question instead of its factual parts · no domain
restriction · uncritical use of content farms and answer sites · assuming a name is unique or
correctly spelt · no research log, so good sources are lost · citing a live page for what it
said last year · never asking a person.

## Original worked example

Question: "How many licensed microfinance deposit-taking institutions operate in Uganda, and
has the number changed since 2020?"
- Compiler first: the Bank of Uganda publishes the list of supervised institutions. Query:
  `site:bou.or.ug "microfinance deposit-taking institutions" list`.
- Change over time: earlier lists recovered through Wayback Machine snapshots of the same page;
  snapshot URLs and dates logged.
- Cross-check: the central bank's annual supervision report (filetype:pdf) for the year-end
  count. Two independent official artefacts agree, or the discrepancy is reported.

## Checklist

- [ ] Question rewritten as answerable sub-questions.
- [ ] Existing compilations searched first.
- [ ] Database sub-questions sent to databases.
- [ ] Operators tested; domain restriction used.
- [ ] Archived versions cited with snapshot URL and timestamp.
- [ ] Query log complete and repeatable.
- [ ] Non-trivial claims double-sourced.

Evidence and currentness: Google Search Central, "Search operators" pages
(developers.google.com/search/docs/monitor-debug/search-operators), accessed 2026-09-24.
Retirement of the cache link and `cache:` operator in 2024 is reported by Google's Search
Liaison and trade press (Search Engine Land, Search Engine Journal); Google's own changelog entry
was not re-read here: NOT_ASSESSED. Behaviour of undocumented operators: NOT_ASSESSED at the time
of any given task.

Sources: MacLeod (2012) *How to Find Out Anything*; Bell (2015) *Librarian's Guide to Online
Searching*; Google Search Central documentation. Reorganised by task.
