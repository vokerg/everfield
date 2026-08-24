# W2 Unity S3 reviewed-v5 lineage instrumentation — recovery review

Mission: `W2-ENG-TECH-UNITY-S3-V5-RERUN-REV-REC-01`  
Recovery issue: #670  
Stranded predecessor review: #669 / claim `5384366594`  
Judged producer: Issue #667 / PR #668  
Judged producer terminal: `5384329522`  
Judged producer head: `1d32cb5f0bf7a7200508cdcddec3c246da748e1f`  
Review base: `ec5fc3f6313ee2e91e530ca83b1f80e2f355eeed`  
Trust mode: `DEGRADED_SINGLE_AGENT`  
Disposition: `PASS_FOR_INTEGRATION`

## Recovery boundary

Issue #669 cannot be resumed through ordinary schema-3 stale-owner recovery: its only ownership generation is beyond the inherited six-hour lease and the declared source branch `planning/issue-669` is absent. This review therefore republishes only the already-required frozen-input review through Issue #670. It does not recreate, validate, close, or otherwise upgrade #669.

The producer branch and PR are immutable judged inputs. This review changes no producer code.

## Frozen identities

Canonical Planning Program v1 remains active through:

- canonical blob `e3120ec203c4156328770aa86c12fbb7187966dc`;
- binding Issue #6 comment `5245368879`;
- activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e` in current-main ancestry.

Producer #667 is terminal `REVIEW_READY` at exact head/work `1d32cb5f0bf7a7200508cdcddec3c246da748e1f`. Draft PR #668 is still open/draft, base `main@ec5fc3f6313ee2e91e530ca83b1f80e2f355eeed`, head `1d32cb5f0bf7a7200508cdcddec3c246da748e1f`.

Exact judged blobs:

- `tools/planning/unity_s3_v5_lineage.py` — `99acf89606ee88d763a1909a1992be102e52bef2`;
- `tools/planning/record_unity_s3_v5_lineage.py` — `43e2f9da098e46948fd0da03a676859b66ba8789`;
- `.github/workflows/unity-s3-v5-lineage-evaluator.yml` — `188e84cf897ca0c09f862ffc03040fed1ce7cd87`;
- `.github/workflows/unity-s3-v5-lineage-recorder.yml` — `3346f422b316f03e7467b804261adccfcb0ac79e`;
- `docs/planning/handoffs/issue-667.md` — `2098ed0ff0d55b0f14f9c423ce144cf2c9adbf15`.

Reviewed-v5 validator remains blob `2c646988dc16e212f43df6a4ee5ce646622ac2a6`. The persistent execution lane remains the terminal Issue #633 route, whose security/authority review #640 ended `PASS_FOR_INTEGRATION` at comment `5377851945` before its later exact-main publication/evidence lifecycle.

## Adversarial review

### 1. Trusted-runner exposure and exact-main fencing — PASS

The evaluator is `workflow_dispatch` only and requires repository `vokerg/everfield`, `refs/heads/main`, the trusted event type, exact checkout `GITHUB_SHA`, current remote main equality, runner name `everfield-unity-mac`, macOS and ARM64 before Unity execution. It has no PR, fork, arbitrary-branch, `pull_request_target`, issue-comment, or artifact-controlled execution trigger.

The persistent job has `contents: read` only. Checkout and upload actions are 40-hex pinned to the identities already used by the reviewed persistent lane. The new evaluator additionally disables persisted checkout credentials. The lane supplies no provider credential; it relies only on the already-approved persistent workstation context. No integration, provider, comparison, readiness, decision, release, or canonical authority is inferred from workflow success.

### 2. Workspace identity and isolation — PASS

Each N1/N2/FI1 attempt receives its own child directory under a new process-scoped `TemporaryDirectory`. The child is created immediately before the attempt, checked empty before project generation, and used as the exact Unity `-projectPath`. A per-attempt marker is written inside that actual directory before project materialization. The retained `workspace_id` is derived from the attempt identity plus the marker digest; the absolute directory path is never retained.

This is sufficient for the reviewed-v5 requirement, which requires a non-empty unique workspace identity rather than a filesystem path or inode identity. The producer additionally requires all three workspace IDs to be unique. Substituting one retained workspace identity across attempts fails validation.

### 3. Reconstruction/reset derivation — PASS

Reset state is fail-closed from a bounded conjunction: fresh child directory creation by the controlled execution path, pre-generation emptiness, absence of known generated-state directories, marker-before-project ordering, source materialization matching the embedded contract, project-version identity, and fixed-input identity. `reset_verified` is recomputed as `all(reset_facts.values())` and validation requires the retained boolean to equal that mechanical result and to be true.

`reset_id` binds attempt identity, workspace identity, generated-source digest, fixed-input digest, and the reset-fact object. The validator requires distinct reset IDs and distinct workspaces for all N1/N2/FI1 attempts. False reset authority, duplicate workspace/reset lineage, tampered source, wrong resource class, wrong run identity and retained sensitive/path data all have explicit rejection paths in the producer/recorder validation logic.

The two control-flow facts (`fresh_attempt_directory_created` and `workspace_marker_created_before_project`) are constants only after the functions that perform those operations have been invoked in that exact order; the independently observed emptiness/source checks prevent those constants from manufacturing a passing reused/generated-state workspace. This does not create a correction-requiring finding.

### 4. `W2-ENG-HOST-COMMON-v2` semantics — PASS

The unchanged reviewed-v5 validator defines `W2-ENG-START-COLD-v2` as `cache_mode=COLD`, `generated_state_policy=REGENERATE_FROM_REPO`, and `resource_class=W2-ENG-HOST-COMMON-v2`. It separately rejects non-common resource-class labels and later requires per-attempt resource-class equality. It does not define `W2-ENG-HOST-COMMON-v2` as “GitHub-hosted” or as a particular ephemeral machine implementation.

#667 realizes the semantic start contract by creating a new isolated attempt directory, refusing pre-existing generated state, and materializing the exact embedded project/input for every attempt. It records the physical execution context separately as `PERSISTENT_SELF_HOSTED_WORKSTATION` plus exact runner name/OS/architecture. Therefore the common-resource semantic class is not being used to conceal or relabel the persistent execution context, and no resource exception is asserted.

### 5. S3 semantics and identity graph — PASS

The producer fixes candidate `Unity`, Unity `6000.5.6f1`, S3, seed `424242`, 32 entities, 600 ticks, 10 actions, two normal attempts and exactly one `FI-S3-INPUT-PERTURB-v2` attempt under `REAL_OR_SHARED_RULES`. Expected normal checksum is `405227`; the perturbation path changes the tick-137 action and expects `405122`.

The identity graph is acyclic in the authority-bearing direction:

1. fixed input and generated project source are canonical-hashed;
2. candidate-work identity binds candidate/version/reviewed-v5 identities/input/source/editor/resource class;
3. lineage digest binds the observed per-attempt envelope but deliberately excludes candidate-generation identity;
4. candidate-generation identity binds candidate-work, source head, run identity and the three lineage digests;
5. the retained raw-attempt digest then binds the sanitized complete attempt record including candidate-generation identity and lineage digest;
6. source-binding identity binds attempt, candidate generation, raw-attempt digest, workspace/reset and generated-source digest;
7. the source registry must exactly reproduce each lineage/raw/source-binding tuple.

Validation recomputes these values and requires three distinct workspace, reset, source-binding and lineage identities. The registry and attempt lists are exact ordered N1/N2/FI1 sets. There is no generation↔lineage hash cycle and no accepted duplicate/cross-attempt substitution path.

“Raw-attempt digest” here is intentionally the canonical digest of the sanitized attempt record, not a hash of Unity logs or credential/session-bearing bytes. That interpretation is consistent with the mission’s explicit prohibition on retaining raw logs/session material and remains mechanically recomputable by the recorder.

### 6. Recorder trust and publication boundary — PASS

The recorder runs on GitHub-hosted Ubuntu after the named evaluator completes successfully. It re-fetches the exact upstream run and checks run ID/attempt, workflow name/ID/path, event, conclusion, source repository, main branch and source head. It then resolves current main; if main has advanced, the source head must still be an ancestor. Projection code is checked out from the exact source head and deterministic validation is rerun there.

Artifact download is constrained to the exact upstream run ID/attempt and exact deterministic artifact name. The recorder stages exactly one generated evidence JSON path. Publication creates a run/attempt-qualified evidence branch and uses a normal non-force push; the workflow neither pushes to main nor creates a PR. The emitted publication metadata explicitly requires a separate normal ownership episode, squash-only handling and a fresh expected-head check.

### 7. Sensitive data and path boundary — PASS

The retained packet contains editor basename/digest, generated-source/input digests, runner classification, bounded process exit/timeout/timing and derived lineage identities. Captured stdout/stderr are held only in memory long enough to parse the bounded checksum and are removed before the attempt record is constructed. Unity log text is read only from the temporary attempt directory and is not copied into the packet or artifact.

Recursive retained-data validation rejects sensitive key fragments, known credential-bearing value fragments, Unix absolute paths and Windows absolute paths. Because arbitrary stdout/stderr/log/environment values are not retained, the scan is applied to a closed code-generated schema rather than an uncontrolled free-text log surface. No secret hash is required or retained.

### 8. Historical immutability and authority boundary — PASS

The five-path producer diff does not modify the persistent provider/access evaluator/recorder, provider validator/projection, reviewed-v5 validator or historical evidence. The packet requires the historical Issue #82 `NOT_RUN` count to remain 50 and mutation flag false.

All authority fields remain false for provider PASS, `PASS_FOR_COMPARISON`, engine selection, implementation readiness, production/commercial/legal/release, verification-PASS, decision and integration; canonicality remains `NOT_CANONICAL`. The recorder repeats the no-integration boundary. A successful native checksum is therefore evidence input only, not a decision.

## Verification boundary

Producer #667 recorded deterministic compile/self-tests and static workflow checks before its terminal status. This review independently inspected the exact frozen code/diff and its negative-control/recomputation paths. No trusted-main Unity execution is performed or authorized by this review; such execution is intentionally a post-integration gate. The review environment did not substitute an untrusted local checkout or a producer-branch runtime for that gate.

## Findings

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

No contract-specific blocker remains for publication of the instrumentation itself.

## Disposition

`PASS_FOR_INTEGRATION` for the exact producer head `1d32cb5f0bf7a7200508cdcddec3c246da748e1f` only.

This disposition is review provenance, not integration authority. It permits only a separately authorized, fresh-current-main, exact-head, squash-only publication of PR #668 as noncanonical instrumentation provenance. After such integration, the next technical gate is a fresh exact-main persistent Unity lineage evaluator run and its separately owned evidence publication. Formal reviewed-v5 adaptation/generation/aggregation and any `PASS_FOR_COMPARISON` remain later verification/review gates.

`NOT_CANONICAL`. No provider PASS, Unity license authority, engine selection, implementation/readiness, verification-PASS, decision, production/commercial/legal/release, or canonical authority.
