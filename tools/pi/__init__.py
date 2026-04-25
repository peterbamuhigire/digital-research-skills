"""Private-investigator utilities — McMahon's *Practical Handbook for Private
Investigators* in code.

Public API:
    ChainOfCustody         — append-only evidence ledger with court-ready export
    WitnessStatement       — guided statement workflow with mandatory closers
    PhotoLog               — photo / video log generator (Figures 13.1-13.3)
    SurveillanceLog        — shift-log generator with state-aware audio rules
"""
from .chain_of_custody import ChainOfCustody, CustodyTransfer
from .witness_statement import WitnessStatement, build_statement
from .photo_log import PhotoLog, PhotoEntry
from .surveillance_log import SurveillanceLog, ShiftEntry

__all__ = [
    "ChainOfCustody", "CustodyTransfer",
    "WitnessStatement", "build_statement",
    "PhotoLog", "PhotoEntry",
    "SurveillanceLog", "ShiftEntry",
]
