# W2-REM-CI-03 — Issue #101 finding dispositions

**Remediation mission:** `W2-REM-CI-03` / Issue #102  
**Frozen substantive predecessor:** Issue #99 @ `7cbfddf90d885c4fe2b1dd6433f6157a9453b0e0`  
**Independent review input:** Issue #101 @ `b0a09ebdb03c8bd8390d08d54f7d312eeb08ffa1`  
**Review artifact:** `7cef42ea12aea65c886a25a5d79e7359aed0bee1`  
**Formal aggregate review:** still `W2-REV-01`; this file is bounded remediation provenance only.

## Disposition summary

| Finding | Severity | Disposition | Mechanical evidence |
|---|---|---|---|
| `PG-REM-CI2-M01` frozen packet did not publish executable validator/corpus | MAJOR | RESOLVED | exact validator Git blob `436eb437051c1acc6a813fd66b152b09e4300c46`; self-bound source digest `sha256:97a8fa00d338907e32cd97a7ca662b81ea1fc8336ffd7a9e6541b00162c91b5d`; S1-S22 execute and result digest reproduces |
| `PG-REM-CI2-M02` predecessor root not independently reconstructable | MAJOR | RESOLVED | embedded exact predecessor-evidence artifact + canonical root algorithm; artifact/root `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`; S22 double-root substitution fails closed |

No finding is waived or resolved by prose alone.

## `PG-REM-CI2-M01` — RESOLVED

Issue #99 authenticated three JSON declarations but did not freeze the executable mapping from fixture to result. Issue #102 publishes `docs/planning/wave-2/evidence/ci-reliability-validator.py` as the exact standard-library-only executable and embeds the complete corpus inside that file.

The source is bound two ways:

1. repository Git blob `436eb437051c1acc6a813fd66b152b09e4300c46` fixes the exact repository bytes;
2. the validator recomputes `sha256-source-with-digest-line-sentinel-v1` before evaluation and requires `sha256:97a8fa00d338907e32cd97a7ca662b81ea1fc8336ffd7a9e6541b00162c91b5d`.

The self-identity digest is included in the emitted harness contract and result object. The source-identity mechanism normalizes only the digest-value declaration to a fixed sentinel, avoiding self-reference while making every other source byte authoritative. A byte-tamper attack outside that field was executed and failed nonzero before fixture evaluation.

The validator derives all aggregates through generic requirement/quarantine/reset/transition/retention functions and compares them to the frozen expected map before emitting evidence. Successful execution reproduced:

- fixture manifest: `sha256:08d009ef6648366835bd2f2c3866572b73b00510c924460471210c10acb20701`;
- fixture cases: `sha256:dd7273115702957d9c6c60f1902ca77e7d012a87189142fe102d369cf34ae97f`;
- harness contract: `sha256:a2a0e914060c1d6dab233763e53acb7f462a33a53e4f5b57c3a046cee840c923`;
- result object: `sha256:87fbf99c40a0a93580cb82b7be8b2a1691844976197378a97eacb915af47c5e0`.

The predecessor S1-S17 coverage remains executable. New regressions close the exact review gap:

- S18: quarantine at expiry boundary → `INCONCLUSIVE`;
- S19: missing replacement-set member → `INCONCLUSIVE`;
- S20: extra replacement-set member → `INCONCLUSIVE`;
- S21: wrong replacement member identity → `INCONCLUSIVE`.

This is executable evidence for the declared behavior, not a semantic-name-only harness descriptor.

## `PG-REM-CI2-M02` — RESOLVED

Issue #99 retained matching declared/observed predecessor-root strings without retaining the evidence needed to recompute them. Issue #102 embeds and emits an exact `predecessor-evidence-v1` artifact containing predecessor candidate, envelope/check/attempt identities, ordered attempt data, results/failure classes, artifact identities, and authoritative hashes.

The transition now binds:

- exact predecessor and successor candidates;
- exact changed-work identity and reason;
- transition ID;
- predecessor evidence artifact digest;
- root algorithm `sha256-canonical-json-sorted-compact-v1`;
- predecessor evidence root.

The validator recomputes the artifact digest and root from the exact embedded bytes and rejects a transition unless both producer-facing root fields equal that recomputed value and all identity relations are coherent.

Exact predecessor artifact digest/root: `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`.

S22 performs the required counterexample: it substitutes both the transition's declared root and the case's claimed-observed root with the same false all-zero value while leaving predecessor evidence bytes fixed. The derived result is `INCONCLUSIVE` because the recomputed root does not change.

The emitted result object retains the predecessor evidence artifact, its digest, the transition, root algorithm, and recomputed root, making later reconstruction independent of producer prose.

## Preserved behavior self-review

The corrected v4 executable corpus was checked for the behavior Issue #102 requires not to regress:

- `CONDITIONALLY_REQUIRED` → `REQUIRED` / `NOT_APPLICABLE`: PASS;
- required `NOT_RUN` gates: PASS;
- PRODUCT failure cannot be laundered by later PASS: PASS;
- explicitly permitted all-INFRA retry may satisfy: PASS;
- explicit FLAKY remains gating: PASS;
- exact quarantine replacement-set equality: PASS;
- quarantine expiry at declared boundary: PASS;
- same-candidate second root/reset rejected: PASS;
- replacement evidence exact identity/ArtifactIdentity/hash binding: PASS;
- retained artifact stable identity/hash/event binding: PASS;
- retention loss and identity/hash substitution reopen authority: PASS;
- CI provider / universal INFRA classifier / production / readiness / implementation / integration / canonicalization authority: NOT CLAIMED.

Self-review result: `0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR` in Issue #102 scope.

## Residual risks and next gate

This synthetic evidence still does not prove correct real-provider INFRA classification, semantic equivalence of replacement checks, complete real evidence acquisition, append-only backend enforcement, production retention guarantees, or provider/account/policy stability.

Those risks remain downstream evidence/review obligations. This remediation remains noncanonical and cannot authorize production or implementation readiness.

After exact Issue #102 `STATUS(REVIEW_READY)`, use this payload as the substantive corrected CI input for later `W2-REV-01`. Preserve Issues #77/#91/#97/#99/#101 as immutable provenance. Formal aggregate independent review remains `W2-REV-01`.