# W2-ENG provider Unity automatic service-account bearer remediation review

## Review identity

- Issue #497 / `W2-ENG-PROVIDER-UNITY-AUTOAUTH-REM-REV-01`
- trust profile: `DEGRADED_SINGLE_AGENT`
- claim: `5311012916`
- judged producer: Issue #495 / draft PR #496
- judged base/current main: `d7a749bb38a73d08ba63ad62296781b6d0b4c0ea`
- judged exact head: `9ea697d0b00f41a52940d37c6c3da14fc575abdf`
- judged validator blob: `d73399df23e29f84607056a972f3fc80e3d49b88`
- judged paths exactly:
  - `tools/planning/engine_provider_effective_validator.py`
  - `docs/planning/handoffs/issue-495.md`
- trusted-main credentialed evaluator workflow blob: `94b740e1b9ca25fc6c23b767d681cc21a497cfac`
- triggering evaluator run/job: `31972340061` / `95226573282`

## Disposition

`CHANGES_NEEDED`

Findings: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

## Finding W2-ENG-PROVIDER-UNITY-AUTOAUTH-REV-M01 — ambiguous license envelope can false-validate auth/license

Severity: `MAJOR`.

The new `unity_license_status_envelope()` accepts any dictionary whose nested `data.active` is a boolean and ignores a conflicting top-level `active` marker. For example, the malformed/ambiguous response:

```json
{"active": false, "data": {"active": true}}
```

is accepted as `(envelope_valid=True, license_active=True)`.

That violates the explicit review contract that only an unambiguous structured `data.active` boolean may validate the envelope and that top-level/ambiguous values fail closed. Because `validate_unity()` sets `authentication_validated = ok(license_status) and envelope_valid` and then `license_validated = license_active is True`, a successful process carrying this conflicting envelope can incorrectly validate both transport/authentication and license state. The later editor/native-S3 gates still remain, but this is nevertheless an authority-significant false-positive at two prerequisite gates and therefore blocks bounded PASS.

The producer self-test covers top-level-only `{"active": true}` but does not attack conflicting nested/top-level markers, so it would not detect this failure mode.

Required correction: make the license-status envelope parser reject conflicting/ambiguous active markers, including any top-level `active` occurrence alongside `data.active`, and add deterministic self-tests for conflicting top-level/nested active booleans. Keep the accepted contract narrowly scoped to the documented structured `data.active` boolean.

## Other adversarial attacks

1. **Frozen identity and scope:** PASS. PR #496 is open, draft, mergeable at review freeze, exact head `9ea697d0b00f41a52940d37c6c3da14fc575abdf`, base `d7a749bb38a73d08ba63ad62296781b6d0b4c0ea`, with exactly the validator plus Issue #495 handoff changed.
2. **Browser/session prerequisite removal:** PASS for the service-account CI path. `validate_unity()` no longer invokes `unity auth login` or `unity auth status`; the first credential-bearing unattended command is `unity license status`. The separate local already-licensed proof path is not the service-account CI authority path.
3. **Credential transport:** PASS. `UNITY_SERVICE_ACCOUNT_ID` / `UNITY_SERVICE_ACCOUNT_SECRET` remain environment-only through `unity_service_account_env()`; they are not placed in argv or stdin, and `run()` receives both as redaction secrets.
4. **Process failure/timeout semantics:** PASS. Authentication requires both `ok(license_status)` and a valid envelope. Failure/timeout therefore cannot become an inactive-license result.
5. **Inactive structured license:** PASS. An accepted `data.active=false` can validate transport/authentication but sets `license_validated=false`, returns `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION`, and cannot produce provider PASS.
6. **Editor/native S3 gates:** PASS. After active-license validation, the exact Unity `6000.5.6f1` install/list/discovery and native S3 path remain downstream. No diff hunks modify the native harness or editor-discovery logic.
7. **Unreal/GHCR/provider independence:** PASS. No Unreal/GHCR or frontier-derivation hunk is changed; the full existing GHCR self-test set remains present.
8. **Trusted-main pre-secret verification:** PASS as a publication prerequisite, not as branch execution evidence. Exact workflow blob `94b740e1b9ca25fc6c23b767d681cc21a497cfac` restricts execution to trusted repository `main`, verifies exact checkout identity, installs/resolves the pinned Unity CLI, then runs `python3 -m py_compile` on the validator/recorder and the full validator `--self-test` before any step introduces provider Secrets. The producer branch did not run credentialed tests, and this review does not promote review-time inspection to empirical provider evidence.
9. **Authority boundaries:** PASS. Authentication, license, editor/native provider access, engine selection, readiness, commercial/production/legal/release, verification, decision, integration and canonical authority remain separate.

## Required next route

Route one bounded blocking remediation for `W2-ENG-PROVIDER-UNITY-AUTOAUTH-REV-M01`. The remediation should change only the validator plus its handoff, reject conflicting/top-level active ambiguity fail-closed, and add deterministic counterexample coverage. A fresh required security/authority review of the corrected exact candidate remains mandatory before any publication of implementation bytes.

After a clean reviewed publication, one fresh trusted-main evaluator/recorder episode remains mandatory before any provider/auth/license conclusion can advance.

## Authority boundary

`NOT_CANONICAL`. Required review provenance only. `CHANGES_NEEDED` grants no integration-by-review, provider credential/PASS, Unity license authority, engine selection, readiness, production/commercial/legal/release, verification-PASS, decision, or canonical authority.
