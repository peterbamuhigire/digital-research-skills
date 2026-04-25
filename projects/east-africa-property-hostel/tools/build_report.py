#!/usr/bin/env python3
"""
Build the Word-document report for east-africa-property-hostel using Schema A
(pain-point research, multi-cohort). Assembles master markdown from cohort files
then renders to .docx via pandoc.

Run from the project root or pass --project-root.
"""

from __future__ import annotations
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

COHORTS = ["students", "owners", "landlords", "tenants"]
COHORT_TITLES = {
    "students": "Students seeking and living in hostels",
    "owners": "Hostel owners and managers",
    "landlords": "General residential landlords",
    "tenants": "Ordinary residential tenants",
}
PROJECT_TITLE = "East Africa Property & Hostel — Pain-Point Research"
PROJECT_SUBTITLE = "Students, Hostel Owners, Landlords, and Tenants across Uganda, Kenya, Tanzania, Rwanda, Burundi, and South Sudan"
AUTHOR = "Peter Bamuhigire"
ENGINE = "digital-research-engine v0.1"


def read(path: Path) -> str:
    if not path.exists():
        return f"\n*[file missing: {path.name}]*\n"
    return path.read_text(encoding="utf-8")


def demote(md: str, levels: int = 1) -> str:
    """Demote # → ## etc. so embedded files don't compete with chapter headings."""
    out = []
    for line in md.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            new_level = "#" * min(len(m.group(1)) + levels, 6)
            out.append(f"{new_level} {m.group(2)}")
        else:
            out.append(line)
    return "\n".join(out)


def strip_first_h1(md: str) -> str:
    """Remove the first top-level heading from a file's body (we'll use our own)."""
    lines = md.splitlines()
    out = []
    skipped = False
    for line in lines:
        if not skipped and re.match(r"^# [^#]", line):
            skipped = True
            continue
        out.append(line)
    return "\n".join(out)


def section(md: str, levels: int = 1) -> str:
    return demote(strip_first_h1(md), levels=levels) + "\n\n"


def assemble_master(project_root: Path) -> str:
    today = dt.date.today().isoformat()

    parts: list[str] = []

    # Cover (pandoc respects %title %subtitle %author %date in metadata,
    # we'll also write a yaml block and a manual cover section)
    parts.append(f"""---
title: "{PROJECT_TITLE}"
subtitle: "{PROJECT_SUBTITLE}"
author: "{AUTHOR}"
date: "{today}"
toc: true
toc-depth: 3
numbersections: true
---

""")

    # 1. Executive summary
    parts.append("# 1. Executive Summary\n\n")
    parts.append("""This report documents the pain points of four interlocking cohorts in the East African property and hostel market: university students seeking and living in hostels, owners and managers of those hostels, general residential landlords, and ordinary residential tenants. Coverage spans Uganda, Kenya, Tanzania, Rwanda, Burundi, and South Sudan.

The market is structurally dysfunctional in mutually reinforcing ways. Students lose money to scams and live with sanitation collapse, sewage, bedbugs, and unfair eviction. Hostel owners absorb HELB / HESLB allowance delays, viral reputational risk from social-media incidents, public-private-partnership competition, and capital lock-in. Residential landlords contend with 7–11-month eviction delays, tenant-screening blindness, currency-driven cost spikes, and growing tax compliance burdens. Ordinary tenants lose 80% of deposits in Uganda, face up to 90% rejection rates if they are single women, and absorb utility failures with no rent-abatement remedy.

The single sharpest statistic in the corpus — Daily Monitor (Uganda), 2 August 2023 — is that **80% of Ugandan tenants never recover their security deposit** even when the property is left in good condition. The same dynamic hits the student cohort identically, making deposit theft the highest-leverage cross-cohort intervention surfaced by this research.

The 2024 Kenya National Building Code, the 2025 Kenya eRITS rental-income tax system, the 2025 Tanzania Use of Foreign Currency Regulations, and the 2024–25 NEMA Uganda wetland demolitions together constitute a 24-month period of significant regulatory repricing across the region. Acorn Holdings, the institutional benchmark on the supply side, is responding by deleveraging its student-housing assets through REIT transfers — a defensive rather than expansionary signal.

The report is organised into per-cohort findings (chapters 3–6), cross-cohort synthesis (chapter 7), two-sided product opportunities (chapter 8), the consolidated regulatory landscape (chapter 9), academic and industry references (chapter 10), a quotes appendix (chapter 11), a tiered source bibliography (chapter 12), and a glossary (chapter 13).

""")

    # 2. Methodology & sources
    parts.append("# 2. Methodology & Sources\n\n")
    parts.append(f"""## Approach

This research was conducted using the **digital-research-engine**, a portable multi-agent skills engine. The project ran two waves of investigation per cohort: a Wave-1 broad sweep and a Wave-2 targeted gap-fill. Cross-cohort synthesis is the orchestrator's responsibility, not delegated to sub-agents.

## Source tier ladder

Every source in this report is classified on a five-tier credibility ladder:

| Tier | Type | Examples |
|---|---|---|
| 1 | Peer-reviewed academic & official statistics | KNBS, World Bank, Wiley, SAGE |
| 2 | Regulatory / institutional | KRA, URA, ULII, Kenyalaw, IRA, NEMA |
| 3 | Established journalism with bylines | Daily Monitor, Daily Nation, The Standard, The Citizen |
| 4 | Industry analyst / NGO | Cytonn, CrossBoundary, Hass Consult, CAHF, Hakijamii |
| 5 | Social / blog / forum | Reddit, X, TikTok, blogs |

## Anti-hallucination guardrail

This engine enforces an **evidence-discipline** rule: no claim, statistic, quote, name, court case, statute, organisation, or URL appears in this report unless traceable to a real, verified source. Where Wave-2 verification could not confirm a Wave-1 claim, the claim has been corrected, downgraded to "(inference)", or struck. The project's `EVIDENCE-AUDIT.md` log tracks every caught fabrication or correction.

## Source counts

| Cohort | Wave-1 sources | Wave-2 sources | Total |
|---|---|---|---|
| Students | ~50 | ~40 | ~90 |
| Hostel owners | ~84 | ~40 | ~120 |
| Residential landlords | ~60 | ~38 | ~100 |
| Tenants | ~75 | ~40 | ~115 |
| **Total (de-duplicated estimate)** | | | **~300+** |

## Scope exclusions

- LGBTQ+ topics — explicitly excluded by project scope
- Hotels, short-let / Airbnb operators
- Commercial-only buildings
- Student hostels are covered in the students/owners cohorts, not in the landlord cohort

## Engine version

Generated by {ENGINE} on {today}.

""")

    # 3-6. Per-cohort findings
    chapter_num = 3
    for cohort in COHORTS:
        title = COHORT_TITLES[cohort]
        parts.append(f"# {chapter_num}. {title}\n\n")
        cohort_dir = project_root / cohort

        # Pain-points / complaints report
        report_file = cohort_dir / "research" / "pain-points-report.md"
        if not report_file.exists():
            report_file = cohort_dir / "research" / "complaints-report.md"
        parts.append(f"## {chapter_num}.1 Pain-points report\n\n")
        parts.append(section(read(report_file), levels=2))

        # Themes
        parts.append(f"## {chapter_num}.2 Theme taxonomy\n\n")
        parts.append(section(read(cohort_dir / "analysis" / "themes.md"), levels=2))

        # By country
        parts.append(f"## {chapter_num}.3 Country-by-country breakdown\n\n")
        parts.append(section(read(cohort_dir / "analysis" / "by-country.md"), levels=2))

        # Cohort-specific extras
        if cohort == "students":
            parts.append(f"## {chapter_num}.4 Named hostels\n\n")
            parts.append(section(read(cohort_dir / "analysis" / "named-hostels.md"), levels=2))
        elif cohort == "owners":
            parts.append(f"## {chapter_num}.4 Academic publications\n\n")
            parts.append(section(read(cohort_dir / "research" / "academic-publications.md"), levels=2))
        elif cohort == "landlords":
            parts.append(f"## {chapter_num}.4 PropTech landscape\n\n")
            parts.append(section(read(cohort_dir / "analysis" / "proptech-landscape.md"), levels=2))
        elif cohort == "tenants":
            parts.append(f"## {chapter_num}.4 Vulnerable groups\n\n")
            parts.append(section(read(cohort_dir / "analysis" / "vulnerable-groups.md"), levels=2))

        # Opportunities
        parts.append(f"## {chapter_num}.{5 if cohort != 'students' else 5} Cohort-specific product opportunities\n\n")
        parts.append(section(read(cohort_dir / "opportunities" / "product-ideas.md"), levels=2))

        chapter_num += 1

    # 7. Cross-cohort synthesis
    parts.append(f"# {chapter_num}. Cross-Cohort Synthesis\n\n")
    parts.append(section(read(project_root / "SYNTHESIS.md"), levels=1))
    chapter_num += 1

    # 8. Two-sided product opportunities (consolidated highlights)
    parts.append(f"# {chapter_num}. Two-Sided Product Opportunities\n\n")
    parts.append("""Cross-cohort synthesis (chapter 7) names nine two-sided product hypotheses. The five highest-leverage in cohort-coverage × severity terms:

1. **Deposit escrow + structured-inspection refund** — relieves tenants and students simultaneously; sharpest single hook (80% Uganda non-refund); cleanest legal anchor (UG L&T Act 2022; KE Tribunal Case E007/2024)
2. **Verified-listing marketplace + landlord KYC** — relieves tenants, students, and landlords; addresses 30% Uganda fake-listing rate
3. **Allowance-bridge financing** — relieves owners and students by closing the HELB / HESLB / Uganda-allowance gap
4. **University-collected rent rail** — relieves owners and students by mirroring the Kenyatta University PPP's most powerful feature
5. **Tenant rental-credit + landlord screening twin** — relieves tenants (counter-signal vs discrimination) and landlords (better screening than informal blacklists); addresses the discrimination loop

Detailed treatment in chapter 7. Per-cohort hypotheses in chapters 3.5, 4.5, 5.5, and 6.5.

""")
    chapter_num += 1

    # 9. Consolidated regulatory landscape
    parts.append(f"# {chapter_num}. Consolidated Regulatory Landscape\n\n")
    parts.append(section(read(project_root / "owners" / "analysis" / "regulatory-landscape.md"), levels=1))
    chapter_num += 1

    # 10. Academic & industry references
    parts.append(f"# {chapter_num}. Academic & Industry References\n\n")
    parts.append("The most rigorous tier-1 sources cited across the four cohorts. Full bibliography in chapter 12.\n\n")
    parts.append(section(read(project_root / "owners" / "research" / "academic-publications.md"), levels=1))
    chapter_num += 1

    # 11. Quotes appendix
    parts.append(f"# {chapter_num}. Quotes Appendix\n\n")
    parts.append("Verbatim attributable quotes pulled from the corpus, organised by cohort.\n\n")
    for cohort in COHORTS:
        parts.append(f"## {COHORT_TITLES[cohort]}\n\n")
        parts.append(section(read(project_root / cohort / "research" / "quotes.md"), levels=2))
    chapter_num += 1

    # 12. Source bibliography (tiered)
    parts.append(f"# {chapter_num}. Source Bibliography\n\n")
    parts.append("Annotated source list per cohort. See each cohort's `research/sources.md` for the canonical version. Sources are grouped by type (academic, regulatory, news, industry, social) within each cohort.\n\n")
    for cohort in COHORTS:
        parts.append(f"## {COHORT_TITLES[cohort]}\n\n")
        parts.append(section(read(project_root / cohort / "research" / "sources.md"), levels=2))
    chapter_num += 1

    # 13. Glossary
    parts.append(f"# {chapter_num}. Glossary\n\n")
    parts.append("""| Term | Definition |
|---|---|
| **AREA Uganda** | Association of Real Estate Agents Uganda |
| **BPRT** | Business Premises Rent Tribunal (Kenya) |
| **CAHF** | Centre for Affordable Housing Finance Africa |
| **CRB** | Credit Reference Bureau |
| **DAWASA** | Dar es Salaam Water and Sewerage Authority |
| **dalali** | Tanzanian informal property broker |
| **DBFOT** | Design–Build–Finance–Operate–Transfer (PPP model) |
| **EARB** | Estate Agents Registration Board (Kenya) |
| **eRITS** | Electronic Rental Income Tax System (KRA, launched April 2025) |
| **HELB** | Higher Education Loans Board (Kenya) |
| **HESLB** | Higher Education Students' Loans Board (Tanzania) |
| **IGC** | International Growth Centre |
| **IRA** | Insurance Regulatory Authority (Kenya / Uganda) |
| **KCCA** | Kampala Capital City Authority |
| **KMRC** | Kenya Mortgage Refinance Company |
| **KNBS** | Kenya National Bureau of Statistics |
| **KPDA** | Kenya Property Developers Association |
| **KPLC** | Kenya Power and Lighting Company |
| **L&T Act 2022** | Landlord and Tenant Act, 2022 (Uganda) |
| **MTI** | Means Testing Instrument (Kenya HE funding model) |
| **MUBS** | Makerere University Business School |
| **muzigo** | Ugandan term for a small one-room rental unit |
| **NCWSC** | Nairobi City Water and Sewerage Company |
| **NEMA** | National Environment Management Authority (Kenya / Uganda) |
| **NSSF** | National Social Security Fund |
| **NWSC** | National Water and Sewerage Corporation (Uganda) |
| **OSINT** | Open-Source Intelligence |
| **PBSA** | Purpose-Built Student Accommodation |
| **PPP** | Public–Private Partnership |
| **PWD** | Person with Disability |
| **REIT** | Real Estate Investment Trust |
| **SHIF** | Social Health Insurance Fund (Kenya, formerly NHIF) |
| **TANESCO** | Tanzania Electric Supply Company |
| **UBO** | Ultimate Beneficial Owner |
| **ULII** | Uganda Legal Information Institute |
| **UMEME** | Uganda's main electricity distributor |
| **UoN** | University of Nairobi |
| **URA** | Uganda Revenue Authority |
| **UR Huye** | University of Rwanda Huye Campus |

---

*Report generated by {engine} on {date}. Repository: https://github.com/peterbamuhigire/digital-research-skills*
""".format(engine=ENGINE, date=today))

    return "\n".join(parts)


def render_docx(master_md: Path, out_docx: Path) -> None:
    cmd = [
        "pandoc",
        str(master_md),
        "-o", str(out_docx),
        "--from=markdown",
        "--to=docx",
        "--toc",
        "--toc-depth=3",
        "--number-sections",
        "--standalone",
    ]
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    today = dt.date.today().isoformat()
    out_docx = Path(args.out) if args.out else project_root / f"report-v1-{today}.docx"
    master_md = project_root / "tools" / f"_master-{today}.md"

    print(f"Project root: {project_root}")
    print(f"Master markdown: {master_md}")
    print(f"Output: {out_docx}")

    md = assemble_master(project_root)
    master_md.write_text(md, encoding="utf-8")
    print(f"Master markdown written: {len(md):,} chars")

    render_docx(master_md, out_docx)
    print(f"Word doc rendered: {out_docx}")
    print(f"Size: {out_docx.stat().st_size:,} bytes")

    return 0


if __name__ == "__main__":
    sys.exit(main())
