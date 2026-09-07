# Analyst Briefing - day-03

## CTI-002:UNC-4471 - Tracked threat actor campaign confirmed active in internal telemetry: UNC-4471
**Severity:** high | **Score:** 55.99 | **State:** unchanged
**What changed:** No material change since the previous briefing.
**Evidence:**
- [commercial_feed] Campaign infrastructure expanded.
- [edr_telemetry] Actor's known C2 domain observed in outbound proxy logs.
**Score components:** {'base': 62.0, 'amplifier_factor': 1.0, 'source_confidence': 1.05, 'signal_confidence': 0.86}
**Recommended action:** Escalate to incident response; hunt for the actor's known TTPs across the estate.

## CTI-001:CVE-2026-41821 - Exploited vulnerability reachable in the environment and targeting our sector: CVE-2026-41821
**Severity:** critical | **Score:** 71.35 | **State:** resolved
**What changed:** No longer observed; treat as resolved pending confirmation.
**Evidence:**
- [asset_inventory] Affected service is internet-facing.
- [sca_scanner] Still KEV-listed; patch not yet deployed.
- [vendor_advisory] Targeting confirmed continues.
**Score components:** {'base': 70.0, 'amplifier_factor': 1.0, 'source_confidence': 1.1, 'signal_confidence': 0.927}
**Recommended action:** Patch or virtually patch within 48 hours; confirm compensating controls until then.
