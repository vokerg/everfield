# W2 Unity S3 v5 recorder-trigger remediation review

## Review identity

- review issue: #843 / `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM-REC-REV-01`
- ownership comment: `5536035671`
- trust mode: `DEGRADED_SINGLE_AGENT`
- judged producer: Issue #841 / draft PR #842
- judged producer terminal: `5525877858`
- exact judged head: `ebb1061c40b1042c3750466e58add81b0836fd4a`
- producer base/current main at review freeze: `ab3bc02d502243a6194c42960dd3ea854d14766f`
- canonical binding: Issue #6 comment `5245368879`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- canonicality: `NOT_CANONICAL`

The producer branch is immutable judged input. This review does not edit #841, execute native Unity, integrate any producer bytes, or upgrade evidence authority.

## Frozen producer packet

PR #842 was re-fetched immediately before review publication and remained open, draft, mergeable only as compatibility information, base `main@ab3bc02d502243a6194c42960dd3ea854d14766f`, head `ebb1061c40b1042c3750466e58add81b0836fd4a`.

Judged paths and exact blobs:

- `.github/workflows/unity-s3-v5-lineage-evaluator.yml` — `45654e9e946f1bb45c6d6502b27b62d8e6df29be`
- `.github/workflows/unity-s3-v5-lineage-recorder.yml` — `54e38393f91e96ca09bd3ad84e311b496fc5c4e9`
- `tools/planning/validate_unity_s3_v5_recorder_trigger.py` — `93f543a014a78f6f61dc172a7bdc07cd4d90100d`
- `docs/planning/handoffs/issue-841.md` — producer handoff only

Historical source evidence remains immutable: predecessor #821 terminal `5521310112`, evaluator run `33721358829` attempt `1`, artifact `9880347470`. No fresh evaluator run was launched for this review.

## Adversarial review results

### Boundaries that remain sound in the judged bytes

1. The native `lineage` job remains on `[self-hosted, macOS, ARM64, everfield-unity]` under workflow-level `contents: read`; the producer does not add `contents: write` to the native job.
2. The proposed recorder execution remains on `ubuntu-24.04`, with its write permission isolated to the recorder caller/called job rather than the native Unity job.
3. The recorder is `workflow_call`-only: the producer removes the suppressed `workflow_run` listener and does not expose independent `workflow_dispatch` or `repository_dispatch` on the recorder itself.
4. Caller inputs are not trusted by value alone. The recorder re-fetches the run and binds run id, run attempt, workflow name/path/id, event, branch, repository, head SHA, and current-main identity before projection.
5. Artifact selection remains exact by run id plus the run/attempt-derived artifact name. Projection checkout is pinned to the supplied/re-fetched source head.
6. Evidence publication retains one bounded generated path, exact staged-path checking, immutable run/attempt branch naming, no direct-main push, no automatic PR, and no integration authority.
7. The exact-main requirement is stronger than the old ancestor allowance: stale-main publication fails closed.
8. The workflow-call syntax and caller-job permission surface are supported by current GitHub Actions reusable-workflow semantics; called-workflow token permissions cannot exceed the caller job's granted permissions.

These points do not cure the liveness defect below.

## Finding `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REV-M01`

**Severity:** MAJOR / correction required before integration.

**Finding:** the proposed same-run reusable recorder cannot satisfy its own source-run terminal-state predicate.

The evaluator adds job `record` after `lineage` and calls the reusable recorder with:

- `source_run_id: ${{ github.run_id }}`
- `source_run_attempt: ${{ github.run_attempt }}`
- `source_head_sha: ${{ github.sha }}`

GitHub reusable-workflow jobs execute in the caller workflow context. The called recorder therefore receives the caller evaluator run identity. Its first binding step immediately re-fetches that same run from `actions/runs/{run_id}` and requires both:

- `run.status == "completed"`
- `run.conclusion == "success"`

But the `record` job itself is still executing as part of that caller workflow run. The caller run cannot be terminal `completed/success` until the recorder job finishes. Therefore the recorder's first binding step is temporally unreachable under the proposed topology: it will observe a nonterminal source run and fail its own `status` and/or `conclusion` checks.

This is not a theoretical authority nit. It recreates the functional symptom being remediated: native lineage may succeed and upload its artifact, but durable recorder publication cannot complete.

Current GitHub documentation supports the premises used here:

- reusable workflows are called as jobs and the called workflow's `github` context is associated with the caller workflow;
- workflow-run status distinguishes nonterminal states such as `in_progress` from terminal `completed`, with a conclusion such as `success` applying to terminal completion.

References:

- https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations
- https://docs.github.com/en/rest/actions/workflow-runs

### Static-validator gap

`validate_unity_s3_v5_recorder_trigger.py` requires the literal `status == "completed"` and `conclusion == "success"` guards to exist, but it never proves that those predicates are reachable in the selected same-run topology. Its positive contract therefore locks in the contradiction rather than detecting it. Static string presence is insufficient for this temporal boundary.

### Required bounded correction

Route exactly one remediation successor against this finding. The correction must preserve all clean boundaries above while restoring a recorder execution episode that can observe a terminal successful evaluator run.

The smallest expected shape is an explicit separate GitHub-native continuation compatible with `GITHUB_TOKEN` recursion rules, such as a narrowly parameterized `repository_dispatch`/`workflow_dispatch` handoff from a GitHub-hosted control surface to a GitHub-hosted recorder run. Because dispatch can race the evaluator's final state, the recorder must either start only after terminalization is mechanically guaranteed or perform a bounded fail-closed wait/re-fetch until the exact source run reaches terminal `completed/success` before artifact projection. It must still bind exact run/attempt/workflow/path/repository/main/head/current-main/artifact identity and must not expose a write-capable token to native Unity.

A different design is acceptable only if it preserves equivalent exact evidence semantics and eliminates the circular dependency. Do not weaken the historical contract by simply deleting the source-run success predicate while still claiming successful-run evidence.

The remediation's deterministic validation must include a temporal/reachability negative control demonstrating that a nonterminal source run cannot be mislabelled as completed evidence and a positive control demonstrating that the selected continuation can observe a terminal exact source run without depending on its own completion.

## Finding counts

- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 0
- informational: 0

## Disposition

`CHANGES_NEEDED`

PR #842 / exact head `ebb1061c40b1042c3750466e58add81b0836fd4a` is **not safe for integration** because `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REV-M01` prevents the recorder lifecycle from reaching its required terminal source-run predicate.

Route exactly one bounded remediation successor. Preserve #841/#842 as immutable failed-review provenance. After remediation reaches `REVIEW_READY`, require a fresh security/authority review of its exact immutable head. Only a clean future `PASS_FOR_INTEGRATION` may route separately authorized squash publication, followed by fresh exact-main end-to-end verification.

## Authority negatives

This review grants no integration, provider PASS, `PASS_FOR_COMPARISON`, aggregate verification PASS, engine selection/readiness, gameplay/high-throughput implementation, production/release, verification PASS, decision, or canonical authority.
