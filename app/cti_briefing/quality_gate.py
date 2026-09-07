"""Pre-publish quality gate.

A report is not written to the "latest" files unless every hard check passes.
Soft checks are reported but do not block publication.
"""

from __future__ import annotations

from dataclasses import dataclass

from .schema import LIVE_BANNER, SYNTHETIC_BANNER, Item, looks_unsafe


@dataclass
class GateResult:
    name: str
    passed: bool
    hard: bool
    detail: str


def run_quality_gate(
    items: list[Item], rendered: dict[str, str], previous_rendered: dict[str, str] | None,
    live: bool = False,
) -> list[GateResult]:
    results: list[GateResult] = []
    expected_banner = LIVE_BANNER if live else SYNTHETIC_BANNER

    results.append(GateResult(
        "data_mode_labeled", all(expected_banner in text for text in rendered.values()), True,
        "Every report must carry the live-data banner." if live else "Every report must carry the synthetic-data banner.",
    ))

    if live:
        results.append(GateResult(
            "unsafe_indicator_check", True, False,
            "Skipped in live mode: live findings intentionally reference real public vulnerability data.",
        ))
    else:
        unsafe_findings = []
        for item in items:
            for record in item.evidence:
                reason = looks_unsafe(record.statement)
                if reason:
                    unsafe_findings.append(f"{item.item_id}: {reason}")
        results.append(GateResult(
            "no_unsafe_live_indicators", not unsafe_findings, True,
            "; ".join(unsafe_findings) if unsafe_findings else "All indicators are within reserved/example ranges.",
        ))

    claims_ok = all(item.components for item in items)
    results.append(GateResult(
        "confidence_scores_explainable", claims_ok, True,
        "Every item must expose its scoring components." if not claims_ok else "All items expose scoring components.",
    ))

    unproven = [item.item_id for item in items if item.state in {"MITIGATED", "RESOLVED"} and not item.remediation]
    results.append(GateResult(
        "resolved_findings_have_remediation_proof", not unproven, True,
        "; ".join(unproven) if unproven else "Every mitigated/resolved item carries remediation evidence.",
    ))

    identical = previous_rendered is not None and rendered.get("analyst") == previous_rendered.get("analyst")
    results.append(GateResult(
        "report_differs_from_previous", not identical, False,
        "Analyst report is byte-identical to the previous briefing." if identical else "Report content changed from the previous briefing.",
    ))

    return results


def gate_passed(results: list[GateResult]) -> bool:
    return all(result.passed for result in results if result.hard)


def render_gate_summary(results: list[GateResult]) -> str:
    lines = ["# Quality Gate", ""]
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        kind = "hard" if result.hard else "soft"
        lines.append(f"- [{status}] ({kind}) {result.name}: {result.detail}")
    return "\n".join(lines)
