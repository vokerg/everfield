# Handoff — Issue #845 / W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM-02

## Remediation boundary

- task class: `BLOCKING_REMEDIATION`;
- issue: #845;
- claim comment: `5536082503`;
- actor/session: `recorder-trigger-remediation-845-gpt56sol-20260904-01`;
- branch: `planning/issue-845`;
- base/current-main basis: `ab3bc02d502243a6194c42960dd3ea854d14766f`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- canonicality: `NOT_CANONICAL`.

Source review/failure:

- failed producer: Issue #841 / PR #842 / `ebb1061c40b1042c3750466e58add81b0836fd4a`;
- required review: Issue #843;
- review terminal: `5536070954`;
- disposition: `CHANGES_NEEDED`;
- finding: `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REV-M01`;
- review report blob: `1b0b5d61c70dd47852dc8a9ab318080c21cc9334`;
- review handoff blob: `9ba0ed1e05a86a558fa5dbf55978baa3c0b25943`.

Historical evaluator run `33721358829` attempt `1` / artifact `9880347470` remains frozen historical evidence. This producer does not rerun or relabel it.

## Defect corrected

The failed #841 design invoked the recorder as a reusable job inside the evaluator workflow and passed that caller's `github.run_id`. The recorder then required the same run to already be `completed/success`. Because the recorder job itself was part of that run, the terminal predicate could not become true until after the recorder returned.

This remediation removes that circular same-run route.

## Remediation topology

### Native evaluator

The native `lineage` job remains unchanged in execution authority:

- runner: `[self-hosted, macOS, ARM64, everfield-unity]`;
- workflow default: `contents: read`;
- no provider credentials;
- no `actions: write`;
- no `contents: write`;
- no direct-main or evidence-branch publication.

After successful native lineage/artifact upload, a separate `dispatch_recording` job runs on `ubuntu-24.04`. That control job:

- has only `actions: write`;
- performs no repository checkout;
- uses the repository `GITHUB_TOKEN`;
- calls the GitHub Actions workflow-dispatch REST endpoint for the recorder on `main`;
- passes only exact source run id, attempt and source head SHA.

GitHub documents that `workflow_dispatch` is an exception to the normal `GITHUB_TOKEN` recursion suppression, and the workflow-dispatch REST endpoint requires Actions write permission. No PAT or GitHub App secret is added.

### Separate recorder run

The recorder is now `workflow_dispatch`-only; both the old suppressed `workflow_run` route and the failed same-run `workflow_call` route are absent.

The recorder starts on `ubuntu-24.04`, checks out its own exact `github.sha` from `main` with persisted credentials disabled, and executes the repository-owned source-run gate:

`tools/planning/unity_s3_v5_recorder_source_gate.py`

The gate:

1. validates source run id, attempt, evaluator workflow name, event, main branch, repository, head and workflow id on every observation;
2. permits only `queued` / `in_progress` while waiting;
3. uses a bounded `24 x 5s` poll window;
4. accepts only terminal `status=completed` plus `conclusion=success`;
5. fails closed on any other state/conclusion, identity drift, API failure or timeout;
6. validates exact evaluator workflow name/path/id;
7. requires source head == exact current `main`;
8. requires the recorder workflow code SHA == the same exact source/current-main SHA.

Only after this gate passes does the recorder check out source projection code and download/project the exact run/attempt artifact.

Immediately before evidence-branch publication, the same gate is rerun with one poll and no wait, closing the artifact-processing/main-drift window as far as the branch-publication handoff permits.

The existing immutable evidence branch, one generated file, staged-path guard, no automatic PR, and no integration authority are preserved.

## Deterministic validation

`tools/planning/validate_unity_s3_v5_recorder_trigger.py` checks:

- native lineage has no write/dispatch authority;
- dispatch authority is isolated to a GitHub-hosted post-lineage job;
- dispatch uses the explicit workflow-dispatch endpoint and exact source inputs;
- same-run `workflow_call` and suppressed `workflow_run` are forbidden;
- recorder is GitHub-hosted and dispatch-only;
- trusted gate checkout/wait/source-checkout ordering is fixed;
- terminal polling is bounded;
- exact artifact and immutable one-file publication identities are preserved;
- final exact-main/source recheck occurs before publication.

The validator executes the source gate's temporal self-test. The self-test proves:

- `queued -> in_progress -> completed/success` is accepted;
- failed terminal source is rejected;
- indefinitely nonterminal source times out;
- wrong run attempt, head, workflow path and current-main/workflow-head identities are rejected.

The validator also runs mutation-negative controls against dispatch permission, dispatch endpoint, same-run route, recorder trigger, and polling policy.

Local deterministic execution of this exact producer packet returned:

`unity-s3-v5 recorder trigger temporal/static contract: PASS`

No native Unity execution was performed.

## Mutable paths

Exactly five paths are part of this bounded producer packet:

- `.github/workflows/unity-s3-v5-lineage-evaluator.yml`;
- `.github/workflows/unity-s3-v5-lineage-recorder.yml`;
- `tools/planning/unity_s3_v5_recorder_source_gate.py`;
- `tools/planning/validate_unity_s3_v5_recorder_trigger.py`;
- `docs/planning/handoffs/issue-845.md`.

The fifth path beyond the expected four is the small shared source-run gate. It is required so runtime terminality semantics and deterministic temporal tests execute the same code rather than duplicating the #841 string-only validation failure.

## Required next gate

This packet is producer evidence only. It must terminate `REVIEW_READY` on an exact-head draft PR, then receive one fresh independent/degraded-independent security/authority review.

The reviewer must attack:

- whether `actions: write` is truly confined to the GitHub-hosted dispatch control;
- manual/forged recorder dispatch inputs;
- source-run polling races and terminal conclusions;
- source/current-main/workflow-code equality;
- arbitrary workflow/run/attempt/head/artifact substitution;
- dispatch recursion/loop risk;
- immutable branch and one-file publication;
- static/temporal test adequacy;
- authority inflation.

Only a clean future `PASS_FOR_INTEGRATION` may route separate authorized squash publication. Fresh exact-main end-to-end native verification belongs after that publication.

## Authority negatives

No provider PASS, `PASS_FOR_COMPARISON`, aggregate verification PASS, engine selection/readiness, gameplay/high-throughput implementation, production/release, verification PASS, integration-by-producer, decision, or canonical authority is granted here.
