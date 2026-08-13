# W2-REM-CI-03 — Executable CI evidence and predecessor-lineage remediation

**Source producer:** `W2-CI-01` / Issue #77 @ `0011a9b02f1c7d8d20b81e0fb4faa6dec9bcae59`  
**Prior remediations:** Issue #91 @ `0a256ae79880c759bcd698160adaaf3b302426d1`; Issue #99 @ `7cbfddf90d885c4fe2b1dd6433f6157a9453b0e0`  
**Independent predecessor review:** `W2-PG-REM-CI-02` / Issue #101 @ `b0a09ebdb03c8bd8390d08d54f7d312eeb08ffa1`  
**Review artifact:** `7cef42ea12aea65c886a25a5d79e7359aed0bee1`  
**Current remediation:** `W2-REM-CI-03` / Issue #102  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authority:** bounded noncanonical planning evidence only; formal aggregate adversarial review remains `W2-REV-01`.

## 1. Scope and non-goals

Issue #101 found two MAJOR evidence-boundary defects in the frozen Issue #99 packet:

1. `PG-REM-CI2-M01`: the packet authenticated fixture/descriptor/result declarations but did not publish the executable validator that supposedly mapped those inputs to those results; quarantine-expiry and replacement-set mismatch regressions were also not executable evidence.
2. `PG-REM-CI2-M02`: the successor transition published a declared predecessor root and matching observed root without the predecessor evidence bytes or root algorithm needed to reconstruct the root independently.

This remediation replaces only those defective boundaries with `ci-reliability-reference-v4`. It preserves the already-correct replacement `ArtifactIdentity`, retained-artifact identity/hash, applicability, retry, quarantine, reset, and authority semantics from the predecessor packet.

Non-goals remain unchanged: this packet does not select a CI provider, define a universal INFRA classifier, prove production storage durability, authorize gameplay implementation, make an implementation-readiness decision, authorize integration, or canonicalize any planning artifact.

## 2. Exact executable validator and corpus

The exact validator and complete synthetic corpus are one frozen repository artifact:

- path: `docs/planning/wave-2/evidence/ci-reliability-validator.py`;
- Git blob: `f872f8082592be8e2f067fdf4772034d25483c5e`;
- validator version: `ci-reliability-reference-v4`;
- dependencies: Python standard library only;
- source identity algorithm: `sha256-source-with-digest-line-sentinel-v1`;
- declared/recomputed source identity: `sha256:96a016c998d4b1af30f2a1803c6723cdfbad64d6ad23e9ed2b3e83f5a5e5f346`.

The source identity algorithm reads the exact source bytes, replaces only the `VALIDATOR_SOURCE_DIGEST = "..."` declaration with the fixed sentinel `__SOURCE_DIGEST__`, and hashes the resulting UTF-8 bytes. The validator recomputes this identity before evaluating any fixture. This avoids a self-referential hash while still making every executable byte outside the single digest-value field content-addressed. The exact Git blob provides the ordinary repository content identity in addition to that executable self-check.

The validator embeds the complete fixture manifest, all synthetic scenario inputs, the predecessor evidence artifact, the canonicalization/root algorithm identifier, expected aggregate outcomes, and the evaluator functions. The published result object is derived in memory by executing those functions; it is not a hand-authored oracle.

A fresh reviewer can run:

`python3 docs/planning/wave-2/evidence/ci-reliability-validator.py`

The process exits nonzero if source identity mismatches or if any derived scenario aggregate differs from the frozen expected map. On success it emits the canonical fixture, harness contract, result object, and their digests as JSON.

## 3. Canonical serialization and evidence identities

Canonical structured-object digests use UTF-8 JSON with sorted keys and compact separators under `sha256-canonical-json-sorted-compact-v1`.

Exact successful execution produced:

- validator source identity: `sha256:96a016c998d4b1af30f2a1803c6723cdfbad64d6ad23e9ed2b3e83f5a5e5f346`;
- fixture-manifest digest: `sha256:08d009ef6648366835bd2f2c3866572b73b00510c924460471210c10acb20701`;
- fixture-cases digest: `sha256:cfef6f1dfe721504480b6a7f3d6983edeae3f335a507b547511773f0543a97fe`;
- harness-contract digest: `sha256:1a9a14a261047cefdcded2be739af3659b70329fecfa2e8df12a92e47fceb475`;
- result-object digest: `sha256:7b0a8659b0c505bdca1f4cbc2b62e2e9b03d4031b05a01dc1ecb543cf4bb8438`;
- predecessor-evidence artifact digest: `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`;
- predecessor-evidence root: `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`.

The harness contract contains the exact validator source identity and identity algorithm, so the harness digest changes when the executable source identity changes. The result object also retains the validator source identity.

## 4. Reconstructable predecessor evidence lineage

The former dangling `source_envelope_id: env-flaky-1` boundary is replaced by a durable `predecessor-evidence-v1` artifact embedded byte-for-byte in the validator corpus and emitted in the result object. It contains:

- exact predecessor candidate `cand-flaky-v1`;
- exact evidence-envelope IDs;
- requirement/check identities;
- ordered attempt identities and ordinals;
- results/failure classes;
- exact artifact keys, `ArtifactIdentity`, and authoritative hashes.

The transition binds the exact expected values for:

- `transition_id`;
- predecessor candidate;
- successor candidate;
- changed-work identity;
- remediation reason;
- predecessor evidence artifact digest;
- root algorithm version;
- predecessor evidence root.

`sha256-canonical-json-sorted-compact-v1` computes the predecessor evidence root directly from the exact embedded predecessor artifact. The validator recomputes the artifact digest and root, requires the artifact digest to equal the frozen predecessor artifact rather than merely a producer-updated digest, and requires every transition identity field to equal the frozen transition contract. It separately checks the claimed observed root against the recomputed value.

The result object retains the exact predecessor artifact, artifact digest, transition, algorithm, and recomputed root, so a reviewer can reconstruct the proof without trusting a producer-provided matching pair of root strings.

## 5. Executed regression corpus

All 26 exact cases are evaluated by generic contract functions rather than a scenario-ID switch.

| ID | Attack / condition | Derived aggregate | Required property |
|---|---|---|---|
| S1 | required baseline PASS | `SATISFIED` | required evidence passes |
| S2 | conditional requirement applies but is `NOT_RUN` | `UNSATISFIED` | `NOT_RUN` is not `NOT_APPLICABLE` |
| S3 | PRODUCT FAIL followed by PASS | `UNSATISFIED` | retry cannot launder product failure |
| S4 | explicitly permitted INFRA FAIL then PASS | `SATISFIED` | bounded INFRA retry preserved |
| S5 | FLAKY then PASS | `UNSATISFIED` | explicit flake remains gating |
| S6 | active quarantine with exact replacement records | `SATISFIED` | exact replacement evidence accepted |
| S7 | replacement omits `artifact_id` | `INCONCLUSIVE` | omitted identity fails closed |
| S8 | replacement uses wrong `artifact_id` | `INCONCLUSIVE` | substituted identity fails closed |
| S9 | same candidate starts a second root | `INCONCLUSIVE` | reset/fork rejected |
| S10 | exact successor + reconstructable predecessor evidence | `SATISFIED` | valid transition accepted |
| S11 | successor transition missing | `INCONCLUSIVE` | lineage required |
| S12 | wrong predecessor candidate | `INCONCLUSIVE` | predecessor binding enforced |
| S13 | predecessor/successor are same candidate | `INCONCLUSIVE` | same-candidate masquerade rejected |
| S14 | retained required artifact becomes unavailable | `INCONCLUSIVE` | retention loss reopens authority |
| S15 | exact original artifact restored at exact hash | `SATISFIED` | exact restoration accepted |
| S16 | same event list under different artifact ID | `INCONCLUSIVE` | identity substitution rejected |
| S17 | same event list under different expected hash | `INCONCLUSIVE` | hash substitution rejected |
| S18 | quarantine evaluated at declared expiry boundary | `INCONCLUSIVE` | expired quarantine cannot satisfy |
| S19 | required replacement member missing | `INCONCLUSIVE` | exact replacement-set equality enforced |
| S20 | extra replacement member supplied | `INCONCLUSIVE` | exact replacement-set equality enforced |
| S21 | wrong replacement-set member supplied | `INCONCLUSIVE` | exact replacement-set equality enforced |
| S22 | declared and claimed-observed predecessor roots both substituted while predecessor bytes stay fixed | `INCONCLUSIVE` | recomputation defeats matching-root laundering |
| S23 | changed-work identity substituted | `INCONCLUSIVE` | exact changed-work binding enforced |
| S24 | transition ID substituted | `INCONCLUSIVE` | exact transition identity enforced |
| S25 | remediation reason substituted | `INCONCLUSIVE` | exact reason binding enforced |
| S26 | predecessor evidence bytes substituted and producer updates digest/root consistently | `INCONCLUSIVE` | exact frozen predecessor artifact remains authoritative |

S18-S21 close the executable regression gap called out in `PG-REM-CI2-M01`. S22 is the exact double-root-substitution attack required by `PG-REM-CI2-M02`. S23-S26 close the stricter successor-admission requirement that changed work, transition identity/reason, and predecessor evidence bytes themselves cannot be replaced while keeping a self-consistent producer-authored packet.

## 6. Finding dispositions

### `PG-REM-CI2-M01` — RESOLVED

The exact frozen Python artifact now contains the evaluator and complete runnable corpus. Its own source identity is content-bound into the harness/result evidence and additionally fixed by Git blob identity. The result object is produced from exact fixture inputs by execution, and all S1-S26 expectations are asserted before output. New S18-S21 cases mechanically cover expiry and missing/extra/wrong replacement-set regressions.

A source-byte mutation outside the digest declaration was also executed as a self-binding attack and exited nonzero with `validator source identity mismatch`.

### `PG-REM-CI2-M02` — RESOLVED

The exact predecessor evidence bytes and root algorithm are now part of the frozen executable packet and emitted result. Successor admission recomputes the predecessor artifact digest/root and verifies exact predecessor, successor, changed-work identity, reason, transition ID, and the frozen predecessor artifact identity itself.

S22 changes both producer-facing root strings to the same false value while keeping predecessor evidence fixed; the validator recomputes from the bytes and returns `INCONCLUSIVE`. S23-S25 reject changed-work, transition-ID, and reason substitution. S26 changes predecessor evidence bytes and updates the producer-facing digest/root consistently; it still returns `INCONCLUSIVE` because the validator binds to the exact frozen predecessor artifact.

No root or transition field can therefore be accepted merely because a producer updates all mutually-consistent declarations together.

## 7. Preserved behavior and authority boundaries

The executable v4 corpus preserves the predecessor semantics required by Issue #102:

- `CONDITIONALLY_REQUIRED` compiles to `REQUIRED` or `NOT_APPLICABLE`; required `NOT_RUN` gates;
- PRODUCT failure cannot be laundered by a later PASS for the same candidate;
- explicit FLAKY remains gating;
- INFRA retry satisfies only when retry is explicitly permitted, all failures are INFRA, and terminal evidence passes;
- quarantine requires exact replacement-set equality and exact replacement evidence identity/ArtifactIdentity/hash;
- quarantine expires at the declared boundary;
- same-candidate second root/reset is rejected;
- replacement evidence remains durable and reconstructable;
- retained-artifact authority remains bound to stable identity, authoritative hash, and ordered events;
- retention loss or identity/hash substitution reopens authority.

This synthetic validator does not grant authority over real provider mechanics, classification correctness, semantic adequacy of replacement checks, real append-only storage, production CI design, implementation readiness, integration, or canonicalization.

## 8. Evidence versus inference

Direct evidence supports only the executable synthetic contract and the exact frozen corpus. It proves that these bytes implement and reproduce the declared cases and digests. It does not prove that a real CI provider supplies trustworthy event classification, that replacement checks are semantically equivalent, or that production artifact stores retain all evidence.

Those remain downstream empirical/review obligations. Treating this validator as production game or CI logic would exceed its declared `PLANNING_EXPERIMENT` authority.

## 9. Failure modes, risks, and reopen conditions

Residual risks include weak external INFRA classification, incomplete real-world evidence acquisition, backend mutation despite the modelled append-only contract, semantic mismatch between quarantined and replacement checks, and provider/account/policy drift.

Reopen if a descendant can:

- change executable validator semantics without changing the bound source identity;
- hand-author a result that cannot be reproduced from frozen inputs by the frozen validator;
- satisfy quarantine at/after expiry or with missing/extra/wrong replacement membership;
- satisfy replacement evidence with missing/wrong ArtifactIdentity or authoritative hash;
- satisfy a claimed successor without the exact predecessor evidence bytes and recomputed root;
- substitute both declared/observed roots while fixed predecessor evidence remains unchanged;
- substitute changed-work identity, transition ID/reason, or predecessor evidence bytes while retaining successor authority;
- erase required `NOT_RUN`, PRODUCT failure, FLAKY, same-candidate reset, or retention-loss evidence;
- silently grant provider, production, readiness, integration, implementation, or canonical authority.

## 10. Downstream handoff

Once Issue #102 freezes at exact `STATUS(REVIEW_READY)`, this v4 packet supersedes Issue #99 as the substantive CI remediation input for later `W2-REV-01`, while Issues #77/#91/#97/#99/#101 remain immutable provenance.

Formal aggregate independent adversarial review remains `W2-REV-01`. This task does not bypass or pre-authorize that gate.