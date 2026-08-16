# W2-ENG-PROVIDER-EFFECTIVE-REM-REV-01 — required remediation review

## Review identity

- Review issue: #402 / `W2-ENG-PROVIDER-EFFECTIVE-REM-REV-01`
- Winning claim: `5306312793`
- Reviewer actor/session: `w2-eng-provider-effective-rem-rev-01-gpt56sol-20260816-02`
- Trust mode: `DEGRADED_SINGLE_AGENT`
- Review base: `main@08a89092a9e9b2bae6f8bd34dd29dd85a8d97bcf`
- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical binding comment: Issue #6 comment `5245368879`
- Canonical activation SHA: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Owner convergence directive: Issue #84 comment `5277825639`
- Owner parallel-frontier directive: Issue #84 comment `5305563203`
- Frozen producer: Issue #373 / PR #397 / head `75728cade4c1646f9a1006e89ccc026234958a2b`
- First required review: Issue #398 / terminal `5306215159` / `CHANGES_NEEDED`
- First-review findings: `W2-ENG-PROVIDER-EFFECTIVE-REV-M01`, `W2-ENG-PROVIDER-EFFECTIVE-REV-M02`
- Judged remediation: Issue #400 / claim `5306254156` / terminal `5306282246`
- Judged remediation implementation work: `d504aa4aa86a27e56329865b7e9af74b87dd0919`
- Judged remediation terminal head: `2f6202747bc517202b406dc2f97e138d21294780`
- Judged remediation PR: #401, draft, base `main@08a89092a9e9b2bae6f8bd34dd29dd85a8d97bcf`, exact head `2f6202747bc517202b406dc2f97e138d21294780`
- Judged remediation changed-file set: exactly six files.

This is a distinct ownership/review episode from remediation #400, but stronger reviewer isolation is unavailable. The review therefore makes no claim of full independence. The #373, #398, and #400 branches are immutable judged inputs and were not edited.

## Disposition

`CHANGES_NEEDED`

Finding count: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

The two original security/authority findings are closed by the exact modified code, but the exact successor PR is not a complete functional replacement for the rejected producer packet. It cannot be integrated as the bounded provider-access machinery in its current form.

## Original finding closure

### `W2-ENG-PROVIDER-EFFECTIVE-REV-M01` — CLOSED

The exact recorder no longer commits or pushes generated evidence directly to `main`. It stages exactly one run-scoped evidence path on `evidence/provider-effective-access/run-<run_id>-attempt-<run_attempt>` and opens a draft PR. The staged path is checked exactly before commit. Re-delivery/branch collision cannot silently overwrite `main`; a non-fast-forward remote branch causes the push to fail closed. The generated PR text explicitly withholds integration authority and requires a separately authorized, fresh expected-head checked, squash-only integration episode.

Workflow success therefore does not itself grant repository integration authority.

### `W2-ENG-PROVIDER-EFFECTIVE-REV-M02` — CLOSED

The credential-bearing evaluator checks out exact trusted-event `github.sha` and asserts repository, `refs/heads/main`, and `git rev-parse HEAD == github.sha` before the secret-bearing validation step. It has only `contents: read`, uses `environment: engine-eval`, and has no PR or fork secret trigger.

The recorder binds the exact successful upstream run id, attempt, event, conclusion, head branch, head SHA, repository, and workflow id through the Actions API. It resolves that workflow id back to the exact `.github/workflows/engine-eval-credentialed.yml` path, requires the source head to remain an ancestor of current `main`, checks out that exact source head, and executes `record_provider_effective_access.py` from the same identity. The projected evidence records workflow id/name/path, source head, projection-code SHA, and observed publication-base main SHA, and rejects a projection-code SHA unequal to the source head.

Artifact content remains data-only. The recorder downloads only the exact run/attempt artifact, parses JSON, and never sources or executes artifact-controlled code.

## Required attacks and results

### 1. Frozen identity/provenance — PASS

The #400 claim, terminal, implementation work SHA, terminal head, PR #401 base/head/draft state, six-path diff, #373 producer identity, and #398 first-review identity were re-derived before review. #402 was unowned before claim and the immediate contention re-check contained only claim `5306312793`.

### 2. Direct-main publication and authority — PASS

No `HEAD:main` or equivalent generated-evidence push remains. The branch/draft-PR route does not promote workflow success into integration authority.

### 3. Publication branch/PR bypasses — PASS within exact code

The evidence branch is derived only from GitHub run id/attempt, the generated path is run-id scoped, only that path is staged, and a conflicting existing remote branch fails the normal non-force push rather than overwriting another lineage. The workflow creates only a draft PR and does not merge it.

### 4. Evaluator trusted-head binding — PASS for the identity correction

Checkout and pre-secret identity assertions bind execution to the exact trusted event SHA. The separate missing-runtime-dependency finding below prevents successful execution, but does not reopen the moving-ref identity defect.

### 5. Consumer workflow/run identity — PASS

The recorder verifies the exact Actions run plus exact workflow id/path through the API rather than relying on display name alone.

### 6. Projection code identity — PASS

Projection executes from exact upstream `head_sha`; `projection_code_sha` must be a 40-hex SHA equal to that head and is persisted in evidence.

### 7. Artifact boundary — PASS

The exact run/attempt artifact is downloaded by pinned `actions/download-artifact`; it is JSON data only. The fixed projection rejects authority promotion, provider/baseline drift, malformed native/process shapes, combined-provider unlock, and historical-cell mutation.

### 8. Credential boundary regression — PASS within reviewed scope

The evaluator remains trusted-repository/main-only with `engine-eval` and `contents: read`; provider secrets are injected only into the validation step. The recorder has repository-write permissions needed for the bounded evidence branch/PR but does not receive the provider secrets or the `engine-eval` environment.

### 9. Provider independence — PASS

Unity and Unreal remain independently unlockable. `combined_predicate_used_for_individual_unlock` is required to remain false.

### 10. Local-vs-hosted and Unreal entitlement semantics — FAIL as packet preservation, not predicate logic

The text still states that durable local Unity S3 evidence remains local-only and that Unreal entitlement is scoped to actual credentialed execution. Those semantics are correct. However, the exact successor omits the frozen local Unity evidence file that supplied the durable local result. This is part of the reconstruction finding below.

### 11. Historical Issue #82 provenance — PASS

The contract and recorder preserve exactly 50 historical `NOT_RUN` cells and reject mutation.

### 12. Authority inflation — PASS

Commercial, production, legal, release, engine-selection, integration, readiness, verification-PASS, decision, and canonical authority remain false or explicitly withheld.

### 13. Exact successor scope/completeness — FAIL

The six-file remediation diff is bounded, but it is too narrow to form a functional successor from current `main`. The rejected producer's unchanged runtime/support/provenance surfaces were not carried forward.

## Material finding

### `W2-ENG-PROVIDER-EFFECTIVE-REM-REV-M01` — MAJOR — successor reconstruction drops required frozen producer surfaces

PR #401 is based directly on `main@08a89092a9e9b2bae6f8bd34dd29dd85a8d97bcf` and adds exactly six remediation files. Frozen producer #373/#397, however, supplied nine files. Three producer surfaces that the remediation did not modify were omitted from the exact successor:

- `tools/planning/engine_provider_effective_validator.py`
- `.github/workflows/engine-eval-health.yml`
- `docs/planning/wave-2/evidence/provider-effective-access-local-unity.json`

All three paths are absent at exact judged remediation head `2f6202747bc517202b406dc2f97e138d21294780`.

This is not merely documentary drift:

1. `.github/workflows/engine-eval-credentialed.yml` explicitly compiles, self-tests, and executes `tools/planning/engine_provider_effective_validator.py`. At the exact #400 head that file does not exist, so the evaluator deterministically fails before it can perform provider validation.
2. `provider-effective-access-contract.json` declares `.github/workflows/engine-eval-health.yml` as the health workflow, but that file is absent from the exact successor.
3. `provider-effective-access.md` says the durable local Unity `6000.5.6f1` S3 N1/N2/FI1 result remains local development evidence, while the frozen evidence file carrying that result is absent from the successor.

The old producer PR #397 cannot be used as an implicit dependency to cure this: it remains the exact packet rejected by required review #398, and its old evaluator/recorder contain the two MAJOR defects that #400 was created to replace. Integrating #401 alone would therefore publish a broken/internally inconsistent provider-access packet; integrating #397 first would reintroduce explicitly rejected code and bypass the required remediation result.

**Required correction:** route exactly one bounded blocking-remediation successor that reconstructs a complete provider-access successor from current `main`. Carry forward the unchanged, review-clean producer runtime/support/provenance surfaces needed by the retained contract and prose—at minimum the validator required by the evaluator, plus the declared health workflow and durable local Unity evidence unless the successor deliberately removes those contract/prose claims. Apply the already-reviewed M01/M02 corrections without restoring direct-main publication or moving-main execution. Do not integrate rejected PR #397 as a prerequisite or shortcut. Freeze the new complete exact head/PR and require one fresh review before any provider-access integration.

## Required next route

Exactly one blocking remediation successor is required for `W2-ENG-PROVIDER-EFFECTIVE-REM-REV-M01`. No additional optional review or producer expansion should be created while that correction is eligible.

The successor must preserve the clean closure of the original M01/M02 findings and all clean provider, credential, artifact, Issue #82, and authority boundaries recorded above.

## Authority boundary

This review is noncanonical required-review provenance only. `CHANGES_NEEDED` grants no integration, provider credential, engine selection, commercial/production/legal/release authority, implementation readiness, verification-PASS, decision, or canonical authority. PR #401 must not be integrated on the basis of this review.