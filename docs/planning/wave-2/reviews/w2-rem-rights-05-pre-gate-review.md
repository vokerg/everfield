# W2-PG-REM-RIGHTS-05 — Independent review of Issue #148

**Mission:** `W2-PG-REM-RIGHTS-05` / Issue #159  
**Reviewed issue:** #148 / `W2-REM-RIGHTS-05`  
**Reviewed head/work:** `91545c6121a3cf071df524fd17e5e2978f7a65b2`  
**Reviewed PR:** #157, draft/open at the exact reviewed head  
**Reviewer actor/session:** `w2-pg-rem-rights-05-gpt56sol-20260813-1405`  
**Trust profile:** `DEGRADED_INDEPENDENT_FRESH_SESSION`; distinct from producer `w2-rem-rights-05-gpt56sol-20260813-1014`  
**Disposition:** `CHANGES_NEEDED`  
**Findings:** 0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR

## Exact input identity

The frozen Issue #148 packet is internally bound as declared:

- fixture Git blob `3318f773b675e1bc0c5e5b41064bb1a1a2db7eea`;
- report Git blob `d3793550c5a19d9ac7e88f029cefc689695b84f8`;
- producer disposition Git blob `819314d42689cd643a9063acd073784953a1342f`;
- handoff Git blob `57da948dfad5337cec51c0fa5fd27a9f604c2a81`;
- predecessor fixture Git blob `39fcdc292cd37661a061c6d3027715106b3a3d27`;
- predecessor exact-byte SHA-256 declared by the corrected packet `6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5`.

The historical Issue #142 source-SHA metadata discrepancy is preserved as historical metadata rather than rewritten. The exact predecessor Git blob remains the authoritative predecessor byte identity for this review.

## Adversarial attack results

### Duplicate derived-trigger closure

The bounded semantic correction is mechanically sound on the finding surface. The wrapper checks `material_triggers` only after requiring a list whose members all satisfy the predecessor `_closed_member` predicate; for that closed-string case it rejects non-unique lists before the predecessor can execute `set(material_triggers)`. Therefore every duplicated member of the six-value closed trigger domain returns exact `UNKNOWN / POLICY_UNRESOLVED` before any accepted derived state.

Malformed nested/list/dict/null/bool/number/unknown-string members do not enter that duplicate-set conversion. They fall through to the immutable predecessor `derive_state`, which first rejects a non-list or any member failing `_closed_member` before its `set(material_triggers)` operation. This preserves total, non-raising fail-closed behavior for the Issue #145 attack class. Valid unique trigger reorder remains non-authoritative because the wrapper does not alter the predecessor set semantics for unique closed members.

### Matrix and valid-domain preservation

The delta extends the inherited malformed-matrix accounting by exactly the six closed-domain duplicate-trigger cases, from 462 to 468, and retains the predecessor zero-uncaught-exception path. The full valid-domain audit implementation is in the exact immutable predecessor blob and is not patched by Issue #148; it exercises `compile_policy` over the 802,816 valid tuples, while the Issue #148 delta changes only `derive_state` duplicate-list handling. Thus the valid policy compilation domain, rule-order comparison, and audit payload are structurally unchanged by the correction.

This review did not substitute producer-reported output for independent authority: it inspected the exact frozen wrapper and predecessor validation/audit code and traced the changed call surface. No semantic regression was found in the bounded duplicate-trigger correction.

### Provenance/reconstruction attack

The packet fails one required reconstruction attack.

The exact #148 executable calls:

`git cat-file blob 39fcdc292cd37661a061c6d3027715106b3a3d27`

at import time. That predecessor blob is made reachable on the task branch by parent commit `7621f6fbf1b08d8ea6a904f8e3bf60ab53b5a898`, which imported the Issue #142 tree. The final #148 commit `91545c6121a3cf071df524fd17e5e2978f7a65b2` then replaces/removes those imported predecessor-tree files and retains only the delta capsule plus report/disposition/handoff.

Current `main@b5dd922b3170361403ee3fb02376febf737da5cc` does not contain `docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py`. Comparing current main to the frozen #148 head shows exactly four #148 additions: the delta fixture, report, disposition, and handoff; it does not retain the predecessor fixture as a tree artifact.

A squash integration of PR #157 records the resulting tree relative to main but does not make the task branch's imported parent commit part of main ancestry. Therefore a normal main-only checkout after that squash cannot rely on Git object `39fcdc...` being reachable. Object availability would depend on the continued existence/fetching of non-main task refs or server object retention, neither of which is a durable evidence contract.

Because a clean result under Issue #159 may authorize squash integration of #148 as noncanonical evidence, this defect is material: the very integration path unlocked by `CLEAN` can make the retained executable evidence non-reconstructable from the integrated packet.

## Finding

### `PG-REM5-RIGHTS-M01` — MAJOR — delta fixture is not self-contained across authorized squash integration

**Observed:** the #148 executable requires predecessor blob `39fcdc...` via `git cat-file`, while that blob is retained only through task-branch ancestry, not as an artifact in the packet's resulting tree/main history.

**Impact:** after squash integration, a main-only checkout is not guaranteed to possess the predecessor object, so the exact retained fixture can fail before executing T01–T16 or the audit. This breaks independent reconstruction of integrated noncanonical evidence and makes `CLEAN` unsafe.

**Bounded correction:** retain/content-bind the exact predecessor bytes in the corrected packet tree (or an equivalent self-contained immutable module/artifact) and make the top-level fixture execute without hidden branch-history/object reachability. Preserve all Issue #148 semantics and recompute exact identities.

**Routed successor:** Issue #162 / `W2-REM-RIGHTS-06`.

## Authority boundary and disposition

Disposition is **`CHANGES_NEEDED`**. Issue #148 is not accepted as clean W2 review input and is not authorized for evidence-provenance integration by this review. `PG-REM4-RIGHTS-M01` appears semantically repaired, but `PG-REM5-RIGHTS-M01` must be corrected and freshly independently reviewed before the rights lane proceeds to formal `W2-REV-01`.

This review grants no legal clearance, provider permission, release approval, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority. Negative review provenance may be retained only through a separately valid integration route.