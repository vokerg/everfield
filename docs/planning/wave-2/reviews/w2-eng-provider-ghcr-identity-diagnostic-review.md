# W2-ENG provider GHCR identity diagnostic review

## Review identity

- mission: `W2-ENG-PROVIDER-GHCR-IDENTITY-DIAG-REV-01`
- review Issue: #624
- trust mode: `DEGRADED_SINGLE_AGENT`
- review claim: Issue #624 comment `5371939377`
- judged producer: Issue #622 / draft PR #623
- exact immutable judged head: `9adb6e25b47ff8740654c6b0cde0712ee0fbe38d`
- judged base/current main: `015ac1d6bc27675c440487e60d54cd2c6e8da273`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`

The producer branch and draft PR remained open, exact-head, and untouched. The
review branch contains only this report and its handoff; no provider secret was
consumed.

## Disposition

`PASS_BOUNDED_UNREAL_IDENTITY_DIAGNOSTIC`

Findings:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

The candidate is clean for separately authorized squash-only publication as
noncanonical Unreal provider diagnostic provenance. Review PASS does not prove
Epic entitlement, provider PASS, Unreal empirical eligibility, engine
selection, implementation/readiness, commercial/production/legal/release,
verification-PASS, decision authority, or integration authority.

## Frozen candidate and scope

The exact diff contains only:

1. `tools/planning/engine_provider_effective_validator.py`;
2. `docs/planning/handoffs/issue-622.md`.

The executable change runs only when the initial trusted Unreal GHCR resource
request is blocked. It does not rotate the PAT, broaden permissions, modify
protected Environment names, alter the provider unlock predicate, mutate
historical evidence, or change Unity behavior.

## Adversarial review

### Fixed host, paths, and redirects — PASS

The probe calls only three fixed `api.github.com` paths: `/user`, the
`EpicGames` membership endpoint, and the `unreal-engine` container package
endpoint. The existing no-redirect opener is reused and rejects redirects
before any credential-bearing follow-up. No caller-controlled host, path,
redirect target, raw URL, or Authorization value is emitted.

### Identity, scope, SSO, and package projection — PASS

The output is limited to HTTP statuses, a bounded GitHub login, expected-login
comparison, recognized scope names, active membership boolean, SSO-header
presence, redirect rejection, the existing GHCR exchange status, and one
bounded diagnostic code. Response bodies are parsed only for the bounded login
and membership fields and are never returned. The diagnostic distinguishes
invalid credentials, identity mismatch, insufficient scope/org authorization,
SSO-required, exchange success/continuation, GitHub API transient failure, and
remaining package/GHCR authorization failure without asserting an external
remediation.

### Secret and sensitive-data boundary — PASS

The PAT exists only as an in-memory argument to the fixed request helper. No
token, bearer value, Authorization header, cookie, response body, raw SSO URL,
hash, or secret-derived value is serialized. The fixture assertion checks that
the projected result contains none of the fixture secret, body text,
authorization, or cookie markers.

### False-PASS and downstream-gate resistance — PASS

The probe is diagnostic-only. It cannot select a UE tag, authorize a manifest,
authenticate Docker, pull an image, execute the editor, change native S3
results, or set `VALIDATED_DEVELOPMENT_ACCESS`. Existing GHCR bearer
validation, downstream engine/native gates, provider independence, historical
50-cell preservation, and authority flags remain unchanged.

### Executable verification — PASS

From an extracted archive of the immutable producer head:

- `python3 -m py_compile tools/planning/engine_provider_effective_validator.py` passed;
- `python3 tools/planning/engine_provider_effective_validator.py --self-test` passed;
- all existing and new self-test cases reported `true`.

The new fixtures cover expected identity/read scope/active EpicGames
membership, invalid identity, insufficient scope, SSO signal, package status,
redirect rejection, and projected-output secret/body isolation. No network or
protected credential was used.

## Review conclusion

No correction is required for the bounded diagnostic objective. The exact
candidate may proceed only through the separately authorized integration route,
followed by one fresh trusted-main credentialed evaluator run. That run must
be inspected only through the bounded `github_access_probe` and existing
`registry_auth_trace`; it must not be treated as provider PASS unless all
existing Unreal gates pass.

## Authority boundary

`NOT_CANONICAL` review provenance only. This review grants no provider
credential, entitlement, PASS, empirical eligibility, engine selection,
implementation/readiness, commercial/production/legal/release,
verification-PASS, decision, or integration authority.
