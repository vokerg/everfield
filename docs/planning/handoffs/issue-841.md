# Handoff — Issue #841 / W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM-REC-01

## Recovery boundary

- task class: `RECOVERY_CONTINUATION -> BLOCKING_REMEDIATION`;
- stranded predecessor: Issue #833 / claim `5521313186`;
- stranded branch `planning/issue-833`: absent after six-hour lease expiry;
- recovery issue: #841;
- recovery ownership: comment `5525782353`;
- branch: `planning/issue-841`;
- claim/current-main basis: `ab3bc02d502243a6194c42960dd3ea854d14766f`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- canonicality: `NOT_CANONICAL`.

The missing #833 branch is not recreated and no terminal record is fabricated on #833. This issue performs the same authorized recorder-trigger remediation in a fresh bounded ownership episode.

## Frozen triggering defect

Immediate technical predecessor #821 terminal `5521310112` proved exact-main sanitized artifact liveness for evaluator run `33721358829`, attempt `1`, artifact `9880347470`, while no reviewed recorder run or immutable evidence branch materialized.

The defect is trigger topology, not native-evaluator execution. The evaluator was repository-dispatched with `GITHUB_TOKEN`; a downstream `workflow_run` listener cannot be assumed to materialize from that token-caused run. Retrying the same topology would not remediate the deterministic platform constraint.

## Remediation design

The producer replaces event-recursive recorder chaining with an explicit same-run reusable-workflow dependency:

1. `.github/workflows/unity-s3-v5-lineage-evaluator.yml`
   - keeps workflow-level `contents: read`;
   - keeps the native `lineage` job on `self-hosted, macOS, ARM64, everfield-unity`;
   - adds a `record` job only after successful `lineage` completion;
   - the caller job has only `actions: read` and `contents: write` and invokes the recorder reusable workflow;
   - passes exact `github.run_id`, `github.run_attempt`, and `github.sha`.

2. `.github/workflows/unity-s3-v5-lineage-recorder.yml`
   - removes `workflow_run` and exposes only `workflow_call` with required run-id, attempt, and source-head inputs;
   - remains on GitHub-hosted `ubuntu-24.04`;
   - re-fetches the supplied source run and rejects mismatched id, attempt, evaluator name/path, event, completion, conclusion, branch, repository, or head;
   - requires the source head to equal exact current `main` before publication;
   - checks out exact source-head projection code;
   - downloads only the exact run/attempt artifact name from the exact source run;
   - keeps the one-generated-file invariant and immutable `evidence/unity-s3-v5-lineage/run-N-attempt-M` branch publication;
   - creates no PR and grants no integration authority.

3. `tools/planning/validate_unity_s3_v5_recorder_trigger.py`
   - deterministic static contract checker for runner/permission separation, explicit dependency, input binding, trigger topology, exact-run/workflow/head/current-main checks, exact artifact binding, immutable evidence branch, one-file publication, and authority negatives.

This design requires no PAT/App secret, no write-capable token on the self-hosted Unity job, no provider credentials, no manual evidence projection, no direct-main write, and no independently forgeable recorder dispatch surface.

## Validation contract

Before terminal status, run or independently reproduce:

```text
python3 tools/planning/validate_unity_s3_v5_recorder_trigger.py
python3 -m py_compile tools/planning/validate_unity_s3_v5_recorder_trigger.py
```

Also inspect the exact PR diff for:
- only evaluator workflow, recorder workflow, static validator, and this handoff;
- native job remains read-only;
- recorder is reusable-only and GitHub-hosted;
- no automatic fresh evaluator run from this producer branch;
- no direct integration/canonicalization authority.

A fresh exact-main native episode is intentionally deferred until after clean required security/authority review and separately authorized squash publication.

## Required next gate

This producer must terminalize only as `STATUS(REVIEW_READY)` on an exact immutable draft-PR head. Route one fresh independent/degraded-independent required review. The review must attack token permissions, runner separation, arbitrary/forged run inputs, workflow identity, source-head/main checks, artifact binding, immutable evidence publication, recursion/loop risk, automatic PR/integration, and authority inflation.

Only a clean review disposition `PASS_FOR_INTEGRATION` may route a separate integration owner. Mergeability or draft state alone is not authority.

## Authority boundary

`NOT_CANONICAL`. Recorder-trigger remediation only. No provider PASS, `PASS_FOR_COMPARISON`, aggregate verification PASS, engine selection/readiness, gameplay/high-throughput implementation, production/release, decision, integration-by-producer, or canonical authority. The terminal Issue #841 schema-3 status is authoritative for final work/head/PR/blob identities after this handoff commit.
