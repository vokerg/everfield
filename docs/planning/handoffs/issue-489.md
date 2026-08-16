# Issue #489 handoff — W2-ENG-PROVIDER-UNITY-CLI-PATH-REM-01

## State

Workflow path-remediation candidate is ready for one fresh required security/authority review.

## Exact provenance

- claim: Issue #489 comment `5309642489`;
- branch: `planning/issue-489`;
- base/current main at claim: `eb30f078fe6ff4f27a54998163b66ebd22d9c84d`;
- triggering evaluator run `31972010957`, job `95225790858`;
- Unity stage `LOGIN_PROCESS_FAILED`, login/status exit `127` after pre-secret syntax/full-self-test PASS;
- immutable evidence PR #488;
- independent Unreal human gate: Issue #480.

## Root cause

The trusted-main install step successfully executes `unity --version`, but then discards the executable actually resolved by the shell and writes the unverified assumption `$HOME/.unity/bin/unity` into `GITHUB_ENV`. The validator executes `UNITY_CLI` directly and fresh evidence observes FileNotFound-style exit `127` for both auth commands.

## Candidate implementation

Implementation commit `9d5350f9e13ff51dfd6c73de4ab26be22b084e76`.

Workflow candidate blob `94b740e1b9ca25fc6c23b767d681cc21a497cfac`.

The candidate changes only the Unity CLI install/path-publication step:

1. install the same exact pinned CLI `1.0.0-beta.5`;
2. keep the existing PATH export;
3. resolve the executable with `command -v unity`;
4. fail closed on empty/non-executable discovery;
5. canonicalize with `readlink -f`;
6. fail closed on empty/non-executable canonical path;
7. execute the exact pinned-version check through the canonical path;
8. publish that exact path as `UNITY_CLI` to `GITHUB_ENV`.

The candidate does not touch environment `engine-eval`, permissions, trusted-main identity checks, validator code, provider secrets, secret injection timing, sanitized evidence checks, artifact publication, Unreal behavior or provider authority semantics.

## Producer-side verification

Exact diff before this handoff: one owned workflow path only, 9 additions / 2 deletions, one commit ahead of exact base.

Static checks from the exact workflow source:

- no provider secret expression appears in the install/path step;
- `command -v unity` is the source of `UNITY_CLI_DISCOVERED`;
- `readlink -f` produces `UNITY_CLI_RESOLVED`;
- both discovered and resolved paths are checked with `test -x`;
- version `1.0.0-beta.5` is checked by invoking `"$UNITY_CLI_RESOLVED" --version`;
- only the resolved path is written to `GITHUB_ENV`;
- pre-secret validator syntax/full-self-test step remains before the credential-bearing validation step.

No task-branch Actions execution is permitted by the workflow because the job is guarded to `refs/heads/main`. Fresh required review must inspect YAML/shell correctness and preservation of secret boundaries. First reviewed publication on main is the executable proof.

## Required fresh review

Attack at least:

1. exact trusted-main/workflow/permission/environment/secret-boundary preservation;
2. whether `command -v` output can be attacker-controlled under the trusted-main runner model;
3. whether `readlink -f` and `test -x` fail closed rather than silently accepting a missing executable;
4. whether exact pinned-version validation occurs through the exact published path;
5. whether any secret becomes available before path resolution;
6. whether newline/path injection into `GITHUB_ENV` is possible from the resolved runner executable path;
7. whether the diff is truly workflow-path-only and leaves validator/provider semantics unchanged;
8. whether reviewed publication followed by a fresh trusted-main run is sufficient to establish the next Unity stage.

Any correction requires a new bounded remediation successor; do not repair `planning/issue-489` from review.

## Authority boundary

`NOT_CANONICAL`. Workflow path remediation only. No provider credential/PASS, Unity license authority, engine selection, readiness, release, verification-PASS, decision, integration or canonical authority.