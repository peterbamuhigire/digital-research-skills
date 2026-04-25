# Codex / generic-agent — dataset-discovery-and-analysis

```yaml
dataset_search:
  query: "..."
  hosts: [...]              # subset of DATASET_REGISTRY
  per_host: <int>
  coverage_filter: "..."    # optional

dataset_retrieve:
  url: "..."
  dest_dir: "projects/<id>/data"
  sha256_expected: "..."   # optional integrity

dataset_profile:
  path: "..."
  segnini_flags: [completeness, duplicates, accuracy, integrity, codes]
```

See `SKILL.md`.
