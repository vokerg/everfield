# Issue #495 handoff — W2-ENG-PROVIDER-UNITY-AUTOAUTH-REM-01

## State

Unity automatic service-account bearer candidate is ready for one fresh required security/authority review.

## Provenance

- Issue #495 claim `5309681597`;
- branch `planning/issue-495`;
- base `main@d7a749bb38a73d08ba63ad62296781b6d0b4c0ea`;
- triggering trusted-main evaluator run `31972340061`, job `95226573282`;
- immutable fresh evidence branch `evidence/provider-effective-access/run-31972340061-attempt-1`, head `376716b67cdedb24f2b3849bf4ff16d510c9e411`, draft evidence PR #494;
- independent Unreal human gate remains Issue #480.

## Triggering condition

The prior reviewed fixes removed the unsupported Unity auth flags and the unverified CLI path. Fresh trusted-main evidence then reached the real pinned Unity CLI and showed `auth login` timing out at the bounded 90-second timeout while service-account environment credentials were configured. No license conclusion was reached.

Official Unity CLI documentation/release notes establish that service accounts are intended for unattended CI and that when `UNITY_SERVICE_ACCOUNT_ID` and `UNITY_SERVICE_ACCOUNT_SECRET` are set, Unity CLI automatically generates bearer authentication for authenticated commands. A browser/session login is therefore not required as a prerequisite for the service-account environment path.

## Candidate implementation

The candidate preserves `unity_service_account_env()` and removes `unity auth login` / `unity auth status` from `validate_unity()`.

The first credentialed Unity command is now:

`unity license status`

under the exact service-account environment. The command is used for two separate facts:

1. **transport/authentication** — process exit must be successful and the response must match the explicit structured license-status envelope;
2. **license state** — only `data.active is true` sets `license_validated=true`.

A successful structured inactive response therefore proves that the service-account automatic bearer path reached the license service but remains a specific license blocker. A process failure, timeout, malformed JSON, missing `data`, missing/non-boolean `active`, or ambiguous envelope remains an authentication/transport failure and cannot become license/provider PASS.

The candidate adds pure deterministic tests for:

- active structured envelope accepted with active=true;
- inactive structured envelope accepted with active=false;
- missing `active` rejected;
- non-boolean `active` rejected;
- top-level/ambiguous `active` rejected;
- exact service-account environment construction.

Exact Unity baseline `6000.5.6f1`, editor install/list, editor discovery, native S3, Unreal/GHCR diagnostics, independent provider unlock semantics and historical authority boundaries remain unchanged.

## Security boundary

- service-account ID/secret remain environment-only;
- no Unity credential is placed in argv or stdin;
- existing `run()` secret redaction remains active;
- no browser/OAuth interactive fallback is accepted;
- authentication success is not license/provider PASS;
- license active is not provider PASS; exact editor/native S3 remain required;
- no credentialed execution occurs from the task branch.

## Verification limitation

The repository's credentialed evaluator is intentionally trusted-main-only. Full branch `py_compile` / complete validator `--self-test` are therefore not executed from this task branch and must not be silently promoted to PASS. The trusted-main workflow preserves its fail-closed pre-secret gate that runs both before provider Secrets are injected. Fresh required review must independently inspect exact source coherence and decide whether that gate is sufficient for bounded publication.

## Required review attacks

1. prove removal of browser/session login does not create an auth bypass;
2. verify structured license-status envelope parsing cannot false-pass ambiguous responses;
3. verify command failure/timeout cannot be reclassified as an inactive license;
4. verify successful inactive response proves only transport/auth, not license/provider PASS;
5. verify credentials remain environment-only and redacted;
6. verify exact Unity editor/native-S3 gates remain unchanged;
7. verify Unreal/GHCR and independent-provider semantics are unchanged;
8. attack syntax/self-test sufficiency under the pre-secret trusted-main gate.

## Required post-review route

After clean review and separately authorized publication, obtain one fresh trusted-main evaluator/recorder episode. Route only the exact observed next Unity state: transport/auth failure, inactive/active license, editor install/discovery, or native S3.

## Authority boundary

`NOT_CANONICAL`. Unity automatic-auth remediation only. No provider credential/PASS, Unity license authority, engine selection, readiness, commercial/production/legal/release, verification-PASS, decision, integration or canonical authority.