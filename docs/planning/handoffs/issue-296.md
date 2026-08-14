# Issue #296 handoff — W2-REM-ACC-13

## Ownership and immutable inputs

- Winning claim: `5294479716`
- Branch: `planning/issue-296`
- Base: `ea7d085fd38d90658abe23ef0b315b786c6c80b4`
- Substantive remediation work head before handoff: `a4583455d12dd922166c40b5709b3c043b0ac86a`
- Canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Source review: Issue #293 claim `5294404386`, terminal `5294463445`, head `dd4ec050025d4321d9e2a0b73b0ecbc6fdc920e3`, work `247e785b20f0cdad7e78d9501e86e7450432bf3e`
- Finding: `W2-REV-ACC15-M01 / SOURCE_LOGICAL_OPERATOR_WEAKENING_AND_INCOMPLETE_VALIDATOR_ORACLE`
- Immutable policy v11 input blob: `b57c0aae729085c672ae9746179d76afb866a721`
- Immutable report v11 input blob: `cb6b2ba3d1226c912874a89a369e9acf7912a034`
- Candidate policy v12 blob: `4c10dc8969a8080a14e8f46e0d2e126bd8a1ee5e`
- Candidate report v12 blob: `197a20ec3fd3cd859c4e7d96e51f7337ea7583d3`

## Completed bounded remediation

The exact inherited `XAG115-PERMANENT-ACTION-CONFIRM-OR-UNDO` identity is preserved, but its weakened `review OR confirmation OR undo` semantic is replaced with an explicit machine-readable conjunction:

```yaml
permanent_or_destructive_action_protection:
  all_of:
    - review_available_for_action
    - confirmation_available_for_action
    - undo_available_for_action
```

The v12 validator/oracle surface rejects none, each one-of-three, and every two-of-three capability set and accepts only review + confirmation + undo. This closes the exact acceptance-affecting logical weakening identified by Issue #293 without renaming or widening the atom.

## Preservation boundary

The packet explicitly freezes:

- exact reviewed v11 `XAG115-DATA-MODIFICATION-REVIEW-CORRECT-REVERSE` semantics `(review AND correct) OR complete_reverse_or_cancel` and all four reviewed witnesses;
- separate `XAG115-NO-BUTTON-HOLD-DESTRUCTIVE-CONFIRMATION` semantics unchanged;
- reviewed XAG 112 corrections;
- reviewed XAG 114 title-exception correction;
- reviewed XAG 116 default-over-20-hours correction;
- exact inventory counts: XAG 112 = 14, XAG 114 = 16, XAG 108–123 = 113, inherited XAG 101–107 = 105, composed XAG 101–123 = 218;
- all evidence/gap routing and fail-closed aggregate state.

No identity is added, removed, split, or renamed.

## Producer disposition

`W2-REV-ACC15-M01` is `RESOLVED_PENDING_FRESH_SCOPED_REVIEW` in producer provenance only.

Bounded producer self-review finds 0 unresolved BLOCKER, 0 unresolved MAJOR, and 0 correction-requiring MINOR in this exact remediation scope. That self-review does not satisfy the independent-review gate.

## Required scoped review route

Issue #299 / `W2-REV-ACC-16` is the required scoped review route. It was created `BLOCKED_PENDING_PRODUCER_TERMINAL` and must bind the exact terminal Issue #296 head/work, v12 policy/report blobs, and exact-head draft PR before claimability.

The review must independently attack:

1. current first-party XAG 115 conjunction semantics;
2. all one-of-three and two-of-three rejection witnesses plus the complete three-of-three PASS witness;
3. exact preservation of the reviewed v11 stored-data operator and four witnesses;
4. separation/preservation of the no-button-hold record;
5. inventory, evidence/gap routing, and fail-closed authority state.

Even a clean #299 review does not accept the separate XAG 115 button-hold surface or XAG 116–123; the required full mapping review must resume after any separately authorized integrations.

## Fail-closed state

- empirical accessibility: `NOT_RUN`
- empirical successor eligible: `false`
- `mapping_complete: false`
- `IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN`
- `W2-REV-M02: OPEN_BOUNDED`
- full corrected XAG 108–123 review complete: `false`
- production/readiness/release authority: `false`
- legal/compliance claim: `false`
- platform certification: `false`
- verification-PASS authority: `false`
- producer integration authority: `false`
- decision authority: `false`
- canonicality: `NOT_CANONICAL`

## Terminal lifecycle

Open an exact-head draft PR from `planning/issue-296` to `main`, verify PR head/base and changed-file scope, then publish terminal schema-3 `STATUS(REVIEW_READY)` for Issue #296 with exact v12 blobs, work/head SHAs, finding state, and required review Issue #299. Any later integration is separately authorized and squash-only.