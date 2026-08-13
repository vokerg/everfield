# W2-PG-REM-CI-02 — Independent pre-gate review of successor CI remediation

**Review mission:** `W2-PG-REM-CI-02` / Issue #101  
**Reviewed remediation:** `W2-REM-CI-02` / Issue #99  
**Reviewed work/head:** `7cbfddf90d885c4fe2b1dd6433f6157a9453b0e0`  
**Reviewed report blob:** `0d821317792fd1be06bf56c51ceee09f7e72c549`  
**Reviewed disposition blob:** `b992ea5a6929575f619557a03bed730d973de1f3`  
**Reviewed handoff blob:** `2f468bfc8e657eaf3530222783f43ec34a1e7020`  
**Source independent review:** Issue #97 work/head `091221bf92699910a01775b4368a7618106f5e14`, artifact `533d4192fecf3e550e57ca630fcea79b9ae17326`  
**Result:** `CHANGES_NEEDED`  
**Severity:** `0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR`

## 1. Scope and authority

This is a bounded independent pre-gate review of the exact frozen Issue #99 remediation payload. It does not edit or re-own `planning/issue-99`, does not replace the required aggregate `W2-REV-01`, and creates no CI-provider, universal-INFRA-classifier, production, readiness, integration, or canonicalization authority.

The review attacked the durable v3 packet rather than accepting Issue #99's remediation prose or self-review. Issue #97 is used as immutable provenance for the three defects Issue #99 claims to close.

## 2. Attack plan executed

1. Reconstructed the exact Appendix A fixture manifest, harness-contract descriptor, and result object and independently recomputed their declared canonical compact-JSON SHA-256 digests.
2. Inspected the exact Issue #99 branch delta from base `c7ba185ed9667b717794c19eaa0834ca41aa4c78` to reviewed work `7cbfddf90d885c4fe2b1dd6433f6157a9453b0e0` and the full reviewed tree for an executable v3 validator or immutable validator reference.
3. Traced replacement-evidence fields through the published S6/S7/S8 durable objects and the stated exact replacement-set/expiry regression claims.
4. Traced successor transition evidence through the published fixture transition, S10 transition object, and `S10_predecessor_evidence_root_observed`.
5. Compared S15/S16/S17 retained-artifact records to confirm the identity/hash substitution objects really preserve the event list while changing only the attacked identity field.
6. Rechecked authority boundaries and the preserved `NOT_RUN`, PRODUCT, INFRA, FLAKY, same-candidate reset, and retention-loss declarations.

## 3. Reproduced evidence that passes

The three Appendix A digests reproduce exactly under JSON sorted keys plus compact separators:

- fixture manifest: `8068cbc8563faf1c91c983b85baaa25be443236da3cd3980c1c27952d90c14ae`;
- harness-contract descriptor: `fe185e57a52b16c4c14fea1ab7c34bfe2198ef835cb244c3ebed89ffcafecfa5`;
- published result object: `dd171542b1b00b94f8e679cd40e575a0b826df410b0d82216b497f5794da07e6`.

The durable S6 replacement records do contain replacement-evidence identity, replacement ID, candidate, requirement, policy version, result, artifact key, stable artifact ID, expected hash, source-envelope ID, and provenance. S7/S8 are declared `INCONCLUSIVE` for omitted/wrong artifact ID.

The retained-artifact substitution objects are structurally correct: S15 uses the original `artifact_id` and authoritative hash, S16 replays the same three events under `art-swapped`, and S17 replays the same events under a substituted expected hash. Their declared aggregates are respectively `SATISFIED`, `INCONCLUSIVE`, and `INCONCLUSIVE`.

The packet also keeps provider implementation, INFRA-classification authority, production/readiness, integration, and canonicalization explicitly out of scope.

These passes establish integrity of the published declarations. They do not establish that the declarations were produced by the claimed v3 evaluator.

## 4. Findings

### PG-REM-CI2-M01 — MAJOR — the frozen payload does not publish the validator that supposedly enforces the v3 semantics

Issue #99's required corrections are validator-level requirements: replacement ArtifactIdentity bindings must be enforced, successor lineage must be validated, identity-substitution fixtures must fail, and the previously-correct applicability/retry/quarantine semantics must not regress. The reviewed report says that a v3 evaluator was executed and publishes aggregate verdicts, but the frozen payload contains no executable evaluator, validator source, immutable validator artifact reference/digest, or deterministic executable specification from which those verdicts can be reproduced.

The exact branch comparison is four commits ahead of base and adds only:

- `docs/planning/wave-2/evidence/ci-reliability-experiment.md`;
- `docs/planning/wave-2/reviews/w2-rem-ci-01-pre-gate-review-dispositions.md`;
- `docs/planning/handoffs/issue-99.md`.

The full reviewed tree contains no separate v3 CI validator artifact. Appendix A contains input/descriptor/result JSON, not the function that maps input to result. The harness-contract digest therefore authenticates only six semantic-name strings; it does not authenticate executable enforcement logic.

This creates a mechanical counterexample to the claimed closure route: a producer can alter the hidden evaluator to return the same published S1-S17 labels, or hand-author those labels, while leaving all three published digests unchanged. A reviewer can prove that the JSON has not changed, but cannot prove that omitted/wrong ArtifactIdentity, a bad transition, an expired quarantine, or a replacement-set mismatch actually causes the stated result.

There is also no published v3 result case for quarantine expiry or wrong/missing/extra replacement-set membership even though Issue #99 explicitly requires those previously-correct behaviors not to regress. The disposition labels them `PRESERVED`, but the frozen packet gives no executable or result-level evidence for that claim.

**Required correction:** publish a deterministic engine/provider-independent validator or an exact immutable validator artifact/ref plus complete runnable fixture corpus. Bind its source/content identity into the harness contract and result evidence. The runnable corpus must include the current S1-S17 cases plus explicit quarantine-expiry and replacement-set mismatch regressions. A fresh reviewer must be able to execute or mechanically evaluate the exact frozen validator and reproduce the published result-object digest from the frozen inputs without trusting prose.

### PG-REM-CI2-M02 — MAJOR — predecessor evidence lineage is not reconstructable from the durable S10 transition proof

Issue #99 claims that the evaluator reconstructs the predecessor envelope chain, recomputes its evidence root, and compares it to the transition record. The durable result publishes:

- `S10_candidate_transition.predecessor_evidence_root = ef6222db...31442`; and
- `S10_predecessor_evidence_root_observed = ef6222db...31442`.

However, neither the Appendix A fixture manifest nor the published result object contains the predecessor evidence-envelope chain, an immutable repository/artifact reference to that chain, a digest-bound envelope manifest, or the canonicalization/version rule needed to recompute that root. The S6 records contain only the dangling string `source_envelope_id: env-flaky-1`; no immutable envelope object/ref is retained.

Consequently the published transition proof is self-consistent but not independently reconstructable. A producer can substitute both the declared predecessor root and the `observed` root with the same arbitrary value while leaving no durable predecessor evidence against which the substitution can be detected. That is exactly the evidence-root substitution attack Issue #101 requires this review to perform.

This does not satisfy the review acceptance requirement that predecessor transition/evidence lineage be reconstructable from the corrected durable result objects. It also prevents an independent reviewer from verifying the claimed changed-work/predecessor-evidence binding even if M01's validator were supplied later.

**Required correction:** retain the exact predecessor evidence-envelope chain in the result packet or retain a content-addressed immutable reference whose bytes and canonical-root algorithm/version are available to the reviewer. The transition result must bind that artifact/ref, the recomputed root, predecessor candidate, successor candidate, changed-work identity, and transition ID. Add a negative fixture that changes the declared/observed root together while holding the predecessor evidence artifact fixed; it must fail.

## 5. Regression and authority assessment

No additional correction is required from the published durable objects for these bounded observations:

- the declared `NOT_RUN` / `NOT_APPLICABLE` distinction remains visible;
- PRODUCT failure retention, permitted INFRA retry, FLAKY gating, same-candidate reset rejection, and retention loss/restoration all have explicit scenario labels;
- exact replacement evidence fields and retained artifact identity/hash/event records are materially stronger than Issue #91's reviewed packet;
- S16/S17 are correctly constructed as identity/hash substitution attacks;
- no provider, production, readiness, integration, or canonicalization authority is claimed.

These are not sufficient to clear M01/M02 because the remaining defects sit at the validator/provenance boundary needed for independent reconstruction.

## 6. Disposition

`CHANGES_NEEDED` before Issue #99 should be treated as a clean substantive CI input to `W2-REV-01`.

The frozen Issue #99 `STATUS(REVIEW_READY)` remains immutable provenance. Do not edit `planning/issue-99`. Route `PG-REM-CI2-M01` and `PG-REM-CI2-M02` together to one bounded remediation successor that recreates the corrected noncanonical payload on a new branch, publishes an exact executable validator/corpus, and closes the predecessor-evidence reconstruction gap.

Formal `W2-REV-01` remains the only declared aggregate independent review authority. This pre-gate result does not authorize integration, implementation, readiness, or canonicalization.
