# Issue 87 Handoff — W2-REM-AUTH-01

```yaml
protocol: planning-v1
handoff_schema: 1
issue: 87
mission_id: W2-REM-AUTH-01
role: bounded_authority_evidence_contract_remediation
branch: planning/issue-87
base_sha: e4b7ee0a2699a57216146e99b990ab64edaae1d1
ownership_generation_comment_id: 5252157771
state: REVIEW_READY
source_issue: 69
source_work_sha: 4f2baf8f97a531ac38491343098ac10c81c12a6b
source_self_review_comment_id: 5251524689
work_sha: 28cbecc13f679da0b43793525a9befd384df9a6d
artifacts:
  - path: docs/planning/wave-2/foundations/authority-evidence-contract.md
    blob_sha: a2cd16e1a20568f72a04e90eea4453b7fb880146
  - path: docs/planning/wave-2/reviews/w2-auth-01-self-review-dispositions.md
    blob_sha: 431950023255cf9672a95c028ce86e10c89db076
self_review_comment_id: 5252354331
self_review_disposition: AUTHOR_SIDE_PASS_FOR_HANDOFF
self_review_findings:
  blocker: 0
  major: 0
  minor: 2
review_index_utf8_bytes: 1517
required_independent_review: W2-REV-01
implementation_authorized: false
canonicality: NON_CANONICAL
```

## Completed

- Dispositioned all five Issue #69 author self-review findings: 3 MAJOR and 2 MINOR are corrected in the remediated candidate.
- Closed contract-layer primitive, predicate, immutable-reference, rule-registry, and exact rule-invocation input semantics.
- Separated retry replacement from check aggregation and made accepted retry replacements append-only/auditable in `EvidenceSatisfaction`.
- Replaced ambiguous required/optional booleans with `MANDATORY | ALTERNATIVE | REPLACEMENT` check roles.
- Made ANY/QUORUM aggregation alternative-only and downstream of the mandatory-check gate; a mandatory FAIL/FLAKY/INCONCLUSIVE/NOT_RUN cannot be outvoted.
- Compiled every RiskFloor dimension deterministically: trust, protected evidence, distinct evidence surfaces, review route.
- Added `NOT_EVALUATED` trust and deterministic capability-derived FULL/DEGRADED behavior; lease continuation does not upgrade trust.
- Made result-class, artifact rights/integrity, freshness, substitution, review-route, and readiness behavior fail closed.
- Preserved `EvidenceSatisfaction` as sole empirical acceptance authority and kept `IR-BLOCKER-EVIDENCE-FOUNDATION` OPEN.
- Added 43 validator fixtures including attacks for the source findings, registered-rule input substitution, mandatory-failure vote-out, retry replacement lineage, and readiness laundering.
- Main-to-work diff contains only the two Issue #87 remediation output paths.
- Review Index measured 1,517 UTF-8 bytes, below the 4,000-byte ceiling.

## Remaining non-blocking author notes

1. `AttemptPolicyV1` has an inactive-field canonicalization cleanup: make contiguous lineage structurally constant/mandatory and reject a non-null registered rule in built-in modes.
2. Set-like collection duplicate semantics should be made explicit before concrete schema/code generation; cross-runtime canonical ordering/encoding remains `W2-HASH-01` authority.

These are MINOR fail-closed schema-hygiene notes, not empirical-acceptance bypasses.

## Required next action

- Preserve exact work SHA `28cbecc13f679da0b43793525a9befd384df9a6d` for review.
- `W2-REV-01`, once its full prerequisite set is eligible, must receive this remediation as durable correction provenance alongside historical Issue #69 work `4f2baf8f97a531ac38491343098ac10c81c12a6b` and author finding comment `5251524689`.
- The independent reviewer should explicitly attack the two remaining MINOR notes plus the Review Index attack list; this author-side review does not count as independent disposition.
- Do not canonicalize, authorize production implementation, or integrate to `main` merely because this remediation is review-ready. Any eventual main integration remains squash-only and must follow the declared review/verification route.
