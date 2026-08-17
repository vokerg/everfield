# Issue #501 handoff — W2-ENG-PROVIDER-UNITY-AUTOAUTH-AMBIG-REM-REV-01

## State

Required security/authority review of Issue #499 / draft PR #500 is complete with disposition `PASS_BOUNDED_PROVIDER_UNITY_AUTOAUTH_AMBIG_REMEDIATION`.

Findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**. Trust profile: `DEGRADED_SINGLE_AGENT`.

## Exact judged remediation

- producer/remediation Issue #499;
- terminal producer comment `5311082200`;
- draft PR #500;
- exact base `8d4c8e29fc01c60fc757a0f77bdd45e3c8cae4e4`;
- exact head `cbcc41156984f237299fa3f6cd64f042df755aa5`;
- corrected validator blob `112e8140a145fdf80556414358dbdd524416f9fa`;
- carried Issue #495 handoff blob `0bce92d35109b39f9e5dd71b0869f8c483dd65cf`;
- remediation handoff blob `b2522465a90b03697e323210ee0ebda480df1ca3`;
- exact changed paths: `docs/planning/handoffs/issue-495.md`, `docs/planning/handoffs/issue-499.md`, and `tools/planning/engine_provider_effective_validator.py`.

Frozen predecessor: Issue #495 / PR #496 head `9ea697d0b00f41a52940d37c6c3da14fc575abdf`, validator blob `d73399df23e29f84607056a972f3fc80e3d49b88`. Frozen prior required review: Issue #497 terminal comment `5311026366`, PR #498 head `838f5e3a32cb37575a93252c6fc912c31d208bb6`, `CHANGES_NEEDED`, finding `W2-ENG-PROVIDER-UNITY-AUTOAUTH-REV-M01`.

## Review result

The bounded finding is closed. The exact final validator rejects every top-level `active` marker before reading nested `data.active` and adds a deterministic regression proving `{"active": false, "data": {"active": true}}` fails closed. Relative to the exact frozen #495 validator, the correction is confined to the two-line guard and two-line regression addition; no judged producer line is deleted.

Exact nested active/inactive envelopes remain accepted with their correct boolean values. Missing, non-boolean, top-level-only, conflicting, malformed, and structurally incomplete envelopes remain rejected.

The rest of the automatic service-account path remains materially unchanged: service-account credentials are environment-only and redacted; browser/session login is not a prerequisite; `unity license status` is the first authenticated unattended command; command failure/timeout or malformed status cannot become authentication/license success; inactive license remains a specific blocker; exact Unity `6000.5.6f1` editor/native-S3 gates remain downstream.

Unreal/GHCR and per-provider independence remain unchanged. The intermediate accidental Unreal `and`→`&&` drift is absent from the frozen final validator.

## Verification boundary

No provider credential execution occurred from the remediation or review branch. Trusted-main workflow blob `94b740e1b9ca25fc6c23b767d681cc21a497cfac` still performs exact trusted-main source fencing, pinned Unity CLI resolution, `py_compile`, and the complete validator `--self-test` before the following step receives provider Secrets.

This clean review is not empirical provider evidence. It does not prove Unity authentication, an active license, editor installation, native S3, or provider PASS.

## Required next route

Owner convergence permits terminal review artifacts to be squash-published as noncanonical review provenance once exact current-main compatibility is established. Publication of the reviewed implementation is a separate integration episode requiring its own fresh current-main, exact-head, mergeability and authority fence; review PASS alone is not integration-by-review.

After reviewed implementation publication, one fresh trusted-main evaluator/recorder episode remains mandatory, including the pre-secret `py_compile` and full self-test gate. Only that fresh observed outcome may advance the Unity provider frontier. Unreal remains independently human-gated.

## Authority boundary

`NOT_CANONICAL`. Required review provenance only. No provider credential/PASS, Unity license authority, engine selection, implementation readiness, commercial/production/legal/release authority, verification-PASS, decision, integration-by-review, or canonical authority.
