# Issue #472 handoff — W2-ENG-PROVIDER-GHCR-DIAG-REM-01

## State

Diagnostic remediation candidate is ready for one fresh required security/authority review.

## Exact authority / provenance

- claim: Issue #472 comment `5309517951`;
- branch: `planning/issue-472`;
- base/current-main at claim: `03b5ef07f164bef3ba1e730c654f7d4d69ac6a8c`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- owner convergence directive: Issue #84 comment `5277825639`;
- owner Unreal external-access-supplied directive: Issue #84 comment `5309426399`;
- prior clean GHCR remediation review: Issue #466 terminal `5309484055`, disposition `PASS_BOUNDED_PROVIDER_GHCR_REMEDIATION`;
- reviewed pre-diagnostic validator blob on `main`: `66696dd6a7d5b8a228aef0010cf64ffd233827bb`.

## Triggering fresh evidence

Post-reviewed-remediation trusted-main evaluator:

- run `31970497548`, attempt 1;
- source head `03b5ef07f164bef3ba1e730c654f7d4d69ac6a8c`;
- job `95222119227`;
- sanitized artifact `9269648835`;
- Unreal credential present/read;
- Unreal result `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION`;
- blocker `EPIC_GHCR_AUTHORIZATION_OR_ENTITLEMENT_FAILED`;
- only collapsed final Registry status retained: `401`.

Recorder run `31970508281` completed and preserved this result on immutable evidence branch `evidence/provider-effective-access/run-31970497548-attempt-1` at exact head `82f7f4468cb70259f5e1370d89a71f164250e5a9`; ownership-aware draft evidence PR #471 exists. Historical evidence is not relabelled by this remediation.

## Diagnostic gap

The reviewed Bearer-flow is now active on trusted `main`, so the old first-resource-401 false-terminal defect is no longer sufficient to explain the fresh failure. The current validator still collapses distinct Registry-auth stages into one terminal status, preventing a justified decision between repository remediation and owner/external access action.

## Candidate implementation

Implementation commit: `933c5d1846f8d83ef2bc2d81f06a03bc1fa036c3`.

Validator candidate blob: `38ce3f46d4db05d7d0ca1bd7a1d3f2942465e1fd`.

The candidate preserves the reviewed decision path and adds only a sanitized `registry_auth_trace` when Registry authentication blocks Unreal. The trace contains scalar statuses/booleans and one bounded stage enum only:

- `initial_status`;
- `challenge_present`;
- `challenge_scheme_bearer`;
- `challenge_realm_matches`;
- `challenge_service_matches`;
- `challenge_scope_matches`;
- `challenge_accepted`;
- `token_exchange_attempted`;
- `token_exchange_status`;
- `token_response_valid`;
- `resource_retry_attempted`;
- `resource_retry_status`;
- `failure_stage`.

Allowed stage values:

- `INITIAL_RESOURCE_FAILURE`;
- `CHALLENGE_MISSING_OR_REJECTED`;
- `TOKEN_EXCHANGE_FAILED`;
- `TOKEN_RESPONSE_INVALID`;
- `RESOURCE_RETRY_FAILED`;
- `SUCCESS`.

The trace does not contain the raw `WWW-Authenticate` value, PAT, Basic authorization, bearer token, token endpoint response body, cookie, raw authorization header, username, realm URL, service string, scope string, tag content, or manifest body.

## Preserved security / provider semantics

The candidate does not relax the clean-reviewed GHCR path:

- the first Registry resource request remains unauthenticated;
- only an exact Bearer challenge can route credentials;
- realm remains exact HTTPS `ghcr.io/token` with no userinfo/non-default port/query/fragment;
- service remains exact `ghcr.io`;
- scope remains exact `repository:epicgames/unreal-engine:pull`;
- authorization-bearing requests still use the no-redirect opener;
- token exchange still requires HTTP 200 and a bounded valid `token`/`access_token` object;
- exact resource retry still uses Bearer only after successful exchange;
- UE 5.8 tag discovery, manifest digest binding, Docker login/pull/logout, pinned-image editor discovery and native S3 remain unchanged;
- Unity logic and per-provider independent unlock semantics remain outside this diagnostic change;
- commercial/production/legal/release/engine-selection authority remains false.

## Producer-side verification

Observed exact diff before this handoff: one owned validator path only, 131 additions / 38 deletions, one commit ahead of base.

The newly added pure diagnostic helpers were independently exercised outside any credentialed environment for:

- exact challenge acceptance: PASS;
- stage `INITIAL_RESOURCE_FAILURE`: PASS;
- stage `CHALLENGE_MISSING_OR_REJECTED`: PASS;
- stage `TOKEN_EXCHANGE_FAILED`: PASS;
- stage `TOKEN_RESPONSE_INVALID`: PASS;
- stage `RESOURCE_RETRY_FAILED`: PASS;
- stage `SUCCESS`: PASS.

The branch also adds deterministic in-validator self-test cases for all six stages, the existing challenge negative cases, and serialized trace absence of fixture secret/bearer/authorization/cookie material.

A full branch `py_compile` / full-file `--self-test` execution was **not run from the task branch in this tool environment** because repository credential workflows are deliberately main-only and no uncredentialed arbitrary-branch runner is available. This is recorded as a verification limitation, not silently promoted to PASS. The fresh required review must inspect the exact candidate and may treat this as material if executable verification cannot be independently established.

No provider credential was consumed from this branch and no credentialed provider run was attempted.

## Required fresh review

Review exact frozen candidate only. Attack at least:

1. whether any raw challenge/header/token/body/credential can enter `registry_auth_trace` or exception/output paths;
2. whether the refactor changes accepted challenge semantics versus reviewed blob `66696dd6...`;
3. whether Basic auth remains confined to the exact validated token realm and redirects remain disabled;
4. whether stage mapping is truthful for non-401 initial responses, rejected challenges, failed token exchange, invalid token body, failed Bearer retry and success;
5. whether successful challenge/token exchange can accidentally inflate provider PASS;
6. whether tag/digest/Docker/pinned-editor/native-S3 gates are materially unchanged;
7. whether Unity and independent-provider/authority semantics are unchanged;
8. whether deterministic tests and syntax are sufficient for bounded publication.

Any semantic correction requires a new remediation successor; do not repair `planning/issue-472` from review.

## Required post-review route

Only after a clean review and separately authorized squash/current-main-compatible publication should one fresh trusted-main credentialed evaluator run be used to observe the exact `failure_stage`. Only that fresh evidence can justify either another repository remediation or owner/external credential/entitlement action.

## Authority boundary

`NOT_CANONICAL`. Diagnostic remediation only. No provider credential/PASS, Unreal empirical eligibility, engine selection, implementation/readiness, commercial/production/legal/release, verification-PASS, decision, integration, or canonical authority.
