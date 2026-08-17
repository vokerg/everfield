# Issue #497 handoff — W2-ENG-PROVIDER-UNITY-AUTOAUTH-REM-REV-01

## State

Required security/authority review is complete with disposition `CHANGES_NEEDED`.

Findings: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**. Trust profile: `DEGRADED_SINGLE_AGENT`.

## Judged immutable candidate

- producer Issue #495;
- producer draft PR #496;
- exact judged base/current main `d7a749bb38a73d08ba63ad62296781b6d0b4c0ea`;
- exact judged head `9ea697d0b00f41a52940d37c6c3da14fc575abdf`;
- exact validator blob `d73399df23e29f84607056a972f3fc80e3d49b88`;
- exact changed paths: `tools/planning/engine_provider_effective_validator.py` and `docs/planning/handoffs/issue-495.md`;
- triggering evaluator run/job `31972340061` / `95226573282`;
- trusted-main credentialed evaluator workflow blob `94b740e1b9ca25fc6c23b767d681cc21a497cfac`.

## Blocking finding

`W2-ENG-PROVIDER-UNITY-AUTOAUTH-REV-M01` / `MAJOR`.

`unity_license_status_envelope()` correctly rejects missing, non-boolean, and top-level-only `active`, but it does not reject a conflicting top-level marker when a nested `data.active` boolean is also present. A payload such as `{"active": false, "data": {"active": true}}` is accepted as a valid active license envelope. That violates the explicit fail-closed requirement for top-level/ambiguous values and can false-validate both transport/authentication and license state.

Required remediation is bounded: reject conflicting/top-level `active` ambiguity whenever the structured `data.active` envelope is present, and add deterministic self-tests for conflicting nested/top-level booleans. Preserve the automatic service-account bearer path, environment-only credentials, process-failure behavior, inactive-license blocker, exact Unity 6000.5.6f1 editor/native-S3 gates, Unreal/GHCR semantics, provider independence, and all authority boundaries.

## Clean review surfaces

The service-account CI path correctly removes browser/session login/status prerequisites; `unity license status` is the first credentialed unattended command; credentials remain environment-only and redacted; process failure/timeout cannot become license state; structured inactive license cannot become provider PASS; editor/native-S3 and Unreal/GHCR behavior are otherwise materially unchanged.

Exact trusted-main workflow ordering is preserved: source identity and Unity CLI resolution precede `py_compile` plus full validator `--self-test`, and provider Secrets are introduced only in the following credentialed validation step. No credentialed branch execution occurred and no empirical provider result is inferred by this review.

## Next route

Create exactly one bounded blocking remediation successor for `W2-ENG-PROVIDER-UNITY-AUTOAUTH-REV-M01`, then require one fresh security/authority review of the corrected exact head before implementation publication. After clean reviewed publication, one fresh trusted-main evaluator/recorder episode remains mandatory.

The exact review draft PR/head is bound by the terminal schema-3 status on Issue #497 after PR creation.

## Authority boundary

`NOT_CANONICAL`. Review provenance only. No integration-by-review, provider credential/PASS, Unity license authority, engine selection, readiness, production/commercial/legal/release, verification-PASS, decision, or canonical authority.
