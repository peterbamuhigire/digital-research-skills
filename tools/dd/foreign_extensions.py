"""Company-suffix → jurisdiction dictionary.

Per Hetherington Appendix E: a string like "BugCo Sp. z.o.o." tells you
the entity is a privately-held Polish LLC before any registry lookup.
"""
from __future__ import annotations


FOREIGN_EXTENSIONS: dict[str, list[dict[str, str]]] = {
    "GmbH": [{"country": "DE", "type": "Gesellschaft mit beschränkter Haftung — private LLC"}],
    "AG": [{"country": "DE/CH/AT", "type": "Aktiengesellschaft — public limited company"}],
    "SE": [{"country": "EU", "type": "Societas Europaea — pan-EU public company"}],
    "AB": [{"country": "SE", "type": "Aktiebolag — limited company"}],
    "HB": [{"country": "SE", "type": "Handelsbolag — trading partnership"}],
    "Kb": [{"country": "SE", "type": "Kommanditbolag — limited partnership"}],
    "AS": [{"country": "NO/DK", "type": "Aksjeselskap — limited company"}],
    "ASA": [{"country": "NO", "type": "Allmennaksjeselskap — public limited"}],
    "ANS": [{"country": "NO", "type": "Ansvarlig selskap — partnership"}],
    "DA": [{"country": "NO", "type": "Delt ansvar — divided-liability partnership"}],
    "KS": [{"country": "NO", "type": "Kommandittselskap — limited partnership"}],
    "ApS": [{"country": "DK", "type": "Anpartsselskab — private limited"}],
    "Sp. z.o.o.": [{"country": "PL", "type": "Spółka z ograniczoną odpowiedzialnością — private LLC"}],
    "SA": [{"country": "PL/FR/CH/various", "type": "Société Anonyme — public limited"}],
    "Sp.k.": [{"country": "PL", "type": "Spółka komandytowa — limited partnership"}],
    "Srl": [{"country": "IT/RO", "type": "Società/Societate a responsabilità limitata"}],
    "SCA": [{"country": "IT", "type": "Società in accomandita per azioni"}],
    "SCS": [{"country": "IT", "type": "Società in accomandita semplice"}],
    "SNC": [{"country": "IT/FR", "type": "Società/Société en nom collectif"}],
    "SAS": [{"country": "FR", "type": "Société par actions simplifiée"}],
    "SARL": [{"country": "FR", "type": "Société à responsabilité limitée"}],
    "EURL": [{"country": "FR", "type": "Entreprise unipersonnelle à responsabilité limitée"}],
    "BV": [{"country": "NL", "type": "Besloten Vennootschap — private LLC"}],
    "NV": [{"country": "NL/BE/SR", "type": "Naamloze Vennootschap — public LC"}],
    "VOF": [{"country": "NL", "type": "Vennootschap onder firma"}],
    "BVBA": [{"country": "BE", "type": "Besloten vennootschap met beperkte aansprakelijkheid"}],
    "d.d.": [{"country": "SI/HR", "type": "delniška družba / dioničko društvo — public LC"}],
    "d.o.o.": [{"country": "SI/HR/RS/BA", "type": "družba z omejeno odgovornostjo / društvo s ograničenom odgovornošću — private LLC"}],
    "d.n.o.": [{"country": "SI", "type": "družba z neomejeno odgovornostjo — unlimited"}],
    "k.d.": [{"country": "SI/HR", "type": "komanditna družba / komanditno društvo — limited partnership"}],
    "AVV": [{"country": "AW", "type": "Aruba Vrijgestelde Vennootschap — Aruba exempt company"}],
    "SAFI": [{"country": "UY", "type": "Sociedad Anónima Financiera de Inversión — Uruguay holding"}],
    "AS Ltd": [{"country": "TR", "type": "Anonim Şirketi — joint-stock"}],
    "Lda": [{"country": "PT/BR", "type": "Limitada — limited company"}],
    "SGPS": [{"country": "PT", "type": "Sociedade Gestora de Participações Sociais — holding"}],
    "S.A. de C.V.": [{"country": "MX", "type": "Sociedad Anónima de Capital Variable"}],
    "Pte Ltd": [{"country": "SG", "type": "Private Limited"}],
    "Sdn Bhd": [{"country": "MY", "type": "Sendirian Berhad — private limited"}],
    "Bhd": [{"country": "MY", "type": "Berhad — public limited"}],
    "Pty Ltd": [{"country": "AU/ZA", "type": "Proprietary Limited"}],
    "ULC": [{"country": "CA", "type": "Unlimited Liability Company"}],
    "ZAO": [{"country": "RU", "type": "Закрытое акционерное общество — closed JSC (legacy)"}],
    "OOO": [{"country": "RU", "type": "Общество с ограниченной ответственностью — LLC"}],
    "PJSC": [{"country": "RU/UA", "type": "Public Joint Stock Company"}],
    "Yunhan Gongsi": [{"country": "CN", "type": "有限公司 — limited liability"}],
}


def foreign_extension_for(name: str) -> list[dict[str, str]]:
    """Return matching jurisdiction(s) for a company name's suffix.

    Returns empty list if no recognised suffix found.
    """
    name_clean = name.strip().rstrip(".,;")
    matches: list[dict[str, str]] = []
    for suffix, entries in FOREIGN_EXTENSIONS.items():
        if name_clean.lower().endswith(suffix.lower()):
            matches.extend(entries)
    return matches
