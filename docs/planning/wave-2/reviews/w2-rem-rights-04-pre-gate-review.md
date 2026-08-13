# W2-REM-RIGHTS-04 independent pre-gate review

## Review identity

- review mission: `W2-PG-REM-RIGHTS-04`
- review issue: `#145`
- reviewer ownership generation: `5277701964`
- reviewed remediation: Issue `#142` / `W2-REM-RIGHTS-04`
- reviewed terminal status: `5277675462`
- reviewed exact work/head: `4b61b276bb28bb114a650e003a7a5d0aeb77411a`
- reviewed fixture Git blob: `39fcdc292cd37661a061c6d3027715106b3a3d27`
- reviewed published fixture source SHA-256: `2238b83bed5a298eb4dc9721a1d75831aa768bc70e2be3c451ff0e3126efa690`
- disposition: `CHANGES_NEEDED`
- BLOCKER: 0
- MAJOR: 1
- MINOR: 0
- routed successor: Issue `#148` / `W2-REM-RIGHTS-05`

This review consumes Issue #142 only at the immutable identities above. It does not mutate or re-own the producer branch.

## Independent method and identity checks

The review re-fetched the exact Issue #142 terminal capsule, draft PR #144 provenance, and the exact fixture at `4b61b276bb28bb114a650e003a7a5d0aeb77411a`. GitHub independently resolves that fixture to Git blob `39fcdc292cd37661a061c6d3027715106b3a3d27`, matching the producer capsule. The exact 1,005-line source was inspected across the closed-domain validation, canonicalization/content-ID, compiler, derived-state, generated malformed-matrix, regression, and finite-domain-audit surfaces.

No GitHub Actions workflow run exists at the reviewed head, so this reviewer did not treat producer stdout as independent execution. Instead, the load-bearing malformed path described below was independently reconstructed from the exact `derive_state()` code and executed locally. That reproduction returned the same semantic result implied by the exact source: duplicate non-quarantine trigger members can produce `CLEAR` rather than fail closed.

The producer's declared generated-matrix cardinality independently reconciles from the exact source loops:

- 6 policy scalar/domain fields × 13 malformed values = 78
- 3 boolean policy fields × 11 non-boolean malformed values = 33
- 10 closed scalar record fields × 13 = 130
- 7 requirement values × 13 = 91
- SourceEvidenceRoot kind × 13 = 13
- record-type dispatch × 13 = 13
- 7 derived evidence-state values × 13 = 91
- one derived trigger-member slot × 13 = 13
- total = `462`

The finite valid-domain cardinality also independently reconciles from the exact enumerated domains: `7 origins × 8 reference classes × 4 release scopes × 2^6 unique trigger subsets × 7 media kinds × 2 × 2 × 2 booleans = 802,816`.

Those two cardinalities are internally consistent with Issue #142. They do not close the finding below because both test generators omit duplicate set-like `derive_state.material_triggers`: the 462-case matrix replaces one trigger member at a time, while the 802,816 audit constructs unique trigger subsets by bit mask.

## Closed-domain attack inventory

The exact producer source correctly installs typed/domain guards before the major hash/membership/index surfaces attacked by this review:

- policy-input `origin_class`, `reference_class`, `release_scope_class`, and `media_kind` are guarded before `_rule_contributions()` performs mapping lookup, set conversion, or set membership;
- policy ID/epoch, boolean fields, identifiers, and material-trigger members fail closed before compilation;
- record-type dispatch is guarded before `RECORD_FIELDS`, `CONTENT_ID_RE`, `ID_PREFIX`, or `SET_FIELDS` indexing;
- `ReferenceUseRecord.reference_class`, `OriginalityReviewRecord.result`, `ReleaseRightsAssessment.derived_rights_or_terms_state`, `ReleaseRightsAssessment.reason_code`, requirement values, and `SourceEvidenceRoot.evidence_entries[].kind` are closed-domain checked before authority-bearing use;
- list validators ensure member typing before duplicate detection with `set(...)`;
- SourceEvidenceRoot record IDs are validated as authority strings before uniqueness hashing;
- derived evidence-state values are type/domain checked before required-state membership tests;
- malformed individual derived trigger members are type/domain checked before `set(material_triggers)`.

Malformed object keys are rejected before canonical object sorting. Nested list/dict values cannot pass the scalar/domain guards on the declared closed surfaces. Duplicate set-like lists are rejected on canonical record surfaces through `_string_list(..., unique=True)`, explicit trigger uniqueness tests, or canonical set-field normalization. The exception is the derived-state trigger list described below.

## Finding `PG-REM4-RIGHTS-M01` — MAJOR

### Duplicate derived-state trigger sets can acquire `CLEAR`

`derive_state(requirements, evidence_states, material_triggers, explicit_restriction=False)` validates that `material_triggers` is a list and that every member is a closed string in `MATERIAL_TRIGGERS`, but it does **not** validate uniqueness before converting the list to a set:

```python
if not isinstance(material_triggers, list) or any(
    not _closed_member(item, MATERIAL_TRIGGERS) for item in material_triggers
):
    return {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
...
independent_risk = set(material_triggers) & {
    "MATERIAL_SIMILARITY_SIGNAL", "CREDIBLE_COMPLAINT", "CONFLICTING_SOURCE"
}
```

The same fixture treats trigger collections as set-like elsewhere: `_validate_policy_input()` rejects duplicate `material_trigger_set` members, `OriginalityEvidenceRequirementSet.material_triggers` requires `triggers == sorted(set(triggers))`, and `ReleaseRightsAssessment.unresolved_triggers` rejects duplicate members. The Issue #145 contract also explicitly requires attack of duplicate set-like inputs.

Independent focused execution of the exact `derive_state()` logic with every requirement `REQUIRED` and every evidence state `SATISFIED` produced:

```text
derive_state(..., ["TERMS_AMBIGUITY", "TERMS_AMBIGUITY"])
=> {"state": "CLEAR", "reason": "ALL_REQUIRED_EVIDENCE_SATISFIED"}

derive_state(..., ["SCOPE_AMBIGUITY", "SCOPE_AMBIGUITY"])
=> {"state": "CLEAR", "reason": "ALL_REQUIRED_EVIDENCE_SATISFIED"}

derive_state(..., ["CREDIBLE_COMPLAINT", "CREDIBLE_COMPLAINT"])
=> {"state": "QUARANTINED", "reason": "MATERIAL_RISK"}
```

The first two cases are a material fail-closed violation: malformed duplicate set-like authority input is accepted and can reach the positive `CLEAR` state. This is not merely an exception-safety defect and cannot be waived as cosmetic normalization.

The producer matrix does not test duplicate derived-state trigger lists. Its `derive_state.material_triggers[]` case tests `[value]` for each malformed scalar/domain value only. The finite audit also cannot reveal the defect because all trigger collections are unique subsets constructed from bit masks.

### Required correction

Issue #148 / `W2-REM-RIGHTS-05` must make duplicate `derive_state.material_triggers` fail closed to exact `UNKNOWN / POLICY_UNRESOLVED` before any set conversion or authority decision; add deterministic duplicate-trigger regressions and explicit generated structural-matrix coverage; and preserve the existing typed element guards, valid unique-trigger semantics, all inherited T01–T15 regressions, the 802,816 valid-domain audit, canonical content identities, stale/quarantine precedence, valid SourceEvidenceRoot ordering, and Issue #95 provenance.

## Other adversarial results

No second BLOCKER/MAJOR was found in the inspected scalar/hash/index surface. In particular:

- unhashable compiler substitutions are stopped by `_closed_member` / `_closed_mapping_member` before rule execution;
- wrong-type record-type values cannot index the schema/content-ID mappings;
- malformed record scalar fields fail through typed validators before membership/hash use;
- requirement values and compiler traces are closed before mapping access;
- malformed SourceEvidenceRoot kinds and IDs are rejected before uniqueness hashing;
- malformed derived evidence-state values fail before membership in missing/stale state sets;
- valid-domain rule-order comparison is structurally independent of this duplicate-trigger defect.

Issue #95 remains immutable parallel provenance; Issue #129, #141, and #142 lineage is reconstructable without upgrading prior evidence to canonical authority.

## Decision and authority boundary

Disposition is `CHANGES_NEEDED` with exactly one MAJOR finding, `PG-REM4-RIGHTS-M01`. Exactly one bounded remediation successor has been created: Issue #148 / `W2-REM-RIGHTS-05`. No additional optional pre-gate review is authorized by this decision. After #148 completes, one fresh independent review is required because this review found a material defect; a clean result after that must converge directly to formal `W2-REV-01`.

This review grants no legal clearance, release approval, provider permission, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority. Any eventual integration remains separately authorized and squash-only.