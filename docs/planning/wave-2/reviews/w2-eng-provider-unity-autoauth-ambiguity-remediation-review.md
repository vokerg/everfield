# W2-ENG provider Unity automatic-auth ambiguity remediation review

## Review identity

- Issue #501 / `W2-ENG-PROVIDER-UNITY-AUTOAUTH-AMBIG-REM-REV-01`
- trust profile: `DEGRADED_SINGLE_AGENT`
- claim: `5311088989`
- judged remediation: Issue #499 / draft PR #500
- judged exact base: `8d4c8e29fc01c60fc757a0f77bdd45e3c8cae4e4`
- judged exact head: `cbcc41156984f237299fa3f6cd64f042df755aa5`
- judged corrected validator blob: `112e8140a145fdf80556414358dbdd524416f9fa`
- frozen source producer: Issue #495 / PR #496 head `9ea697d0b00f41a52940d37c6c3da14fc575abdf`, validator blob `d73399df23e29f84607056a972f3fc80e3d49b88`
- frozen source required review: Issue #497 terminal comment `5311026366`, PR #498 head `838f5e3a32cb37575a93252c6fc912c31d208bb6`, disposition `CHANGES_NEEDED`
- finding under review: `W2-ENG-PROVIDER-UNITY-AUTOAUTH-REV-M01`
- trusted-main credentialed evaluator workflow blob: `94b740e1b9ca25fc6c23b767d681cc21a497cfac`
- judged paths exactly:
  - `docs/planning/handoffs/issue-495.md`
  - `docs/planning/handoffs/issue-499.md`
  - `tools/planning/engine_provider_effective_validator.py`

## Disposition

`PASS_BOUNDED_PROVIDER_UNITY_AUTOAUTH_AMBIG_REMEDIATION`

Findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

## Closure of W2-ENG-PROVIDER-UNITY-AUTOAUTH-REV-M01

The exact corrected validator closes the prior MAJOR finding fail-closed. Relative to the immutable judged #495 validator, the final correction adds the top-level ambiguity guard:

```python
if "active" in data:
    return False, None
```

and a deterministic conflicting-marker regression case for `{"active": false, "data": {"active": true}}`. Direct inspection of the two immutable validator blobs confirms these are the only semantic insertion sites needed for the finding: four added lines and zero deletions relative to the frozen producer validator.

The corrected parser therefore rejects any top-level `active` occurrence before consulting nested `data.active`. A successful process carrying a conflicting top-level/nested envelope cannot validate transport/authentication or license state.

## Adversarial attacks

1. **Frozen identity / scope — PASS.** PR #500 was frozen before judgment as open, draft, mergeable/clean, base `8d4c8e29fc01c60fc757a0f77bdd45e3c8cae4e4`, head `cbcc41156984f237299fa3f6cd64f042df755aa5`, with exactly the three routed paths above.
2. **Immutable producer carry — PASS.** The copied Issue #495 handoff in PR #500 has blob `0bce92d35109b39f9e5dd71b0869f8c483dd65cf`, exactly matching the handoff at immutable producer head `9ea697d0b00f41a52940d37c6c3da14fc575abdf`.
3. **Conflicting active markers — PASS.** `unity_license_status_envelope({"active": false, "data": {"active": true}})` is rejected. The same top-level guard also rejects the opposite conflicting polarity.
4. **Valid nested active/inactive — PASS.** Exact `{"data":{"active":true}}` remains accepted as `(True, True)` and exact `{"data":{"active":false}}` remains accepted as `(True, False)`.
5. **Malformed/top-level-only envelopes — PASS.** Missing `data.active`, non-boolean `data.active`, top-level-only `active`, non-dictionary envelopes, and missing/non-dictionary `data` remain rejected.
6. **Automatic service-account path — PASS.** The rest of the judged #495 path is materially unchanged: credentials remain in `UNITY_SERVICE_ACCOUNT_ID` / `UNITY_SERVICE_ACCOUNT_SECRET` environment variables; no browser/session login prerequisite is added; `unity license status` remains the first authenticated unattended command; command failure/timeout or invalid JSON/envelope fails closed; a structured inactive license remains a specific blocker and cannot provider-pass.
7. **Exact Unity downstream gates — PASS.** Unity baseline `6000.5.6f1`, editor install/list/discovery, native S3 N1/N2/FI1, and the requirement for native execution before `VALIDATED_DEVELOPMENT_ACCESS` remain unchanged from the judged producer.
8. **Unreal/GHCR/provider independence — PASS.** Final corrected validator preserves the judged Unreal Registry/GHCR challenge, token-exchange, digest, Docker and native-S3 logic and the independent per-provider frontier. The intermediate accidental `and`→`&&` Unreal drift documented by #499 is absent from the frozen final validator; the final embedded Unreal Python script retains valid Python `and` semantics.
9. **Credential boundary / branch execution — PASS.** No provider credential execution is claimed or performed from the remediation or review branch. The current trusted-main workflow still checks exact trusted-main source identity, resolves the pinned Unity CLI, then runs `python3 -m py_compile` plus the complete validator `--self-test` before the following step introduces provider Secrets.
10. **Stale-base handling — PASS.** #499 was re-materialized on `main@8d4c8e29fc01c60fc757a0f77bdd45e3c8cae4e4` after publication of the #497/#498 `CHANGES_NEEDED` review provenance. PR #500 is mergeable against that exact base without modifying the frozen #495/#496 or #497/#498 provenance branches.
11. **Authority discipline — PASS.** This review establishes only that the bounded parser-ambiguity remediation is clean. It does not establish Unity authentication, an active Unity license, editor/native-S3 execution, provider PASS, engine selection, implementation readiness, release, verification-PASS, decision or canonical authority.

## Required next route

A separately governed noncanonical publication of the clean reviewed remediation may proceed only after a fresh exact current-main/expected-head compatibility and integration-authority check, using squash-only integration. Review provenance may likewise be published separately under the owner convergence rule for terminal review artifacts.

After implementation publication, the trusted-main pre-secret `py_compile` plus full validator `--self-test` gate and one fresh credentialed evaluator/recorder episode remain mandatory. Only the exact observed provider state from that trusted-main episode may advance the Unity provider frontier. Unreal remains independently authority-gated.

## Authority boundary

`NOT_CANONICAL`. Required review provenance only. This PASS grants no integration-by-review, provider credential/PASS, Unity license authority, engine selection, implementation readiness, commercial/production/legal/release authority, verification-PASS, decision or canonical authority.
