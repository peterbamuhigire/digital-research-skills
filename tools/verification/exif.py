"""EXIF metadata extraction + metadata-stripped detection.

Per Silverman: social platforms strip metadata on upload, so original files
obtained via in-person/encrypted channels are evidentially superior to
re-uploaded versions. This tool tells you which.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class ExifData:
    has_metadata: bool
    camera_make: Optional[str] = None
    camera_model: Optional[str] = None
    captured_at: Optional[str] = None  # ISO8601 string
    gps_lat: Optional[float] = None
    gps_lon: Optional[float] = None
    gps_alt: Optional[float] = None
    software: Optional[str] = None
    raw: dict[str, str] | None = None


def extract_exif(image_path_or_bytes: str | bytes) -> ExifData:
    """Extract EXIF from a file path or bytes.

    Lazy-imports `exifread` and `piexif`.
    """
    import exifread  # type: ignore

    if isinstance(image_path_or_bytes, str):
        with open(image_path_or_bytes, "rb") as f:
            tags = exifread.process_file(f, details=False)
    else:
        import io
        tags = exifread.process_file(io.BytesIO(image_path_or_bytes), details=False)

    if not tags:
        return ExifData(has_metadata=False)

    raw = {k: str(v) for k, v in tags.items()}
    return ExifData(
        has_metadata=True,
        camera_make=raw.get("Image Make"),
        camera_model=raw.get("Image Model"),
        captured_at=raw.get("EXIF DateTimeOriginal") or raw.get("Image DateTime"),
        gps_lat=_dms_to_decimal(raw.get("GPS GPSLatitude"), raw.get("GPS GPSLatitudeRef")),
        gps_lon=_dms_to_decimal(raw.get("GPS GPSLongitude"), raw.get("GPS GPSLongitudeRef")),
        gps_alt=_to_float(raw.get("GPS GPSAltitude")),
        software=raw.get("Image Software"),
        raw=raw,
    )


def has_been_stripped(image_path_or_bytes: str | bytes) -> bool:
    """Heuristic: image was uploaded via a metadata-stripping platform.

    Strong signal: zero EXIF tags AND software field absent.
    Weaker signal: software field includes 'Facebook', 'Twitter', etc.
    """
    data = extract_exif(image_path_or_bytes)
    if not data.has_metadata:
        return True
    sw = (data.software or "").lower()
    return any(x in sw for x in ("facebook", "twitter", "instagram", "whatsapp"))


def _dms_to_decimal(dms_str: Optional[str], ref: Optional[str]) -> Optional[float]:
    if not dms_str or not ref:
        return None
    try:
        # "[12, 34, 56/100]" — exifread's printable form
        cleaned = dms_str.strip("[]").replace(" ", "")
        parts = cleaned.split(",")
        deg = float(parts[0])
        minutes = float(parts[1])
        sec = _parse_rational(parts[2])
        decimal = deg + minutes / 60 + sec / 3600
        if ref in ("S", "W"):
            decimal = -decimal
        return decimal
    except (ValueError, IndexError):
        return None


def _parse_rational(s: str) -> float:
    if "/" in s:
        n, d = s.split("/")
        return float(n) / float(d)
    return float(s)


def _to_float(s: Optional[str]) -> Optional[float]:
    if not s:
        return None
    try:
        return _parse_rational(s)
    except (ValueError, IndexError):
        return None
