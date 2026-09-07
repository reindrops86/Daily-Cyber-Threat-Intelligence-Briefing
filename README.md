# Daily Cyber Threat Intelligence Briefing

Correlates multi-source cyber threat intelligence signals — exploited vulnerabilities, tracked
actor campaigns, dark-web mentions, and multi-source indicator corroboration — into a
prioritized daily briefing, instead of a raw feed dump.

```
Exploited CVE (KEV-listed)
  + sector targeting confirmed by vendor
  + reachable from the internet
  = one critical briefing item, patch within 48 hours
```

A single CVE, IOC, or dark-web post is not a briefing item on its own. It becomes one when it
combines with sector targeting, internal telemetry, or independent corroboration.

## Detections

1. Exploited vulnerability reachable in the environment and targeting the organization's sector
2. Tracked threat actor campaign confirmed active via internal telemetry
3. Dark-web mention referencing the organization or sector (early warning, lower confidence)
4. Indicator corroborated by multiple independent sources
5. Newly disclosed high-severity vulnerability, reachable but not yet exploited

## Scoring

```
score = base x amplifier_factor x source_confidence x signal_confidence
```

Severity is derived from the score, never hand-set. Corroboration across independent sources
raises confidence; a single unconfirmed source cannot present as certain.

## Lifecycle across daily briefings

Items carry state across runs: `new`, `unchanged`, `escalated`, `de-escalated`, or `resolved`.
Unchanged low- or medium-priority items are suppressed to keep the briefing signal-dense;
critical and high items are never suppressed while still active. A resolved item is reported
once, explicitly, rather than silently dropped from the feed.

## Run

```powershell
python -m app.main
python -m pytest -q
```

The demo runs a synthetic three-day feed and writes, for each day, an analyst briefing, an
executive summary, and a watchlist to `reports/`. It also writes `latest-*.md` copies of the
most recent day for daily automation to overwrite.

- **Analyst briefing:** every reportable item with full evidence, score components, and
  recommended action.
- **Executive summary:** active material risks, items resolved since the last briefing, and the
  multi-day trend.
- **Watchlist:** a compact status line per tracked item.

## Daily Automation

`.github/workflows/daily-reports.yml` runs the briefing pipeline every day at 11:00 UTC and can
be started manually from the repository's **Actions** tab. It uploads the day's reports and
commits changed artifacts only when their content differs from the previous run.

## Scope

This is a deterministic, synthetic MVP. Production collection can map commercial threat feeds,
KEV catalogs, vulnerability scanners, EDR telemetry, and dark-web monitoring services into
`Signal` objects without changing correlation, scoring, or reporting.

## License

MIT. See `LICENSE`.
