# Digital Research Engine

The Digital Research Engine is Chwezi Core Systems' cross-cutting engine for finding, evaluating, verifying and synthesising evidence. It holds 59 skills that plan research and run it in waves: admitting and scoring sources, verifying URLs, quotations, statistics and claim links, and building evidence-to-claim graphs. Further skills cover analytic tradecraft, calibrated forecasting, OSINT, due-diligence and legal research, primary fieldwork, web data collection, dataset quality work and quantitative modelling. Its method follows named standards: PRISMA 2020 and the EQUATOR Network reporting guidelines (CONSORT, STROBE, MOOSE), GRADE and the Cochrane Handbook for evidence synthesis, ODNI ICD 203 and ICD 206 for analytic and sourcing standards, the NATO Admiralty Code (STANAG 2511) for source reliability, the Berkeley Protocol for digital open-source investigation, and IETF RFC 9309 for crawler conduct. Every material claim must be traceable to a source, independently verified, dated for currentness and kept separate from inference.

The engine produces research plans and wave roadmaps, source registers and verification manifests, evidence-claim graphs, audit-ready evidence packs, and intelligence briefs and estimative memos. It also delivers due-diligence reports, OSINT chronologies, legal research memoranda, systematic and scoping literature reviews, theses and dissertations checked against named Ugandan and Kenyan university handbooks, policy briefs, market analyses, decision memos, white papers, and professional Microsoft Word, Excel and PDF documents with render evidence. It is written for researchers, analysts, consultants, investigators, due-diligence teams, postgraduate students and their supervisors, and for decision-makers who need evidence they can defend. The other Chwezi engines consult it alongside their own skills whenever a task depends on current or uncertain facts.

## Installation

Prerequisites:

- Claude Code, for the plugin route.
- Node.js 18 or newer, for the clone installers (`install.sh` and `install.ps1` both delegate to `scripts/install-engine.js`).
- Python 3.11 or newer, for the research workspace CLI (`python -m engine`), the validators and the Codex model-policy helper. CI runs Python 3.12 with `PyYAML` and `pytest`; the document tools also use `python-docx` and `xlsxwriter`.

**Claude Code plugin.** The marketplace is `chwezi-research` and the plugin is `research` (`.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`):

```text
/plugin marketplace add https://github.com/peterbamuhigire/digital-research-skills
/plugin install research@chwezi-research
```

**Clone and install.** The installer copies the engine into `~/.claude` (`--scope user`, the default) or into `.claude` under the current directory (`--scope project`). It also accepts `--dry-run`, `--json` and `--force`:

```text
git clone https://github.com/peterbamuhigire/digital-research-skills
cd digital-research-skills
./install.sh --scope project      # macOS, Linux, Git Bash
.\install.ps1 --scope project     # Windows PowerShell
node scripts/install-engine.js doctor --scope project
```

The same script also runs `uninstall --engine <name>` and `list-installed`.

**Codex.** Point Codex at the clone. It reads `AGENTS.md`, which routes to `SKILL.md` and `rules/common/core.md`. The Codex-only model-policy check lives in `.codex/`:

```text
python <engine-root>/.codex/ensure_model_policy.py --runtime codex --check
```

**Manual use (any agent).** Clone the repository and read `CLAUDE.md` (Claude Code) or `AGENTS.md` (other runners). Then open the router `SKILL.md` and load only the routed `skills/<skill-name>/SKILL.md` files. To scaffold and check a research workspace:

```text
python -m engine doctor
python -m engine new-project "<name>" --type <research-type> --audience <audience>
python -m engine validate <project>
python -m engine pack <project> --out <file>.zip
```

## Capabilities

Skills are stored flat as `skills/<skill-name>/SKILL.md`, so the table groups them by workflow. It lists 59 active skills in 11 groups, generated from the skill front matter; `skills/doc-standards.md` and `skills/encoding-patterns-into-skills.md` are shared notes, not skills. The router is [`SKILL.md`](SKILL.md).

| Category | Skill | What it does |
|---|---|---|
| Research operating system (6) | [`00-meta-initialization`](skills/00-meta-initialization/) | Initialises a research workspace with profile, method, audience-output matrix, wave roadmap and dispatch gate |
| | [`doctrine-spine`](skills/doctrine-spine/) | Defines and audits the mandatory research sequence from evidence discipline to export |
| | [`research-orchestration`](skills/research-orchestration/) | Chooses research type, discipline strategy and reading mode, then plans waves, gap filling and synthesis |
| | [`research-design`](skills/research-design/) | Sets formal questions, method, case logic, historical or trend design and MROC design |
| | [`research-techniques`](skills/research-techniques/) | Supplies named techniques: mini-analysis, crosswalk matrix, gap analysis, reference interview, search-operator grammar |
| | [`agentic-research-operations`](skills/agentic-research-operations/) | Designs and audits multi-agent research: briefs, roles, tool limits, verification loops and recovery |
| Source discipline and verification (5) | [`source-evaluation`](skills/source-evaluation/) | Admits sources after testing provenance, authority, independence, timeliness, bias and fit to the claim |
| | [`source-verification`](skills/source-verification/) | Verifies URLs, quotations, statistics, claim-source links, archive snapshots and release readiness |
| | [`evidence-claim-graph`](skills/evidence-claim-graph/) | Builds a traceable graph of sources, evidence, claims, warrants, gaps and contradictions |
| | [`validation-contract`](skills/validation-contract/) | Defines the seven evidence categories and the Release Evidence Bundle for specialist skills and releases |
| | [`peer-review-loop`](skills/peer-review-loop/) | Runs adversarial, red-team, source and method review with dissent handling before release |
| Reasoning, analysis and forecasting (6) | [`critical-reasoning-and-argument`](skills/critical-reasoning-and-argument/) | Tests claims for warrants, assumptions, countercases and implications |
| | [`analytic-tradecraft`](skills/analytic-tradecraft/) | Applies structured analytic techniques, bias checks and calibrated estimative language |
| | [`calibration-and-forecasting`](skills/calibration-and-forecasting/) | Calibrates, scores and updates forecasts, probability judgements and confidence claims |
| | [`decision-support-analysis`](skills/decision-support-analysis/) | Frames decisions with alternatives, values, uncertainty, trade-offs and pre-mortems |
| | [`systems-thinking-and-mental-models`](skills/systems-thinking-and-mental-models/) | Analyses feedback loops, root causes and leverage points with systemigrams and mental models |
| | [`mind-mapping-and-synthesis`](skills/mind-mapping-and-synthesis/) | Compresses a verified corpus into a navigable mind map for synthesis and decomposition |
| Data and quantitative work (3) | [`dataset-discovery-and-analysis`](skills/dataset-discovery-and-analysis/) | Finds public datasets, retrieves them with integrity checks and profiles their quality |
| | [`data-quality-pipeline`](skills/data-quality-pipeline/) | Profiles, cleans, merges and validates tabular data through lineage and quality gates |
| | [`quantitative-modelling`](skills/quantitative-modelling/) | Builds market-sizing, scenario and forecast models with assumption registers and model audits |
| Investigation and collection (7) | [`osint-investigation`](skills/osint-investigation/) | Runs lawful public-source investigation: reconnaissance, adverse media, chronology and case vaults |
| | [`due-diligence`](skills/due-diligence/) | Conducts corporate, sanctions, ownership and background due diligence with an auditable finding trail |
| | [`pi-investigation`](skills/pi-investigation/) | Supports authorised licensed-investigator work with chain of custody and evidentiary reports |
| | [`online-legal-research`](skills/online-legal-research/) | Researches statutes, cases and treaties by jurisdiction and refuses unverified law |
| | [`primary-research`](skills/primary-research/) | Designs interviews, observation, focus groups and coding for first-hand qualitative evidence |
| | [`web-scraping-foundations`](skills/web-scraping-foundations/) | Chooses the least invasive web acquisition path, with politeness and error handling |
| | [`scraping-engineering-python`](skills/scraping-engineering-python/) | Scales Python scrapers with caching, concurrency, browser automation and form handling |
| Academic research (5) | [`academic-writing`](skills/academic-writing/) | Drafts academic prose with source-away composition, citation, synthesis and register controls |
| | [`academic-reporting-standards`](skills/academic-reporting-standards/) | Applies named reporting and examination standards to papers, theses and systematic reviews |
| | [`dissertation-writing-process`](skills/dissertation-writing-process/) | Plans and drafts a dissertation from research question to defence-ready manuscript |
| | [`uganda-academic-research`](skills/uganda-academic-research/) | Checks academic work against named Ugandan university handbooks |
| | [`kenya-academic-research`](skills/kenya-academic-research/) | Checks academic work against named Kenya-based institutional handbooks |
| Writing and communication (9) | [`research-output-formats`](skills/research-output-formats/) | Selects the document form and academic or non-academic variant for a deliverable |
| | [`analytical-report-shapes`](skills/analytical-report-shapes/) | Shapes decision-grade artefacts: intelligence briefs, estimative and decision memos, evaluation reports |
| | [`report-and-proposal-craft`](skills/report-and-proposal-craft/) | Drafts long-form reports, proposals, business plans, bid responses and white papers |
| | [`business-writing`](skills/business-writing/) | Drafts emails, memos, letters, articles, web copy and speeches |
| | [`executive-communication`](skills/executive-communication/) | Turns verified research into answer-first memos, reports, decks and one-pagers |
| | [`consulting-delivery`](skills/consulting-delivery/) | Structures consulting work with issue trees, hypothesis-led workplans and implementation logic |
| | [`east-african-english`](skills/east-african-english/) | Adjusts English to natural, professional East African usage |
| | [`anti-ai-slop`](skills/anti-ai-slop/) | Prevents generic, unsupported or mechanical prose while an artefact is produced |
| | [`ai-slop-audit`](skills/ai-slop-audit/) | Grades a finished artefact for AI slop with evidenced findings, fixes and a verdict |
| Document production (5) | [`professional-word-output`](skills/professional-word-output/) | Produces and checks Word documents with controlled styles, pagination, tables and render evidence |
| | [`excel-spreadsheets`](skills/excel-spreadsheets/) | Builds and repairs Excel workbooks with formulas, tables, charts and formatting |
| | [`python-document-generation`](skills/python-document-generation/) | Generates branded Excel, Word and PDF exports from Python |
| | [`manual-guide`](skills/manual-guide/) | Writes end-user manuals and reference guides for ERP or SaaS features |
| | [`markdown-lint-cleanup`](skills/markdown-lint-cleanup/) | Repairs Markdown lint issues without changing meaning |
| Knowledge products (2) | [`knowledge-mining`](skills/knowledge-mining/) | Turns a corpus into claim libraries, evidence maps, dossiers and ontology seeds |
| | [`knowledge-productization`](skills/knowledge-productization/) | Converts research into reusable knowledge assets and audience-specific offerings |
| Requirements and project documentation (5) | [`project-requirements`](skills/project-requirements/) | Runs a discovery interview that yields requirements, business rules, user types and workflows |
| | [`systems-process-requirements`](skills/systems-process-requirements/) | Describes systems, processes, interfaces, states and data in testable, traceable form |
| | [`spec-architect`](skills/spec-architect/) | Produces coding-ready specifications with scope, acceptance criteria and risks |
| | [`doc-architect`](skills/doc-architect/) | Generates a project's layered `AGENTS.md` documentation from observed workspace evidence |
| | [`update-claude-documentation`](skills/update-claude-documentation/) | Reconciles project documentation with code after an authorised change |
| Engine and skill practice (6) | [`skill-writing`](skills/skill-writing/) | Creates or upgrades a skill under the canonical chwezi-dev-engine standard |
| | [`skill-composition-standards`](skills/skill-composition-standards/) | Sets house style, artefact contracts and evidence declarations for composed skills |
| | [`skill-taxonomy-and-routing`](skills/skill-taxonomy-and-routing/) | Normalises skill names, resolves skill-or-reference decisions and updates routers |
| | [`skill-safety-audit`](skills/skill-safety-audit/) | Reviews a new or changed skill for credential harvesting, unsafe installers and hidden mutation |
| | [`capability-matrix`](skills/capability-matrix/) | Maps a technology domain to its foundation, implementation, validation and companion skills |
| | [`ai-evaluation-and-data-flywheel`](skills/ai-evaluation-and-data-flywheel/) | Designs evaluations, failure analysis, regression sets and feedback loops for AI-assisted research |

**Total: 59 skills** (6 + 5 + 6 + 3 + 7 + 5 + 9 + 5 + 2 + 5 + 6).

## Operating rules and quality gates

- Load [`rules/common/core.md`](rules/common/core.md) with any routed skill. Current, legal, regulatory and platform claims need an authoritative source and a dated currentness check. Unexecuted checks are reported as `NOT_ASSESSED`.
- Release gates live in [`docs/quality-gates/`](docs/quality-gates/). The standards register is [`docs/source-registers/research-standards-register.md`](docs/source-registers/research-standards-register.md). Kaizen evidence is under [`docs/continuous-improvement/`](docs/continuous-improvement/).
- Checks: `python -X utf8 scripts/validate_engine.py`, `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json`, `python -X utf8 scripts/routing_smoke_test.py --min-rank1 84 --lint-fixtures` and `python -m pytest -q tests engine/tests`.
- Book-derived knowledge enters only as paraphrased, task-oriented references. `scripts/check_no_book_extractions.py` blocks book extractions from the repository.

## References

The sources below are those cited in this repository: skill source sections and source registers, [`RESEARCH_CRAFT_INTEGRATION.md`](RESEARCH_CRAFT_INTEGRATION.md), the July 2026 book-to-engine map, Kaizen records, the 2026-Q4 ecosystem scan and code attribution comments. Where the repository omits an author, year or publisher, so does this list. Citations only; no book content is reproduced.

### Books

- Aaker, Kumar, Leone and Day (2022) *Marketing Research*, 13th ed., Wiley.
- Abbott (2014) *Digital Paper*.
- Bailey (2018) *Academic Writing: A Handbook for International Students*, 5th ed., Routledge.
- Bazerman (1988) *Shaping Written Knowledge: The Genre and Activity of the Experimental Article in Science*, University of Wisconsin Press.
- Bazzell *Open Source Intelligence Techniques*, 11th ed.
- Bean (2011) *No More Secrets: Open Source Information and the Reshaping of U.S. Intelligence*, Praeger Security International / ABC-CLIO.
- Behrens and Hawranek (1991) *Manual for the Preparation of Industrial Feasibility Studies*, rev. ed., UNIDO.
- Belcher (2019) *Writing Your Journal Article in Twelve Weeks*, 2nd ed., University of Chicago Press.
- Bell (2015) *Librarian's Guide to Online Searching*, 4th ed.
- Berg (2004) *Qualitative Research Methods for the Social Sciences*, Pearson.
- Bergeron (2003) *Essentials of Knowledge Management*.
- Boardman and Sauser *Systemic Thinking: Building Maps for Worlds of Systems*.
- Booth, Colomb, Williams, Bizup and FitzGerald (2016) *The Craft of Research*, 4th ed., University of Chicago Press.
- Booth, Sutton and Papaioannou (2021) *Systematic Approaches to a Successful Literature Review*, 3rd ed., SAGE.
- Botwright (2024) *Advanced OSINT Strategies: Online Investigations and Intelligence Gathering*.
- Boynton *The New New Journalism*.
- Brause (1999) *Writing Your Doctoral Dissertation: Invisible Rules for Success*, Falmer Press / RoutledgeFalmer.
- BRB Publications *The Sourcebook to Public Record Information*.
- Brockman (ed.) *Thinking: The New Science of Decision-Making, Problem-Solving, and Prediction*.
- Brody (2017) *The Ultimate Guide to Web Scraping*.
- Brown (2017) *Harnessing the Power of Google*.
- Bui (2019) *How to Write a Master's Thesis*, 3rd ed., SAGE.
- Burke (1945) *A Grammar of Motives*.
- Burtonshaw-Gunn *Essential Tools for Management Consulting*.
- Buzan *Mind Map Mastery*; Buzan *Buzan Study Skills Handbook*.
- Caples and Hahn (1998) *Tested Advertising Methods*, 5th ed., Prentice Hall.
- Clark (2019) *Intelligence Analysis: A Target-Centric Approach*, 6th ed., CQ Press.
- Clippinger (2019) *Business Report Guides: Research Reports and Business Plans*.
- Cottrell (2023) *Critical Thinking Skills*, 4th ed., Bloomsbury.
- Day and Gastel (2017) *How to Write and Publish a Scientific Paper*, 8th ed., Cambridge University Press.
- Deason *Internet Research with Google*.
- Denscombe (2019) *Research Proposals: A Practical Guide*, 2nd ed., Open University Press.
- Duarte (2014) *Slidedocs: Spread Ideas with Effective Visual Documents*, Duarte Inc.
- Dunleavy (2003) *Authoring a PhD*, Palgrave Macmillan.
- Eco (2015) *How to Write a Thesis* (English translation).
- Edwards (2019) *Legal Writing and Analysis*, 5th ed., Wolters Kluwer.
- Ellet (2007) *The Case Study Handbook*, Harvard Business Review Press.
- Forsyth (2016) *How to Write Reports and Proposals*.
- Garner (2013) *HBR Guide to Better Business Writing*, Harvard Business Review Press.
- Garner (2013) *Legal Writing in Plain English*, 2nd ed., University of Chicago Press.
- Geffner *Business English*.
- George *Excel 2019 Advanced Topics*.
- George and Bruce (eds.) (2008) *Analyzing Intelligence: Origins, Obstacles, and Innovations*, Georgetown University Press.
- Glaser and Strauss (1967) *The Discovery of Grounded Theory*.
- Glatthorn and Joyner (2017) *Writing the Winning Thesis or Dissertation*, 4th ed., Corwin.
- Gottschall (2013) *The Storytelling Animal: How Stories Make Us Human*, Mariner Books.
- Graham (2013) *White Papers For Dummies*, Wiley.
- Grant (2021) *Contemporary Strategy Analysis*, 11th ed., Wiley.
- Hackos *The Complete Guide to Knowledge Management*.
- Hague, Hague and Morgan (2022) *Market Research in Practice*, 4th ed., Kogan Page.
- Hancock and Algozzine (2006) *Doing Case Study Research: A Practical Guide for Beginning Researchers*, Teachers College Press.
- Hanington and Martin *The Pocket Universal Methods of Design*.
- Hart (2018) *Doing a Literature Review*, 2nd ed., SAGE.
- Hart *Storycraft*.
- Hartley (2008) *Communicating Ideas: The Politics of Scholarly Publishing*, Routledge.
- Hattori *The McKinsey Edge*.
- Heath and Heath (2013) *Decisive: How to Make Better Choices in Life and Work*, Random House.
- Henwood (2020) *Business Writing for Innovators and Change-Makers*, Business Expert Press.
- Hetherington (2015) *The Guide to Online Due Diligence Investigations*, 2nd ed., Facts on Demand Press.
- Heuer (1999) *Psychology of Intelligence Analysis*, CIA Center for the Study of Intelligence.
- Heuer and Pherson *Structured Analytic Techniques for Intelligence Analysis*, CQ Press / SAGE (1st ed. 2010; 3rd ed. cited as 2020 and 2021).
- Hewings and Hewings *Grammar and Context*, Routledge.
- Hood *Words at Work*.
- Hyland (1998) *Hedging in Scientific Research Articles*.
- Hyland (2004) *Disciplinary Discourses: Social Interactions in Academic Writing*, 2nd ed., University of Michigan Press.
- Jordan *ICDL Word*.
- Kamler and Thomson (2014) *Helping Doctoral Students Write*, 2nd ed., Routledge.
- Kantor (2009) *Crafting White Paper 2.0*, Lulu.
- Kelley *The Art of Reasoning: An Introduction to Logic and Critical Thinking*.
- Koelsch *Requirements Writing for System Engineering*.
- Kotler and Keller (2022) *Marketing Management*, 16th ed., Pearson.
- Kramer and Call *Telling True Stories*.
- Krone *Navigating the Dissertation Writing Process*.
- Kunz, Schmedemann, Erlinder, Downs and Bateson (2020) *The Process of Legal Research: Practices and Resources*, 9th ed., Wolters Kluwer.
- Lawson (2015) *Web Scraping with Python*, Packt.
- Lindsell-Roberts (2024) *Business Writing with AI for Dummies*, Wiley.
- Locke, Spirduso and Silverman (2013) *Proposals That Work*, 6th ed., SAGE.
- Lockridge and Van Ittersum *Writing Workflows*.
- Long *Legal Research Using the Internet*.
- MacLeod (2012) *How to Find Out Anything*.
- Magaziner and Patinkin (1989) *The Silent War*, Random House.
- Maslen (2019) *Persuasive Copywriting*, 2nd ed., Kogan Page.
- Maxwell (2020) *7 Steps to Better Writing*.
- McCandless (2014) *Knowledge is Beautiful*, William Collins.
- McInerny *Being Logical: A Guide to Good Thinking*.
- McMahon (2001) *Practical Handbook for Professional Investigators*.
- Medina (2014) *Brain Rules*, 2nd ed., Pear Press.
- Merriam (2001) *Qualitative Research and Case Study Applications in Education*, Jossey-Bass.
- Minto (1985; revised 1996, 2002, 2009) *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving*, Minto Books International.
- Morley (2017) *Academic Phrasebank*, 4th ed.
- Murray (2017) *How to Write a Thesis*, 4th ed., Open University Press.
- National Research Council (2011) *Intelligence Analysis for Tomorrow: Advances from the Behavioral and Social Sciences*, National Academies Press.
- Norman (2004) *Emotional Design: Why We Love (or Hate) Everyday Things*, Basic Books.
- O'Dell and McCarthy (2017) *English Collocations in Use Advanced*, 2nd ed., Cambridge University Press.
- Ogilvy (1985) *Ogilvy on Advertising*, Vintage.
- Oxylabs (2024) *Python Web Scraping for Developers*.
- Patton (2015) *Qualitative Research & Evaluation Methods: Integrating Theory and Practice*, 4th ed., SAGE.
- Phillips and Pugh (2015) *How to Get a PhD*, 6th ed., Open University Press.
- Porter (1980) *Competitive Strategy*, Free Press; Porter (1985) *Competitive Advantage*.
- Poynter (2010) *The Handbook of Online and Social Media Research*.
- Punch (2016) *Developing Effective Research Proposals*, 3rd ed., SAGE.
- Putman and Albright (2018) *Legal Research, Analysis and Writing*, Cengage.
- Ramsey (2017) *Business Writing Scenarios*, Bedford/St Martin's.
- Rasiel (1999) *The McKinsey Way*, McGraw-Hill.
- Rasiel and Friga (2001) *The McKinsey Mind*, McGraw-Hill.
- Raymond (2003) *Pamphlets and Pamphleteering in Early Modern Britain*, Cambridge University Press.
- Ridley (2012) *The Literature Review: A Step-by-Step Guide for Students*, 2nd ed., SAGE.
- Roman and Raphaelson (2000) *Writing That Works*, 3rd ed.
- Rowland (2000) *The Creative Guide to Research*.
- Rubie and Provost *How to Tell a Story*.
- Rumelt (2011) *Good Strategy, Bad Strategy*, Crown Business.
- Russell (2019) *The Joy of Search*.
- Seely *The Oxford Guide to Effective Writing and Speaking*.
- Shiach *How to Write Essays*.
- Shikhman and Mueller (2021) *Mathematical Foundations of Big Data Analytics*.
- Silverman (ed.) (2015) *Verification Handbook for Investigative Reporting*.
- Smith and Albaum (2005) *Fundamentals of Marketing Research*, SAGE.
- Stake (1995) *The Art of Case Study Research*, SAGE.
- Starkman, Hamilton, Chittum and Salmon (eds.) (2014) *The Best Business Writing 2014*, Columbia University Press / Columbia Journalism Review Books.
- Stelzner (2007) *Writing White Papers*, WhitePaperSource Publishing.
- Stoner and Perkins (2015) *Making Sense of Messages*, 2nd ed., Routledge.
- Strunk and White *The Elements of Style*, 4th ed.
- Sugarman (2007) *The Adweek Copywriting Handbook*, Wiley.
- Swales (1990) *Genre Analysis*.
- Swales and Feak (2012) *Academic Writing for Graduate Students*, 3rd ed., University of Michigan Press.
- Thompson (2014) *Feasibility Studies: Tools and Techniques*, Routledge.
- Treverton (2003) *Reshaping National Intelligence for an Age of Information*, Cambridge University Press.
- Trzeciak and Mackay (1994) *Study Skills for Academic Writing*.
- Tufte (2001) *The Visual Display of Quantitative Information*, 2nd ed.
- Urban *Advanced Excel for Productivity*.
- Van Der Post *Python in Excel Advanced*.
- Vic *Microsoft Word 2022 for Beginners & Pros*.
- Walkenbach and Alexander *Microsoft Excel 365 Bible*.
- Walker *Python Data Cleaning Cookbook*.
- Wallwork (2016) *English for Writing Research Papers*, 2nd ed., Springer.
- Watkins *The Six Disciplines of Strategic Thinking*.
- Wempen *Advanced Microsoft Word 2016*.
- Wengler (2026) *Automate Excel with Python*.
- Wiegers *More About Software Requirements*.
- Wiegers and Hokanson *Software Requirements Essentials*.
- Williams and Newton (2007) *Visual Communication: Integrating Media, Art, and Science*, Routledge.
- Wohlstetter (1962) *Pearl Harbor: Warning and Decision*, Stanford University Press.
- Yayici *Business Analysis Methodology Book*.
- Yin (2014) *Case Study Research: Design and Methods*, 5th ed., SAGE; Yin (2018) *Case Study Research and Applications: Design and Methods*, 6th ed., SAGE.
- Young and Quinn (2002) *Writing Effective Public Policy Papers*, Open Society Institute.
- Zelazny (2001) *Say It With Charts: The Executive's Guide to Visual Communication*, 4th ed., McGraw-Hill.
- Titles cited without an author: *AI-Based Data Analytics: Applications for Business Management*; *Applying the Kaizen in Africa* (2018); *Better Data Visualizations*; *Business Requirements Gathering and Data Architecture Modeling*; *Clear Written Communication* (50Minutes); *Critical Thinking, Logic & Problem Solving*; *Critical Thinking Skills: Developing Effective Analysis and Argument*; *Critical Thinking Skills for Education Students*; *Dare to Disrupt*; *Data Analytics using Python*; *Data Journalism Heist*; *Design Systems Handbook*; *Design Thinking*; *Designing for AI* (early release); *Developments in Information and Knowledge Management Systems for Business Applications*; *Doing Internet Research*; *Doing Your Research Project*; *Excel 2025 All-in-One*; *Facility Move Playbook*; *Finish Your Thesis or Dissertation! Tips & Hacks for Success*; *Growth Engineering*; *Hands-On Website Scraping with Python*; *How to Write a Literature Review: A Workbook in Six Steps*; *How to Write a Master's Thesis Fast*; *Inside the Minds: Leading Consultants*; *Introduction to Data Analytics*; *Knowledge Management and Business Strategies*; *LEAN Ultimate Collection* (2018); *Legal Research* (anonymous compendium); *Make Phenomenal Profits*; *Mental Models 2*; *Microsoft Excel Bible 2026*; *MSC Software Magazine* (2019); *Oxford Guide to Effective Argument and Critical Thinking*; *Platform Enterprise* (early release); *Project Scope Management: A Practical Guide to Requirements*; *Remarkable Business Growth*; *Rewired: The McKinsey Guide to Outcompeting in the Age of Digital and AI*; *Smart Thinking: Skills for Critical Understanding and Writing*, 2nd ed.; *The Art of Asking Essential Questions*; *The Data Analytics Advantage*; *The Great Mental Models, Volume 1*; *Think Deeper*; *Thinking in Systems and Mental Models*; *True or False*; *Ultimate Excel Formula & Function Reference Guide*; *Writing a Postgraduate Thesis or Dissertation: Tools for Success*.

### Repositories

- affaan-m/ECC — https://github.com/affaan-m/ECC — MIT — `santa-method` dual-reviewer convergence and stratified batch sampling (`peer-review-loop`); `scientific-thinking-literature-review` rigour levels (`academic-reporting-standards`); the MSYS2 path fix and installer scope choice (`install.sh`, `scripts/install-engine.js`).
- obra/superpowers — https://github.com/obra/superpowers — MIT, commit `8ca22db` — the description-narration lint in `skills/skill-writing/scripts/quick_validate.py` (my-10-kaizen SP-14).
- addyosmani/agent-skills — https://github.com/addyosmani/agent-skills — MIT, commit `2686b62` — four Tier-1 lint rules from `scripts/lib/skill-lint.js` (`quick_validate.py`) and the owner-outranks-self routing rule from `scripts/run-evals.js` (`scripts/routing_smoke_test.py`) (my-10-kaizen M10-03).
- JuliusBrussee/caveman — https://github.com/JuliusBrussee/caveman — MIT (skill side only), commit `2fd153c` — the evidence-rung vocabulary for improvement claims in `ai-evaluation-and-data-flywheel/references/eval-flywheel.md` (my-10-kaizen CV-07).
- DietrichGebert/ponytail — https://github.com/DietrichGebert/ponytail — MIT, commit `e3ba2aa` — the thin `CLAUDE.md` bridge to `AGENTS.md` and a real semantic version, 1.1.0 (my-10-kaizen PT-01, PT-04).
- pbakaus/impeccable — https://github.com/pbakaus/impeccable — Apache-2.0, commit `114ea1d` — anti-slop source record, the design trigger block, the detector rule-source pin for the K5 re-audit and the `PROJECT.md` context read in `AGENTS.md` (my-10-kaizen IM-11); ideas paraphrased, no code copied.
- ComposioHQ/awesome-claude-skills — https://github.com/ComposioHQ/awesome-claude-skills — NOASSERTION, commit `be2a406` — scan source for the first quarterly ecosystem scan (my-10-kaizen AC-04); nothing installed.
- Egonex-AI/Understand-Anything — https://github.com/Egonex-AI/Understand-Anything — MIT, commit `b05cc3b` — `/understand-knowledge` sandbox pilot recorded as `NOT_ASSESSED` under the zero-spend rule; not installed or adopted.
- WebBreacher/obsidian-osint-templates — https://github.com/WebBreacher/obsidian-osint-templates — practitioner OSINT note structure (`osint-investigation/references/osint-case-vaults.md`).
- donvito/codex-astra-luna-orchestrator — https://github.com/donvito/codex-astra-luna-orchestrator — commit `21f4561` — concept reference for the Codex model-policy helper in `.codex/`; independently implemented.
- peterbamuhigire/chwezi-dev-engine — https://github.com/peterbamuhigire/chwezi-dev-engine — canonical skill-writing standard and ecosystem-scan intake procedure.
- Reviewed in the 2026-Q4 ecosystem scan with no borrowing (licences and verdicts in [`docs/continuous-improvement/ecosystem-scan-2026-Q4.md`](docs/continuous-improvement/ecosystem-scan-2026-Q4.md)): agentskills/agentskills, alibaba/open-code-review, alirezarezvani/claude-skills, anthropics/skills, asgeirtj/system_prompts_leaks, blader/humanizer, career-ops-hq/career-ops, cathrynlavery/diagram-design, CherryHQ/cherry-studio, diegosouzapw/OmniRoute, farion1231/cc-switch, github/awesome-copilot, googleworkspace/cli, Graphify-Labs/graphify, headroomlabs-ai/headroom, hesreallyhim/awesome-claude-code, Imbad0202/academic-research-skills, jeecgboot/JeecgBoot, JimLiu/baoyu-skills, K-Dense-AI/scientific-agent-skills, KKKKhazix/khazix-skills, Leonxlnx/taste-skill, mvanhorn/last30days-skill, nextlevelbuilder/ui-ux-pro-max-skill, nexu-io/open-design, NousResearch/hermes-agent, NVIDIA/SkillSpector, OthmanAdi/planning-with-files, Panniantong/Agent-Reach, pascalorg/editor, phuryn/pm-skills, reactive-resume/reactive-resume, router-for-me/CLIProxyAPI, rtk-ai/rtk, ruvnet/ruflo, shanraisshan/claude-code-best-practice, shareAI-lab/learn-claude-code, sickn33/agentic-awesome-skills, snyk-labs/toxicskills-goof, stablyai/orca, thedotmack/claude-mem, titanwings/distilly, topoteretes/cognee, tt-a1i/archify, virgiliojr94/book-to-skill, VoltAgent/awesome-agent-skills, VoltAgent/awesome-openclaw-skills, zhayujie/CowAgent.

### Standards and official sources

- PRISMA 2020 statement and checklist — https://www.prisma-statement.org/prisma-2020; Page et al., *BMJ* 2021;372:n71.
- EQUATOR Network reporting guidelines — https://www.equator-network.org/ — including CONSORT 2025 (https://www.consort-spirit.org/), STROBE (https://www.strobe-statement.org/) and MOOSE (Stroup et al., *JAMA* 2000;283:2008-2012).
- GRADE Working Group — https://www.gradeworkinggroup.org/; GRADEpro handbook — https://gradepro.org/handbook/.
- Cochrane Handbook for Systematic Reviews — https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current.
- Center for Open Science TOP Guidelines — https://www.cos.io/initiatives/top-guidelines.
- ICMJE Recommendations — https://www.icmje.org/recommendations/.
- ODNI Intelligence Community Directive 203, *Analytic Standards* (2015) — https://www.dni.gov/files/documents/ICD/ICD-203.pdf; ICD 206, *Sourcing Requirements for Disseminated Analytic Products*.
- Kent (1964) "Words of Estimative Probability", *Studies in Intelligence* — https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf.
- NATO Admiralty Code, STANAG 2511 / AJP-2.1.
- UK Professional Head of Intelligence Assessment, *Probability Yardstick*.
- Silberman-Robb WMD Commission Report (2005).
- Berkeley Protocol on Digital Open Source Investigations — https://humanrights.berkeley.edu/wp-content/uploads/2024/02/Berkeley-Protocol.pdf.
- FIRST CTI SIG, "Source Evaluation" — https://www.first.org/global/sigs/cti/curriculum/source-evaluation.
- IETF RFC 9309, *Robots Exclusion Protocol* (September 2022).
- NIST AI Risk Management Framework — https://www.nist.gov/itl/ai-risk-management-framework; NIST, "Four Principles of Explainable Artificial Intelligence" — https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence.
- IEEE Computer Society, SWEBOK Guide V4.0 — https://www.computer.org/education/bodies-of-knowledge/software-engineering.
- Schema.org `ClaimReview` — https://schema.org/ClaimReview; Google Fact Check structured data — https://developers.google.com/search/docs/appearance/structured-data/factcheck; Google Search Central documentation.
- Citation standards: APA 7; *OSCOLA*, 4th ed. (2012); *The Bluebook: A Uniform System of Citation*, 21st ed. (2020).
- IFRS Conceptual Framework (qualitative characteristics of useful financial information).
- Plain Language Action and Information Network, *Federal Plain Language Guidelines*.
- World Bank Project Appraisal Document templates and *Reference Guide to Cost-Benefit Analysis*; ESOMAR *Global Market Research* and methodology guidelines.
- Institutional doctoral regulations (accessed 2026-04-26): University of Cambridge, University of Oxford, London School of Economics, Harvard Griffin GSAS and SEAS, Yale GSAS and Registrar, and Princeton Graduate School and Library. Links are in `skills/academic-reporting-standards/references/oxbridge-ivy-examination-conventions.md`.
- Ugandan handbooks: Busitema University research dissemination handbook; Makerere University Directorate of Research and Graduate Training guidelines (2011); Uganda Christian University Research Manual (revised April 2018).
- Kenyan handbooks: Adventist University of Africa Research Handbook; Regional Centre on Groundwater Resources research guide (2019); Kenyatta University School of Hospitality research guide.
- W3C WCAG 2.2; Apple Human Interface Guidelines (Onboarding); GOV.UK Service Manual (user research and prototypes), from the design and product learning record.
- Anthropic, Claude Code plugin manifest reference — https://code.claude.com/docs/en/plugins-reference; OpenAI API models and pricing pages — https://developers.openai.com/api/docs/models (currentness register `docs/source-registers/skills-kaizen-wave2-2026-09.json`).

### Websites and articles

- Bellingcat, *Online Open Source Investigation Toolkit* and the Information Laundromat — https://bellingcat.gitbook.io/toolkit/more/all-tools/the-information-laundromat.
- Dutch OSINT Guy, "OSINT Is A State Of Mind" (2018) — https://medium.com/@Dutchosintguy/osint-as-a-mindset-7d42ad72113d.
- AaronCTI, "My OSINT Blueprint — Methodology and Tools", parts one and two (2024) — https://aaroncti.com/my-osint-blueprint-methodology-and-tools-part-one/ and https://aaroncti.com/my-osint-blueprint-methodology-and-tools-part-two/.
- CQCore, "OSINT Methodology" (2024) — https://www.cqcore.uk/osint-methodology/.
- Sector035, "Week in OSINT #2023-06" — https://sector035.nl/articles/2023-06.
- Neon Maxima, "How I Turned Obsidian Into a Black-Ops Intelligence Hub" (Medium, 2025); Obsidian — https://obsidian.md/.
- NATO StratCom COE, report on information laundering in the Nordic-Baltic region — https://stratcomcoe.org/news/a-new-report-focuses-on-information-laundering-in-the-nordic-baltic-region/133.
- FEVER dataset — https://fever.ai/dataset/fever.html; AVeriTeC dataset — https://fever.ai/dataset/averitec.html.
- "Automated Fact-Checking" survey, *TACL* (2022) — https://aclanthology.org/2022.tacl-1.11.pdf; CREDULE / EVVER — https://arxiv.org/abs/2404.18971; Guo et al., "On Calibration of Modern Neural Networks" — https://arxiv.org/abs/1706.04599.
- Barbara Minto — https://www.barbaraminto.com/; McKinsey Alumni interview, "Barbara Minto: MECE" — https://www.mckinsey.com/alumni/news-and-events/global-news/alumni-news/barbara-minto-mece-i-invented-it-so-i-get-to-say-how-to-pronounce-it.
- University of Manchester, *Academic Phrasebank* (online).
- Cleveland and McGill (1984) "Graphical perception", *Journal of the American Statistical Association* 79(387).
- Cowan (2000) "The Magical Number 4 in Short-term Memory", *Behavioral and Brain Sciences* 24.
- Davis and Morley (2015) "Phrasal intertextuality", *Journal of Second Language Writing* 28.
- DeMarco and Tufts (2014) "The Mechanics of Writing a Policy Brief", *Nursing Outlook* 62(3).
- Dow et al. (2010), parallel prototyping study, *ACM TOCHI* 17(4).
- Flowers (1979) "Madman, Architect, Carpenter, Judge".
- MacEachin (1994) "Tradecraft of Analysis: Challenge and Change in the CIA".
- Wineburg and McGrew (2019) "Lateral reading and the nature of expertise", *Teachers College Record* 121(11).
- Open policy and communication guides: IDRC, *How to Write a Policy Brief*; ODI, *Writing Policy Papers*; Tsai, *Communicating Research for Policy Change*; Anthony, *Communicating Research to Non-Specialist Audiences* (Wellcome Trust); The Op-Ed Project, *How to Write an Op-Ed*; Content Marketing Institute, *Case Study Roadmap*.
- Eleken design and product guides (design-system checklist, onboarding, product-idea validation, dashboards, SaaS launch, AI design workflow, design consistency, UX ideas), from `docs/continuous-improvement/eleken-design-product-learning-2026-08.md`.
