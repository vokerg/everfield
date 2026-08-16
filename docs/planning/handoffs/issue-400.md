# Issue #400 handoff — provider publication and identity remediation

## State

`REMEDIATION IMPLEMENTED / DRAFT PR AND FRESH REQUIRED REVIEW PENDING`

This handoff records the bounded correction of the two MAJOR findings from
required review Issue #398. It grants no integration, provider, commercial,
production, legal, release, engine-selection, readiness, verification-PASS,
decision, or canonical authority.

## Ownership and base

- issue: #400
- mission: `W2-ENG-PROVIDER-EFFECTIVE-REM-01`
- branch: `planning/issue-400`
- winning claim: Issue #400 comment `5306254156`
- actor session: `w2-eng-provider-effective-rem-01-gpt56sol-20260816-01`
- task class: `BLOCKING_REMEDIATION`
- exact remediation base main: `08a89092a9e9b2bae6f8bd34dd29dd85a8d97bcf`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`

## Frozen predecessor provenance

Producer:
- Issue #373 / `W2-ENG-PROVIDER-EFFECTIVE-01`
- claim `5305595166`
- terminal `5306084733`
- exact work/head `75728cade4c1646f9a1006e89ccc026234958a2b`
- draft PR #397

Required review:
- Issue #398 / `W2-ENG-PROVIDER-EFFECTIVE-REV-01`
- claim `5306201352`
- terminal `5306215159`
- review work `dd50c223aa641f8e994752ac9c2a1f82c5de9f8a`
- review head `8e001aa76d68e0bf04ac44e04d694e27215d8b58`
- draft PR #399, squash-published as noncanonical review provenance at
  `08a89092a9e9b2bae6f8bd34dd29dd85a8d97bcf`
- disposition `CHANGES_NEEDED`
- findings: 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR

The predecessor producer and review branches remain immutable.

## Changed successor surfaces

- `.github/workflows/engine-eval-credentialed.yml`
- `.github/workflows/engine-eval-evidence-recorder.yml`
- `tools/planning/record_provider_effective_access.py`
- `docs/planning/wave-2/evidence/provider-effective-access-contract.json`
- `docs/planning/wave-2/evidence/provider-effective-access.md`
- `docs/planning/handoffs/issue-400.md`

No provider credentials, historical Issue #82 result cells, local Unity evidence,
engine selection, or unrelated engine evidence are changed by this remediation.

## Finding closure candidate

### W2-ENG-PROVIDER-EFFECTIVE-REV-M01

Status: `CLOSED_IN_REMEDIATION_CANDIDATE_PENDING_FRESH_REVIEW`.

The recorder has no direct `HEAD:main` push. Sanitized projected evidence is
committed only to a deterministic run/attempt evidence branch and exposed as a
draft PR. The PR is a handoff that requires repository ownership/review plus a
separately authorized squash-only integration with a fresh exact expected-head
check. Workflow success grants no integration authority.

### W2-ENG-PROVIDER-EFFECTIVE-REV-M02

Status: `CLOSED_IN_REMEDIATION_CANDIDATE_PENDING_FRESH_REVIEW`.

The evaluator checks out exact trusted-main event `github.sha` and verifies
that identity before provider secrets are consumed. The recorder validates the
successful upstream run through the Actions API, binds exact workflow id/path,
run attempt, repository, branch, and head SHA, checks out the exact upstream
head, and runs projection code from that same identity. Those source identities
are preserved in the projected evidence.

## Preserved review-clean boundaries

- Unity and Unreal remain independent provider predicates.
- Unity local S3 evidence remains local development evidence only.
- Unreal entitlement and package-read credential remain scoped only to actual
  credentialed Unreal execution; non-secret preparation stays eligible.
- Provider secrets remain trusted-main-only in `engine-eval`, with
  `contents: read` in the credential-bearing evaluator.
- Sanitized artifacts remain data-only and are never executed.
- Issue #82's 50 historical `NOT_RUN` cells remain immutable provenance.
- No engine selection, commercial/production/legal/release authority,
  readiness, verification-PASS, decision, integration, or canonical authority
  is inferred.

## Verification performed before publication

- Python syntax compilation for the remediated recorder.
- Deterministic recorder fixture exercised successful identity projection and
  fail-closed rejection of a mismatched projection-code SHA.
- Both changed workflow YAML documents parse.
- Static checks confirm the credentialed workflow uses exact `github.sha`, the
  recorder binds the exact workflow path and upstream head, and no recorder
  command pushes `HEAD:main`.
- Contract JSON parses and explicitly records the draft-PR/squash-only
  publication boundary.

## Required next route

Open and verify an exact-head draft PR for this branch, then publish terminal
schema-3 `STATUS(REVIEW_READY)`. Route exactly one fresh independent or
degraded-independent required review of this exact remediation packet. Only
that review may determine whether both findings are actually closed and whether
`PASS_BOUNDED_PROVIDER_EFFECTIVE_ACCESS` is warranted.

## Authority boundary

`NOT_CANONICAL`. No integration authority. No provider credential or engine
choice. No commercial, production, legal, or release authority. No
implementation readiness or verification-PASS. Any eventual publication to
`main` remains separately authorized, requires a fresh exact expected-head
check, and is squash-only.
