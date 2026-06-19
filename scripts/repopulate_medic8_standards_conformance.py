from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import xlsxwriter


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "projects" / "healthcare-app-clinical-data"
OUTPUT = PROJECT / "05-output" / "medic8-global-settings"
EXPORT = PROJECT / "export" / "medic8-global-settings"
DATE = "2026-05-06"
VERSION = "v3"


def load_base_generator():
    path = ROOT / "scripts" / "generate_medic8_global_settings_outputs.py"
    spec = importlib.util.spec_from_file_location("medic8_base_generator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_base_generator()


@dataclass(frozen=True)
class StandardProfile:
    slug: str
    primary_standard: str
    primary_system_uri: str
    primary_code_field: str
    version_field: str
    display_fields: tuple[str, ...]
    value_set_uri: str
    fhir_resource: str
    output_rule: str
    required_fields: tuple[str, ...]
    alternate_fields: tuple[str, ...]
    facility_boundary: str


PROFILES: dict[str, StandardProfile] = {
    "tenant-blueprints": StandardProfile("tenant-blueprints", "Medic8 Blueprint ID", "https://medic8.local/fhir/CodeSystem/tenant-blueprint", "blueprint_id", "code_system_version", ("facility_type", "blueprint_name", "name"), "https://medic8.local/fhir/ValueSet/tenant-blueprints", "ImplementationGuide / PlanDefinition", "Blueprint outputs must reference standards-backed country, role, workflow, form, catalogue, and billing subsets.", ("blueprint_id",), ("country", "default_roles", "default_workflows", "required_forms", "linked_orders"), "Facility confirms legal entity, services, staff, licences, prices, and integrations."),
    "country-packs": StandardProfile("country-packs", "ISO 3166", "urn:iso:std:iso:3166", "country_code", "code_system_version", ("country_name", "country"), "https://medic8.local/fhir/ValueSet/country-packs", "Location / Organization", "Country output must include ISO country, ISO 4217 currency, timezone, regulator, privacy-law, and reporting identifiers where sourced.", ("country_code",), ("currency_code", "timezone", "regulators", "privacy_law", "iso4217"), "Facility confirms country-specific identifiers and reporting unit codes."),
    "facilities": StandardProfile("facilities", "National Facility Registry / Facility Type", "https://medic8.local/fhir/CodeSystem/facility-type", "facility_type_id", "code_system_version", ("facility_type", "facility_type_name", "name"), "https://medic8.local/fhir/ValueSet/facility-types", "Organization / Location", "Facility output must preserve country, tier, ownership, service capability, registry/licence fields, and optional GLN.", ("facility_type_id",), ("country", "facility_level", "ownership", "gln", "registry"), "Facility confirms legal identity, physical address, licence, national facility code, and service list."),
    "roles-permissions": StandardProfile("roles-permissions", "RBAC / Professional Council", "https://medic8.local/fhir/CodeSystem/role", "role_id", "code_system_version", ("role_name", "cadre", "role_family"), "https://medic8.local/fhir/ValueSet/roles", "PractitionerRole", "Role output must preserve professional-council mapping, licence requirement, least-privilege permissions, and facility-scoped assignment.", ("role_id",), ("regulator", "council", "permission", "licence", "cadre"), "Facility supplies named users, licence evidence, employment status, and role assignments."),
    "workflows": StandardProfile("workflows", "Medic8 Workflow Template", "https://medic8.local/fhir/CodeSystem/workflow-template", "workflow_id", "code_system_version", ("workflow_name", "workflow_domain"), "https://medic8.local/fhir/ValueSet/workflows", "PlanDefinition / ActivityDefinition", "Workflow output must reference standards-backed forms, conditions, orders, reports, roles, and KPIs.", ("workflow_id",), ("linked_orders", "required_forms", "linked_reports", "conditions", "loinc", "icd", "atc"), "Facility confirms active workflows, owners, queues, and local SOP variants."),
    "conditions": StandardProfile("conditions", "ICD-10", "http://hl7.org/fhir/sid/icd-10", "icd10_code", "code_system_version", ("condition_name", "icd10_title", "description"), "http://hl7.org/fhir/sid/icd-10", "Condition", "Condition output must carry ICD-10 for reporting and alternate SNOMED CT/ICD-11/HMIS codings where sourced.", ("icd10_code",), ("snomed", "icd11", "hmis", "idsr"), "Medical director confirms active problem-list subset and specialty add-ons."),
    "drugs": StandardProfile("drugs", "WHO ATC/DDD", "http://www.whocc.no/atc", "atc_code", "code_system_version", ("inn", "drug_name", "brand_inn"), "http://www.whocc.no/atc", "Medication / MedicationKnowledge", "Medication output must carry ATC, INN, RxNorm where sourced, formulary flags, storage, restrictions, and local registration status.", ("atc_code", "inn"), ("rxnorm", "eml", "emhslu", "keml", "nda", "ppb", "tmda"), "Pharmacist confirms stocked formulary, suppliers, prices, lots, and licence restrictions."),
    "drug-interactions": StandardProfile("drug-interactions", "DDInter / ATC Pair", "https://ddinter.scbdd.com/", "interaction_id", "code_system_version", ("drug_a", "drug_b", "mechanism"), "https://medic8.local/fhir/ValueSet/drug-interaction-rules", "DetectedIssue / ClinicalUseDefinition", "Interaction output must preserve both coded drugs, severity, mechanism, consequence, monitoring, and override policy.", ("interaction_id",), ("atc", "rxnorm", "severity"), "Clinical safety lead confirms alert display, severity thresholds, and override governance."),
    "paediatric-dosing": StandardProfile("paediatric-dosing", "ATC + UCUM", "http://www.whocc.no/atc", "dosing_id", "code_system_version", ("drug_name", "indication"), "https://medic8.local/fhir/ValueSet/paediatric-dosing-rules", "PlanDefinition / MedicationKnowledge", "Dosing output must preserve ATC, age/weight bands, route, dose unit, frequency, max dose, neonatal flag, and high-risk flags.", ("dosing_id", "atc_code", "dose_per_kg_unit"), ("ucum", "route", "age_band_min_months", "age_band_max_months", "weight_band_min_kg", "weight_band_max_kg"), "Paediatric clinical lead validates local protocol and high-risk neonatal rules."),
    "allergens": StandardProfile("allergens", "SNOMED CT / RxNorm", "http://snomed.info/sct", "allergen_id", "code_system_version", ("allergen_name",), "https://medic8.local/fhir/ValueSet/allergens", "AllergyIntolerance", "Allergy output must support SNOMED CT and RxNorm codings plus severity, manifestations, and cross-reaction evidence.", ("allergen_id",), ("snomed", "rxnorm", "atc"), "Clinical safety lead confirms allergy capture workflow and local labels."),
    "lab-tests": StandardProfile("lab-tests", "LOINC + UCUM", "http://loinc.org", "loinc_code", "code_system_version", ("test_name", "long_common_name", "display_name"), "http://loinc.org", "Observation / DiagnosticReport", "Lab output must carry LOINC code, UCUM unit for numeric values, specimen, method, reference range, critical values, and answer-list binding where applicable.", ("loinc_code",), ("ucum", "snomed", "specimen", "container", "answer_list"), "Lab manager confirms in-house menu, analyser method, reference ranges, prices, and accreditation status."),
    "ucum": StandardProfile("ucum", "UCUM", "http://unitsofmeasure.org", "uom_code", "code_system_version", ("uom_display", "unit_name", "dimension", "category"), "http://unitsofmeasure.org", "Quantity", "Quantity output must use UCUM system URI and canonical unit code; conversions must preserve dimension and exact/approximate flag.", ("uom_code",), ("ucum_canonical_form", "category", "conversion_factor_to_base", "conversion_offset_to_base"), "Facility only confirms display preferences where needed."),
    "imaging": StandardProfile("imaging", "LOINC / RadLex / DICOM", "http://loinc.org", "loinc_code", "code_system_version", ("study_name", "procedure_name", "modality"), "http://loinc.org", "ImagingStudy / DiagnosticReport / ServiceRequest", "Imaging output must carry study/report code, modality, body region, RadLex/DICOM mapping where sourced, and report/document type.", ("loinc_code",), ("radlex", "dicom", "modality", "body_region"), "Radiology lead confirms installed modalities, PACS details, contrast stock, and prices."),
    "procedures": StandardProfile("procedures", "ICHI / ICD-10-PCS / CDT", "https://medic8.local/fhir/CodeSystem/procedure-catalogue", "procedure_name", "code_system_version", ("procedure_name", "service_name"), "https://medic8.local/fhir/ValueSet/procedures", "Procedure / ServiceRequest", "Procedure output must preserve procedure/service name, coding system fields, consent requirement, role, BOM, and billing linkage.", ("procedure_name",), ("ichi", "icd10", "pcs", "cdt", "snomed"), "Medical director and accountant confirm active services, prices, consent, and revenue accounts."),
    "consumables": StandardProfile("consumables", "UNSPSC / GMDN / GS1", "https://medic8.local/fhir/CodeSystem/item-master", "item_id", "code_system_version", ("item_name", "description"), "https://medic8.local/fhir/ValueSet/consumables", "InventoryItem / Device", "Consumable output must preserve item ID, procurement taxonomy, device identifiers where sourced, pack size, storage, expiry/lot requirements, and BOM linkage.", ("item_id",), ("unspsc", "gmdn", "gs1", "gtin"), "Store keeper confirms physical stock, suppliers, unit costs, lots, and expiry dates."),
    "boms": StandardProfile("boms", "Medic8 BOM", "https://medic8.local/fhir/CodeSystem/bom", "bom_code", "code_system_version", ("bom_name", "service_name", "linked_id"), "https://medic8.local/fhir/ValueSet/boms", "ActivityDefinition / SupplyRequest", "BOM output must preserve parent service, child consumable/drug/test codes, quantity, unit, substitution rule, and auto-deduction status.", ("bom_code",), ("loinc", "atc", "item_id", "ucum", "linked_id", "linked_kind"), "Domain owner confirms substitutions, pack quantities, and SOP differences."),
    "vaccines": StandardProfile("vaccines", "ATC J07 / EPI", "http://www.whocc.no/atc", "vaccine_code", "code_system_version", ("vaccine_name", "antigen"), "https://medic8.local/fhir/ValueSet/vaccines", "Immunization / MedicationKnowledge", "Vaccine output must preserve antigen, ATC J07 where sourced, schedule, cold chain, MDVP, AEFI, and country programme flags.", ("vaccine_code", "atc_code"), ("atc", "cvx", "schedule_who", "schedule_uganda", "schedule_kenya", "schedule_tanzania", "temperature_zone"), "EPI focal person confirms stocked antigens, cold-chain locations, and schedule variants."),
    "standard-forms": StandardProfile("standard-forms", "LOINC Document / National Form", "http://loinc.org", "form_code", "code_system_version", ("form_name", "domain"), "https://medic8.local/fhir/ValueSet/standard-forms", "Questionnaire / DocumentReference", "Form output must preserve form code, document type, LOINC document code where sourced, owner, reporting cadence, and required fields.", ("form_code",), ("loinc", "hmis", "dhis2", "idsr"), "Records officer confirms reporting unit IDs and optional/private forms."),
    "reporting-kpis": StandardProfile("reporting-kpis", "WHO/HMIS/DHIS2 Indicator", "https://medic8.local/fhir/CodeSystem/kpi", "indicator_id", "code_system_version", ("indicator_name", "indicator_domain"), "https://medic8.local/fhir/ValueSet/reporting-kpis", "Measure / MeasureReport", "KPI output must preserve numerator, denominator, disaggregation, reporting cadence, source programme, and target system mapping.", ("indicator_id",), ("dhis2", "hmis", "pepfar", "loinc_group"), "M&E lead confirms mandatory reports, donor IDs, thresholds, and reporting calendar."),
    "billing-tariffs": StandardProfile("billing-tariffs", "ISO 4217 / Payer Tariff", "urn:iso:std:iso:4217", "charge_item_id", "code_system_version", ("charge_item_name", "charge_category"), "https://medic8.local/fhir/ValueSet/billing-tariffs", "ChargeItemDefinition / Claim", "Billing output must preserve charge item, currency, price-list source, payer mapping, tax/revenue account, and effective dates.", ("charge_item_id",), ("currency", "sha", "insurance", "tariff"), "Accountant confirms prices, insurer contracts, tax treatment, and revenue accounts."),
    "holiday-calendars": StandardProfile("holiday-calendars", "ISO 3166 / IANA Timezone", "urn:iso:std:iso:3166", "holiday_id", "code_system_version", ("holiday_name_en", "holiday_name_local"), "https://medic8.local/fhir/ValueSet/holiday-calendars", "Schedule", "Calendar output must preserve country, observed date, legal/source citation, lunar/substitute flags, and operational applicability.", ("holiday_id", "country_iso2", "date_observed"), ("timezone", "country_iso2"), "Facility confirms local closures and exceptional working days."),
}


STANDARD_KEYWORDS = (
    "loinc",
    "ucum",
    "snomed",
    "rxnorm",
    "atc",
    "icd",
    "radlex",
    "dicom",
    "cvx",
    "gs1",
    "gmdn",
    "unspsc",
    "dhis2",
    "hmis",
    "iso",
    "currency",
    "timezone",
    "code",
    "version",
)


def value(row: dict[str, str], field: str) -> str:
    if field in row:
        return row[field]
    lower = field.lower()
    for key, item in row.items():
        if key.lower() == lower:
            return item
    return ""


def has_gap(text: str) -> bool:
    low = (text or "").lower()
    return "[gap" in low or "[unverified" in low or "pending verification" in low


def display_value(row: dict[str, str], profile: StandardProfile) -> str:
    for field in profile.display_fields:
        item = value(row, field)
        if item and not has_gap(item):
            return item
    for key, item in row.items():
        if key.startswith("_"):
            continue
        if item and not has_gap(item):
            return item
    return value(row, profile.primary_code_field) or value(row, "_row_key")


def alternate_codings(row: dict[str, str], profile: StandardProfile) -> str:
    payload = {}
    for key, item in row.items():
        if key.startswith("_"):
            continue
        low = key.lower()
        if key == profile.primary_code_field:
            continue
        if any(token in low for token in STANDARD_KEYWORDS):
            payload[key] = item
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def gap_fields(row: dict[str, str]) -> str:
    gaps = []
    for key, item in row.items():
        if key.startswith("_"):
            continue
        if has_gap(item):
            gaps.append(key)
    return "; ".join(gaps)


def conformance_status(row: dict[str, str], profile: StandardProfile) -> str:
    if profile.slug == "ucum" and value(row, "from_uom") and value(row, "to_uom"):
        edge_missing = [field for field in ("from_uom", "to_uom", "factor") if not value(row, field) or has_gap(value(row, field))]
        if edge_missing:
            return "requires curator mapping"
        if gap_fields(row):
            return "standards-shaped with gaps"
        return "global-standard conformant"
    missing_required = [field for field in profile.required_fields if not value(row, field) or has_gap(value(row, field))]
    gaps = gap_fields(row)
    if missing_required:
        return "requires curator mapping"
    if gaps:
        return "standards-shaped with gaps"
    if profile.primary_system_uri.startswith("https://medic8.local"):
        return "internal-standard conformant"
    return "global-standard conformant"


def output_blocker(row: dict[str, str], profile: StandardProfile) -> str:
    status = conformance_status(row, profile)
    if status == "requires curator mapping":
        return "yes"
    if profile.slug in {"lab-tests", "ucum"}:
        if profile.slug == "lab-tests":
            unit_fields = [key for key in row if "unit" in key.lower() or "ucum" in key.lower()]
            if unit_fields and any(has_gap(value(row, key)) for key in unit_fields):
                return "conditional"
        if profile.slug == "ucum" and value(row, "from_uom") and value(row, "to_uom") and not value(row, "factor"):
            return "yes"
    return "no"


def standardized_row(cohort, row: dict[str, str], profile: StandardProfile) -> dict[str, str]:
    primary_code = value(row, profile.primary_code_field) or value(row, "_row_key")
    if profile.slug == "ucum" and not value(row, profile.primary_code_field) and value(row, "from_uom") and value(row, "to_uom"):
        primary_code = f"{value(row, 'from_uom')}->{value(row, 'to_uom')}"
    return {
        "cohort": cohort.slug,
        "row_key": value(row, "_row_key"),
        "display": display_value(row, profile),
        "primary_standard": profile.primary_standard,
        "primary_system_uri": profile.primary_system_uri,
        "primary_code": primary_code,
        "primary_code_field": profile.primary_code_field,
        "standard_version": value(row, profile.version_field),
        "value_set_uri": profile.value_set_uri,
        "fhir_resource": profile.fhir_resource,
        "conformance_status": conformance_status(row, profile),
        "output_blocker": output_blocker(row, profile),
        "alternate_codings_json": alternate_codings(row, profile),
        "gap_fields": gap_fields(row),
        "source_file": value(row, "_source_file"),
        "facility_confirmation_boundary": profile.facility_boundary,
        "output_rule": profile.output_rule,
    }


def write_sheet(workbook, name: str, headers: list[str], rows: list[list[str]]) -> None:
    sheet = workbook.add_worksheet(name[:31])
    header_fmt = workbook.add_format({"bold": True, "bg_color": "#D9EAF7", "border": 1, "text_wrap": True, "valign": "top"})
    cell_fmt = workbook.add_format({"border": 1, "text_wrap": True, "valign": "top"})
    for col, header in enumerate(headers):
        sheet.write(0, col, header, header_fmt)
    for row_idx, items in enumerate(rows, 1):
        for col, item in enumerate(items):
            sheet.write(row_idx, col, item, cell_fmt)
    sheet.freeze_panes(1, 0)
    if rows:
        sheet.autofilter(0, 0, len(rows), len(headers) - 1)
    for col, header in enumerate(headers):
        width = min(max(len(header) + 4, 18), 70)
        if header in {"alternate_codings_json", "output_rule", "facility_confirmation_boundary"}:
            width = 70
        sheet.set_column(col, col, width)


def write_repopulation_note(cohort, rows: list[dict[str, str]], std_rows: list[dict[str, str]], profile: StandardProfile) -> Path:
    counts = Counter(row["conformance_status"] for row in std_rows)
    blockers = Counter(row["output_blocker"] for row in std_rows)
    top_gap_fields = Counter()
    for row in std_rows:
        for field in row["gap_fields"].split("; "):
            if field:
                top_gap_fields[field] += 1
    lines = [
        f"# {cohort.title} - Standards Repopulation",
        "",
        f"**Generated:** {DATE}",
        "",
        "## Standards Profile",
        "",
        f"- Primary standard: {profile.primary_standard}",
        f"- Primary system URI: `{profile.primary_system_uri}`",
        f"- Primary code field: `{profile.primary_code_field}`",
        f"- Value set URI: `{profile.value_set_uri}`",
        f"- FHIR/resource target: `{profile.fhir_resource}`",
        "",
        "## Row Status",
        "",
    ]
    for key, count in counts.most_common():
        lines.append(f"- {key}: {count}")
    lines.extend(["", "## Output Blockers", ""])
    for key, count in blockers.most_common():
        lines.append(f"- {key}: {count}")
    lines.extend(["", "## Highest-Frequency Gap Fields", ""])
    if top_gap_fields:
        for key, count in top_gap_fields.most_common(12):
            lines.append(f"- `{key}`: {count}")
    else:
        lines.append("- None detected in parsed rows.")
    lines.extend([
        "",
        "## Output Rule",
        "",
        profile.output_rule,
        "",
        "## Facility Confirmation Boundary",
        "",
        profile.facility_boundary,
        "",
        "## Rule",
        "",
        "Rows marked `requires curator mapping` must not be promoted to production global settings until the missing standard code or required output field is sourced. Rows marked `standards-shaped with gaps` can be staged but must carry the gap fields forward to the curator worklist.",
    ])
    path = PROJECT / cohort.slug / "analysis" / "standards-repopulation.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def validate_office(path: Path) -> None:
    with zipfile.ZipFile(path) as zf:
        bad = zf.testzip()
    if bad:
        raise RuntimeError(f"Invalid Office file {path}: {bad}")


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    EXPORT.mkdir(parents=True, exist_ok=True)
    all_rows: list[dict[str, str]] = []
    summaries: list[list[str]] = []
    notes: list[Path] = []
    cohort_rows: dict[str, list[dict[str, str]]] = {}

    for cohort in base.COHORTS:
        profile = PROFILES[cohort.slug]
        source_rows = base.load_rows(cohort)
        std_rows = [standardized_row(cohort, row, profile) for row in source_rows]
        all_rows.extend(std_rows)
        cohort_rows[cohort.slug] = std_rows
        counts = Counter(row["conformance_status"] for row in std_rows)
        blockers = Counter(row["output_blocker"] for row in std_rows)
        summaries.append([
            cohort.slug,
            str(len(std_rows)),
            profile.primary_standard,
            profile.primary_system_uri,
            profile.fhir_resource,
            str(counts.get("global-standard conformant", 0) + counts.get("internal-standard conformant", 0)),
            str(counts.get("standards-shaped with gaps", 0)),
            str(counts.get("requires curator mapping", 0)),
            str(blockers.get("yes", 0)),
            str(blockers.get("conditional", 0)),
            profile.facility_boundary,
        ])
        notes.append(write_repopulation_note(cohort, source_rows, std_rows, profile))

    workbook_path = OUTPUT / f"medic8-all-cohorts-standards-repopulated-{VERSION}-{DATE}.xlsx"
    workbook = xlsxwriter.Workbook(str(workbook_path))

    summary_headers = ["cohort", "rows", "primary_standard", "primary_system_uri", "fhir_resource", "conformant", "standards_shaped_with_gaps", "requires_curator_mapping", "hard_output_blockers", "conditional_output_blockers", "facility_boundary"]
    write_sheet(workbook, "Cohort Summary", summary_headers, summaries)

    profile_headers = ["cohort", "primary_standard", "primary_system_uri", "primary_code_field", "value_set_uri", "fhir_resource", "required_fields", "alternate_fields", "output_rule", "facility_boundary"]
    profile_rows = []
    for cohort in base.COHORTS:
        profile = PROFILES[cohort.slug]
        profile_rows.append([
            cohort.slug,
            profile.primary_standard,
            profile.primary_system_uri,
            profile.primary_code_field,
            profile.value_set_uri,
            profile.fhir_resource,
            "; ".join(profile.required_fields),
            "; ".join(profile.alternate_fields),
            profile.output_rule,
            profile.facility_boundary,
        ])
    write_sheet(workbook, "Standards Profiles", profile_headers, profile_rows)

    row_headers = ["cohort", "row_key", "display", "primary_standard", "primary_system_uri", "primary_code", "primary_code_field", "standard_version", "value_set_uri", "fhir_resource", "conformance_status", "output_blocker", "alternate_codings_json", "gap_fields", "source_file", "facility_confirmation_boundary", "output_rule"]
    write_sheet(workbook, "All Standardized Rows", row_headers, [[row[h] for h in row_headers] for row in all_rows])

    worklist = [row for row in all_rows if row["conformance_status"] != "global-standard conformant" and row["conformance_status"] != "internal-standard conformant"]
    worklist_headers = ["cohort", "row_key", "display", "conformance_status", "output_blocker", "primary_standard", "primary_code_field", "primary_code", "gap_fields", "source_file", "facility_confirmation_boundary"]
    write_sheet(workbook, "Curator Worklist", worklist_headers, [[row[h] for h in worklist_headers] for row in worklist])

    for cohort in base.COHORTS:
        rows = cohort_rows[cohort.slug]
        write_sheet(workbook, cohort.slug, row_headers, [[row[h] for h in row_headers] for row in rows])

    workbook.close()
    validate_office(workbook_path)
    shutil.copy2(workbook_path, EXPORT / workbook_path.name)
    validate_office(EXPORT / workbook_path.name)

    manifest = PROJECT / "04-synthesis" / f"standards-repopulation-manifest-{DATE}.md"
    lines = [
        "# Medic8 Standards Repopulation Manifest",
        "",
        f"**Generated:** {DATE}",
        f"**Version:** {VERSION}",
        "",
        "## Output",
        "",
        f"- `{workbook_path.relative_to(PROJECT).as_posix()}`",
        f"- `export/medic8-global-settings/{workbook_path.name}`",
        "",
        "## Scope",
        "",
        "All active cohorts were repopulated into standards-shaped import rows. Source research tables were not overwritten; rows that cannot be safely completed from the evidence corpus are marked for curator mapping instead of being guessed.",
        "",
        "## Cohort Summary",
        "",
        "| cohort | rows | conformant | with gaps | curator mapping | hard blockers |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in summaries:
        lines.append(f"| {row[0]} | {row[1]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} |")
    lines.extend(["", "## Per-Cohort Notes", ""])
    for note in notes:
        lines.append(f"- `{note.relative_to(PROJECT).as_posix()}`")
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("Repopulated all cohorts into standards-shaped rows")
    print(f"Rows: {len(all_rows)}")
    print(f"Workbook: {workbook_path}")
    print(f"Manifest: {manifest}")


if __name__ == "__main__":
    main()
