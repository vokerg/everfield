# Issue #466 handoff — W2-ENG-PROVIDER-GHCR-REM-REV-01

## Terminal review result

Disposition: `PASS_BOUNDED_PROVIDER_GHCR_REMEDIATION`

Findings:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

Trust mode: `DEGRADED_SINGLE_AGENT`.

## Exact judged input

- remediation Issue #463;
- claim comment `5309438896`;
- terminal comment `5309463811`;
- implementation SHA `d607c7ec1d99ee57b906bdd295665569741ba128`;
- immutable remediation head `aa2e377eddf63bc03b31b70cbbc7f4a33efaf7c3`;
- draft PR #465;
- original base `886438990ed395cde2fad0ee6cb98ca6ade0f26f`;
- exact changed paths: `tools/planning/engine_provider_effective_validator.py` and `docs/planning/handoffs/issue-463.md`.

## Review conclusion

The exact remediation safely replaces the pre-remediation first-`401` terminal classification with bounded Registry v2 Bearer challenge negotiation:

- first GHCR resource request carries no PAT;
- only an exact Bearer challenge can route credentials;
- credential destination is constrained to HTTPS `ghcr.io/token` with exact service `ghcr.io` and pull-only scope `repository:epicgames/unreal-engine:pull`;
- alternate realm/service/repository/broader scope/query forms fail closed;
- authorization-bearing requests do not follow redirects;
- PAT and bearer values are not emitted/persisted/hashed;
- a bearer exchange is not provider PASS;
- tag 5.8, manifest digest, Docker pull, pinned-image editor discovery and native S3 remain required;
- per-provider independent unlock semantics and all commercial/production/legal/release/selection authority boundaries remain unchanged.

The review did not consume provider credentials and does not prove current Epic entitlement.

## Current-main compatibility condition

Review claim/current-main base: `40179080013d742b70b4a5be611f1666dd3cd599`.

`main` advanced after #463 terminal through separately reviewed S6 publication. PR #465 therefore reported non-mergeable at review claim while the exact judged head remained immutable. That stale-base condition is a convergence/publication issue, not a defect in the security judgment.

Do not mutate `planning/issue-463` to cure it. Any publication must use a separately authorized current-main-compatible squash/recovery route that preserves the exact reviewed validator semantics and provenance.

## Required next route

1. Open an exact-head draft PR for this review branch and terminalize #466.
2. Publish the review provenance only under separate convergence authority if current-main compatible.
3. Recover/publish the exact reviewed #463 remediation onto then-current `main` without semantic drift if PR #465 remains stale/non-mergeable.
4. Only after the reviewed remediation is on trusted `main`, obtain one fresh credentialed provider run.
5. Route the exact fresh Unreal outcome. Do not infer provider PASS or empirical eligibility from this review.

## Authority boundary

`NOT_CANONICAL`. Required security/authority review only. No provider credential/PASS, Unreal unlock, engine selection, implementation/readiness, commercial/production/legal/release, verification-PASS, decision, integration-by-review, or canonical authority.
