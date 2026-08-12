# W2-CI-01 pre-gate review finding dispositions

**Remediation mission:** `W2-REM-CI-01` / Issue #91  
**Source mission:** `W2-CI-01` / Issue #77  
**Source frozen head/work:** `0011a9b02f1c7d8d20b81e0fb4faa6dec9bcae59`  
**Source report blob:** `7f9cb919c5e28299b7edbb1ea5495138d1509791`  
**Pre-gate review:** Issue #77 comment `5270075412`  
**Remediation claim:** Issue #91 comment `5270083695`  
**Corrected report path:** `docs/planning/wave-2/evidence/ci-reliability-experiment.md`  
**Formal independent review:** still `W2-REV-01`; this document is remediation provenance, not a `REVIEW_STATUS`.

## Disposition summary

| Finding | Severity | Disposition | Mechanical evidence |
|---|---|---|---|
| `PG-M01` quarantine replacement not evidence-bound | MAJOR | RESOLVED | exact quarantine requirement/policy/candidate; exact replacement-set equality; evidence-bearing replacement records; S7/S8/S9/S16 fail closed |
| `PG-M02` candidate/attempt identity absent across remediation episodes | MAJOR | RESOLVED | exact candidate/base in every envelope; append-only envelope chain; S11 rejects same-candidate root reset; S12 uses distinct successor candidate |
| `PG-m01` retention restoration lacks durable artifact episode | MINOR | RESOLVED | stable `artifact_id`; ordered availability events; S13/S14/S15 preserve loss/exact-restore/wrong-hash lineage |

No finding is waived, downgraded by assertion, or treated as resolved solely by prose.

## PG-M01 — RESOLVED

### Source defect

The frozen Issue #77 harness accepted quarantine replacement through truthiness of an arbitrary replacement mapping. It did not mechanically bind the exact replacement IDs, policy version, candidate, result, artifact identity, or current artifact integrity.

### Correction

The revised fixture defines quarantine as exact requirement `CI-EXP-REQ-v2-q1` under policy `ci-reliability-exp-v2-q1`, bound to `cand-flaky-v1` and the exact set `short_soak` + `static_invariant`.

Each replacement record must match:

- its required replacement ID;
- exact candidate ID;
- exact quarantine policy version;
- result `PASS`;
- exact required artifact key/ArtifactIdentity;
- current reachable artifact bytes at the expected content hash.

The evaluator requires replacement-key set equality before inspecting the records.

### Negative evidence

- S7: required replacement missing -> `INCONCLUSIVE`.
- S8: arbitrary replacement key -> `INCONCLUSIVE`.
- S9: exact IDs but wrong artifact binding -> `INCONCLUSIVE`.
- S16: exact IDs/artifacts but wrong policy -> `INCONCLUSIVE`.
- S10: otherwise-valid replacement after expiry -> `UNSATISFIED`.

Thus arbitrary booleans or partially matching replacement packets cannot mint satisfaction.

## PG-M02 — RESOLVED

### Source defect

The frozen Issue #77 harness had one base SHA but no exact candidate identity in attempts/envelopes. A later scenario described as a remediated candidate could begin with fresh PASS attempts without proving the candidate changed or retaining the prior negative episode.

### Correction

The revised fixture binds every envelope to exact `candidate_id` + `base_sha` and requires an append-only predecessor chain for multiple envelopes of one candidate. A second root/fork for the same candidate is invalid evidence and makes the aggregate `INCONCLUSIVE`.

The remediated case is a distinct successor:

- source: `cand-flaky-v1`;
- successor: `cand-flaky-v2`;
- declared `supersedes: cand-flaky-v1`.

### Negative/positive evidence

- S5: `cand-flaky-v1` retains FLAKY + later PASS -> `UNSATISFIED`.
- S11: another fresh root envelope for `cand-flaky-v1` -> `INCONCLUSIVE` with reset/fork reason.
- S12: distinct successor `cand-flaky-v2` with fresh exact evidence -> `SATISFIED`.

This makes candidate change a machine-visible prerequisite for escaping same-candidate negative history.

## PG-m01 — RESOLVED

### Source defect

The frozen retention scenarios were independent aggregate calls. Hash equality was checked, but there was no single durable artifact/evidence identity whose outage and restoration events were retained.

### Correction

The revised fixture uses stable ArtifactIdentity state with an ordered event list. The unit evidence uses one `artifact_id` throughout:

1. reachable at exact expected hash;
2. unreachable;
3. either reachable again at the exact expected hash or reachable at a wrong hash.

The result object retains the event lineage, so restoration is a transition of the same historical evidence identity rather than an unrelated fresh PASS input.

### Evidence

- S13: same artifact becomes unavailable -> `INCONCLUSIVE`.
- S14: same artifact exact-hash restoration -> `SATISFIED` with loss + restore events retained.
- S15: same artifact wrong-hash restoration -> `INCONCLUSIVE`.

## Exact corrected evidence identity

The corrected report embeds the executable reference harness and canonical digest functions.

- fixture digest: `2f07e41bccd8eef9e35ad7bc03e2aad7b6792a62cfc6d1560b933a814604c988`;
- harness-contract digest: `9963302d28ed3057a4e46070b462a91e45aebef6f57829569a3bafe57a53700a`;
- result-object digest: `b2905c4cf9095ba70c42770505073dc21d616996316f2dc800293d78ca8ea057`.

The harness contract digest is over the explicit canonical `HARNESS_IDENTITY` object, not source whitespace. Re-execution of the exact embedded appendix reproduces all three values and the 16-scenario aggregate matrix.

## Remediation self-review

Against Issue #91 acceptance criteria and only the declared remediation scope:

- unresolved BLOCKER: 0;
- unresolved MAJOR: 0;
- correction-requiring MINOR: 0;
- `PG-M01`: mechanically resolved;
- `PG-M02`: mechanically resolved;
- `PG-m01`: mechanically resolved;
- required `NOT_RUN` versus `NOT_APPLICABLE`: preserved;
- PRODUCT/INFRA/FLAKY lineage semantics: preserved;
- quarantine expiry: preserved;
- provider-specific mechanics: still explicitly unverified/noncanonical;
- production/readiness authority leakage: none identified.

A self-review provenance defect in the first remediation draft was also corrected before terminalization: the report no longer publishes a source-format-dependent harness hash. Its harness digest now has an explicit canonical preimage and is reproduced by Appendix A.

## Authority limits and next gate

These dispositions make the corrected Issue #91 payload a cleaner substantive input for later review; they do not independently validate the broader CI design, provider enforcement, INFRA classification, replacement adequacy, or production readiness.

`W2-REV-01` remains the required formal independent adversarial review after its complete Wave-2 prerequisite set becomes eligible. No implementation-readiness blocker is closed here, and no canonicalization is claimed.
