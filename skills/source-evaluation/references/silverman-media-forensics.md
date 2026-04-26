# Media forensics verification

Silverman + Bellingcat: the difference between investigative journalism and rumour amplification is **systematic forensic checks** on every claimed primary source.

## The verification layers

### 1. EXIF metadata
Original files carry rich metadata; social-platform re-uploads strip it. The presence/absence of metadata IS evidence.

```python
from tools.verification import extract_exif, has_been_stripped

data = extract_exif("/path/to/photo.jpg")
print(data.captured_at, data.gps_lat, data.gps_lon, data.camera_model)
print(has_been_stripped("/path/to/photo.jpg"))  # heuristic
```

**Decision rule:** if metadata is stripped, treat as a re-upload, NOT as the original. Hunt the original.

### 2. Reverse image search
Find earlier-known versions of the image — establishes provenance.

| Engine | Strength | URL |
|---|---|---|
| TinEye | Best for crops/edits | https://tineye.com |
| Google Images | Largest index | https://images.google.com |
| Yandex | Best for faces/places | https://yandex.com/images |
| Bing | Best for product images | https://bing.com/images |

Always check **all four** for important images. Different indices have different blind spots.

### 3. Geolocation by landmark
Bellingcat technique:
1. Identify singular landmarks in the image — mosque, dome, sign, shop name, road network
2. Search Google Earth / OpenStreetMap for the same arrangement
3. Cross-reference with EXIF GPS if present (don't trust either alone)

For video: extract frames, run reverse image search per frame, look for landmark matches.

### 4. Shadow-time analysis
Solar position from shadow direction → time-of-day at known location.

- Use **SunCalc** (https://www.suncalc.org) interactively
- Or programmatically with `ephem` / `skyfield`:

```python
import ephem
obs = ephem.Observer()
obs.lat, obs.lon, obs.date = "1.30", "32.58", "2024/06/15 12:30"
sun = ephem.Sun(obs)
azimuth_deg = sun.az * 180 / 3.14159  # match against shadow direction in image
```

### 5. Archive recovery
Dead links are often resurrectable.

```python
from tools.verification import wayback_resurrect, all_snapshots

snap = wayback_resurrect("https://example.com/dead-page", timestamp="20240615")
if snap:
    print(snap.archive_url, snap.captured_at)

for s in all_snapshots(url):
    print(s.archive_name, s.archive_url, s.captured_at)
```

### 6. Provenance tracing
The Ottawa Shooting anti-pattern: chronological provenance comes from the **earliest known** timestamp, not the loudest re-poster.

```python
from tools.verification import trace_earliest_known, ProvenanceCandidate
from datetime import datetime

candidates = [
    ProvenanceCandidate(url="https://twitter.com/police/...", platform="twitter",
                        timestamp=datetime(2024, 6, 15, 14, 30), author="@OttawaPolice"),
    ProvenanceCandidate(url="https://twitter.com/random/...", platform="twitter",
                        timestamp=datetime(2024, 6, 15, 14, 50), author="@random"),
]
trace = trace_earliest_known("photo-X", candidates)
print(trace.earliest())  # earliest-known origin
```

Use this BEFORE attributing.

## Standard verification workflow

For any claimed primary-source image / video:

1. **EXIF check** — present? GPS? Capture date?
2. **Reverse image** — TinEye + Google + Yandex + Bing
3. **Earliest snapshot** — Wayback + archive.today
4. **Landmark geolocation** — match against Google Earth / OSM
5. **Shadow-time** — if exterior shot with shadows
6. **Cross-platform footprint** — same image on FB / IG / TikTok with different metadata?
7. **Provenance trace** — earliest known timestamp wins
8. **Document the verification packet** — every step, every link, every screenshot

## Worked example — verification packet structure

```markdown
# Verification: claimed-source-image-X

## 1. EXIF
- Camera: Canon EOS R5
- Captured: 2024-06-15T14:30:00+03
- GPS: 1.300, 32.580 (Kampala)
- Software: <none — likely original>
- VERDICT: original; metadata intact

## 2. Reverse image
- TinEye: 0 matches (likely first publication)
- Google Images: 1 match (this article only)
- Yandex: 0 matches
- VERDICT: not previously published online

## 3. Landmark geolocation
- Visible: Old Kampala mosque (white dome, twin minarets)
- OSM match: 0.3133, 32.5808 — within 50m of EXIF GPS
- VERDICT: location confirmed

## 4. Shadow-time
- Shadow direction: ~50° from north
- Predicted azimuth at 14:30 EAT: 47°
- VERDICT: time-of-day consistent with claim
```

## Anti-patterns (Silverman)

- Treating embedding as permission (legally distinct; ethically not)
- "Cannot be independently verified" disclaimer abuse — state which of {source, date, location} you DID confirm
- Naming witnesses in active situations
- Origin = loudest re-poster (Ottawa Shooting cascade)
- Confirmation bias — fitting evidence to a preferred narrative
- Trusting EXIF GPS without landmark confirmation (EXIF can be edited)
- Trusting landmark match without checking shadow / time consistency

## See also

- `tools/verification/exif.py`, `archive.py`, `provenance.py` — implementation
- `evidence-discipline` — verification feeds discipline
- `osint-methodology` — adjacent skill for entity profiling
- `provenance-chain` (roadmap) — formalised earliest-known-timestamp protocol
