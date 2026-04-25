"""Data cleaning + assessment + analysis utilities.

The bridge between `tools/datasets/` (retrieval) and `tools/academic/` (writing).
Every dataset that enters the engine passes through this layer:

  retrieve  →  profile  →  dq_score  →  clean  →  analyse  →  cite

Public API:
    profile_dataframe          — per-column report (Walker + ydata-style)
    score_data_quality         — four-axis: completeness / usefulness / reliability / relevance
    check_merge                — Walker's anti-join pattern with indicator + crosstab
    detect_outliers            — univariate + multivariate panel
    repair_encoding            — charset-normalizer + ftfy + BOM strip
    tidy_check                 — Wickham violation detector
    advise_imputation          — recommends method based on missingness mechanism
    validate_schema            — Pandera wrapper
"""
from .profiler import profile_dataframe, ProfileReport, ColumnProfile as DataColumnProfile
from .dq_score import score_data_quality, DataQualityScore, AxisScore
from .checkmerge import check_merge, MergeAuditReport
from .outlier_panel import detect_outliers, OutlierReport, OutlierMethod
from .encoding_repair import repair_encoding, RepairReport
from .tidy_check import tidy_check, TidyViolation
from .imputation_advisor import advise_imputation, ImputationAdvice

__all__ = [
    "profile_dataframe", "ProfileReport", "DataColumnProfile",
    "score_data_quality", "DataQualityScore", "AxisScore",
    "check_merge", "MergeAuditReport",
    "detect_outliers", "OutlierReport", "OutlierMethod",
    "repair_encoding", "RepairReport",
    "tidy_check", "TidyViolation",
    "advise_imputation", "ImputationAdvice",
]
