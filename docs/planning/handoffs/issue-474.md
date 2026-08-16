# Issue #474 handoff — W2-ENG-PROVIDER-GHCR-DIAG-REM-REV-01

## Terminal review result

Disposition: `PASS_BOUNDED_PROVIDER_GHCR_DIAGNOSTICS`

Findings:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

Trust mode: `DEGRADED_SINGLE_AGENT`.

## Exact judged input

- remediation Issue #472;
- claim `5309517951`;
- terminal `5309544191`;
- implementation SHA `933c5d1846f8d83ef2bc2d81f06a03bc1fa036c3`;
- validator blob `38ce3f46d4db05d7d0ca1bd7a1d3f2942465e1fd`;
- exact terminal head `fdfb75cf826594e2f320c75d9a9d3f90ac34d500`;
- draft PR #473, exact head/base and mergeable at review claim;
- changed paths exactly validator + Issue #472 handoff.

A later competing Issue #474 claim appeared after winning claim `5309548763`; the deterministic branch was still at the exact base when this review episode began writing. The judged producer branch remained immutable.

## Review conclusion

The candidate is clean for bounded diagnostic publication because it adds only sanitized auth-stage observability and does not relax the previously reviewed GHCR authentication decision path.

Security properties confirmed from the exact patch:

- first Registry request remains unauthenticated;
- exact Bearer challenge predicate remains unchanged in substance;
- Basic PAT remains confined to exact validated HTTPS `ghcr.io/token`;
- authorization-bearing redirects remain disabled;
- PAT, Basic Authorization, bearer token, raw challenge, token response body and cookies are not copied into diagnostic evidence;
- diagnostic trace contains only safe status integers/`None`, booleans and one bounded stage enum;
- token acceptance and exact resource retry semantics remain unchanged;
- Registry-auth `SUCCESS` cannot create provider PASS;
- UE 5.8 tag, manifest digest, Docker login/pull/logout, digest-pinned editor and native S3 remain required;
- Unity/provider independence/historical authority boundaries remain unchanged.

Stage mapping is truthful for:

- `INITIAL_RESOURCE_FAILURE`;
- `CHALLENGE_MISSING_OR_REJECTED`;
- `TOKEN_EXCHANGE_FAILED`;
- `TOKEN_RESPONSE_INVALID`;
- `RESOURCE_RETRY_FAILED`;
- `SUCCESS`.

## Producer verification limitation disposition

Producer #472 did not run full branch `py_compile` / complete `--self-test`; this review does not rewrite those fields as executed PASS.

The exact source diff was inspected against a known-valid reviewed predecessor, including consistent function return/call arities and the added deterministic stage cases. The new pure diagnostic stage/challenge helpers were separately exercised without credentials.

The trusted-main evaluator also provides a fail-closed executable gate: `python3 -m py_compile` and validator `--self-test` run before the later step that injects `UNITY_SERVICE_ACCOUNT_*` or `UNREAL_GITHUB_TOKEN`. Therefore a latent syntax/test defect fails before secret consumption or provider evidence generation. The mandatory first post-publication trusted-main run is the executable confirmation.

This closes the producer runner limitation for bounded security publication without claiming a producer execution that did not happen.

## Required next route

1. Open exact-head draft review PR and terminalize #474.
2. Publish this review provenance only under separate convergence authority.
3. Publish exact #472 candidate onto then-current main if still compatible; otherwise recover byte-equivalently without semantic drift.
4. Obtain one fresh trusted-main evaluator run and matching recorder evidence.
5. Read only the sanitized `registry_auth_trace.failure_stage` and safe status/boolean fields.
6. Route the exact next action:
   - repository remediation if a parser/response/retry implementation defect is observed;
   - owner/external credential/entitlement action only if the fresh stage evidence specifically supports it;
   - continue downstream UE validation if Registry auth succeeds.

## Authority boundary

`NOT_CANONICAL`. Required security/authority review only. No provider credential/PASS, Unreal empirical eligibility, engine selection, implementation/readiness, commercial/production/legal/release, verification-PASS, decision, integration-by-review, or canonical authority.
