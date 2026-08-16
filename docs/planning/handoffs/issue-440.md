# Issue #440 handoff — provider evidence publication recovery

## Identity

- Mission: `W2-ENG-PROVIDER-RECORDER-PR-REM-01`
- Task class: recovery-oriented blocking remediation
- Claim: Issue #440 comment `5308498265`
- Base main: `437b9fc60d1db8cdc2c2006096707bdb9ee8276f`
- Branch: `planning/issue-440`
- Workflow correction commit: `33ef6b02730c3660c500dcb3cb1ee75c25c846ce`
- Contract correction commit: `4f01cfdb479b960fd81a93d66ca1656fb6efcf0a`
- Prose correction commit: `2922affa77feb59c21530dbb35fc9b022a1ef650`
- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical binding: Issue #6 comment `5245368879`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Owner convergence directive: Issue #84 comment `5277825639`
- Owner parallel-frontier directive: Issue #84 comment `5305563203`

This packet is noncanonical recovery/remediation provenance only. It does not validate a provider, integrate generated evidence, select an engine, establish readiness/verification PASS, authorize release or content fan-in, make a decision, or create canonical authority.

## Frozen predecessor and integration provenance

- Issue #421 / `W2-ENG-PROVIDER-RECORDER-REM-01` terminal `5307463195`, exact head `3878500aecb740bdb4169357a3ab3775eb298237`, PR #423.
- Issue #425 / `W2-ENG-PROVIDER-RECORDER-REM-REV-01` terminal `5308459743`, disposition `PASS_BOUNDED_PROVIDER_RECORDER_REMEDIATION`, 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.
- Exact #421 squash publication: `b03193c230e00dde6ad9340d69308c2a8de1ae56`; durable integration status: #421 comment `5308474314`.
- Exact #425 review-provenance squash publication: `437b9fc60d1db8cdc2c2006096707bdb9ee8276f`.

The predecessor branches/reviews remain immutable.

## Fresh post-integration recovery evidence

The prior worktree defect is closed in fresh trusted-main execution.

Latest exact evaluator:

- run `31959049126`, attempt 1;
- source/head `437b9fc60d1db8cdc2c2006096707bdb9ee8276f`;
- conclusion `success`;
- artifact `9266735823`, `w2-engine-effective-access-31959049126-1`;
- artifact digest `sha256:545adb1ebeac3204fd9c0c92f8a3bfd3ca71387284097307c9d89d187f831f71`.

Latest exact recorder:

- run `31959057717`;
- job `95194131380`;
- exact upstream workflow/run/attempt/head/repository/path binding: PASS;
- exact source checkout and side-effect-free projection-code identity check: PASS;
- artifact download: PASS;
- validation/projection: PASS;
- exact post-projection single-evidence-path worktree guard: PASS;
- evidence commit and branch push: PASS;
- automated REST draft-PR creation: FAIL with HTTP 403.

The same post-integration pattern occurred for evaluator `31958951650` / recorder `31958963402`: the recorder reached the final publication step and failed there rather than at the repaired worktree guard.

## Immutable recovered evidence handoff

The latest recorder successfully published:

- branch `evidence/provider-effective-access/run-31959049126-attempt-1`;
- exact head `ad34a0039d99efd04869ae8aeceaed2097d30924`;
- exact evidence path `docs/planning/wave-2/evidence/ci/provider-effective-access/31959049126/effective.json`;
- evidence blob `eb35148dbbdb7f7ff459390cffb30a9ff7e2ed15`.

A concurrent normal repository recovery episode opened draft PR #438 from that exact immutable branch/head to `main`. The PR body correctly retains recorder run `31959057717` as a **failed** run whose branch publication was recovered; it does not relabel the workflow as successful and grants no integration authority.

The projected evidence remains fail-closed:

- Unity: `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION`, blocker `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED`;
- Unreal Engine: `NOT_CONFIGURED`, blocker `UNREAL_GITHUB_USERNAME_AND_TOKEN_NOT_CONFIGURED`;
- neither provider unlocked;
- no commercial, production, legal, release, engine-selection, integration, readiness, verification, decision, or canonical authority.

## Root cause

The recorder combined two publication operations under the Actions token:

1. exact bounded evidence-branch publication, which succeeds with `contents: write`;
2. REST draft-PR creation, which is denied by repository Actions policy with HTTP 403 even though the workflow declared `pull-requests: write`.

The normal repository integration used for planning can create PRs, but its GitHub App cannot read the repository Actions workflow-permission setting (`403 Resource not accessible by integration`). This remediation therefore does not assume or alter a global repository setting and does not introduce a PAT or another long-lived credential solely to create PRs.

## Exact remediation

### Recorder workflow

`.github/workflows/engine-eval-evidence-recorder.yml` now:

- retains the exact trusted-main upstream run/workflow/source/ancestry binding;
- retains exact source-head checkout and projection-code identity;
- retains side-effect-free in-memory syntax validation and pre-projection clean-worktree assertion;
- retains exact run artifact download and data-only projection;
- retains the exact post-projection `?? $EVIDENCE_PATH` guard;
- retains deterministic evidence branch naming and exact staged-path check;
- retains branch-only `git push origin "HEAD:refs/heads/$EVIDENCE_BRANCH"`;
- removes `pull-requests: write` permission;
- removes REST `POST /pulls` and all PR-creation code from the Actions job;
- emits exact handoff metadata after branch push, including `draft_pr_required=true`, `draft_pr_created_by_workflow=false`, and `next_step=SEPARATE_NORMAL_OWNERSHIP_EPISODE_OPENS_DRAFT_PR`.

The workflow still never pushes generated evidence directly to `main` and workflow success still grants no integration authority.

### Contract and prose

`provider-effective-access-contract.json` and `provider-effective-access.md` keep the publication mode `BOUNDED_EVIDENCE_BRANCH_DRAFT_PR` and `draft_pr_required=true`, but explicitly split responsibility:

- recorder -> immutable bounded evidence branch only;
- separate normal ownership/recovery episode -> required draft PR from that exact branch.

A bare evidence branch is not promoted to integrable status. The draft PR remains mandatory before any later evidence integration consideration.

## Producer-side verification required before terminal status

Before terminalizing this remediation:

1. Re-fetch current ownership and branch head.
2. Parse the changed workflow YAML.
3. Parse the changed contract JSON.
4. Verify workflow permissions are exactly bounded to Actions read / Contents write and contain no PR write permission.
5. Verify no REST PR creation remains in the recorder.
6. Verify exact upstream identity, artifact, pre/post worktree, deterministic branch, staged-path, and no-direct-main guards remain present.
7. Verify PR #438 is open/draft at exact evidence head `ad34a0039d99efd04869ae8aeceaed2097d30924` and remains recovery provenance only.
8. Verify the remediation diff is limited to the recorder workflow, provider contract, provider prose, and this handoff.
9. Open an exact-head draft PR from `planning/issue-440` to `main` before terminal status.

## Required fresh review

A fresh independent/degraded-independent security/authority review of the exact remediation packet is mandatory before any squash publication. It must attack whether separating branch publication from draft-PR creation preserves the required ownership/review boundary instead of weakening it to a bare unowned branch, and must verify no new credential or authority path was introduced.

Suggested successor mission: `W2-ENG-PROVIDER-RECORDER-PR-REM-REV-01`.

## Authority boundary

`NOT_CANONICAL`. Recovery/remediation only. No provider credential/PASS, provider-evidence integration, engine selection, commercial/production/legal/release authority, implementation readiness, verification-PASS, content fan-in, decision, or canonical authority.
