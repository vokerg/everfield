# Issue #622 handoff — bounded Unreal PAT identity diagnostic

Mission: `W2-ENG-PROVIDER-GHCR-IDENTITY-DIAG-01`

## State

Substantive implementation is complete on the claimed task branch. The branch
adds a validator-local, secret-safe GitHub API probe that runs only when the
existing trusted-main Unreal GHCR path fails before tag discovery. It does not
rotate credentials, broaden scopes, alter protected Environment names, or
change the provider unlock predicate.

## Immutable inputs

- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- task claim: Issue #622 comment `5371864346`;
- source main / claim base: `015ac1d6bc27675c440487e60d54cd2c6e8da273`;
- substantive commit: `0574466`;
- source trigger: trusted-main evaluator run `32434985056`, attempt `1`;
- source artifact: `9430425271`;
- observed prior stage: GHCR challenge accepted, token exchange `403`,
  resource retry not attempted.

## Implementation

`tools/planning/engine_provider_effective_validator.py` now:

1. calls only three fixed `api.github.com` paths using the existing PAT in
   memory and a no-redirect opener;
2. projects only bounded API statuses, sanitized login, expected-login
   comparison, recognized `X-OAuth-Scopes` names, membership-active status,
   SSO-header presence, redirect rejection, the GHCR exchange status, and one
   bounded diagnostic code;
3. never serializes the PAT, Authorization header, response bodies, raw SSO
   URL, cookies, or hashes;
4. leaves all GHCR bearer validation, UE 5.8 identity, Docker, editor, native
   S3, provider-independence, and authority boundaries unchanged;
5. runs offline mock-only self-tests for invalid identity, expected
   `read:packages`, insufficient scope, active EpicGames membership, SSO,
   package status, malformed/redirect responses, and secret/body isolation.

The diagnostic is attached only to the sanitized source artifact when the
initial Unreal registry request is blocked. Existing fixed recorder projection
and historical evidence remain unchanged; the source run/artifact binding is
the durable handoff identity for this bounded diagnostic episode.

## Verification

Passed on the task branch:

- `python3 -m py_compile tools/planning/engine_provider_effective_validator.py`;
- `python3 tools/planning/engine_provider_effective_validator.py --self-test`;
- `git diff --check`;
- exact changed-path check: validator only before this handoff;
- no protected secret was consumed on the planning branch.

The self-test result was
`W2-ENG-PROVIDER-EFFECTIVE-ACCESS-SELFTEST-v1`, `pass: true`, with all
existing GHCR/Unity authority cases and the new GitHub probe cases passing.

## Required continuation

1. Commit this handoff as the second task-branch commit.
2. Re-fetch current `main`, re-check Issue #622 ownership and the remote task
   branch, then open an exact-head draft PR to `main`.
3. Verify draft PR base/head/files and publish terminal
   `STATUS(REVIEW_READY)` with the exact terminal head and handoff path.
4. Route one fresh independent/degraded-independent security/authority review
   of the immutable branch. Attack token/header/body isolation, fixed-host and
   redirect behavior, scope/SSO interpretation, package-status ambiguity,
   false identity/PASS risk, and preservation of downstream Unreal gates.
5. If clean, use the separately authorized squash-only integration route and
   re-fetch `main` before triggering one fresh trusted-main evaluator. Inspect
   only the bounded `github_access_probe` plus existing `registry_auth_trace`.

## Authority boundary

`NOT_CANONICAL`. This handoff grants no provider PASS, Unreal entitlement,
engine selection, implementation/readiness, commercial/legal/release,
verification-PASS, decision, integration, or canonical authority. A fresh
trusted-main result is required before any exact external action is inferred.
