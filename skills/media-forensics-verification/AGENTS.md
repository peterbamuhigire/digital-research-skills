# Codex / generic-agent — media-forensics-verification

```yaml
artefact_id: <id>
exif:
  has_metadata: bool
  gps: {lat, lon} | null
  captured_at: <iso8601> | null
  software: "..." | null
reverse_image:
  tineye_matches: <int>
  google_matches: <int>
  yandex_matches: <int>
  bing_matches: <int>
  earliest_match_url: "..." | null
  earliest_match_date: <date> | null
geolocation:
  landmark_match: bool
  coordinates: {lat, lon} | null
  source: "google_earth" | "osm" | null
shadow_time:
  shadow_azimuth_deg: <float>
  predicted_azimuth: <float>
  consistent: bool
archive:
  wayback_snapshots: [...]
  archive_today: "..." | null
provenance:
  earliest_known_url: "..." | null
  earliest_known_at: <iso8601> | null
verification_status: confirmed | partial | failed
```

See `SKILL.md`.
