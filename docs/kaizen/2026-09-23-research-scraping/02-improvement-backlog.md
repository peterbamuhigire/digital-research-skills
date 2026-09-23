# Improvement backlog (target 95/100)

| Gap | Root cause | Change | Acceptance evidence | Risk/rollback | Target |
|---|---|---|---|---|---:|
| No end-to-end bounded collector | Tooling was componentized but not composed | Add `ResearchScraper` and CLI | Unit tests plus manifest fixture | Revert new module/CLI | 95 |
| Raw responses not tied to run evidence | Cache had no research record contract | Add JSONL records with SHA-256 and run manifest | `test_cache_prevents_refetch_on_second_run` | Delete only local run output | 95 |
| Crawl scope could be implicit | No same-host queue boundary | Same-host default and explicit cross-host flag | Link-scope test | Narrow scope; no bypass | 95 |
| Model currentness unresolved | Runtime catalogue not exposed; policy drift | Keep `NOT_ASSESSED`, retain pins, recheck next cycle | Currentness record and policy check log | No config change | 95 |

Next experiment: run the CLI against one operator-authorized public site with
one seed and at most three pages, review the manifest and three extracted
records, then decide whether a richer schema or a Scrapy adapter is warranted.
