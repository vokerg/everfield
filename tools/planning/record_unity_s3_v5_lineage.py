#!/usr/bin/env python3
# Validate and project one exact trusted-main Unity S3 v5 lineage artifact.
from __future__ import annotations

import argparse
import copy
import json
import pathlib
from typing import Any

from tools.planning.unity_s3_v5_lineage import (
    MISSION_ID,
    REPOSITORY,
    SCHEMA as SOURCE_SCHEMA,
    SHA_RE,
    sensitive_scan,
    synthetic_packet,
    validate_packet,
)

EVIDENCE_SCHEMA = "W2-ENG-UNITY-S3-V5-LINEAGE-EVIDENCE-v1"
WORKFLOW_NAME = "Everfield Unity S3 reviewed-v5 lineage evaluator"
WORKFLOW_PATH = ".github/workflows/unity-s3-v5-lineage-evaluator.yml"
ALLOWED_EVENT = "workflow_dispatch"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


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
    validate_packet(source)
    require(source.get("schema") == SOURCE_SCHEMA, "source schema mismatch")
    require(source.get("mission_id") == MISSION_ID, "source mission mismatch")
    require(str(run_id).isdigit() and str(run_attempt).isdigit(), "invalid upstream run identity")
    require(isinstance(head_sha, str) and SHA_RE.fullmatch(head_sha) is not None, "invalid source head")
    require(branch == "main", "source branch is not main")
    require(source_workflow_name == WORKFLOW_NAME, "source workflow name mismatch")
    require(source_workflow_path == WORKFLOW_PATH, "source workflow path mismatch")
    require(source_event == ALLOWED_EVENT, "source event mismatch")
    require(source_conclusion == "success", "source conclusion mismatch")
    require(projection_code_sha == head_sha, "projection code is not bound to source head")
    require(isinstance(publication_base_main_sha, str) and SHA_RE.fullmatch(publication_base_main_sha) is not None,
            "publication base main SHA invalid")
    source_run = source["run"]
    require(source_run["repository"] == REPOSITORY, "source repository mismatch")
    require(source_run["ref"] == "refs/heads/main", "source ref mismatch")
    require(source_run["event"] == source_event, "artifact event mismatch")
    require(source_run["head_sha"] == head_sha, "artifact head mismatch")
    require(source_run["run_id"] == str(run_id), "artifact run id mismatch")
    require(source_run["run_attempt"] == str(run_attempt), "artifact run attempt mismatch")
    evidence = {
        "schema": EVIDENCE_SCHEMA,
        "source_schema": SOURCE_SCHEMA,
        "mission_id": MISSION_ID,
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
        "reviewed_v5": copy.deepcopy(source["reviewed_v5"]),
        "contract": copy.deepcopy(source["contract"]),
        "editor": copy.deepcopy(source["editor"]),
        "source": copy.deepcopy(source["source"]),
        "adaptation_seed": copy.deepcopy(source["adaptation_seed"]),
        "candidate": copy.deepcopy(source["candidate"]),
        "attempts": copy.deepcopy(source["attempts"]),
        "run_registry_refs": list(source["run_registry_refs"]),
        "all_attempt_refs": list(source["all_attempt_refs"]),
        "source_registry": copy.deepcopy(source["source_registry"]),
        "native_s3_pass": source["native_s3_pass"],
        "historical_not_run_cells_preserved": source["historical_not_run_cells_preserved"],
        "historical_not_run_cells_mutated": source["historical_not_run_cells_mutated"],
        "authority": copy.deepcopy(source["authority"]),
        "publication": {
            "mode": "IMMUTABLE_UNITY_S3_V5_LINEAGE_EVIDENCE_BRANCH",
            "direct_main_push": False,
            "draft_pr_created_by_workflow": False,
            "separate_draft_pr_handoff_required": True,
            "integration_authority": False,
            "squash_only_required": True,
            "fresh_expected_head_check_required": True,
        },
        "workflow_success_is_not_comparison_authority": True,
    }
    sensitive_scan(evidence)
    validate_evidence(evidence)
    return evidence


def validate_evidence(evidence: Any) -> None:
    require(isinstance(evidence, dict), "evidence must be an object")
    sensitive_scan(evidence)
    require(evidence.get("schema") == EVIDENCE_SCHEMA, "evidence schema mismatch")
    require(evidence.get("source_schema") == SOURCE_SCHEMA, "evidence source schema mismatch")
    require(evidence.get("mission_id") == MISSION_ID, "evidence mission mismatch")
    run = evidence.get("run")
    require(isinstance(run, dict), "evidence run missing")
    require(str(run.get("run_id", "")).isdigit() and str(run.get("run_attempt", "")).isdigit(), "evidence run identity invalid")
    require(isinstance(run.get("head_sha"), str) and SHA_RE.fullmatch(run["head_sha"]) is not None, "evidence head invalid")
    require(run.get("branch") == "main" and run.get("event") == ALLOWED_EVENT and run.get("conclusion") == "success",
            "evidence source execution identity invalid")
    workflow = run.get("workflow")
    require(isinstance(workflow, dict), "workflow identity missing")
    require(workflow.get("name") == WORKFLOW_NAME and workflow.get("path") == WORKFLOW_PATH, "workflow identity mismatch")
    require(str(workflow.get("id", "")).isdigit(), "workflow id invalid")
    require(run.get("projection_code_sha") == run["head_sha"], "projection code binding mismatch")
    require(isinstance(run.get("publication_base_main_sha"), str) and SHA_RE.fullmatch(run["publication_base_main_sha"]) is not None,
            "publication base invalid")
    source_packet = {
        key: copy.deepcopy(evidence[key])
        for key in (
            "reviewed_v5", "contract", "editor", "source", "adaptation_seed",
            "candidate", "attempts", "run_registry_refs", "all_attempt_refs",
            "source_registry", "native_s3_pass", "historical_not_run_cells_preserved",
            "historical_not_run_cells_mutated", "authority",
        )
    }
    source_packet.update({
        "schema": SOURCE_SCHEMA,
        "mission_id": MISSION_ID,
        "run": {
            "repository": REPOSITORY,
            "ref": "refs/heads/main",
            "head_sha": run["head_sha"],
            "event": run["event"],
            "run_id": run["run_id"],
            "run_attempt": run["run_attempt"],
        },
    })
    validate_packet(source_packet)
    publication = evidence.get("publication")
    require(publication == {
        "mode": "IMMUTABLE_UNITY_S3_V5_LINEAGE_EVIDENCE_BRANCH",
        "direct_main_push": False,
        "draft_pr_created_by_workflow": False,
        "separate_draft_pr_handoff_required": True,
        "integration_authority": False,
        "squash_only_required": True,
        "fresh_expected_head_check_required": True,
    }, "publication authority mismatch")
    require(evidence.get("workflow_success_is_not_comparison_authority") is True, "workflow success authority boundary missing")


def self_test() -> None:
    base = synthetic_packet()
    evidence = record(
        base,
        run_id="123",
        run_attempt="1",
        head_sha="b" * 40,
        branch="main",
        source_workflow_id="987",
        source_workflow_name=WORKFLOW_NAME,
        source_workflow_path=WORKFLOW_PATH,
        source_event=ALLOWED_EVENT,
        source_conclusion="success",
        projection_code_sha="b" * 40,
        publication_base_main_sha="c" * 40,
    )
    validate_evidence(evidence)
    negatives: list[str] = []

    def rejected(name: str, fn) -> None:
        try:
            fn()
        except ValueError:
            negatives.append(name)
        else:
            raise AssertionError(f"negative case accepted: {name}")

    rejected("wrong_run_id", lambda: record(
        base, run_id="999", run_attempt="1", head_sha="b" * 40, branch="main",
        source_workflow_id="987", source_workflow_name=WORKFLOW_NAME,
        source_workflow_path=WORKFLOW_PATH, source_event=ALLOWED_EVENT,
        source_conclusion="success", projection_code_sha="b" * 40,
        publication_base_main_sha="c" * 40,
    ))
    rejected("wrong_head", lambda: record(
        base, run_id="123", run_attempt="1", head_sha="d" * 40, branch="main",
        source_workflow_id="987", source_workflow_name=WORKFLOW_NAME,
        source_workflow_path=WORKFLOW_PATH, source_event=ALLOWED_EVENT,
        source_conclusion="success", projection_code_sha="d" * 40,
        publication_base_main_sha="c" * 40,
    ))
    rejected("wrong_workflow", lambda: record(
        base, run_id="123", run_attempt="1", head_sha="b" * 40, branch="main",
        source_workflow_id="987", source_workflow_name="OTHER",
        source_workflow_path=WORKFLOW_PATH, source_event=ALLOWED_EVENT,
        source_conclusion="success", projection_code_sha="b" * 40,
        publication_base_main_sha="c" * 40,
    ))
    tampered = copy.deepcopy(base)
    tampered["attempts"]["UNITY-S3-FI1"]["source_binding_id"] = "0" * 64
    rejected("tampered_lineage", lambda: record(
        tampered, run_id="123", run_attempt="1", head_sha="b" * 40, branch="main",
        source_workflow_id="987", source_workflow_name=WORKFLOW_NAME,
        source_workflow_path=WORKFLOW_PATH, source_event=ALLOWED_EVENT,
        source_conclusion="success", projection_code_sha="b" * 40,
        publication_base_main_sha="c" * 40,
    ))
    secret = copy.deepcopy(base)
    secret["session_token"] = "redacted"
    rejected("sensitive_field", lambda: record(
        secret, run_id="123", run_attempt="1", head_sha="b" * 40, branch="main",
        source_workflow_id="987", source_workflow_name=WORKFLOW_NAME,
        source_workflow_path=WORKFLOW_PATH, source_event=ALLOWED_EVENT,
        source_conclusion="success", projection_code_sha="b" * 40,
        publication_base_main_sha="c" * 40,
    ))
    assert len(negatives) == 5
    print(json.dumps({"self_test": "PASS", "negative_cases": negatives}, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--input")
    parser.add_argument("--output")
    parser.add_argument("--run-id")
    parser.add_argument("--run-attempt")
    parser.add_argument("--head-sha")
    parser.add_argument("--branch")
    parser.add_argument("--source-workflow-id")
    parser.add_argument("--source-workflow-name")
    parser.add_argument("--source-workflow-path")
    parser.add_argument("--source-event")
    parser.add_argument("--source-conclusion")
    parser.add_argument("--projection-code-sha")
    parser.add_argument("--publication-base-main-sha")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    required = (
        args.input, args.output, args.run_id, args.run_attempt, args.head_sha, args.branch,
        args.source_workflow_id, args.source_workflow_name, args.source_workflow_path,
        args.source_event, args.source_conclusion, args.projection_code_sha,
        args.publication_base_main_sha,
    )
    require(all(value is not None for value in required), "all recorder arguments are required")
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
    output = pathlib.Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "schema": EVIDENCE_SCHEMA,
        "run_id": args.run_id,
        "head_sha": args.head_sha,
        "native_s3_pass": evidence["native_s3_pass"],
        "candidate_generation_id": evidence["candidate"]["candidate_generation_id"],
        "sanitized": True,
        "integration_authority": False,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
