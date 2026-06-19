from __future__ import annotations

import json
import re
import shutil
import zipfile
from collections import defaultdict
from copy import deepcopy
from pathlib import Path
from typing import Any

import xlsxwriter


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "projects" / "healthcare-app-clinical-data"
OUTPUT = PROJECT / "05-output" / "medic8-global-settings-v4"
EXPORT = PROJECT / "export" / "medic8-global-settings-v4"
DATE = "2026-05-07"
VERSION = "v4"

COMMON_COLUMNS = [
    "row_key",
    "stable_code",
    "display_name",
    "country_applicability",
    "source_url",
    "source_citation_text",
    "accessed_date",
    "licence_class",
    "curator_status_recommendation",
    "gap_flags",
    "owner_role",
    "facility_confirmation_required",
    "preconfigure_scope",
    "fail_closed_reason",
]

HARD_BLOCK = (
    "HARD CONSTRAINT - NO HALLUCINATION:\n"
    "- Do NOT invent statistics, names, organisations, court cases, statutes, or URLs.\n"
    "- Cite every numeric claim and every direct quote at the point it appears.\n"
    "- If you cannot find a source for a fact, mark it as a \"gap\" - do not fabricate filler.\n"
    "- For any claim you assemble from multiple sources, mark it \"(synthesis)\".\n"
    "- For any inference, mark it \"(inference)\".\n"
    "- Verbatim quotes must reproduce text exactly as it appeared in the source - no creative editing.\n"
    "- If a search returns nothing, report \"no source found\" - do not write what is plausible."
)


SOURCES: dict[str, dict[str, str]] = {
    "ucum": {
        "url": "https://ucum.org/ucum",
        "citation": "Regenstrief Institute, Unified Code for Units of Measure (UCUM) specification; used for canonical unit codes and safe conversion edges.",
        "licence": "open-standard-use-with-attribution",
    },
    "hl7-fhir-questionnaire": {
        "url": "https://hl7.org/fhir/R4/questionnaire.html",
        "citation": "HL7 FHIR R4 Questionnaire resource; used as the interoperable JSON form structure.",
        "licence": "HL7-FHIR-license",
    },
    "ug-country-local": {
        "url": "projects/healthcare-app-clinical-data/country-packs/research/wave1-data.md",
        "citation": "Project country-pack Wave 1 table for Uganda, citing Uganda MoH, statutory councils, NIRA, PDPO, HMIS and IDSR sources.",
        "licence": "project-research-corpus",
    },
    "ke-country-local": {
        "url": "projects/healthcare-app-clinical-data/country-packs/research/wave1-data.md",
        "citation": "Project country-pack Wave 1 table for Kenya, citing Kenya MoH, statutory councils, ODPC, SHA, KHIS/DHIS2 and Kenya legal sources.",
        "licence": "project-research-corpus",
    },
    "ug-dppa": {
        "url": "https://ulii.org/akn/ug/act/2019/9/eng@2019-05-03",
        "citation": "Uganda Data Protection and Privacy Act, 2019 text on ULII; used for Uganda privacy-law and breach-notification handling.",
        "licence": "official-legal-text",
    },
    "ke-odpc-breach": {
        "url": "https://www.odpc.go.ke/report-a-data-breach/",
        "citation": "Kenya Office of the Data Protection Commissioner breach-reporting page; used for the 72-hour breach reporting control.",
        "licence": "official-government-web",
    },
    "ke-health-act": {
        "url": "https://new.kenyalaw.org/akn/ke/act/2017/21/eng@2017-06-30",
        "citation": "Kenya Health Act, 2017 on Kenya Law; used for health-sector governance context.",
        "licence": "official-legal-text",
    },
    "ke-sha-tariffs": {
        "url": "https://health.go.ke/sites/default/files/2024-11/TARIFFS%20TO%20THE%20BENEFIT%20PACKAGE%20TO%20THE%20SHI.pdf",
        "citation": "Kenya Ministry of Health tariff schedule to the benefit package under the Social Health Insurance Act; used for SHA amount rows where the PDF publishes amounts.",
        "licence": "official-government-pdf",
    },
    "ug-hmis-local": {
        "url": "projects/healthcare-app-clinical-data/_context/sources-cache/uganda-hmis-107.md",
        "citation": "Cached Uganda HMIS 107/HMIS source notes; used for Uganda HMIS forms and reporting outputs.",
        "licence": "project-source-cache",
    },
    "ug-idsr-local": {
        "url": "projects/healthcare-app-clinical-data/_context/sources-cache/uganda-idsr.md",
        "citation": "Cached Uganda IDSR guideline notes; used for surveillance forms, workflows and notifiable-disease reporting dependencies.",
        "licence": "project-source-cache",
    },
    "workflows-local": {
        "url": "projects/healthcare-app-clinical-data/workflows/research/wave1-data.md",
        "citation": "Project workflow Wave 1 table for Uganda and Kenya clinical and operational workflows.",
        "licence": "project-research-corpus",
    },
    "forms-local": {
        "url": "projects/healthcare-app-clinical-data/standard-forms/research/wave1-data.md",
        "citation": "Project standard-forms Wave 1 table for Uganda HMIS, IDSR, HIV, ANC, maternity, commodities and related forms.",
        "licence": "project-research-corpus",
    },
    "kpis-local": {
        "url": "projects/healthcare-app-clinical-data/reporting-kpis/research/wave1-data.md",
        "citation": "Project reporting-KPI Wave 1 table defining facility indicators, numerators, denominators, forms and workflows for Uganda and Kenya.",
        "licence": "project-research-corpus",
    },
    "blueprints-local": {
        "url": "projects/healthcare-app-clinical-data/tenant-blueprints/research/wave1-data.md",
        "citation": "Project tenant-blueprints Wave 1 integration table tying countries, facilities, roles, workflows, forms, KPIs, inventories and tariff packs.",
        "licence": "project-research-corpus",
    },
    "billing-local": {
        "url": "projects/healthcare-app-clinical-data/billing-tariffs/research/wave1-data.md",
        "citation": "Project billing Wave 1 table for Uganda and Kenya charge item categories, payer mappings and source/gap discipline.",
        "licence": "project-research-corpus",
    },
    "who-surgical-checklist": {
        "url": "https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery/tool-and-resources",
        "citation": "World Health Organization safe surgery checklist resources; used for theatre/procedure workflow guardrails.",
        "licence": "official-WHO-publication",
    },
}


def source(source_id: str) -> dict[str, str]:
    return SOURCES[source_id]


def clean_cell(value: str) -> str:
    value = re.sub(r"<br\s*/?>", "\n", str(value), flags=re.I)
    value = re.sub(r"`([^`]*)`", r"\1", value)
    return (
        value.strip()
        .replace("**", "")
        .replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("â€“", "-")
        .replace("â€”", "-")
        .replace("â‰¥", ">=")
        .replace("â‰ˆ", "~")
        .replace("Âµ", "u")
    )


def split_row(line: str) -> list[str]:
    row = line.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    cells: list[str] = []
    cur: list[str] = []
    escaped = False
    for ch in row:
        if escaped:
            cur.append(ch)
            escaped = False
        elif ch == "\\":
            escaped = True
        elif ch == "|":
            cells.append(clean_cell("".join(cur)))
            cur = []
        else:
            cur.append(ch)
    cells.append(clean_cell("".join(cur)))
    return cells


def markdown_tables(path: Path) -> list[tuple[list[str], list[dict[str, str]]]]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    tables: list[tuple[list[str], list[dict[str, str]]]] = []
    i = 0
    sep_re = re.compile(r"^\|\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
    while i < len(lines) - 1:
        if lines[i].lstrip().startswith("|") and sep_re.match(lines[i + 1]):
            headers = split_row(lines[i])
            rows: list[dict[str, str]] = []
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                vals = split_row(lines[i])
                rows.append({headers[j]: vals[j] if j < len(vals) else "" for j in range(len(headers))})
                i += 1
            tables.append((headers, rows))
        else:
            i += 1
    return tables


def row_base(
    row_key: str,
    code: str,
    name: str,
    country: str,
    source_id: str,
    status: str,
    owner: str,
    facility_confirmation: str,
    scope: str,
    gap_flags: list[str] | None = None,
    fail_closed_reason: str = "",
) -> dict[str, Any]:
    src = source(source_id)
    return {
        "row_key": row_key,
        "stable_code": code,
        "display_name": name,
        "country_applicability": country,
        "source_url": src["url"],
        "source_citation_text": src["citation"],
        "accessed_date": DATE,
        "licence_class": src["licence"],
        "curator_status_recommendation": status,
        "gap_flags": gap_flags or [],
        "owner_role": owner,
        "facility_confirmation_required": facility_confirmation,
        "preconfigure_scope": scope,
        "fail_closed_reason": fail_closed_reason,
    }


def safe_key(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").upper()
    return cleaned or "ROW"


def build_ucum() -> dict[str, Any]:
    tables = markdown_tables(PROJECT / "ucum" / "research" / "wave1-data.md")
    master = []
    edges = []
    for _, rows in tables:
        if rows and "uom_code" in rows[0]:
            master = rows
        if rows and "from_uom" in rows[0]:
            edges = rows
    edge_map: dict[str, list[dict[str, str]]] = defaultdict(list)
    for edge in edges:
        if "GAP" in edge.get("from_uom", ""):
            continue
        edge_map[edge["from_uom"]].append(edge)
        edge_map[edge["to_uom"]].append({
            "from_uom": edge["to_uom"],
            "to_uom": edge["from_uom"],
            "factor": edge["factor"],
            "offset": edge["offset"],
            "formula_notes": f"Reverse relation of {edge['from_uom']} to {edge['to_uom']}; use with dimensional validation.",
            "source_citations": edge["source_citations"],
        })
    rows_out = []
    for row in master:
        code = row["uom_code"]
        gap = "GAP" in " ".join(row.values())
        base = row_base(
            f"UOM-{safe_key(code)}",
            code,
            row["uom_display"],
            "Global",
            "ucum",
            "candidate" if gap else "active",
            "Platform admin",
            "No; facility may choose display aliases only.",
            "Preconfigure globally before clinical catalogue import.",
            ["substance_specific_conversion"] if gap else [],
            "Do not auto-convert without substance-specific table." if gap else "",
        )
        base.update({
            "canonical_ucum_code": code,
            "display": row["uom_display"],
            "aliases": [x.strip() for x in row["common_aliases"].split(",") if x.strip()],
            "unit_kind": row["category"],
            "base_unit": row["base_uom_in_category"],
            "si_flag": "true" if row["category"] in {"Mass", "Volume", "Length", "Time", "Pressure", "Temperature", "Energy"} else "contextual",
            "conversion_factor_to_base": row["conversion_factor_to_base"],
            "conversion_offset_to_base": row["conversion_offset_to_base"],
            "used_in_cohorts": [x.strip() for x in row["used_in_cohorts"].split(",") if x.strip()],
            "conversion_relations_json": edge_map.get(code, []),
        })
        rows_out.append(base)
    return {"slug": "ucum-units", "title": "UCUM / Units", "rows": rows_out, "extra_sheets": {"Conversion Edges": edges}}


def build_country_packs() -> dict[str, Any]:
    ug = row_base("COUNTRY-UG", "UG", "Uganda country pack", "UG", "ug-country-local", "active", "Platform admin / compliance lead", "Yes for facility licence, reporting IDs and local consent SOP.", "Preconfigure as Uganda first-launch country pack.", ["fixed_hour_breach_sla_not_verified", "facility_record_retention_policy_required"], "For legal fields without a verified national numeric default, require facility policy confirmation before go-live.")
    ug.update({
        "currency_code": "UGX",
        "currency_minor_units": 0,
        "timezone": "Africa/Kampala",
        "languages_json": ["English", "Swahili", "Luganda"],
        "health_ministry": "Ministry of Health Uganda",
        "medicine_regulator": "National Drug Authority; Pharmacy Council of Uganda",
        "nursing_council": "Uganda Nurses and Midwives Council",
        "clinical_officer_council": "Allied Health Professionals Council",
        "lab_regulator": "Allied Health Professionals Council for laboratory cadres; facility accreditation policy must be confirmed.",
        "insurance_regulator": "No statutory national health insurance payer tariff activated in this pack; private insurance contracts are facility-specific.",
        "privacy_authority": "Personal Data Protection Office",
        "privacy_law": "Data Protection and Privacy Act, 2019",
        "breach_sla_rule": "Notify the Authority immediately where the breach is likely to result in risk or harm; no fixed hour value is activated.",
        "clinical_record_retention_rule": "Facility record-retention schedule required before production go-live; no national fixed-year default activated by this pack.",
        "consent_thresholds_json": {"minor_threshold_years": None, "activation_rule": "facility policy and applicable law confirmation required"},
        "national_id_rules_json": [{"kind": "NIN", "issuer": "NIRA"}, {"kind": "birth_registration_number", "issuer": "NIRA"}],
        "licence_number_formats_json": [{"cadre": "medical_dental", "lookup_url": "https://www.ehealthlicense.go.ug/index.php/search/cadre"}, {"cadre": "allied_health", "lookup_url": "https://www.ehealthlicense.go.ug/index.php/search/cadre"}],
        "mandatory_reports_json": ["HMIS-105", "HMIS-107", "HMIS-108", "HMIS-106A", "HMIS-033A", "HMIS-033B", "HMIS-033C"],
        "hmis_dhis2_references_json": ["Uganda HMIS/DHIS2", "mTrac/eIDSR"],
    })
    ke = row_base("COUNTRY-KE", "KE", "Kenya country pack", "KE", "ke-country-local", "active", "Platform admin / compliance lead", "Yes for county, facility code, licences, SHA status and local consent SOP.", "Preconfigure as Kenya first-launch country pack.", ["facility_record_retention_policy_required", "khis_field_mapping_required"], "KHIS field mapping and facility-specific SHA/provider credentials must be confirmed before production claims.")
    ke.update({
        "currency_code": "KES",
        "currency_minor_units": 2,
        "timezone": "Africa/Nairobi",
        "languages_json": ["English", "Kiswahili"],
        "health_ministry": "Ministry of Health Kenya",
        "medicine_regulator": "Pharmacy and Poisons Board",
        "nursing_council": "Nursing Council of Kenya",
        "clinical_officer_council": "Clinical Officers Council",
        "lab_regulator": "Kenya Medical Laboratory Technicians and Technologists Board",
        "insurance_regulator": "Social Health Authority; Insurance Regulatory Authority for private insurers",
        "privacy_authority": "Office of the Data Protection Commissioner",
        "privacy_law": "Data Protection Act, 2019",
        "breach_sla_rule": "Report personal-data breach to ODPC within 72 hours after becoming aware.",
        "clinical_record_retention_rule": "Facility record-retention schedule required before production go-live; no fixed-year default activated by this pack.",
        "consent_thresholds_json": {"minor_threshold_years": None, "activation_rule": "facility policy and applicable law confirmation required"},
        "national_id_rules_json": [{"kind": "Maisha_Namba", "issuer": "National Registration Bureau / Directorate of Immigration Services"}, {"kind": "Maisha_Card", "issuer": "National Registration Bureau / Directorate of Immigration Services"}],
        "licence_number_formats_json": [{"cadre": "medical_dental", "lookup_url": "https://kmpdc.go.ke/registers-practitioners-php/"}, {"cadre": "clinical_officer", "lookup_url": "https://clinicalofficerscouncil.org/"}],
        "mandatory_reports_json": ["KHIS/DHIS2 monthly facility reports", "IDSR reports", "SHA claims where enrolled"],
        "hmis_dhis2_references_json": ["Kenya KHIS on DHIS2", "Kenya Master Health Facility List"],
    })
    stub_rows = []
    for code, name, cur, tz, langs in [
        ("TZ", "Tanzania", "TZS", "Africa/Dar_es_Salaam", ["Swahili", "English"]),
        ("RW", "Rwanda", "RWF", "Africa/Kigali", ["Kinyarwanda", "English", "French", "Swahili"]),
        ("GH", "Ghana", "GHS", "Africa/Accra", ["English"]),
        ("NG", "Nigeria", "NGN", "Africa/Lagos", ["English", "Hausa", "Yoruba", "Igbo"]),
        ("ZA", "South Africa", "ZAR", "Africa/Johannesburg", ["English", "Zulu", "Xhosa", "Afrikaans"]),
        ("IN", "India", "INR", "Asia/Kolkata", ["Hindi", "English"]),
        ("PH", "Philippines", "PHP", "Asia/Manila", ["Filipino", "English"]),
        ("CD", "Democratic Republic of Congo", "CDF", "Africa/Kinshasa; Africa/Lubumbashi", ["French", "Lingala", "Swahili", "Kongo", "Tshiluba"]),
    ]:
        r = row_base(f"COUNTRY-{code}", code, f"{name} country stub", code, "ug-country-local", "stub", "Platform admin", "Yes; not in v4 launch scope.", "Do not preconfigure for UG/KE launch.", ["out_of_scope_for_ug_ke_v4"], "Stub country; not allowed for onboarding until fully verified.")
        r.update({"currency_code": cur, "timezone": tz, "languages_json": langs})
        stub_rows.append(r)
    return {"slug": "country-packs", "title": "Country Packs", "rows": [ug, ke] + stub_rows}


def build_holidays() -> dict[str, Any]:
    tables = markdown_tables(PROJECT / "holiday-calendars" / "research" / "wave1-data.md")
    holiday_rows = []
    for _, rows in tables:
        if rows and "holiday_id" in rows[0]:
            holiday_rows = rows
            break
    out = []
    for row in holiday_rows:
        if row.get("country_iso2") not in {"UG", "KE"}:
            continue
        movable = row.get("is_lunar_calculated") == "true" or row.get("holiday_kind") in {"MUSLIM", "CHRISTIAN"}
        status = "candidate" if row.get("is_lunar_calculated") == "true" else "active"
        sid = "ug-country-local" if row["country_iso2"] == "UG" else "ke-country-local"
        base = row_base(
            f"HOL-{row['holiday_id']}",
            row["holiday_id"],
            f"{row['holiday_name_en']} {row['year']}",
            row["country_iso2"],
            sid,
            status,
            "Facility admin",
            "Yes for local closure days and gazetted substitutions.",
            "Preload national calendar for scheduling; movable holidays require annual review.",
            ["movable_or_lunar_date_requires_confirmation"] if row.get("is_lunar_calculated") == "true" else [],
            "Movable/religious holiday dates must be confirmed against annual government gazette before production use." if row.get("is_lunar_calculated") == "true" else "",
        )
        base.update({
            "year": row["year"],
            "date_observed": row["date_observed"],
            "holiday_name_local": row.get("holiday_name_local", ""),
            "holiday_kind": row.get("holiday_kind", ""),
            "is_lunar_calculated": row.get("is_lunar_calculated", ""),
            "is_substitute_day": row.get("is_substitute_day", ""),
            "substitute_day_rule": "Use official gazetted observed date; do not auto-create substitutes without country notice.",
            "uncertain_movable_holiday": str(row.get("is_lunar_calculated") == "true").lower(),
            "observed_by_government": row.get("observed_by_government", ""),
            "typically_observed_by_facility": row.get("typically_observed_by_facility", ""),
            "original_source_citations": row.get("source_citations", ""),
        })
        out.append(base)
    return {"slug": "holiday-calendars", "title": "Holiday Calendars", "rows": out}


def workflow_steps(kind: str) -> list[dict[str, str]]:
    templates = {
        "registration": [("Reception clerk", "PATIENT_REGISTER", "patient demographics and ID evidence", "patient record and visit created"), ("Records officer", "PATIENT_VIEW", "duplicate check", "unique facility ID confirmed")],
        "triage": [("Nurse", "OPD_TRIAGE", "vitals and danger signs", "acuity category"), ("Clinical officer", "OPD_CONSULT", "red/yellow escalation", "urgent review or routine queue")],
        "opd": [("Clinical officer", "OPD_CONSULT", "triage note and complaint", "diagnosis, orders, prescription or referral"), ("Records officer", "PATIENT_VIEW", "completed encounter", "OPD register output")],
        "prescription": [("Prescriber", "OPD_PRESCRIBE", "medication order", "signed prescription"), ("Pharmacy", "PHARMACY_VERIFY", "allergy/DDI/stock check", "dispense or prescriber query")],
        "dispensing": [("Pharmacy", "PHARMACY_DISPENSE", "verified prescription", "labelled medicine and stock decrement"), ("Cashier", "PAYMENT_RECEIVE", "chargeable item", "receipt if prepayment is enabled")],
        "lab": [("Clinician", "LAB_REQUEST", "test order and indication", "lab request"), ("Lab technologist", "LAB_RESULT_VERIFY", "specimen and result", "verified result returned")],
        "imaging": [("Clinician", "IMAGING_REQUEST", "study request and indication", "imaging order"), ("Radiographer", "IMAGING_REPORT", "image acquisition and report", "signed report returned")],
        "billing": [("Billing clerk", "BILLING_CREATE", "service event", "invoice"), ("Cashier", "PAYMENT_RECEIVE", "payment", "receipt and ledger entry")],
        "immunisation": [("Nurse", "OPD_TRIAGE", "eligible child/adult and vaccine stock", "immunisation event"), ("Records officer", "REPORT_SUBMIT", "immunisation event", "EPI/HMIS summary")],
        "anc": [("Midwife", "ANC_REGISTER", "pregnancy registration", "ANC visit note"), ("Lab/pharmacy", "LAB_REQUEST", "ANC screening and supplements", "results and dispensing")],
        "ipd": [("Clinician", "IPD_ADMIT", "admission decision", "bed assignment and admission orders"), ("Clinician", "IPD_DISCHARGE", "discharge readiness", "signed discharge summary")],
        "procedure": [("Clinician", "PROCEDURE_PERFORM", "procedure indication and consent", "procedure record"), ("Theatre nurse", "THEATRE_RECORD", "WHO checklist and counts", "signed theatre/procedure log")],
        "reporting": [("M&E lead", "REPORT_SUBMIT", "period close data", "HMIS/KHIS report"), ("Facility director", "REPORT_VIEW", "validation summary", "signed submission")],
    }
    return [{"step_order": str(i + 1), "actor_role": a, "required_permission": p, "inputs": inp, "outputs": out, "audit_event": f"{kind}.{i + 1}"} for i, (a, p, inp, out) in enumerate(templates[kind])]


def build_workflows() -> dict[str, Any]:
    workflow_defs = [
        ("WF-REG-001", "Patient registration", "registration", "registration", "none"),
        ("WF-TRI-001", "Triage", "triage", "outpatient", "none"),
        ("WF-OPD-001", "OPD consultation", "opd", "outpatient", "after_registration"),
        ("WF-RX-001", "Prescription", "prescription", "pharmacy", "before_dispensing_if_cash"),
        ("WF-DISP-001", "Dispensing", "dispensing", "pharmacy", "before_handover_if_cash"),
        ("WF-LAB-001", "Lab order/result", "lab", "lab", "before_specimen_collection_if_cash"),
        ("WF-IMG-001", "Imaging order/result", "imaging", "imaging", "before_study_if_cash"),
        ("WF-BIL-001", "Billing/payment", "billing", "billing", "on_chargeable_event"),
        ("WF-IMM-001", "Immunisation", "immunisation", "mch", "none_for_public_programme"),
        ("WF-ANC-001", "Antenatal care", "anc", "mch", "none_for_public_programme_or_before_paid_package"),
        ("WF-IPD-001", "IPD admission/discharge", "ipd", "inpatient", "deposit_or_credit_approval_if_private"),
        ("WF-PRC-001", "Theatre/procedure", "procedure", "procedure", "before_elective_procedure_if_cash"),
        ("WF-REP-001", "Statutory reporting", "reporting", "reporting", "none"),
        ("WF-IDS-001", "IDSR notification", "reporting", "surveillance", "none"),
    ]
    rows = []
    for code, name, kind, module, trigger in workflow_defs:
        sid = "who-surgical-checklist" if code == "WF-PRC-001" else "workflows-local"
        r = row_base(f"WORKFLOW-{code}", code, name, "UG;KE", sid, "active", "Medical director / operations lead", "Yes for actor assignments and payment policy.", "Preconfigure as launch workflow template.", [], "")
        steps = workflow_steps(kind if code != "WF-IDS-001" else "reporting")
        r.update({
            "module": module,
            "step_order_json": steps,
            "pre_payment_trigger": trigger,
            "inputs_json": sorted({s["inputs"] for s in steps}),
            "outputs_json": sorted({s["outputs"] for s in steps}),
            "audit_events_json": [s["audit_event"] for s in steps],
            "fallback_manual_path": "Paper form/register with later back-entry; retain timestamps and staff sign-off.",
        })
        rows.append(r)
    return {"slug": "workflows", "title": "Workflows", "rows": rows}


def questionnaire(code: str, title: str, items: list[tuple[str, str, str]]) -> dict[str, Any]:
    return {
        "resourceType": "Questionnaire",
        "id": code.lower().replace("_", "-"),
        "status": "draft",
        "title": title,
        "item": [{"linkId": link, "text": text, "type": typ, "required": True} for link, text, typ in items],
    }


def build_forms() -> dict[str, Any]:
    defs = [
        ("FORM-REG-001", "Registration form", "registration", "WF-REG-001", [("patient_name", "Patient name", "string"), ("date_of_birth", "Date of birth", "date"), ("sex", "Sex", "choice"), ("contact", "Contact", "string")]),
        ("FORM-CONSENT-001", "General consent form", "consent", "WF-REG-001", [("consent_type", "Consent type", "choice"), ("signed_by", "Signed by", "string"), ("date_signed", "Date signed", "date")]),
        ("FORM-TRI-001", "Triage form", "triage", "WF-TRI-001", [("temperature", "Temperature", "decimal"), ("bp", "Blood pressure", "string"), ("pulse", "Pulse", "integer"), ("acuity", "Acuity", "choice")]),
        ("FORM-OPD-001", "OPD note", "outpatient", "WF-OPD-001", [("chief_complaint", "Chief complaint", "text"), ("diagnosis", "Diagnosis", "string"), ("plan", "Plan", "text")]),
        ("FORM-RX-001", "Prescription", "pharmacy", "WF-RX-001", [("drug", "Drug", "string"), ("dose", "Dose", "string"), ("frequency", "Frequency", "string"), ("duration", "Duration", "string")]),
        ("FORM-LAB-REQ-001", "Lab request", "lab", "WF-LAB-001", [("test", "Test", "string"), ("specimen", "Specimen", "choice"), ("clinical_notes", "Clinical notes", "text")]),
        ("FORM-LAB-RES-001", "Lab result", "lab", "WF-LAB-001", [("result", "Result", "string"), ("unit", "Unit", "string"), ("verified_by", "Verified by", "string")]),
        ("FORM-IMG-REQ-001", "Imaging request", "imaging", "WF-IMG-001", [("study", "Study", "string"), ("indication", "Indication", "text"), ("urgency", "Urgency", "choice")]),
        ("FORM-IMG-REP-001", "Imaging report", "imaging", "WF-IMG-001", [("findings", "Findings", "text"), ("impression", "Impression", "text"), ("reported_by", "Reported by", "string")]),
        ("FORM-BILL-001", "Invoice and receipt", "billing", "WF-BIL-001", [("charge_item", "Charge item", "string"), ("amount", "Amount", "decimal"), ("payment_method", "Payment method", "choice")]),
        ("FORM-DIS-001", "Discharge summary", "inpatient", "WF-IPD-001", [("admission_diagnosis", "Admission diagnosis", "string"), ("discharge_diagnosis", "Discharge diagnosis", "string"), ("follow_up", "Follow-up", "text")]),
        ("FORM-DEATH-001", "Death certificate data capture", "mortality", "WF-IPD-001", [("immediate_cause", "Immediate cause", "string"), ("underlying_cause", "Underlying cause", "string"), ("certifier", "Certifier", "string")]),
        ("FORM-HMIS-UG-001", "Uganda HMIS report set", "reporting", "WF-REP-001", [("period", "Reporting period", "date"), ("form_code", "HMIS form code", "string"), ("submitted_by", "Submitted by", "string")]),
        ("FORM-KHIS-KE-001", "Kenya KHIS report set", "reporting", "WF-REP-001", [("period", "Reporting period", "date"), ("khis_dataset", "KHIS dataset", "string"), ("submitted_by", "Submitted by", "string")]),
        ("FORM-IMM-001", "Immunisation card/register", "immunisation", "WF-IMM-001", [("antigen", "Antigen", "string"), ("dose_number", "Dose number", "integer"), ("date_given", "Date given", "date")]),
        ("FORM-ANC-001", "ANC card/register", "anc", "WF-ANC-001", [("gravida", "Gravida", "integer"), ("gestational_age", "Gestational age", "integer"), ("visit_number", "Visit number", "integer")]),
    ]
    rows = []
    for code, name, domain, workflow, items in defs:
        sid = "forms-local" if code.startswith("FORM-HMIS") else ("ke-country-local" if code.startswith("FORM-KHIS") else "hl7-fhir-questionnaire")
        status = "candidate" if code == "FORM-KHIS-KE-001" else "active"
        flags = ["khis_dataset_mapping_required"] if code == "FORM-KHIS-KE-001" else []
        fail = "County/KHIS dataset fields must be confirmed before statutory submission." if flags else ""
        r = row_base(f"STD-{code}", code, name, "UG" if "UG" in code else ("KE" if "KE" in code else "UG;KE"), sid, status, "Records officer / M&E lead", "Yes for local paper equivalent and statutory dataset mapping.", "Preconfigure form template; submit statutory reports only after facility confirmation.", flags, fail)
        r.update({
            "domain": domain,
            "linked_workflow": workflow,
            "fhir_questionnaire_json": questionnaire(code, name, items),
            "paper_form_equivalent": "Facility paper form or national HMIS/KHIS equivalent",
            "dhis2_program_uid_per_country_json": {},
        })
        rows.append(r)
    return {"slug": "standard-forms", "title": "Standard Forms", "rows": rows}


def build_kpis() -> dict[str, Any]:
    defs = [
        ("KPI-OPD-001", "OPD visits", "count(OPD encounters)", "none", "Daily; monthly rollup", "All", "UG;KE", "WF-OPD-001", "FORM-OPD-001"),
        ("KPI-PAT-NEW-001", "New patients", "count(new patient registrations)", "none", "Daily; monthly rollup", "All", "UG;KE", "WF-REG-001", "FORM-REG-001"),
        ("KPI-REV-001", "Revenue billed", "sum(invoice total)", "none", "Daily; monthly rollup", "All", "UG;KE", "WF-BIL-001", "FORM-BILL-001"),
        ("KPI-PAY-001", "Payments received", "sum(receipts)", "none", "Daily; monthly rollup", "All", "UG;KE", "WF-BIL-001", "FORM-BILL-001"),
        ("KPI-AR-001", "Accounts receivable", "sum(open invoice balance)", "sum(invoice total)", "Daily", "Private/PNFP/hospitals", "UG;KE", "WF-BIL-001", "FORM-BILL-001"),
        ("KPI-STOCK-001", "Stockouts", "count(active stock items at zero or below reorder floor)", "count(active stock items)", "Daily; monthly rollup", "All with inventory", "UG;KE", "WF-STK-001", "FORM-HMIS-UG-001"),
        ("KPI-LAB-TAT-001", "Lab turnaround time", "median(result_verified_at - specimen_collected_at)", "none", "Daily; monthly rollup", "Facilities with lab", "UG;KE", "WF-LAB-001", "FORM-LAB-RES-001"),
        ("KPI-RX-001", "Prescription volume", "count(prescriptions signed)", "none", "Daily; monthly rollup", "All with pharmacy", "UG;KE", "WF-RX-001", "FORM-RX-001"),
        ("KPI-DDI-001", "DDI overrides", "count(DDI alerts overridden)", "count(DDI alerts shown)", "Daily; monthly rollup", "Facilities using CDS", "UG;KE", "WF-RX-001", "FORM-RX-001"),
        ("KPI-IMM-001", "Immunisations", "count(immunisation events)", "target cohort where configured", "Monthly", "Clinics and hospitals with EPI", "UG;KE", "WF-IMM-001", "FORM-IMM-001"),
        ("KPI-ANC-001", "ANC visits", "count(ANC contacts)", "estimated pregnancies where configured", "Monthly", "Clinics and hospitals with ANC", "UG;KE", "WF-ANC-001", "FORM-ANC-001"),
        ("KPI-ADM-001", "Admissions", "count(IPD admissions)", "none", "Daily; monthly rollup", "Hospitals", "UG;KE", "WF-IPD-001", "FORM-DIS-001"),
        ("KPI-DIS-001", "Discharges", "count(IPD discharges)", "count(IPD admissions)", "Daily; monthly rollup", "Hospitals", "UG;KE", "WF-IPD-001", "FORM-DIS-001"),
        ("KPI-BED-001", "Bed occupancy", "sum(occupied bed days)", "available beds * days in period", "Daily; monthly rollup", "Hospitals", "UG;KE", "WF-IPD-001", "FORM-DIS-001"),
    ]
    rows = []
    for code, name, num, den, cadence, levels, country, workflow, form in defs:
        r = row_base(f"KPI-{code}", code, name, country, "kpis-local", "active", "M&E lead", "Yes for local denominator settings and dashboard thresholds.", "Preconfigure launch dashboards; statutory submission requires country form mapping.", [], "")
        r.update({
            "numerator": num,
            "denominator": den,
            "cadence": cadence,
            "required_source_table_or_event": workflow.replace("WF-", "event."),
            "facility_levels": levels,
            "linked_workflow": workflow,
            "linked_form": form,
            "dashboard_default": "trend line plus current-period summary",
        })
        rows.append(r)
    return {"slug": "reporting-kpis", "title": "Reporting KPIs", "rows": rows}


def build_tariffs() -> dict[str, Any]:
    rows = []
    defs = [
        ("UG-CASH-CONSULT", "Consultation - facility cash baseline", "UG", "UGX", 0, None, "consultation", "patient_checked_in", "Consultation revenue", "candidate", ["facility_price_required"], "Facility must set private/PNFP cash price before charging."),
        ("UG-PUBLIC-OPD-ZERO", "Public OPD consultation no patient charge", "UG", "UGX", 0, 0, "consultation", "patient_checked_in", "Public service subsidy", "active", [], ""),
        ("UG-PUBLIC-MAT-ZERO", "Public maternity package no patient charge", "UG", "UGX", 0, 0, "maternity", "delivery_admission", "Public service subsidy", "active", [], ""),
        ("UG-CASH-LAB", "Lab test - facility cash baseline", "UG", "UGX", 0, None, "lab", "lab_ordered", "Laboratory revenue", "candidate", ["facility_price_required"], "Facility must set test-level price list before charging."),
        ("UG-CASH-IMG", "Imaging - facility cash baseline", "UG", "UGX", 0, None, "imaging", "imaging_ordered", "Imaging revenue", "candidate", ["facility_price_required"], "Facility must set modality/study price list before charging."),
        ("KE-SHA-PHF-OPD", "SHA PHF outpatient care services", "KE", "KES", 2, 90000, "consultation", "patient_checked_in", "SHA receivable", "candidate", ["claim_code_not_published"], "Use only after SHA facility credentials and claim-code table are confirmed."),
        ("KE-SHA-SHIF-OPD", "SHA SHIF outpatient visit", "KE", "KES", 2, 200000, "consultation", "patient_checked_in", "SHA receivable", "candidate", ["claim_code_not_published"], "Use only after SHA facility credentials and claim-code table are confirmed."),
        ("KE-SHA-L4-BED", "SHA Level 4 inpatient per diem", "KE", "KES", 2, 350000, "bed_day", "midnight_census", "SHA receivable", "candidate", ["claim_code_not_published"], "Use only after SHA facility credentials and claim-code table are confirmed."),
        ("KE-SHA-L5-BED", "SHA Level 5 inpatient per diem", "KE", "KES", 2, 400000, "bed_day", "midnight_census", "SHA receivable", "candidate", ["claim_code_not_published"], "Use only after SHA facility credentials and claim-code table are confirmed."),
        ("KE-SHA-NORMAL-DEL", "SHA normal delivery package", "KE", "KES", 2, 1120000, "maternity", "delivery_completed", "SHA receivable", "candidate", ["claim_code_not_published"], "Use only after SHA facility credentials and claim-code table are confirmed."),
        ("KE-SHA-CS", "SHA caesarean section package", "KE", "KES", 2, 3260000, "theatre", "caesarean_completed", "SHA receivable", "candidate", ["claim_code_not_published"], "Use only after SHA facility credentials and claim-code table are confirmed."),
        ("KE-CASH-CONSULT", "Consultation - facility cash baseline", "KE", "KES", 2, None, "consultation", "patient_checked_in", "Consultation revenue", "candidate", ["facility_price_required"], "Facility must set cash/private price before charging."),
        ("KE-CASH-LAB", "Lab test - facility cash baseline", "KE", "KES", 2, None, "lab", "lab_ordered", "Laboratory revenue", "candidate", ["facility_price_required"], "Facility must set test-level price list before charging."),
        ("KE-CASH-IMG", "Imaging - facility cash baseline", "KE", "KES", 2, None, "imaging", "imaging_ordered", "Imaging revenue", "candidate", ["facility_price_required"], "Facility must set modality/study price list before charging."),
    ]
    for code, name, country, currency, minor, amount, category, trigger, account, status, flags, fail in defs:
        sid = "ke-sha-tariffs" if code.startswith("KE-SHA") else "billing-local"
        r = row_base(f"TARIFF-{code}", code, name, country, sid, status, "Accountant", "Yes; prices, payer contracts and tax treatment are facility-specific.", "Preconfigure tariff skeletons; activate only rows with confirmed amount/payer.", flags, fail)
        r.update({
            "service_category": category,
            "currency_code": currency,
            "currency_minor_units": minor,
            "tariff_amount_minor": amount,
            "amount_activation_mode": "source_amount" if amount is not None else "facility_entered",
            "payer_type": "SHA" if code.startswith("KE-SHA") else ("public_no_patient_charge" if "ZERO" in code else "cash_self_pay"),
            "revenue_account_role": account,
            "billing_trigger": trigger,
            "insurance_payer_notes": "SHA amount row; claim code not activated in v4." if code.startswith("KE-SHA") else "Cash/public baseline row.",
        })
        rows.append(r)
    return {"slug": "billing-tariffs", "title": "Billing Tariffs", "rows": rows}


def build_blueprints() -> dict[str, Any]:
    base_modules = ["registration", "triage", "opd", "prescribing", "dispensing", "billing", "inventory", "reporting"]
    hospital_modules = base_modules + ["lab", "imaging", "ipd", "theatre", "maternity", "immunisation", "anc"]
    blueprint_defs = [
        ("BP-SMALL-CLINIC-UG", "Uganda small clinic", "UG", base_modules + ["lab-basic"], ["WORKFLOW-WF-REG-001", "WORKFLOW-WF-TRI-001", "WORKFLOW-WF-OPD-001", "WORKFLOW-WF-RX-001", "WORKFLOW-WF-DISP-001", "WORKFLOW-WF-BIL-001"], ["TARIFF-UG-CASH-CONSULT", "TARIFF-UG-PUBLIC-OPD-ZERO"]),
        ("BP-GEN-HOSPITAL-UG", "Uganda general hospital", "UG", hospital_modules, ["WORKFLOW-WF-REG-001", "WORKFLOW-WF-TRI-001", "WORKFLOW-WF-OPD-001", "WORKFLOW-WF-LAB-001", "WORKFLOW-WF-IMG-001", "WORKFLOW-WF-IPD-001", "WORKFLOW-WF-PRC-001", "WORKFLOW-WF-REP-001"], ["TARIFF-UG-PUBLIC-OPD-ZERO", "TARIFF-UG-PUBLIC-MAT-ZERO"]),
        ("BP-MISSION-HOSPITAL-UG", "Uganda mission hospital", "UG", hospital_modules + ["pnfp-cost-share"], ["WORKFLOW-WF-REG-001", "WORKFLOW-WF-TRI-001", "WORKFLOW-WF-OPD-001", "WORKFLOW-WF-LAB-001", "WORKFLOW-WF-IMG-001", "WORKFLOW-WF-IPD-001", "WORKFLOW-WF-PRC-001", "WORKFLOW-WF-BIL-001"], ["TARIFF-UG-CASH-CONSULT", "TARIFF-UG-CASH-LAB", "TARIFF-UG-CASH-IMG"]),
        ("BP-SMALL-CLINIC-KE", "Kenya small clinic", "KE", base_modules + ["lab-basic", "sha-eligibility"], ["WORKFLOW-WF-REG-001", "WORKFLOW-WF-TRI-001", "WORKFLOW-WF-OPD-001", "WORKFLOW-WF-RX-001", "WORKFLOW-WF-DISP-001", "WORKFLOW-WF-BIL-001"], ["TARIFF-KE-CASH-CONSULT", "TARIFF-KE-SHA-PHF-OPD"]),
        ("BP-L4-HOSPITAL-KE", "Kenya Level 4/5 hospital test path", "KE", hospital_modules + ["sha-claims"], ["WORKFLOW-WF-REG-001", "WORKFLOW-WF-TRI-001", "WORKFLOW-WF-OPD-001", "WORKFLOW-WF-LAB-001", "WORKFLOW-WF-IMG-001", "WORKFLOW-WF-IPD-001", "WORKFLOW-WF-PRC-001", "WORKFLOW-WF-BIL-001", "WORKFLOW-WF-REP-001"], ["TARIFF-KE-SHA-PHF-OPD", "TARIFF-KE-SHA-L4-BED", "TARIFF-KE-SHA-NORMAL-DEL", "TARIFF-KE-SHA-CS"]),
    ]
    rows = []
    for code, name, country, modules, workflows, tariffs in blueprint_defs:
        flags = ["facility_price_required"] if any("CASH" in t for t in tariffs) else []
        flags += ["sha_credentials_required"] if country == "KE" else []
        status = "active" if code in {"BP-SMALL-CLINIC-UG", "BP-GEN-HOSPITAL-UG"} else "candidate"
        fail = "Resolve flagged tariff/payer credentials before production go-live." if flags else ""
        r = row_base(f"BLUEPRINT-{code}", code, name, country, "blueprints-local", status, "Medic8 implementation lead", "Yes; facility services, staff, licences, prices, banks and reporting IDs must be confirmed.", "Executable setup recipe for one-hour onboarding rehearsal.", flags, fail)
        r.update({
            "enabled_modules_json": modules,
            "default_roles_json": ["Facility admin", "Reception/records", "Nurse", "Clinical officer/medical officer", "Pharmacy", "Cashier"] + (["Lab", "Radiographer", "Ward nurse", "Theatre nurse", "M&E lead"] if "ipd" in modules else []),
            "workflows_json": workflows,
            "forms_json": ["STD-FORM-REG-001", "STD-FORM-TRI-001", "STD-FORM-OPD-001", "STD-FORM-RX-001", "STD-FORM-BILL-001"] + (["STD-FORM-LAB-REQ-001", "STD-FORM-LAB-RES-001", "STD-FORM-DIS-001", "STD-FORM-ANC-001", "STD-FORM-IMM-001"] if "ipd" in modules else []),
            "kpis_json": ["KPI-KPI-OPD-001", "KPI-KPI-PAT-NEW-001", "KPI-KPI-REV-001", "KPI-KPI-PAY-001", "KPI-KPI-STOCK-001"] + (["KPI-KPI-ADM-001", "KPI-KPI-DIS-001", "KPI-KPI-BED-001", "KPI-KPI-LAB-TAT-001"] if "ipd" in modules else []),
            "starter_inventory_json": ["gloves", "syringes", "gauze", "rapid malaria tests", "basic antibiotics", "paracetamol", "oral rehydration salts"],
            "starter_formulary_json": ["amoxicillin", "paracetamol", "ORS", "artemether-lumefantrine", "metformin", "salbutamol"],
            "starter_lab_menu_json": ["malaria RDT", "haemoglobin", "urinalysis", "pregnancy test", "blood glucose"],
            "starter_imaging_procedure_list_json": ["chest X-ray", "obstetric ultrasound", "suturing", "incision and drainage"] if "imaging" in modules else ["suturing"],
            "tariff_pack_json": tariffs,
            "launch_checklist_json": ["country pack selected", "facility profile confirmed", "roles seeded", "opening balances entered", "stock counts entered", "workflows enabled", "price list selected", "go-live gate reviewed"],
            "expected_onboarding_steps_json": ["select blueprint", "confirm facility identity", "seed users", "select price list", "load starter stock", "run OPD smoke test", "review go-live gate"],
        })
        rows.append(r)
    return {"slug": "tenant-blueprints", "title": "Tenant Blueprints", "rows": rows}


def build_acceptance_fixtures(blueprints: list[dict[str, Any]]) -> dict[str, Any]:
    fixtures = []
    for bp in blueprints:
        code = bp["stable_code"]
        country = bp["country_applicability"]
        is_hospital = "ipd" in bp["enabled_modules_json"]
        fixtures.append({
            "fixture_id": f"{code}-ONBOARDING-60MIN",
            "blueprint_row_key": bp["row_key"],
            "timed_acceptance_target_minutes": 60,
            "synthetic_fixture": True,
            "initial_facility_profile": {
                "country_code": country,
                "facility_name": f"Medic8 Test {bp['display_name']}",
                "facility_level": "small_clinic" if not is_hospital else ("level_4_or_5_hospital" if country == "KE" else "general_or_mission_hospital"),
                "licence_number": "FACILITY-CONFIRMATION-REQUIRED",
            },
            "staff_roles": bp["default_roles_json"],
            "opening_balances": {"cash_minor": 0, "bank_minor": 0, "currency_code": "KES" if country == "KE" else "UGX"},
            "stock_locations": ["main_store", "dispensary"] + (["lab_store", "ward_store", "theatre_store"] if is_hospital else []),
            "starter_stock_counts": [{"item": item, "count": 10, "unit": "pack"} for item in bp["starter_inventory_json"]],
            "price_list_selections": bp["tariff_pack_json"],
            "enabled_workflows": bp["workflows_json"],
            "launch_checklist": bp["launch_checklist_json"],
            "expected_results": [
                {"step": "select blueprint", "expected": "blueprint dependencies resolved"},
                {"step": "seed users", "expected": "role count matches fixture"},
                {"step": "run OPD smoke test", "expected": "registration, triage, consult, prescription, billing events close without unresolved mandatory reference"},
                {"step": "go-live gate", "expected": "pass for test replay; production gate blocks if facility licence, price list or SHA credentials are still unconfirmed"},
            ],
        })
    return {"version": f"{VERSION}-{DATE}", "fixtures": fixtures}


def build_curator_worklist(cohorts: list[dict[str, Any]]) -> dict[str, Any]:
    items = []
    for cohort in cohorts:
        for row in cohort["rows"]:
            flags = row.get("gap_flags") or []
            if row["curator_status_recommendation"] == "active" and not flags:
                continue
            priority = "P0" if any(flag in {"facility_price_required", "sha_credentials_required", "claim_code_not_published", "khis_dataset_mapping_required"} for flag in flags) else ("P1" if flags else "P2")
            uncertainty = "legal/licensing" if any(x in " ".join(flags) for x in ["sha", "licence", "breach", "record_retention", "claim"]) else "clinical/enrichment"
            items.append({
                "priority": priority,
                "uncertainty_class": uncertainty,
                "cohort": cohort["slug"],
                "row_key": row["row_key"],
                "display_name": row["display_name"],
                "gap_flags": flags,
                "owner_role": row["owner_role"],
                "facility_confirmation_required": row["facility_confirmation_required"],
                "blocking_rule": row["fail_closed_reason"] or "Curator review before activation.",
            })
    must_active = [
        "COUNTRY-UG", "COUNTRY-KE",
        "WORKFLOW-WF-REG-001", "WORKFLOW-WF-TRI-001", "WORKFLOW-WF-OPD-001", "WORKFLOW-WF-RX-001", "WORKFLOW-WF-BIL-001",
        "STD-FORM-REG-001", "STD-FORM-TRI-001", "STD-FORM-OPD-001", "STD-FORM-RX-001", "STD-FORM-BILL-001",
        "KPI-KPI-OPD-001", "KPI-KPI-PAT-NEW-001", "KPI-KPI-REV-001", "KPI-KPI-PAY-001",
    ]
    return {"version": f"{VERSION}-{DATE}", "must_be_active_before_onboarding": must_active, "items": items}


def as_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=True, separators=(",", ":"))
    if value is None:
        return ""
    return str(value)


def write_sheet(workbook: Any, name: str, rows: list[dict[str, Any]]) -> None:
    ws = workbook.add_worksheet(re.sub(r"[\[\]:*?/\\]", "_", name)[:31])
    if not rows:
        ws.write(0, 0, "no_rows")
        return
    headers = COMMON_COLUMNS + [h for h in rows[0].keys() if h not in COMMON_COLUMNS]
    header_fmt = workbook.add_format({"bold": True, "bg_color": "#1F4E79", "font_color": "white", "border": 1})
    cell_fmt = workbook.add_format({"text_wrap": True, "valign": "top", "border": 1})
    ws.write_row(0, 0, headers, header_fmt)
    for r, row in enumerate(rows, 1):
        ws.write_row(r, 0, [as_cell(row.get(h, "")) for h in headers], cell_fmt)
    ws.freeze_panes(1, 0)
    ws.autofilter(0, 0, len(rows), len(headers) - 1)
    for idx, header in enumerate(headers):
        ws.set_column(idx, idx, min(max(len(header) + 4, 16), 54))


def write_workbook(cohort: dict[str, Any]) -> Path:
    path = OUTPUT / f"medic8-{cohort['slug']}-{VERSION}-{DATE}.xlsx"
    workbook = xlsxwriter.Workbook(str(path))
    readme = workbook.add_worksheet("README")
    readme.write("A1", cohort["title"])
    readme.write("A2", f"Version: {VERSION}-{DATE}")
    readme.write("A3", "Evidence rule")
    readme.write("B3", "No active row has placeholder GAP text; all active rows carry a source URL and citation text.")
    readme.write("A4", "Rows")
    readme.write("B4", len(cohort["rows"]))
    write_sheet(workbook, "Data", cohort["rows"])
    if cohort.get("extra_sheets"):
        for sheet_name, rows in cohort["extra_sheets"].items():
            write_sheet(workbook, sheet_name, rows)
    workbook.close()
    validate_office(path)
    return path


def write_json(cohort: dict[str, Any]) -> Path:
    path = OUTPUT / f"medic8-{cohort['slug']}-{VERSION}-{DATE}.json"
    payload = deepcopy(cohort)
    payload["version"] = f"{VERSION}-{DATE}"
    payload["hard_constraint_for_subtasks"] = HARD_BLOCK
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    return path


def validate_office(path: Path) -> None:
    with zipfile.ZipFile(path) as zf:
        bad = zf.testzip()
    if bad:
        raise RuntimeError(f"Invalid Office artifact {path}: {bad}")


def validate_active_rows(cohorts: list[dict[str, Any]]) -> list[str]:
    issues: list[str] = []
    for cohort in cohorts:
        for row in cohort["rows"]:
            text = json.dumps(row, ensure_ascii=True)
            if row["curator_status_recommendation"] == "active":
                if not row["source_url"] or not row["source_citation_text"]:
                    issues.append(f"{cohort['slug']}:{row['row_key']} missing source")
                if re.search(r"\[(?:P0\s+)?GAP|STUB", text, re.I):
                    issues.append(f"{cohort['slug']}:{row['row_key']} active row contains placeholder text")
    return issues


def build_cross_references(cohorts: list[dict[str, Any]]) -> dict[str, Any]:
    all_keys = {row["row_key"]: cohort["slug"] for cohort in cohorts for row in cohort["rows"]}
    refs = {}
    for cohort in cohorts:
        for row in cohort["rows"]:
            row_refs = []
            for value in row.values():
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, str) and item in all_keys:
                            row_refs.append({"token": item, "resolves_to": f"{all_keys[item]}[{item}]", "optional": False})
            if row_refs:
                refs[row["row_key"]] = row_refs
    return {"version": f"{VERSION}-{DATE}", "references": refs}


def write_handoff(cohorts: list[dict[str, Any]], worklist: dict[str, Any]) -> Path:
    p0 = [i for i in worklist["items"] if i["priority"] == "P0"]
    lines = [
        "# Medic8 v4 UG/KE Activation Pack Handoff",
        "",
        f"Generated: {DATE}",
        "",
        "## Status",
        "",
        "- UG small clinic: GO for timed onboarding replay; production charging still requires facility price confirmation if using private/PNFP cash tariffs.",
        "- UG general hospital: GO for timed onboarding replay; production go-live requires facility licence, reporting IDs, record-retention SOP and local price policy confirmation.",
        "- KE small clinic: GO for timed onboarding replay; production SHA claims remain blocked until SHA credentials and claim-code tables are confirmed.",
        "- KE Level 4/5 hospital: GO for timed onboarding replay; production claims and KHIS field submission are blocked pending facility/SHA/KHIS confirmation.",
        "",
        "## Remaining Blockers",
        "",
    ]
    if p0:
        for item in p0:
            lines.append(f"- {item['priority']} {item['uncertainty_class']}: {item['cohort']} {item['row_key']} - {item['blocking_rule']}")
    else:
        lines.append("- No P0 blockers detected by generator validation.")
    lines.extend([
        "",
        "## Active Row Gate",
        "",
        "Rows listed in `curator-worklist-v4-2026-05-07.json` under `must_be_active_before_onboarding` must remain active for any onboarding replay. Candidate billing/SHA/KHIS rows can be selected for testing, but production go-live must fail closed until their listed confirmations are complete.",
    ])
    path = OUTPUT / f"handoff-{VERSION}-{DATE}.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def copy_outputs(paths: list[Path]) -> None:
    EXPORT.mkdir(parents=True, exist_ok=True)
    for path in paths:
        dest = EXPORT / path.name
        shutil.copy2(path, dest)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    EXPORT.mkdir(parents=True, exist_ok=True)
    cohorts = [
        build_ucum(),
        build_country_packs(),
        build_holidays(),
        build_workflows(),
        build_forms(),
        build_kpis(),
        build_tariffs(),
    ]
    blueprints = build_blueprints()
    cohorts.append(blueprints)

    issues = validate_active_rows(cohorts)
    if issues:
        raise SystemExit("Active-row validation failed:\n" + "\n".join(issues))

    artifacts: list[Path] = []
    row_counts = {}
    for cohort in cohorts:
        row_counts[cohort["slug"]] = len(cohort["rows"])
        artifacts.append(write_workbook(cohort))
        artifacts.append(write_json(cohort))

    cross_refs = build_cross_references(cohorts)
    cross_path = OUTPUT / "cross-references.json"
    cross_path.write_text(json.dumps(cross_refs, indent=2, ensure_ascii=True), encoding="utf-8")
    artifacts.append(cross_path)

    fixtures = build_acceptance_fixtures(blueprints["rows"])
    fixtures_path = OUTPUT / "acceptance-fixtures.json"
    fixtures_path.write_text(json.dumps(fixtures, indent=2, ensure_ascii=True), encoding="utf-8")
    artifacts.append(fixtures_path)

    worklist = build_curator_worklist(cohorts)
    worklist_path = OUTPUT / f"curator-worklist-{VERSION}-{DATE}.json"
    worklist_path.write_text(json.dumps(worklist, indent=2, ensure_ascii=True), encoding="utf-8")
    artifacts.append(worklist_path)

    handoff = write_handoff(cohorts, worklist)
    artifacts.append(handoff)

    manifest = OUTPUT / f"manifest-{VERSION}-{DATE}.md"
    manifest.write_text(
        "\n".join([
            f"# Medic8 Global Settings {VERSION} Manifest",
            "",
            f"Generated: {DATE}",
            "",
            "## Row Counts",
            "",
            *[f"- {slug}: {count}" for slug, count in row_counts.items()],
            "",
            "## Artifacts",
            "",
            *[f"- `{path.name}`" for path in artifacts],
        ]) + "\n",
        encoding="utf-8",
    )
    artifacts.append(manifest)

    copy_outputs(artifacts)
    print(f"Generated {len(artifacts)} v4 artifacts")
    print(f"Output: {OUTPUT}")
    print(f"Export: {EXPORT}")
    for slug, count in row_counts.items():
        print(f"{slug}: {count}")


if __name__ == "__main__":
    main()
