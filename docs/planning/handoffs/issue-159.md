# Issue #159 handoff — W2-PG-REM-RIGHTS-05

## Episode identity

- mission: `W2-PG-REM-RIGHTS-05`
- issue: `#159`
- branch: `planning/issue-159`
- reviewer actor/session: `w2-pg-rem-rights-05-gpt56sol-20260813-1405`
- trust profile: `DEGRADED_INDEPENDENT_FRESH_SESSION`
- base main at claim: `b5dd922b3170361403ee3fb02376febf737da5cc`
- ownership claim comment: `5280206364`
- reviewed remediation: Issue #148 terminal `5278118090`
- reviewed head/work: `91545c6121a3cf071df524fd17e5e2978f7a65b2`
- reviewed draft PR: #157 at the exact reviewed head
- review artifact: `docs/planning/wave-2/reviews/w2-rem-rights-05-pre-gate-review.md`

## Review result

Disposition: `CHANGES_NEEDED`.

Findings:

- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 0
- material finding: `PG-REM5-RIGHTS-M01`

The bounded duplicate-trigger semantic correction itself withstands the review attacks: all closed-domain duplicate trigger lists are rejected before the inherited set conversion; malformed nested/container/scalar members remain on the predecessor typed fail-closed path; valid unique-trigger ordering is not strengthened into authority; and Issue #148 does not modify the predecessor valid-domain compilation/audit implementation.

The packet is nevertheless not clean because its executable evidence is not self-contained across the authorized squash-integration lifecycle. The Issue #148 delta fixture imports predecessor Git blob `39fcdc292cd37661a061c6d3027715106b3a3d27` using `git cat-file`, but that object is preserved only through Issue #148 task-branch ancestry. The resulting #148 PR tree does not retain the predecessor fixture. A squash commit to main therefore does not guarantee that a main-only checkout can resolve the blob, so the integrated evidence capsule can become non-executable before T01–T16/audit reproduction.

## Routed remediation

Exactly one bounded successor was created: Issue #162 / `W2-REM-RIGHTS-06`, initially BLOCKED until this review terminalizes with `CHANGES_NEEDED` / `PG-REM5-RIGHTS-M01`.

That successor must make the rights delta evidence self-contained in the resulting tree, bind the exact predecessor bytes durably, preserve the duplicate-trigger correction and inherited semantics, and then undergo one fresh independent pre-gate review. If that later review is clean, the rights lane proceeds to formal `W2-REV-01`; optional review churn is not authorized.

## Authority and stopping boundary

Issue #148 is not accepted as clean W2 review input by this episode and is not authorized for noncanonical evidence-provenance integration by this review. This negative review may itself be retained as review provenance only through a separately valid integration route.

No legal clearance, provider permission, release approval, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority is created.

Before terminal schema-3 `STATUS(REVIEW_READY)`, an open draft PR from `planning/issue-159` to `main` must exist and its head must equal the exact terminal `head_sha`. No branch mutation may occur after that exact-head binding and before terminal status.