# W2-GH-01 — GitHub multi-ref ownership and conflict-lock empirical spike

**Mission:** `W2-GH-01`  
**Issue:** #70  
**Task class:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Task branch:** `planning/issue-70`  
**Activation/base:** `e4b7ee0a2699a57216146e99b990ab64edaae1d1`  
**Schema-3 claim:** comment `5251309873`  
**Observed date:** 2026-08-11  
**Mature lock/CAS adoption result:** **INCONCLUSIVE**  
**Current ownership authority:** canonical schema-3 remains authoritative.

## Review Index

- **Scope:** actual-repository tests of ref creation/nonexistence, non-force update fencing, recovery lineage, namespace reconciliation, unordered multi-ref contention, current ruleset/permission state, and post-squash ref persistence.
- **Positive evidence:** duplicate exact ref creation was rejected; a recovered ref head fenced a stale sibling writer; namespace scanning reconstructed the current lock ref without event history.
- **Negative/risk evidence:** naive unordered acquisition of two independent lock refs permits a circular partial-hold state; squash integration does not garbage-collect task refs.
- **Inconclusive surfaces:** true multi-credential concurrency, server-time lease expiry, webhook/event-loss recovery, non-admin/ruleset enforcement, GraphQL `expectedHeadOid` execution, and ref deletion/GC were not available in this execution surface.
- **Decision:** do not promote mature multi-ref lock/CAS. Keep it `EVIDENCE_REQUIRED`; keep schema-3 as the sole ownership/status authority.
- **Next review:** `W2-REV-01` should attack overclaiming from sequential/same-credential surrogates, permission assumptions, deadlock recovery, and GC.

## 1. Scope and non-goals

This experiment asks whether GitHub refs can mature into a stronger ownership/conflict-lock mechanism for Everfield without replacing canonical schema-3 authority.

In scope:

- create-if-absent/nonexistence behavior;
- stale-writer fencing after recovery;
- crash/event-independent state reconstruction by ref scan;
- multi-ref acquisition/deadlock behavior;
- current repository ruleset and credential capability;
- GC feasibility and post-squash persistence;
- exact attempt lineage retained as Git objects/refs.

Non-goals:

- no production/gameplay implementation;
- no replacement of schema-3 comments as current authority;
- no claim of distributed-lock correctness from one credential or sequential tests;
- no engine, provider, or implementation-readiness decision.

## 2. Constraints and assumptions

### Observed constraints

- The connected GitHub actor is `vokerg` with repository `admin` permission.
- Repository ruleset enumeration returned an empty set (`[]`) during this episode.
- The available connector exposes ref creation/update/read and raw Git object writes, but not a ref-delete mutation or GitHub GraphQL mutation execution.
- Only one authenticated execution credential/context was available for these GitHub mutations.

### Consequence

Permission separation, active ruleset enforcement, true two-credential racing, exact GraphQL `expectedHeadOid` behavior, and create/delete GC cannot receive empirical PASS here. They remain **INCONCLUSIVE**, even where current GitHub documentation describes the relevant capability.

## 3. External primary-source evidence

All external capability claims below were refreshed from GitHub's official documentation on 2026-08-11.

1. Git references REST API: https://docs.github.com/en/rest/git/refs
   - create-reference requires repository Contents write permission and documents `201`, `409`, and `422` outcomes;
   - update-reference with `force=false` is specified to require a fast-forward rather than overwrite work;
   - matching-refs supports namespace reconstruction;
   - delete-reference is documented and requires Contents write permission.
   - documentation examples observed during this episode use API version `2026-03-10`.
2. GraphQL commit mutation: https://docs.github.com/en/enterprise-cloud@latest/graphql/reference/commits
   - `createCommitOnBranch` atomically creates a commit and updates its branch.
3. GraphQL input contract: https://docs.github.com/en/enterprise-cloud@latest/graphql/reference/input-objects
   - `CreateCommitOnBranchInput.expectedHeadOid` is the expected branch-head object ID before the mutation.
4. Repository rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
5. Available rules: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
   - rulesets may restrict creations, updates, deletions, and force pushes, with configurable bypass actors.

These documentation claims are capability evidence, not proof that Everfield currently has an enforcing lock ruleset or that this credential is representative of ordinary agents.

## 4. Attempt lineage and observed results

| ID | Action | Immutable state / response | Result | Classification |
|---|---|---|---|---|
| A01 | Create deterministic task ref `planning/issue-70` at current main | `e4b7ee0a2699a57216146e99b990ab64edaae1d1` | created | observed |
| A02 | Create the same exact ref again | GitHub `422 Reference already exists` | duplicate rejected | observed PASS for sequential nonexistence gate |
| L01 | Create `planning/issue-70-exp-lease` at current main | `e4b7ee0a2699a57216146e99b990ab64edaae1d1` | created | observed |
| L02 | Create generation-0 commit from main tree | `b9b1409eaa3c82ee7acf301cc3616fbac599d035` | created | observed |
| L03 | Non-force update lease ref to L02 | ref -> `b9b1409...` | success | observed |
| L04 | Create stale-writer sibling from L02 | `04d5727e0e4d74c56dd6b61fa83122797794061d` | created | observed |
| L05 | Create recovery-owner sibling from L02 | `d346a57d4281fad028f2a1de4264dbdd864c1a5c` | created | observed |
| L06 | Non-force update lease ref to recovery sibling | ref -> `d346a57...` | success | observed |
| L07 | Stale writer tries non-force update to sibling L04 | GitHub `422 Update is not a fast forward` | stale write fenced | observed PASS for divergent stale-writer fence |
| R01 | List matching refs for `heads/planning/issue-70-exp` | lease ref resolves to `d346a57...` | current state reconstructed | observed PASS for pull-based reconciliation primitive |
| D01 | Contender surrogate A creates `planning/issue-70-exp-lock-a` | ref at `e4b7ee0...` | success | observed |
| D02 | Contender surrogate B creates `planning/issue-70-exp-lock-b` | ref at `e4b7ee0...` | success | observed |
| D03 | A attempts to acquire B's already-held exact ref | `422 Reference already exists` | blocked | observed |
| D04 | B attempts to acquire A's already-held exact ref | `422 Reference already exists` | blocked | observed |
| P01 | Enumerate repository rulesets | `[]` | no active repository ruleset observed | observed |
| P02 | Resolve current actor permission | `vokerg`: `admin` | ordinary-agent enforcement not tested | observed / limitation |
| S01 | Inspect prior W1 canonicalization task branch after squash-main advance | `planning/issue-43` still exists at `0084a63007c5f216b71771285d584cd2c6ebe009` | ref persisted | observed |
| S02 | Compare current main to surviving Issue 43 task ref | diverged; merge-base `e95f5e833a9713aa6aa8d5af9c69dc3cd37bcc66` | squash did not GC task ref | observed |

### Retained experimental refs

The following refs are deliberately retained as reconstructable experiment evidence because this execution surface does not expose ref deletion:

- `planning/issue-70-exp-lease` -> `d346a57d4281fad028f2a1de4264dbdd864c1a5c`
- `planning/issue-70-exp-lock-a` -> `e4b7ee0a2699a57216146e99b990ab64edaae1d1`
- `planning/issue-70-exp-lock-b` -> `e4b7ee0a2699a57216146e99b990ab64edaae1d1`

They are disposable/noncanonical evidence fixtures, not ownership authority.

## 5. Evidence versus inference

### Observed evidence

1. Exact duplicate ref creation is rejected in this repository for this credential.
2. A non-force ref update to a divergent sibling is rejected after another sibling has advanced the ref.
3. Matching-ref enumeration can reconstruct current ref state without consuming a prior event stream.
4. Independent acquisition of two lock refs can produce a partial-hold configuration in which each logical contender is blocked on the other's ref.
5. No repository rulesets were active when queried.
6. The current credential is admin.
7. A task branch can survive a squash integration and diverge from later `main`; cleanup is not implicit.

### Inferences, not proven facts

- Create-if-absent refs are a plausible primitive for a **single** conflict key, but sequential same-credential evidence is insufficient for a mature distributed claim protocol.
- Non-force fast-forward behavior is a useful fencing primitive, but a complete lease protocol still needs expiry semantics, authority over recovery, and independent actors.
- Matching-ref enumeration can support reconciliation after missed events, but webhook/event loss itself was not injected.
- Multi-ref locking requires a deterministic global ordering and bounded rollback/recovery if retained; the current experiment demonstrates the circular-wait risk rather than a fully concurrent deadlock implementation.

## 6. Alternatives and recommendation

### Alternative A — keep schema-3 only

Continue the canonical schema-3 ownership/status protocol as the sole authority. This is the **recommended current state** because it is already canonical and the mature lock/CAS evidence set is incomplete.

### Alternative B — one auxiliary ref per task/conflict key

Use a ref as an optimization/early contention signal while schema-3 remains authoritative. Advantages: strong observed duplicate-create behavior and readable reconciliation. Risks: permission/bypass, GC, expiry, and cross-actor semantics remain unproven.

### Alternative C — ordered multi-ref locks

Acquire conflict-key refs in one canonical total order, release/retire partial acquisitions on failure, and recover leaked generations with fenced ancestry. This directly addresses the D01-D04 circular-wait pattern, but it needs a real multi-credential experiment before adoption.

### Alternative D — one aggregate control-plane ref

Serialize a conflict-set/lease state into one CAS-updated branch/ref to avoid atomic multi-ref acquisition. This reduces multi-ref deadlock surface but introduces a hotspot and still needs expected-head, permissions, recovery, and GC evidence.

### Recommendation

**Do not promote mature GitHub lock/CAS in Wave 2 from this episode. Result: INCONCLUSIVE.** Preserve canonical schema-3 authority. Carry forward the positive ref primitives only as evidence for later experiments/design, never as independent ownership truth.

## 7. Dependencies and interfaces

- Canonical dispatcher/ownership authority: `docs/planning/PLANNING-PROGRAM-v1.md` and its inherited schema-3 protocol.
- Foundation constraint: `docs/planning/WAVE-1-FOUNDATIONS-v1.md` keeps mature GitHub lock/CAS `EVIDENCE_REQUIRED` while schema-3 remains usable authority.
- This artifact does not create a new hard prerequisite for other root missions.
- Declared downstream review is `W2-REV-01`.

## 8. Observability and evaluation

A future reviewer can reconstruct the core attempt lineage from repository Git objects/ref heads plus the exact SHAs above. A stronger retry should additionally retain:

- two or more credential/permission identities;
- server timestamps for acquire/renew/expiry/recover;
- exact request/response envelopes or workflow artifacts;
- webhook delivery IDs plus deliberate dropped/reordered delivery cases;
- active ruleset identity and bypass configuration;
- create/delete/restore lineage for GC;
- exact API version and capability fingerprint.

A mature adoption PASS must cover all required dimensions; one successful primitive may not aggregate into protocol PASS by itself.

## 9. Failure modes and risks

- admin or configured bypass defeats intended lock protection;
- unprotected ref namespace permits force/deletion outside the protocol;
- multiple locks acquired in inconsistent order deadlock or livelock;
- client clocks incorrectly decide lease expiry;
- stale recovery actor rewrites a newer generation;
- crash after partial acquisition leaks locks;
- garbage collection races a valid owner or deletes audit lineage;
- branch-name/prefix collisions create false ownership;
- API semantics/version or repository policy changes invalidate prior evidence;
- event-only reconciliation misses dropped deliveries;
- an auxiliary lock is accidentally treated as stronger authority than schema-3.

## 10. Unresolved questions and reopen conditions

Reopen the mature-lock decision when at least one of these becomes true:

1. two isolated credentials/actors with distinct permissions are available for concurrent race tests;
2. an active branch/tag ruleset can be installed on the experimental namespace and tested for ordinary actor plus explicit bypass behavior;
3. ref deletion is available so GC, stale-generation cleanup, restoration, and delete races can be exercised;
4. webhook/audit delivery can be injected, dropped, reordered, and reconciled;
5. a server-time lease/expiry harness can test delayed renewals, recovery, and stale-owner attempts;
6. GraphQL `createCommitOnBranch(expectedHeadOid)` can be executed against controlled branches and compared with REST non-force semantics;
7. GitHub materially changes ref/ruleset APIs or applicable repository policy.

## 11. Required independent critique

`W2-REV-01` must review the exact terminal work SHA and should specifically try to falsify:

- any implication that sequential duplicate-create proves concurrent atomic claiming;
- any implication that admin-context success proves ordinary-agent protection;
- the proposed ordering/rollback remedy for multi-ref circular wait;
- the distinction between event-independent reconciliation and actual event-loss testing;
- the retained-ref/GC limitation and cleanup safety;
- continued schema-3 primacy.

## 12. Downstream work unblocked

This mission contributes its exact evidence package to `W2-REV-01`. It authorizes no production work, no engine decision, no implementation-readiness transition, and no canonical replacement of schema-3.