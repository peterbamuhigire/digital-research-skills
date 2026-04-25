---
name: citation-brachiation
description: Use when traversing the citation graph in either direction — backward to references, forward to cited-by, sideways via shared references. Encodes Andrew Abbott's "brachiation" technique with vintage-aware index-term back-translation. Cross-cited by Abbott (Digital Paper), Bell (Librarian's Guide), and Rowland (Creative Guide).
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Citation brachiation

Brachiation: the motion of apes swinging through trees. Abbott's coinage for hopping primary source → reference list → index → another primary source via citations rather than searches. Two qualities make it powerful:

1. **Back-and-forth-ness** — going against the indexer's grain. Use known-good papers' references to discover the *right* indexing terms for the period, then use those terms to find more known-good papers.
2. **Free-riding on certified experts** — start in a source already produced by a high-quality bibliographer. Saves you from having to evaluate every candidate from scratch.

## Three traversal directions

### Backward (B → A): the references of a known paper
- Read paper B's reference list
- Identify cited papers A by relevance and recency
- Pull the full text of high-priority A papers
- Extract their references; walk one more layer if useful

### Forward (B → C): who cites a known paper
- "Cited by" search on Google Scholar / Web of Science / Scopus
- Bounded by date — papers before B can't cite B
- High citations to B = B was important; high citations *of B* in any specific later paper = that paper engaged seriously
- Use to discover **how the field absorbed B** and to find the most recent advances

### Sideways (B ↔ D via shared references): bibliographic coupling
- Two papers that share many references are likely on similar topics, even if their topic words differ
- Web of Science exposes this directly via "Related Records"
- "About as close to searching by concept as opposed to searching by words as you can get" (Bell)

## Decision rules

- **Always do at least one backward and one forward pass** on any seminal source for a project.
- **Vintage-aware index-term back-translation.** Subject headings drift over decades. If pre-1980 work uses a term different from the current standard, search using both. Bell: pre-1965 Black history is filed under "Negroes," 1965–1985 under "Afro-Americans," post-1985 under "African Americans." Use the right vintage for the right epoch.
- **Free-ride on certified bibliographers.** Reference lists in *Annual Review of X*, in highly-cited review papers, and in dissertations are vetted bibliographies. Use them.
- **Don't trust user-provided citations verbatim.** Bell's Reference Desk Rule No. 1: "citations are never quite accurate." Always plan for citation cleanup before counting "times cited" or claiming authority.
- **Stop when you start seeing the same papers** in three consecutive walks — the cluster is mapped.
- **Cite-rank as proxy** for importance is reliable **only early in a project**. Late in a project, your domain judgement should override.

## Standard tools

- **Google Scholar** — free; "cited by" link; PDF surfacing
- **Web of Science** — paid; cleanest forward citations + Related Records (bibliographic coupling)
- **Scopus** — paid; alternative forward citations
- **Connected Papers** — visualises citation graph
- **Inciteful** — free Connected-Papers alternative
- **Semantic Scholar** — free; AI-assisted summaries

## Citation disambiguation

Authors cite messily. Bell shows 30+ printed variants of "Watson, Double Helix, 1968." Before counting citations or asserting authority, normalise:

- Author name variants (initials vs first name; last-first vs first-last)
- Title abbreviations
- Year drift (preprint year vs publication year)
- Page-number errors

Run a citation-disambiguation pass before any "times cited" claim makes it to a report.

## Anti-patterns

- Searching by topic words alone in a domain where citation graphs already exist
- Treating recency as quality (high-cite-count old papers still matter)
- Citing the second-hand reference rather than the original
- Ignoring vintage-shift in subject headings
- Trusting a single citation database for forward citations (overlap is partial)

## See also

- `academic-source-mining` — uses brachiation as one of its standard moves
- `pearl-growing-iteration` — citation walks generate vocabulary for refined searches
- `source-verification` — Tier-1 sources especially benefit from forward-citation cross-check
- `citation-disambiguation` (roadmap) — pre-count normalisation
