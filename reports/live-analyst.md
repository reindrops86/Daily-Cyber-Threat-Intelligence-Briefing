# Analyst Briefing - 2026-09-25

**Generated:** 2026-09-25

> LIVE DATA: vulnerability existence, exploitation status, and severity are sourced from the public CISA KEV catalog and the NVD API. Sector relevance and environment reachability are self-declared by the analyst in config/watchlist.json and are not independently verified -- edit that file to match your real environment before relying on this report. Actor-campaign, dark-web, and corroborated-indicator findings do not appear here unless supplied via data/manual_signals.json; this project has no live source for those signal types.

_Score = base (rule severity) x amplifier_factor (extra corroborating signal types) x source_confidence (independent sources, capped so circular reporting cannot inflate it) x signal_confidence (mean collector confidence) x asset_multiplier (data sensitivity, exposure, and operational importance of the affected asset), capped at 100. Severity is a fixed band on that score, never hand-set._

_Confidence bands: >=0.85 high (multiple reliable sources or direct telemetry), 0.60-0.84 moderate (single reliable source or partial corroboration), <0.60 low (single low-reliability source, e.g. an unconfirmed dark-web post)._

## CTI-001:CVE-2025-25249 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2025-25249
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Fortinet Multiple Products - Fortinet FortiOS, FortiSwitchManager, and FortiSASE contain a heap-based buffer overflow vulnerability that allows an attacker to execute unauthorized code or commands via specially crafted packets. (added 2026-09-09, remediation due 2026-09-12). (first seen 2026-09-09, last seen 2026-09-25; source date 2026-09-09; collected 2026-09-25T15:51:52+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'fortios'). Edit that file to reflect your real environment. (first seen 2026-09-10, last seen 2026-09-25; source date 2026-09-10; collected 2026-09-25)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'EDIT ME: e.g. financial services, healthcare, manufacturing' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-10, last seen 2026-09-10; source date 2026-09-10)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'fortios' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-25; source date 2026-09-11; collected 2026-09-25)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-09-17 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-19490 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-19490
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler - Citrix NetScaler ADC and NetScaler Gateway contain an authentication-bypass vulnerability involving an alternate path or channel. When the NetScaler appliance is configured as an AAA virtual server or as a Gateway (SSL VPN, ICA Proxy, CVPN, or RDP Proxy), an unauthenticated remote threat actor may be able to bypass authentication. (added 2026-09-09, remediation due 2026-09-12). (first seen 2026-09-09, last seen 2026-09-25; source date 2026-09-09; collected 2026-09-25T15:51:52+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-11, last seen 2026-09-25; source date 2026-09-11; collected 2026-09-25)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-25; source date 2026-09-11; collected 2026-09-25)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-09-18 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-001:CVE-2026-8452 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-8452
**Severity:** high | **Score:** 50.59 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** deadline passed
**Independent sources:** 3
**Evidence:**
- [cisa_kev, reliability A, confidence 0.99, supports] CISA KEV catalog: Citrix NetScaler ADC and NetScaler Gateway - Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability which could lead to denial of service.  (added 2026-08-26, remediation due 2026-08-29). (first seen 2026-08-26, last seen 2026-09-25; source date 2026-08-26; collected 2026-09-25T15:51:52+00:00; [original source](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- [user_watchlist_config, reliability B, confidence 0.60, supports] Declared reachable per config/watchlist.json (matched 'citrix netscaler'). Edit that file to reflect your real environment. (first seen 2026-09-11, last seen 2026-09-25; source date 2026-09-11; collected 2026-09-25)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Organization sector declared as 'airlines and healthcare (research interest, not an operated environment)' in config/watchlist.json; this is a self-declared business fact, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-11; source date 2026-09-11; collected 2026-09-11)
- [user_watchlist_config, reliability C, confidence 0.60, supports] Sector relevance for 'citrix netscaler' declared as 'airlines and healthcare' in config/watchlist.json; this is a self-declared judgment, not independently corroborated. (first seen 2026-09-11, last seen 2026-09-25; source date 2026-09-11; collected 2026-09-25)
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.73, 'asset_multiplier': 0.9}
**Owner:** research | **Deadline:** 2026-09-18 | **Recommended action:** Patch or virtually patch within the SLA window; confirm compensating controls until then.
**Verification method:** Re-scan the asset and confirm the vulnerability signature is no longer detected.

## CTI-004:TI-2026-0002 - Indicator corroborated by multiple independent sources: TI-2026-0002
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0002 (73 indicators: 0356cc5dbb826085c0de5ca038d5888bf29cd4c80b26da987a2b9dc2eee727be, 03745f11d65fcbea95ff01e32e31f0e0a687679deba39156be37ef977424d551, 089fadf8fcee6e35649065940f346777ac0f2067761259bde81b6710fc89d6b8, 0c0de3e0ddad3300bb1e3b17fe4ea48e3cfa7e5d0d313f355a6d25e230b796ff, 104.248.194.193:80, 159812997d29881c7ea02642914fe1efb997130477889e4fe3426f81434b5bad, 15f5980c718cda6c5b16ea81cd153ebef15f07a03378594a669395c0d51c64ed, 1707c849c17706537c7db56edf5f08aeb5e2cfa2d3e9c144a96d75a6dac09268, 1907be92bfb56439610fce9fa7be748c0e424b4c07ab1a163704a30d56b94f53, 206.189.104.97:80, 247a8bd16be5e5d8c26d4e0ba3697ad4abdf523e4424a8105b9688f98bfd4497, 33cb2391cc0a21681eb67b1b85ce43117641059494c249030be388fa178bbda2, 4043c95c58dfa8dedb4f485ea59f849b150d5882f4be8ba36cb98ff9dd67fc4e, 434baa345fb6291b150f5c8d577993c53b2eb18b8987af84142f7fe7e426f973, 4701f196c74af42b5ced01592bf4a74d54437b1c63b8aabfe1f92e9beabec769, 52d2fcbdd59d0beae12c03c5ae13adeffc39f50cec436d6071890a3c1b971d5e, 57fc974927b70736976b88fd369e7547892d8f227e7aa1a322e5b61aa562a93a, 5b66b317f4190b7d5835ee78b02c207ac6ade782564267f75a39cb2cbf46ed9f, 5b7487d9528a49f6b83d41c772529b4d02d08a363c4501a60a3c8f9a3eeb53fa, 5cc27b17795bd0cb766249d43e4082c5b900ef9d1184877cfa9c048533c945e0, 5d73b00bd37e96853bcb1f2cba845ce806b3c0dd8b83be3aaa58d0f42a235152, 5ec78072bdc620125502b8361c19cb3529a6d5b382da40197d2e7c103537fd47, 5f2f8bcba674f06398d2916abceb7e828aa0eb7ae74b2cb26bb0b4d58a14f85c, 665c09db96aa8704a4bfc44d4c4c3e6705c22f074c4c36ac32839e9006dddd30, 6d85af515457833a879ce9442a4b538b57558e10676c57a098db083722c889e3, 6e2c9918a3eee4233cb3058385011fb7c79bf2f801655ff7711174196f1dcb59, 6fa9d4e59f3555278ff55dd617356a51ecb43239abafa333c8fa82da2a1c7088, 7243f66e3c28ef7d20a2ab34b30c577fe6f1f4273145a3379be7d3b9fea625a1, 7667b3e5e69c6203451b915a7c3b8f2227630243dfaa6209b4beff8bcaa520ed, 7d7ccd876375c5eebcf2c8b37d39bfe3eaf1f509fe1bb9ce478ece0d7abfd274, 845de1a956040d6e66c06ad4f8acd0dcf78dc02b6434a95dfa9c4623f6bd07c3, 88ec1d463f4a7241a6cd5638bd5538efab076ac2553e73437a2b6d0924328423, 89aad11bff0ba0d654016e4e95b02f6f94b18f01f09475b83b0d983ed0764af2, 8a4ef80cf6dbce39425c82d90953189e14ff8fc4c69627a6f06d24565c3421ec, 8c8c72b6149130a65f7d69fb97fad7eedd7580fa07f863a62b4d72aa460951bc, 9121ad58f09f380d849ba89071899f8c48c436bac21f7a3aba084ea0861c16cd, 984154b2fe7ff4fae1bfa0136041b4d9605044042e12037d7de168098f07f0b4, 9bda679c0a2996e9562e2e8477891771c61e872cd226d441d3b17e907c42a762, 9f4404e77102d3778c31c9a88ef98e0e4ba792721edfbbb88cb164cbd1a4db61, a07994990f1976669d69febbe9603be9e10132fe9f6d6e8e4184fa91462cba72, a18aa476ad595ad3567df4fa98f3a615a3c6b6ac450c8dc3d2e95ce98c7634a7, a386c3666f529ec462fd4bfb2fe11ee25924ef4c0bd8a09836479cb900d8eac4, a39eb6928c17a779f4030bf6ac0eeec41f828a64140f2a06cb63b8658e589267, a3e786a3d2b8baa9c1fda58f2116542606e156bee898a6a2d485fd65790029f3, aa1c7587dc1edfa419a4b6a78efae6b6e6265038cf7124253502589805b55c25, aa89eb6107f9ec242faa91a24a099db0850b81b3a845d9e8d30a747e4770e7b2, b30450f0db56652e2652318b24f9a36fb04786af99c22995584766923bebec1e, b92a53b7853807b3f417e8aaab19662f3451480743c3fc6831b8131a5859bfce, basequill9.com, bb2d62df63ff1726eec5e17cc9e30850c39d0a15353aa267a916bcdb75d709c6, bd1b6bed346570b063a14e9f4f7ddf21b19f61dbe1f820e03401fe82c509fd7b, be4c116c7072b012dca6a5ba971d54800bdcc3bae7131f8aca621268b8527b74, bedc5ef2bc2ad17fd0d627b2539a47e6ad55f9b83cfe3febaf8de2ee32e9c9af, beefe66a3125211b8f62829521f59e50ed2a6f214129721cf3dbad6006f98c70, c1284e45e618b6ce2fa48aa7257f3b1b5bd7fe542efd24ebfd9c488a4a5dd048, c59ad0ccb24fd26854831a949138182a707b7f61480b743e118508d4cd424a36, d3552befdb5519741191cd15d8b6e5109c9f8bba584a4506b3c551253f993474, d6df4b637007ff7a81677e739277468e8448d361d3a3321e9175bb433a4c2f6b, d729286210cc1566ea7eef55258bc20fe94e418cb478ac5544feb288e2fb803c, d9ec29da13d670682f81f6bfb172bd3eea79486a0856578126889a8ed1a61db4, delta-canvas.com, e8fdb578177f84033916427efad848f72d8fd43e1672744fc625b5165f2feca7, ef3bec3fc56611025ea5c9e67197f70f8f9d625b3b08eaea7c444f7285264bad, f91311823973108b313e941881d0ba501569b59221585b05cb69d2baeba68a74, fdb0a9a7f5d181c2ac16938a37d7faa375121a945d2e0e3e5c6f3340f8bdf6a4, http://104.248.194.193/api/metrics/run, http://104.248.194.193/contact, https://basequill9.com/curl/av6t87xg9gon/ahlg4goj9kfsh1itrutp47.dat, https://basequill9.com/zyemb6slon_3vwvlkskdijurcyhy5cfntchnavrnmgu/hiddenfix/update, https://delta-canvas.com/zxc/kito, https://delta-canvas.com/zxc/mdw, https://questlyric8.com/api/metrics/run?event=pasted, questlyric8.com). malware_family_overlap: correlated malware family osx.amos (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0003 - Indicator corroborated by multiple independent sources: TI-2026-0003
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0003 (6 indicators: 25ce426b8b075dee1d250a417423b60d55c572a8b38641d919d87b83c4ea6edd, fbc460f7b29d7e709c28fc9368a592f3140fdb51fff5de54471450e250b6345a, https://yoauction.com/curl/b42a0ed9d1ecb72e42d6034502c304845d98805481d99cea4e259359f9ab206e, https://zanderrealestate.com/curl/85cb26206d920216eee0c5f67e8de516b4d55bd1752025bb3c08a069a44fdbdf, yoauction.com, zanderrealestate.com). malware_family_overlap: correlated malware family osx.macsync (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0007 - Indicator corroborated by multiple independent sources: TI-2026-0007
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0007 (19 indicators: http://102.33.78.165:43065/mozi.m, http://103.18.14.237:35291/mozi.m, http://103.186.77.81:45076/mozi.m, http://103.26.83.108:55431/mozi.m, http://103.82.121.182:52844/mozi.m, http://115.50.66.64:58386/mozi.m, http://119.152.228.80:36317/mozi.m, http://124.29.226.80:56932/mozi.m, http://175.107.217.82:48392/mozi.a, http://175.107.3.230:53543/mozi.m, http://183.253.69.180:45735/mozi.m, http://190.196.253.43:11724/mozi.m, http://190.196.253.46:10921/mozi.m, http://202.47.54.27:45758/mozi.m, http://202.70.139.77:49185/mozi.m, http://203.101.186.93:59346/mozi.7, http://203.99.56.135:39928/mozi.m, http://72.255.15.203:45769/mozi.m, http://72.255.32.109:53235/mozi.m). malware_family_overlap: correlated malware family elf.mozi (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0016 - Indicator corroborated by multiple independent sources: TI-2026-0016
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0016 (6 indicators: 193.143.1.247:8848, 41.68.226.249, 41.68.226.249:5554, 46.246.84.6, 46.246.84.6:8848, 5.175.169.212:7777). malware_family_overlap: correlated malware family win.dcrat (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0019 - Indicator corroborated by multiple independent sources: TI-2026-0019
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0019 (2 indicators: 174.129.92.184:8809, f47ed4ce3fb2d369dc31737419e1546abb3be79052b910e52347c05500d908ab). malware_family_overlap: correlated malware family win.grandoreiro (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0020 - Indicator corroborated by multiple independent sources: TI-2026-0020
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0020 (2 indicators: https://res.gridstack.cc/, media.hazelnook.cc). malware_family_overlap: correlated malware family win.acr_stealer (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0021 - Indicator corroborated by multiple independent sources: TI-2026-0021
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0021 (3 indicators: http://178.16.54.165/, http://31.56.19.29, http://45.13.186.37/noncrypt/21-32/hnmh.exe). malware_family_overlap: correlated malware family win.stealc (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0022 - Indicator corroborated by multiple independent sources: TI-2026-0022
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0022 (3 indicators: impact.hjdeboer.com, px-img.leewhitman-raymond.com, sso.ebeenj.com). malware_family_overlap: correlated malware family js.fakeupdates (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0023 - Indicator corroborated by multiple independent sources: TI-2026-0023
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0023 (5 indicators: 87c640d3184c17d3b446a72d5f13d643a774b4ecc7afbedfd4e8da7795ea8077, 8f096174b0ded0a598f634567c618e12808088848cd07eb99ca4ac57a744cdd9, b7a495f517b9bf23f529552b145121f922ab4915e24b663ae68b3007daea3804, d887f20ec383d7ce3a5727856bf7fa68ceb972108b6d0a5dd9924707e820dc24, e34c9d3d3a50be99609cc843f91bbfcd0d79853b8c373c5146bcbf77643fb8c2). malware_family_overlap: correlated malware family win.remoteadmin (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0025 - Indicator corroborated by multiple independent sources: TI-2026-0025
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0025 (3 indicators: http://123.143.141.75:10006/sshd, http://165.73.108.6:8025//sshd, http://174.71.237.86:1101/sshd). malware_family_overlap: correlated malware family elf.sshdoor (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0026 - Indicator corroborated by multiple independent sources: TI-2026-0026
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0026 (2 indicators: http://168.121.168.84/photo.scr, https://nomore.quest/questremoval.exe). malware_family_overlap: correlated malware family win.xmrig (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0028 - Indicator corroborated by multiple independent sources: TI-2026-0028
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0028 (2 indicators: 160.179.176.98:2222, ccb05e8e1b680a6766c9cfffe71e5543f0b9b0432d2ea10d8f4661188ec5b951). malware_family_overlap: correlated malware family win.meterpreter (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0029 - Indicator corroborated by multiple independent sources: TI-2026-0029
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0029 (11 indicators: 3a37758233921a3022659d0e1dfc62d61c990cd8e787512939dad90bb443203b, 5086d80f6e009feaccedf2c69368ddae803e11a8d7ffaafb4b790177828abc90, 586960df8bf559ffbba600f11917a99baed4a875cb7faa5eabc060bcde67277b, 7aac36e30a811f7463cfb882ee6ff76834a60428c436b0b3fa15ff8f94b8db51, 876cc349fd0bcea044f99178e7ab4911a2b078eba1612b7ad5db176e889451d7, 97eaa49999cbcc866fc30ca2ba20f2a1d4e9b01d1c824d3924a185683d2b87c5, aa52e1cbe3208208156ed785dfd651f758e4ef3fd58992144187500dd1159b2b, c78352eaf38880fbc3ce60b4eec4c577478d618c990bbe510dd1367ee3274824, cdcb1f84e63d751507c306ff5469d8e2773df0da132efcfd082483aad0d50bf9, e7f0d98ed2fd14827712e1e9ad514a4dc494a77ef30ae8bf25c599da1d1c9bad, f407f10ce043dce0f4a8aeed21912f20f21f613ec0fe495394451097dc8ced0b). malware_family_overlap: correlated malware family elf.bashlite (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0031 - Indicator corroborated by multiple independent sources: TI-2026-0031
**Severity:** low | **Score:** 5.25 | **State:** PENDING_VERIFICATION _Score and severity reflect the last active measurement on 2026-09-24, not current risk; state is PENDING_VERIFICATION._
**What changed:** No supporting evidence today (1 day(s) since last observed); not yet treated as reduced risk.
**Why reported today:** state changed to PENDING_VERIFICATION
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0031 (3 indicators: http://130.94.30.168:8080/?h=130.94.30.168&p=8080&t=tcp&a=l32&stage=true, http://130.94.30.168:8080/?h=130.94.30.168&p=8080&t=tcp&a=l64&stage=true, http://150.109.94.129:443/?h=150.109.94.129&p=443&t=ws&a=l64&stage=true). malware_family_overlap: correlated malware family elf.snowlight (first seen 2026-09-22, last seen 2026-09-24; source date 2026-09-22; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0048 - Indicator corroborated by multiple independent sources: TI-2026-0048
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0048 (2 indicators: 138.124.14.35:9091, 93.152.214.199:8443). malware_family_overlap: correlated malware family elf.evilginx (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0049 - Indicator corroborated by multiple independent sources: TI-2026-0049
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0049 (2 indicators: 177.22.119.68:9001, 207.211.189.214:443). malware_family_overlap: correlated malware family win.danabot (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0050 - Indicator corroborated by multiple independent sources: TI-2026-0050
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0050 (3 indicators: chilloutvrmod.org, chilloutvrmodded.net, https://kittiesmc.com/ws). malware_family_overlap: correlated malware family unknown_stealer (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0051 - Indicator corroborated by multiple independent sources: TI-2026-0051
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0051 (2 indicators: https://89.46.235.116:80/, https://89.46.235.116:9443/). malware_family_overlap: correlated malware family win.metaencryptor (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0052 - Indicator corroborated by multiple independent sources: TI-2026-0052
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0052 (3 indicators: 1ca26b57598f79603d7e4da730c98965, 6161c1e746b8e29297917c72f93652a137691a3b9d4c6d6fbce38f80f7732d34, badbf7f86834fca16610045cb7c13159932bcd4b). malware_family_overlap: correlated malware family win.dboxagent (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0053 - Indicator corroborated by multiple independent sources: TI-2026-0053
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0053 (3 indicators: 833cdd365d2dd29832a711dc2da5a584, c13cea04f598e2b0c248d603a6e31bd13aabb64d8149c1b6a77b64e0b983a86f, f495880eb6ee7bb930a9957f092f395695cf89a4). malware_family_overlap: correlated malware family win.logedrut (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0054 - Indicator corroborated by multiple independent sources: TI-2026-0054
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0054 (3 indicators: 94ffe61fb9619a00d8c1066dc8728df2af733f0b9ca8783a93ecbe1e52e59562, dd63f54137cd8c2ba7bb43cb6a45db5b2238698c, e629a420112f2bcb593f5467a362a91a). malware_family_overlap: correlated malware family win.shimrat (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0055 - Indicator corroborated by multiple independent sources: TI-2026-0055
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0055 (3 indicators: 31edc1eef538fdb429601d26422834b3, 919f9a20b675968f038bf43c009611a697f11119e037ad577bca4bb2fe746f1c, 974abebcdf2bfcb5440d9590234b4814318698eb). malware_family_overlap: correlated malware family win.nanocore (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0056 - Indicator corroborated by multiple independent sources: TI-2026-0056
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0056 (3 indicators: 55d635733571cf404f3af64646dc97e9, 668dd8566eacd7b89dab013b36cccf0f94be8c4a, ce3d16f1bcb319135a99b10d4daa2a680c2cadadb8d8082b39d3696b7016e096). malware_family_overlap: correlated malware family win.gcleaner (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0057 - Indicator corroborated by multiple independent sources: TI-2026-0057
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0057 (4 indicators: 0eedde175f5d230ee129dc4add72be8a32e7c05a, 12651a9b77448b0bc439f301d24fc52cd331705f10cb58103f48a1d8b02caea2, 221e2c855e78d5cc7fb84738effb88bb11a47be6ce10530c909534e15f47e0b4, c705fea2fd2e6c119c1138f1b74cd798). malware_family_overlap: correlated malware family win.svcstealer (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0058 - Indicator corroborated by multiple independent sources: TI-2026-0058
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0058 (3 indicators: 0c7dd3b979c3fdeba56c6ae312345548, 2cbd1f5b16cc5e17be51a801de7fed705a2336a5, fb48f55e9e2b1ef2d904b0f06547ce698bcb151b43dd032fc7257a7c0f940bd4). malware_family_overlap: correlated malware family jar.crossrat (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0059 - Indicator corroborated by multiple independent sources: TI-2026-0059
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0059 (3 indicators: 541677c2ce44edbb6241907c36463e6ded77a9d7cdb48ceb4113f1111ad2f9e8, aafeaf4892cd200b9dd7b9e03259b49204d2973b, f5ec29d01c9adb0ecabb2da6bc8fb81a). malware_family_overlap: correlated malware family win.wannacryptor (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0060 - Indicator corroborated by multiple independent sources: TI-2026-0060
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0060 (2 indicators: blancharl.icu, courtoos.icu). malware_family_overlap: correlated malware family js.kongtuke (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0061 - Indicator corroborated by multiple independent sources: TI-2026-0061
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0061 (4 indicators: 46.246.12.23:32722, 46.246.12.23:7045, brain.dynip.se, jamesmore02.work.gd). malware_family_overlap: correlated malware family win.houdini (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0062 - Indicator corroborated by multiple independent sources: TI-2026-0062
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0062 (3 indicators: 94.154.43.83:8443, https://ns.devmicro7.workers.dev/zips/f2d0984b93e808eb.zip, sk.bumblemovies.com). malware_family_overlap: correlated malware family jar.microstealer (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.

## CTI-004:TI-2026-0063 - Indicator corroborated by multiple independent sources: TI-2026-0063
**Severity:** low | **Score:** 5.25 | **State:** UNCHANGED
**What changed:** No material change since the previous briefing.
**Why reported today:** state changed to UNCHANGED
**Independent sources:** 1
**Evidence:**
- [threat-ingest-cluster, reliability D, confidence 0.15, supports] Threat-Ingest infrastructure cluster TI-2026-0063 (2 indicators: 2a018987d8fb348a3e5e05595afbcd4bfa5631b6e0df83219390cca2e5ea758a, https://theoremaoliveoil.com/wp-content/uploads/2019/04/pieletjf.exe). malware_family_overlap: correlated malware family win.koiloader (first seen 2026-09-24, last seen 2026-09-25; source date 2026-09-24; collected 2026-09-24T22:39:09+00:00)
**Score components:** {'base': 35.0, 'amplifier_factor': 1.0, 'source_confidence': 1.0, 'signal_confidence': 0.15, 'asset_multiplier': 1.0}
**Owner:** Unassigned (synthetic) | **Deadline:** 2026-10-24 | **Recommended action:** Add to the active watchlist and block at available control points.
**Verification method:** Confirm the indicator no longer appears in egress or DNS telemetry after blocking.
