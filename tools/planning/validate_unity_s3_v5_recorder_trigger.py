#!/usr/bin/env python3
"""Static and temporal fail-closed checks for the reviewed-v5 Unity recorder trigger boundary."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EVALUATOR = ROOT / ".github/workflows/unity-s3-v5-lineage-evaluator.yml"
RECORDER = ROOT / ".github/workflows/unity-s3-v5-lineage-recorder.yml"
SOURCE_GATE = ROOT / "tools/planning/unity_s3_v5_recorder_source_gate.py"


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"missing recorder-trigger invariant: {label}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise SystemExit(f"forbidden recorder-trigger topology: {label}")


def require_order(text: str, first: str, second: str, label: str) -> None:
    first_index = text.find(first)
    second_index = text.find(second)
    if first_index < 0 or second_index < 0 or first_index >= second_index:
        raise SystemExit(f"recorder-trigger ordering violation: {label}")


def validate(evaluator: str, recorder: str) -> None:
    # Native Unity remains read-only. Dispatch authority exists only on a separate
    # GitHub-hosted post-lineage control job.
    require(evaluator, "permissions:\n  contents: read\n", "evaluator workflow read-only default")
    require(evaluator, "runs-on: [self-hosted, macOS, ARM64, everfield-unity]", "native runner identity")
    lineage, separator, dispatch = evaluator.partition("\n  dispatch_recording:\n")
    if not separator:
        raise SystemExit("missing separate GitHub-hosted recorder dispatch control job")
    forbid(lineage, "actions: write", "Actions write permission on native lineage job")
    forbid(lineage, "contents: write", "contents write permission on native lineage job")
    require(dispatch, "needs: lineage", "dispatch depends on native lineage")
    require(dispatch, "runs-on: ubuntu-24.04", "dispatch control is GitHub-hosted")
    require(dispatch, "permissions:\n      actions: write", "minimum workflow-dispatch permission")
    forbid(dispatch, "contents: write", "contents write permission on dispatch control")
    require(
        dispatch,
        "/actions/workflows/{recorder_workflow}/dispatches",
        "REST workflow_dispatch endpoint",
    )
    require(dispatch, '"ref": "main"', "recorder dispatch targets main")
    require(dispatch, '"source_run_id": source_run_id', "dispatch exact source run id")
    require(dispatch, '"source_run_attempt": source_run_attempt', "dispatch exact source attempt")
    require(dispatch, '"source_head_sha": source_head_sha', "dispatch exact source head")
    forbid(
        evaluator,
        "uses: ./.github/workflows/unity-s3-v5-lineage-recorder.yml",
        "same-run reusable recorder call",
    )

    # Recorder is a separate workflow_dispatch run. Old suppressed workflow_run and
    # the reviewed-but-deadlocked same-run workflow_call routes are both forbidden.
    require(recorder, "  workflow_dispatch:\n", "separate recorder workflow dispatch trigger")
    forbid(recorder, "  workflow_run:\n", "suppressed workflow_run dependency")
    forbid(recorder, "  workflow_call:\n", "same-run reusable workflow deadlock")
    forbid(recorder, "  repository_dispatch:\n", "unexpected alternate recorder dispatch surface")
    require(recorder, "runs-on: ubuntu-24.04", "GitHub-hosted recorder runner")
    require(recorder, "source_run_id:\n", "bounded source run input")
    require(recorder, "source_run_attempt:\n", "bounded source attempt input")
    require(recorder, "source_head_sha:\n", "bounded source head input")
    require(recorder, "actions: read", "recorder Actions read permission")
    require(recorder, "contents: write", "recorder evidence-branch permission")

    # The repository token must not be persisted by either checkout. Publication
    # authentication is injected only for the final Git push subprocess.
    if recorder.count("persist-credentials: false") != 2:
        raise SystemExit("recorder must retain exactly two non-persisting checkouts")
    forbid(recorder, "persist-credentials: true", "checkout credential persistence")
    publication_marker = "\n      - name: Publish immutable lineage evidence branch handoff\n"
    _before_publication, publication_separator, publication = recorder.partition(publication_marker)
    if not publication_separator:
        raise SystemExit("missing immutable lineage publication step")
    require(publication, "          GH_TOKEN: ${{ github.token }}\n", "publication-scoped repository token")
    require(
        publication,
        "auth_header=\"$(printf 'x-access-token:%s' \"$GH_TOKEN\" | base64",
        "ephemeral basic-auth header derivation",
    )
    authenticated_push = (
        "          GIT_CONFIG_COUNT=1 \\\n"
        "          GIT_CONFIG_KEY_0=http.https://github.com/.extraheader \\\n"
        "          GIT_CONFIG_VALUE_0=\"AUTHORIZATION: basic $auth_header\" \\\n"
        "            git push origin \"HEAD:refs/heads/$EVIDENCE_BRANCH\""
    )
    require(publication, authenticated_push, "ephemeral Git-config authenticated evidence push")
    require(publication, "          unset auth_header\n", "ephemeral auth variable cleanup")
    require_order(
        publication,
        "auth_header=",
        "git push origin \"HEAD:refs/heads/$EVIDENCE_BRANCH\"",
        "authentication is derived before publication",
    )
    if publication.count('git push origin "HEAD:refs/heads/$EVIDENCE_BRANCH"') != 1:
        raise SystemExit("recorder must contain exactly one bounded evidence-branch push")
    forbid(publication, "https://x-access-token:", "token-bearing remote URL")
    forbid(publication, "git config --local http", "persistent local HTTP auth configuration")

    # Trusted gate code is loaded from the recorder's exact main workflow head before
    # any source-head checkout, then the shared temporal gate waits on the exact source.
    require_order(
        recorder,
        "name: Checkout trusted current-main recorder gate",
        "name: Wait for exact evaluator terminal success and bind current main",
        "trusted gate checkout precedes source wait",
    )
    require_order(
        recorder,
        "name: Wait for exact evaluator terminal success and bind current main",
        "name: Checkout exact source head for trusted projection code",
        "terminal gate precedes source projection checkout",
    )
    require(
        recorder,
        "python3 tools/planning/unity_s3_v5_recorder_source_gate.py",
        "shared source-run temporal gate invocation",
    )
    require(recorder, "--max-polls 24", "bounded terminal poll count")
    require(recorder, "--sleep-seconds 5", "bounded terminal poll interval")
    require(
        recorder,
        'test "$SOURCE_HEAD_SHA" = "$PUBLICATION_BASE_MAIN_SHA"',
        "projection exact-current-main binding",
    )
    require_order(
        recorder,
        "name: Reconfirm exact terminal source and current main before publication",
        "name: Publish immutable lineage evidence branch handoff",
        "final exact-main recheck precedes publication",
    )
    require(recorder, "--max-polls 1", "final terminal source recheck")
    require(recorder, "--sleep-seconds 0", "final recheck has no wait")

    # Artifact and publication remain exact and bounded.
    require(
        recorder,
        "name: w2-unity-s3-v5-lineage-${{ inputs.source_run_id }}-${{ inputs.source_run_attempt }}",
        "exact artifact name binding",
    )
    require(recorder, "run-id: ${{ inputs.source_run_id }}", "exact artifact run binding")
    require(
        recorder,
        'EVIDENCE_BRANCH="evidence/unity-s3-v5-lineage/run-${RUN_ID}-attempt-${RUN_ATTEMPT}"',
        "immutable run-attempt evidence branch",
    )
    require(
        recorder,
        'test "$(git diff --cached --name-only)" = "$EVIDENCE_PATH"',
        "one-file staged publication guard",
    )
    require(recorder, '"draft_pr_created_by_workflow": False', "no automatic PR")
    require(recorder, '"integration_authority": False', "no integration authority")

    # The shared source gate must encode the reachability semantics that the failed
    # #841 validator missed. These are structural checks plus executable self-tests.
    gate = SOURCE_GATE.read_text(encoding="utf-8")
    require(gate, 'NONTERMINAL_STATUSES = frozenset({"queued", "in_progress"})', "bounded nonterminal states")
    require(gate, 'if status == "completed":', "terminal status branch")
    require(gate, 'run.get("conclusion") != "success"', "terminal success requirement")
    require(gate, "sleep_fn(sleep_seconds)", "bounded wait between nonterminal polls")
    require(gate, "did not reach terminal success", "poll timeout fails closed")
    require(gate, '"event": run.get("event") == "workflow_dispatch"', "source event identity")
    require(gate, '"head_branch": run.get("head_branch") == "main"', "source branch identity")
    require(gate, '"repository": (run.get("repository") or {}).get("full_name") == EXPECTED_REPOSITORY', "source repository identity")
    require(gate, '"head_sha": str(run.get("head_sha") or "").lower() == expected_head', "source head identity")
    require(gate, "validate_workflow_identity(workflow, workflow_id)", "source workflow API identity")
    require(gate, "source head is not exact current main", "stale main rejection")
    require(gate, "recorder workflow code is not exact source/current main", "recorder workflow head binding")


def temporal_self_test() -> None:
    result = subprocess.run(
        [sys.executable, str(SOURCE_GATE), "--self-test"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(
            "source-run temporal gate self-test failed:\n"
            + result.stdout
            + result.stderr
        )
    if "source-run gate self-test: PASS" not in result.stdout:
        raise SystemExit("source-run temporal gate self-test did not report PASS")


def negative_static_controls(evaluator: str, recorder: str) -> None:
    publication_marker = "\n      - name: Publish immutable lineage evidence branch handoff\n"
    before_publication, separator, publication = recorder.partition(publication_marker)
    if not separator:
        raise SystemExit("negative controls cannot locate publication step")
    auth_start = publication.find("          auth_header=")
    auth_end_marker = "          unset auth_header\n"
    auth_end = publication.find(auth_end_marker)
    if auth_start < 0 or auth_end < auth_start:
        raise SystemExit("negative controls cannot locate bounded publication authentication")
    unauthenticated_publication = (
        publication[:auth_start]
        + "          git push origin \"HEAD:refs/heads/$EVIDENCE_BRANCH\"\n"
        + publication[auth_end + len(auth_end_marker):]
    )
    mutations = [
        (
            evaluator.replace("permissions:\n      actions: write", "permissions:\n      contents: write", 1),
            recorder,
            "dispatch permission mutation",
        ),
        (
            evaluator.replace(
                'f"{api}/repos/{repo}/actions/workflows/{recorder_workflow}/dispatches"',
                '"not-a-dispatch-endpoint"',
                1,
            ),
            recorder,
            "dispatch endpoint mutation",
        ),
        (
            evaluator
            + "\n# invalid same-run route\n# uses: ./.github/workflows/unity-s3-v5-lineage-recorder.yml\n",
            recorder,
            "same-run route mutation",
        ),
        (
            evaluator,
            recorder.replace("  workflow_dispatch:\n", "  workflow_call:\n", 1),
            "recorder trigger mutation",
        ),
        (
            evaluator,
            recorder.replace("--max-polls 24", "--max-polls 25", 1),
            "unbounded-policy poll mutation",
        ),
        (
            evaluator,
            recorder.replace("persist-credentials: false", "persist-credentials: true", 1),
            "credential persistence mutation",
        ),
        (
            evaluator,
            before_publication + separator + unauthenticated_publication,
            "unauthenticated plain-push topology",
        ),
    ]
    for mutated_evaluator, mutated_recorder, label in mutations:
        try:
            validate(mutated_evaluator, mutated_recorder)
        except SystemExit:
            continue
        raise SystemExit(f"negative static control unexpectedly passed: {label}")


def main() -> None:
    evaluator = EVALUATOR.read_text(encoding="utf-8")
    recorder = RECORDER.read_text(encoding="utf-8")
    if not SOURCE_GATE.is_file():
        raise SystemExit("missing shared source-run temporal gate")

    validate(evaluator, recorder)
    temporal_self_test()
    negative_static_controls(evaluator, recorder)
    print("unity-s3-v5 recorder trigger temporal/static contract: PASS")


if __name__ == "__main__":
    main()
