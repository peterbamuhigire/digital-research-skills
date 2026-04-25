"""Registry of known public-dataset hosts.

Categories:
- Government open-data portals (CKAN-based, Socrata-based, custom)
- IGO / multilateral statistical bodies
- Academic / research repositories (Zenodo, ICPSR, Figshare, Dataverse)
- ML dataset hubs (Kaggle, HuggingFace Datasets)
- East African specific (KNBS, UBOS, NBS, NISR)
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DatasetHost:
    name: str
    base_url: str
    type: str  # "ckan" | "socrata" | "custom" | "kaggle" | "huggingface" | "zenodo" | "dataverse"
    coverage: str  # geographic / topical scope
    api_docs: str | None = None
    requires_key: bool = False


DATASET_REGISTRY: list[DatasetHost] = [
    # United States federal & state
    DatasetHost("data.gov", "https://catalog.data.gov", "ckan", "US federal", "https://catalog.data.gov/api/3/"),
    DatasetHost("BLS", "https://www.bls.gov/data/", "custom", "US labor statistics"),
    DatasetHost("Census Bureau", "https://api.census.gov/data", "custom", "US population/economic"),
    DatasetHost("FRED", "https://api.stlouisfed.org/fred/", "custom", "US macroeconomic", "https://fred.stlouisfed.org/docs/api/", True),

    # International / multilateral
    DatasetHost("World Bank Open Data", "https://api.worldbank.org/v2/", "custom", "Global development", "https://datahelpdesk.worldbank.org/"),
    DatasetHost("IMF DataMapper", "https://www.imf.org/external/datamapper/api/v1/", "custom", "Global macroeconomic"),
    DatasetHost("OECD", "https://data.oecd.org/api/", "custom", "OECD countries"),
    DatasetHost("UN Data", "https://data.un.org/", "custom", "Global UN system"),
    DatasetHost("WHO GHO", "https://ghoapi.azureedge.net/api/", "custom", "Global health"),
    DatasetHost("UNICEF", "https://data.unicef.org/", "custom", "Children/health/education"),
    DatasetHost("FAOSTAT", "https://www.fao.org/faostat/en/#data", "custom", "Food and agriculture"),
    DatasetHost("ILO", "https://ilostat.ilo.org/data/", "custom", "Labor"),

    # European
    DatasetHost("Eurostat", "https://ec.europa.eu/eurostat/api/dissemination/", "custom", "EU statistics"),
    DatasetHost("data.europa.eu", "https://data.europa.eu/api/hub/search/", "custom", "EU + member states"),
    DatasetHost("UK data.gov.uk", "https://data.gov.uk/api/3/", "ckan", "UK government"),

    # East Africa specific
    DatasetHost("KNBS", "https://www.knbs.or.ke/", "custom", "Kenya official statistics"),
    DatasetHost("UBOS", "https://www.ubos.org/", "custom", "Uganda official statistics"),
    DatasetHost("NBS Tanzania", "https://www.nbs.go.tz/", "custom", "Tanzania official statistics"),
    DatasetHost("NISR Rwanda", "https://www.statistics.gov.rw/", "custom", "Rwanda official statistics"),
    DatasetHost("Africa Open Data", "https://africaopendata.org/", "ckan", "Pan-African"),

    # Academic / research
    DatasetHost("Zenodo", "https://zenodo.org/api/", "zenodo", "Open research data"),
    DatasetHost("Dataverse", "https://dataverse.harvard.edu/api/", "dataverse", "Academic"),
    DatasetHost("ICPSR", "https://www.icpsr.umich.edu/", "custom", "Social science"),
    DatasetHost("Figshare", "https://api.figshare.com/v2/", "custom", "Open research"),
    DatasetHost("OpenAIRE", "https://api.openaire.eu/", "custom", "EU research outputs"),

    # ML / data-science hubs
    DatasetHost("Kaggle", "https://www.kaggle.com/api/v1/", "kaggle", "ML datasets", requires_key=True),
    DatasetHost("HuggingFace Datasets", "https://huggingface.co/api/datasets", "huggingface", "ML datasets"),

    # Geospatial
    DatasetHost("OpenStreetMap Overpass", "https://overpass-api.de/api/interpreter", "custom", "Geospatial"),
    DatasetHost("Humanitarian Data Exchange", "https://data.humdata.org/api/3/", "ckan", "Humanitarian/crisis"),
    DatasetHost("NASA EOSDIS", "https://earthdata.nasa.gov/", "custom", "Earth observation"),
]


def hosts_by_type(type_: str) -> list[DatasetHost]:
    return [h for h in DATASET_REGISTRY if h.type == type_]


def hosts_by_coverage(keyword: str) -> list[DatasetHost]:
    k = keyword.lower()
    return [h for h in DATASET_REGISTRY if k in h.coverage.lower()]
