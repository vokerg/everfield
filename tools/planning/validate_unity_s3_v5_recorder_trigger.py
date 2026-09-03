#!/usr/bin/env python3
"""Static fail-closed checks for the reviewed-v5 Unity recorder trigger boundary."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EVALUATOR = ROOT / ".github/workflows/unity-s3-v5-lineage-evaluator.yml"
RECORDER = ROOT / ".github/workflows/unity-s3-v5-lineage-recorder.yml"


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"missing recorder-trigger invariant: {label}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise SystemExit(f"forbidden recorder-trigger topology: {label}")


def main() -> None:
    evaluator = EVALUATOR.read_text(encoding="utf-8")
    recorder = RECORDER.read_text(encoding="utf-8")

    # The native Unity job remains self-hosted and workflow-level read-only.
    require(evaluator, "permissions:\n  contents: read\n", "evaluator workflow read-only default")
    require(evaluator, "runs-on: [self-hosted, macOS, ARM64, everfield-unity]", "native runner identity")
    lineage, separator, record_job = evaluator.partition("\n  record:\n")
    if not separator:
        raise SystemExit("missing explicit GitHub-hosted recorder continuation job")
    forbid(lineage, "contents: write", "write permission on native Unity lineage job")
    require(record_job, "needs: lineage", "recorder depends on successful native lineage")
    require(record_job, "actions: read", "recorder caller actions read permission")
    require(record_job, "contents: write", "recorder caller bounded evidence-branch permission")
    require(
        record_job,
        "uses: ./.github/workflows/unity-s3-v5-lineage-recorder.yml",
        "explicit reusable recorder call",
    )
    require(record_job, "source_run_id: ${{ github.run_id }}", "exact caller run id")
    require(record_job, "source_run_attempt: ${{ github.run_attempt }}", "exact caller run attempt")
    require(record_job, "source_head_sha: ${{ github.sha }}", "exact caller source head")

    # The recorder is reusable only: no event-recursion or independently forgeable dispatch route.
    require(recorder, "  workflow_call:\n", "reusable recorder trigger")
    forbid(recorder, "  workflow_run:\n", "suppressed workflow_run dependency")
    forbid(recorder, "  workflow_dispatch:\n", "independent manual recorder dispatch")
    forbid(recorder, "  repository_dispatch:\n", "independent repository recorder dispatch")
    require(recorder, "runs-on: ubuntu-24.04", "GitHub-hosted recorder runner")
    require(recorder, "source_run_id:\n", "required source run input")
    require(recorder, "source_run_attempt:\n", "required source attempt input")
    require(recorder, "source_head_sha:\n", "required source head input")

    # Runtime binding rejects arbitrary runs/workflows/heads and stale main.
    for needle, label in (
        ('"id": str(run.get("id")) == run_id', "run id binding"),
        ('"run_attempt": str(run.get("run_attempt")) == run_attempt', "attempt binding"),
        ('"name": run.get("name") == expected_name', "workflow name binding"),
        ('"event": run.get("event") == "workflow_dispatch"', "source event binding"),
        ('"status": run.get("status") == "completed"', "completed source binding"),
        ('"conclusion": run.get("conclusion") == "success"', "successful source binding"),
        ('"head_branch": run.get("head_branch") == "main"', "main branch binding"),
        ('"head_sha": run.get("head_sha") == expected_head', "source head binding"),
        ('workflow.get("path") != expected_path', "workflow path binding"),
        ('workflow.get("name") != expected_name', "workflow API name binding"),
        ('if publication_base != expected_head:', "exact-current-main binding"),
        ('raise SystemExit("source head is not exact current main")', "main drift fail-closed"),
    ):
        require(recorder, needle, label)

    require(recorder, "ref: ${{ inputs.source_head_sha }}", "projection checkout exact source head")
    require(
        recorder,
        "name: w2-unity-s3-v5-lineage-${{ inputs.source_run_id }}-${{ inputs.source_run_attempt }}",
        "exact artifact name binding",
    )
    require(recorder, "run-id: ${{ inputs.source_run_id }}", "artifact source run binding")
    require(
        recorder,
        'EVIDENCE_BRANCH="evidence/unity-s3-v5-lineage/run-${RUN_ID}-attempt-${RUN_ATTEMPT}"',
        "immutable run/attempt evidence branch",
    )
    require(recorder, 'test "$(git diff --cached --name-only)" = "$EVIDENCE_PATH"', "one-file publication bound")
    require(recorder, '"draft_pr_created_by_workflow": False', "no automatic PR")
    require(recorder, '"integration_authority": False', "no integration authority")

    print("unity-s3-v5 recorder trigger static contract: PASS")


if __name__ == "__main__":
    main()
