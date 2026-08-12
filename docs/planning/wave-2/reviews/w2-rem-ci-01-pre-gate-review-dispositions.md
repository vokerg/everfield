# W2-REM-CI-02 — Issue #97 pre-gate review finding dispositions

**Remediation mission:** `W2-REM-CI-02` / Issue #99  
**Frozen predecessor remediation:** Issue #91 @ `0a256ae79880c759bcd698160adaaf3b302426d1`  
**Independent review input:** Issue #97 @ `091221bf92699910a01775b4368a7618106f5e14`  
**Review artifact:** `533d4192fecf3e550e57ca630fcea79b9ae17326`  
**Formal aggregate review:** still `W2-REV-01`; this file is remediation provenance only.

## Disposition summary

| Finding | Severity | Disposition | Mechanical evidence |
|---|---|---|---|
| `PG-REM-CI-M01` replacement evidence lacks durable ArtifactIdentity/result reconstruction | MAJOR | RESOLVED | v3 `ReplacementEvidenceRecord`; exact records retained in published result; S7/S8 fail omitted/wrong `artifact_id` |
| `PG-REM-CI-M02` successor candidate does not validate predecessor lineage | MAJOR | RESOLVED | v3 `CandidateTransitionRecord` + recomputed predecessor evidence root; S11-S13 fail missing/wrong/same-candidate transition |
| `PG-REM-CI-M03` retention result strips artifact identity/hash | MAJOR | RESOLVED | full `artifact_identity_lineage` retained; S16/S17 fail identity/hash substitution with identical event history |

No finding is waived or resolved by prose alone.

## PG-REM-CI-M01 — RESOLVED

The predecessor harness accepted replacement records that identified only the replacement/candidate/policy/result/artifact key, then looked up ArtifactIdentity from evaluator-global state. The published aggregate also discarded those replacement records.

V3 requires exact `replacement_evidence_id`, replacement ID, candidate, quarantine requirement and policy, result, artifact key, `artifact_id`, authoritative `expected_hash`, source envelope, and provenance. The validator compares the submitted record to the exact policy and retained artifact identity state. The published result object retains the exact records.

Negative evidence:

- S7: omitted `artifact_id` → `INCONCLUSIVE`;
- S8: wrong `artifact_id` → `INCONCLUSIVE`.

The positive S6 record is fully reconstructable from Appendix A of the corrected report.

## PG-REM-CI-M02 — RESOLVED

The predecessor harness declared `cand-flaky-v2.supersedes = cand-flaky-v1`, but admission never consumed that relation. A new candidate could therefore start a fresh root and satisfy without proving why it was the successor to the failed predecessor.

V3 introduces an exact `CandidateTransitionRecord` and requires:

- predecessor candidate `cand-flaky-v1`;
- successor candidate `cand-flaky-v2`;
- immutable changed-work identity and reason;
- exact predecessor evidence root;
- supplied predecessor envelope chain whose canonical root independently recomputes to the declared value.

Positive/negative evidence:

- S10 valid exact transition/root → `SATISFIED`;
- S11 missing transition → `INCONCLUSIVE`;
- S12 wrong predecessor → `INCONCLUSIVE`;
- S13 same candidate masquerade → `INCONCLUSIVE`.

The exact transition and observed root are retained in the published result object.

## PG-REM-CI-M03 — RESOLVED

The predecessor result retained only artifact event lists, even though evaluator memory separately knew stable identity and authoritative hash. A downstream consumer could not reconstruct which artifact the events belonged to.

V3 publishes and validates one complete record per retained artifact:

- stable `artifact_id`;
- authoritative `expected_hash`;
- ordered availability/integrity events.

Negative reconstruction evidence:

- S16 replays exact restoration events under another artifact ID → `INCONCLUSIVE`;
- S17 replays exact restoration events under another authoritative hash → `INCONCLUSIVE`.

S15 restores `SATISFIED` only for the original identity and hash.

## Regression self-review

The corrected v3 fixture also preserves the semantics Issue #97 judged clean:

- required conditional `NOT_RUN` remains gating: PASS;
- PRODUCT failure retention: PASS;
- explicitly permitted INFRA retry: PASS;
- explicit FLAKY remains gating: PASS;
- exact quarantine replacement-set requirement: PRESERVED;
- quarantine expiry/wrong-policy fail-closed rule: PRESERVED by unchanged v3 policy contract;
- same-candidate reset/fork rejection: PASS;
- retention loss reopens authority: PASS;
- provider/INFRA-classification/production/readiness/canonicalization authority: NOT CLAIMED.

## Authority and next gate

This disposition closes only Issue #97's three MAJOR findings for the bounded synthetic CI evidence contract. It does not prove provider implementation, replacement semantic equivalence, correct INFRA classification, or production storage durability.

The corrected Issue #99 packet may supersede Issue #91 as the substantive CI remediation input after terminal `STATUS(REVIEW_READY)`. Formal aggregate independent review remains `W2-REV-01`.