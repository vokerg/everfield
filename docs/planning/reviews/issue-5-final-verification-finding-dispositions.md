# Issue #5 Final Verification Finding Dispositions

**State:** REVIEWED-CANDIDATE SUPPORT  
**Remediation issue:** #16  
**Candidate:** `docs/planning/11-planning-program-v1-bootstrap-final-candidate.md`  
**Manifest:** `docs/planning/11-planning-program-v1-canonicalization-manifest.yaml`

## Disposition

| Finding | Severity | Disposition | Correction |
|---|---|---|---|
| V5-B08 | BLOCKER | ACCEPTED_AND_CORRECTED | Adds generic schema-3 `VERIFICATION_RESTART` for changed candidate/manifest after terminal verification and `VERIFICATION_REFRESH` for unchanged-candidate base drift after PASS. Both serialize ownership and require full verification evidence; Issue #6 selects only the highest valid exact-current-base PASS for the effective candidate tuple. |

## Why two transitions are required

The defect had two materially different causes that must not share a shortcut:

- **Candidate changed:** prior verification says nothing authoritative about the new payload. `VERIFICATION_RESTART` acquires a new fenced verification episode and mandates full normal verification.
- **Candidate unchanged, base changed:** the prior candidate judgment may still be relevant but its base binding is stale. `VERIFICATION_REFRESH` exists only to acquire a new fenced episode; it still mandates the full required cold-start/adversarial suite against the new base.

This separation prevents a candidate edit from masquerading as a lightweight compatibility check.

## V5-B08 regression scenario

```text
PASS(C,A)
main advances A -> B
Issue #6 current-base selection finds no PASS(C,B)
VERIFICATION_REFRESH(source=PASS(C,A), new_base=B)
lowest valid contender owns
full evidence rerun
  PASS(C,B) -> Issue #6 eligible while main==B
  FAIL(C,B) -> bounded remediation
```

If main advances again to `D`, repeat refresh from the latest valid PASS for the unchanged tuple. If candidate changes to `C2`, refresh is invalid; restart/full verification is required.

## Current bootstrap re-entry scenario

The current Issue #5 source result is formal schema-3 FAIL comment `5244679631`, which verified the Issue #14 candidate. Issue #16 changes candidate/manifest identity, so after Issue #16 provenance integration:

1. `VERIFICATION_RESTART` references source comment `5244679631`;
2. new payload is the exact Issue #16 candidate/manifest on current main;
3. `new_verified_base_main_sha` equals that current main;
4. contenders bind source/new tuple/base/current Issue #5 branch head; lowest valid comment ID wins;
5. winner becomes current owner and performs full verification;
6. final `BOOTSTRAP_VERIFICATION_STATUS` binds the Issue #16 tuple/base and ordinary independence/evidence profile.

The old one-time `BOOTSTRAP_RESUME` remains provenance and is not reused.

## Ownership and result safety

Both new transitions are ownership grants, not result assertions. They do not bypass:

- current branch-head mutation fencing;
- current-owner terminal-result fencing;
- report/simulation evidence requirements;
- FULL or `DEGRADED_SINGLE_AGENT` independence profiles;
- zero BLOCKER/MAJOR requirement for PASS;
- exact candidate/manifest/adopted-Wave1 tuple binding;
- exact current-main base requirement for Issue #6;
- squash-only integration.

Competing restart/refresh contenders use the same deterministic lowest-comment-ID winner rule and exact source/head binding used elsewhere in the protocol.

## Composition safety

The Issue #16 candidate does not restate the complete reviewed base model. It composes exact Issue #14 blobs with explicit section/path operations. Base candidate Sections 1, 24, and 25 are excluded so non-canonical bootstrap status/downstream instructions cannot leak into the future canonical wrapper. Base manifest modifications are expressed as replace/extend/append operations against immutable blob `1f062de59afcfe8496b4cff0fdff594c2d5fd50c`; unresolved target/key collisions fail verification.

## Preserved findings

V5-B03 through V5-B07 remain accepted/corrected through immutable base adoption:

- durable ancestry/blob canonical binding;
- one PLANNING phase across root entry docs;
- executable bootstrap Issue #5/#6 schema-3 bridge;
- typed/current-owner-fenced status results;
- explicit degraded single-agent liveness mode.

## Remaining risks / reopen conditions

- Repeated base movement may create verification churn; if observed, scheduler-level integration locks or a stronger transactional control plane should be evaluated.
- `DEGRADED_SINGLE_AGENT` remains weaker than isolated independent contexts and must reopen when stronger execution isolation becomes available.
- Procedural Git expected-parent fencing should later be strengthened by machine-enforced control-plane primitives.

None of these risks permits skipping current verification or Issue #6 terminal activation.

## Verification readiness

V5-B08 is corrected in the Issue #16 candidate/manifest. The next required step is Bootstrap Issue #5 full re-verification of the exact Issue #16 work state and then-current main. Issue #6 remains blocked until PASS.