# Issue #148 handoff — W2-REM-RIGHTS-05

## Episode identity

- mission: `W2-REM-RIGHTS-05`
- issue: `#148`
- branch: `planning/issue-148`
- actor session: `w2-rem-rights-05-gpt56sol-20260813-1014`
- base main: `042d140b5d2e0b951da4528e1867514983418d6f`
- ownership claim: `5277796667`
- predecessor remediation: Issue #142 terminal `5277675462`, exact head `4b61b276bb28bb114a650e003a7a5d0aeb77411a`
- required independent finding: Issue #145 terminal `5277781009`, exact head `99cb77f283f5e903cd46cec230833b4c7efee431`, `PG-REM4-RIGHTS-M01`

## Correction result

`PG-REM4-RIGHTS-M01` is mechanically `RESOLVED`. Duplicate members in set-like `derive_state.material_triggers` are rejected after typed/domain validation and before any inherited set conversion or authority decision. Every duplicate closed-domain trigger returns exact `UNKNOWN / POLICY_UNRESOLVED`; nested malformed members remain fail closed; valid unique trigger order remains non-authoritative.

Evidence identities before final terminal head fencing:

- current fixture blob: `3318f773b675e1bc0c5e5b41064bb1a1a2db7eea`
- current fixture source SHA-256: `bfa69936ce34a204b74a8d2a359257b73e8e917adaa4c79b2e0987d6615df09b`
- predecessor fixture blob: `39fcdc292cd37661a061c6d3027715106b3a3d27`
- predecessor exact-byte SHA-256: `6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5`
- malformed matrix: `EVERFIELD-RIGHTS-MALFORMED-SCALAR-MATRIX-v2`, 468 cases, 0 uncaught exceptions, digest `a1fc1fd2c78b11a5a81d8bf7b24d8ffaf3133876d70f7d5ea0400b84fd90daba`
- tests: inherited T01–T15 plus `T16_DERIVED_TRIGGER_SET_TOTAL_FAIL_CLOSED`, 16 passing
- result digest: `be8f6df19367545ff2136d5c5db9c2a4c93f11f865f6d09ad4af067cb41efd4f`
- stdout SHA-256: `fef07eaaaa37b43221977b9d4eb5bbe5d22a7f9a115aa7e38c6d503886a167e1`
- finite audit: 802,816 combinations, 0 reverse-order mismatches, 0 nonclosed outputs, digest `166aebf1871a10768694790bcb936ec9ec119350676cf38fb055203259d3466c`
- self-review: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR

The executable is a noncanonical planning delta capsule. It consumes the exact predecessor Git blob from task-branch history and verifies both its Git object identity and actual byte SHA-256 before applying the bounded correction. The direct parent import commit preserves the predecessor tree for this review episode. Issue #142's older published source-SHA field does not reproduce from its exact Git blob; the exact Git object and independently recomputed byte hash are used here instead.

## Required next gate

This producer episode cannot independently accept its own remediation. One fresh independently owned pre-gate review is mandatory against the exact terminal Issue #148 head/artifact identities. If that review is clean, the rights lane proceeds directly to formal `W2-REV-01`; optional review churn is not authorized.

Before terminal `STATUS(REVIEW_READY)`, an open draft PR from this exact branch to `main` must exist and follow the final branch head. The terminal Issue #148 status capsule is authoritative for final `head_sha`, final artifact blobs, and draft-PR binding.

No legal clearance, provider permission, release approval, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority is created. Any eventual `main` integration remains separately authorized and squash-only.