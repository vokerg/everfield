# W2-PG-REM-CI-01 — Independent pre-gate review of corrected CI evidence

**Review mission:** `W2-PG-REM-CI-01` / Issue #97  
**Reviewed remediation:** `W2-REM-CI-01` / Issue #91  
**Reviewed work/head:** `0a256ae79880c759bcd698160adaaf3b302426d1`  
**Reviewed report blob:** `1b9436f0aa29a1340439596d4373521a05d28b7e`  
**Reviewed disposition blob:** `e76d6fc46c0360a61f6269bd73b2a2466ee3e25f`  
**Reviewed handoff blob:** `b3ac498060c09096f5e89c4e8c12825152b4f88b`  
**Source producer:** Issue #77 work/head `0011a9b02f1c7d8d20b81e0fb4faa6dec9bcae59`  
**Source pre-gate findings:** Issue #77 comment `5270075412`  
**Result:** `CHANGES_NEEDED`  
**Severity:** `0 BLOCKER / 3 MAJOR / 0 correction-requiring MINOR`

## 1. Scope and authority

This is a bounded independent pre-gate review of the exact frozen Issue #91 remediation payload. It does not edit or re-own `planning/issue-91`, does not replace the required aggregate `W2-REV-01`, and creates no production, readiness, canonicalization, CI-provider, or INFRA-classification authority.

The review attacked the executable Appendix A semantics rather than accepting the remediation prose or self-review. The original Issue #77 findings were used only as immutable provenance and attack targets.

## 2. Attack plan executed

1. Trace quarantine replacement validation from `replacement_ev` through `validate_quarantine` and the aggregate result object.
2. Trace same-candidate reset and successor-candidate handling through `CANDIDATES`, `validate_envelope_chain`, and `aggregate`.
3. Trace retained artifact identity through `art_state`, `latest_artifact_status`, and the published aggregate result.
4. Recheck `NOT_RUN` / `NOT_APPLICABLE`, PRODUCT/INFRA/FLAKY retry behavior, quarantine expiry, and authority limits for regressions.

The negative fixtures S7-S11/S13-S16 do close several original paths, but three load-bearing acceptance claims remain mechanically false or under-enforced.

## 3. Findings

### PG-REM-CI-M01 — MAJOR — quarantine replacement records still do not bind ArtifactIdentity and are not reconstructable from the result

Issue #91 requires each replacement to bind the exact expected ArtifactIdentity and requires exact replacement attempts/artifacts plus policy identity to be reconstructable from the result object. The harness does not satisfy that contract.

`replacement_ev(...)` carries only `replacement_id`, `candidate_id`, `policy_version`, `result`, and `artifact_key`. It carries no `artifact_id`, expected content hash, attempt/evidence-envelope identity, or immutable evidence record identity. `validate_quarantine(...)` verifies the `artifact_key` and then separately consults the global `artifact_states[spec["artifact_key"]]`; therefore the submitted replacement record itself never proves which ArtifactIdentity it claims to carry.

The aggregate result makes this weaker still: `result["checks"]` records only effective/satisfied/reason, and `result` does not retain `replacement_evidence` at all. A downstream reviewer cannot reconstruct which exact replacement records were supplied from the canonical result object.

Mechanical counterexample: the published `VALID_REPLACEMENTS` contain no artifact identity fields and nevertheless produce S6 `SATISFIED`. This directly violates Issue #91 acceptance criteria that exact replacement attempts/artifacts and policy identity be reconstructable from the result object.

**Required correction:** make each replacement evidence object bind at least exact replacement evidence/attempt identity, candidate, quarantine requirement/policy version, replacement ID, exact ArtifactIdentity (`artifact_id` + expected content hash or exact ref), result, and provenance/envelope. Validate those fields against the policy and retain the exact records (or immutable refs/digest) in the aggregate result. Add a negative fixture in which correct replacement IDs/artifact keys point at a wrong or omitted ArtifactIdentity and require failure.

### PG-REM-CI-M02 — MAJOR — successor-candidate acceptance does not validate predecessor lineage

Issue #91 requires remediation to use a distinct successor candidate and to retain/reject prior same-candidate failure lineage deterministically. The fixture defines `cand-flaky-v2.supersedes = cand-flaky-v1`, but no validator consumes that relation.

`validate_envelope_chain(...)` validates only envelopes for one `candidate_id`. `aggregate("remediated", ...)` accepts `env-remediated-1` as a fresh root because first-envelope predecessor must be null. S12 therefore becomes `SATISFIED` without supplying or validating any predecessor candidate envelope, predecessor work/evidence identity, or transition record from `cand-flaky-v1`.

The static `supersedes` string in `CANDIDATES` is descriptive fixture metadata, not an enforced chain. Consequently the harness proves that a named new candidate can start clean; it does not prove that a claimed remediation successor is linked to the failed predecessor whose negative history motivated the new candidate identity.

**Required correction:** introduce an explicit candidate transition/supersession record with predecessor candidate identity, successor candidate identity, changed-work identity/reason, and predecessor evidence root/digest. Validate successor admission against that record and retain it in the aggregate result. Add negative fixtures for missing predecessor evidence, wrong predecessor, and an unchanged/same candidate masquerading as a successor.

### PG-REM-CI-M03 — MAJOR — retained artifact identity is stripped from the published result object

The runtime `artifact_states` structure has `artifact_id`, `expected_hash`, and ordered events, and `latest_artifact_status(...)` correctly checks current reachability/hash. However the aggregate result serializes only:

`"artifact_event_lineage": {k: v["events"] ...}`

It omits both `artifact_id` and `expected_hash`. S13-S15 therefore test one in-memory state object correctly, but the published canonical result object cannot prove that outage and restoration events belong to one exact ArtifactIdentity or what hash was authoritative. This conflicts with Issue #91's requirement that restoration use one stable evidence/artifact identity and that exact identity plus lineage be reconstructable from the result object.

**Required correction:** serialize the full stable artifact identity record (or exact immutable ref/digest) together with event lineage into the result. Add a negative reconstruction fixture showing that swapping an artifact identity while replaying the same event list cannot preserve authority.

## 4. Preserved behavior that passed attack

No additional correction is required in this pre-gate scope for the following bounded semantics:

- required conditional evidence remains distinct from `NOT_APPLICABLE`; S2 leaves conditionally required package evidence `NOT_RUN` and gates the aggregate;
- PRODUCT failure is retained across later same-envelope PASS in S3;
- explicitly classified INFRA failures may be retried only under the declared `allow_infra_retry` rule and still remain in attempt lineage;
- explicit FLAKY remains gating in S5;
- quarantine requires exact replacement key-set equality, so missing/extra/arbitrary replacement IDs fail closed;
- wrong replacement policy and quarantine expiry fail closed;
- same-candidate second root envelope is rejected within one supplied candidate-envelope chain;
- unavailable and wrong-hash artifact states reopen aggregate authority in the in-memory evaluation;
- provider mechanics, universal INFRA classification, implementation readiness, and canonicalization remain explicitly unclaimed.

These passes do not cure M01-M03 because the missing bindings are exactly at the durable evidence/result-object boundaries required for later authority reconstruction.

## 5. Disposition

`CHANGES_NEEDED` before Issue #91 should be treated as a clean substantive CI input to `W2-REV-01`.

The frozen Issue #91 `STATUS(REVIEW_READY)` remains immutable provenance. Do not edit `planning/issue-91`. Route M01-M03 to one bounded remediation successor that recreates the corrected noncanonical payload on a new branch and preserves Issue #91 as source provenance.

Formal `W2-REV-01` remains the only declared aggregate independent review authority. This pre-gate result does not authorize integration, implementation, readiness, or canonicalization.
