# W2-ENG provider GHCR remediation review

## Review identity

- mission: `W2-ENG-PROVIDER-GHCR-REM-REV-01`
- review Issue: #466
- trust mode: `DEGRADED_SINGLE_AGENT`
- excluded producer session: `frontier-drain-provider-ghcr-rem-gpt56sol-20260816-01`
- judged remediation Issue: #463
- judged claim: `5309438896`
- judged terminal status: `5309463811`
- judged implementation SHA: `d607c7ec1d99ee57b906bdd295665569741ba128`
- exact immutable judged head: `aa2e377eddf63bc03b31b70cbbc7f4a33efaf7c3`
- judged draft PR: #465
- original judged base: `886438990ed395cde2fad0ee6cb98ca6ade0f26f`
- review base/current main at claim: `40179080013d742b70b4a5be611f1666dd3cd599`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- owner Unreal external-access-supplied directive: Issue #84 comment `5309426399`

The producer branch and PR were treated as immutable. No provider credentials were consumed in this review and no judged file was repaired from review.

## Disposition

`PASS_BOUNDED_PROVIDER_GHCR_REMEDIATION`

Findings:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

This disposition means only that exact remediation head `aa2e377eddf63bc03b31b70cbbc7f4a33efaf7c3` is security/authority-clean for a separately authorized, current-main-compatible squash publication or byte-equivalent recovery publication. It does **not** establish current Epic entitlement, provider PASS, Unreal empirical eligibility, engine selection, implementation/readiness, commercial/production/legal/release authority, verification-PASS, decision authority, or canonicality.

A fresh trusted-main credentialed provider execution remains mandatory after reviewed publication before Unreal state may change.

## Frozen triggering evidence

The reviewed correction is grounded in the immutable pre-remediation result:

- evaluator run `31966257482`, attempt 2;
- evaluator job `95219881945`;
- sanitized artifact `9269411306`;
- Unreal credential was configured/read;
- producer state: `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION`;
- blocker: `EPIC_GHCR_AUTHORIZATION_OR_ENTITLEMENT_FAILED`;
- first Registry response: HTTP `401`;
- recorder run `31969621677` succeeded and staged immutable evidence on `evidence/provider-effective-access/run-31966257482-attempt-2`, commit `d43c498`.

That historical evidence remains a failure result from the old validator. This review does not relabel it.

## Adversarial review

### 1. Frozen identity and scope — PASS

The exact judged head is the head recorded by Issue #463 terminal status and PR #465. The terminal diff contains exactly:

- `tools/planning/engine_provider_effective_validator.py`;
- `docs/planning/handoffs/issue-463.md`.

The substantive validator change is at `d607c7ec1d99ee57b906bdd295665569741ba128`. The only unrelated textual drift in the validator is removal/shortening of explanatory comments/docstring around unchanged Unity logic; no Unity executable semantics changed.

### 2. First resource request carries no provider credential — PASS

`registry_request()` constructs the resource URL from fixed origin `https://ghcr.io` plus an internally supplied repository path and performs the first request with only an `Accept` header. Neither the PAT nor Basic authorization is attached to that request.

The path guard rejects empty, leading-slash, double-slash, and backslash forms. All actual callers use the constant repository `epicgames/unreal-engine` plus fixed tag-list/manifest suffixes.

### 3. Credential use requires an exact Bearer challenge — PASS

A credential can reach `_ghcr_bearer_token()` only after:

1. the exact resource request returns `401`;
2. a `WWW-Authenticate` header is present;
3. the scheme is `Bearer`;
4. the parsed challenge passes the exact realm/service/scope checks.

Non-Bearer or malformed challenges return the original `401` path and therefore remain blocked.

### 4. Realm/service/scope fail closed — PASS

The challenge parser requires all of the following:

- scheme `https`;
- hostname exactly `ghcr.io`;
- no username or password in the realm URL;
- no non-default port;
- path exactly `/token`;
- no query or fragment supplied by the challenge;
- service exactly `ghcr.io`;
- scope exactly `repository:epicgames/unreal-engine:pull`.

A broader `pull,push` scope, alternate repository, alternate service, HTTP realm, alternate host, or challenge-controlled query therefore cannot route the provider credential.

Duplicate recognized challenge keys are rejected. Unrecognized attributes cannot change the validated realm/service/scope or credential destination.

### 5. Redirect / credential-exfiltration boundary — PASS

All HTTP activity in the new Registry helper uses an opener whose redirect handler returns no redirected request. Consequently:

- the Basic PAT request to the token endpoint cannot follow a redirect with authorization material;
- the Bearer retry cannot follow a redirect with bearer material;
- a redirect is observed as failure rather than as a new credential destination.

This is stricter than ordinary automatic redirect behavior and is fail-closed.

### 6. Token response handling — PASS

The token endpoint result is accepted only when:

- HTTP status is 200;
- body parses as a JSON object;
- `token` or `access_token` is a string within the bounded accepted length;
- if both fields are present, their values agree.

The PAT and bearer are kept in local variables only. Neither is added to the returned provider evidence. Existing top-level evidence flags remain `secret_values_in_evidence=false` and `secret_hashes_in_evidence=false`.

The bearer is used only as the `Authorization` header for retrying the exact original GHCR resource request.

### 7. First 401 is no longer a false terminal, but challenge success is not PASS — PASS

The old false-terminal behavior is removed: an initial `401` may now enter the bounded Bearer exchange.

The correction does not create a shortcut to provider validation. After a successful tag-list exchange the validator still requires, in order:

- an observed UE 5.8 vendor tag;
- accessible manifest;
- `Docker-Content-Digest` identity;
- successful `docker login ghcr.io`;
- successful container pull;
- logout cleanup;
- pinned digest image;
- executable Unreal editor discovery inside the pinned image;
- native S3 execution with all attempts passing.

Only the final native pass sets `VALIDATED_DEVELOPMENT_ACCESS`.

A failed Bearer exchange, failed retry, missing tag/digest, Docker failure, editor failure, or native S3 failure remains a blocked/inconclusive provider result rather than provider PASS.

### 8. Existing Unreal execution semantics preserved — PASS

Beyond the bounded auth helper and constant reuse, the UE 5.8 tag-selection regex, manifest-digest requirement, Docker login/pull/logout sequence, digest-pinned image use, editor probe, and native N1/N2/FI1 S3 execution are materially unchanged.

No engine-evidence scenario, workflow secret boundary, or provider contract was broadened by this remediation.

### 9. Provider independence and authority boundaries — PASS

`derive_frontier()` remains per-provider:

- Unity eligibility derives only from Unity `VALIDATED_DEVELOPMENT_ACCESS`;
- Unreal eligibility derives only from Unreal `VALIDATED_DEVELOPMENT_ACCESS`;
- the combined-provider predicate is recorded but explicitly not used for individual unlock.

The historical `NOT_RUN` preservation count remains 50. Commercial license authority, production authority, legal clearance, release authority, and engine selection remain false in the evidence model.

The remediation does not touch the independently observed Unity `exit 127` authentication defect.

### 10. Deterministic negative coverage — PASS

The producer self-test retains the previous empty-provider, independent-unlock, redaction, and commercial-authority checks and adds deterministic challenge checks for:

- exact Bearer challenge accepted;
- HTTP realm rejected;
- wrong host rejected;
- wrong service rejected;
- broader `pull,push` scope rejected;
- another repository rejected;
- non-Bearer challenge rejected;
- challenge realm query injection rejected.

The code was independently inspected rather than accepting those producer assertions as sufficient proof. The static control flow matches the intended fail-closed outcomes.

## Current-main drift / publication condition

After #463 terminalized, `main` advanced through separately owned reviewed S6 publication. At this review claim PR #465 therefore reported non-mergeable against the moved base even though its exact head remained unchanged.

This is **not** a security defect in the immutable judged remediation and does not require mutation of `planning/issue-463`. It is a convergence/publication condition. Any later integration must re-derive current `main` and use a separately authorized current-main-compatible squash publication or byte-equivalent recovery route while preserving the reviewed validator bytes/semantics and exact provenance.

The review disposition does not itself grant that integration authority.

## Required next state

1. Publish this review provenance only through a separately authorized, exact-head, squash-only route if current-main compatible.
2. Recover/publish the exact reviewed #463 remediation onto then-current `main` without changing its judged semantics if stale-base compatibility requires it.
3. After the reviewed remediation is present on trusted `main`, obtain one fresh credentialed provider execution.
4. Judge the fresh Unreal outcome exactly as observed. Do not infer entitlement or empirical eligibility from this review.

## Authority boundary

`NOT_CANONICAL` required security/authority review only. No provider credential/PASS, Unreal unlock, engine ranking/selection, implementation/readiness, commercial/production/legal/release, verification-PASS, decision, integration-by-review, or canonical authority is granted.
