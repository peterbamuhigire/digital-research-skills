"""Per-country regulator / registry / sanctions-issuer atlas.

Hetherington Appendix E in machine-readable form. Tells the engine, for any
country, where to look for: corporate registry, securities regulator, AML/FIU,
court records, sanctions lists.

Coverage is a starting set — extend per project.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class RegistryEntry:
    name: str
    url: str
    type: str   # "corporate_registry" | "securities" | "aml_fiu" | "court" | "sanctions" | "professional"
    free: bool = True
    notes: str = ""


REGISTRY_ATLAS: dict[str, list[RegistryEntry]] = {
    "UK": [
        RegistryEntry("Companies House", "https://find-and-update.company-information.service.gov.uk/", "corporate_registry"),
        RegistryEntry("FCA Register", "https://register.fca.org.uk/", "professional"),
        RegistryEntry("HM Treasury Sanctions", "https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets", "sanctions"),
        RegistryEntry("Insolvency Service", "https://www.gov.uk/government/organisations/insolvency-service", "court"),
        RegistryEntry("Disqualified Directors", "https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/", "professional"),
    ],
    "US": [
        RegistryEntry("SEC EDGAR", "https://www.sec.gov/edgar.shtml", "securities"),
        RegistryEntry("FINRA BrokerCheck", "https://brokercheck.finra.org/", "professional"),
        RegistryEntry("OFAC SDN", "https://sanctionssearch.ofac.treas.gov/", "sanctions"),
        RegistryEntry("PACER (federal courts)", "https://pacer.uscourts.gov/", "court", free=False),
        RegistryEntry("CourtListener", "https://www.courtlistener.com/", "court"),
        RegistryEntry("SAM.gov", "https://sam.gov/", "professional"),
        RegistryEntry("BRBPublications state index", "https://www.brbpublications.com/", "corporate_registry"),
    ],
    "KE": [
        RegistryEntry("BRS Kenya (companies)", "https://brs.go.ke/", "corporate_registry"),
        RegistryEntry("CMA Kenya", "https://www.cma.or.ke/", "securities"),
        RegistryEntry("Kenya Law", "https://kenyalaw.org/", "court"),
        RegistryEntry("EACC (anti-corruption)", "https://www.eacc.go.ke/", "aml_fiu"),
    ],
    "UG": [
        RegistryEntry("URSB (companies)", "https://ursb.go.ug/", "corporate_registry"),
        RegistryEntry("CMA Uganda", "https://www.cmauganda.co.ug/", "securities"),
        RegistryEntry("ULII (court records)", "https://ulii.org/", "court"),
        RegistryEntry("FIA Uganda", "https://www.fia.go.ug/", "aml_fiu"),
    ],
    "TZ": [
        RegistryEntry("BRELA Tanzania", "https://onlineservices.brela.go.tz/", "corporate_registry"),
        RegistryEntry("CMSA Tanzania", "https://www.cmsa.go.tz/", "securities"),
        RegistryEntry("TanzLII", "https://tanzlii.org/", "court"),
        RegistryEntry("FIU Tanzania", "https://www.fiu.go.tz/", "aml_fiu"),
    ],
    "RW": [
        RegistryEntry("RDB Rwanda", "https://www.rdb.rw/", "corporate_registry"),
        RegistryEntry("CMA Rwanda", "https://www.cma.rw/", "securities"),
        RegistryEntry("RwandaLII", "https://rwandalii.org/", "court"),
        RegistryEntry("FIC Rwanda", "https://www.fic.gov.rw/", "aml_fiu"),
    ],
    "ZA": [
        RegistryEntry("CIPC South Africa", "https://www.cipc.co.za/", "corporate_registry"),
        RegistryEntry("FSCA", "https://www.fsca.co.za/", "securities"),
        RegistryEntry("SAFLII", "https://www.saflii.org/", "court"),
        RegistryEntry("FIC South Africa", "https://www.fic.gov.za/", "aml_fiu"),
    ],
    "NG": [
        RegistryEntry("CAC Nigeria", "https://www.cac.gov.ng/", "corporate_registry"),
        RegistryEntry("SEC Nigeria", "https://sec.gov.ng/", "securities"),
        RegistryEntry("EFCC Nigeria", "https://www.efcc.gov.ng/", "aml_fiu"),
    ],
    "FR": [
        RegistryEntry("Infogreffe", "https://www.infogreffe.fr/", "corporate_registry"),
        RegistryEntry("AMF", "https://www.amf-france.org/", "securities"),
        RegistryEntry("Tracfin", "https://www.economie.gouv.fr/tracfin", "aml_fiu"),
    ],
    "DE": [
        RegistryEntry("Handelsregister", "https://www.handelsregister.de/", "corporate_registry"),
        RegistryEntry("BaFin", "https://www.bafin.de/", "securities"),
    ],
    "SG": [
        RegistryEntry("ACRA Singapore", "https://www.acra.gov.sg/", "corporate_registry"),
        RegistryEntry("MAS Singapore", "https://www.mas.gov.sg/", "securities"),
    ],
    "HK": [
        RegistryEntry("HK Companies Registry", "https://www.cr.gov.hk/", "corporate_registry"),
        RegistryEntry("HK Monetary Authority", "https://www.hkma.gov.hk/", "securities"),
    ],
    "VG": [
        RegistryEntry("BVI Financial Services Commission", "https://www.bvifsc.vg/", "corporate_registry",
                      notes="High shell-company concentration; verify substance"),
    ],
    "KY": [
        RegistryEntry("Cayman CIMA", "https://www.cima.ky/", "securities",
                      notes="High shell-company concentration; verify substance"),
    ],
}


def registry_for_country(iso2: str, *, type_: str | None = None) -> list[RegistryEntry]:
    """Return registries for an ISO-2 country code, optionally filtered by type."""
    entries = REGISTRY_ATLAS.get(iso2.upper(), [])
    if type_:
        return [e for e in entries if e.type == type_]
    return entries
