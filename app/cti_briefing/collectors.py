"""Live collectors for public, free, unauthenticated threat data.

Only two sources are integrated as genuinely live here: the CISA Known
Exploited Vulnerabilities (KEV) catalog and the NVD recent-CVE feed. Both are
public, require no API key, and involve no credentials, scraping of
restricted content, or dark-web access.

Actor-campaign activity, dark-web mentions, internal telemetry, and
multi-source indicator corroboration have no equivalent free public source.
This module deliberately does not fabricate them; see live.py and
data/manual_signals.json for how an analyst supplies that evidence themselves.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from typing import Callable

from .schema import Signal

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
USER_AGENT = "daily-cti-briefing/1.0 (+https://github.com/reindrops86/Daily-Cyber-Threat-Intelligence-Briefing)"


class CollectionError(Exception):
    """A live source could not be reached. Callers should catch this and
    continue with whatever other sources succeeded, rather than fail the
    whole run over one unreachable feed."""


def _get_json(url: str, timeout: float = 15.0) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - fixed, public HTTPS endpoints only
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        raise CollectionError(f"could not reach {url}: {exc}") from exc


def fetch_cisa_kev(fetch: Callable[[str], dict] = _get_json) -> list[Signal]:
    """Every entry in this catalog is, by CISA's own inclusion criteria, a
    vulnerability with confirmed evidence of active exploitation."""
    payload = fetch(KEV_URL)
    today = date.today().isoformat()
    signals: list[Signal] = []
    for entry in payload.get("vulnerabilities", []):
        cve = entry.get("cveID")
        if not cve:
            continue
        signals.append(Signal(
            signal_type="known_exploited_vulnerability",
            subject=cve,
            source="cisa_kev",
            source_reliability="A",
            confidence=0.99,
            detail=(
                f"CISA KEV catalog: {entry.get('vendorProject', 'unknown vendor')} "
                f"{entry.get('product', '')} - {entry.get('shortDescription', '')} "
                f"(added {entry.get('dateAdded', 'unknown date')}, remediation due "
                f"{entry.get('dueDate', 'unknown')})."
            ),
            observed_at=entry.get("dateAdded", today),
            collected_at=today,
            upstream_id=f"cisa-kev:{cve}",
        ))
    return signals


def fetch_recent_high_severity_cves(
    days: int = 2, min_cvss: float = 7.0, limit: int = 25,
    fetch: Callable[[str], dict] = _get_json,
) -> list[Signal]:
    """Recently published CVEs above a CVSS floor, from the public NVD API.

    No API key is used, so this is deliberately capped and best-effort: NVD
    rate-limits unauthenticated callers, and a daily briefing does not need
    an exhaustive feed, only enough to demonstrate real prioritization.
    """
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days)
    url = (
        f"{NVD_URL}?pubStartDate={start.strftime('%Y-%m-%dT%H:%M:%S.000')}"
        f"&pubEndDate={end.strftime('%Y-%m-%dT%H:%M:%S.000')}&resultsPerPage={limit}"
    )
    payload = fetch(url)
    today = date.today().isoformat()
    signals: list[Signal] = []
    for item in payload.get("vulnerabilities", []):
        cve = item.get("cve", {})
        cve_id = cve.get("id")
        metrics = cve.get("metrics", {})
        score = None
        for key in ("cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
            if metrics.get(key):
                score = metrics[key][0]["cvssData"]["baseScore"]
                break
        if not cve_id or score is None or score < min_cvss:
            continue
        descriptions = cve.get("descriptions", [])
        summary = next((d["value"] for d in descriptions if d.get("lang") == "en"), "")
        signals.append(Signal(
            signal_type="high_severity_vulnerability",
            subject=cve_id,
            source="nvd",
            source_reliability="A",
            confidence=0.9,
            detail=f"NVD: {cve_id}, CVSS {score}. {summary[:200]}",
            observed_at=(cve.get("published") or today)[:10],
            collected_at=today,
        ))
    return signals
