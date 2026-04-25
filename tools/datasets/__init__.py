"""Public dataset discovery, retrieval, and analysis.

Public API:
    DATASET_REGISTRY     — known dataset hosts + metadata
    search_datasets      — federated search across portals
    retrieve_dataset     — download with caching + format detection
    profile_dataset      — automatic schema + stats + missingness profile
"""
from .registry import DATASET_REGISTRY, DatasetHost
from .search import search_datasets, DatasetSearchResult
from .retrieve import retrieve_dataset, RetrievalResult
from .analyse import profile_dataset, DatasetProfile

__all__ = [
    "DATASET_REGISTRY", "DatasetHost",
    "search_datasets", "DatasetSearchResult",
    "retrieve_dataset", "RetrievalResult",
    "profile_dataset", "DatasetProfile",
]
