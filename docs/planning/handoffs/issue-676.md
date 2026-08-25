# Issue #676 — Factory liveness repair handoff

## Scope
Owner-directed repair of the planning factory's liveness and queue hygiene. No gameplay implementation, engine choice, verification PASS, decision, or canonical authority is created.

## Defects addressed
- GitHub-open issues could remain in the candidate queue after trusted schema-3 `DONE`, `SUPERSEDED`, or `INVALIDATED` terminal records.
- Required next routes could be recorded only in terminal comments without a live successor/recovery issue.
- A required `workflow_dispatch` continuation could be misclassified as a project-level external blocker merely because an agent connector lacked a dispatch operation.
- Explicitly rejected draft PRs could remain open and pollute frontier scans.

## Repair
- `tools/planning/frontier_maintenance.py`: conservative trusted-author schema-3 reconciliation, rejected-draft cleanup, missing-transition materialization, and whitelist-only exact-main workflow dispatch.
- `.github/workflows/planning-frontier-maintenance.yml`: runs on every `main` push, hourly schedule, and manual dispatch; permissions are bounded to read contents plus issues/PR/actions writes required by maintenance.
- `.github/planning-frontier-routes.json`: explicit execution allowlist. Initial registration covers only the blocked Unity S3 reviewed-v5 lineage dispatch route from Issue #675.
- `AGENTS.md` and `docs/planning/START-HERE.md`: record the owner liveness directive so fresh agents reconcile terminal storage state and materialize missing required transitions before normal frontier priority.

## Safety properties
- Untrusted issue comments cannot create terminal authority for maintenance; only OWNER/MEMBER/COLLABORATOR schema-3 terminal comments are consumed.
- `BLOCKED`, `REVIEW_READY`, `VERIFICATION_READY`, and ordinary open work are not auto-closed.
- PR auto-retirement is limited to trusted-author draft PRs whose own body explicitly carries `CHANGES_NEEDED`, `CHANGES_REQUIRED`, `must not integrate`, or `must not be merged`.
- Required-next-route text cannot execute arbitrary code. Only exact route IDs in the repository-owned JSON registry may dispatch, and registered dispatches require `ref: main`.
- Closure/dispatch creates no review, verification, integration, selection, readiness, decision, or canonical authority.

## Verification performed
- Maintenance Python compiles with Python 3.
- The target Unity lineage workflow was re-read and accepts the registered optional `reason` input under `workflow_dispatch`, while itself enforcing exact repository/ref/SHA/current-main/runner identity.
- Main integration remains squash-only. A fresh review of the immutable producer head is required before integration because this change has issue/PR/action write permissions.

## Expected post-integration behavior
The push of the squash commit to `main` triggers maintenance. It should reconcile terminal-open issues, close explicitly rejected draft PRs, recognize Issue #674 as already consumed by successor #675, materialize the still-required successor from terminal Issue #675, and dispatch the registered Unity lineage evaluator on the exact new current `main`.
