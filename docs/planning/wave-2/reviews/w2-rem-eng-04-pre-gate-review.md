# W2-PG-REM-ENG-04 — Independent pre-gate review of engine schema/adaptation remediation

**Mission:** `W2-PG-REM-ENG-04` / Issue #122  
**Reviewed issue:** #112 / `W2-REM-ENG-04`  
**Reviewed work/head:** `6c5777ca56d43e22cba9b5e776e436d11b846325`  
**Reviewed harness blob:** `58e6e0832e36fdc4dd2bee7d1984e12e3fa4fc9f`  
**Reviewed validator blob:** `7837695c91365273b2c89f3852b401c2f127af54`  
**Reviewed disposition blob:** `fbae989e6d806788bcd22827b98e87624662e07b`  
**Reviewed handoff blob:** `d572aeafb733b4ffbd623ca727a305abd2a15092`  
**Authority:** independent noncanonical pre-gate evidence only; formal aggregate review remains `W2-REV-01`.

## Disposition

`CHANGES_NEEDED`

Independent review found **0 BLOCKER / 2 MAJOR / 1 correction-requiring MINOR**. Issue #112 genuinely closes the new reset/workspace/index, candidate/adaptation binding, and history-validity findings from Issue #110, but two preserved authority surfaces remain materially fail-open and several malformed adaptation/container shapes still raise rather than reject deterministically.

A single bounded successor is Issue #126 / `W2-REM-ENG-05`. Frozen Issue #112 remains immutable.

## Exact reproduction

The validator was fetched from exact Git blob `7837695c91365273b2c89f3852b401c2f127af54` and reconstructed as **35,451 exact bytes**. Independent Git-object hashing reproduced the same blob SHA:

- `sha1("blob 35451\\0" + bytes) = 7837695c91365273b2c89f3852b401c2f127af54`.

Independent raw-byte SHA-256 reproduced the producer source identity:

- validator source: `915d84b10fc1744af6d077bcec5025fd95f02877af341082a45e5cfaa90bc8fa`.

`python -m py_compile` succeeded. Two complete executions of the exact bytes were byte-identical and reproduced stdout SHA-256:

- deterministic stdout: `6f194aa5426c42e545130160da3eeb2d5e36d05ea3296d2b54c4cb9add177baa`.

The emitted semantic identities exactly matched Issue #112:

- validator contract: `5f37d97fa2bb263d87a10bc5cfd9311c744e1b80e83d42c8d6a9b202ccfef269`;
- feature slice: `9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`;
- scenario manifest: `be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`;
- fixture inputs: `15fd95e053acc634a7df2953ab411895fd47b8ee6145465a7faf6623579d3a6b`;
- result object: `f76a166ec79ea08ceb2dc60ad5988f33a108a59cd153fb1157ebf0817fe850ac`.

The independently generated attack evidence contained **64 cases**; its canonical review-local JSON serialization had SHA-256 `401d656117ea287c97696f70bd63251ee4be33f23d59333661c4fb9270fd0194`. The review result below is based on direct execution against the exact frozen module, not producer prose.

## Confirmed closures

### `PG-REM3-M01` targeted AttemptRecord fields

The exact validator returns structural `INCONCLUSIVE` with `valid_envelope=false`, without exceptions, for all independently repeated required attacks:

- null/empty/blank reset identity;
- null/empty/blank workspace identity;
- integer/string/null `reset_verified` instead of exact boolean;
- null/string/boolean/zero/negative/float normal indices;
- duplicate normal indices;
- a failure-injection record carrying a normal index;
- a normal record carrying an injection identity;
- a failure-injection record missing its injection identity.

Reordered unique positive normal indices and reversed attempt-dictionary insertion order remain deterministic. Non-contiguous unique positive indices also remain deterministic, consistent with the declared positive/unique contract.

### `PG-REM3-M02` adaptation-to-consumer binding

Independent mutations of missing/blank/wrong candidate identity, harness identity, feature-slice identity, scenario identity, required fixed inputs, cross-candidate adaptation reuse, and stored adaptation-binding identity all fail closed with invalid envelopes. S3 mechanism-authority weakening, S9 package substitution, and S10 hidden-context transfer also fail closed.

### `PG-REM3-m01` history validity split

A correctly linked same-candidate repair history containing a generation with an invalid normal index reports:

- `lineage_valid=true`;
- `evidence_valid=false`;
- `valid=false`;
- reason `generation_evidence_envelope_invalid`.

The same result occurs when the second generation carries a substituted adaptation-binding ID. Structurally linked provenance therefore does not launder invalid generation evidence.

### Preserved no-laundering checks that remain sound

Independent attacks confirmed duplicate required-injection identity with retained failure, cross-candidate normal/injection attempts, normal reset/workspace reuse, resource mismatch, retained normal failure/flake behavior, omissions/extras in registry membership, and ordinary string-valued invalid result/failure-class pairs all retain their declared fail-closed/gating outcomes.

## Findings

### `PG-REM4-M01` — MAJOR — malformed result/failure-class values can crash instead of failing closed

Issue #112 explicitly says the inherited closed `result × failure_class` matrix remains structural and that malformed envelopes fail closed. The exact implementation performs hash-based membership before validating that the values are hashable scalar enum members:

- `result not in MATRIX`;
- `failure_class not in MATRIX[result]`.

Independent attacks set `result=[]` and separately `failure_class=[]`. Both raise `TypeError: unhashable type: 'list'` from `validate_attempt_record()` instead of returning a typed invalid envelope.

This is material because the preserved Issue #104 correction is not total over malformed input shapes: an authority-bearing synthetic evidence object can terminate validation rather than derive deterministic invalid evidence. The producer fixture `AG-17` proves only a malformed **string-valued** pair (`PASS + PRODUCT`), not malformed value types.

**Required correction:** validate scalar/type shape before hash membership and add executable unhashable/container negatives for both fields. Every malformed shape must return structural `INCONCLUSIVE`, `valid_envelope=false`, without exception.

### `PG-REM4-M02` — MAJOR — retained-attempt registry equality aliases multisets to sets

Issue #112 claims the inherited exact run-registry/retained-attempt equality remains in force. The validator currently checks:

- `set(run_registry_refs) == set(attempts)`;
- `set(all_attempt_refs) == set(attempts)`.

This catches omissions and unknown extras but does **not** enforce one-to-one identity. Independent attacks appended an already-present attempt ID to `run_registry_refs`, then separately to `all_attempt_refs`; each malformed evidence envelope still derived `PASS_FOR_COMPARISON` with `valid_envelope=true`. Duplicating an existing reference in **both** lists simultaneously also preserved `PASS_FOR_COMPARISON`.

This is a real authority defect rather than formatting noise: a malformed retained-evidence registry can receive positive comparison authority even though the claimed exact registry/reference relation is false.

**Required correction:** validate both containers as exact nonempty-ID lists/records, require uniqueness and cardinality equality before set/key equality, and reject duplicate refs structurally. Null/malformed registry containers must also reject without exceptions.

### `PG-REM4-m01` — MINOR — malformed adaptation/container shapes raise instead of typed rejection

The new candidate/binding attacks are correctly handled for well-shaped dictionaries, but several malformed nested container shapes raise exceptions:

- `fixed_input_refs=None` → `TypeError`;
- `mappings=None` → `AttributeError`;
- `bounds=None` → `AttributeError`;
- unhashable `scenario_id=[]` → `TypeError`;
- `run_registry_refs=None` / `all_attempt_refs=None` → `TypeError`.

These cases did not produce false `PASS_FOR_COMPARISON`, so this review does not elevate them to a separate MAJOR beyond the registry authority defect. They nevertheless violate the validator's intended deterministic machine-input behavior and should be closed in the same bounded successor.

**Required correction:** type-check authority-bearing containers/keys before set/dict/hash operations and return a typed invalid envelope.

## Lifecycle and authority check

Issue #112's own lifecycle correction is valid: draft PR #121 is currently open, remains draft, targets `main`, and its head is exactly `6c5777ca56d43e22cba9b5e776e436d11b846325`, matching Issue #112's terminal `head_sha`. Thus `PG-REM3-B01` is closed for Issue #112 itself.

The reviewed harness also preserves explicit authority limits: it is `PLANNING_EXPERIMENT` evidence only and claims no engine execution/scoring/selection, production/gameplay implementation, implementation readiness, integration, verification, release, or canonicalization authority. Formal `W2-REV-01` remains required.

## Routing

`CHANGES_NEEDED` routes exactly one bounded successor: **Issue #126 / `W2-REM-ENG-05`**. That successor is blocked until this review publishes a valid terminal schema-3 status. It must correct only the three findings above and preserve Issue #112's valid closures and all earlier provenance.

No change is authorized on frozen Issue #112. No merge or main integration is authorized by this review.
