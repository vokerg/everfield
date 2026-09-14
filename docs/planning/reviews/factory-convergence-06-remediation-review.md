# Required Review — FACTORY-CONVERGENCE-06-REM-REV-01

## Disposition

**CHANGES_NEEDED**

Finding counts: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

This review is `DEGRADED_SINGLE_AGENT` and judges immutable remediation Issue #1112 / PR #1113 exact head `32e48e398bcabef437e9291fd9b33d15c2690aa8`. It does not mutate the producer or remediation branches and grants no integration or higher authority.

## Frozen packet

- producer Issue #1108 terminal: `5659405978`
- producer PR #1109 head: `36afc975248e5fede3e1f5dc333041578674cc08`
- frozen clean v3 blob: `c1ae395df4222dfd307d75f09ae7ec466569ab29`
- required Review #1110 terminal: `5659450844`
- predecessor disposition: `CHANGES_NEEDED`
- predecessor finding: `FACTORY-CONVERGENCE-06-REV-MAJ01`
- remediation Issue #1112 terminal: `5659505881`
- remediation PR #1113 head: `32e48e398bcabef437e9291fd9b33d15c2690aa8`
- remediated v5 blob: `b2e3eff7583fb8aad3567fbfe20b689224230905`
- remediation handoff blob: `602e77059b2afcd8638c3a552ac299f31a9de734`

## Material finding

### FACTORY-CONVERGENCE-06-REM-REV-MAJ01 — losing ownership contenders are incorrectly treated as current generations

The new v5 helper `terminal_owner_generation_is_current` enumerates every syntactically trusted schema-3 record whose kind is in `OWNERSHIP_KINDS`, then selects the highest comment ID before the terminal. That is not equivalent to the canonical current **valid/winning** ownership generation.

The canonical Planning Program explicitly states that a losing contention record has **zero authority effect** and that lowest valid GitHub comment ID wins ownership contention. Therefore a later losing duplicate `CLAIM`, `RESUME`, or `RECOVER` cannot supersede the real owner merely because its comment ID is larger.

A bounded counterexample is:

1. owner B is the valid winning/current ownership generation;
2. a later duplicate contender C posts a trusted but losing ownership-kind record;
3. owner B then publishes an otherwise valid owner-bound `DONE` or `SUPERSEDED` terminal with an exact no-route sentinel;
4. the shared terminal parser still accepts B's terminal because it correctly binds the terminal to B's referenced ownership record;
5. the new helper instead selects losing C as the numerically latest prior ownership-kind record and rejects B's valid terminal as non-current.

That false rejection leaves the exact factory-wrapper generation unresolved. A closed duplicate/not-planned wrapper can then remain eligible for exact-generation reuse/reopen, reintroducing the liveness loop that FACTORY-CONVERGENCE-06 is intended to eliminate.

This is not theoretical repository shape: duplicate claims with explicit loser correction are routine in this repository, including the #1112 chain itself. The remediation self-test covers a valid recovery generation B followed immediately by B's terminal, but does not insert a losing ownership contender between the winning generation and the terminal.

## Required correction

The v5 terminal-no-route consumer must compare the terminal's referenced ownership generation with the current **valid/winning** schema-3 ownership generation, not the highest syntactically parseable ownership-kind comment.

A bounded correction must:

- ignore ownership records with zero authority effect, including losing contention records;
- preserve rejection of a genuinely superseded prior owner after valid `RESUME`/`RECOVER`;
- preserve consumption of a current valid owner-bound `DONE`/`SUPERSEDED` no-route terminal even when a later losing duplicate contender exists before that terminal;
- add deterministic coverage for winning owner B → losing duplicate contender C → valid B no-route terminal → **consume**;
- keep malformed linkage, `INVALIDATED`, open/untrusted wrappers, actionable routes, and exact-generation mismatch non-consuming;
- retain frozen v3 `NONE`/`NONE_*` classification, v4 semantic composition, explicit-successor handling, recursion/registered-dispatch gates, stale-generation checks, and typed GitHub rate-limit deferral unchanged.

If proving winning/current ownership requires a helper outside the currently bounded v5 surface, route explicit scope revision rather than silently broadening the remediation.

## Other required attacks

The following static attacks are clean on the reviewed coherent composition:

- stale prior-owner terminal after a later valid recovery generation: rejected;
- current recovered owner terminal with no intervening losing contender: consumable;
- `DONE`/`SUPERSEDED` only; `INVALIDATED` remains non-consuming;
- actionable terminal route remains non-consuming;
- open or untrusted wrapper remains non-consuming;
- exact source-generation tuple remains the consumed unit;
- frozen v3 classifier treats exactly `NONE` and `NONE_*` as non-actionable while `NONEISH` and `SOME_NONE_ROUTE` remain actionable;
- v4 semantic resolution remains composed through one closed-transition comment fetch;
- typed GitHub rate-limit deferral remains present and generic forbidden responses remain fatal;
- PR #1113 changes only v5 plus the #1112 handoff;
- no review, verification-PASS, readiness, engine-selection, release, decision, integration, or canonical authority is created.

## Execution limitation

No full patched v1→v5 execution PASS is claimed. In particular, PR #1113 by itself does not contain the frozen v3 classifier change; any eventual clean integration must publish the reviewed v3 semantics and corrected v5 semantics coherently, then require exact-new-main push-triggered v1→v5 workflow acceptance.

## Authority boundary

`NOT_CANONICAL`. Required review provenance only. This review blocks integration of the current remediation packet and routes one bounded successor remediation for `FACTORY-CONVERGENCE-06-REM-REV-MAJ01`.
