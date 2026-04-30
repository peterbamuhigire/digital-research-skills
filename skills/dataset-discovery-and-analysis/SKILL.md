---
name: dataset-discovery-and-analysis
description: Use whenever a research project would benefit from public datasets — finds them across government / IGO / academic / ML hubs, retrieves with integrity checks, and produces a Segnini-style five-step quality profile (completeness, duplicates, accuracy, integrity, codes). Backed by tools/datasets/.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Dataset discovery and analysis

<!-- dual-compat-start -->
## Use When

- Use when a research project needs public datasets, official statistics, replication
  data, ML datasets, or dataset profiling.

## Do Not Use When

- Do not use when the task only needs literature or narrative sources.

## Required Inputs

- Research question, geography, period, discipline, preferred source types, and required
  output.

## Workflow

- Discover, retrieve, profile, cite, and hand off datasets using the three-step process
  below.

## Quality Standards

- Prefer official or primary datasets, record version/licence/SHA-256, and profile before
  analysis.

## Anti-Patterns

- Do not cite a chart without tracing the underlying dataset.

## Outputs

- Dataset shortlist, retrieved dataset, profile, quality notes, or citation-ready source
  record.

## References

- Use the tools and companion skills listed below for retrieval, profiling, and evidence
  discipline.

The engine should treat **public datasets as a first-class source type** alongside academic papers and journalism. Most research projects can be sharpened with a directly-cited dataset.

## Three steps

### 1. Discovery — `tools/datasets/search.py`

Federated search across the registered hosts:

```python
from tools.datasets import search_datasets, DATASET_REGISTRY

for r in search_datasets("rental housing Kenya", per_host=10, coverage_filter="kenya"):
    print(r.host, r.title, r.url, r.formats)
```

**Decision rules:**
- Always search both **government open-data portals** (data.gov, KNBS, UBOS, NBS, NISR, Eurostat) and **IGO bodies** (World Bank, IMF, OECD, WHO, UNICEF, FAOSTAT) for any cross-border quantitative question.
- Use **Zenodo / Dataverse / Figshare** for academic / replication datasets.
- Use **HuggingFace Datasets / Kaggle** for ML / pre-cleaned datasets.
- Combine with `discipline-router` — different research disciplines have different canonical hosts.

### 2. Retrieval — `tools/datasets/retrieve.py`

```python
from tools.datasets import retrieve_dataset

result = retrieve_dataset(
    "https://data.knbs.or.ke/dataset/.../household-survey.csv",
    dest_dir="projects/<project-id>/data",
    sha256_expected="abc123...",  # optional integrity check
)
```

- Goes through the engine's `tools/scraping/http_client` for retries + ethics.
- Computes SHA-256 for integrity / re-use detection.
- Detects format from extension + content-type (CSV / Parquet / Excel / NetCDF / etc.).
- Caches on disk; re-runs are free.

### 3. Analysis — `tools/datasets/analyse.py`

```python
from tools.datasets import profile_dataset

prof = profile_dataset("projects/<project-id>/data/household-survey.csv")
print(prof.n_rows, prof.n_columns, prof.duplicate_rows)
for col in prof.columns:
    print(col.name, col.null_rate, col.dtype)
print(prof.quality_flags)  # warnings per Segnini's checklist
```

The profile applies Segnini's **five-step verification** (Verification Handbook):
1. **Completeness** — null-rate per column with warning threshold
2. **Duplicates** — duplicate-row count
3. **Accuracy** — min/max/mean/std for numeric columns; extreme-value spot-check
4. **Integrity** — sample values surfaced for human review
5. **Codes / acronyms** — build a glossary if columns use codes

## Decision rules

- **Always profile before analysing.** Treat the profile as the dataset's `five-term-source-doubt` equivalent.
- **Document SHA-256 in the source citation.** Datasets change; lock the exact version you used.
- **Prefer official portals over secondary aggregators.** KNBS direct beats data.gov mirror of KNBS.
- **License is part of the source citation.** Note CC-BY-4.0 / OGL / etc. in `<cohort>/research/sources.md`.
- **When the dataset is large and you only need a slice**, pull the slice via API rather than downloading the full dataset.
- **Cite the dataset, not the visualisation.** A chart in a news article cites the underlying dataset; trace it.
- **Classify the analytics question before analysis.** Name whether the dataset is being
  used for descriptive, diagnostic, predictive, or prescriptive claims, then pair with
  `data-quality-pipeline/references/analytics-quality-method-gate.md` before modelling or
  publishing figures.

## Integration with other skills

| Pair with | Why |
|---|---|
| `evidence-discipline` | Dataset claims must be traceable to source dataset version |
| `source-verification` | Datasets are typically Tier 1 (official) or Tier 2 (regulator) |
| `discipline-router` | Discipline determines which dataset hosts to prioritise |
| `regulatory-landscape-mapping` | Government datasets often back regulatory analysis |
| `crosswalk-matrix` | Datasets occupy a column in the matrix |
| `research-report-builder` | Methodology section names the dataset + version + license |

## Anti-patterns

- Citing a chart without finding the underlying dataset
- Downloading without recording SHA-256 — dataset versions drift silently
- Skipping the profile step — null rates and duplicates are real findings
- Assuming the dataset's column meaning matches your assumption (always read the codebook)
- Using a stale cached version when the source has updated
- Ignoring the license on republication

## East African dataset anchors

- **KNBS** (Kenya National Bureau of Statistics) — Census, KIHBS, KCHS
- **UBOS** (Uganda Bureau of Statistics) — UDHS, UNHS
- **NBS Tanzania** — HBS, DHS
- **NISR Rwanda** — EICV, DHS
- **Africa Open Data** — pan-African aggregator
- **World Bank Open Data** — best for cross-country comparison
- **Humanitarian Data Exchange (HDX)** — crisis / refugee data, including East African flows

## See also

- `tools/datasets/registry.py` — full host list with API URLs
- `tools/datasets/search.py` — federated search
- `tools/datasets/retrieve.py` — download with integrity
- `tools/datasets/analyse.py` — profiling
- `evidence-discipline` — every dataset citation must include version + URL + license + access date

<!-- dual-compat-end -->
