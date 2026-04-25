"""Dataset download with caching + format detection.

Goes through the engine's own scraping http_client for retries + ethics.
Detects common formats by extension and content-type:
  CSV / TSV / JSON / NDJSON / Parquet / Excel / SQLite / NetCDF / Shapefile / GeoJSON / Stata / SPSS
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


_FORMAT_BY_EXT = {
    "csv": "csv", "tsv": "tsv", "json": "json", "jsonl": "ndjson", "ndjson": "ndjson",
    "parquet": "parquet", "pq": "parquet",
    "xlsx": "excel", "xls": "excel",
    "sqlite": "sqlite", "db": "sqlite",
    "nc": "netcdf",
    "shp": "shapefile", "geojson": "geojson", "kml": "kml", "kmz": "kmz",
    "dta": "stata", "sav": "spss",
    "zip": "zip", "tar": "tar", "gz": "gz",
}


@dataclass(slots=True)
class RetrievalResult:
    url: str
    local_path: Path
    sha256: str
    bytes_downloaded: int
    detected_format: str
    content_type: Optional[str] = None


def retrieve_dataset(
    url: str, *, dest_dir: str | Path = "./data",
    sha256_expected: Optional[str] = None,
    overwrite: bool = False,
) -> RetrievalResult:
    """Download a dataset with caching + integrity verification.

    If `sha256_expected` is provided and a local copy matches, skip download.
    """
    from ..scraping.http_client import fetch

    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    filename = url.rsplit("/", 1)[-1].split("?")[0] or "download.bin"
    local = dest_dir / filename

    if local.exists() and not overwrite:
        h = _sha256_file(local)
        if sha256_expected is None or h == sha256_expected:
            return RetrievalResult(
                url=url, local_path=local, sha256=h,
                bytes_downloaded=local.stat().st_size,
                detected_format=_detect_format(local, None),
            )

    result = fetch(url, respect_robots=False)
    local.write_bytes(result.content)
    h = _sha256_file(local)
    if sha256_expected is not None and h != sha256_expected:
        raise ValueError(
            f"sha256 mismatch for {url}: expected {sha256_expected}, got {h}"
        )

    return RetrievalResult(
        url=url, local_path=local, sha256=h,
        bytes_downloaded=len(result.content),
        detected_format=_detect_format(local, result.headers.get("content-type")),
        content_type=result.headers.get("content-type"),
    )


def _detect_format(path: Path, content_type: Optional[str]) -> str:
    ext = path.suffix.lstrip(".").lower()
    if ext in _FORMAT_BY_EXT:
        return _FORMAT_BY_EXT[ext]
    if content_type:
        ct = content_type.lower()
        if "csv" in ct: return "csv"
        if "json" in ct: return "json"
        if "parquet" in ct: return "parquet"
        if "excel" in ct or "spreadsheet" in ct: return "excel"
        if "zip" in ct: return "zip"
    return "unknown"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65_536), b""):
            h.update(chunk)
    return h.hexdigest()
