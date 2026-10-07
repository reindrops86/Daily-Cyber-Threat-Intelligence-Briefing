# Analyst Briefing - 2026-10-07

**Generated:** 2026-10-07

> LIVE DATA: vulnerability existence, exploitation status, and severity are sourced from the public CISA KEV catalog and the NVD API. Sector relevance and environment reachability are self-declared by the analyst in config/watchlist.json and are not independently verified -- edit that file to match your real environment before relying on this report. Infrastructure clusters, direct KEV exposure observations, and provider enrichment context may be supplied through data/manual_signals.json by Threat-Ingest. Imported provider context is evidence for analyst review, not an independent verdict of maliciousness. Actor-campaign and dark-web findings are unavailable unless supplied by an analyst.

_Score = base (rule severity) x amplifier_factor (extra corroborating signal types) x source_confidence (independent sources, capped so circular reporting cannot inflate it) x signal_confidence (mean collector confidence) x asset_multiplier (data sensitivity, exposure, and operational importance of the affected asset), capped at 100. Severity is a fixed band on that score, never hand-set._

_Confidence bands: >=0.85 high (multiple reliable sources or direct telemetry), 0.60-0.84 moderate (single reliable source or partial corroboration), <0.60 low (single low-reliability source, e.g. an unconfirmed dark-web post)._

_Evidence labels: Reported fact = published by an authoritative source (CISA KEV, NVD, vendor advisory); Observed telemetry = seen directly in the organization's own tooling; Third-party report = a feed, sharing group, or monitoring service's claim, not verified here; Automated inference = produced by correlation or provider enrichment (Threat-Ingest clusters, exposure matches, provider context) and requires analyst review; Analyst assessment = a judgment declared by the analyst (config/watchlist.json, manual entries), not independently verified._

## Vulnerability Patch Priority (KEV + EPSS + CVSS)

_Patch priority combines three independent signals and is shown alongside, not folded into, the finding score: P1 = listed in CISA KEV (exploitation confirmed); P2 = not in KEV but EPSS >= 0.10 or CVSS >= 9.0; P3 = neither. EPSS is FIRST.org's modelled probability of exploitation in the next 30 days; CVSS is the NVD base severity. A missing value is reported as 'n/a', never guessed._

| CVE | Priority | In KEV | EPSS (percentile) | CVSS | Finding |
|---|---|---|---|---|---|
| CVE-2025-25249 | P1 - patch now | yes | 0.039 (90%) | 8.1 | CTI-001:CVE-2025-25249 |
| CVE-2026-19490 | P1 - patch now | yes | 0.232 (98%) | 9.3 | CTI-001:CVE-2026-19490 |
| CVE-2026-8452 | P1 - patch now | yes | 0.010 (62%) | 8.8 | CTI-001:CVE-2026-8452 |
| CVE-2026-88771 | P1 - patch now | yes | 0.011 (64%) | 9.5 | CTI-001:CVE-2026-88771 |
| CVE-2026-88772 | P1 - patch now | yes | 0.013 (70%) | 9.5 | CTI-001:CVE-2026-88772 |
| CVE-2026-88779 | P1 - patch now | yes | 0.006 (47%) | 8.7 | CTI-001:CVE-2026-88779 |

## CTI-001:CVE-2025-25249 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2025-25249
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Addresses:** PIR-001
**Patch priority:** P1 - patch now (listed in CISA KEV, exploitation confirmed)
**Evidence:**
- **Reported fact:** [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Fortinet Multiple Products - Fortinet FortiOS, FortiSwitchManager, and FortiSASE contain a heap-based buffer overflow vulnerability that allows an attacker to execute unauthorized code or commands via specially crafted packets. (added 2026-09-09, remediation due 2026-09-12). (first seen 2026-09-09, last seen 2026-10-07; source date 2026-09-09; collected 2026-10-07T17:51:59+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- **Analyst assessment:** [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'fortios'). Edit that file to reflect your real environment. (first seen 2026-09-10, last seen 2026-10-07; source date 2026-09-10; collected 2026-10-07)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'EDIT ME: e.g. financial services, healthcare, manufacturing' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-10, last seen 2026-09-10; source date 2026-09-10)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'fortios' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-10-07; source date 2026-09-11; collected 2026-10-07)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-09-17 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-19490 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-19490
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Addresses:** PIR-001
**Patch priority:** P1 - patch now (listed in CISA KEV, exploitation confirmed)
**Evidence:**
- **Reported fact:** [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an authentication-bypass vulnerability involving an alternate path or channel. When the NetScaler appliance is configured as an AAA virtual server or as a Gateway (SSL VPN, ICA Proxy, CVPN, or RDP Proxy), an unauthenticated remote threat actor may be able to bypass authentication. (added 2026-09-09, remediation due 2026-09-12). (first seen 2026-09-09, last seen 2026-10-07; source date 2026-09-09; collected 2026-10-07T17:51:59+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- **Analyst assessment:** [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-11, last seen 2026-10-07; source date 2026-09-11; collected 2026-10-07)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-10-07; source date 2026-09-11; collected 2026-10-07)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-09-18 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-8452 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-8452
**Severity:** high | **Score:** 50.59 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-25, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (12 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** deadline passed
**Independent sources:** 3
**Addresses:** PIR-001
**Patch priority:** P1 - patch now (listed in CISA KEV, exploitation confirmed)
**Evidence:**
- **Reported fact:** [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler ADC and NetScaler Gateway - Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability which could lead to denial of service.  (added 2026-08-26, remediation due 2026-08-29). (first seen 2026-08-26, last seen 2026-09-25; source date 2026-08-26; collected 2026-09-25T15:51:52+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- **Analyst assessment:** [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-11, last seen 2026-09-25; source date 2026-09-11; collected 2026-09-25)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-25; source date 2026-09-11; collected 2026-09-25)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-09-18 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-88771 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-88771
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Addresses:** PIR-001
**Patch priority:** P1 - patch now (listed in CISA KEV, exploitation confirmed)
**Evidence:**
- **Reported fact:** [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands. (added 2026-09-27, remediation due 2026-09-30). (first seen 2026-09-27, last seen 2026-10-07; source date 2026-09-27; collected 2026-10-07T17:51:59+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- **Analyst assessment:** [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-10-07; source date 2026-09-29; collected 2026-10-07)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-29, last seen 2026-10-07; source date 2026-09-29; collected 2026-10-07)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-06 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-88772 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-88772
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Addresses:** PIR-001
**Patch priority:** P1 - patch now (listed in CISA KEV, exploitation confirmed)
**Evidence:**
- **Reported fact:** [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service (added 2026-09-27, remediation due 2026-09-30). (first seen 2026-09-27, last seen 2026-10-07; source date 2026-09-27; collected 2026-10-07T17:51:59+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- **Analyst assessment:** [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-10-07; source date 2026-09-29; collected 2026-10-07)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-29, last seen 2026-10-07; source date 2026-09-29; collected 2026-10-07)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-06 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-88779 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-88779
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** severity requires continued visibility
**Independent sources:** 3
**Addresses:** PIR-001
**Patch priority:** P1 - patch now (listed in CISA KEV, exploitation confirmed)
**Evidence:**
- **Reported fact:** [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC (formerly Citrix ADC) and Citrix NetScaler Gateway (formerly Citrix Gateway) contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for a denial of service. (added 2026-10-04, remediation due 2026-10-07). (first seen 2026-10-04, last seen 2026-10-07; source date 2026-10-04; collected 2026-10-07T17:51:59+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- **Analyst assessment:** [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-10-05, last seen 2026-10-07; source date 2026-10-05; collected 2026-10-07)
- **Analyst assessment:** [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-10-05, last seen 2026-10-07; source date 2026-10-05; collected 2026-10-07)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-12 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.
