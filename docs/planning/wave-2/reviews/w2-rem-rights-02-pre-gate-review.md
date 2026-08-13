# W2-PG-REM-RIGHTS-02 — Independent pre-gate review of deterministic rights remediation

**Mission:** `W2-PG-REM-RIGHTS-02` / Issue #125  
**Reviewed remediation:** Issue #119 / `W2-REM-RIGHTS-02`  
**Reviewed exact work/head:** `7b856e2589d7b98c6fa224f670c500fa2f67b6d9`  
**Reviewed report blob:** `a65f31c1a39eea7f32c4de0524c118c25c07cd6e`  
**Reviewed fixture blob:** `5f821bdfce5c3e75869dcddedfe816fbda17d97c`  
**Reviewed disposition blob:** `170f35ce2b76742155a534429af9a2831c4f6c17`  
**Reviewed handoff blob:** `7f9ad281cae9b3bfcb5b9979ad87254d3b334634`  
**Review visibility:** Issue #119 draft PR #124 was independently re-fetched open/draft at exact head `7b856e2589d7b98c6fa224f670c500fa2f67b6d9`.  
**Authority:** independent non-authority pre-gate evidence only; formal `W2-REV-01` remains required.

## 1. Disposition

**`CHANGES_NEEDED` — 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.**

The epoch-2 overlap lattice, order-independent merge, closed `REQUIRED|NOT_APPLICABLE` output, stale-evidence precedence, and Issue #95 provenance reconciliation survive fresh attack. The packet nevertheless does not mechanically satisfy its stronger claim that every declared compiler input is present/typed/fail-closed and that recomputable content identity is schema-closed authority. Two exact executable gaps remain and are routed to bounded remediation Issue #129. Frozen Issue #119 remains immutable.

## 2. Mechanical reproduction and attack envelope

The exact Git blob `5f821bdfce5c3e75869dcddedfe816fbda17d97c` resolves from the frozen candidate and its executable statements reproduce the declared nine-test result digest:

```yaml
policy_id: ORIGINALITY-RISK-v2
policy_epoch: 2
serialization_version: EVERFIELD-RIGHTS-CANONICAL-JSON-v1
declared_fixture_source_sha256: 8c19575ad09769515dee74ae8462233184cf1aece07cd7e27450ba1a63aaaa8a
reproduced_result_digest_sha256: 4530e561ffc8ccc85bba22ce02932300b4b7995ceb5b5979196e9dad5d588ced
reproduced_tests_passed: 9
fresh_execution_outputs_byte_identical: true
```

The connector exposed the exact Git blob text but not a raw byte-mounted checkout, so this review does **not** claim an independent second computation of the producer-published source SHA-256; exact Git blob identity and executable behavior were independently resolved. This limitation does not create either finding below.

Beyond the producer's nine cases, the reviewer exhaustively enumerated the finite valid policy domain across all declared origin classes, reference classes, release-scope classes, media kinds, three booleans, and all 64 material-trigger subsets. Results:

```yaml
valid_combinations_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
trigger_permutation_same_requirement_set_id: true
adversarial_evidence_digest_sha256: ee841909435616e50803743ee82e706a2bff4388ec37358e170c245f0217153e
```

Thus `PG-REM-RIGHTS-M01`'s original overlap defect is mechanically closed for the admitted valid domain, and the stale-state loop still covers all seven requirement kinds with independent material-risk quarantine precedence.

## 3. `PG-REM2-RIGHTS-M01` — MAJOR — compiler input validation is not total or fail-closed for declared authority bindings

Issue #119 Section 2.1 says a compiler input is valid only when **all** declared fields are present and typed exactly, and that unknown/malformed contextual input fails closed as `UNKNOWN(POLICY_UNRESOLVED)`. The executable `_validate_policy_input` checks the policy/enum/boolean/trigger fields, but it does not validate `artifact_id`, `reference_use_id`, or `release_scope_ref` before `compile_policy` indexes or hashes them.

Fresh executable attacks against the frozen logic produce:

```yaml
invalid_inputs_that_return_COMPILED:
  - artifact_id: null
  - artifact_id: 7
  - reference_use_id: null
  - reference_use_id: false
  - release_scope_ref: null
  - release_scope_ref: []
missing_declared_fields_raise_uncaught_KeyError:
  - artifact_id
  - reference_use_id
  - release_scope_ref
malformed_trigger_members_raise_uncaught_TypeError:
  - material_trigger_set: [{}]
  - material_trigger_set: [["bad"]]
```

The trigger crashes occur because validation constructs `set(triggers)` before proving every member is hashable/typed. These are not merely cosmetic diagnostics: malformed authority-bearing bindings can be accepted into a `COMPILED` requirement-set payload and receive a content ID, while other malformed inputs escape the stated closed failure state entirely.

**Impact:** epoch-2 compilation is deterministic on the admitted valid domain but is not a total closed function over malformed/unknown inputs, and exact binding identifiers are not mechanically required before compilation. That leaves the `PG-REM-RIGHTS-M02` fail-closed applicability/authority correction materially incomplete.

**Required correction:** validate presence, closed type/shape, and admissible identity syntax/semantics for every declared compiler input before indexing or compilation; validate trigger member type before set construction; return one deterministic unresolved state for all malformed input rather than `COMPILED` or uncaught exceptions. Add negative fixtures for every case above.

## 4. `PG-REM2-RIGHTS-M02` — MAJOR — content-ID recomputation is not schema validation

Issue #119 correctly defines canonical JSON, domain separation, set normalization, and recomputation. But the executable `content_id` / `validate_claimed_id` path hashes whatever dictionary it is given; it does not prove that the dictionary contains the complete inherited record schema or that required fields have the declared closed types/value domains. `source_evidence_root` likewise hashes arbitrary evidence-entry dictionaries without first enforcing the report's required entry fields.

Fresh attacks demonstrate that the frozen helpers accept and self-validate materially underspecified authority objects:

```yaml
ReferenceUseRecord_empty_payload:
  content_id_computable: true
  claimed_id_recomputes_equal: true
ReferenceUseRecord_missing_provider_terms_refs:
  content_id_computable: true
  claimed_id_recomputes_equal: true
SourceEvidenceRoot_entry_with_only_kind:
  content_id_computable: true
  example_root: ser-sha256:8e9f4cf194c36d96e277defcea827ef12596653188d8ecf1f1c0e8f662f1d0b0
```

Changing a present bound field does change its digest, so the producer's mutation fixtures are valid; the missing property is **schema closure before authority**. A newly recomputed ID for an incomplete payload can still satisfy `validate_claimed_id`, which means recomputation equality alone cannot enforce Issue #119's statement that every declared record field is included or that every `SourceEvidenceRoot` entry has `kind`, `record_id`, `content_sha256`, and `immutable_ref` with valid closed forms. The same helper path permits no machine-checkable rejection of unknown/forbidden fields or conflicting duplicate record identities represented by distinct entry dictionaries.

**Impact:** a consumer can manufacture a self-consistent content identity over an underspecified authority payload. Unless an external validator is silently assumed, the exact frozen bytes do not mechanically prove the complete record graph required before `CLEAR`; that reintroduces downstream implementation choice at the authority boundary that Issue #118 required this remediation to close.

**Required correction:** publish and execute a versioned schema validator for each authority-bearing record and `SourceEvidenceRoot` entry before ID/root acceptance. Required fields, allowed/forbidden fields, types/value domains, identity syntax, semantic-set uniqueness, and conflicting duplicate record identities must fail closed mechanically. Preserve the existing canonicalization/digest contract after schema validation.

## 5. Preserved checks and non-findings

The following attacked surfaces are clean in this review:

- all 802,816 valid finite-domain policy combinations produce the same normalized requirements under forward versus reverse rule application;
- no valid combination emits `CONDITIONAL` or another third terminal requirement state;
- equivalent material-trigger ordering normalizes to the same requirement-set identity;
- all seven required evidence kinds route stale evidence to `UNKNOWN(STALE_EVIDENCE)`, with independent material risk taking `QUARANTINED` precedence;
- the Issue #119 handoff explicitly preserves Issue #95 as prior parallel immutable remediation provenance, does not treat #114 as the unique/first successor, and reconstructs the #80/#95/#114/#118/#119 lineage for formal review;
- PR #124 is open, draft, based on `main`, and exactly binds the reviewed #119 head;
- no legal clearance, release approval, provider permission beyond sourced evidence, production/readiness, implementation, integration, verification, or canonicalization authority is promoted.

## 6. Routing

The two MAJOR findings are routed to exactly one bounded, unclaimed remediation successor: Issue #129 / `W2-REM-RIGHTS-03`. That successor is blocked until this review's exact terminal `STATUS(REVIEW_READY)` exists, must be owned by a distinct session, and must preserve the valid epoch-2 lattice/stale/provenance behavior while adding total input and schema validation plus negative fixtures.

This review does not edit/re-own Issue #119, does not claim Issue #129, and does not replace formal `W2-REV-01`.