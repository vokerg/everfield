# Handoff — Issue #1112 / FACTORY-CONVERGENCE-06-REM-01

## State

`REVIEW_READY` remediation candidate pending exact-head draft PR verification, fresh required-review materialization, and terminal schema-3 status.

This handoff records only bounded factory-liveness remediation provenance. It grants no review, verification-PASS, integration, implementation-readiness, engine-selection, release, decision, or canonical authority.

## Ownership and canonical basis

- issue: #1112 / `FACTORY-CONVERGENCE-06-REM-01`
- winning claim: comment `5659453690`
- actor: `frontier-drain-factory-conv06-rem1112-gpt56sol-20260914-01`
- branch: `planning/issue-1112`
- exact branch base: `main@98f0e66c1332f9a3ce47cf56ad352fab2223e8cd`
- canonical binding: Issue #6 comment `5245368879`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- owner convergence directive: Issue #84 comment `5277825639`
- later competing claim `5659455118` lost contention and was explicitly excluded by correction comment `5659456377`

## Frozen predecessor and review

Producer Issue #1108:
- winning claim `5659344391`
- terminal `5659405978`
- exact producer head `36afc975248e5fede3e1f5dc333041578674cc08`
- work SHA `21519f96055da88abb099219ded6f8fee3ca9f8e`
- draft PR #1109
- producer v3 blob `c1ae395df4222dfd307d75f09ae7ec466569ab29`
- producer v5 blob `86050867d2bf168a0bbd38bc2a292edf0eb1be34`

Required Review Issue #1110:
- winning claim `5659409017`
- terminal `5659450844`
- exact review head/work `5220308375070fa6b301c762a532b1cc4281238d`
- draft PR #1111
- disposition `CHANGES_NEEDED`
- findings: 0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR
- exact finding: `FACTORY-CONVERGENCE-06-REV-MAJ01`

Producer and review branches remain immutable judged provenance.

## Exact remediation

Owned mutable paths are exactly:
- `tools/planning/frontier_maintenance_v5.py`
- `docs/planning/handoffs/issue-1112.md`

The v5 file carries forward the frozen producer's v5 terminal-no-route generation-consumption implementation and adds one fail-closed ownership-supersession guard:

1. the shared v1 terminal parser still proves trusted owner linkage, immutable terminal shape, actor/mission binding, and terminal state;
2. v5 additionally enumerates trusted schema-3 ownership-generation records before the terminal;
3. the terminal's referenced `ownership_generation_comment_id` must equal the latest such prior ownership-generation record;
4. therefore owner A → later RESUME/RECOVER owner B → stale A no-route terminal cannot consume the exact factory source generation;
5. a current B-owned `DONE`/`SUPERSEDED` no-route terminal remains consumable.

Any later trusted ownership-generation record makes an older reference stale or ambiguous and therefore non-consuming. This is intentionally fail-closed; it does not invent authority for a malformed ownership chain.

The clean predecessor behavior is otherwise retained: exact source-generation identity, `DONE`/`SUPERSEDED` only, `INVALIDATED` rejection, trusted wrapper requirement, closed-wrapper requirement, actionable-route rejection, v4 semantic composition, same closed-transition comment pass, explicit successor handling, registered dispatch, recursion suppression, and typed GitHub-rate-limit deferral.

The predecessor's clean v3 `NONE` / `NONE_*` route classification remains frozen in Issue #1108 / PR #1109 and is not re-authored here because #1112 owns no v3 path.

## Deterministic regression coverage

The v5 self-test now includes both sides of the reviewed ownership race:

- initial owner A claim;
- trusted stale-recovery intent;
- later owner B `RECOVER`;
- stale A `SUPERSEDED` terminal with `NONE_SOURCE_ROUTE_ALREADY_CONSUMED` → must not consume;
- current B `SUPERSEDED` terminal linked to B's recovery generation → must consume.

The assertion also demonstrates that the shared v1 parser alone accepts the stale-A terminal, making the v5 guard's reviewed purpose explicit.

Existing producer assertions remain for `DONE`, `SUPERSEDED`, `INVALIDATED`, actionable route, untrusted wrapper, open wrapper, exact-generation reuse, and explicit-successor behavior.

## Validation and limitation

- exact source inspection of the modified helper and deterministic assertions: PASS
- targeted ownership-race decision matrix: PASS
- changed implementation surface: v5 only
- scope expansion outside declared owned paths: none

A repository checkout is not available in this execution environment, so no claim is made that the complete patched v1→v5 self-test chain executed here. Any later clean integration route must retain exact-new-main push-triggered v1→v5 workflow acceptance. Failure of that acceptance must route bounded remediation/rollback rather than DONE.

## Self-review

- unresolved BLOCKER: 0
- unresolved MAJOR: 0
- unresolved correction-requiring MINOR: 0
- authority inflation: none
- predecessor/review branch mutation: none

## Required next gate

After an exact-head draft PR exists, materialize exactly one fresh required degraded-independent review of this immutable two-path remediation packet.

That review must:
- bind the exact #1108 producer and #1110 review identities above;
- retest `FACTORY-CONVERGENCE-06-REV-MAJ01` with the stale-A/current-B ownership race;
- verify the frozen `NONE` / `NONE_*` predecessor behavior is preserved rather than broadened;
- verify no unrelated factory authority or API-pass behavior changed;
- preserve mandatory exact-new-main post-publication v1→v5 acceptance.

A clean review may only route a separate owner-authorized squash-only integration episode with that post-publication acceptance. It grants no higher planning authority by itself.

## Authority boundary

`NOT_CANONICAL`. Factory-liveness remediation only.
