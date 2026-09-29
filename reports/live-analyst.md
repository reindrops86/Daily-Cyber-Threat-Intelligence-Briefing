# Analyst Briefing - 2026-09-29

**Generated:** 2026-09-29

> LIVE DATA: vulnerability existence, exploitation status, and severity are sourced from the public CISA KEV catalog and the NVD API. Sector relevance and environment reachability are self-declared by the analyst in config/watchlist.json and are not independently verified -- edit that file to match your real environment before relying on this report. Actor-campaign, dark-web, and corroborated-indicator findings do not appear here unless supplied via data/manual_signals.json; this project has no live source for those signal types.

_Score = base (rule severity) x amplifier_factor (extra corroborating signal types) x source_confidence (independent sources, capped so circular reporting cannot inflate it) x signal_confidence (mean collector confidence) x asset_multiplier (data sensitivity, exposure, and operational importance of the affected asset), capped at 100. Severity is a fixed band on that score, never hand-set._

_Confidence bands: >=0.85 high (multiple reliable sources or direct telemetry), 0.60-0.84 moderate (single reliable source or partial corroboration), <0.60 low (single low-reliability source, e.g. an unconfirmed dark-web post)._

## CTI-001:CVE-2025-25249 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2025-25249
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Fortinet Multiple Products - Fortinet FortiOS, FortiSwitchManager, and FortiSASE contain a heap-based buffer overflow vulnerability that allows an attacker to execute unauthorized code or commands via specially crafted packets. (added 2026-09-09, remediation due 2026-09-12). (first seen 2026-09-09, last seen 2026-09-29; source date 2026-09-09; collected 2026-09-29T16:55:52+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'fortios'). Edit that file to reflect your real environment. (first seen 2026-09-10, last seen 2026-09-29; source date 2026-09-10; collected 2026-09-29)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'EDIT ME: e.g. financial services, healthcare, manufacturing' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-10, last seen 2026-09-10; source date 2026-09-10)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'fortios' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-29; source date 2026-09-11; collected 2026-09-29)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-09-17 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-19490 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-19490
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an authentication-bypass vulnerability involving an alternate path or channel. When the NetScaler appliance is configured as an AAA virtual server or as a Gateway (SSL VPN, ICA Proxy, CVPN, or RDP Proxy), an unauthenticated remote threat actor may be able to bypass authentication. (added 2026-09-09, remediation due 2026-09-12). (first seen 2026-09-09, last seen 2026-09-29; source date 2026-09-09; collected 2026-09-29T16:55:52+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-11, last seen 2026-09-29; source date 2026-09-11; collected 2026-09-29)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-29; source date 2026-09-11; collected 2026-09-29)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-09-18 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-8452 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-8452
**Severity:** high | **Score:** 50.59 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-25, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (4 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** deadline passed
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler ADC and NetScaler Gateway - Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability which could lead to denial of service.  (added 2026-08-26, remediation due 2026-08-29). (first seen 2026-08-26, last seen 2026-09-25; source date 2026-08-26; collected 2026-09-25T15:51:52+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-11, last seen 2026-09-25; source date 2026-09-11; collected 2026-09-25)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-25; source date 2026-09-11; collected 2026-09-25)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-09-18 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-88771 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-88771
**Severity:** medium | **Score:** 49.12 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 5
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands. (added 2026-09-27, remediation due 2026-09-30). (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:52+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-28, last seen 2026-09-29; source date 2026-09-28; collected 2026-09-29)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-28, last seen 2026-09-29; source date 2026-09-28; collected 2026-09-29)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.15, 'signal_confidence': 0.678, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-05 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-88772 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-88772
**Severity:** medium | **Score:** 49.12 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 5
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service (added 2026-09-27, remediation due 2026-09-30). (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:52+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-28, last seen 2026-09-29; source date 2026-09-28; collected 2026-09-29)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-28, last seen 2026-09-29; source date 2026-09-28; collected 2026-09-29)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.15, 'signal_confidence': 0.678, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-05 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-005:CVE-2026-88773 - Newly disclosed high-severity vulnerability reachable but not yet exploited: CVE-2026-88773
**Severity:** low | **Score:** 28.35 | **State:** NEW
**What changed:** First observed.
**Why reported today:** state changed to NEW
**Independent sources:** 2
**Evidence:**
- [nvd, reliability A, confidence 0.90, supports] NVD: CVE-2026-88773, CVSS 10.0. Inconsistent interpretation of HTTP requests ('HTTP Request/Response smuggling') vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before  (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:53+00:00; [original source](https://nvd.nist.gov/vuln/detail/CVE-2026-88773))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-29; source date 2026-09-29; collected 2026-09-29)
**Score components:** {'base': 40.0, 'amplifier_factor': 1.0, 'source_confidence': 1.05, 'signal_confidence': 0.75, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-29 | **Recommended action:** Prioritize patching ahead of public exploitation; track KEV status daily.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-005:CVE-2026-88774 - Newly disclosed high-severity vulnerability reachable but not yet exploited: CVE-2026-88774
**Severity:** low | **Score:** 28.35 | **State:** NEW
**What changed:** First observed.
**Why reported today:** state changed to NEW
**Independent sources:** 2
**Evidence:**
- [nvd, reliability A, confidence 0.90, supports] NVD: CVE-2026-88774, CVSS 7.2. Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gatewa (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:53+00:00; [original source](https://nvd.nist.gov/vuln/detail/CVE-2026-88774))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-29; source date 2026-09-29; collected 2026-09-29)
**Score components:** {'base': 40.0, 'amplifier_factor': 1.0, 'source_confidence': 1.05, 'signal_confidence': 0.75, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-29 | **Recommended action:** Prioritize patching ahead of public exploitation; track KEV status daily.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-005:CVE-2026-88775 - Newly disclosed high-severity vulnerability reachable but not yet exploited: CVE-2026-88775
**Severity:** low | **Score:** 28.35 | **State:** NEW
**What changed:** First observed.
**Why reported today:** state changed to NEW
**Independent sources:** 2
**Evidence:**
- [nvd, reliability A, confidence 0.90, supports] NVD: CVE-2026-88775, CVSS 9.8. Memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS a (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:53+00:00; [original source](https://nvd.nist.gov/vuln/detail/CVE-2026-88775))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-29; source date 2026-09-29; collected 2026-09-29)
**Score components:** {'base': 40.0, 'amplifier_factor': 1.0, 'source_confidence': 1.05, 'signal_confidence': 0.75, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-29 | **Recommended action:** Prioritize patching ahead of public exploitation; track KEV status daily.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-005:CVE-2026-88776 - Newly disclosed high-severity vulnerability reachable but not yet exploited: CVE-2026-88776
**Severity:** low | **Score:** 28.35 | **State:** NEW
**What changed:** First observed.
**Why reported today:** state changed to NEW
**Independent sources:** 2
**Evidence:**
- [nvd, reliability A, confidence 0.90, supports] NVD: CVE-2026-88776, CVSS 9.8. Memory overflow vulnerability vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.
This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1. (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:53+00:00; [original source](https://nvd.nist.gov/vuln/detail/CVE-2026-88776))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-29; source date 2026-09-29; collected 2026-09-29)
**Score components:** {'base': 40.0, 'amplifier_factor': 1.0, 'source_confidence': 1.05, 'signal_confidence': 0.75, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-29 | **Recommended action:** Prioritize patching ahead of public exploitation; track KEV status daily.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-005:CVE-2026-88777 - Newly disclosed high-severity vulnerability reachable but not yet exploited: CVE-2026-88777
**Severity:** low | **Score:** 28.35 | **State:** NEW
**What changed:** First observed.
**Why reported today:** state changed to NEW
**Independent sources:** 2
**Evidence:**
- [nvd, reliability A, confidence 0.90, supports] NVD: CVE-2026-88777, CVSS 9.8. Memory overflow vulnerability vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1 (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:53+00:00; [original source](https://nvd.nist.gov/vuln/detail/CVE-2026-88777))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-29; source date 2026-09-29; collected 2026-09-29)
**Score components:** {'base': 40.0, 'amplifier_factor': 1.0, 'source_confidence': 1.05, 'signal_confidence': 0.75, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-29 | **Recommended action:** Prioritize patching ahead of public exploitation; track KEV status daily.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-005:CVE-2026-88778 - Newly disclosed high-severity vulnerability reachable but not yet exploited: CVE-2026-88778
**Severity:** low | **Score:** 28.35 | **State:** NEW
**What changed:** First observed.
**Why reported today:** state changed to NEW
**Independent sources:** 2
**Evidence:**
- [nvd, reliability A, confidence 0.90, supports] NVD: CVE-2026-88778, CVSS 7.5. Predictable exact value from previous values vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS,  (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:53+00:00; [original source](https://nvd.nist.gov/vuln/detail/CVE-2026-88778))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-29; source date 2026-09-29; collected 2026-09-29)
**Score components:** {'base': 40.0, 'amplifier_factor': 1.0, 'source_confidence': 1.05, 'signal_confidence': 0.75, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-29 | **Recommended action:** Prioritize patching ahead of public exploitation; track KEV status daily.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-005:CVE-2026-88771 - Newly disclosed high-severity vulnerability reachable but not yet exploited: CVE-2026-88771
**Severity:** low | **Score:** 27.72 | **State:** NEW
**What changed:** First observed.
**Why reported today:** state changed to NEW
**Independent sources:** 3
**Evidence:**
- [nvd, reliability A, confidence 0.90, supports] NVD: CVE-2026-88771, CVSS 9.8. Improper input validation vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37. (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:53+00:00; [original source](https://nvd.nist.gov/vuln/detail/CVE-2026-88771))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-29; source date 2026-09-29; collected 2026-09-29)
**Score components:** {'base': 40.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.7, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-29 | **Recommended action:** Prioritize patching ahead of public exploitation; track KEV status daily.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-005:CVE-2026-88772 - Newly disclosed high-severity vulnerability reachable but not yet exploited: CVE-2026-88772
**Severity:** low | **Score:** 27.72 | **State:** NEW
**What changed:** First observed.
**Why reported today:** state changed to NEW
**Independent sources:** 3
**Evidence:**
- [nvd, reliability A, confidence 0.90, supports] NVD: CVE-2026-88772, CVSS 8.1. Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gatewa (first seen 2026-09-27, last seen 2026-09-29; source date 2026-09-27; collected 2026-09-29T16:55:53+00:00; [original source](https://nvd.nist.gov/vuln/detail/CVE-2026-88772))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-29; source date 2026-09-29; collected 2026-09-29)
**Score components:** {'base': 40.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.7, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-29 | **Recommended action:** Prioritize patching ahead of public exploitation; track KEV status daily.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-004:TI-2026-0048 - Indicator corroborated by multiple independent sources: TI-2026-0048
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0048 (2 indicators: 138.124.14.35:9091, 93.152.214.199:8443). malware_family_overlap: correlated malware family elf.evilginx (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0049 - Indicator corroborated by multiple independent sources: TI-2026-0049
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0049 (2 indicators: 177.22.119.68:9001, 207.211.189.214:443). malware_family_overlap: correlated malware family win.danabot (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0050 - Indicator corroborated by multiple independent sources: TI-2026-0050
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0050 (3 indicators: chilloutvrmod.org, chilloutvrmodded.net, https://kittiesmc.com/ws). malware_family_overlap: correlated malware family unknown_stealer (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0051 - Indicator corroborated by multiple independent sources: TI-2026-0051
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0051 (2 indicators: https://89.46.235.116:80/, https://89.46.235.116:9443/). malware_family_overlap: correlated malware family win.metaencryptor (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0052 - Indicator corroborated by multiple independent sources: TI-2026-0052
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0052 (3 indicators: 1ca26b57598f79603d7e4da730c98965, 6161c1e746b8e29297917c72f93652a137691a3b9d4c6d6fbce38f80f7732d34, badbf7f86834fca16610045cb7c13159932bcd4b). malware_family_overlap: correlated malware family win.dboxagent (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0053 - Indicator corroborated by multiple independent sources: TI-2026-0053
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0053 (3 indicators: 833cdd365d2dd29832a711dc2da5a584, c13cea04f598e2b0c248d603a6e31bd13aabb64d8149c1b6a77b64e0b983a86f, f495880eb6ee7bb930a9957f092f395695cf89a4). malware_family_overlap: correlated malware family win.logedrut (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0054 - Indicator corroborated by multiple independent sources: TI-2026-0054
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0054 (3 indicators: 94ffe61fb9619a00d8c1066dc8728df2af733f0b9ca8783a93ecbe1e52e59562, dd63f54137cd8c2ba7bb43cb6a45db5b2238698c, e629a420112f2bcb593f5467a362a91a). malware_family_overlap: correlated malware family win.shimrat (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0055 - Indicator corroborated by multiple independent sources: TI-2026-0055
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0055 (3 indicators: 31edc1eef538fdb429601d26422834b3, 919f9a20b675968f038bf43c009611a697f11119e037ad577bca4bb2fe746f1c, 974abebcdf2bfcb5440d9590234b4814318698eb). malware_family_overlap: correlated malware family win.nanocore (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0056 - Indicator corroborated by multiple independent sources: TI-2026-0056
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0056 (3 indicators: 55d635733571cf404f3af64646dc97e9, 668dd8566eacd7b89dab013b36cccf0f94be8c4a, ce3d16f1bcb319135a99b10d4daa2a680c2cadadb8d8082b39d3696b7016e096). malware_family_overlap: correlated malware family win.gcleaner (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0057 - Indicator corroborated by multiple independent sources: TI-2026-0057
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0057 (4 indicators: 0eedde175f5d230ee129dc4add72be8a32e7c05a, 12651a9b77448b0bc439f301d24fc52cd331705f10cb58103f48a1d8b02caea2, 221e2c855e78d5cc7fb84738effb88bb11a47be6ce10530c909534e15f47e0b4, c705fea2fd2e6c119c1138f1b74cd798). malware_family_overlap: correlated malware family win.svcstealer (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0058 - Indicator corroborated by multiple independent sources: TI-2026-0058
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0058 (3 indicators: 0c7dd3b979c3fdeba56c6ae312345548, 2cbd1f5b16cc5e17be51a801de7fed705a2336a5, fb48f55e9e2b1ef2d904b0f06547ce698bcb151b43dd032fc7257a7c0f940bd4). malware_family_overlap: correlated malware family jar.crossrat (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0059 - Indicator corroborated by multiple independent sources: TI-2026-0059
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0059 (3 indicators: 541677c2ce44edbb6241907c36463e6ded77a9d7cdb48ceb4113f1111ad2f9e8, aafeaf4892cd200b9dd7b9e03259b49204d2973b, f5ec29d01c9adb0ecabb2da6bc8fb81a). malware_family_overlap: correlated malware family win.wannacryptor (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0060 - Indicator corroborated by multiple independent sources: TI-2026-0060
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0060 (2 indicators: blancharl.icu, courtoos.icu). malware_family_overlap: correlated malware family js.kongtuke (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0061 - Indicator corroborated by multiple independent sources: TI-2026-0061
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0061 (4 indicators: 46.246.12.23:32722, 46.246.12.23:7045, brain.dynip.se, jamesmore02.work.gd). malware_family_overlap: correlated malware family win.houdini (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0062 - Indicator corroborated by multiple independent sources: TI-2026-0062
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0062 (3 indicators: 94.154.43.83:8443, https://ns.devmicro7.workers.dev/zips/f2d0984b93e808eb.zip, sk.bumblemovies.com). malware_family_overlap: correlated malware family jar.microstealer (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0063 - Indicator corroborated by multiple independent sources: TI-2026-0063
**Severity:** low | **Score:** 5.25 | **State:** STALE _Score and severity reflect the last active measurement on 2026-09-26, not current risk; state is STALE._
**What changed:** No supporting evidence for 3 day(s), past the 2-day freshness window for this finding type.
**Why reported today:** state changed to STALE
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0063 (2 indicators: 2a018987d8fb348a3e5e05595afbcd4bfa5631b6e0df83219390cca2e5ea758a, https://theoremaoliveoil.com/wp-content/uploads/2019/04/pieletjf.exe). malware_family_overlap: correlated malware family win.koiloader (first seen 2026-09-24, last seen 2026-09-26; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.
