# Daily Cyber Threat Intelligence Briefing

> **All data in this project is synthetic.** Every actor id, CVE, organization name, IP
> address, and telemetry event is fabricated for demonstration. CVE ids use the year 2099
> and a `-SYNTH` suffix so they cannot be mistaken for a real, assignable identifier. IP
> addresses are drawn only from the IETF-reserved TEST-NET ranges (RFC 5737):
> `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`. Nothing here corresponds to a real
> vulnerability, incident, or indicator, and nothing should be actioned against real
> infrastructure. The same banner is embedded in every generated report.

Correlates multi-source cyber threat intelligence signals into a prioritized daily
briefing, and tracks each finding through an evidence-backed lifecycle so that a
scanner going quiet is never mistaken for a problem being fixed.

## The problem this project is built around

An earlier version of this engine treated "no longer present in today's feed" as
equivalent to "resolved." That is wrong: a scanner can miss a host, a feed can have an
outage, and an unpatched vulnerability does not patch itself just because nobody
re-reported it today. This version never marks a finding resolved without direct
remediation evidence (a patch deployment record, a credential revocation, an exposure
removal, or a confirmed incident closure) -- and distinguishes *reported* remediation
from *verified* remediation.

## Lifecycle states

| State | Meaning |
|---|---|
| `NEW` | First time this finding was observed. |
| `ACTIVE` | Still observed, and something about it changed materially (score moved). |
| `UNCHANGED` | Still observed, no material change since the last briefing. |
| `PENDING_VERIFICATION` | No supporting evidence today, but still within this finding type's freshness window. Not yet treated as reduced risk. |
| `STALE` | No supporting evidence for longer than the freshness window, with no remediation proof. The claim has expired, not been disproven. |
| `MITIGATED` | Remediation evidence was reported but not yet independently verified. |
| `RESOLVED` | Remediation evidence was independently verified (e.g. a re-scan confirms the fix). |
| `REOPENED` | Supporting evidence reappeared after the finding was `STALE`, `MITIGATED`, or `RESOLVED`. |

A vulnerability finding can sit in `PENDING_VERIFICATION` indefinitely if it is never
remediated -- that is correct behavior, not a bug. A dark-web mention can only ever reach
`STALE`; this engine has no remediation artifact for an unconfirmed forum post, so it is
never allowed to resolve on its own (see `demo_days()` for the run where it happens).

## Suppression, and why suppressed findings are not gone

A finding is suppressed from a given day's report only when **all** of these hold: its
state did not change since the last briefing, its severity is `low` or `medium`, and its
deadline has not passed. Suppressed findings are still tracked with full history and
still appear in the watchlist (flagged `[suppressed this cycle]`). The moment severity
rises, new evidence appears, the deadline passes, or the state changes (including
`STALE`, `MITIGATED`, `RESOLVED`, or `REOPENED`), the finding reappears in the very next
briefing without having lost its record.

## Scoring and confidence

```
score = base (rule severity)
      x amplifier_factor (extra corroborating signal types present)
      x source_confidence (independent sources, capped so shared-upstream
        reports cannot inflate it -- see "Corroboration" below)
      x signal_confidence (mean collector confidence across the evidence used)
      x asset_multiplier (data sensitivity, exposure, and operational
        importance of the affected asset)
```

Severity is a fixed band on that score (`critical` >= 70, `high` >= 50, `medium` >= 30,
`low` below that) -- it is derived, never hand-set.

Confidence bands: `>=0.85` high (multiple reliable sources or direct telemetry),
`0.60-0.84` moderate (a single reliable source or partial corroboration), `<0.60` low (a
single low-reliability source, such as an unconfirmed dark-web post).

## Freshness (per-signal TTL)

Each signal type has a time-to-live before it stops counting as current evidence:

| Signal type | TTL | Rationale |
|---|---|---|
| `multi_source_corroboration` (IP/indicator) | 2 days | Indicators churn fast. |
| `internal_ioc_sighting` | 3 days | Telemetry hits are only relevant briefly. |
| `dark_web_mention` | 1 day | Uncorroborated claims should expire quickly, not linger. |
| `sector_targeting` | 30 days | Targeting assessments persist longer. |
| `actor_campaign_activity` | 21 days | Campaign infrastructure persists. |
| `known_exploited_vulnerability`, `high_severity_vulnerability`, `environment_reachable` | 3650 days | Vulnerability facts stay active until remediation evidence says otherwise -- they do not expire on their own. |

A rule's own freshness window is governed only by its **required** signal types, not by
optional amplifiers -- an amplifier's longer TTL must never stretch out how long a
required signal is allowed to be missing before the finding is treated as stale.

## Corroboration and circular reporting

Two signals that share an `upstream_id` are the same report republished, not two
independent confirmations. The engine collapses them into a single independent source
before computing `source_confidence`, and flags the finding as `circular_reporting` so
an analyst can see that two feeds were not actually independent.

## Asset and business context

Each subject carries an `AssetContext`: owner, internet exposure, production status,
data sensitivity, existing controls, exploitability, and operational importance. This
combines into an `asset_multiplier` so a gap on an internet-facing, production,
crown-jewel asset outranks the same gap on a low-importance system, without hand-tuning
individual rule weights.

## Ownership and remediation tracking

Every finding carries an owner, a deadline (SLA by severity: critical 2 days, high 7,
medium 14, low 30, measured from first observation or the most recent reopening), a
recommended action, and a verification method that states exactly what would need to be
observed to confirm the fix.

## Analyst feedback loop

Analysts can label a finding `useful`, `duplicate`, `false_positive`,
`insufficient_evidence`, `accepted_risk`, or `confirmed_incident` (see
`feedback.FeedbackLog`). These labels feed evaluation metrics -- mean time to triage,
false-positive rate -- for measuring how well the engine is scoring things. They are
**not** fed back automatically into future scoring; that would let a single mislabeled
finding silently change how the engine treats everything after it.

## Executive metrics

The executive report includes: new vs. recurring findings per day, mean time to triage,
mean time to mitigate, overdue critical findings, cumulative reopened findings, the
suppression rate, the false-positive rate (from analyst feedback), and the total
exposure trend (sum of reportable scores per day).

## Automated quality gates

Before a day's reports overwrite the `latest-*.md` files, `quality_gate.run_quality_gate`
checks:

- **Synthetic data labeled** (hard) -- every report carries the synthetic-data banner.
- **No unsafe live indicators** (hard) -- every IP in evidence text is in a reserved
  TEST-NET range and every domain used as an indicator ends in `.example`/`.test`/
  `.invalid`/`.localhost`.
- **Confidence scores explainable** (hard) -- every item exposes its scoring components.
- **Resolved findings have remediation proof** (hard) -- no item in `MITIGATED` or
  `RESOLVED` without at least one remediation-evidence record attached.
- **Report differs from the previous briefing** (soft) -- flags, but does not block, a
  briefing that is byte-identical to yesterday's.

If a hard check fails, that day's dated report and quality-gate file are still written
for audit purposes, but `latest-*.md` is not overwritten and the run prints a warning.

## Run and reproduce

```powershell
python -m app.main
python -m pytest -q
```

`python -m app.main` replays a fixed five-day synthetic feed
(`app/cti_briefing/simulate.py`, dated 2026-09-01 through 2026-09-05) through the full
pipeline and writes, for each day, an analyst briefing, an executive summary, a
watchlist, and a quality-gate report to `reports/`, plus `latest-*.md` copies of the most
recent day. The collection dates in the fixture are fixed for reproducibility; the
`**Generated:**` line in each analyst report uses the actual wall-clock time the command
was run. Because the fixture is deterministic, running the command again reproduces
identical dated reports.

## Daily Automation

`.github/workflows/daily-reports.yml` runs the briefing pipeline every day at 11:00 UTC
and can be started manually from the repository's **Actions** tab. It uploads the day's
reports and commits changed artifacts only when their content differs from the previous
run.

## Layout

```
app/
  main.py                        orchestrates a run: correlate -> gate -> render -> write
  cti_briefing/
    schema.py                    Signal, Item, AssetContext, states, TTLs, safety checks
    engine.py                    rule definitions, corroboration, scoring, advance()
    feedback.py                  analyst feedback log and executive trend metrics
    quality_gate.py               pre-publish checks
    reports.py                    analyst / executive / watchlist rendering
    simulate.py                   five-day synthetic fixture (safe, reserved indicators)
tests/
  test_lifecycle.py              state-machine unit tests, incl. the full transition chain
  test_core.py                   integration tests over the demo fixture and quality gate
reports/                         generated markdown, one set per day plus `latest-*`
```

## Limitations

- **Data gaps look like `PENDING_VERIFICATION`, not confirmation of anything.** A
  scanner outage and a genuinely fixed problem produce the same "no evidence today"
  input; this engine treats both identically as "not yet confirmed," by design. Actual
  disambiguation requires a real collection-health signal, which this demo does not have.
- **Source dependence.** All corroboration and confidence math is a function of the
  sources actually configured. A single compromised or mistaken feed used across several
  rules will bias every finding derived from it in the same direction.
- **False positives are possible and expected.** Scoring and lifecycle logic reduce
  noise; they do not eliminate mis-scoped rules, coincidental signal co-occurrence, or
  stale asset-context assumptions. The analyst feedback loop exists to measure this rate,
  not to guarantee it is zero.
- **This is a demonstration, not a detection product.** Rule thresholds, TTLs, and
  scoring weights are illustrative and hand-set, not calibrated against real outcome
  data. Production use would require real collectors, a real collection-health signal,
  and calibration against a labeled history of true/false positives.

## License

MIT. See `LICENSE`.
