# W2-ENG provider GHCR diagnostics remediation review

## Review identity

- mission: `W2-ENG-PROVIDER-GHCR-DIAG-REM-REV-01`
- review Issue: #474
- trust mode: `DEGRADED_SINGLE_AGENT`
- winning claim: Issue #474 comment `5309548763`
- producer session excluded: `frontier-drain-provider-ghcr-diag-rem-gpt56sol-20260816-01`
- judged remediation Issue: #472
- judged claim: `5309517951`
- judged terminal: `5309544191`
- judged implementation SHA: `933c5d1846f8d83ef2bc2d81f06a03bc1fa036c3`
- judged validator blob: `38ce3f46d4db05d7d0ca1bd7a1d3f2942465e1fd`
- exact immutable judged head: `fdfb75cf826594e2f320c75d9a9d3f90ac34d500`
- judged draft PR: #473
- judged base/current main at claim: `03b5ef07f164bef3ba1e730c654f7d4d69ac6a8c`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`

A later competing claim appeared after the winning claim and its immediate contention re-check. The deterministic review branch remained untouched at the exact base before this review write; no judged producer branch was modified.

## Disposition

`PASS_BOUNDED_PROVIDER_GHCR_DIAGNOSTICS`

Findings:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

The exact diagnostic candidate is clean for separately authorized squash publication as noncanonical provider-validator provenance. This review does **not** establish Epic entitlement, provider PASS, Unreal empirical eligibility, engine selection, implementation/readiness, commercial/production/legal/release authority, verification-PASS, decision authority, integration authority by review alone, or canonicality.

One fresh trusted-main credentialed evaluator run after publication is mandatory before any owner/external action is inferred.

## Frozen triggering evidence

The reviewed diagnostic correction follows a real post-Bearer-remediation trusted-main result:

- evaluator run `31970497548`, attempt 1;
- source head `03b5ef07f164bef3ba1e730c654f7d4d69ac6a8c`;
- job `95222119227`;
- sanitized artifact `9269648835`;
- Unreal credential was present/read;
- Unreal remained `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION` with blocker `EPIC_GHCR_AUTHORIZATION_OR_ENTITLEMENT_FAILED` and only collapsed final Registry status `401`;
- recorder run `31970508281` preserved that exact result at immutable evidence head `82f7f4468cb70259f5e1370d89a71f164250e5a9`;
- ownership-aware draft evidence PR #471 exists.

That historical result remains unchanged and is not interpreted as proof of an invalid PAT or missing Epic entitlement.

## Adversarial review

### 1. Frozen identity and scope — PASS

PR #473 is exact-head `fdfb75cf826594e2f320c75d9a9d3f90ac34d500`, draft and mergeable against exact base `03b5ef07f164bef3ba1e730c654f7d4d69ac6a8c`. Changed paths are exactly:

- `tools/planning/engine_provider_effective_validator.py`;
- `docs/planning/handoffs/issue-472.md`.

The executable diff is confined to GHCR diagnostic/refactor surfaces and their self-tests. No workflow, secret, evidence, provider contract or Unity-specific execution path changes.

### 2. Trace data boundary — PASS

`_empty_ghcr_auth_trace()` defines a closed scalar envelope containing only:

- HTTP status integers / `None`;
- booleans for challenge/exchange/retry facts;
- one bounded `failure_stage` string.

No raw header, URL, username, realm/service/scope value, request body, response body, cookie, Authorization value, PAT, Basic credential or bearer token is placed in the trace.

The only raw `WWW-Authenticate` value remains a local variable used to derive booleans and the already-reviewed bounded challenge object. That raw value is not returned in `registry_auth_trace`.

### 3. First resource request and path restriction — PASS

`registry_request()` still creates the exact GHCR resource URL from fixed origin `https://ghcr.io` plus internally generated provider paths. The first `_http_request()` carries only `Accept`, not provider Authorization.

The existing fail-closed path guard remains present and rejects empty, leading-slash, double-slash and backslash forms. Actual callers remain fixed to the Unreal repository tag-list or manifest path.

### 4. Challenge acceptance semantics — PASS

The prior clean-reviewed challenge parser was refactored into `_ghcr_challenge_details()` but the acceptance predicate is materially identical:

- `Bearer` scheme required;
- realm scheme exact HTTPS;
- host exact `ghcr.io`;
- no userinfo;
- port only default/443;
- path exact `/token`;
- no realm query or fragment;
- service exact `ghcr.io`;
- scope exact `repository:epicgames/unreal-engine:pull`;
- duplicate recognized challenge keys reject.

The additional booleans observe those checks; they do not relax them. `parse_ghcr_bearer_challenge()` delegates to the same exact predicate.

### 5. Credential destination and redirects — PASS

Basic username/PAT construction remains inside `_ghcr_bearer_token()` after exact challenge acceptance. The token request remains bound to the validated realm plus locally constructed service/scope query.

All HTTP requests continue through the existing no-redirect opener. The diagnostic change does not introduce an alternate HTTP client or redirect path. Authorization-bearing token or resource requests therefore still fail closed on redirects rather than forwarding credentials.

### 6. Token acceptance and non-emission — PASS

The token acceptance predicate remains materially unchanged:

- token endpoint HTTP 200;
- JSON object;
- `token` or `access_token` accepted only as a bounded string;
- conflicting simultaneous token fields rejected.

The function now returns only `(token_or_none, status, valid_bool)` to its immediate caller. Only status and validity are copied into the trace. The bearer itself stays local and is used only for the resource retry. Token endpoint response body is not copied to evidence.

### 7. Resource retry and decision semantics — PASS

A retry occurs only after exact challenge acceptance and valid token response. The exact original resource URL is retried with Bearer.

Diagnostic assignment occurs after the same request outcomes that already controlled behavior. No diagnostic field is used to authorize a request, set provider PASS, select a tag, or skip a downstream gate.

A retry failure remains a blocked provider result. A Registry-auth `SUCCESS` stage only means the Registry resource returned success; it is not mapped to `VALIDATED_DEVELOPMENT_ACCESS`.

### 8. Stage truthfulness — PASS

The stage mapping is deterministic and mutually ordered:

- initial 200 -> `SUCCESS`;
- initial non-401/non-200 -> `INITIAL_RESOURCE_FAILURE`;
- initial 401 without accepted challenge -> `CHALLENGE_MISSING_OR_REJECTED`;
- accepted challenge with token endpoint status not 200 -> `TOKEN_EXCHANGE_FAILED`;
- token endpoint 200 with invalid token body -> `TOKEN_RESPONSE_INVALID`;
- valid token but missing/non-200 resource retry -> `RESOURCE_RETRY_FAILED`;
- valid token plus successful retry -> `SUCCESS`.

The producer separately exercised this pure stage matrix and exact challenge helper without credentials. The code diff independently confirms the same state transitions.

### 9. Manifest auth diagnostics — PASS

The manifest request uses the same `registry_request()` helper. Only if manifest access fails does `validate_unreal()` attach that call's sanitized trace. Manifest headers/body and Authorization material are not included in the trace.

### 10. Downstream provider gates remain intact — PASS

After Registry tag access succeeds, the validator still requires all prior provider gates:

- observed vendor-published UE 5.8 tag;
- accessible manifest;
- `Docker-Content-Digest` identity;
- successful `docker login ghcr.io`;
- successful container pull;
- logout cleanup;
- digest-pinned image;
- executable Unreal editor discovery;
- native N1/N2/FI1 S3 pass.

Only final native execution success sets `VALIDATED_DEVELOPMENT_ACCESS`. The diagnostic trace cannot create provider PASS.

### 11. Provider independence / authority boundaries — PASS

The diff does not modify `derive_frontier()`. Unity and Unreal remain independently unlockable, the combined predicate is not used for individual unlock, and the historical 50 `NOT_RUN` cells remain preserved. Commercial, production, legal, release and engine-selection authority flags remain false.

The existing Unity service-account failure is outside this candidate and unchanged.

### 12. Producer executable-verification limitation — REVIEW-CLOSED

Producer #472 explicitly recorded that full branch `py_compile` and complete `--self-test` were not executed from the task branch. The review does not relabel those producer fields as executed PASS.

The exact patch was inspected against a known-valid reviewed predecessor. All changed Python blocks are structurally coherent: function signatures/call sites are updated consistently, tuple return arities match both `registry_request()` callers, and the newly added pure helper stage matrix was separately exercised without credentials.

More importantly for security/authority, the trusted-main evaluator has an existing fail-closed pre-secret gate: it executes `python3 -m py_compile` for the validator and then the validator `--self-test` **before** the later step that injects `UNITY_SERVICE_ACCOUNT_*` or `UNREAL_GITHUB_TOKEN`. Therefore any latent syntax/self-test defect after publication prevents credential consumption and provider execution rather than exposing secrets or creating false evidence.

This resolves the producer execution gap for bounded security publication without pretending the producer ran a test it did not run. The first post-publication trusted-main run remains the mandatory executable confirmation.

## Non-authority note

The new self-test's serialized-trace secret assertion is intentionally structural rather than a network-token fixture test; because the trace schema itself has no field carrying raw auth values and the credential-bearing code path is not exercised in self-test, this is not relied upon as the sole secret-isolation proof. The source-level dataflow and pre-existing evidence sanitization gate remain the controlling evidence.

No correction is required for the bounded diagnostic objective.

## Required next route

1. Open exact-head draft review PR and terminalize this review.
2. Publish review provenance only under separate convergence authority.
3. Publish the exact reviewed #472 candidate onto then-current `main` only if current-main compatible; if stale, use byte-equivalent recovery without semantic drift.
4. Let the trusted-main evaluator execute its pre-secret syntax/self-test gate and then one fresh credentialed provider evaluation.
5. Preserve the resulting recorder evidence and inspect only the new sanitized `registry_auth_trace.failure_stage` / safe statuses.
6. Request owner/PAT/Epic action **only** if that fresh evidence specifically demonstrates an external-auth stage rather than a repository implementation defect.

## Authority boundary

`NOT_CANONICAL` required security/authority review only. No provider credential/PASS, Unreal empirical eligibility, engine selection, implementation/readiness, commercial/production/legal/release, verification-PASS, decision, integration-by-review, or canonical authority is granted.
