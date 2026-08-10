issue: 24
mission_id: W1-FAC-02
role: control-plane/scheduler planner
branch: planning/issue-24
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5245482549
work_sha: 095372a41498e8d7e3b25364cba89dbc647b8839
state: REVIEW_READY
completed:
  - Produced docs/planning/wave-1/proposals/github-control-plane-and-scheduler.md from the authoritative repository packet plus current official GitHub documentation triggered by the issue's capability-evidence requirement.
  - Distinguished canonical repository graph/contracts, authoritative GitHub operational state, derived scheduler/Projects caches, and disposable agent state.
  - Proposed native GitHub issue dependencies as a hard-edge mirror while preserving richer typed canonical graph edges.
  - Proposed and bounded an empirical GraphQL updateRefs task/ref-lock CAS design for atomic claim/resume/recovery/conflict locking; did not claim the combined protocol is proven before spike FAC2-E1.
  - Defined separate ownership fence vs lease freshness semantics and a reconciliation path for crashes between CAS and audit-event publication.
  - Defined deterministic READY proof, cycle/invalid-dependency validation, scheduler classes, WIP governors, starvation diagnostics, and quality-queue preference.
  - Defined squash-only PR integration with repository merge-method restriction, expected PR head, and Everfield current-base verification invariant.
  - Deferred merge-queue adoption until an explicit squash/current-base/provenance spike passes.
  - Proposed least-privilege GitHub App/reconciliation architecture and Projects as a derived UI/cache only.
  - Defined garbage-collection constraints and nine bounded control-plane experiments.
remaining:
  - W1-REV-FAC must attack factory/liveness/WIP/authority/GC assumptions after all factory producer inputs are ready.
  - W1-REV-TECH must attack API/ref-lock/ruleset/check/merge/reconciliation assumptions after all technical producer inputs are ready.
  - FAC2-E1/E2/E4/E5/E6 are required before the most security-sensitive enforcement recommendations can become canonical implementation decisions.
checks_performed:
  - Review Index measured approximately 3.7 KB UTF-8, below the 4,000-byte limit.
  - Current GitHub capability claims are supported by official docs for refs/updateRefs, issue dependencies/sub-issues, rulesets/protection, PR merge expected SHA/method, repository merge settings, GitHub App permissions, and Projects automation.
  - Unproven composition claims are explicitly labeled experiments/assumptions rather than facts.
  - READY derivation does not use labels/assignees/Projects as authority.
  - Head-SHA merge protection is explicitly supplemented by verified-base equality/refresh; stale-base merge is not treated as safe.
  - WIP/scheduler policy is deterministic class-first and avoids an opaque scalar reward function.
  - Control-plane App permissions are proposed least-privilege and high-privilege ruleset provisioning is separated.
  - No gameplay implementation, automation installation, ruleset mutation, extra current-wave issue creation, self-review, or self-canonicalization is authorized.
  - All main integration remains squash-only.
evidence:
  - docs/planning/wave-1/proposals/github-control-plane-and-scheduler.md at work_sha 095372a41498e8d7e3b25364cba89dbc647b8839
  - official GitHub Docs refs enumerated in the proposal's evidence table (snapshot 2026-08-10)
  - canonical repository packet at activation main 413e729e8d2d5ac2eb138903f3f2ace07283b23e
known_problems:
  - The proposed multi-ref lock protocol has not yet been executed against this repository; exact namespace/ruleset/permission behavior remains empirical.
  - No final authoritative lease timestamp store is selected.
  - Exact WIP/high-watermark values require benchmark evidence.
  - Merge queue remains deferred until exact squash/current-base behavior is verified.
  - Exact permission split and protected-check topology require W1-FAC-03/W1-FAC-04 synthesis.
decisions:
  - Canonical task graph/contract is content-addressed repository authority; native issue dependencies mirror hard edges; Projects are derived.
  - Comments/labels/assignees alone are insufficient for mature atomic ownership.
  - Prefer CAS ref fencing plus reconciliation if FAC2-E1 validates it; otherwise reconsider transactional substrate.
  - Keep current-base verification as a separate invariant from expected-head merge protection.
  - Scheduler policy changes are judge-affecting and must be versioned/benchmarked/reviewed.
scope_deviations: []
recommended_next_action: Leave this proposal NON-CANONICAL and REVIEW_READY; continue the root frontier. W1-REV-FAC and W1-REV-TECH will review it independently once their full prerequisite packets are ready.

## Final head note

`work_sha` is the substantive proposal commit. Final schema-3 STATUS must bind the later branch head containing this handoff.