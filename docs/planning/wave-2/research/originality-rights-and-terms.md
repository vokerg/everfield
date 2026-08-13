# W2-REM-RIGHTS-02 — Rights policy determinism and content-identity remediation

**Mission:** `W2-REM-RIGHTS-02` / Issue #119  
**Branch:** `planning/issue-119`  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Frozen predecessor:** Issue #114 work/head `4ba39fa26404ba9564702fd385c133df75b71972`  
**Frozen predecessor report blob:** `124866c20a6082624d3beba624859273b0d5572a`  
**Independent review:** Issue #118 work/head `e35d83b9758dfb1ffa07747a5c60cb82e80c5411`  
**Independent review artifact blob:** `45f513bc4e8328ed75b979b76e982a2454705956`  
**Authority:** noncanonical Wave-2 remediation input only; formal `W2-REV-01` remains required.

## 1. Composition, scope, and non-goals

This artifact is a bounded successor overlay over the exact frozen Issue #114 report blob `124866c20a6082624d3beba624859273b0d5572a`. Every Issue #114 clause, including its exact import of the Issue #80 producer packet, remains inherited unless this remediation explicitly replaces it below. If the predecessor blob or the exact Issue #118 review artifact cannot be resolved, this remediation is invalid.

The only corrections in scope are the three Issue #118 findings:

- `PG-REM-RIGHTS-M01`: overlapping originality-risk rules lacked a closed precedence/merge operation;
- `PG-REM-RIGHTS-M02`: contextual/`CONDITIONAL` applicability and content-bound authority identities were not mechanically closed;
- `PG-REM-RIGHTS-m01`: stale-state derivation did not explicitly cover every originality evidence kind that can compile `REQUIRED`.

The predecessor's source research, provider-terms matrix, reference-use taxonomy, provenance/originality separation, similarity-as-escalation-only semantics, release blocking, freshness triggers, and authority limits remain unchanged. This remediation does not provide legal advice or clearance, release approval, engine selection, implementation readiness, production authority, integration authority, verification authority, or canonical status.

## 2. `ORIGINALITY-RISK-v2`: closed policy compiler

Issue #114 `ORIGINALITY-RISK-v1` is superseded for policy compilation by `ORIGINALITY-RISK-v2`, epoch `2`. The executable reference implementation is:

`docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py`

Its exact Git blob is `5f821bdfce5c3e75869dcddedfe816fbda17d97c` and exact source SHA-256 is `8c19575ad09769515dee74ae8462233184cf1aece07cd7e27450ba1a63aaaa8a`.

### 2.1 Exact compiler input

A compiler input is valid only when all of these fields are present and typed exactly:

```yaml
policy_id: ORIGINALITY-RISK-v2
policy_epoch: 2
artifact_id: <exact ArtifactIdentity>
reference_use_id: <exact ReferenceUseRecord identity>
release_scope_ref: <exact release-scope identity>
origin_class: PROJECT_NATIVE | GENERATED_PROVIDER | EXTERNAL_REFERENCE | EXTERNAL_ASSET | THIRD_PARTY_OUTPUT | LICENSED_MATERIAL | PUBLIC_DOMAIN_CLAIM
reference_class: FACTUAL_OR_FUNCTIONAL | GENERAL_CONCEPTUAL | STYLE_OR_CREATOR_NAMED | EXPRESSION_SPECIFIC | DIRECT_ASSET_OR_CODE | MARK_LIKENESS_PERSONA | CONFIDENTIAL_PRIVATE_RESTRICTED | PUBLIC_DOMAIN_CLAIM
release_scope_class: INTERNAL_RESEARCH | BUILD_CANDIDATE | DISTRIBUTION_CANDIDATE | RELEASE
material_trigger_set:
  - MATERIAL_SIMILARITY_SIGNAL | CREDIBLE_COMPLAINT | CONFLICTING_SOURCE | TERMS_AMBIGUITY | PERMISSION_AMBIGUITY | SCOPE_AMBIGUITY
media_kind: NONE | TEXT | IMAGE | AUDIO | VIDEO | CODE | MIXED
references_exist: <boolean>
incorporation_or_release_intent: <boolean>
legal_interpretation_material: <boolean>
```

Unknown enums, unknown or duplicate material triggers, a missing/wrong policy epoch, or a non-boolean typed predicate produce `UNKNOWN(POLICY_UNRESOLVED)`. They never compile by default inference.

`references_exist`, `media_kind`, `incorporation_or_release_intent`, and `legal_interpretation_material` are the closed predicates replacing Issue #114 phrases such as `CONDITIONAL`, `where media-appropriate`, or materially equivalent contextual choices. A consumer may not introduce an unversioned contextual predicate and still claim `ORIGINALITY-RISK-v2` conformance.

### 2.2 Closed requirement lattice and merge rule

A terminal `OriginalityEvidenceRequirementSet` contains only:

```text
NOT_APPLICABLE < REQUIRED
```

There is no terminal `CONDITIONAL` value in epoch 2. Every matched rule contributes zero or more `REQUIRED` cells. All matching contributions are joined cell-by-cell using `max` over the two-element lattice above. Therefore:

- `REQUIRED` dominates `NOT_APPLICABLE`;
- joins are commutative, associative, and idempotent;
- rule iteration order cannot change the normalized requirement set;
- an overlap is not an error and cannot silently select an easier row;
- a consumer that emits a third requirement state is invalid for epoch 2.

The compiler records the exact matched rule IDs in a normalized `compiler_trace`.

### 2.3 Closed rule set

The following rules are exact policy contributions. Multiple matches are expected and are joined with the lattice above.

| Rule | Exact predicate | Requirement contribution |
|---|---|---|
| `R0_TOTAL_BASELINE` | every valid tuple | `known_reference_comparison=REQUIRED` when `references_exist`; `exact_identity=REQUIRED` when scope is `BUILD_CANDIDATE` or stronger, incorporation/release intent is true, or origin is not `PROJECT_NATIVE`; at distribution/release with references and `media_kind != NONE`, normalized identity and near-duplicate checks are required; at distribution/release for reference classes other than factual/general, judgment review is required; qualified legal review is required when `legal_interpretation_material` or a terms/permission/scope ambiguity trigger is present. |
| `R1_INTERNAL_RESEARCH` | scope `INTERNAL_RESEARCH` | exact identity is required when references exist or origin is non-native; known-reference comparison is required when references exist. |
| `R2_NATIVE_BUILD` | scope `BUILD_CANDIDATE` or stronger, origin `PROJECT_NATIVE`, reference class factual/general/style-named | exact identity required; if references exist, known-reference comparison and judgment review required; if references exist and media applies, normalized identity and near-duplicate checks required. |
| `R3_STYLE_OR_CREATOR` | distribution/release + `STYLE_OR_CREATOR_NAMED` | exact identity, normalized identity, known-reference comparison, near-duplicate checks, targeted external search, and judgment review required; qualified legal review required when `legal_interpretation_material` or any material trigger is present. |
| `R4_EXPRESSION_OR_DIRECT` | distribution/release + `EXPRESSION_SPECIFIC` or `DIRECT_ASSET_OR_CODE` | exact identity, normalized identity, known-reference comparison, judgment review required; near-duplicate checks required when media applies; targeted external search required when references exist; qualified legal review required when `legal_interpretation_material` or a terms/permission/scope ambiguity trigger is present. |
| `R5_MARK_LIKENESS_PERSONA` | distribution/release + `MARK_LIKENESS_PERSONA` | exact identity, known-reference comparison, targeted external search, judgment review required; normalized identity and near-duplicate checks required when media applies; qualified legal review required when legal interpretation is material or scope is `RELEASE`. |
| `R6_RESTRICTED_REFERENCE` | `CONFIDENTIAL_PRIVATE_RESTRICTED` | exact identity, judgment review, and qualified legal review required; known-reference comparison required when references exist. These checks do not cure the independent restriction. |
| `R7_MATERIAL_TRIGGER` | non-empty `material_trigger_set` | known-reference comparison and judgment review required; near-duplicate checks required when media applies; targeted external search required when references exist; qualified legal review required for terms/permission/scope ambiguity or when legal interpretation is material. |

No score, similarity threshold, or self-authored judgment can lower a requirement produced by these rules.

### 2.4 Required overlap case from Issue #118

The review's concrete tuple:

```yaml
origin_class: PROJECT_NATIVE
reference_class: STYLE_OR_CREATOR_NAMED
release_scope_class: RELEASE
material_trigger_set: []
media_kind: IMAGE
references_exist: true
incorporation_or_release_intent: true
legal_interpretation_material: false
```

matches `R0_TOTAL_BASELINE`, `R2_NATIVE_BUILD`, and `R3_STYLE_OR_CREATOR`. Its normalized result requires exact identity, normalized identity, known-reference comparison, near-duplicate checks, targeted external search, and judgment review. Qualified legal review remains `NOT_APPLICABLE` for this exact tuple because neither the legal-material predicate nor a material/ambiguity trigger is present.

The executable fixture reverses rule application order and verifies the same normalized result. This closes the Issue #118 same-tuple ambiguity without selecting one row post hoc.

## 3. Canonical authority identities and recomputation

Issue #114's stable/content-bound identity intent is replaced by the following exact serialization and digest contract.

### 3.1 Serialization version and domain separation

Serialization version is `EVERFIELD-RIGHTS-CANONICAL-JSON-v1`.

For each authority-bearing record, the **claimed identity field itself is excluded** from its canonical payload to avoid a circular hash. Every other field declared by that record schema is included unless a later canonical revision explicitly versions the schema differently.

The canonical envelope is UTF-8 JSON with:

- object keys sorted lexicographically;
- separators exactly `,` and `:` with no insignificant whitespace;
- JSON strings encoded without ASCII-only escaping;
- no floats or implicit numeric/string coercion;
- `null`, boolean, integer, and string values represented by their JSON primitives;
- the exact top-level shape:

```json
{"payload":<normalized-record>,"record_type":"<RecordType>","serialization_version":"EVERFIELD-RIGHTS-CANONICAL-JSON-v1"}
```

The content identity is:

```text
sha256( UTF8("everfield:rights:<RecordType>:v1\0") || canonical_envelope_bytes )
```

with these textual prefixes:

- `ReferenceUseRecord` -> `rur-sha256:<hex>`
- `OriginalityReviewRecord` -> `orr-sha256:<hex>`
- `ReleaseRightsAssessment` -> `rra-sha256:<hex>`
- `OriginalityEvidenceRequirementSet` -> `oers-sha256:<hex>`
- `SourceEvidenceRoot` -> `ser-sha256:<hex>`

A consumer MUST recompute and compare each claimed identity before the record may contribute authority. A mismatch is invalid evidence and cannot produce `CLEAR`.

### 3.2 Set-valued versus ordered list fields

The following list-valued fields are semantic sets. Their members are individually canonicalized, duplicate canonical members are rejected, and members are sorted lexicographically by their canonical JSON before hashing:

```yaml
ReferenceUseRecord:
  - source_reference_ids
  - allowed_reuse
  - prohibited_reuse
  - license_or_permission_refs
  - provider_terms_refs
OriginalityReviewRecord:
  - reference_corpus_ref
  - exact_duplicate_checks
  - near_duplicate_checks
  - targeted_external_search_refs
  - material_signals
  - blind_spots
ReleaseRightsAssessment:
  - provider_terms_refs
  - license_or_permission_refs
  - unresolved_triggers
  - freshness_refs
  - reopen_conditions
OriginalityEvidenceRequirementSet:
  - material_triggers
SourceEvidenceRoot:
  - evidence_entries
```

All other list fields are ordered lists and their order is authority-bearing unless the producer deterministically normalizes them before constructing the payload. In epoch 2 the compiler emits `compiler_trace` in sorted rule-ID order; `derivation_trace` remains an ordered causal trace.

This distinction means reordering a semantic set does not change its record identity, while adding/removing/substituting a set member does. Reordering an authority-bearing ordered trace does change identity.

### 3.3 Source-evidence root

`ReferenceUseRecord.source_evidence_root` MUST be the `SourceEvidenceRoot` content identity of the exact semantic set of authority evidence entries consumed by the record. Each entry has at least:

```yaml
kind: <closed record kind>
record_id: <exact content-bound or immutable record identity>
content_sha256: <sha256 of exact evidence bytes>
immutable_ref: <repository blob/commit or other immutable protected reference>
```

The source-evidence set must cover the exact provenance, source/reference, license/permission, provider-terms, provider-input-admission, policy, and other authority records the `ReferenceUseRecord` claims to consume. A changed evidence entry, digest, or immutable ref changes the root. Merely changing a locator while retaining inaccessible or unverifiable bytes does not preserve authority.

### 3.4 Cross-record binding

Before `ReleaseRightsAssessment` can derive `CLEAR`:

1. the claimed IDs of `ReferenceUseRecord`, `OriginalityReviewRecord`, `OriginalityEvidenceRequirementSet`, and `ReleaseRightsAssessment` MUST each recompute from their exact declared payloads;
2. the `ReferenceUseRecord.source_evidence_root` MUST recompute from the exact consumed authority-evidence entries;
3. candidate artifact, release scope, reference-use identity, policy epoch, and compiled requirement-set identity MUST agree across consuming records as declared by Issue #114;
4. the requirement-set identity MUST be recomputed from the epoch-2 compiler output, not copied from a previous context;
5. substituting purpose, allowed/prohibited reuse, terms, license/permission, source/reference identities, release scope, policy requirement identity, or other bound fields while retaining an old claimed ID is invalid.

A stable string chosen by a producer is not a content identity. Exact recomputation is mandatory.

## 4. Deterministic stale-evidence and rights-state derivation

Issue #114 Section 4 is replaced with this total precedence for the evidence kinds governed by the compiled requirement set:

```text
1. if independent material-risk trigger in
     {MATERIAL_SIMILARITY_SIGNAL, CREDIBLE_COMPLAINT, CONFLICTING_SOURCE}
   is active:
       QUARANTINED(MATERIAL_RISK)
2. else if any compiled REQUIRED evidence kind is STALE:
       UNKNOWN(STALE_EVIDENCE)
3. else if any compiled REQUIRED evidence kind is
     MISSING | CONFLICTING | OUT_OF_SCOPE | NOT_RUN | INCONCLUSIVE
   or lacks a validated authority binding:
       UNKNOWN(REQUIRED_EVIDENCE_UNSATISFIED)
4. else if an explicit scope restriction applies:
       RESTRICTED(EXPLICIT_SCOPE_RESTRICTION)
5. else if every compiled REQUIRED evidence kind is SATISFIED
     and every required content identity/root validates:
       CLEAR(ALL_REQUIRED_EVIDENCE_SATISFIED)
6. else:
       UNKNOWN(UNCLASSIFIED_EVIDENCE_STATE)
```

This stale branch applies equally to every requirement kind:

- exact identity;
- normalized identity;
- known-reference comparison;
- near-duplicate checks;
- targeted external search;
- judgment review;
- qualified legal review.

Terms/permission/scope ambiguity may strengthen the qualified-legal-review requirement but does not by itself masquerade as the independent material-risk trigger set above. A separate material-risk trigger has quarantine precedence.

A historical `CLEAR` record remains immutable history at its exact evidence and policy epoch. Freshness loss creates a new current derived state; it never rewrites the historical assessment. Clearing again requires a fresh assessment whose exact required evidence and content bindings validate under the current policy epoch.

## 5. Mechanical evidence and reproducibility

The executable fixture is planning evidence only and uses Python standard library APIs; it is not production game logic or legal logic.

Exact fixture identity and expected result:

```yaml
path: docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py
git_blob_sha: 5f821bdfce5c3e75869dcddedfe816fbda17d97c
source_sha256: 8c19575ad09769515dee74ae8462233184cf1aece07cd7e27450ba1a63aaaa8a
policy_id: ORIGINALITY-RISK-v2
policy_epoch: 2
serialization_version: EVERFIELD-RIGHTS-CANONICAL-JSON-v1
result_digest_sha256: 4530e561ffc8ccc85bba22ce02932300b4b7995ceb5b5979196e9dad5d588ced
tests_passed: 9
```

The exact frozen blob syntax-compiles. Two fresh executions were byte-identical and emitted the result digest above.

The nine deterministic checks are:

1. `T01_OVERLAP_JOIN_ORDER_INDEPENDENT` — the Issue #118 overlap tuple compiles to the same strongest normalized requirements even when rule order is reversed;
2. `T02_NO_CONDITIONAL_TERMINAL` — emitted cells are only `REQUIRED` or `NOT_APPLICABLE`;
3. `T03_UNKNOWN_FAILS_CLOSED` — an unknown contextual enum yields `UNKNOWN(POLICY_UNRESOLVED)`;
4. `T04_SET_ORDER_CANONICAL` — reordering declared semantic sets does not change identity;
5. `T05_BOUND_FIELDS_CHANGE_REFERENCE_USE_ID` — changing purpose, release scope, provider terms, license/permission refs, or source/reference refs changes `ReferenceUseRecord` identity;
6. `T06_SOURCE_ROOT_RECOMPUTABLE` — source evidence set reordering is stable while evidence-content substitution changes the root;
7. `T07_ALL_REQUIRED_KINDS_HAVE_STALE_PRECEDENCE` — every required evidence kind derives `UNKNOWN(STALE_EVIDENCE)`, with independent material risk taking quarantine precedence;
8. `T08_CLEAR_REQUIRES_ALL_REQUIRED_SATISFIED` — `CLEAR` requires all compiled required kinds satisfied;
9. `T09_ALL_AUTHORITY_RECORD_IDS_RECOMPUTABLE` — all authority-bearing record types recompute and reject bound-payload mutation.

A fresh reviewer can execute the exact frozen fixture and compare the printed canonical summary, Git blob identity, and source SHA-256 with the values above.

## 6. Finding disposition

### `PG-REM-RIGHTS-M01` — RESOLVED

The epoch-2 requirement lattice and join operation are closed, order-independent, and executable. The exact overlap tuple identified by Issue #118 now has one normalized requirement set. No row-selection or post-hoc weaker interpretation remains.

Evidence: `T01_OVERLAP_JOIN_ORDER_INDEPENDENT`, `T02_NO_CONDITIONAL_TERMINAL`.

### `PG-REM-RIGHTS-M02` — RESOLVED

All formerly contextual compiler decisions are represented by exact typed inputs/predicates and fail closed when unknown. Authority-bearing records and `source_evidence_root` now have a versioned canonical serialization, declared set/ordered-list behavior, SHA-256 domain separation, and mandatory recomputation/equality validation. Bound-context substitution cannot retain the prior identity.

Evidence: `T02_NO_CONDITIONAL_TERMINAL`, `T03_UNKNOWN_FAILS_CLOSED`, `T04_SET_ORDER_CANONICAL`, `T05_BOUND_FIELDS_CHANGE_REFERENCE_USE_ID`, `T06_SOURCE_ROOT_RECOMPUTABLE`, `T09_ALL_AUTHORITY_RECORD_IDS_RECOMPUTABLE`.

### `PG-REM-RIGHTS-m01` — RESOLVED

The stale branch applies to every evidence kind that can compile `REQUIRED`; independent material-risk quarantine has explicit precedence; historical `CLEAR` remains immutable history.

Evidence: `T07_ALL_REQUIRED_KINDS_HAVE_STALE_PRECEDENCE`, `T08_CLEAR_REQUIRES_ALL_REQUIRED_SATISFIED`.

Self-review against the exact Issue #119 scope: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

## 7. Preserved authority boundaries

The following Issue #114/Issue #80 semantics remain normative:

- provenance, provider/contract permission, originality/similarity signal, and release-sensitive rights state are orthogonal;
- provider output allocation is not legal/release clearance;
- provider input/data-use/training terms remain a separate admission dimension;
- unknown, restricted, or quarantined material cannot silently satisfy a release gate;
- public accessibility does not imply reuse permission;
- exact provider/account/product terms epoch remains required where applicable;
- similarity is escalation evidence only and cannot prove infringement, non-infringement, originality, or independent creation;
- protected/private evidence stays protected rather than copied into ordinary public artifacts;
- source freshness and reopen triggers remain active;
- unresolved legal/IP questions remain OPEN where project evidence does not decide them.

`qualified_legal_review=REQUIRED` in this planning policy means the project must obtain/record that qualified evidence before its own `CLEAR` state where the typed predicate requires it. It is not a legal conclusion and does not make this artifact legal advice.

## 8. Reopen conditions

Reopen this remediation if:

- one exact valid tuple/epoch can compile to two materially different normalized requirement sets;
- rule application order changes the normalized requirement set;
- a consumer can emit or retain an unresolved `CONDITIONAL` while claiming epoch-2 conformance;
- an unknown predicate, enum, trigger, or policy epoch can produce `CLEAR`;
- a declared authority-bearing field can change without changing/rejecting its recomputed record identity/root;
- a duplicate semantic-set member can pass canonicalization silently;
- any compiled required evidence kind can become stale without deterministically deriving `UNKNOWN(STALE_EVIDENCE)` absent a higher-priority independent material-risk trigger;
- a similarity score or self-authored review can reduce license/permission/provider-terms requirements;
- the exact predecessor/review blobs cannot be resolved;
- formal `W2-REV-01` identifies a new BLOCKER/MAJOR.

## 9. Downstream and integration boundary

When this packet is validly frozen at exact `STATUS(REVIEW_READY)` with the required draft review-visibility PR already open at the same head, it supersedes Issue #114 as the substantive corrected rights input for later Wave-2 review while preserving Issues #80/#114/#118 as immutable provenance.

That transition grants no integration or canonicalization authority. Formal aggregate `W2-REV-01` remains required. Any eventual integration into `main` must follow a separately eligible route and use squash merge only.