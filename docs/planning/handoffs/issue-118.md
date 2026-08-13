# Issue #118 handoff — W2-PG-REM-RIGHTS-01

## Status

Independent bounded pre-gate review of Issue #114 is complete on `planning/issue-118` from exact `main@042d140b5d2e0b951da4528e1867514983418d6f`.

Disposition: **`CHANGES_NEEDED` — 0 BLOCKER / 2 MAJOR / 1 MINOR.**

This review is non-authority input only. Formal aggregate `W2-REV-01` remains required.

## Immutable reviewed input

- Issue #114 terminal status comment: `5276636185`
- Issue #114 work/head: `4ba39fa26404ba9564702fd385c133df75b71972`
- corrected report blob: `124866c20a6082624d3beba624859273b0d5572a`
- finding-disposition blob: `8cb5c60a9c0db2536194504325559d6bf25ca228`
- handoff blob: `7a54200799f68ce5154f065acb1593dc8b372f8f`
- review-visibility PR: #116, treated as visibility only

Frozen upstream producer provenance remains Issue #80 work/head `3c262cbf767633e0ca42f6bdf387e262056b4fb0` with report blob `bda0551c446c93492c9d8e809d087d592dfcdae3`.

## Exact review artifact

- `docs/planning/wave-2/reviews/w2-rem-rights-01-pre-gate-review.md`
- review artifact blob: `45f513bc4e8328ed75b979b76e982a2454705956`

## Findings

### `PG-REM-RIGHTS-M01` — MAJOR

`ORIGINALITY-RISK-v1` policy rows overlap without a closed row-selection, precedence, or merge operation. One exact tuple such as `PROJECT_NATIVE + STYLE_OR_CREATOR_NAMED + RELEASE + no material triggers` matches materially conflicting rows, so the packet cannot guarantee one exact normalized evidence-requirement set.

### `PG-REM-RIGHTS-M02` — MAJOR

Many `CONDITIONAL`/contextual evidence cells have no exact predicate that deterministically compiles them to `REQUIRED` or `NOT_APPLICABLE`. In addition, authority-bearing IDs/root are only described as stable/content-bound: no canonical encoding, field-inclusion, ordering, digest/domain-separation, or mandatory recomputation rule makes changed reference-use context mechanically force an identity change.

### `PG-REM-RIGHTS-m01` — MINOR

The stale-state precedence explicitly covers provider/legal/license/permission evidence, while the same policy can require other originality evidence kinds. Those stale required evidence kinds block `CLEAR` but do not have one exact primary state/reason derivation.

## Preserved boundaries

The exact Issue #114 packet does preserve the intended no-legal-clearance boundary, similarity-as-escalation-only semantics, release blocking for unresolved state, and no production/readiness/integration/verification/canonicalization authority. This review adds no stronger authority.

## Bounded successor

Issue #119 / `W2-REM-RIGHTS-02` was created as the single remediation successor and is **BLOCKED until this review publishes a valid terminal schema-3 `STATUS(REVIEW_READY)`**. It must consume this review immutably and repair only the policy determinism/content-identity/stale-state gaps.

Do not claim Issue #119 from this review episode.

## Required terminal steps

1. Open a draft PR from exact `planning/issue-118` to `main` for review visibility.
2. Re-fetch the branch and PR after this handoff commit.
3. Require PR open + draft and PR head equal the exact terminal `head_sha`.
4. Publish schema-3 `STATUS(REVIEW_READY)` on Issue #118 with disposition `CHANGES_NEEDED`, exact artifact refs, findings, and successor #119.

No integration is authorized. Any eventual `main` integration remains squash-only through a separately valid route.