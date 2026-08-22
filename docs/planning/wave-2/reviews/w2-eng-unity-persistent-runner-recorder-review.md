# W2-ENG-UNITY-PERSISTENT-RUNNER-REC-REV-01 — recorder cache remediation review

## Frozen identity

- reviewed issue: #644 / `W2-ENG-UNITY-PERSISTENT-RUNNER-REC-01`;
- reviewed PR: #645;
- producer base: `730bb3d05fe89de43c029e7ec640445eae2e310b`;
- producer head: `ee5263dd948ef25d270d18aa2740bfa6c9d69b11`;
- review issue: #646;
- trust mode: `DEGRADED_SINGLE_AGENT_FRESH_REVIEW_EPISODE`;
- exact changed path: `.github/workflows/unity-persistent-evidence-recorder.yml`.

## Review checks

The immutable producer was checked out separately and verified as exactly one workflow-line remediation:

1. `PYTHONPYCACHEPREFIX="$RUNNER_TEMP/persistent-unity-recorder-pycache"` scopes bytecode output to runner temp.
2. The existing `py_compile` command remains unchanged in inputs and still runs before the clean-checkout assertion.
3. The recorder's exact upstream workflow/run/head/artifact binding, projection, evidence path, branch publication, permissions, and authority boundaries are untouched.
4. The bounded compile test with the temporary cache prefix leaves the checkout clean.
5. Ruby YAML parsing and `git diff --check` pass.

## Finding

`R1 — PASS`: the remediation fixes the observed `__pycache__` false failure without weakening the clean-worktree fence or changing any Unity/evidence semantics.

## Disposition

`PASS_FOR_INTEGRATION`

No BLOCKER, MAJOR, or correction-requiring MINOR finding. The candidate is safe for the separately authorized squash-only integration, after which one fresh exact-main Unity/recorder episode is required.

Authority: review provenance only; `NOT_CANONICAL`.
