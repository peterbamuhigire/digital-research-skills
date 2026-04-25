"""Due diligence utilities — Hetherington's *Authoritative Guide* in code.

Public API:
    triangulate_identity     — anti-defamation guard: ≥3 sources must agree
    trace_ubo                — beneficial-ownership walker
    search_adverse_media     — multi-source negative-news with disambiguation
    build_dd_report          — Hetherington-style DOCX/PDF report
    foreign_extension_for    — classify jurisdiction from company-name suffix
    registry_for_country     — per-country regulator/registry atlas
"""
from .identity_triangulator import triangulate_identity, IdentityCandidate, IdentityVerdict
from .ubo import trace_ubo, OwnershipNode, OwnershipGraph
from .adverse_media import search_adverse_media, AdverseMediaHit
from .report_builder import build_dd_report, DDReport
from .foreign_extensions import foreign_extension_for, FOREIGN_EXTENSIONS
from .registry_atlas import registry_for_country, REGISTRY_ATLAS

__all__ = [
    "triangulate_identity", "IdentityCandidate", "IdentityVerdict",
    "trace_ubo", "OwnershipNode", "OwnershipGraph",
    "search_adverse_media", "AdverseMediaHit",
    "build_dd_report", "DDReport",
    "foreign_extension_for", "FOREIGN_EXTENSIONS",
    "registry_for_country", "REGISTRY_ATLAS",
]
