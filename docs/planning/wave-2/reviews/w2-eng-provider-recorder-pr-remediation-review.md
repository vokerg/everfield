# W2-ENG-PROVIDER-RECORDER-PR-REM-REV-01 — security/authority review

**Issue:** #445  
**Judged remediation:** Issue #440 / `W2-ENG-PROVIDER-RECORDER-PR-REM-01`  
**Task class:** `REQUIRED_REVIEW`  
**Trust:** `DEGRADED_SINGLE_AGENT`  
**Disposition:** `PASS_BOUNDED_PROVIDER_RECORDER_PR_REMEDIATION`  
**Canonicality:** `NOT_CANONICAL`

## 1. Frozen judged packet

This review judges only immutable Issue #440 / draft PR #443 at exact head `6744b13a410af8caebc1fd40f62459e4e070f5d9`.

- producer claim: Issue #440 comment `5308498265`;
- producer terminal: `5308528422`;
- producer actor: `frontier-drain-provider-recorder-pr-rem-01-gpt56sol-20260816-01`;
- producer claim base: `437b9fc60d1db8cdc2c2006096707bdb9ee8276f`;
- substantive work: `2922affa77feb59c21530dbb35fc9b022a1ef650`;
- exact terminal head / PR #443 head: `6744b13a410af8caebc1fd40f62459e4e070f5d9`;
- PR #443 state at final review fence: open, draft, mergeable, base branch `main`, observed base SHA `1c4401f124ae455590e5d5fa3285cf38c3cba26e`;
- workflow blob: `8262841a9f944b8695f77a54a003d4f8905fd884`;
- provider contract blob: `07675bcebecf99266c6a2ba5e15cca3e04ef7e44`;
- provider prose blob: `aa24aaea22cf6cf3fec989abf58bb199f2ca0ec7`;
- producer handoff blob: `fa682a16b6cee6d3b6f9269a4fcb84440b96e681`.

Changed paths are exactly:

1. `.github/workflows/engine-eval-evidence-recorder.yml`;
2. `docs/planning/wave-2/evidence/provider-effective-access-contract.json`;
3. `docs/planning/wave-2/evidence/provider-effective-access.md`;
4. `docs/planning/handoffs/issue-440.md`.

The judged producer branch was not edited by this review.

## 2. Canonical and predecessor authority

Current `main` at the final pre-write review fence is `1c4401f124ae455590e5d5fa3285cf38c3cba26e`.

Canonical authority remains:

- Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`;
- binding comment `5245368879`;
- activation SHA `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner convergence directive `5277825639`;
- owner parallel-frontier directive `5305563203`.

Frozen predecessor chain:

- recorder worktree remediation Issue #421 terminal `5307463195`, exact head `3878500aecb740bdb4169357a3ab3775eb298237`;
- required review Issue #425 terminal `5308459743`, disposition `PASS_BOUNDED_PROVIDER_RECORDER_REMEDIATION`, findings `0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR`;
- #421 squash publication `b03193c230e00dde6ad9340d69308c2a8de1ae56`, integration-status comment `5308474314`;
- #425 review-provenance publication `437b9fc60d1db8cdc2c2006096707bdb9ee8276f`.

These predecessor identities are treated as immutable provenance.

## 3. Frozen recovery evidence

The bounded recovery reason is reconstructable from exact retained evidence:

- credentialed evaluator run `31959049126`, attempt `1`, source head `437b9fc60d1db8cdc2c2006096707bdb9ee8276f`, conclusion `success`;
- artifact `9266735823`, digest `sha256:545adb1ebeac3204fd9c0c92f8a3bfd3ca71387284097307c9d89d187f831f71`;
- recorder run `31959057717`, job `95194131380`;
- exact source/run/workflow binding, exact checkout, side-effect-free source syntax check, pre-projection clean-worktree check, artifact download, projection, exact post-projection single-path guard, evidence commit, and evidence-branch push all completed before the recorder failed at Actions-token REST pull-request creation with HTTP 403.

Immutable generated-evidence handoff:

- branch `evidence/provider-effective-access/run-31959049126-attempt-1`;
- head `ad34a0039d99efd04869ae8aeceaed2097d30924`;
- evidence path `docs/planning/wave-2/evidence/ci/provider-effective-access/31959049126/effective.json`;
- evidence blob `eb35148dbbdb7f7ff459390cffb30a9ff7e2ed15`.

Recovered evidence PR #438 was re-fenced during review and remains open, draft, mergeable, head `ad34a0039d99efd04869ae8aeceaed2097d30924`, base branch `main`, with exactly one changed path: the evidence JSON above. Its body retains recorder run `31959057717` as a failed run whose already-pushed branch was recovered; it does not relabel the workflow as successful.

The evidence itself remains fail-closed:

- Unity: `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION`, blocker `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED`;
- Unreal Engine: `NOT_CONFIGURED`, blocker `UNREAL_GITHUB_USERNAME_AND_TOKEN_NOT_CONFIGURED`;
- neither provider is unlocked;
- historical Issue #82 `50 NOT_RUN` cells remain preserved;
- evidence states `direct_main_push=false`, `integration_authority=false`, `fresh_expected_head_check_required=true`, `squash_only_required=true`, and contains no secret values or secret hashes.

## 4. Review method

No provider credential or secret-bearing execution was needed or performed for this review. The review inspected exact GitHub objects and immutable bytes:

- PR #443 exact head/base/draft/mergeability and exact four-file diff;
- candidate recorder workflow bytes at blob `8262841a9f944b8695f77a54a003d4f8905fd884`;
- candidate provider contract bytes at blob `07675bcebecf99266c6a2ba5e15cca3e04ef7e44`;
- candidate provider prose bytes at blob `aa24aaea22cf6cf3fec989abf58bb199f2ca0ec7`;
- producer handoff diff and frozen recovery provenance;
- pre-remediation contract on `main@437b9fc60d1db8cdc2c2006096707bdb9ee8276f` to identify the exact permission/publication responsibility change;
- PR #438 exact state, head, scope, and evidence bytes.

The workflow correction is materially subtractive at the PR-creation boundary: it removes `pull-requests: write`, removes the Actions-token REST `POST /pulls` implementation, and preserves the already-reviewed identity, projection, worktree, branch, and staged-path guards.

## 5. Mandatory attacks and results

### A1 — frozen identity and scope

**PASS.** #440 claim/terminal/work/head, #443 state, all four exact blobs, and the four-path diff are frozen and mutually consistent. No unrelated provider or engine surface appears in the judged diff.

### A2 — recorder permissions and secret boundary

**PASS.** Candidate recorder permissions are exactly:

- `actions: read`;
- `contents: write`.

`pull-requests: write` is removed. The recorder has no provider-secret environment and no new credential boundary. Contract `secret_boundary.recorder_stage_permissions` and implementation permissions match the workflow.

### A3 — automatic PR creation removed without bypass

**PASS.** The exact diff removes the urllib/REST PR-creation block and the final workflow step contains no alternate Actions-token draft-PR creator. The step publishes the evidence branch and emits bounded handoff metadata only.

### A4 — upstream workflow/run/source identity remains fail-closed

**PASS.** The workflow still verifies exact run id, run attempt, workflow name, event, completed/success state, `main` branch, source SHA, repository, workflow id, and exact workflow path through the Actions API. It also verifies the source head remains an ancestor of the observed publication-base `main`.

### A5 — exact checkout, projection-code identity, artifact boundary, and pre-projection clean state

**PASS.** The workflow still checks out the exact upstream `head_sha`, asserts `git rev-parse HEAD` equality, verifies expected files, compiles trusted projection source in memory without checkout bytecode, and requires a clean worktree before projection. The exact run artifact is downloaded and treated as data; projection executes the recorder code from the exact trusted source head.

### A6 — post-projection single-path, deterministic branch, staged-path, and no-direct-main guards

**PASS.** The exact post-projection assertion remains `?? $EVIDENCE_PATH`; deterministic branch naming remains `evidence/provider-effective-access/run-${RUN_ID}-attempt-${RUN_ATTEMPT}`; the staged-path assertion still requires exactly `$EVIDENCE_PATH`; publication pushes only `HEAD:refs/heads/$EVIDENCE_BRANCH`. No generated-evidence `main` push is introduced.

### A7 — workflow success remains bounded handoff only

**PASS.** After branch publication the workflow emits:

- `draft_pr_created_by_workflow=false`;
- `draft_pr_required=true`;
- exact evidence branch/path and run/source identities;
- `integration_authority=false`;
- `next_step=SEPARATE_NORMAL_OWNERSHIP_EPISODE_OPENS_DRAFT_PR`.

Thus success after this remediation means the bounded evidence branch exists and awaits the mandatory draft-PR handoff; it does not imply provider or integration authority.

### A8 — contract/prose preserve branch + draft-PR boundary

**PASS.** Contract publication mode remains `BOUNDED_EVIDENCE_BRANCH_DRAFT_PR`, with `recorder_publishes_branch_only=true`, `draft_pr_required=true`, and `draft_pr_creator=SEPARATE_NORMAL_OWNERSHIP_EPISODE`. It retains separate integration authority, fresh expected-head, and squash-only requirements. The prose explicitly states a bare evidence branch is not integrable and that a separate normal ownership/recovery episode must open the draft PR from the immutable evidence branch.

### A9 — recovered evidence PR exactness

**PASS.** PR #438 remains draft and exact-head at `ad34a0039d99efd04869ae8aeceaed2097d30924`; it changes exactly one generated evidence path whose blob is `eb35148dbbdb7f7ff459390cffb30a9ff7e2ed15`. Its body retains all authority boundaries and identifies the recorder failure accurately.

### A10 — failed recorder provenance is not laundered

**PASS.** Contract recovery provenance records `fresh_recorder_failure=ACTIONS_GITHUB_TOKEN_PR_CREATE_HTTP_403_AFTER_EVIDENCE_BRANCH_PUSH` and `failed_recorder_run_relabelled_as_success=false`. Prose and PR #438 also explicitly retain recorder `31959057717` as failed provenance.

### A11 — no PAT, long-lived credential, or repository-setting assumption

**PASS.** The correction removes token scope instead of adding credentials. No PAT, new secret, provider environment, or repository-setting mutation is introduced for PR creation. Draft-PR creation is moved to the ordinary ownership-aware repository control plane.

### A12 — provider independence and evidence semantics

**PASS.** Unity and Unreal remain independently evaluated. Current retained evidence unlocks neither. No combined-provider predicate is introduced, and the correction changes publication responsibility rather than provider validation semantics.

### A13 — authority inflation

**PASS.** Workflow, contract, prose, handoff, and recovered evidence PR all deny provider PASS, evidence integration, engine selection, commercial/production/legal/release authority, implementation readiness, verification-PASS, content fan-in, decision, and canonical authority.

### A14 — exact remediation surface

**PASS.** PR #443 changes exactly the recorder workflow, provider contract, provider prose, and Issue #440 handoff. PR #438 is a separate immutable evidence handoff containing exactly one generated evidence file. No unrelated provider/engine/content surface is changed.

## 6. Finding ledger

- BLOCKER: `0`
- MAJOR: `0`
- correction-requiring MINOR: `0`

No material defect was found in the exact judged remediation.

## 7. Disposition

**`PASS_BOUNDED_PROVIDER_RECORDER_PR_REMEDIATION`**

Exact Issue #440 / PR #443 is clean for **separately authorized squash publication of the remediation packet only** under then-current repository authority.

This disposition means:

- it is acceptable for the recorder to publish the exact bounded evidence branch using only `actions: read` + `contents: write`;
- the workflow must not create the draft PR;
- a separate ownership-aware repository episode must create the mandatory draft PR from the exact immutable evidence branch;
- a bare evidence branch is not integrable;
- workflow success grants no provider or integration authority;
- recovered evidence PR #438 remains a separate noncanonical evidence handoff requiring its own fresh integration-authority derivation.

The clean review does **not** itself integrate #440 or #438.

## 8. Authority boundary

This review is noncanonical security/authority provenance only. It grants no provider credential or provider PASS, no generated-evidence integration, no engine selection, no gameplay/high-throughput or production implementation authority, no commercial/legal/release authority, no implementation readiness or verification-PASS, no content-fan-in authority, no decision authority, and no canonical authority.

Any publication of exact #440 must be separately derived against current `main`, exact PR head, current ownership, and contract-specific gates, and must be squash-only. Any later handling of evidence PR #438 is a distinct authority episode.
