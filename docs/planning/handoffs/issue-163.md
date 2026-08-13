# Issue #163 handoff — ARCH-CONVERGENCE-REM-02

## Episode identity

- mission: `ARCH-CONVERGENCE-REM-02`
- issue: #163
- branch: `planning/issue-163`
- actor/session: `arch-convergence-rem-02-gpt56sol-20260813-1405`
- winning ownership claim: `5280287906`
- claim/base main: `6cdadcc77cbc386168da586154de85e5dedf63f1`
- immutable predecessor candidate: Issue #154 head `57a941f98a00f0c49b29148e2d60b6febe7fb788`, blob `d04174e22a0bb2b45de622778c0b97a53106e8df`
- independent review input: Issue #152 terminal status `5280237142`, review head `1bbea3e446f2b6451c8eac87c9df37e04466ec80`, review blob `5eb6e513befc2706f830f91f6789b86a0041ff9b`
- routed findings: `ARCH-REV-M01`, `ARCH-REV-M02`
- revised candidate path: `docs/planning/architecture/FRONTIER-CONVERGENCE-AMENDMENT-v1.md`
- revised candidate blob before this handoff commit: `42e130f4c0faf4db181b26d9f7e3ae86e270f6f7`

## Corrections completed

### ARCH-REV-M01 — expected-base publication

The candidate no longer relies on an advisory lease plus a post-merge parent assertion. It now requires one deterministic one-parent squash commit `S(parent=A)` constructed from exact source head `H` after compatibility is checked against exact `main=A`, followed only by a non-force `refs/heads/main -> S` update or another server-enforced primitive with the same expected-base safety property.

If an external actor advances `main` from A to B before publication, S is not a descendant of B and the non-force update must reject before changing `main`. `force=true` and fallback to a normal PR merge endpoint lacking expected-base/CAS semantics are forbidden. Branch-protection/permission rejection is typed `PUBLICATION_BLOCKED` and performs zero source-packet mutation on main.

After exact `main == S` confirmation, source PR linkage/closure is separate bookkeeping. A post-publication PR-close failure becomes `MAIN_PUBLISHED_PR_CLOSE_PENDING` and is continued without republishing S.

### ARCH-REV-M02 — one discoverable authority ledger and typed recovery

The active PolicyEpoch must bind exactly one `integration_control_issue`. That issue is the sole global `MAIN_INTEGRATION_LEASE` ledger; every actor discovers it through active canonical binding -> active PolicyEpoch and folds the same comment stream.

The singleton lease key is `repo:vokerg/everfield:refs/heads/main`. Global claims and recovery use GitHub server `created_at` plus PolicyEpoch-fixed TTL, exact generation/predecessor references, lowest-valid-comment-ID contention, mandatory immediate winner recheck, typed stale recovery/supersession, and release/abandon/commit terminals.

The separate IntegrationUnit namespace now has its own explicit server-time claim/recovery state machine on the source issue, rather than delegating stale behavior to ordinary task-ownership principles. Recovery never reopens source task ownership and never grants source-branch mutation authority.

## Preserved architecture

Revision 2 retains all Issue #152-confirmed strengths:

- scoped noncanonical storage cannot bypass governing independent review;
- aggregate cross-domain review remains mandatory for the decisions/readiness scopes that declare it and is not a universal storage gate;
- `IntegrationUnit` remains separately claimable without per-merge issue creation;
- unrelated disjoint main churn can be compatible without review storms while relevant policy/path/dependency/control-surface drift fails closed;
- terminal negative/positive review provenance can drain with `acceptance_authority: NONE` and no recursive review-of-review;
- producer self-review can never satisfy independent scoped acceptance;
- PolicyEpoch migration cannot rewrite historical evidence/trust states;
- noncanonical integration cannot satisfy canonical/readiness/production prerequisites;
- bounded review/remediation recursion and convergence-first dispatcher ordering remain intact;
- every eventual main integration remains one squash commit only.

## Producer adversarial self-review

The candidate specifies normative simulations:

1. two unrelated IntegrationUnits contending for the singleton global lease;
2. stale global lease recovery with two concurrent recoverers;
3. stale IntegrationUnit owner recovery without task reopening;
4. external main advance after final compatibility check;
5. source PR head movement after IntegrationUnit derivation;
6. disjoint versus relevant main churn;
7. publication primitive unavailable because of protection/permission;
8. PR linkage/closure failure after successful main publication.

Observed architectural disposition in bounded self-review:

- unresolved BLOCKER: 0
- unresolved MAJOR: 0
- correction-requiring MINOR: 0
- `ARCH-REV-M01`: `RESOLVED` in candidate design
- `ARCH-REV-M02`: `RESOLVED` in candidate design
- prior `ARCH-SR-M01` through `ARCH-SR-M04`: remain closed

The safety proof does not rely on protocol actors respecting the global lease: the expected-base non-force publication rule independently prevents an external `main` race from landing the source packet on an unchecked base.

## Remaining required route

This packet is still `NONCANONICAL_ARCHITECTURE_CANDIDATE_REVISION_2`. One fresh independently owned architecture review is mandatory; the Issue #152 reviewer episode must not adjudicate its own routed remediation.

Only after a clean fresh architecture review may a separately scoped canonical schema/PolicyEpoch revision and migration become eligible. That later Stage-B work must bind the exact global control issue, lease TTLs, typed records, compatibility migration, and permitted expected-base publication primitive. Nothing in Issue #163 activates those mechanisms directly.

## Authority boundary

No workflow activation, integration permission, canonicality, verification, readiness, production, implementation, engine selection, release, legal/provider, or merge authority is created. The required exact-head draft PR is review/provenance visibility only. Every eventual main integration remains separately authorized and squash-only.