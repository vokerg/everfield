#!/usr/bin/env python3
"""Fail-closed source-run gate for the Unity S3 reviewed-v5 lineage recorder."""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.request
from collections.abc import Callable
from typing import Any


EXPECTED_REPOSITORY = "vokerg/everfield"
EXPECTED_WORKFLOW_NAME = "Everfield Unity S3 reviewed-v5 lineage evaluator"
EXPECTED_WORKFLOW_PATH = ".github/workflows/unity-s3-v5-lineage-evaluator.yml"
NONTERMINAL_STATUSES = frozenset({"queued", "in_progress"})


class GateError(RuntimeError):
    """Raised when source evidence identity or terminality fails closed."""


def _sha40(value: str, label: str) -> str:
    normalized = value.lower()
    if len(normalized) != 40 or any(c not in "0123456789abcdef" for c in normalized):
        raise GateError(f"{label} is not sha40")
    return normalized


def validate_source_run_identity(
    run: dict[str, Any],
    *,
    run_id: str,
    run_attempt: str,
    source_head_sha: str,
) -> str:
    if not run_id.isdigit() or not run_attempt.isdigit():
        raise GateError("source run identity is not numeric")
    expected_head = _sha40(source_head_sha, "source head")
    workflow_id = str(run.get("workflow_id") or "")
    checks = {
        "id": str(run.get("id")) == run_id,
        "run_attempt": str(run.get("run_attempt")) == run_attempt,
        "name": run.get("name") == EXPECTED_WORKFLOW_NAME,
        "event": run.get("event") == "workflow_dispatch",
        "head_branch": run.get("head_branch") == "main",
        "head_sha": str(run.get("head_sha") or "").lower() == expected_head,
        "repository": (run.get("repository") or {}).get("full_name") == EXPECTED_REPOSITORY,
        "workflow_id": workflow_id.isdigit(),
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise GateError(f"source run identity mismatch: {failed}")
    return workflow_id


def wait_for_terminal_success(
    fetch_run: Callable[[], dict[str, Any]],
    *,
    run_id: str,
    run_attempt: str,
    source_head_sha: str,
    max_polls: int,
    sleep_seconds: float,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> tuple[dict[str, Any], str, list[str]]:
    if max_polls < 1:
        raise GateError("max polls must be positive")
    if sleep_seconds < 0:
        raise GateError("sleep seconds must be nonnegative")

    observed: list[str] = []
    for poll_index in range(max_polls):
        run = fetch_run()
        workflow_id = validate_source_run_identity(
            run,
            run_id=run_id,
            run_attempt=run_attempt,
            source_head_sha=source_head_sha,
        )
        status = str(run.get("status") or "")
        observed.append(status)
        if status == "completed":
            if run.get("conclusion") != "success":
                raise GateError(
                    f"source evaluator reached terminal non-success conclusion: {run.get('conclusion')!r}"
                )
            return run, workflow_id, observed
        if status not in NONTERMINAL_STATUSES:
            raise GateError(f"unexpected nonterminal source status: {status!r}")
        if poll_index + 1 < max_polls:
            sleep_fn(sleep_seconds)

    raise GateError(
        f"source evaluator did not reach terminal success within {max_polls} polls; "
        f"observed={observed}"
    )


def validate_workflow_identity(workflow: dict[str, Any], workflow_id: str) -> None:
    checks = {
        "id": str(workflow.get("id")) == workflow_id,
        "name": workflow.get("name") == EXPECTED_WORKFLOW_NAME,
        "path": workflow.get("path") == EXPECTED_WORKFLOW_PATH,
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise GateError(f"source workflow identity mismatch: {failed}")


def validate_current_main(
    branch: dict[str, Any],
    *,
    source_head_sha: str,
    recorder_workflow_sha: str,
) -> str:
    expected_head = _sha40(source_head_sha, "source head")
    workflow_head = _sha40(recorder_workflow_sha, "recorder workflow head")
    publication_base = str((branch.get("commit") or {}).get("sha") or "").lower()
    if publication_base != expected_head:
        raise GateError("source head is not exact current main")
    if workflow_head != expected_head:
        raise GateError("recorder workflow code is not exact source/current main")
    return publication_base


def _self_test() -> None:
    base = {
        "id": 101,
        "run_attempt": 2,
        "name": EXPECTED_WORKFLOW_NAME,
        "event": "workflow_dispatch",
        "head_branch": "main",
        "head_sha": "a" * 40,
        "repository": {"full_name": EXPECTED_REPOSITORY},
        "workflow_id": 77,
    }

    snapshots = [
        {**base, "status": "queued", "conclusion": None},
        {**base, "status": "in_progress", "conclusion": None},
        {**base, "status": "completed", "conclusion": "success"},
    ]
    cursor = iter(snapshots)
    run, workflow_id, observed = wait_for_terminal_success(
        lambda: next(cursor),
        run_id="101",
        run_attempt="2",
        source_head_sha="a" * 40,
        max_polls=3,
        sleep_seconds=0,
        sleep_fn=lambda _: None,
    )
    assert run["conclusion"] == "success"
    assert workflow_id == "77"
    assert observed == ["queued", "in_progress", "completed"]

    def must_fail(fn: Callable[[], object], needle: str) -> None:
        try:
            fn()
        except GateError as exc:
            assert needle in str(exc), (needle, str(exc))
        else:
            raise AssertionError(f"expected GateError containing {needle!r}")

    must_fail(
        lambda: wait_for_terminal_success(
            lambda: {**base, "status": "completed", "conclusion": "failure"},
            run_id="101",
            run_attempt="2",
            source_head_sha="a" * 40,
            max_polls=1,
            sleep_seconds=0,
        ),
        "terminal non-success",
    )
    must_fail(
        lambda: wait_for_terminal_success(
            lambda: {**base, "status": "in_progress", "conclusion": None},
            run_id="101",
            run_attempt="2",
            source_head_sha="a" * 40,
            max_polls=2,
            sleep_seconds=0,
            sleep_fn=lambda _: None,
        ),
        "did not reach terminal success",
    )
    must_fail(
        lambda: wait_for_terminal_success(
            lambda: {**base, "run_attempt": 3, "status": "in_progress", "conclusion": None},
            run_id="101",
            run_attempt="2",
            source_head_sha="a" * 40,
            max_polls=1,
            sleep_seconds=0,
        ),
        "run_attempt",
    )
    must_fail(
        lambda: wait_for_terminal_success(
            lambda: {**base, "head_sha": "b" * 40, "status": "in_progress", "conclusion": None},
            run_id="101",
            run_attempt="2",
            source_head_sha="a" * 40,
            max_polls=1,
            sleep_seconds=0,
        ),
        "head_sha",
    )
    must_fail(
        lambda: wait_for_terminal_success(
            lambda: {**base, "name": "wrong", "status": "in_progress", "conclusion": None},
            run_id="101",
            run_attempt="2",
            source_head_sha="a" * 40,
            max_polls=1,
            sleep_seconds=0,
        ),
        "name",
    )
    validate_workflow_identity(
        {"id": 77, "name": EXPECTED_WORKFLOW_NAME, "path": EXPECTED_WORKFLOW_PATH},
        "77",
    )
    must_fail(
        lambda: validate_workflow_identity(
            {"id": 77, "name": EXPECTED_WORKFLOW_NAME, "path": ".github/workflows/other.yml"},
            "77",
        ),
        "path",
    )
    assert (
        validate_current_main(
            {"commit": {"sha": "a" * 40}},
            source_head_sha="a" * 40,
            recorder_workflow_sha="a" * 40,
        )
        == "a" * 40
    )
    must_fail(
        lambda: validate_current_main(
            {"commit": {"sha": "b" * 40}},
            source_head_sha="a" * 40,
            recorder_workflow_sha="b" * 40,
        ),
        "exact current main",
    )
    must_fail(
        lambda: validate_current_main(
            {"commit": {"sha": "a" * 40}},
            source_head_sha="a" * 40,
            recorder_workflow_sha="b" * 40,
        ),
        "recorder workflow code",
    )
    print("unity-s3-v5 recorder source-run gate self-test: PASS")


def _api_get(path: str, *, api: str, repo: str, token: str) -> dict[str, Any]:
    request = urllib.request.Request(
        f"{api}/repos/{repo}/{path}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id")
    parser.add_argument("--run-attempt")
    parser.add_argument("--source-head-sha")
    parser.add_argument("--recorder-workflow-sha")
    parser.add_argument("--github-env")
    parser.add_argument("--max-polls", type=int, default=24)
    parser.add_argument("--sleep-seconds", type=float, default=5.0)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        _self_test()
        return

    required = {
        "run-id": args.run_id,
        "run-attempt": args.run_attempt,
        "source-head-sha": args.source_head_sha,
        "recorder-workflow-sha": args.recorder_workflow_sha,
        "github-env": args.github_env,
    }
    missing = [name for name, value in required.items() if not value]
    if missing:
        raise SystemExit(f"missing required arguments: {missing}")

    api = os.environ["GITHUB_API_URL"].rstrip("/")
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GH_TOKEN"]
    if repo != EXPECTED_REPOSITORY:
        raise SystemExit("repository identity mismatch")

    try:
        run, workflow_id, observed = wait_for_terminal_success(
            lambda: _api_get(f"actions/runs/{args.run_id}", api=api, repo=repo, token=token),
            run_id=args.run_id,
            run_attempt=args.run_attempt,
            source_head_sha=args.source_head_sha,
            max_polls=args.max_polls,
            sleep_seconds=args.sleep_seconds,
        )
        workflow = _api_get(f"actions/workflows/{workflow_id}", api=api, repo=repo, token=token)
        validate_workflow_identity(workflow, workflow_id)
        branch = _api_get("branches/main", api=api, repo=repo, token=token)
        publication_base = validate_current_main(
            branch,
            source_head_sha=args.source_head_sha,
            recorder_workflow_sha=args.recorder_workflow_sha,
        )
    except GateError as exc:
        raise SystemExit(str(exc)) from exc

    with open(args.github_env, "a", encoding="utf-8") as out:
        out.write(f"SOURCE_WORKFLOW_ID={workflow_id}\n")
        out.write(f"SOURCE_WORKFLOW_PATH={EXPECTED_WORKFLOW_PATH}\n")
        out.write(f"SOURCE_WORKFLOW_NAME={EXPECTED_WORKFLOW_NAME}\n")
        out.write(f"PUBLICATION_BASE_MAIN_SHA={publication_base}\n")

    print(
        json.dumps(
            {
                "publication_base_main_sha": publication_base,
                "run_attempt": run["run_attempt"],
                "run_id": run["id"],
                "source_head_sha": args.source_head_sha.lower(),
                "source_status": run["status"],
                "source_conclusion": run["conclusion"],
                "source_workflow_id": workflow_id,
                "terminal_gate_observations": observed,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
