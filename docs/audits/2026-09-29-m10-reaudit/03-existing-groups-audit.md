# 03 Existing groups and sampled skills

All scores are judged. Groups are the auditor's working assignment of all 59 skills (see 02).
Group scores weigh the sampled skills, catalogue-wide scan counts and reference depth. Skills that
were not sampled are not scored individually.

## Catalogue-wide scan facts (heuristic, all 59 skills)

- **Contract validator:** 59/59 fully compliant locally (measured). CI reports 57/59.
- **Worked examples:** every skill has a worked-example section, but 56 of 59 are under 60 words.
  Only `excel-spreadsheets` (223 words), `professional-word-output` (91) and
  `python-document-generation` (72) exceed that.
- **Duplicate H2 sections:** 19 skills, for example `decision-support-analysis` has two
  "Companion Skills" headings, the first empty.
- **Generated sub-headings:** 39 skills carry "Notes", "Guidance" or "Detail" headings, such as
  "Quantitative Modelling Evidence Notes 2". The count is heuristic and includes some legitimate
  headings.
- **No references directory content:**
  - `ai-slop-audit`
  - `anti-ai-slop`
  - `east-african-english`
  - `manual-guide`
  - `markdown-lint-cleanup`
  - `project-requirements`
  - `skill-safety-audit`
  - `spec-architect`
  - `dataset-discovery-and-analysis` (0 files under `references/`)
  - `scraping-engineering-python` (0 files under `references/`)
- **Absolute workstation paths (`C:/wamp64`):** four files —
  - `skill-safety-audit/SKILL.md:97`
  - `skill-taxonomy-and-routing/SKILL.md:104`
  - `skill-writing/SKILL.md:13`
  - `source-evaluation/references/book-driven-source-admission-and-currentness.md:19`
- **Fan-in (`skill_fanin.py`, measured):** zero inbound skill links for `00-meta-initialization`
  (reached via the router), `capability-matrix` and `skill-taxonomy-and-routing`. 29 skills have
  no routing fixture.

## Group scores

| # | Group (skills) | Score | Justification |
|---|---|---:|---|
| G1 | Source discipline and validation (5): `source-evaluation`, `source-verification`, `evidence-claim-graph`, `data-quality-pipeline`, `validation-contract` | 60 | The core of the engine: 10 references in source-evaluation, a verifier tool, support-state contract fixtures and an untrusted-source contract. Held back by one-sentence worked examples, `source-verification` repeating its inputs, anti-patterns and workflow twice, and `validation-contract` being a 1.0-cosine duplicate of dev |
| G2 | Research design and execution (6): `00-meta-initialization`, `research-design`, `research-techniques`, `research-orchestration`, `primary-research`, `agentic-research-operations` | 56 | Wave model, type, discipline and reading-mode routers, sequential fallback, 10–11 references in design and techniques. No filled wave plan or graded synthesis exemplar. An SEO article standard sits oddly inside orchestration. Companion names are stale |
| G3 | Investigation and collection (6): `due-diligence`, `osint-investigation`, `pi-investigation`, `online-legal-research`, `web-scraping-foundations`, `scraping-engineering-python` | 57 | Deepest reference layer (OSINT 11, DD 7, legal 5), CARA, a strong refusal list, sanctions tests and a scraping CLI with tests. The legal overlay lists categories only. The DD worked output is a three-line fixture. The Berkeley Protocol is cited only in the triage reference |
| G4 | Data, analysis and synthesis (10): `dataset-discovery-and-analysis`, `quantitative-modelling`, `analytic-tradecraft`, `calibration-and-forecasting`, `critical-reasoning-and-argument`, `mind-mapping-and-synthesis`, `systems-thinking-and-mental-models`, `decision-support-analysis`, `peer-review-loop`, `knowledge-mining` | 50 | Tradecraft (ACH, KAC, estimative language) and forecasting method are sound, and the dataset tools are real code. Quantitative modelling is thin (one reference, no sizing example). Several skills are mostly generated contract sections with little method beyond the headings |
| G5 | Academic and regional (6): `academic-writing`, `academic-reporting-standards`, `dissertation-writing-process`, `kenya-academic-research`, `uganda-academic-research`, `east-african-english` | 52 | EQUATOR routing, rigour-level defaulting for literature review, 17 references in academic writing. TOP is stated in its superseded form. Rich-institution conventions (Oxbridge and Ivy) dominate, while regional skills are 116–117 lines with one reference each |
| G6 | Communication and deliverables (12): `research-output-formats`, `analytical-report-shapes`, `report-and-proposal-craft`, `business-writing`, `executive-communication`, `consulting-delivery`, `knowledge-productization`, `python-document-generation`, `professional-word-output`, `excel-spreadsheets`, `anti-ai-slop`, `ai-slop-audit` | 50 | Largest group, with real generation code and the only worked examples over 60 words. Two members break CI through cross-repository links. `ai-slop-audit` duplicates dev and srs. Much of this belongs with the design and dev engines |
| G7 | Engine and agent practice (7): `skill-taxonomy-and-routing`, `skill-writing`, `skill-safety-audit`, `skill-composition-standards`, `ai-evaluation-and-data-flywheel`, `capability-matrix`, `doctrine-spine` | 42 | Only `ai-evaluation-and-data-flywheel` is research-specific, and its pilot is "design only; no labelled pilot cohort". The others are dev-engine material, one retired there, with absolute paths |
| G8 | Engineering and documentation imports (7): `spec-architect`, `project-requirements`, `systems-process-requirements`, `doc-architect`, `update-claude-documentation`, `markdown-lint-cleanup`, `manual-guide` | 32 | No research function. `project-requirements` (485 lines) and `update-claude-documentation` (444 lines, with product-specific residue) are long, but they are out of scope and duplicate engineering-engine capability |

## Sampled skills

| Skill | Score | Refs | Worked example | Doctrine cited | Depth note |
|---|---:|---:|---|---|---|
| `source-evaluation` | 63 | 10 | One sentence | Yes | Strong router across source types and a universal ship gate. The "Studies older than 3 years" rule is blunt. A stale `data-quality-assessment` companion |
| `source-verification` | 58 | 4 | One sentence | Yes | Support-state contract and untrusted-source rules are good. The body repeats the same five anti-patterns three times |
| `osint-investigation` | 60 | 11 | One sentence | Yes | Best refusal boundary in the engine. No filled case-vault or chronology exemplar |
| `due-diligence` | 57 | 7 | One sentence (the reference has a code sketch) | Yes | CRAWL and CARA, and a sanctions discipline. The only "dossier" example is a fixture |
| `online-legal-research` | 54 | 5 | One sentence | Yes | Method, IRAC and the currency rule are sound. Source books are US-based. The EA overlay lists categories only, with no repository access log. Degraded and evidence sections are duplicated |
| `research-orchestration` | 56 | 5 | Short | Yes | Wave model and routers. No filled brief or wave-plan exemplar |
| `academic-reporting-standards` | 55 | 7 | Short | Yes | Rigour defaulting and EQUATOR routing. TOP is superseded. The "600+ journals" endorsement figure is not dated |
| `dataset-discovery-and-analysis` | 55 | 0 | Short | Yes | Backed by real `tools/datasets` code. The drift warning is honest. No references directory content |
| `analytic-tradecraft` | 58 (partial read) | 6 | Short | Yes | SATs and estimative language present |
| `calibration-and-forecasting` | 50 | 2 | Scenario sentence | Yes | Sound method. Brier or other scoring is not specified in the SKILL body. Generated headings throughout |
| `decision-support-analysis` | 48 | 2 | One sentence | Partial | Reasonable options method. An empty duplicate "Companion Skills" heading |
| `quantitative-modelling` | 42 | 1 | One sentence | Partial | Seven-step method only. No TAM/SAM/SOM, top-down or bottom-up worked model, or unit-reconciliation example. "Evidence Notes 1/2" padding |
| `ai-evaluation-and-data-flywheel` | 46 | 3 | Short | Yes | Sound loop. The pilot protocol is design only, with no labelled cohort |
| `validation-contract` | 35 | 4 | Short | n/a | Identical to the dev skill (cosine 1.0) |
| `skill-safety-audit` | 38 | 0 | Short | n/a | Retired in dev, still active here, with an absolute `C:/wamp64` path |
| `capability-matrix` | 30 | 2 | Short | n/a | Technology-stack lookup naming design and engineering skills; zero inbound links |
| `update-claude-documentation` | 30 | 1 | Short | n/a | Out of domain; carries product-specific residue |

Frontmatter only was read for `spec-architect` and `project-requirements`. They are covered in the
G8 score, not scored individually.
