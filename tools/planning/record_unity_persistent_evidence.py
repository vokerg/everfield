#!/usr/bin/env python3
"""Project only sanitized evidence from the persistent Unity evaluator."""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from typing import Any

from tools.planning.record_provider_effective_access import native_projection, process_fields

SOURCE_SCHEMA = "W2-ENG-UNITY-PERSISTENT-ACCESS-v1"
EVIDENCE_SCHEMA = "W2-ENG-UNITY-PERSISTENT-ACCESS-EVIDENCE-v1"
MISSION_ID = "W2-ENG-UNITY-PERSISTENT-RUNNER-01"
WORKFLOW_NAME = "Everfield persistent Unity exact-main evaluator"
WORKFLOW_PATH = ".github/workflows/unity-persistent-evaluator.yml"
REPOSITORY = "vokerg/everfield"
RUNNER_NAME = "everfield-unity-mac"
ALLOWED_EVENTS = {"push", "workflow_dispatch"}
STATES = {
    "VALIDATED_DEVELOPMENT_ACCESS",
    "TRANSIENT_VALIDATION_FAILURE",
    "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SENSITIVE_VALUE_FRAGMENTS = (
    "unity_service_account_secret",
    "unreal_github_token",
    "password=",
    "token=",
    "authorization:",
    "cookie=",
    "bearer ",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_runner(source: Any, *, head_sha: str, source_event: str) -> dict[str, Any]:
    require(isinstance(source, dict), "runner identity must be an object")
    required = {
        "repository", "event", "ref", "sha", "run_id", "run_attempt",
        "runner_name", "runner_os", "runner_arch", "checks", "trusted",
    }
    require(set(source) == required, "unexpected runner identity fields")
    require(source["repository"] == REPOSITORY, "runner repository mismatch")
    require(source["event"] in ALLOWED_EVENTS, "runner event is not allowed")
    require(source["event"] == source_event, "runner/source event mismatch")
    require(source["ref"] == "refs/heads/main", "runner ref is not main")
    require(source["sha"] == head_sha and SHA_RE.fullmatch(head_sha), "runner SHA mismatch")
    require(source["runner_name"] == RUNNER_NAME, "runner name mismatch")
    require(source["runner_os"] == "macOS", "runner OS mismatch")
    require(source["runner_arch"] == "ARM64", "runner architecture mismatch")
    require(source["trusted"] is True, "runner identity is not trusted")
    require(isinstance(source["checks"], dict), "runner checks are not an object")
    require(set(source["checks"]) == {
        "repository_matches", "event_allowed", "ref_is_main", "sha_present",
        "runner_name_matches", "runner_os_matches", "runner_arch_matches",
    }, "unexpected runner checks")
    require(all(value is True for value in source["checks"].values()), "runner checks did not pass")
    return {
        key: source[key]
        for key in (
            "repository", "event", "ref", "sha", "run_id", "run_attempt",
            "runner_name", "runner_os", "runner_arch", "trusted", "checks",
        )
    }


def project_unity(source: Any) -> dict[str, Any]:
    require(isinstance(source, dict), "Unity result must be an object")
    require(source.get("provider") == "Unity", "unexpected Unity provider")
    require(source.get("baseline") == "6000.5.6f1", "Unity baseline drift")
    require(source.get("state") in STATES, "unexpected Unity state")
    for key in ("commercial_authority", "production_authority", "legal_clearance", "release_authority"):
        require(source.get(key) is False, f"Unity authority boundary violated: {key}")
    require(source.get("credential_values_read") is False, "persistent evidence consumed a credential")
    processes = source.get("processes")
    require(isinstance(processes, dict) and set(processes) == {"auth_status", "license_status"}, "invalid Unity process envelope")
    projection = {
        "provider": "Unity",
        "baseline": source["baseline"],
        "state": source["state"],
        "authentication_validated": bool(source.get("authentication_validated")),
        "license_validated": bool(source.get("license_validated")),
        "editor_installed": bool(source.get("editor_installed")),
        "editor_executed": bool(source.get("editor_executed")),
        "native_s3": native_projection(source.get("native_s3")),
        "processes": {
            "auth_status": process_fields(processes["auth_status"]),
            "license_status": process_fields(processes["license_status"]),
        },
        "blocker": source.get("blocker"),
        "credential_values_read": False,
        "commercial_authority": False,
        "production_authority": False,
        "legal_clearance": False,
        "release_authority": False,
    }
    if projection["state"] == "VALIDATED_DEVELOPMENT_ACCESS":
        require(projection["authentication_validated"], "validated Unity result lacks authentication")
        require(projection["license_validated"], "validated Unity result lacks license validation")
        require(projection["editor_installed"], "validated Unity result lacks editor installation")
        require(projection["editor_executed"], "validated Unity result lacks editor execution")
        require(projection["native_s3"] is not None and projection["native_s3"]["pass"], "validated Unity result lacks native S3 PASS")
    return projection


def record(
    source: dict[str, Any],
    *,
    run_id: str,
    run_attempt: str,
    head_sha: str,
    branch: str,
    source_workflow_id: str,
    source_workflow_name: str,
    source_workflow_path: str,
    source_event: str,
    source_conclusion: str,
    projection_code_sha: str,
    publication_base_main_sha: str,
) -> dict[str, Any]:
    require(source.get("schema") == SOURCE_SCHEMA, "unexpected persistent Unity source schema")
    require(source.get("mission_id") == MISSION_ID, "unexpected persistent Unity mission")
    require(source.get("execution_context") == "PERSISTENT_SELF_HOSTED_WORKSTATION", "execution context is not persistent")
    require(source.get("secret_values_in_evidence") is False, "source declares secret values")
    require(source.get("secret_hashes_in_evidence") is False, "source declares secret hashes")
    require(source.get("historical_not_run_cells_preserved") == 50, "historical cells were not preserved")
    require(source.get("historical_not_run_cells_mutated") is False, "historical cells were mutated")
    require(source.get("engine_selected") is False, "engine selection authority was asserted")
    require(isinstance(source.get("provider_unlock"), bool), "persistent Unity provider unlock is not boolean")
    require(source_workflow_name == WORKFLOW_NAME, "unexpected source workflow name")
    require(source_workflow_path == WORKFLOW_PATH, "unexpected source workflow path")
    require(source_event in ALLOWED_EVENTS, "unexpected source event")
    require(source_conclusion == "success", "source workflow was not successful")
    require(branch == "main", "source branch is not main")
    require(SHA_RE.fullmatch(head_sha), "invalid source head SHA")
    require(SHA_RE.fullmatch(projection_code_sha) and projection_code_sha == head_sha, "projection identity mismatch")
    require(SHA_RE.fullmatch(publication_base_main_sha), "invalid publication base SHA")
    serialized = json.dumps(source, sort_keys=True).lower()
    for fragment in SENSITIVE_VALUE_FRAGMENTS:
        require(fragment not in serialized, f"sensitive value fragment found: {fragment}")
    runner = validate_runner(source.get("runner"), head_sha=head_sha, source_event=source_event)
    unity = project_unity(source.get("unity"))
    require(
        source["provider_unlock"] == (unity["state"] == "VALIDATED_DEVELOPMENT_ACCESS"),
        "persistent Unity provider unlock disagrees with provider state",
    )
    return {
        "schema": EVIDENCE_SCHEMA,
        "source_schema": SOURCE_SCHEMA,
        "mission_id": MISSION_ID,
        "execution_context": "PERSISTENT_SELF_HOSTED_WORKSTATION",
        "run": {
            "run_id": str(run_id),
            "run_attempt": str(run_attempt),
            "head_sha": head_sha,
            "branch": branch,
            "event": source_event,
            "conclusion": source_conclusion,
            "workflow": {
                "id": str(source_workflow_id),
                "name": source_workflow_name,
                "path": source_workflow_path,
            },
            "projection_code_sha": projection_code_sha,
            "publication_base_main_sha": publication_base_main_sha,
        },
        "runner": runner,
        "unity": unity,
        "authority": {
            "provider_pass": False,
            "engine_selected": False,
            "implementation_readiness": False,
            "commercial_authority": False,
            "production_authority": False,
            "legal_clearance": False,
            "release_authority": False,
            "integration_authority": False,
            "decision_authority": False,
            "canonicality": "NOT_CANONICAL",
        },
        "publication": {
            "mode": "PERSISTENT_UNITY_EVIDENCE_BRANCH_DRAFT_PR",
            "direct_main_push": False,
            "integration_authority": False,
            "squash_only_required": True,
            "fresh_expected_head_check_required": True,
        },
        "secret_values_in_evidence": False,
        "secret_hashes_in_evidence": False,
        "workflow_success_is_not_authority": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--run-attempt", required=True)
    parser.add_argument("--head-sha", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--source-workflow-id", required=True)
    parser.add_argument("--source-workflow-name", required=True)
    parser.add_argument("--source-workflow-path", required=True)
    parser.add_argument("--source-event", required=True)
    parser.add_argument("--source-conclusion", required=True)
    parser.add_argument("--projection-code-sha", required=True)
    parser.add_argument("--publication-base-main-sha", required=True)
    args = parser.parse_args()
    source = json.loads(pathlib.Path(args.input).read_text(encoding="utf-8"))
    evidence = record(
        source,
        run_id=args.run_id,
        run_attempt=args.run_attempt,
        head_sha=args.head_sha,
        branch=args.branch,
        source_workflow_id=args.source_workflow_id,
        source_workflow_name=args.source_workflow_name,
        source_workflow_path=args.source_workflow_path,
        source_event=args.source_event,
        source_conclusion=args.source_conclusion,
        projection_code_sha=args.projection_code_sha,
        publication_base_main_sha=args.publication_base_main_sha,
    )
    pathlib.Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.output).write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "schema": EVIDENCE_SCHEMA,
        "mission_id": MISSION_ID,
        "execution_context": evidence["execution_context"],
        "run_id": args.run_id,
        "head_sha": args.head_sha,
        "unity_state": evidence["unity"]["state"],
        "native_s3_pass": evidence["unity"]["native_s3"]["pass"],
        "secret_values_in_evidence": False,
        "secret_hashes_in_evidence": False,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
