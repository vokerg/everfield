# W1-REC-02 — Post-Wave-2 planning liveness recovery

## Scope and authority

This is a bounded `recovery_episode_v1` for Issue #333. It does not create gameplay/high-throughput implementation, engine-selection, provider/legal/platform, release, verification-PASS, readiness, integration, or canonical authority.

Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`.
Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.
Recovery claim: Issue #333 comment `5301195807`.
Frozen recovery base: `main@597b72b73d5a1e06f38c29edc38994e355694189`.

## Fresh graph snapshot

At recovery acquisition:

- GitHub reported zero open pull requests.
- The newest open `[PLAN-v1]` records are terminal/integrated records, not unowned READY producer work.
- Issue #237 / `W2-READY-04` already verified the `W2-READY-M03` synthesis correction `PASS`; its verification provenance was separately squash-integrated. Re-running #232/#234/#237 would duplicate terminal work.
- Issue #82 / `W2-ENG-03` terminalized at exact head `1575cb3a18c9c7be1776b64c9ec92cc8990a97e0` with `INCONCLUSIVE_ENVIRONMENT_BLOCKED`, 50/50 candidate × S1-S10 cells `NOT_RUN`, and zero engine processes executed. Exact terminal evidence was later squash-integrated through PR #123 as noncanonical provenance. No engine was selected.
- Formal review finding `W2-REV-M01` therefore remains `OPEN_BOUNDED`: later authority requires equivalent real-toolchain execution while retaining the failed/inconclusive episode.
- The corrected accessibility mapping chain completed required mapping review through Issue #329. Issue #331 / `W2-EV-ACC-01` then terminalized `EVIDENCE_INCOMPLETE / NO_CONCRETE_EXECUTABLE_OR_BUILD_ARTIFACT_AVAILABLE`; its exact bounded evidence-availability packet is the current-main squash commit `597b72b73d5a1e06f38c29edc38994e355694189`.
- `W2-REV-M02`, `IR-BLOCKER-ACCESSIBILITY-CURRENT`, empirical accessibility evidence, and `mapping_complete` remain fail-closed because there is no concrete executable/build target. The PLANNING phase does not authorize manufacturing a gameplay build merely to satisfy this evidence gate.
- Formal review finding `W2-REV-M03` remains `OPEN_BOUNDED`: provider-independent protected-evidence/evaluator/CI contracts exist, but provider-specific production-control evidence is unproven.
- The rights remediation lineage reached a clean deterministic review input (Issue #162, clean review #172) but explicitly grants no legal clearance, provider permission, release, or readiness authority.
- Platform/product-scope planning evidence remains planning evidence rather than a release commitment/certification authority.
- The current readiness ledger is still a `W2-SYN-REM-03` candidate lineage. It predates the late accessibility mapping/evidence terminal chain and therefore cannot by itself serve as a current dispatcher frontier index.

## Failure classification

Primary liveness defect: `MISSING_POST_TERMINAL_CONVERGENCE_TRANSITION`.

Secondary dispatcher defect: `TERMINAL_OPEN_RECORDS_CONFUSED_WITH_RUNNABLE_FRONTIER`.

The graph is not blocked by an open merge queue, stale producer PR, unresolved `W2-READY-M03`, or reusable W1-REC-01 episode. It is stranded because several evidence lines terminated honestly on external capability/authority predicates, while no later bounded convergence transition recompiles those results into a current frontier/readiness state.

## Blocker classification

| Surface | Current state | Recovery classification | Exact trigger for stronger state |
|---|---|---|---|
| Engine / `W2-REV-M01` | 50 comparative cells `NOT_RUN`; terminal/integrated inconclusive evidence | `EXTERNAL_TRIGGER_REQUIRED` | repository-visible environment/toolchains capable of equivalent admitted-engine S1-S10 execution, followed by required evidence/review route |
| Accessibility / `W2-REV-M02` | mapping review complete; empirical evidence `NOT_RUN`; target build unbound | `EXTERNAL_TRIGGER_REQUIRED` | concrete reproducible executable/build identity plus required environment/AT coverage, followed by empirical evidence/review route |
| Evidence foundation / `W2-REV-M03` | provider-independent contracts retained; provider production controls unproven | `AUTHORITY_REQUIRED` / `EXTERNAL_TRIGGER_REQUIRED` | selected/bound production provider and provider-specific credentials/control/audit evidence sufficient for the declared empirical route |
| Rights | deterministic planning/review input exists; no legal/provider permission authority | `AUTHORITY_REQUIRED` | actual scoped legal clearance/provider permission when a production/release decision requires it |
| Platform | planning recommendation/scope evidence only | `AUTHORITY_REQUIRED` at commitment boundary | separately authorized platform/release commitment or certification evidence as applicable |
| Readiness synthesis | latest ledger predates later terminal evidence lines | `INVALID/MISSING_TRANSITION` | bounded convergence synthesis that consumes immutable latest terminal/integration identities and republishes current fail-closed frontier/readiness state |

No recovery action may convert an external trigger into repository-local PASS.

## Dispatcher correction

For frontier derivation, GitHub `state=open` is only an index candidate. An open issue is not runnable when a valid terminal/result record already fixes its episode and any required publication/integration is complete. Such an issue becomes runnable again only through an explicit protocol-valid restart/recovery/reopen transition whose predicate is presently satisfied.

In particular, Issues #82, #232, #234, #237, #329, and #331 must not be repeatedly selected merely because issue closure state lags lifecycle state.

## Smallest lawful continuation

No existing unintegrated review/verification/remediation/producer packet was found that can autonomously resolve the current no-READY state. The smallest missing transition is one bounded **post-Wave-2 convergence synthesis/readiness refresh**.

That successor must:

1. consume exact immutable latest terminal/integration identities rather than replay producer work;
2. update the current frontier/readiness representation to distinguish `EXTERNAL_TRIGGER_REQUIRED`, `AUTHORITY_REQUIRED`, and internally actionable work;
3. preserve `W2-REV-M01`, `W2-REV-M02`, and `W2-REV-M03` as OPEN unless their exact predicates are empirically satisfied;
4. preserve false for production implementation/readiness, engine selection, empirical accessibility PASS, legal/provider permission, release, verification-PASS, and canonicality;
5. publish explicit reopen triggers for the external-blocked lines;
6. route one fresh readiness verification of the exact convergence candidate;
7. create no gameplay implementation backlog and no substitute evidence.

Recommended mission identity: `W2-SYN-CONV-01`.

The successor is synthesis/convergence only. It does not itself solve external evidence/authority blockers; it restores a truthful runnable planning frontier and prevents dispatch loops.

## Reopen / invalidation conditions

Invalidate this recovery diagnosis if, before successor claim, any of the following becomes durable repository state:

- a valid active owner or eligible existing terminal integration appears and outranks synthesis;
- a concrete executable/build target appears for accessibility;
- a capable real-toolchain engine execution environment appears;
- provider-specific production-control evidence/authority becomes available;
- a later valid terminal/integration record supersedes any identity relied upon here;
- current `main` changes in a way that creates a higher-priority existing continuation.

In that case re-derive the frontier; do not blindly execute the synthesis successor.

## Result

`RECOVERY_PATH_IDENTIFIED`.

One missing bounded planning transition is identified: post-terminal Wave-2 convergence synthesis plus fresh readiness verification. External evidence/authority gates remain fail-closed. No gate is waived and no implementation authority is created.
