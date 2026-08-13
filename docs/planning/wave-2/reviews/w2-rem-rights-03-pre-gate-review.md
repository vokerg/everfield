# W2-PG-REM-RIGHTS-03 — independent review of Issue #129

**Mission:** `W2-PG-REM-RIGHTS-03` / Issue #141  
**Reviewed candidate:** W2-REM-RIGHTS-03 / Issue #129  
**Reviewed work/head:** `714394de603dd425a2cb9d2fd2eea1b7cb6135ca`  
**Reviewed fixture blob:** `8777e6eb45a47fd82b3dc976ab2a5a416fb909fb`  
**Reviewed report blob:** `c141b4f0db79390228c4088439f2396db56d26b8`  
**Prior review:** Issue #125 terminal comment `5277037579`  
**Independence profile:** `DEGRADED_SINGLE_AGENT`; immutable candidate; reviewer did not edit Issue #129.  
**Disposition:** `CHANGES_NEEDED`.

## 1. Attack order and evidence boundary

The review attacked the exact frozen Issue #129 validator source before relying on remediation rationale. The GitHub connector reproduced the exact candidate path at the declared work/head and exposed the source used for the checks below. The current execution runtime does not mount connector-retrieved GitHub bytes as executable local files, so the producer's complete 14-test/stdout/audit digest suite was not treated as independently re-executed evidence. This does not block the disposition because a fresh deterministic source-level attack reaches a material exception path in the exact frozen validator.

The critical Python operation was also reproduced independently in the execution runtime: membership of a `list` or `dict` in a `set` or `dict` raises `TypeError: unhashable type`, rather than evaluating to a boolean rejection.

## 2. Finding `PG-REM3-RIGHTS-M01` — MAJOR

**Title:** closed authority validators still hash untyped JSON-shaped scalar fields before fail-closed rejection.

Issue #129 correctly added exact top-level field sets, identifier validation, and pre-set validation for `material_trigger_set`, but the closure is not total over arbitrary malformed JSON-shaped values. Multiple authority-bearing paths perform hash-table membership before establishing that the candidate field is a scalar string.

### Compiler path

The exact `_validate_policy_input` performs:

```python
if inp["origin_class"] not in ORIGIN_CLASSES: ...
if inp["reference_class"] not in REFERENCE_CLASSES: ...
if inp["release_scope_class"] not in RELEASE_SCOPES: ...
if inp["media_kind"] not in MEDIA_KINDS: ...
```

`ORIGIN_CLASSES`, `REFERENCE_CLASSES`, and `MEDIA_KINDS` are sets; `RELEASE_SCOPES` is a dict. A JSON-shaped list/dict in any of these fields reaches membership before a type guard and raises `TypeError`. Therefore malformed compiler input can still crash instead of returning the promised exact `UNKNOWN(POLICY_UNRESOLVED)` result.

### Authority-record/schema paths

The same root cause is present after compilation:

- `ReferenceUseRecord.reference_class` is tested directly against `REFERENCE_CLASSES`;
- `OriginalityReviewRecord.result` is tested directly against `REVIEW_RESULTS`;
- `ReleaseRightsAssessment.derived_rights_or_terms_state` and `reason_code` are tested directly against set domains;
- `OriginalityEvidenceRequirementSet.requirements` values are tested with `value not in LEVEL`, where `LEVEL` is a dict;
- `SourceEvidenceRoot` entry `kind` is tested directly against `SOURCE_EVIDENCE_KINDS`.

For each of these, an unhashable list/dict value can raise before the function returns its intended typed invalid result. This contradicts the Issue #129 objective and acceptance criterion that malformed inputs and authority records fail closed deterministically without uncaught `TypeError` paths.

### Why existing tests did not close it

The published negative groups cover missing/unknown fields, malformed trigger members, reduced records, malformed source hashes/IDs, duplicate roots, and inherited valid enum domains. They do not exhaust malformed container substitutions for every scalar enum/domain field. `T11` is strong specifically for trigger members, but that guard does not generalize to the other set/dict membership sites.

### Required correction

One bounded successor must:

1. establish exact scalar type/domain validation before **every** set/dict membership or indexing operation on externally supplied compiler, record, requirement, and source-root fields;
2. ensure all malformed JSON-shaped substitutions return the declared fail-closed result rather than raising;
3. add a mechanically generated malformed-value matrix across every authority-bearing scalar/domain field, including `null`, booleans, numbers, empty strings, lists, and dicts;
4. preserve the valid epoch-2 lattice, canonicalization, stale/quarantine semantics, SourceEvidenceRoot valid ordering, and Issue #95 parallel provenance;
5. rerun the inherited 14 groups and finite valid-domain audit after correction.

## 3. Other attacked boundaries

Within the bounded static/mechanical attack performed before the MAJOR disposition:

- complete-record field-set validation precedes content-ID construction;
- `material_trigger_set` itself validates container/member string type before set construction and rejects duplicates/unknown members;
- `SourceEvidenceRoot` requires an exact four-field entry shape and finite source-evidence kind vocabulary;
- canonical content IDs validate record schema before hashing;
- the Issue #129 report preserves Issue #95 as parallel immutable provenance and does not claim unique-successor authority;
- no legal clearance, release approval, provider permission, production/readiness, implementation, integration, verification, release, or canonicalization authority is created.

These preserved properties do not waive `PG-REM3-RIGHTS-M01`.

## 4. Disposition

```yaml
disposition: CHANGES_NEEDED
blocker_count: 0
major_count: 1
correction_requiring_minor_count: 0
findings:
  - PG-REM3-RIGHTS-M01
reviewed_issue: 129
reviewed_head_sha: 714394de603dd425a2cb9d2fd2eea1b7cb6135ca
formal_review_required: W2-REV-01
rights_lane_clean_for_W2_REV_01: false
```

Issue #129 remains immutable. Exactly one bounded remediation successor is required; this review does not start another optional review loop. After that successor is independently adjudicated as clean, formal `W2-REV-01` is the next rights authority.
