# Scraper Troubleshooting and Etiquette

Use this guide to make a scraper reliable, polite and debuggable, and to diagnose one that has
broken. It applies the engine's identification and rate policy in
`politeness-and-ratelimiting.md`; where anything here seems to conflict, that policy wins.

## Inputs

- Target site, its terms of use and `robots.txt`.
- Authorisation basis for the collection (public data, licence, client permission) and any
  personal data involved (route to `../../pi-investigation/references/legal-and-ethical-bounds.md`).
- Volume, frequency and deadline.
- The failing output, if troubleshooting: status code, headers, first bytes of body.

## 1. Eight operational concerns

Every non-trivial scraper addresses all eight before it ships:

1. Honest identification and correct request headers.
2. Logins and session cookies, only where authorised.
3. Hidden form fields such as CSRF tokens.
4. `robots.txt` compliance.
5. Request pacing so the server is never strained.
6. Scale limits, including whether distributing load is justified at all.
7. Network-error handling.
8. Graceful handling of missing HTML elements.

## 2. Headers: identify honestly, send what a client normally sends

Default library headers can trigger error pages or stripped-down content. The fix is to send a
complete, well-formed set of headers (`Accept`, `Accept-Language`, `Accept-Encoding`) and the
engine's identifying User-Agent from `politeness-and-ratelimiting.md`, not to impersonate a
browser. If a site serves different content to an honestly identified client, treat that as the
site's access decision: look for an official API or data export, ask the owner, or record the
source as not collectable. Do not combine user-agent impersonation, IP rotation and CAPTCHA
solving to defeat access controls.

```python
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en;q=0.8",
    "User-Agent": "digital-research-engine/0.1 (+https://github.com/peterbamuhigire/digital-research-skills)",
}
r = requests.get(url, headers=headers, timeout=30)
```

If content still differs from what a browser shows, the data is probably loaded by JavaScript
(section 8).

## 3. Sessions and login cookies

Sites that require login bind the data to a session cookie. A fresh request without that cookie returns the login page or an error.

**Use a `requests.Session`** (or equivalent in your HTTP library):

```python
s = requests.Session()
s.headers.update(headers)
s.post("https://example.com/login", data={"email": "...", "password": "..."})
# subsequent calls inherit cookies set by the server
r = s.get("https://example.com/protected_page")
```

**Default rule:** do *not* send cookies to sites you scrape unless you must. Cookies tie all your traffic to one identity — easier to throttle, ban, or fingerprint.

## 4. CSRF tokens and hidden form fields

Many POST forms include hidden fields with random per-request tokens (CSRF protection). Posting directly to the form's submit URL without the token returns an error.

**Procedure (the "load-then-submit" pattern):**

1. GET the page that contains the form.
2. Parse the HTML and extract every hidden field's name + value.
3. POST to the form's action URL with all extracted hidden fields plus your own form values, in the same `Session`.

```python
from bs4 import BeautifulSoup

s = requests.Session()
page = s.get("https://example.com/form_page", headers=headers).text
soup = BeautifulSoup(page, "html.parser")
hidden = {i["name"]: i.get("value", "") for i in soup.select('input[type="hidden"]')}
payload = {**hidden, "your_field": "your_value"}
r = s.post("https://example.com/submit", data=payload, headers=headers)
```

Token expiry is real — fetch the form fresh just before submitting.

## 5. robots.txt — the de-facto contract

The Robots Exclusion Protocol (standardised as RFC 9309 in 2022) at `/robots.txt` lets a site signal which paths are off-limits to automated clients. It is not an access-control mechanism or legal advice, but the engine **treats it as binding** — both for ethics and to reduce the chance of being blocked.

```python
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("https://example.com/robots.txt")
rp.read()
if rp.can_fetch("YourScraperUA/1.0", url):
    fetch(url)
```

Cache the parsed robots.txt for the run; re-fetch on long-running jobs (RFC 9309 advises against using a cached copy for more than 24 hours). Honour `Crawl-delay:` if present.

## 6. Slowing down — be the polite user

A real person does not fire 50 requests per second. Working defaults:

- **Default delay** between requests: 1–3 seconds, jittered.
- **Concurrency** to a single host: ≤2 in-flight by default.
- **Off-peak preference**: schedule large jobs for the site's off-hours.
- **Back off on errors** — exponential backoff on 429 / 5xx; respect `Retry-After`.
- **One ID per host** — do not rotate session cookies on the same IP to multiply identity; it gets noticed.

```python
import time, random

def polite_get(session, url):
    time.sleep(random.uniform(1.0, 3.0))
    return session.get(url, headers=headers, timeout=30)
```

## 7. Distributing across IPs (only when scale demands)

When a single IP cannot finish the job inside the polite envelope, consider a proxy pool only if the site's terms permit it. Rule: **politeness still applies per host, regardless of IP rotation.** Rotation reduces ban risk; it does not license abuse.

- Use a managed proxy service (residential or datacentre) for production.
- Track failures per proxy and bench bad ones.
- Keep one session/cookie set bound to one proxy; do not share cookies across proxies.

## 8. Scraping data not in the response HTML

If the page renders correctly in a browser but `requests.get(...)` returns an empty container:

1. **Open dev tools → Network tab → XHR/Fetch.** Find the JSON endpoint the page calls. Hit that endpoint directly; it is almost always faster, cleaner, and more stable than parsing rendered HTML.
2. **Check the page source vs the inspector.** The inspector shows the *current* DOM; the source shows what the server returned. If the data is in the inspector but not in the source, it was injected by JavaScript.
3. **Last resort: headless browser** (Playwright, Selenium, Splash, PyQt WebKit). Slow and resource-heavy — only when no JSON endpoint is available.

## 9. Network-error guarding

Every request can fail in five distinct ways:

| Failure | Handling |
|---|---|
| DNS error / connection refused | Retry with backoff; cap retries (3–5); log and skip |
| Timeout | Always set `timeout=`; retry once with longer timeout |
| 5xx server error | Exponential backoff; respect `Retry-After`; cap retries |
| 429 rate limit | Honour `Retry-After`; lengthen delay floor for the rest of the run |
| 4xx auth/forbidden | Do not retry; investigate (cookies, headers, robots.txt) |

Wrap every fetch with a retry decorator. **Never crash a long crawl on a single bad URL** — record and continue.

## 10. Missing-element resilience

Pages drift. A field present on 99 % of records may be missing on 1 %. Naive parsing crashes the whole crawl on the first miss.

**Rules:**

- Use selectors that return lists, then check `if found`. Never index `[0]` blindly.
- Normalise missing → `None`; do not let one missing field sink the row.
- Log the URL when a field is missing; do not log a stack trace per row.
- Schema-validate per row (Pandera/pydantic) at the end of each batch — failure rate is a quality signal.

## 11. Pattern discovery: two skills

The two abilities a scraper needs:

1. **Find the right URLs that return the data you want.**
   - Browse the site as a human; observe URL changes.
   - Identify list pages vs detail pages; identify pagination patterns.
   - Use search forms; record the exact URL/params they generate.
   - Check sitemap.xml for a server-blessed enumeration.
2. **Find the structure in the HTML document.**
   - Identify repeating wrappers (`<li class="result-item">`, `<div class="card">`).
   - Pin selectors to **stable** attributes (`data-*`, semantic class names) over fragile ones (auto-generated hashes, deeply nested positions).
   - Verify selectors against ≥3 records before scaling.

## 12. Troubleshooting workflow

When a scraper breaks:

1. **Print everything.** Status code, response length, response headers, first 500 bytes of body. Most bugs are visible in 5 lines of output.
2. **Diff browser vs scraper.** Open the URL in your browser; compare what your code sees vs what the browser sees. Different content = headers, cookies, or JS rendering issue.
3. **Inspect the actual response, not the rendered DOM.** Right-click → "View source" (not "Inspect element") to see what the server actually returned. The DOM in the inspector is the post-JavaScript view.
4. **Make small changes.** Change one variable at a time. Re-run.
5. **Reproduce in a REPL.** The interactive shell beats edit-save-run for HTTP debugging.
6. **Read the response body on errors.** 4xx and 5xx pages often explain the problem ("missing CSRF token," "rate limit exceeded").
7. **If desperate, use mitmproxy** to capture exactly what the browser sends and replay from your code.

## 13. Anti-patterns

- Impersonating a browser instead of identifying honestly, or ignoring the content difference that follows.
- Sending cookies to sites that don't require login — invites tracking and bans.
- POSTing directly to a form's submit URL without fetching hidden CSRF fields first.
- Ignoring robots.txt because "it's not legally binding."
- No `time.sleep` between requests — saturates the host and earns a ban.
- Rotating IPs as a substitute for politeness rather than as a complement.
- Indexing parsed nodes with `[0]` without checking emptiness.
- Crashing a 100 k-URL crawl on the first 404.
- Trusting the inspector's DOM as a parsing target instead of the raw response source.
- Using a headless browser when a JSON XHR endpoint exists.
- Re-running the entire crawl from zero on every bug fix instead of resuming from a checkpoint.

## 14. Ship gate

- [ ] Engine User-Agent with contact URL; complete, well-formed headers.
- [ ] Sessions used only when login required; cookies stripped otherwise.
- [ ] Hidden form fields fetched fresh and resubmitted.
- [ ] robots.txt parsed; disallowed paths skipped; `Crawl-delay` honoured.
- [ ] Default sleep 1–3 s with jitter; concurrency ≤2 per host.
- [ ] Retry policy: exponential backoff on 5xx/429; cap retries; respect `Retry-After`.
- [ ] Selectors verified against ≥3 records.
- [ ] Missing fields normalised, not crashed.
- [ ] Per-URL errors logged, crawl continues.
- [ ] Checkpoint file or resumable queue exists for crawls >5 min.
- [ ] If a JSON XHR endpoint exists, that is used instead of HTML parsing.

## See also

- `web-scraping-foundations` — engine's HTTP/HTML basics
- `scraping-politeness-and-ratelimiting` — extended politeness layer
- `scraping-engineering-python` — caching, concurrency, dynamic content, Scrapy
- `data-quality-assessment` — schema-validate scraped output

Evidence and currentness: RFC 9309 *Robots Exclusion Protocol* (IETF, September 2022),
rfc-editor.org/rfc/rfc9309 (not re-read on 2026-09-24; RFC status is stable);
the `Crawl-delay` directive is not part of RFC 9309 and is honoured as a courtesy only.
Legality of scraping any specific site: NOT_ASSESSED; route to `../../pi-investigation/references/legal-and-ethical-bounds.md`.

Sources: Brody (2017) *The Ultimate Guide to Web Scraping*; Lawson (2015) *Web Scraping with
Python*; IETF RFC 9309. Reorganised by task.
