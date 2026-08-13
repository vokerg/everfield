# W2-PG-REM-CI-04 — Independent pre-gate review of replacement-evidence provenance remediation

**Mission:** `W2-PG-REM-CI-04` / Issue #115  
**Winning ownership generation:** claim comment `5276627047` / actor `w2-pg-rem-ci-04-agent-20260813-0811-01`  
**Reviewed issue:** #107 / `W2-REM-CI-04`  
**Reviewed terminal status:** comment `5276347966`  
**Reviewed work/head:** `c22bfedf02ca0b79716e4783d77d114c75655bd9`  
**Validator blob:** `b951064b701045763f72bcd5247cac45329d1fe5`  
**Report blob:** `38697b9cc93e98cdd39c28061fbb08fc465163e1`  
**Disposition blob:** `fe8e54118aa6750a707c322c41601c8588215ad9`  
**Handoff blob:** `4f8469eec6b5c1c53d5aa76ba12aeed4aedba222`  
**Authority:** independent noncanonical pre-gate evidence only; formal aggregate review remains `W2-REV-01`.

## 1. Disposition

`CLEAN_FOR_W2_REVIEW_INPUT`

Independent attack found **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** in the bounded Issue #115 scope. The exact frozen v5 packet mechanically closes `PG-REM-CI3-M01`; no reviewed v4 lineage/retry/applicability/retention/reset authority regression was found.

Issue #107 remained immutable. This review does not re-own or edit its branch.

## 2. Contention and inherited-state handling

Issue #115 had two near-simultaneous schema-3 claims. Comment `5276627047` precedes comment `5276627247`, so `5276627047` is the valid ownership generation under the deterministic lowest-comment-ID rule. The losing episode subsequently wrote commits and published a `STATUS(REVIEW_READY)` naming losing generation `5276627247`; that status is not an authoritative terminal state.

The winning episode treated those branch bytes as untrusted inherited state, independently inspected the exact #107 target and independently reconstructed/attacked the validator semantics before retaining any inherited prose. This commit supersedes the inherited review/handoff text under the winning ownership generation.

## 3. Exact mechanical reproduction

The exact validator was read from frozen Git blob `b951064b701045763f72bcd5247cac45329d1fe5`. The producer report was not treated as an oracle. From the validator's exact embedded structures and evaluator rules, this review independently reconstructed the 34-case corpus and output bundle with Python standard-library canonical JSON/SHA-256 semantics.

All **34/34** scenario aggregates matched the frozen `EXPECTED` map.

The following identities reproduced exactly:

- validator source declaration: `sha256:75dc8a78c1489b0afbe39047261f5bfeed77a08d970885cb670d77f3d3d8d8d3`;
- fixture manifest: `sha256:fd16a0496085b923ea87e91f5aa211d58b281f13477a0e1fb62084247f526075`;
- fixture cases: `sha256:c6ed8dca6d4fa7c3b2f49c082070a0b081c6bd8f1f03c3869820b9066adbd069`;
- harness contract: `sha256:a7bd2145b4cc5ffea6472950305bb85f50bd12b891b45497ab7317df3b8fe33a`;
- result object: `sha256:c5c752b9fac136eb9619cabbce1b108627402686864b41738d423da46189e5fa`;
- replacement execution envelope set: `sha256:2ac80d5dd1f8e08de84d9409b37c20d99d2251420dc81c50b9ffbfbd4692b9d5`;
- predecessor evidence artifact/root: `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`.

The individual replacement envelope identities also reproduced:

- `repl-env-short-soak-v1`: `sha256:36ea19895b16624e8b821b7463f82879e094e29912d89d1c541523c2f510377c`;
- `repl-env-static-invariant-v1`: `sha256:1520beba77c89b44dbe01ecd20c4a2ddb1a046ce22df2e47f2495b197483fa0a`.

The exact pretty-printed bundle shape reconstructed to **95,815 bytes** including the trailing newline and SHA-256 `a146b66d1378540157923dee8c67f4b319e9012274a3db004b4401ececcfa70b`, matching the frozen report's execution evidence.

The source guard is structurally fail-closed in the reviewed bytes: `normalized_source()` substitutes only the declared digest line, `source_digest()` hashes all other source bytes, and `bundle()` exits before fixture evaluation if the observed normalized-source identity differs from `VALIDATOR_SOURCE_DIGEST`. Therefore a non-digest semantic/source mutation cannot preserve execution under the frozen source identity.

## 4. Fresh adversarial mutation matrix

Beyond the built-in S27-S34 corpus, this review executed **37 additional negative quarantine mutations** against the reconstructed exact evaluator plus one positive control. The positive unmodified active quarantine returned `SATISFIED`; every negative returned `INCONCLUSIVE`; no attack retained `SATISFIED`.

Fresh record-level attacks covered substitution of:

- candidate ID;
- requirement ID;
- policy version;
- replacement ID;
- check ID;
- result;
- artifact key;
- `artifact_id`;
- authoritative expected hash;
- source-envelope digest;
- replacement-evidence ID;
- source-envelope ID;
- provenance ID;
- provenance value.

Fresh source-envelope attacks covered substitution of:

- replacement-evidence ID;
- candidate ID;
- requirement ID;
- policy version;
- replacement ID;
- check ID;
- result;
- artifact key;
- `artifact_id`;
- authoritative expected hash;
- provenance ID;
- provenance value.

Additional attacks removed or added envelope-map members, crossed the quarantine candidate, hit the expiry boundary, and changed record+envelope fields **in sync** while recomputing the record's per-envelope digest. Synchronized tampering of candidate, requirement, policy, result, artifact identity, expected hash, and provenance still failed because the complete supplied envelope set must match the immutable frozen set identity and the exact frozen envelope bytes.

These fresh attacks independently confirm that agreement between attacker-controlled record/envelope pairs is insufficient: accepted authority is anchored to the frozen IDs, frozen catalog, frozen envelope bytes, and frozen envelope-set digest.

## 5. `PG-REM-CI3-M01` closure

The predecessor review found v4 could preserve `SATISFIED` after changing replacement evidence identity, source-envelope identity, or provenance. In v5:

1. each keyed replacement must carry its exact frozen `replacement_evidence_id`;
2. all replacement evidence IDs must be unique;
3. each keyed replacement must name its exact frozen `source_envelope_id`;
4. all source-envelope IDs must be unique;
5. the supplied envelope map must equal the frozen envelope set by canonical digest;
6. the referenced envelope must exist, match the frozen per-envelope digest, and equal the frozen envelope bytes;
7. candidate, requirement, policy, replacement/check identity, result, artifact key, `ArtifactIdentity`, expected hash, evidence ID, and structured provenance must agree between record and envelope;
8. artifact identity/hash must also match the frozen artifact catalog;
9. the result object retains the positive records, exact envelope bytes, per-envelope digests, and set digest for later reconstruction.

Built-in S27-S34 exercise the original defect classes and all derive `INCONCLUSIVE`. The 37 fresh attacks above extend the adversarial surface and found no bypass.

`PG-REM-CI3-M01` is therefore **CLOSED by exact reviewed bytes**, not by remediation prose.

## 6. Preserved v4 behavior

The independently reconstructed S1-S26 truth classes all matched the frozen expected results. This includes:

- required `NOT_RUN` remains `UNSATISFIED`;
- PRODUCT fail then pass cannot be laundered by retry;
- permitted INFRA fail then pass may satisfy;
- FLAKY then pass remains `UNSATISFIED`;
- valid active exact quarantine is `SATISFIED`;
- expiry boundary and wrong/missing/extra replacement sets fail closed;
- same-candidate second-root reset fails closed;
- valid successor transition satisfies only with exact predecessor bytes/root and exact transition/work/reason identities;
- predecessor/root/work/transition/reason/artifact substitutions fail closed;
- retention loss, artifact-identity swap, and expected-hash swap fail closed while exact restoration satisfies.

No regression was found in the bounded semantics Issue #107 claimed to preserve.

## 7. Authority boundaries and reopen conditions

No authority leakage was found. Neither Issue #107 nor this review selects a CI provider, defines a universal INFRA classifier, proves production storage durability, authorizes implementation/gameplay work, establishes implementation readiness, authorizes integration, performs formal verification, authorizes release, or canonicalizes any artifact.

Reopen if a descendant can retain quarantine `SATISFIED` while substituting/duplicating replacement evidence identity; using dangling/wrong/duplicated/mutated source envelopes; changing candidate/policy/check/result/artifact identity/hash/provenance without invalidation; changing semantics without a new bound source identity; or regressing any S1-S26 truth class.

## 8. Review result

**CLEAN_FOR_W2_REVIEW_INPUT** — exact Issue #107 packet is suitable as additional noncanonical input to later formal `W2-REV-01`. This result creates no integration, verification, readiness, release, production, or canonicalization authority.
