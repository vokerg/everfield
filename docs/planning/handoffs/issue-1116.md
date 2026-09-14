# Handoff — Issue #1116 / FACTORY-CONVERGENCE-06-REM-02

## State

Blocking remediation is **REVIEW_READY** pending one fresh required degraded-independent review.

This episode closes candidate finding `FACTORY-CONVERGENCE-06-REM-REV-MAJ01` in the bounded v5 ownership-consumption surface. It grants no review, integration, verification-PASS, implementation-readiness, engine-selection, release, decision, or canonical authority.

## Ownership and canonical basis

- winning claim: `5659575959`
- actor/session: `frontier-drain-factory-conv06-rem1116-gpt56sol-20260914-01`
- branch: `planning/issue-1116`
- branch base: `51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- current main observed before handoff write: `51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- canonical binding: Issue #6 comment `5245368879`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`

## Frozen predecessor chain

- producer #1108 terminal: `5659405978`
- producer PR #1109 head: `36afc975248e5fede3e1f5dc333041578674cc08`
- frozen clean v3 blob: `c1ae395df4222dfd307d75f09ae7ec466569ab29`
- Review #1110 terminal: `5659450844`, `CHANGES_NEEDED`
- remediation #1112 terminal: `5659505881`
- remediation PR #1113 head: `32e48e398bcabef437e9291fd9b33d15c2690aa8`
- predecessor remediated v5 blob: `b2e3eff7583fb8aad3567fbfe20b689224230905`
- Review #1114 terminal: `5659555729`, `CHANGES_NEEDED`
- exact finding: `FACTORY-CONVERGENCE-06-REM-REV-MAJ01`

## Remediation

Final v5 candidate blob before this handoff write: `477bc36ea788867cf2744f4f9b9ccfb161c875b6`.

The terminal no-route owner guard now reconstructs a winning schema-3 ownership chain instead of choosing the numerically latest ownership-kind comment. It preserves first-valid `CLAIM` ownership and permits `RESUME` / `RECOVER` supersession only when the grant binds the lowest winning `RESUME_INTENT`, the current generation, and the expected predecessor shape.

Consequently:

- a genuinely recovered owner B supersedes stale owner A, so stale A no-route terminal remains non-consuming;
- a later losing duplicate CLAIM after current owner B has zero authority effect;
- a later losing duplicate RECOVER whose intent/actor or predecessor does not win has zero authority effect;
- valid current owner B `DONE` / `SUPERSEDED` no-route terminal remains consumable;
- malformed linkage, `INVALIDATED`, open/untrusted wrappers, actionable routes, and exact-generation mismatch remain non-consuming.

The branch intentionally carries the coherent #1112 v5 candidate forward and modifies no path outside v5 plus this handoff.

## Deterministic coverage

The v5 self-test now contains both required ownership races:

1. owner A → winning STALE recovery B → stale A no-route terminal → **must not consume**;
2. winning/current B → later losing duplicate contender C → valid B no-route terminal → **must consume**.

The second attack is covered for both a losing duplicate `CLAIM` and a losing duplicate `RECOVER`.

Static source review against the canonical schema-3 manifest and #1114 finding is complete. A full patched v1→v5 execution PASS was **not** run or claimed in this environment. Exact-new-main push-triggered workflow acceptance remains mandatory after any later separately authorized coherent squash publication.

## Self-review

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- finding closure candidate: `FACTORY-CONVERGENCE-06-REM-REV-MAJ01`
- full patched v1→v5 execution PASS: **not claimed**
- integration authority: **false**
- canonicality: `NOT_CANONICAL`

## Required next route

One fresh required `DEGRADED_SINGLE_AGENT` review must judge the exact final head and the coherent frozen-v3/corrected-v5 composition before any integration. Any later clean integration must be squash-only and preserve mandatory exact-new-main push-triggered v1→v5 workflow acceptance.
