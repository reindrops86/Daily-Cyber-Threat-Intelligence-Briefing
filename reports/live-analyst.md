# Analyst Briefing - 2026-09-30

**Generated:** 2026-09-30

> LIVE DATA: vulnerability existence, exploitation status, and severity are sourced from the public CISA KEV catalog and the NVD API. Sector relevance and environment reachability are self-declared by the analyst in config/watchlist.json and are not independently verified -- edit that file to match your real environment before relying on this report. Infrastructure clusters, direct KEV exposure observations, and provider enrichment context may be supplied through data/manual_signals.json by Threat-Ingest. Imported provider context is evidence for analyst review, not an independent verdict of maliciousness. Actor-campaign and dark-web findings are unavailable unless supplied by an analyst.

_Score = base (rule severity) x amplifier_factor (extra corroborating signal types) x source_confidence (independent sources, capped so circular reporting cannot inflate it) x signal_confidence (mean collector confidence) x asset_multiplier (data sensitivity, exposure, and operational importance of the affected asset), capped at 100. Severity is a fixed band on that score, never hand-set._

_Confidence bands: >=0.85 high (multiple reliable sources or direct telemetry), 0.60-0.84 moderate (single reliable source or partial corroboration), <0.60 low (single low-reliability source, e.g. an unconfirmed dark-web post)._

## CTI-001:CVE-2025-25249 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2025-25249
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Fortinet Multiple Products - Fortinet FortiOS, FortiSwitchManager, and FortiSASE contain a heap-based buffer overflow vulnerability that allows an attacker to execute unauthorized code or commands via specially crafted packets. (added 2026-09-09, remediation due 2026-09-12). (first seen 2026-09-09, last seen 2026-09-30; source date 2026-09-09; collected 2026-09-30T16:53:03+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'fortios'). Edit that file to reflect your real environment. (first seen 2026-09-10, last seen 2026-09-30; source date 2026-09-10; collected 2026-09-30)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'EDIT ME: e.g. financial services, healthcare, manufacturing' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-10, last seen 2026-09-10; source date 2026-09-10)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'fortios' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-30; source date 2026-09-11; collected 2026-09-30)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-09-17 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-19490 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-19490
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an authentication-bypass vulnerability involving an alternate path or channel. When the NetScaler appliance is configured as an AAA virtual server or as a Gateway (SSL VPN, ICA Proxy, CVPN, or RDP Proxy), an unauthenticated remote threat actor may be able to bypass authentication. (added 2026-09-09, remediation due 2026-09-12). (first seen 2026-09-09, last seen 2026-09-30; source date 2026-09-09; collected 2026-09-30T16:53:03+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-11, last seen 2026-09-30; source date 2026-09-11; collected 2026-09-30)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-30; source date 2026-09-11; collected 2026-09-30)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-09-18 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-8452 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-8452
**Severity:** high | **Score:** 50.59 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-25, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (5 day(s) since last observed); not yet treated as reduced risk.
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
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** severity requires continued visibility
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands. (added 2026-09-27, remediation due 2026-09-30). (first seen 2026-09-27, last seen 2026-09-30; source date 2026-09-27; collected 2026-09-30T16:53:03+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-30; source date 2026-09-29; collected 2026-09-30)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-29, last seen 2026-09-30; source date 2026-09-29; collected 2026-09-30)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-06 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-88772 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-88772
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** severity requires continued visibility
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service (added 2026-09-27, remediation due 2026-09-30). (first seen 2026-09-27, last seen 2026-09-30; source date 2026-09-27; collected 2026-09-30T16:53:03+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-29, last seen 2026-09-30; source date 2026-09-29; collected 2026-09-30)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-29, last seen 2026-09-30; source date 2026-09-29; collected 2026-09-30)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-10-06 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-006:1.14.100.25 - Infrastructure enrichment observed for an indicator: 1.14.100.25
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 1.14.100.25: ASN=AS45090; network=TENCENT-NET-AP - Shenzhen Tencent Computer Systems Company Limited; country=CN; tags=FRPS, HTTP, MYSQL, OPENVPN; resolved_ips=1.14.100.25; TLS fingerprints=c63c1822a564a1e6f7483f6bc20e5105e9e3c0818ab9c98ae372e3d753771cc5, d8df8a4a64ecf6094fd09b928751376f7dc5246182bd422338f6fe1b8ef64995; open_ports=443, 1194, 3306, 7000, 18080; service_count=6. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:103.42.30.245 - Infrastructure enrichment observed for an indicator: 103.42.30.245
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 103.42.30.245: ASN=AS62468; network=HKCLOUDX - VpsQuan L.L.C.; country=HK; tags=DCERPC, HTTP, SMB, UNKNOWN; resolved_ips=103.42.30.245; related_domains=usdt888.club, winapp.work; TLS fingerprints=372eea056604a6dcd33cc585789e7a314125d80f32cd31be3cc14195e8ecd512; open_ports=135, 139, 445, 5357, 8020, 8027, 8383, 8443; service_count=8. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:120.46.128.236 - Infrastructure enrichment observed for an indicator: 120.46.128.236
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 120.46.128.236: ASN=AS55990; network=HWCSNET - Huawei Cloud Service data center; country=CN; tags=HTTP, SSH; resolved_ips=120.46.128.236; open_ports=22, 3000, 8100, 9000, 9001; service_count=5. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:130.94.29.211 - Infrastructure enrichment observed for an indicator: 130.94.29.211
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 130.94.29.211: ASN=AS154177; network=LIGHT4-AS-AP - LIGHT NODE LIMITED; country=KR; tags=DNS, HTTP, MYSQL, SSH; resolved_ips=130.94.29.211; TLS fingerprints=58e429f0a00f76931da8488aee9bd0e62f03066388991811b7db4b1461923874; open_ports=22, 53, 80, 443, 888, 3306, 8080, 8088, 8090, 8888, 9999; service_count=11. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:139.99.88.62 - Infrastructure enrichment observed for an indicator: 139.99.88.62
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 139.99.88.62: ASN=AS16276; network=OVH - OVH SAS; country=SG; tags=HTTP, SSH; resolved_ips=139.99.88.62; related_domains=62.ip-139-99-88.net, vps-e95c3321.vps.ovh.ca; open_ports=22, 8080; service_count=2. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:155.103.71.233 - Infrastructure enrichment observed for an indicator: 155.103.71.233
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 155.103.71.233: ASN=AS44382; network=WhiteLabel - Fiba Cloud Operation Company, LLC; country=TR; resolved_ips=155.103.71.233; service_count=0. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:162.14.107.40 - Infrastructure enrichment observed for an indicator: 162.14.107.40
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 162.14.107.40: ASN=AS45090; network=TENCENT-NET-AP - Shenzhen Tencent Computer Systems Company Limited; country=CN; tags=HTTP; resolved_ips=162.14.107.40; open_ports=8082; service_count=1. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:23.159.160.195 - Infrastructure enrichment observed for an indicator: 23.159.160.195
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 23.159.160.195: ASN=AS26548; network=PUREVOLTAGE-INC - PureVoltage Hosting Inc.; country=US; tags=HTTP; resolved_ips=23.159.160.195; open_ports=8888; service_count=1. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:43.173.38.253 - Infrastructure enrichment observed for an indicator: 43.173.38.253
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 43.173.38.253: ASN=AS132203; network=TENCENT-NET-AP-CN - Tencent Building, Kejizhongyi Avenue; country=ID; resolved_ips=43.173.38.253; service_count=0. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:45.76.110.248 - Infrastructure enrichment observed for an indicator: 45.76.110.248
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 45.76.110.248: ASN=AS20473; network=AS-VULTR - The Constant Company, LLC; country=JP; tags=HTTP, SSH; resolved_ips=45.76.110.248; related_domains=tokyo.getallnodes.com; open_ports=22, 443, 8082, 8084; service_count=4. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:64.118.132.68 - Infrastructure enrichment observed for an indicator: 64.118.132.68
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 64.118.132.68: ASN=AS138997; network=EDCL-AS-AP - Eons Data Communications Limited; country=HK; tags=HTTP, SSH, UNKNOWN; resolved_ips=64.118.132.68; open_ports=22, 8082, 8083, 44321, 44322, 44323; service_count=6. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:89.106.83.156 - Infrastructure enrichment observed for an indicator: 89.106.83.156
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 89.106.83.156: ASN=AS200051; network=VPSLab-Networks - RIZKI ABDUL AZIS; country=DE; tags=DCERPC, HTTP, RDP, SMB, UNKNOWN, WINRM; resolved_ips=89.106.83.156; TLS fingerprints=9f73a80b2d9c8059a7e19ba1f0156ac6d3b775625e9b1f5e322ba1bc4a99dd09; open_ports=135, 139, 445, 3389, 5985, 47001; service_count=6. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.

## CTI-006:93.177.77.234 - Infrastructure enrichment observed for an indicator: 93.177.77.234
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-29, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-censys, reliability C, confidence 0.35, supports] censys enrichment context for 93.177.77.234: ASN=AS55933; network=CLOUDIE-AS-AP - Cloudie Limited; country=HK; tags=HTTP; resolved_ips=93.177.77.234; related_domains=jutbh.my, se123.b28a8.cyou, sjytd.win, yy11.win, yy16.my; TLS fingerprints=cf93931ecbc1db8a6c170a718b52e37cb017bc1f96cc247f14528b5632594709; open_ports=443, 8080, 9000, 18080; service_count=4. Context only; this observation alone does not establish maliciousness. (first seen 2026-09-26, last seen 2026-09-29; source date 2026-09-26; collected 2026-09-29T22:50:23+00:00)
**Score components:** {'base': 15.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.35, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-29 | **Recommended action:** Review the provider context and correlate it with independent telemetry before taking action.
**Verification method:** Re-query the provider and compare its latest observation; absence alone is not remediation.
