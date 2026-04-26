# Web search operator grammar

Most engine searches are too broad, too narrow, or off-target because the operator layer is left to default. This skill encodes the operator stack as a layered query-build pipeline.

## Four operator layers (build queries in this order)

### 1. Punctuation operators
- `"exact phrase"` — preserves word order; **only way** to keep stop-words
- `-term` — exclude (e.g. `banana -bread`)
- `*` — wildcard for half-remembered phrases (`"a * is worth a thousand words"`)
- `..` — numeric range (e.g. `2018..2024`)
- `$` — price (`camera $200`)
- `#` — hashtag

### 2. Field operators
- `site:domain` — restrict to a single site / TLD (`site:gov.ke`, `site:.edu`)
- `intitle:term` — must appear in the page title (precision)
- `inurl:term` — must appear in URL
- `intext:term` — must appear in body

### 3. Refinement operators
- `filetype:pdf` — restrict to file format (also `xlsx`, `docx`, `csv`, `pptx`)
- `related:url` — find similar pages
- `cache:url` — Google's cached copy (recovery for slow/dead pages)
- `link:url` — pages linking to URL (deprecated for Google but works elsewhere)

### 4. Boolean operators
- `OR` / `|` — synonym sets `(homeless OR unhoused OR rough-sleeping)`
- `AND` — implicit on most engines; explicit when stacking with OR
- `NOT` / `-` — exclusion (avoid `NOT` in **commercial databases** per Bell — too risky in indexed sources)

## The canonical query template

```
"<core phrase>" (synonym1 OR synonym2) -<excluded sense>
   site:<institutional domain> filetype:<grey-lit type>
   intitle:<must-appear-in-title>
```

## Decision rules

- **Default to phrase-quote** any multi-word concept first
- **Combine `site:` + `filetype:pdf`** for institutional grey literature (theses, reports, regulator filings)
- Use **`intitle:`** when topic centrality matters more than recall
- Use **`*`** to recover citations or quotes from memory
- **Don't use `NOT` in commercial databases** — too risky to over-exclude; AND-in another term instead
- **Phrase-quote is NOT just for accuracy** — it's the only way to force inclusion of stop-words like *or*, *it*, *the*

## Engine-specific syntax differences

| Operator | Google | Bing | DuckDuckGo | Brave | Kagi |
|---|---|---|---|---|---|
| `site:` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `filetype:` | ✓ | `ext:` | ✓ | ✓ | ✓ |
| `intitle:` | ✓ | `intitle:` | ✓ | ✓ | ✓ |
| `cache:` | ✓ (limited) | ✗ | ✗ | ✗ | ✗ |
| `related:` | ✓ | ✗ | ✗ | ✗ | ✗ |
| `..` | ✓ | ✓ | ✗ | ✓ | ✓ |
| `*` wildcard | ✓ | ✓ | ✗ | ✓ | ✓ |

For commercial databases (EBSCO, ProQuest, WoS, PubMed, Factiva, LexisNexis), see the **vendor-syntax-adapter** skill (roadmap) which has its own operator family.

## Anti-patterns

- Treating the search engine as the Web (it indexes a sample, not the whole)
- Adding more terms when a search returns too few — **broaden, don't narrow**
- Quoting freely without realising you've over-constrained word order
- Using a single engine for breadth claims — index overlap is partial; combine 2+ for breadth
- Stripping stop-words assuming the engine will keep them (Google drops them unless quoted)
- Trusting search-engine answer cards as primary — they paraphrase

## Answer-card-first routing

Many factual lookups don't require page retrieval. Recognise queries served by the engine's answer card:
- Calculator (`12 * 0.075`)
- Conversions (`100 USD to KSH`)
- Definitions (`define: kintsugi`)
- Stock prices, weather, sunrise/sunset, flight status
- Sport scores
- Translations (`translate hello to swahili`)

These return without a page fetch — saves tokens and latency in agent loops.

## See also

- `pearl-growing-iteration` — the iteration loop on top of these operators
- `discipline-router` — picks which engine + operator family to use
- `vendor-syntax-adapter` (roadmap) — same idea for commercial DBs
- `evidence-discipline` — operator output still needs verification
