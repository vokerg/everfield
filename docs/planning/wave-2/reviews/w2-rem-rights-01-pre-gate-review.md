# W2-PG-REM-RIGHTS-01 — Independent pre-gate review of rights authority remediation

**Mission:** `W2-PG-REM-RIGHTS-01` / Issue #118  
**Reviewed remediation:** Issue #114 / `W2-REM-RIGHTS-01`  
**Reviewed exact work/head:** `4ba39fa26404ba9564702fd385c133df75b71972`  
**Reviewed report blob:** `124866c20a6082624d3beba624859273b0d5572a`  
**Reviewed disposition blob:** `8cb5c60a9c0db2536194504325559d6bf25ca228`  
**Reviewed handoff blob:** `7a54200799f68ce5154f065acb1593dc8b372f8f`  
**Frozen producer provenance:** Issue #80 work/head `3c262cbf767633e0ca42f6bdf387e262056b4fb0`, report blob `bda0551c446c93492c9d8e809d087d592dfcdae3`  
**Authority:** independent non-authority pre-gate evidence only; formal `W2-REV-01` remains required.

## 1. Disposition

**`CHANGES_NEEDED` — 0 BLOCKER / 2 MAJOR / 1 MINOR.**

Issue #114 materially improves the predecessor: it introduces an explicit reference-use graph, a named/versioned originality-risk policy, and a single primary stale-state precedence for provider/legal/license/permission evidence. However, fresh adversarial reconstruction finds that the claimed deterministic policy compiler is not actually closed, and the claimed content-bound replay resistance is not mechanically reconstructable from the frozen bytes. A smaller stale-evidence state gap also remains for required originality evidence outside the provider/legal/license/permission subset.

The frozen Issue #114 candidate remains immutable. These findings require one bounded successor remediation; this review does not edit or re-own Issue #114.

## 2. Attack plan and exact reconstruction

The review attacked the three corrected authority surfaces independently of Issue #114's disposition prose:

1. instantiate exact policy tuples chosen to satisfy multiple rows of the `ORIGINALITY-RISK-v1` compilation table and compare emitted requirement cells;
2. instantiate a single-row tuple containing `CONDITIONAL` cells and attempt to derive their mandatory pre-assessment collapse using only the frozen policy bytes;
3. mutate fields that the report says participate in `reference_use_id` / `source_evidence_root` and search the frozen packet for a canonical serialization, field-inclusion, ordering, digest, or validation rule that forces identity change;
4. walk stale-state derivation for required evidence kinds enumerated by the policy but not named by the stale-precedence condition;
5. recheck authority language for accidental legal, release, production/readiness, integration, verification, or canonicalization promotion.

No current-source refresh was necessary to establish these findings: they are internal contract/derivation defects in the exact frozen remediation bytes, not a dispute about current provider terms.

## 3. `PG-REM-RIGHTS-M01` — MAJOR — policy rows overlap without precedence or merge semantics

Issue #114 says that one exact `(origin_class, reference_class, release_scope_class, material_trigger_set)` tuple emits **exactly one** `OriginalityEvidenceRequirementSet`. The frozen table does not define a closed row-selection, precedence, or merge algorithm, and its rows overlap.

A concrete same-tuple attack is:

```yaml
origin_class: PROJECT_NATIVE
reference_class: STYLE_OR_CREATOR_NAMED
release_scope_class: RELEASE
material_trigger_set: []
```

With no material signal, this tuple matches both:

- `BUILD_CANDIDATE or stronger + PROJECT_NATIVE/GENERAL_CONCEPTUAL and no material signal`; and
- `STYLE_OR_CREATOR_NAMED at DISTRIBUTION_CANDIDATE or RELEASE`.

Those rows disagree materially. The first permits `normalized_identity: CONDITIONAL`, `near_duplicate_checks: CONDITIONAL`, `targeted_external_search: NOT_APPLICABLE`, `judgment_review: CONDITIONAL`, and `qualified_legal_review: NOT_APPLICABLE`. The second requires normalized identity, near-duplicate checks, targeted search, and judgment review, with legal review conditional. The frozen bytes say neither “most specific wins,” “strongest requirement wins,” nor any other deterministic composition rule.

The material-trigger row also overlaps prior rows and says “previous requirements remain,” but does not define a typed merge operation over conflicting cells. Therefore an implementation can select one row, combine rows, or apply an unstated precedence while still plausibly claiming conformance.

**Impact:** the same exact policy tuple can produce materially different evidence authority. `PG-RIGHTS-M02` from the predecessor is therefore not mechanically closed.

**Required correction:** publish a closed row-selection/precedence or deterministic lattice/merge rule and executable or machine-checkable cases for every overlap class. For any exact tuple/epoch, only one normalized requirement set may be derivable.

## 4. `PG-REM-RIGHTS-M02` — MAJOR — `CONDITIONAL` has no closed applicability predicates and content-bound authority identities are underspecified

### 4.1 Unresolved conditional compilation

The packet correctly says every `CONDITIONAL` must compile to `REQUIRED` or `NOT_APPLICABLE` before assessment, but it does not supply the predicates that perform that compilation for many cells.

For example:

```yaml
origin_class: PROJECT_NATIVE
reference_class: GENERAL_CONCEPTUAL
release_scope_class: BUILD_CANDIDATE
material_trigger_set: []
```

The matching baseline row yields `normalized_identity: CONDITIONAL`, `near_duplicate_checks: CONDITIONAL`, and `judgment_review: CONDITIONAL`. The frozen policy contains no closed predicate determining whether any of those three becomes `REQUIRED` or `NOT_APPLICABLE`. “With a reason” records an implementation's choice after the fact; it does not determine the choice.

Equivalent unresolved phrases occur elsewhere, including `REQUIRED where media-appropriate`, targeted-search `CONDITIONAL`, and legal-review `CONDITIONAL` cases. These phrases are useful policy intent, but they do not meet the remediation's own claim of deterministic compilation from one exact tuple.

### 4.2 Replay-resistant identity cannot be mechanically reconstructed

`ReferenceUseRecord.reference_use_id`, `OriginalityReviewRecord.review_id`, `ReleaseRightsAssessment.assessment_id`, and `OriginalityEvidenceRequirementSet.requirement_set_id` are described as stable/content-bound identities. `ReferenceUseRecord.source_evidence_root` is described as a content-addressed digest of referenced authority records. The frozen packet does not define:

- the canonical serialization/version used to derive those identities;
- which exact fields are included or excluded;
- ordering/canonicalization for list-valued fields such as `source_reference_ids`, `allowed_reuse`, `prohibited_reuse`, terms refs, and permission refs;
- the digest algorithm/domain separator for record IDs/root; or
- a validator/recomputation procedure that rejects an asserted ID/root when bound field bytes change.

The prose rule “changed context requires a new `ReferenceUseRecord`” is correct intent, but without an identity derivation/validation contract, a consumer can carry the same asserted `reference_use_id` while changing `allowed_reuse`, `provider_terms_refs`, or `release_scope_ref`; the frozen bytes do not provide a mechanical function that proves the ID must change. The same weakness applies to `source_evidence_root` because “all referenced authority records” is not an exact canonicalization contract.

**Impact:** both deterministic applicability and the replay-resistant exact binding required by predecessor findings remain partly delegated to downstream implementation choice. That is material because these records are the authority boundary for `CLEAR`.

**Required correction:** define one versioned canonical encoding/content-identity function for every authority-bearing record/root, enumerate included fields and list/set ordering, and require recomputation/equality before any consuming assessment. Also replace every `CONDITIONAL`/contextual phrase with exact typed predicates or a closed sub-policy whose unknown state fails closed. Add negative fixtures or machine-checkable examples for changed purpose/reuse/terms/license/release scope and unresolved conditional inputs.

## 5. `PG-REM-RIGHTS-m01` — MINOR — stale-state precedence omits some required originality evidence kinds

The corrected precedence says:

1. active independent material-risk/conflict trigger -> `QUARANTINED(...)`;
2. stale required **provider/legal/license/permission** evidence -> `UNKNOWN(STALE_EVIDENCE)`;
3. missing/conflicting/out-of-scope evidence -> `UNKNOWN(...)`;
4. restriction -> `RESTRICTED(...)`;
5. otherwise satisfied -> `CLEAR`.

But `ORIGINALITY-RISK-v1` can require exact identity, normalized identity, known-reference comparison, near-duplicate checks, targeted external search, and judgment review. The policy separately says any required stale evidence blocks `CLEAR`. The state-derivation stale branch does not state what primary reason/state is derived when one of those non-provider/legal/license/permission required evidence items is stale and no independent material-risk trigger is active.

Safety still fails closed because stale required evidence cannot yield `CLEAR`, so this does not rise to MAJOR. But exact remediation/clearing state remains under-specified for a class of required stale evidence.

**Required correction:** make the stale branch apply to **all compiled REQUIRED evidence**, or define a closed evidence-kind-to-state mapping. Preserve the material-risk quarantine precedence and immutable historical `CLEAR` record.

## 6. Preserved authority boundaries

The review found no legal-clearance or release-authority promotion in the exact Issue #114 packet. It repeatedly states that similarity evidence is escalation-only; provider terms or output allocation are not release clearance; unknown/restricted/quarantined state blocks release; and formal `W2-REV-01` remains required. No production/readiness, implementation, integration, verification, or canonicalization authority is created by Issue #114 or this review.

## 7. Finding reconciliation

- predecessor `PG-RIGHTS-M01`: **PARTIALLY CLOSED / MATERIAL FOLLOW-UP REQUIRED** — the missing reference-use graph is now explicit, but its authority-bearing content identities/root are not mechanically derivable or validated;
- predecessor `PG-RIGHTS-M02`: **NOT CLOSED** — a named policy exists, but overlapping rows and unresolved conditional predicates prevent deterministic compilation for one exact tuple;
- predecessor `PG-RIGHTS-m01`: **MOSTLY CLOSED / MINOR FOLLOW-UP REQUIRED** — provider/legal/license/permission staleness has deterministic precedence, but other compiled required originality evidence lacks an exact stale-state branch.

## 8. Required bounded successor

Create one remediation successor that edits only the Issue #114 rights-policy/report/disposition surface and:

1. closes policy row overlap with exact precedence/merge semantics;
2. replaces every conditional/contextual requirement with deterministic typed predicates or a fail-closed sub-policy;
3. defines canonical, content-bound record/root derivation plus recomputation validation for authority-bearing IDs;
4. generalizes stale-state derivation to every compiled required evidence kind;
5. publishes mechanical negative/positive cases sufficient for an independent reviewer to reproduce the closure;
6. preserves all current legal/release/readiness authority limits and mandatory draft-PR-before-terminal behavior.

Formal `W2-REV-01` remains the required aggregate review after the Wave-2 prerequisite graph is satisfied.