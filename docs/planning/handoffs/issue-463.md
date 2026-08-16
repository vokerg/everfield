# Issue #463 handoff — W2-ENG-PROVIDER-GHCR-REM-01

## State

Producer remediation is ready for fresh required security/authority review after the exact-head draft PR is opened and terminal status is published.

## Scope

This episode repairs only Unreal GHCR Registry v2 authentication challenge handling in `tools/planning/engine_provider_effective_validator.py`.

It does **not** modify provider credentials, historical evidence, Unity provider semantics, engine selection, implementation/readiness, commercial/production/legal/release authority, verification-PASS authority, decision authority, or canonicality.

## Authority / provenance

- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner convergence directive: Issue #84 comment `5277825639`;
- owner parallel-frontier directive: Issue #84 comment `5305563203`;
- owner Unreal external-access-supplied directive: Issue #84 comment `5309426399`;
- winning Issue #463 claim: comment `5309438896`;
- base `main`: `886438990ed395cde2fad0ee6cb98ca6ade0f26f`.

## Fresh failure evidence that triggered remediation

Trusted-main evaluator run `31966257482`, attempt 2, job `95219881945`, read the configured Unreal credential and returned:

- Unreal state `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION`;
- blocker `EPIC_GHCR_AUTHORIZATION_OR_ENTITLEMENT_FAILED`;
- first registry status `401`;
- sanitized artifact `9269411306`.

Recorder run `31969621677` completed successfully and preserved that result on immutable branch `evidence/provider-effective-access/run-31966257482-attempt-2` at staged evidence commit `d43c498`. Historical attempt-2 evidence is not relabelled by this remediation.

## Root cause

The pre-remediation validator sent Basic credentials directly to a GHCR Registry resource and treated the first non-200 response as terminal entitlement failure. Registry v2 authentication is challenge/response: a protected resource may first return `401` plus `WWW-Authenticate: Bearer ...`; the client obtains a scoped bearer token and retries the original resource request.

Therefore the observed first-response `401` was insufficient to distinguish a normal registry challenge from a genuine authorization failure.

## Remediation

Implementation commit `d607c7ec1d99ee57b906bdd295665569741ba128`:

- performs an unauthenticated exact GHCR resource request first;
- accepts only an exact Bearer challenge for HTTPS `ghcr.io/token`, service `ghcr.io`, and scope `repository:epicgames/unreal-engine:pull`;
- rejects alternate schemes/hosts/ports/paths/query/fragment, wrong service/repository, broader `pull,push` scope, duplicate challenge keys, and non-Bearer challenges;
- sends Basic username/PAT only to the validated token realm;
- accepts only a bounded `token`/`access_token` response and rejects conflicting token fields;
- retries the exact resource URL with the short-lived bearer token;
- disables HTTP redirects for credential-bearing/token-bearing requests so authorization material is not forwarded to another origin;
- never returns or emits the PAT or bearer token;
- preserves existing exact UE 5.8 tag discovery, manifest digest binding, Docker login/pull/logout, pinned-image editor probe, native S3 execution, per-provider independent unlocks, and all authority flags.

## Producer-side verification

Executed against the remediation source:

- `python3 -m py_compile tools/planning/engine_provider_effective_validator.py`: PASS;
- `python3 tools/planning/engine_provider_effective_validator.py --self-test`: PASS;
- existing independent-provider and authority self-tests: PASS;
- added fail-closed GHCR challenge tests: PASS for exact challenge acceptance and rejection of HTTP realm, wrong host, wrong service, broader push scope, other repository, non-Bearer auth, and realm query injection;
- diff from base is confined to the validator plus this handoff;
- no provider secret value, hash, or bearer value is committed or recorded.

No credentialed Unreal execution is performed from this task branch. A fresh trusted-main provider run is required only after review and authorized integration.

## Required next step

One fresh independent/degraded-independent required security/authority review must attack:

1. challenge parser correctness and fail-closed behavior;
2. exact realm/service/scope binding;
3. redirect and credential-exfiltration resistance;
4. bearer-token non-persistence/non-emission;
5. false-PASS possibilities when token exchange or resource retry fails;
6. preservation of Unity behavior, provider independence, historical evidence, and authority boundaries.

Only a clean review may make the remediation eligible for separately authorized squash integration. After integration, obtain one fresh trusted-main provider run before changing Unreal empirical eligibility.
