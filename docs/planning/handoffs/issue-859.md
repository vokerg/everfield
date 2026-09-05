# Handoff — Issue #859 / W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM-02-REV-01

## Review identity

- task class: `REQUIRED_SECURITY_AUTHORITY_REVIEW`;
- trust mode: `DEGRADED_SINGLE_AGENT`;
- ownership: Issue #859 comment `5551671778`;
- review branch: `planning/issue-859`;
- base/current-main basis: `88b704183e99dbd0dd102131c67a99fd0013ff36`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- canonicality: `NOT_CANONICAL`.

Judged producer:

- Issue #845 terminal `STATUS(REVIEW_READY)`: comment `5550540041`;
- producer recovery owner: comment `5550531730`;
- PR #853, draft/open;
- exact branch/head: `planning/issue-845@53463beff138d5854f4268c5be20cdc11554716a`;
- source review: Issue #843 terminal comment `5536070954`, `CHANGES_NEEDED`;
- source finding: `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REV-M01`.

## Review result

Disposition: `CHANGES_NEEDED`.

Counts:

- BLOCKER: 0;
- MAJOR: 1;
- correction-requiring MINOR: 0;
- informational: 0.

Finding: `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM02-REV-M01`.

The producer fixes the prior same-run terminality deadlock by moving recording into a separate GitHub-hosted `workflow_dispatch` run and keeps write/dispatch authority off the persistent Unity runner. Its source terminality/current-main/artifact/projection identity gates are otherwise materially bounded.

The remaining MAJOR is evidence-branch publication liveness. The reviewed recorder sets `persist-credentials: false` on both checkouts, then later performs a plain `git push origin` without explicitly supplying `${{ github.token }}` or another Git authentication mechanism. `contents: write` scopes the token but does not automatically authenticate a Git command after checkout credentials are deliberately not persisted. The current-main predecessor source checkout had default persisted credentials; the reviewed packet introduces the credential removal while leaving the push unchanged.

The producer validator does not test this path: it checks write permission, branch naming and one-file staging but has no authenticated-publication invariant or negative control.

Review report:

- path: `docs/planning/wave-2/reviews/w2-unity-s3-v5-recorder-trigger-remediation-02-review.md`;
- blob: `a63f1944a497d4397e54fe932e11fb4b9c948c84`.

## Required next route

Create exactly one bounded blocking-remediation successor for `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM02-REV-M01` that restores authenticated evidence-branch publication only on the GitHub-hosted recorder path and adds deterministic/static coverage for that authentication boundary.

The successor must preserve:

- no write-capable token on the persistent native Unity job;
- exact separate recorder dispatch topology and bounded terminal source polling;
- exact run/attempt/workflow/repository/head/current-main/artifact identities;
- one generated evidence file and immutable evidence branch;
- no direct-main publication, no automatic PR and no integration authority;
- no token leakage or broader repository write authority.

After remediation, route a fresh exact-head independent/degraded-independent security/authority review. Only a clean future `PASS_FOR_INTEGRATION` can route separate authorized squash-only publication followed by fresh exact-main end-to-end verification.

No native evaluator run was performed by this review. No provider PASS, `PASS_FOR_COMPARISON`, aggregate verification PASS, engine selection/readiness, implementation, production/release, integration, decision, or canonical authority is granted.
