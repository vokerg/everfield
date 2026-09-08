# Factory convergence v5 review — Issue #950

## Verdict
`PASS_FOR_INTEGRATION_WITH_POST_PUBLICATION_WORKFLOW_ACCEPTANCE`

Trust mode: `DEGRADED_SINGLE_AGENT`.

Reviewed immutable producer:
- Issue #948 terminal comment `5589449393`;
- draft PR #949;
- exact producer head `037e7c6a483c6ef628901b4dd85a869598c59495`;
- base/current main at review: `96384e0bb80e8225ba41346f6f942b66c0a5081b`;
- exactly three changed paths.

The superseded producer head `766abda23f671238cafea3831f9227f660864d93` was not judged. Producer recovery `5589428167` closed its stale-ownership reopen defect before this review claim.

## Findings
- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- INFO: 1

### INFO-01 — execution acceptance is post-publication
The review environment cannot resolve `github.com` for a local clone, so no local repository self-test PASS is claimed. The workflow modification makes the push-triggered maintenance job compile v1-v5 and execute the complete v5 self-test chain before performing reconciliation. Integration is acceptable only with immediate inspection of that exact-main run; failure requires bounded remediation/rollback and cannot be treated as PASS.

## Adversarial review

### 1. Route parser / false-positive control — CLEAN
`explicit_successor_issue_number` recognizes only underscore-bounded `ISSUE`, `INTEGRATION`, `REVIEW`, and `REMEDIATION` route forms and collects all matched issue numbers into a set. It returns a target only when exactly one unique number remains. Thus an ambiguous route such as `ISSUE_10_THEN_ISSUE_11` fails closed. PR-number fragments are not parsed as successors. Generic prose is never scanned by this rule.

The duplicate matching of the same target through nested forms such as `BLOCKING_REMEDIATION_ISSUE_833` remains unambiguous because both patterns resolve to the same set member.

### 2. Successor eligibility / authority isolation — CLEAN
Explicit route consumption requires the parsed target to exist in the current recent issue index, to be a trusted/eligible issue under the reviewed v2 predicate, and to be neither a pull request nor a factory-transition issue. Closed `duplicate`/`not_planned` targets are rejected. The new rule only suppresses redundant wrapper materialization; it does not mark the target terminal, verified, reviewed, integrated, selected, ready, or canonical.

### 3. Exact-generation wrapper retirement — CLEAN
`explicit_transition_redundancy_reason` first requires the wrapper generation to equal the source's current exact `(issue, terminal_comment_id, route)` generation. Old/stale wrapper generations therefore cannot be retired merely because a later source route names an issue. Before closing a redundant wrapper, v5 delegates to the existing reviewed `transition_has_active_operational_state`; active trusted schema-3 ownership is preserved.

### 4. Exact-generation reuse / stale ownership — CLEAN AFTER PRODUCER RECOVERY
The recovered producer prefers an existing open wrapper. Closed history is eligible only when state reason is `duplicate` or `not_planned` and the existing reviewed operational-state checker reports no active trusted state. Completed history is excluded. This closes the producer self-review finding that existed at the superseded head.

The self-test exposes the checker as an injectable dependency only for deterministic network-free controls; production defaults to the reviewed v2 operational-state function. The `perform_reopen` switch likewise defaults true in production and is used false only by self-tests.

### 5. Existing v1-v4 behavior — CLEAN
v5 composes v4 rather than rewriting it. Normal successor edges, dispatch-backed resolution, v4 semantic transition resolution, registered-route direct dispatch, current-main dispatch binding, recursion suppression, trusted-author checks, and retry semantics are called through the existing layers. No route registry entry changes.

### 6. Workflow surface — CLEAN
The workflow changes only the validation/execution entry point from v4 to v5 and adds v5 to `py_compile`. Existing schedule, concurrency, action checkout pin, and permissions remain unchanged. The v5 self-test calls v4 self-test transitively, preserving the existing v1→v4 deterministic controls.

### 7. Same-run mutation / duplicate loop — CLEAN
The retirement passes mutate only `open_issues`. After retirement, v5 rebuilds its recent issue/index view before materialization. An explicit-target source is then skipped by `explicit_successor_generation_consumed`, so a wrapper closed in the explicit-target retirement pass cannot be recreated later in the same run.

For unresolved non-explicit routes, historical exact-generation reuse happens only after no matching open wrapper exists. If a safe retired wrapper is reopened, it is appended to `open_issues` and no new issue is created. On the next run, normal matching finds the reopened wrapper. This prevents issue-number explosion while preserving liveness.

### 8. Scope / current-main compatibility — CLEAN
PR #949 is mergeable against unchanged `main@96384e0bb80e8225ba41346f6f942b66c0a5081b`. Diff is confined to:
1. `.github/workflows/planning-frontier-maintenance.yml`;
2. `tools/planning/frontier_maintenance_v5.py`;
3. `docs/planning/handoffs/issue-948.md`.

No canonical program, route registry, provider/engine evidence, content packet, implementation source, or unrelated workflow is changed.

### 9. Authority boundary — CLEAN
The repair changes liveness bookkeeping only. It does not bypass review, verification, ownership, exact-head, squash-only integration, engine-selection, implementation-readiness, release, decision, or canonical gates.

## Required integration / acceptance
A clean review authorizes only the bounded owner-directed squash publication of exact PR #949 head `037e7c6a483c6ef628901b4dd85a869598c59495`.

Immediately after publication:
1. verify the returned squash SHA is exact `main`;
2. inspect the push-triggered `Everfield planning frontier maintenance` run for that main SHA;
3. require the validation step to compile v1-v5 and report the complete v5 self-test chain PASS;
4. require reconciliation to complete successfully;
5. re-count open `FACTORY-TRANSITION` issues and verify explicit-target wrappers are retired and no new duplicate exact generations are minted;
6. if the run fails, route bounded factory remediation immediately rather than accepting the integration as operationally successful.

`NOT_CANONICAL` process provenance only.
