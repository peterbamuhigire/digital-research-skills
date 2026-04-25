"""Text / money / URL cleaning."""
from __future__ import annotations

import html
import re
import unicodedata
from decimal import Decimal, InvalidOperation
from typing import Optional
from urllib.parse import urldefrag, urljoin, urlparse, urlunparse


_WS = re.compile(r"\s+")


def clean_text(s: str) -> str:
    """NFKC + HTML unescape + whitespace collapse + strip."""
    if not s:
        return ""
    s = unicodedata.normalize("NFKC", s)
    s = html.unescape(s)
    s = _WS.sub(" ", s)
    return s.strip()


_MONEY = re.compile(r"[^\d.,\-]")


def parse_money(s: str, *, default_currency: str = "USD") -> Optional[Decimal]:
    """Extract Decimal from a money-ish string.

    Strips currency symbols, thousands separators (NBSP, comma, space),
    handles minus sign. Does NOT auto-detect currency — caller passes default.
    """
    if not s:
        return None
    cleaned = _MONEY.sub("", s)
    if "," in cleaned and "." in cleaned:
        # Assume US format: 1,234.56 (drop commas)
        cleaned = cleaned.replace(",", "")
    elif "," in cleaned and "." not in cleaned:
        # Could be EU format: 1.234,56 → flip
        # If exactly one comma followed by 2 digits, treat as decimal
        if re.match(r"^-?\d+,\d{1,2}$", cleaned):
            cleaned = cleaned.replace(",", ".")
        else:
            cleaned = cleaned.replace(",", "")
    try:
        return Decimal(cleaned)
    except InvalidOperation:
        return None


def canonicalize_url(url: str, *, base: Optional[str] = None) -> str:
    """Lowercase host, strip fragment, resolve relative against base."""
    if base is not None:
        url = urljoin(base, url)
    url, _ = urldefrag(url)
    p = urlparse(url)
    return urlunparse(p._replace(netloc=p.netloc.lower()))


def parse_int_loose(s: str) -> Optional[int]:
    """Loose int parse: strips commas, NBSPs, surrounding text."""
    if not s:
        return None
    m = re.search(r"-?\d[\d, \s]*", s)
    if m is None:
        return None
    digits = re.sub(r"[^\d-]", "", m.group(0))
    try:
        return int(digits)
    except ValueError:
        return None
