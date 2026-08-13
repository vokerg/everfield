# Issue #141 handoff — W2-PG-REM-RIGHTS-03

**Mission:** `W2-PG-REM-RIGHTS-03`  
**Issue:** #141  
**Branch:** `planning/issue-141`  
**Ownership generation:** Issue #141 comment `5277369574`  
**Actor session:** `w2-pg-rem-rights-03-agent-20260813-0929-sol`  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Reviewed Issue #129 work/head:** `714394de603dd425a2cb9d2fd2eea1b7cb6135ca`  
**Reviewed fixture blob:** `8777e6eb45a47fd82b3dc976ab2a5a416fb909fb`  
**Reviewed report blob:** `c141b4f0db79390228c4088439f2396db56d26b8`  
**Review artifact blob:** `a181a88dcaa768fe6d0addc2c9eb38558e189e0d`  
**Disposition:** `CHANGES_NEEDED`  
**Finding:** `PG-REM3-RIGHTS-M01` (MAJOR)  
**Bounded successor:** Issue #142 / `W2-REM-RIGHTS-04`  
**Formal review:** `W2-REV-01` remains required after the rights lane is clean.

## Completed independent attack

The exact frozen Issue #129 validator source was inspected before remediation rationale. A fresh attack found one root-cause MAJOR: closed scalar/domain values are frequently passed directly into Python set/dict membership before their type is proven scalar/string.

The exact compiler source directly checks `origin_class`, `reference_class`, `release_scope_class`, and `media_kind` against set/dict domains. Authority schema paths repeat the pattern for `ReferenceUseRecord.reference_class`, `OriginalityReviewRecord.result`, rights-state/reason enums, requirement values, and SourceEvidenceRoot `kind`.

Independent runtime proof confirmed Python raises `TypeError: unhashable type` when a list/dict is used for set/dict membership. Therefore malformed JSON-shaped values can still crash these exact Issue #129 paths rather than return the declared fail-closed result.

This is one root cause, not multiple findings. Issue #142 is the only routed remediation and is blocked until this review terminalizes.

## Preserved evidence

The review found no reason to discard the valid Issue #129 corrections outside the affected totality boundary:

- exact field-set validation precedes content-ID construction;
- `material_trigger_set` has explicit list/string/member/duplicate guards before set construction;
- SourceEvidenceRoot has an exact entry shape and finite kind vocabulary;
- content IDs validate schema before hashing;
- valid epoch-2 policy semantics and stale/quarantine rules remain provenance to preserve;
- Issue #95 remains parallel immutable provenance;
- no legal/release/readiness/integration/canonicalization authority is created.

## Evidence limitation

The connector-retrieved GitHub bytes are not mounted into the local execution runtime, so the producer's full 14-test/stdout/802,816-combination audit suite was not falsely claimed as independently re-executed. The disposition does not depend on trusting those producer results: the exact frozen source itself contains deterministic unguarded hash-membership paths, and the underlying Python exception behavior was reproduced independently.

## Remaining route

1. Terminalize this review at exact branch head with draft PR visibility.
2. Issue #142 becomes eligible and must type-guard every externally supplied scalar/domain field before hash membership/indexing.
3. #142 must add a generated malformed-value matrix across all closed scalar/domain fields and rerun the inherited 14 tests plus finite-domain audit.
4. One fresh independent adjudication follows because this review found a material defect.
5. If that adjudication is clean, stop the rights pre-gate loop and let formal `W2-REV-01` consume the rights lane.

No other successor or optional review is authorized by this handoff.
