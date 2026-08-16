#!/usr/bin/env python3
"""Validate and persist only a fixed, non-secret provider-evaluation projection."""
from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

SOURCE_SCHEMA = "W2-ENG-PROVIDER-EFFECTIVE-ACCESS-v1"
EVIDENCE_SCHEMA = "W2-ENG-PROVIDER-EFFECTIVE-ACCESS-EVIDENCE-v1"
FORBIDDEN_TERMS = ("password", "token", "secret", "authorization", "cookie", "credential")
PROVIDER_NAMES = ("Unity", "Unreal Engine")
STATES = {
    "NOT_CONFIGURED",
    "CONFIGURED_UNVALIDATED",
    "VALIDATED_DEVELOPMENT_ACCESS",
    "TRANSIENT_VALIDATION_FAILURE",
    "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
}


def reject_sensitive_keys(value: Any, path: str = "root") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            lowered = str(key).lower()
            if any(term in lowered for term in FORBIDDEN_TERMS):
                raise ValueError(f"sensitive key at {path}.{key}")
            reject_sensitive_keys(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_sensitive_keys(child, f"{path}[{index}]")


def process_fields(process: Any) -> dict[str, Any] | None:
    if not isinstance(process, dict):
        return None
    required = {"exit", "timed_out", "seconds"}
    if set(process) != required:
        raise ValueError("unexpected process fields")
    if not isinstance(process["timed_out"], bool):
        raise ValueError("invalid process timeout field")
    return {key: process[key] for key in ("exit", "timed_out", "seconds")}


def native_projection(native: Any) -> dict[str, Any] | None:
    if native is None:
        return None
    if not isinstance(native, dict) or set(native) != {"scenario_id", "harness_id", "attempts", "native_execution", "pass"}:
        raise ValueError("unexpected native S3 fields")
    if native["scenario_id"] != "S3" or not isinstance(native["attempts"], list):
        raise ValueError("invalid native S3 envelope")
    attempts = []
    for attempt in native["attempts"]:
        if not isinstance(attempt, dict):
            raise ValueError("invalid native S3 attempt")
        allowed = {
            "attempt_id", "scenario_id", "kind", "normal_index", "injection_id",
            "expected_checksum", "observed_checksum", "result", "failure_class",
            "native_command", "process",
        }
        if set(attempt) != allowed:
            raise ValueError("unexpected native S3 attempt fields")
        attempts.append({
            "attempt_id": attempt["attempt_id"],
            "scenario_id": attempt["scenario_id"],
            "kind": attempt["kind"],
            "normal_index": attempt["normal_index"],
            "injection_id": attempt["injection_id"],
            "expected_checksum": attempt["expected_checksum"],
            "observed_checksum": attempt["observed_checksum"],
            "result": attempt["result"],
            "failure_class": attempt["failure_class"],
            "native_command": attempt["native_command"],
            "process": process_fields(attempt["process"]),
        })
    return {
        "scenario_id": native["scenario_id"],
        "harness_id": native["harness_id"],
        "attempts": attempts,
        "native_execution": bool(native["native_execution"]),
        "pass": bool(native["pass"]),
    }


def provider_projection(provider: Any) -> dict[str, Any]:
    if not isinstance(provider, dict):
        raise ValueError("provider must be an object")
    if provider.get("provider") not in PROVIDER_NAMES:
        raise ValueError("unexpected provider name")
    if provider.get("state") not in STATES:
        raise ValueError("unexpected provider state")
    expected_baseline = "6000.5.6f1" if provider["provider"] == "Unity" else "5.8"
    if provider.get("baseline") != expected_baseline:
        raise ValueError("provider baseline drift")
    for key in ("commercial_authority", "production_authority", "legal_clearance", "release_authority"):
        if provider.get(key, False) is not False:
            raise ValueError(f"authority boundary violated: {key}")
    projection = {
        "provider": provider["provider"],
        "baseline": provider.get("baseline"),
        "state": provider["state"],
        "authentication_validated": bool(provider.get("authentication_validated", False)),
        "license_validated": bool(provider.get("license_validated", False)),
        "registry_authorization_validated": bool(provider.get("registry_authorization_validated", False)),
        "editor_installed": bool(provider.get("editor_installed", False)),
        "editor_executed": bool(provider.get("editor_executed", False)),
        "native_s3": native_projection(provider.get("native_s3")),
        "commercial_authority": bool(provider.get("commercial_authority", False)),
        "production_authority": bool(provider.get("production_authority", False)),
        "legal_clearance": bool(provider.get("legal_clearance", False)),
        "release_authority": bool(provider.get("release_authority", False)),
        "blocker": provider.get("blocker"),
    }
    for key in ("authentication_process", "authentication_status_process", "license_process", "container_pull_process"):
        if key in provider:
            projection[key] = process_fields(provider[key])
    if provider.get("container_identity") is not None:
        identity = provider["container_identity"]
        if not isinstance(identity, str) or not identity.startswith("sha256:"):
            raise ValueError("invalid container identity")
        projection["container_identity"] = identity
    return projection


def record(source: dict[str, Any], *, run_id: str, run_attempt: str, head_sha: str, branch: str) -> dict[str, Any]:
    if source.get("schema") != SOURCE_SCHEMA or source.get("mission_id") != "W2-ENG-PROVIDER-EFFECTIVE-01":
        raise ValueError("unexpected source contract")
    if source.get("secret_values_in_evidence") is not False or source.get("secret_hashes_in_evidence") is not False:
        raise ValueError("source evidence declares secret material")
    providers = source.get("providers")
    if not isinstance(providers, dict) or set(providers) != set(PROVIDER_NAMES):
        raise ValueError("provider set is not independent and complete")
    frontier = source.get("frontier")
    if not isinstance(frontier, dict):
        raise ValueError("missing frontier")
    required_frontier = {
        "provider_unlocks", "unity_empirical_cells_eligible", "unreal_empirical_cells_eligible",
        "combined_provider_predicate", "combined_predicate_used_for_individual_unlock",
        "commercial_license_authority", "production_authority", "legal_clearance",
        "release_authority", "engine_selected", "historical_not_run_cells_preserved",
        "historical_not_run_cells_mutated",
    }
    if set(frontier) != required_frontier:
        raise ValueError("unexpected frontier fields")
    if frontier["combined_predicate_used_for_individual_unlock"] is not False:
        raise ValueError("combined predicate used for individual unlock")
    if frontier["historical_not_run_cells_preserved"] != 50 or frontier["historical_not_run_cells_mutated"] is not False:
        raise ValueError("historical issue 82 evidence was not preserved")
    result = {
        "schema": EVIDENCE_SCHEMA,
        "source_schema": source["schema"],
        "mission_id": source["mission_id"],
        "run": {"run_id": str(run_id), "run_attempt": str(run_attempt), "head_sha": head_sha, "branch": branch},
        "providers": {name: provider_projection(providers[name]) for name in PROVIDER_NAMES},
        "frontier": {
            "provider_unlocks": frontier["provider_unlocks"],
            "unity_empirical_cells_eligible": frontier["unity_empirical_cells_eligible"],
            "unreal_empirical_cells_eligible": frontier["unreal_empirical_cells_eligible"],
            "combined_provider_predicate": frontier["combined_provider_predicate"],
            "combined_predicate_used_for_individual_unlock": False,
            "commercial_license_authority": False,
            "production_authority": False,
            "legal_clearance": False,
            "release_authority": False,
            "engine_selected": False,
            "historical_not_run_cells_preserved": 50,
            "historical_not_run_cells_mutated": False,
        },
        "secret_values_in_evidence": False,
        "secret_hashes_in_evidence": False,
        "workflow_success_is_not_authority": True,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--run-attempt", required=True)
    parser.add_argument("--head-sha", required=True)
    parser.add_argument("--branch", required=True)
    args = parser.parse_args()
    source = json.loads(pathlib.Path(args.input).read_text())
    evidence = record(source, run_id=args.run_id, run_attempt=args.run_attempt, head_sha=args.head_sha, branch=args.branch)
    pathlib.Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.output).write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"schema": evidence["schema"], "providers": {name: data["state"] for name, data in evidence["providers"].items()}}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
