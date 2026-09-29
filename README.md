# Digital Research Engine

The Digital Research Engine is a source-led research and analysis skill library for finding, evaluating, verifying, and synthesising evidence. Its current 59-skill inventory covers source evaluation and verification, research design and execution, primary research, investigations, data work, analysis, and research communication. Its operating rules require traceable claims, explicit source limitations, independent verification for material claims, and clear separation of evidence from inference.

It supports researchers, analysts, consultants, writers, and decision-makers producing research plans, evidence registers, verified findings, analyses, reports, academic or business documents, and decision support. Workflows include web collection and scraping guidance, data quality and modelling, peer review, synthesis, and document production; current, legal, and regulatory claims require authoritative sources and a stated currentness check.

## Installation

Install the native Claude Code plugin, or clone the repository and use its installer. The clone installer requires Node.js 18 or newer and supports user or project scope.

```text
/plugin marketplace add https://github.com/peterbamuhigire/digital-research-skills
/plugin install research@chwezi-research

git clone https://github.com/peterbamuhigire/digital-research-skills
cd digital-research-skills
./install.sh --scope project      # macOS/Linux/Git Bash
.\install.ps1 --scope project     # Windows PowerShell
```

## Capabilities

The 59 active skill files are grouped below by workflow. The [skills directory](skills/) is the complete live inventory; the [engine router](SKILL.md) sets the research sequence and directs selection of task-specific skills.

| Category | Core routes | Focus |
|---|---|---|
| Source discipline and validation | [source evaluation](skills/source-evaluation/), [source verification](skills/source-verification/), [evidence claim graph](skills/evidence-claim-graph/), [validation contract](skills/validation-contract/), [data quality](skills/data-quality-pipeline/) | Provenance, authority, claim fit, verification, uncertainty, and evidence readiness |
| Research design and execution | [research design](skills/research-design/), [research techniques](skills/research-techniques/), [orchestration](skills/research-orchestration/), [primary research](skills/primary-research/) | Research questions, search strategy, fieldwork, project planning, and research waves |
| Investigation and collection | [due diligence](skills/due-diligence/), [OSINT](skills/osint-investigation/), [PI investigation](skills/pi-investigation/), [legal research](skills/online-legal-research/), [web scraping](skills/web-scraping-foundations/), [Python scraping](skills/scraping-engineering-python/) | Due diligence, open-source and private investigation workflows, legal sources, and web data collection |
| Data, analysis, and synthesis | [dataset discovery](skills/dataset-discovery-and-analysis/), [quantitative modelling](skills/quantitative-modelling/), [analytic tradecraft](skills/analytic-tradecraft/), [mind mapping and synthesis](skills/mind-mapping-and-synthesis/), [systems thinking](skills/systems-thinking-and-mental-models/), [decision support](skills/decision-support-analysis/) | Dataset assessment, modelling, analytical reasoning, synthesis, and decisions |
| Academic, policy, and specialist research | [academic writing](skills/academic-writing/), [academic reporting](skills/academic-reporting-standards/), [dissertation process](skills/dissertation-writing-process/), [Kenya research](skills/kenya-academic-research/), [Uganda research](skills/uganda-academic-research/) | Scholarly methods and outputs, reporting standards, and country-specific research guidance |
| Communication and deliverables | [research output formats](skills/research-output-formats/), [analytical report shapes](skills/analytical-report-shapes/), [report and proposal craft](skills/report-and-proposal-craft/), [business writing](skills/business-writing/), [executive communication](skills/executive-communication/), [document generation](skills/python-document-generation/) | Reports, proposals, briefs, academic and business writing, spreadsheets, and professional documents |
| Engine and agent practice | [research operations](skills/agentic-research-operations/), [skill taxonomy and routing](skills/skill-taxonomy-and-routing/), [skill writing](skills/skill-writing/), [skill safety](skills/skill-safety-audit/), [AI evaluation](skills/ai-evaluation-and-data-flywheel/) | Agent workflows, skill composition and safety, capability review, and AI evaluation |

## References

- [Digital Research Engine repository](https://github.com/peterbamuhigire/digital-research-skills) — active skill inventory and source implementation.
- [Engine router](SKILL.md), [common rules](rules/common/core.md), [source evaluation](skills/source-evaluation/SKILL.md), and [source verification](skills/source-verification/SKILL.md) — evidence and workflow contracts consulted for this overview.
- [Everything Claude Code (ECC)](https://github.com/affaan-m/ECC) — referenced by the repository installer comments for its Windows/MSYS2 path-resolution handling.
