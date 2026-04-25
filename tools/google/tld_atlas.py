"""TLD / state-domain / IGO-domain matrix.

Brown's Table 4.4 (every US state has BOTH a `state.XX.us` legacy domain
AND a modern `.gov` domain — search both for completeness) plus the
foreign-government and IGO atlas.

This is a maintained reference dataset, not just text.
"""
from __future__ import annotations


# Brown's worked example: Colorado has 4,080 results on state.co.us alone but
# 7,110 across BOTH state.co.us + colorado.gov for the same query. Always search both.
US_STATE_DOMAINS: dict[str, list[str]] = {
    "AL": ["alabama.gov", "state.al.us"],
    "AK": ["alaska.gov", "state.ak.us"],
    "AZ": ["az.gov", "state.az.us"],
    "AR": ["arkansas.gov", "state.ar.us"],
    "CA": ["ca.gov", "state.ca.us"],
    "CO": ["colorado.gov", "state.co.us"],
    "CT": ["ct.gov", "state.ct.us"],
    "DE": ["delaware.gov", "state.de.us"],
    "FL": ["myflorida.com", "state.fl.us"],
    "GA": ["georgia.gov", "state.ga.us"],
    "HI": ["hawaii.gov", "state.hi.us"],
    "ID": ["idaho.gov", "state.id.us"],
    "IL": ["illinois.gov", "state.il.us"],
    "IN": ["in.gov", "state.in.us"],
    "IA": ["iowa.gov", "state.ia.us"],
    "KS": ["kansas.gov", "state.ks.us"],
    "KY": ["kentucky.gov", "state.ky.us"],
    "LA": ["louisiana.gov", "state.la.us"],
    "ME": ["maine.gov", "state.me.us"],
    "MD": ["maryland.gov", "state.md.us"],
    "MA": ["mass.gov", "state.ma.us"],
    "MI": ["michigan.gov", "state.mi.us"],
    "MN": ["mn.gov", "state.mn.us"],
    "MS": ["ms.gov", "state.ms.us"],
    "MO": ["mo.gov", "state.mo.us"],
    "MT": ["mt.gov", "state.mt.us"],
    "NE": ["nebraska.gov", "state.ne.us"],
    "NV": ["nv.gov", "state.nv.us"],
    "NH": ["nh.gov", "state.nh.us"],
    "NJ": ["nj.gov", "state.nj.us"],
    "NM": ["newmexico.gov", "state.nm.us"],
    "NY": ["ny.gov", "state.ny.us"],
    "NC": ["nc.gov", "state.nc.us"],
    "ND": ["nd.gov", "state.nd.us"],
    "OH": ["ohio.gov", "state.oh.us"],
    "OK": ["ok.gov", "state.ok.us"],
    "OR": ["oregon.gov", "state.or.us"],
    "PA": ["pa.gov", "state.pa.us"],
    "RI": ["ri.gov", "state.ri.us"],
    "SC": ["sc.gov", "state.sc.us"],
    "SD": ["sd.gov", "state.sd.us"],
    "TN": ["tn.gov", "state.tn.us"],
    "TX": ["texas.gov", "state.tx.us"],
    "UT": ["utah.gov", "state.ut.us"],
    "VT": ["vermont.gov", "state.vt.us"],
    "VA": ["virginia.gov", "state.va.us"],
    "WA": ["wa.gov", "state.wa.us"],
    "WV": ["wv.gov", "state.wv.us"],
    "WI": ["wisconsin.gov", "state.wi.us"],
    "WY": ["wyo.gov", "state.wy.us"],
}


# Foreign-government domain patterns (incomplete; expand as needed).
FOREIGN_GOV_DOMAINS: dict[str, str] = {
    "UK": "gov.uk",
    "AU": "gov.au",
    "JP": "go.jp",
    "FR": "gouv.fr",
    "DE": "bund.de",
    "IT": "gov.it",
    "ES": "gob.es",
    "MX": "gob.mx",
    "BR": "gov.br",
    "AR": "gob.ar",
    "EC": "gob.ec",
    "CL": "gob.cl",
    "CO": "gov.co",
    "ZA": "gov.za",
    "KE": "go.ke",
    "UG": "go.ug",
    "TZ": "go.tz",
    "RW": "gov.rw",
    "EG": "gov.eg",
    "NG": "gov.ng",
    "GH": "gov.gh",
    "IN": "gov.in",
    "CN": "gov.cn",
    "KR": "go.kr",
    "TH": "go.th",
    "ID": "go.id",
    "MY": "gov.my",
    "PH": "gov.ph",
    "VN": "gov.vn",
    "RU": "gov.ru",
    "PL": "gov.pl",
    "CA": "gc.ca",
    "NZ": "govt.nz",
    "IE": "gov.ie",
    "NL": "overheid.nl",
    "BE": "fed.be",
    "SE": "regeringen.se",
    "NO": "regjeringen.no",
    "DK": "dk",
    "FI": "fi",
}


# Inter-governmental organisations + multilateral bodies.
IGO_DOMAINS: list[str] = [
    "un.org", "ohchr.org", "unhcr.org", "unicef.org", "unhabitat.org", "unocha.org",
    "undp.org", "unesco.org", "wfp.org", "ilo.org", "fao.org", "wto.org", "wipo.int",
    "who.int", "imf.org", "worldbank.org", "afdb.org", "iadb.org", "adb.org",
    "oecd.org", "eu.int", "europa.eu", "coe.int", "icc-cpi.int", "icj-cij.org",
    "africa-union.org", "asean.org", "eac.int", "eccas.int", "ecowas.int",
]


def all_domains_for_state(state: str) -> list[str]:
    """Get both legacy + modern state.gov domains. Brown's "search BOTH" rule."""
    return US_STATE_DOMAINS.get(state.upper(), [])


def all_us_state_domains() -> list[str]:
    """Flat list of every US state legacy + modern domain."""
    out: list[str] = []
    for v in US_STATE_DOMAINS.values():
        out.extend(v)
    return out


def domain_for_country(iso2: str) -> str | None:
    return FOREIGN_GOV_DOMAINS.get(iso2.upper())
