---
name: academic-citation-styles
description: Use when producing academic outputs (theses, dissertations, papers) that require strict citation discipline. Covers Chicago, APA, MLA, Harvard, and Vancouver styles, in-text citation rules, reference-list ordering, footnote vs endnote vs author-date conventions, and DOI / persistent-identifier hygiene.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Academic citation styles

Academic outputs are judged in part on citation rigour. A great argument with sloppy citations is rejected; a thin argument with clean citations passes peer review. This skill defines the rules.

## Pick the right style

| Style | Field default | Quick sniff |
|---|---|---|
| **APA 7th** | Psychology, education, social sciences, business | (Author, Year, p. nn) in-text |
| **Chicago Notes-Bibliography (NB)** | History, humanities, arts | Footnotes / endnotes + bibliography |
| **Chicago Author-Date** | Sciences using Chicago | (Author Year, nn) in-text |
| **MLA 9th** | Literature, languages, cultural studies | (Author nn) in-text |
| **Harvard** | UK / Australia / Commonwealth defaults across disciplines | (Author Year, p. nn) in-text |
| **Vancouver** | Medicine, biomedical sciences | Numeric superscript¹; numbered reference list |

When the user / target journal hasn't specified, **Chicago Author-Date** is the safest default for mixed-domain research; **APA 7** for social sciences; **Vancouver** for medical / health.

## Universal rules across all styles

- **DOI > URL > nothing.** Always include a DOI when one exists. Use https://doi.org/<doi> form.
- **Date everything.** Year mandatory; month/day where the style asks for it.
- **Page numbers for direct quotes.** Always.
- **Italicise journal / book titles.** Underline only in handwriting.
- **Authors as they appear in the source.** Do not invent middle initials.
- **n.d. for no date** — never omit the date field.
- **Et al. rules vary by style.** Do not assume.

## In-text citation patterns

### APA 7
```
(Author, Year)
(Author, Year, p. 12)
(Author1 & Author2, Year)
(Author1, Author2, & Author3, Year) [first time]
(Author1 et al., Year) [subsequent]
6+ authors → Author1 et al. from first occurrence
```

### Chicago Author-Date
```
(Author Year)
(Author Year, 12)
(Author1 and Author2 Year)
4+ authors → Author1 et al.
```

### Chicago Notes-Bibliography
First note (full):
```
1. Firstname Lastname, Title (City: Publisher, Year), 12.
```
Subsequent (short):
```
2. Lastname, Title, 12.
```
Bibliography entry (note the inversion):
```
Lastname, Firstname. Title. City: Publisher, Year.
```

### MLA 9
```
(Author 12)
(Author1 and Author2 12)
3+ authors → Author1 et al. 12
```

### Harvard
```
(Author, Year, p. 12)
(Author, Year, pp. 12–14)
```

### Vancouver
Superscript number on first cite¹; same number reused for subsequent cites of the same source. Reference list ordered by first appearance.

## Reference list / bibliography ordering

| Style | Order |
|---|---|
| APA, Harvard, Chicago Author-Date | Alphabetical by first-author last name |
| Chicago NB | Alphabetical by first-author last name (same) |
| MLA | Alphabetical by first-author last name |
| Vancouver | Numeric, by order of first citation |

## Common reference formats

### Journal article (APA 7)
```
Author, A. A., & Author, B. B. (Year). Title of article. Journal Title, Volume(Issue), pages. https://doi.org/...
```

### Journal article (Chicago Author-Date)
```
Author, Firstname, and Firstname Author. Year. "Title of article." Journal Title volume (issue): pages. https://doi.org/...
```

### Book (APA 7)
```
Author, A. A. (Year). Title of book (edition). Publisher.
```

### Book (Chicago NB note)
```
Firstname Lastname, Title of Book (City: Publisher, Year), pp.
```

### Edited chapter (APA 7)
```
Chapter author, A. A. (Year). Chapter title. In Editor, A. A. (Ed.), Book title (pp. xx–yy). Publisher.
```

### Court case (Chicago Author-Date — common-law adapted)
```
Case name, citation (Court Year). URL.
```
Example: `Komakech & 7 Ors v Ayaa & Anor, [2018] UGHCCD 54 (High Court of Uganda 2018). https://ulii.org/...`

### Statute
```
Title of Act, Year (Jurisdiction). https://...
```
Example: `Landlord and Tenant Act, 2022 (Uganda). https://ulii.org/en/akn/ug/act/2022/9/eng@2023-12-31`

### Dissertation / thesis (APA 7)
```
Author, A. A. (Year). Title (Doctoral dissertation / Master's thesis, Institution). Database / URL.
```

### Web source (APA 7)
```
Author, A. A. (Year, Month Day). Title of page. Site Name. URL
```

### Newspaper article (APA 7)
```
Author, A. A. (Year, Month Day). Article title. Newspaper Name. URL
```

## Decision rules

- **Pick the style upfront** — switching mid-document creates inconsistencies that reviewers will catch.
- **Use a citation manager when ≥30 sources.** Zotero is free; Mendeley, EndNote, Citavi are alternatives.
- **For pandoc workflows** — use a `.bib` file + a CSL style file (citationstyles.org has 10,000+ free).
- **DOI hygiene** — verify each DOI resolves. A bad DOI is worse than no DOI.
- **Don't cite Wikipedia in academic work.** Use it as a starting point only.
- **Don't cite ChatGPT / Claude / etc. as a source.** Cite the underlying source the LLM was paraphrasing.
- **Self-citation is permitted but should be sparing** — only when it materially supports the argument.

## Anti-patterns

- Mixing styles within one document
- Listing URLs without dates
- Treating "ResearchGate" or "Academia.edu" as the publisher (they are hosts)
- Citing book titles without page numbers when quoting
- Using "Anonymous" instead of the actual lack-of-attribution marker
- Padding reference lists with sources not actually cited (reviewers grep)
- Adding citations after writing — reverse order leads to under-citation

## Pandoc integration

For pandoc-driven .docx generation:
- Citations as `[@key]` in markdown
- `--citeproc` to resolve
- `--bibliography=refs.bib`
- `--csl=apa.csl` (or chicago-author-date.csl, etc.)

```bash
pandoc master.md \
  -o thesis.docx \
  --citeproc \
  --bibliography=refs.bib \
  --csl=chicago-author-date.csl \
  --reference-doc=template.docx \
  --toc --toc-depth=3 --number-sections
```

## See also

- `academic-writing-conventions` — for the structural conventions (lit review, methodology, IRB)
- `evidence-discipline` — anti-hallucination rules apply doubly in academic work
- `source-verification` — tier discipline applies
- `research-report-builder` — Schemas L, N, P (academic variants)
