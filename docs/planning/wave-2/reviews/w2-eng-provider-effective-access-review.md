# W2-ENG-PROVIDER-EFFECTIVE-REV-01 — required security/authority review

## Review identity

- Review issue: #398 / `W2-ENG-PROVIDER-EFFECTIVE-REV-01`
- Winning claim: `5306201352`
- Review mode: `DEGRADED_SINGLE_AGENT`
- Review base: `main@56f8ac296d1eb779a9e684edda0e8a822691a8bf`
- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical binding comment: `5245368879`
- Canonical activation SHA: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Owner convergence directive: `5277825639`
- Owner parallel-frontier directive: `5305563203`
- Judged producer: Issue #373 / `W2-ENG-PROVIDER-EFFECTIVE-01`
- Producer terminal status: `5306084733`
- Immutable producer head/work: `75728cade4c1646f9a1006e89ccc026234958a2b`
- Producer draft PR: #397, exact head `75728cade4c1646f9a1006e89ccc026234958a2b`
- Judged changed-file set: nine files exactly as reported by PR #397.

The producer branch is an immutable judged input. This review does not edit `planning/issue-373`.

## Disposition

`CHANGES_NEEDED`

Finding count: **0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR**.

The packet's scoped provider model and credential boundary are useful, but the exact publication/provenance machinery is not safe for integration yet. Exactly one bounded remediation successor is required, followed by a fresh required review.

## Required attacks and results

### Frozen identity and ownership — PASS

Current `main`, the active canonical binding, Issue #373 terminal identity, PR #397 exact head, the open frontier, and ownership were re-derived before claim. Higher-priority world remediation #389 was validly owned; narrative remediation #396 remained blocked on in-progress required review #394. Issue #398 was unowned and the post-claim contention re-check contained only claim `5306201352`.

### Independent provider state and authority separation — PASS

The contract and machine packet keep Unity and Unreal independently unlockable, preserve `combined_predicate_used_for_individual_unlock=false`, keep commercial/production/legal/release/engine-selection authority false, and preserve Issue #82's historical 50 `NOT_RUN` cells without mutation. Unreal entitlement is represented as a provider-specific external condition and does not globally block Unity or unrelated public-toolchain work.

### Trusted credential boundary / fork-PR exposure — PASS within reviewed scope

`.github/workflows/engine-eval-credentialed.yml` triggers only on `push` to `main` or manual dispatch constrained to `refs/heads/main`, uses `environment: engine-eval`, and has only `contents: read`. Provider secrets are injected only into the validation step. No `pull_request` or `pull_request_target` secret-bearing path exists in the judged workflow. The pinned third-party actions are commit-pinned.

The weekly/dispatch health workflow is likewise `contents: read`, uses `engine-eval`, and has no PR trigger. This pass does not grant commercial/provider/release authority.

### Sanitized projection — PASS with retained remediation requirements below

`record_provider_effective_access.py` projects fixed provider/frontier fields and rejects authority promotion, baseline drift, unexpected native S3/process shapes, combined-provider unlock, and mutation of the historical 50-cell provenance. The local Unity packet explicitly distinguishes local native execution from GitHub-hosted CI and keeps Unreal `NOT_CONFIGURED`.

This pass does not cure the publication and exact-execution identity defects below.

## Material findings

### W2-ENG-PROVIDER-EFFECTIVE-REV-M01 — MAJOR — recorder self-publishes directly to `main`

The exact recorder workflow declares `contents: write`, checks out `main`, commits the projected evidence, and executes:

`git push origin HEAD:main`

That is incompatible with the repository's active integration model. Owner convergence directive `5277825639` requires every integration into `main` to remain squash-only with an exact expected-head check and explicitly separates integration authority from review/readiness state. The recorder has no task ownership claim, no review episode for the generated durable payload, no PR exact-head gate, and no squash merge. Calling the update "data-only" does not remove those authority requirements.

**Required correction:** remove direct self-publication to `main`. The credentialed stage may emit sanitized data, but durable repository publication must use a reviewed, ownership-aware route that creates a bounded branch/PR or otherwise hands the immutable artifact to an authorized squash-only integration episode with exact expected-head checking. The recorder itself must not gain general main-write authority merely because a trusted workflow completed.

### W2-ENG-PROVIDER-EFFECTIVE-REV-M02 — MAJOR — recorded head/workflow identity is not the code identity actually executed

The credentialed evaluator is triggered by a specific trusted-main event but `actions/checkout` explicitly uses `ref: main` rather than the triggering commit. If `main` advances after the event is queued and before checkout, the validator executed can come from a later commit while the downstream recorder labels the evidence with `github.event.workflow_run.head_sha` from the earlier triggering event.

The recorder repeats the same moving-ref pattern: it checks out current `main` and runs the current `record_provider_effective_access.py`, while recording the producer workflow's earlier `head_sha`. It filters the upstream workflow by display name and successful trusted-main metadata, but does not prove that the exact workflow/code identity that produced and projected the artifact equals the recorded source identity. This violates the required fail-closed binding between trusted workflow identity, successful run, head SHA, and the code used to interpret the artifact.

**Required correction:** pin evaluator execution to the triggering SHA and mechanically assert the checkout identity before credentials are used. Bind the consumer to the exact trusted workflow identity/path and exact upstream head. Run projection logic from an explicitly bound reviewed identity, and fail closed on any mismatch. The eventual publication route must preserve those source identities without executing artifact-controlled code.

## Regression/pass boundaries that must be preserved by remediation

The remediation must preserve all reviewed-clean properties:

- per-provider independent readiness; no combined Unity+Unreal predicate;
- Unity local S3 remains local development evidence only, not hosted-CI validation;
- Unreal Epic/GitHub entitlement and package credential remain scoped external prerequisites only for actual credentialed Unreal execution;
- non-secret Unreal CI/container/native-S3 preparation remains eligible;
- credentialed evaluator remains trusted-main-only, `engine-eval`, minimal read permission, and no fork/PR secret path;
- artifact input remains data-only and schema-validated; artifact content is never executed;
- Issue #82's 50 historical `NOT_RUN` cells remain immutable provenance;
- no engine selection, commercial licensing, production readiness, legal/release authority, verification-PASS, decision authority, canonicality, or integration authority is inferred.

## Required successor

Route exactly one bounded blocking remediation successor, `W2-ENG-PROVIDER-EFFECTIVE-REM-01`, limited to M01 and M02 and the minimum consistency updates required by those fixes. The exact producer #373/#397 packet remains immutable. A fresh independent/degraded-independent required review of the exact remediation packet is mandatory before `PASS_BOUNDED_PROVIDER_EFFECTIVE_ACCESS` or any publication/integration of this machinery.

No Epic credential or Unity CI entitlement is a prerequisite to perform that remediation.

## Authority boundary

This review is noncanonical required-review provenance only. It grants no integration, provider credential, engine selection, commercial/production/legal/release authority, implementation readiness, verification-PASS, decision, or canonical authority.