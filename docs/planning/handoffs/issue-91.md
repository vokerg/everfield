# Issue #91 handoff — W2-REM-CI-01

**Mission:** `W2-REM-CI-01`  
**Issue:** #91  
**Branch:** `planning/issue-91`  
**Ownership generation:** Issue #91 comment `5270083695`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Source W2-CI-01 head/work:** `0011a9b02f1c7d8d20b81e0fb4faa6dec9bcae59`  
**Source report blob:** `7f9cb919c5e28299b7edbb1ea5495138d1509791`  
**Pre-gate review:** Issue #77 comment `5270075412`  
**Corrected report blob:** `1b9436f0aa29a1340439596d4373521a05d28b7e`  
**Finding-dispositions blob:** `e76d6fc46c0360a61f6269bd73b2a2466ee3e25f`  
**Intended terminal state:** `REVIEW_READY`  
**Required formal review:** `W2-REV-01`

## Completed work

Created a bounded remediation of the frozen W2-CI-01 producer evidence without editing the source branch.

The corrected report:

- binds every execution envelope to an exact candidate ID and base SHA;
- makes multiple envelopes for one candidate an append-only predecessor chain;
- rejects a same-candidate fresh-root reset/fork;
- models the remediated flaky candidate as a distinct successor identity;
- replaces boolean quarantine flags with an exact versioned replacement-evidence packet;
- requires exact replacement-set equality, candidate/policy/result/artifact bindings, and reachable exact artifact bytes;
- models retention loss/restoration as event lineage on one stable ArtifactIdentity;
- preserves required `NOT_RUN` versus `NOT_APPLICABLE`, PRODUCT/INFRA/FLAKY behavior, expiry, and provider-independent scope.

The finding-dispositions artifact explicitly closes the 2 MAJOR / 1 MINOR pre-gate findings with mechanical evidence rather than waiver.

## Exact corrected evidence

- fixture digest: `2f07e41bccd8eef9e35ad7bc03e2aad7b6792a62cfc6d1560b933a814604c988`;
- harness-contract digest: `9963302d28ed3057a4e46070b462a91e45aebef6f57829569a3bafe57a53700a`;
- result-object digest: `b2905c4cf9095ba70c42770505073dc21d616996316f2dc800293d78ca8ea057`.

The exact embedded Appendix A was re-executed after the harness-identity correction and reproduces these three digests plus the 16-scenario aggregate matrix.

## Review finding dispositions

- `PG-M01` MAJOR — RESOLVED: quarantine replacement is exact, version/candidate/artifact bound, with missing/arbitrary/wrong-artifact/wrong-policy negative probes.
- `PG-M02` MAJOR — RESOLVED: exact candidate identity + append-only envelope chain; reset/fork negative probe; distinct successor positive case.
- `PG-m01` MINOR — RESOLVED: stable artifact identity + ordered loss/exact-restore/wrong-hash event lineage.

## Self-review

Final remediation self-review against Issue #91 acceptance criteria:

- BLOCKER: 0;
- MAJOR: 0;
- correction-requiring MINOR: 0;
- exact source provenance retained: PASS;
- all pre-gate findings dispositioned: PASS;
- arbitrary quarantine evidence cannot satisfy: PASS;
- same-candidate reset cannot erase negative history: PASS;
- retention restoration keeps stable identity/event history: PASS;
- executable fixture digests reproduce: PASS;
- provider mechanics remain explicitly experimental/noncanonical: PASS;
- production/readiness/canonicalization authority leakage: none identified.

A self-review provenance defect in the first remediation draft was corrected before this handoff: the harness identity is now an explicit canonical semantic object whose digest is reproduced by the embedded harness, rather than a source-format-dependent hash.

## Remaining risks / unresolved questions

- real INFRA-versus-PRODUCT classification authority remains unresolved;
- semantic adequacy/equivalence of quarantine replacements remains a later review question;
- a real provider/storage implementation may not enforce immutable lineage, expiry, or availability atomically;
- formal aggregate adversarial review has not run.

## Next action

Publish owner schema-3 `STATUS(REVIEW_READY)` for the exact final Issue #91 branch head and artifact blobs. Then leave `planning/issue-91` frozen.

Record durable linkage on Issue #77 that Issue #91 supersedes the frozen producer payload as the substantive CI evidence input for later `W2-REV-01`, while retaining Issue #77 as immutable provenance.

Do **not** treat this remediation, its self-review, a PR, or any future noncanonical main integration as the formal independent `W2-REV-01` disposition. No production implementation is authorized.
