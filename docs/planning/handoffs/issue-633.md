# Issue #633 — persistent local Unity execution hub

## Mission / state

- mission: `W2-ENG-UNITY-PERSISTENT-RUNNER-01`;
- role: bounded trusted persistent Unity execution-lane bootstrap;
- state: `IN_PROGRESS`;
- branch: `planning/issue-633`;
- base main: `06134838ebda6a7c348e4ff278062220545f0397`;
- claim comment: Issue #633 comment `5377794869`;
- execution checklist: Issue #633 comment `5377793467`;
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner Option-D trigger: Issue #563 comment `5374920635`.

## Scope

This candidate adds a repository-scoped, Unity-only persistent workstation lane that remote agents can trigger with `workflow_dispatch`, executes the existing native S3 harness on Unity `6000.5.6f1`, and records only sanitized evidence. It keeps the existing GitHub-hosted provider workflow and Unreal lane independent.

Non-goals: gameplay implementation, engine selection, paid Unity licensing, new cloud infrastructure, exporting browser/session/license material, generic self-hosted execution, or any provider/readiness/decision authority.

## Local workstation bootstrap

- runner name: `everfield-unity-mac`;
- repository scope: `vokerg/everfield`;
- runner labels: `self-hosted`, `macOS`, `ARM64`, `everfield-unity`;
- runner version: `2.336.0`;
- official asset: `actions-runner-osx-arm64-2.336.0.tar.gz`;
- asset SHA-256: `8e8839c49b7060b6b2154f4931f815df330c27f167d53ef2239ee3dfce28b079`;
- local runner directory: `/Users/dg/actions-runner-everfield-unity`;
- service: per-user macOS LaunchAgent installed and started by `svc.sh`;
- registration token: ephemeral, not printed, committed, or recorded;
- registration verification: GitHub API reported `online`, `busy=false`, exact name and labels.

## Local evidence before repository mutation

- Unity CLI: `1.0.0-beta.5`;
- Unity editor: `6000.5.6f1`;
- local license status: active;
- local native S3: `N1=PASS`, `N2=PASS`, `FI1=PASS`;
- local execution context: existing approved persistent workstation;
- auth status remains local/provider-scoped and no session material is exported.

## Repository interfaces

- evaluator: `.github/workflows/unity-persistent-evaluator.yml`;
- recorder: `.github/workflows/unity-persistent-evidence-recorder.yml`;
- producer validator mode: `python3 tools/planning/engine_provider_effective_validator.py --persistent-unity-proof`;
- sanitized producer schema: `W2-ENG-UNITY-PERSISTENT-ACCESS-v1`;
- sanitized evidence schema: `W2-ENG-UNITY-PERSISTENT-ACCESS-EVIDENCE-v1`;
- evidence path after recorder publication: `docs/planning/wave-2/evidence/ci/unity-persistent-access/<run-id>/effective.json`.

Remote trigger contract after integration:

```bash
gh workflow run "Everfield persistent Unity exact-main evaluator" --repo vokerg/everfield --ref main
```

The workflow accepts only `workflow_dispatch` on `main`, checks the checked-out SHA against the current `main` branch, requires the exact runner identity/platform labels, and never consumes repository Unity credentials. It uploads a bounded artifact; the recorder validates the exact upstream run and publishes an immutable evidence branch for the normal draft-PR/squash lifecycle.

## Security / authority boundary

- no `pull_request`, fork, arbitrary-branch, or `pull_request_target` path targets the persistent runner;
- job permissions are `contents: read` only;
- actions are pinned by commit SHA;
- runner identity, repository, event, ref, current-main SHA, editor identity, and execution context are checked before native Unity use;
- evidence contains no session, cookie, password, OAuth, license, Authorization, registration-token, or secret hash material;
- workflow success and local Unity PASS do not grant provider, engine-selection, implementation-readiness, production, legal, release, verification, decision, or canonical authority.

## Checks completed

- `python3 -m py_compile` for validator and recorder: PASS;
- existing validator full deterministic self-test: PASS;
- persistent runner identity self-tests: PASS;
- in-memory sanitized recorder fixture: PASS;
- Ruby YAML parse for both workflows: PASS;
- `git diff --check`: PASS;
- workstation runner online/idle: PASS.

## Remaining gates

1. Commit and push the producer branch.
2. Open the exact-head draft PR and publish `STATUS(REVIEW_READY)`.
3. Complete the required independent security/authority review.
4. Squash-integrate through a separate authorized integration episode.
5. Trigger one fresh exact-main persistent Unity run and publish its immutable sanitized evidence.

## Reopen / fail-closed conditions

Reopen if any runner identity, label, trusted-main, workflow event, editor-version, evidence-schema, or secret-sanitization check drifts. Stop at `SUCCESS` only after the integrated exact-main workflow executes native Unity and the recorder publishes durable evidence; otherwise record the exact external or safety condition without weakening the runner boundary.

Authority: `NOT_CANONICAL`.
