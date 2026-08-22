# W2-ENG-UNITY-PERSISTENT-RUNNER-REV-01 — security and authority review

## Review identity

- reviewed issue: #633 / `W2-ENG-UNITY-PERSISTENT-RUNNER-01`;
- reviewed PR: #639;
- producer base: `06134838ebda6c7a348e4ff278062220545f0397`;
- producer head: `a2b28e0913f47f943e2903fcec3ab6982fcf927d`;
- review base: `06134838ebda6c7a348e4ff278062220545f0397`;
- review issue: #640;
- trust mode: `DEGRADED_SINGLE_AGENT_FRESH_REVIEW_EPISODE`;
- producer branch was not modified.

## Review method

The immutable producer head was checked out into a separate detached worktree. The review ran:

- `python3 -m py_compile tools/planning/engine_provider_effective_validator.py tools/planning/record_unity_persistent_evidence.py`;
- full existing validator `--self-test`;
- `git diff --check`;
- workflow/action/reference inspection;
- repository-wide self-hosted target search;
- sanitized recorder fixture validation;
- local runner API observation from the approved workstation: exact name/labels, `online`, `busy=false`.

## Findings

| ID | Attack surface | Result | Evidence |
| --- | --- | --- | --- |
| R1 | Public-repository exposure | PASS | Persistent evaluator has only `workflow_dispatch`; job requires repository `vokerg/everfield`, `refs/heads/main`, and no pull-request/fork event path. Repository-wide search found no other self-hosted target. |
| R2 | Exact trusted source | PASS | Checkout uses pinned `actions/checkout`; job compares checkout HEAD to `GITHUB_SHA` and queries GitHub's current `main` SHA before Unity use. |
| R3 | Runner isolation | PASS | `runs-on` requires `self-hosted`, `macOS`, `ARM64`, `everfield-unity`; the validator additionally requires runner name `everfield-unity-mac`, OS, architecture, repository, event, ref, and SHA. |
| R4 | Permissions and supply chain | PASS | Evaluator is `contents: read`; recorder is the only workflow with `contents: write` and runs on `ubuntu-24.04`; all referenced actions are full commit SHAs. |
| R5 | Session/license boundary | PASS | Evaluator passes no Unity/Unreal secrets; it consumes only local Unity CLI/license state, writes no session material, and uploads only the bounded JSON envelope. |
| R6 | Native execution identity | PASS | The evaluator pins Unity CLI `1.0.0-beta.5`, requires editor `6000.5.6f1`, runs the existing native S3 harness, and labels the result `PERSISTENT_SELF_HOSTED_WORKSTATION`. |
| R7 | Evidence and authority | PASS | Recorder binds exact upstream run/workflow/head/event, projects only fixed fields, rejects sensitive fragments, preserves 50 historical cells, and keeps provider/engine/readiness/decision/canonical authority false. |
| R8 | Failure behavior | PASS | Provider failure remains a bounded sanitized state; unsafe runner identity fails before native execution and recorder rejects untrusted source identity. |

## Residual conditions

The runner's online/idle state is workstation/GitHub external state and must be rechecked before each fresh exact-main run. The local Personal license remains local-only evidence until the integrated workflow produces its own persistent-context evidence. Neither review nor a successful workflow grants provider PASS, engine selection, implementation readiness, production/legal/release, verification, decision, or canonical authority.

## Disposition

`PASS_FOR_INTEGRATION`

No BLOCKER, MAJOR, or correction-requiring MINOR finding was found in the frozen producer. The candidate is safe for the separately authorized exact-head squash integration episode followed by one fresh exact-main persistent Unity run.
