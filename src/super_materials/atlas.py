"""State Atlas validation and deterministic campaign generation."""
from __future__ import annotations

from collections import Counter
from itertools import product
from typing import Any

ALLOWED_SOURCE_CLASSES = {
    "peer_reviewed_experiment",
    "peer_reviewed_theory",
    "preprint",
    "secondary",
}
ALLOWED_EVIDENCE_LEVELS = {
    "anomaly",
    "transport",
    "phase_linked",
    "bulk_consistent",
    "mechanism_resolved",
    "independently_replicated",
}


def validate_atlas_record(record: dict[str, Any]) -> list[str]:
    """Return human-readable validation errors without silently filling fields."""
    errors: list[str] = []
    required = ("state_id", "role", "material", "source", "preparation", "retained_state", "retention_observations", "limitations")
    for key in required:
        if key not in record:
            errors.append(f"missing {key}")
    if errors:
        return errors

    if not isinstance(record["state_id"], str) or not record["state_id"].strip():
        errors.append("state_id must be a non-empty string")

    material = record["material"]
    if not isinstance(material, dict) or not material.get("formula"):
        errors.append("material.formula is required")

    source = record["source"]
    if not isinstance(source, dict):
        errors.append("source must be an object")
    else:
        if not source.get("doi"):
            errors.append("source.doi is required")
        if source.get("source_class") not in ALLOWED_SOURCE_CLASSES:
            errors.append("source.source_class is invalid")

    preparation = record["preparation"]
    if not isinstance(preparation, dict):
        errors.append("preparation must be an object")
    else:
        p = preparation.get("formation_or_quench_pressure_gpa")
        if p is not None and (not isinstance(p, (int, float)) or p < 0):
            errors.append("preparation pressure must be nonnegative or null")

    retained = record["retained_state"]
    if not isinstance(retained, dict):
        errors.append("retained_state must be an object")
    else:
        p = retained.get("pressure_gpa")
        if p is not None and (not isinstance(p, (int, float)) or p < 0):
            errors.append("retained_state.pressure_gpa must be nonnegative or null")
        evidence = retained.get("evidence_level")
        if evidence not in ALLOWED_EVIDENCE_LEVELS:
            errors.append("retained_state.evidence_level is invalid")

    observations = record["retention_observations"]
    if not isinstance(observations, list):
        errors.append("retention_observations must be a list")
    else:
        for i, obs in enumerate(observations):
            if not isinstance(obs, dict):
                errors.append(f"retention_observations[{i}] must be an object")
                continue
            t = obs.get("temperature_k")
            d = obs.get("duration_s")
            if t is not None and (not isinstance(t, (int, float)) or t <= 0):
                errors.append(f"retention_observations[{i}].temperature_k must be positive or null")
            if d is not None and (not isinstance(d, (int, float)) or d < 0):
                errors.append(f"retention_observations[{i}].duration_s must be nonnegative or null")
            if not obs.get("status"):
                errors.append(f"retention_observations[{i}].status is required")

    if not isinstance(record["limitations"], list) or not record["limitations"]:
        errors.append("limitations must be a non-empty list")
    return errors


def validate_atlas_document(document: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    records = document.get("records")
    if not isinstance(records, list) or not records:
        return ["records must be a non-empty list"]

    seen: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"records[{index}] must be an object")
            continue
        for error in validate_atlas_record(record):
            errors.append(f"records[{index}]: {error}")
        state_id = record.get("state_id")
        if state_id in seen:
            errors.append(f"records[{index}]: duplicate state_id {state_id}")
        if isinstance(state_id, str):
            seen.add(state_id)
    return errors


def atlas_summary(document: dict[str, Any]) -> dict[str, Any]:
    """Compact counts useful for dashboards and CI sanity checks."""
    records = document.get("records", [])
    roles = Counter(r.get("role", "unknown") for r in records)
    statuses = Counter(r.get("retained_state", {}).get("status", "unknown") for r in records)
    sc = Counter(r.get("retained_state", {}).get("superconductivity_observed") for r in records)
    return {
        "records": len(records),
        "roles": dict(sorted(roles.items())),
        "retained_statuses": dict(sorted(statuses.items())),
        "superconductivity_true": sc.get(True, 0),
        "superconductivity_false": sc.get(False, 0),
        "superconductivity_unknown": sc.get(None, 0),
    }


def generate_q_mrh6_campaign() -> list[dict[str, Any]]:
    """Generate the 12-run first-wave factorial campaign.

    Temperatures/rates are deliberately left as regimes rather than invented
    instrument-specific setpoints. Every run uses the same pressure ladder and
    mandatory same-state measurements.
    """
    protocols = (
        ("cold_fast", "cryogenic", "minimal dwell; fastest safe decompression"),
        ("cold_staged", "cryogenic", "registered dwell at each pressure stop"),
        ("warm_staged", "warmer_control", "registered dwell at each pressure stop"),
    )
    isotopes = ("H", "D")
    precursors = ("crystalline", "disordered")
    ladder = (30, 20, 15, 10, 5, 2, 1, 0)

    runs: list[dict[str, Any]] = []
    for index, ((protocol, temperature_regime, dwell), isotope, precursor) in enumerate(
        product(protocols, isotopes, precursors), start=1
    ):
        runs.append({
            "run_id": f"QMRH6-{index:02d}",
            "protocol": protocol,
            "temperature_regime": temperature_regime,
            "dwell_strategy": dwell,
            "isotope": isotope,
            "precursor_state": precursor,
            "pressure_ladder_gpa": ladder,
            "formation_anchor_gpa": 30,
            "mandatory_measurements": (
                "phase_fingerprint",
                "four_probe_transport",
                "elapsed_time",
                "pressure",
                "temperature",
            ),
            "promotion_signal": "verified H6 fingerprint retained to a lower pressure while the same state preserves a superconducting signature",
            "kill_signal": "H6 fingerprint disappears before the transport anomaly or no preparation-path variable reproducibly shifts the retention floor",
        })
    return runs
