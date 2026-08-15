#!/usr/bin/env python3
"""Fail-closed policy validator for W2-CI-REM-01 capability evidence."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import pathlib
from typing import Any

CAPABILITY_SCHEMA = "W2-CI-ENGINE-TOOLCHAIN-CAPABILITY-v2"
ARTIFACT_LOCK_SCHEMA = "W2-CI-ENGINE-ARTIFACT-LOCK-v1"
PUBLIC = ("Bevy", "Defold", "Godot")
AUTHORITY_SCOPED = ("Unity", "Unreal Engine")
CAPABLE = {"CAPABLE", "CAPABLE_WITH_PRESEED"}
AUTHORITY_ALLOWED = CAPABLE | {"BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY"}


def sha256_file(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_sha256(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value.lower())


def validate(cap: dict[str, Any], artifact_lock: dict[str, Any], bevy_lock_sha: str) -> list[str]:
    errors: list[str] = []
    if cap.get("schema") != CAPABILITY_SCHEMA:
        errors.append("capability_schema_mismatch")
    if artifact_lock.get("schema") != ARTIFACT_LOCK_SCHEMA:
        errors.append("artifact_lock_schema_mismatch")
    if cap.get("historical_not_run_cells_preserved") != 50 or cap.get("prior_not_run_promoted") is not False:
        errors.append("historical_not_run_boundary_broken")

    candidates = cap.get("candidates")
    if not isinstance(candidates, dict):
        return errors + ["candidates_missing"]

    summary = cap.get("status_summary")
    observed_summary = {name: candidates.get(name, {}).get("status") for name in (*PUBLIC, *AUTHORITY_SCOPED)}
    if summary != observed_summary:
        errors.append("status_summary_mismatch")

    for name in PUBLIC:
        status = candidates.get(name, {}).get("status")
        if status not in CAPABLE:
            errors.append(f"{name}:unexpected_public_status:{status}")

    for name in AUTHORITY_SCOPED:
        item = candidates.get(name, {})
        status = item.get("status")
        if status not in AUTHORITY_ALLOWED:
            errors.append(f"{name}:unexpected_authority_scoped_status:{status}")
        if item.get("credential_values_read") is not False:
            errors.append(f"{name}:credential_boundary_broken")

    bevy = candidates.get("Bevy", {})
    lock_sha = bevy.get("retained_lock_sha256")
    if not is_sha256(lock_sha) or lock_sha != bevy_lock_sha:
        errors.append("Bevy:retained_lock_identity_mismatch")
    if bevy.get("lock_replay_bound") is not True:
        errors.append("Bevy:locked_replay_not_bound")
    lock_record = artifact_lock.get("bevy_lock", {})
    if lock_record.get("sha256") != bevy_lock_sha:
        errors.append("Bevy:artifact_lock_record_mismatch")

    entries = artifact_lock.get("entries", {})
    for name, key in (
        ("Defold", "defold_bob_1.13.0"),
        ("Godot", "godot_4.7.1_linux_x86_64_zip"),
    ):
        item = candidates.get(name, {})
        ident = item.get("artifact_identity", {})
        expected = ident.get("expected_sha256")
        observed = ident.get("observed_sha256")
        if not (is_sha256(expected) and is_sha256(observed) and expected == observed and ident.get("verified") is True):
            errors.append(f"{name}:artifact_identity_not_verified")
        entry = entries.get(key, {})
        if entry.get("sha256") != expected:
            errors.append(f"{name}:artifact_lock_entry_mismatch")

    full_expected = all(observed_summary.get(name) in CAPABLE for name in (*PUBLIC, *AUTHORITY_SCOPED))
    if cap.get("full_five_candidate_harness_capable") is not full_expected:
        errors.append("full_five_summary_mismatch")
    external_expected = [name for name in (*PUBLIC, *AUTHORITY_SCOPED) if observed_summary.get(name) == "BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY"]
    if cap.get("residual_external_authority_candidates") != external_expected:
        errors.append("external_authority_summary_mismatch")
    return errors


def self_test() -> dict[str, Any]:
    lock_bytes = b"synthetic-lock\n"
    lock_sha = hashlib.sha256(lock_bytes).hexdigest()
    d = "a" * 64
    artifact_lock = {
        "schema": ARTIFACT_LOCK_SCHEMA,
        "mission_id": "W2-CI-REM-01",
        "bevy_lock": {"sha256": lock_sha},
        "entries": {
            "defold_bob_1.13.0": {"sha256": d},
            "godot_4.7.1_linux_x86_64_zip": {"sha256": d},
        },
    }
    cap = {
        "schema": CAPABILITY_SCHEMA,
        "historical_not_run_cells_preserved": 50,
        "prior_not_run_promoted": False,
        "candidates": {
            "Bevy": {"status": "CAPABLE_WITH_PRESEED", "retained_lock_sha256": lock_sha, "lock_replay_bound": True},
            "Defold": {"status": "CAPABLE", "artifact_identity": {"expected_sha256": d, "observed_sha256": d, "verified": True}},
            "Godot": {"status": "CAPABLE", "artifact_identity": {"expected_sha256": d, "observed_sha256": d, "verified": True}},
            "Unity": {"status": "BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY", "credential_values_read": False},
            "Unreal Engine": {"status": "BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY", "credential_values_read": False},
        },
        "full_five_candidate_harness_capable": False,
        "residual_external_authority_candidates": ["Unity", "Unreal Engine"],
    }
    cap["status_summary"] = {k: v["status"] for k, v in cap["candidates"].items()}

    cases: dict[str, bool] = {}
    cases["baseline_allowed"] = validate(cap, artifact_lock, lock_sha) == []

    bad_public = copy.deepcopy(cap)
    bad_public["candidates"]["Defold"]["status"] = "FAILED"
    bad_public["status_summary"]["Defold"] = "FAILED"
    cases["public_failed_rejected"] = bool(validate(bad_public, artifact_lock, lock_sha))

    cases["bevy_lock_substitution_rejected"] = bool(validate(cap, artifact_lock, "b" * 64))

    bad_artifact = copy.deepcopy(cap)
    bad_artifact["candidates"]["Godot"]["artifact_identity"]["observed_sha256"] = "c" * 64
    cases["artifact_substitution_rejected"] = bool(validate(bad_artifact, artifact_lock, lock_sha))

    bad_auth = copy.deepcopy(cap)
    bad_auth["candidates"]["Unity"]["status"] = "FAILED"
    bad_auth["status_summary"]["Unity"] = "FAILED"
    cases["authority_unexpected_failed_rejected"] = bool(validate(bad_auth, artifact_lock, lock_sha))

    return {"schema": "W2-CI-CAPABILITY-POLICY-SELFTEST-v1", "cases": cases, "pass": all(cases.values())}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--capability-json")
    ap.add_argument("--artifact-lock")
    ap.add_argument("--bevy-lock")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        result = self_test()
        print(json.dumps(result, sort_keys=True))
        return 0 if result["pass"] else 2

    if not (args.capability_json and args.artifact_lock and args.bevy_lock):
        ap.error("--capability-json, --artifact-lock, and --bevy-lock are required unless --self-test is used")

    cap = json.loads(pathlib.Path(args.capability_json).read_text())
    artifact_lock = json.loads(pathlib.Path(args.artifact_lock).read_text())
    bevy_lock_sha = sha256_file(pathlib.Path(args.bevy_lock))
    errors = validate(cap, artifact_lock, bevy_lock_sha)
    print(json.dumps({"schema": "W2-CI-CAPABILITY-POLICY-v1", "pass": not errors, "errors": errors}, sort_keys=True))
    return 0 if not errors else 3


if __name__ == "__main__":
    raise SystemExit(main())
