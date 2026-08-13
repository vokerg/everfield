# Issue #176 handoff — ARCH-CONVERGENCE-REV-03

## Episode identity

- mission: `ARCH-CONVERGENCE-REV-03`
- issue: #176
- branch: `planning/issue-176`
- actor/session: `arch-convergence-rev-03-gpt56sol-20260813-1442-run`
- winning ownership claim: `5280548190`
- claim/base main: `9b84a565111428616856e5fd15b48a4760d64d20`
- trust mode: `DEGRADED_SINGLE_AGENT_FRESH_REVIEW_EPISODE`
- reviewed issue: #174 / `ARCH-CONVERGENCE-REM-03`
- reviewed exact head/work: `dba063d20d63d74402f01e58c6a96bfd54909aa0`
- reviewed candidate blob: `4c9543671f2d650ee1c45797d1eee3c1cd3145e0`
- reviewed PR: #175, open/draft/exact-head at review time
- predecessor review: Issue #167 head `10d1648ebbabcfec76b22778903ffa23d82c3686`, review blob `552b0ef5ba4d8461c4b4236090b9e6408a391f07`
- review artifact: `docs/planning/reviews/arch-convergence-03-review.md`
- review artifact blob after substantive review commit: `56a3a07a0265ee8ea2e07cd7786197ce6d3b2813`
- substantive review commit: `abf30009af5254f49c31fabe367861db1f896356`

## Disposition

`PASS_FOR_CANONICAL_REVISION`

Findings: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

The fresh review independently reconstructs Revision 3 and closes both routed Issue #167 findings:

- `ARCH-REV2-M01`: closed by making IntegrationUnit/global comment generations coordination/recovery records only and using an exact expected-old server ref transaction as the sole `main` mutation arbiter;
- `ARCH-REV2-M02`: closed by making immutable terminal `H` the sole source packet authority after terminalization and treating the live PR as provenance/UI bookkeeping only.

## Key attack results

- concurrent same-base publishers: exact-old transaction permits at most one `main` mutation;
- forward, rewind, delete/recreate, or unrelated ref replacement: every `current_main != A` case must fail before mutation;
- stale owner plus recovered owner: coordination can overlap without split-brain mutation authority;
- divergent live PR head: cannot alter exact frozen `H` packet or make later commits appear integrated;
- ambiguous successful ref update: exact known `S` / IntegrationUnit marker is checked before any retry, preventing duplicate publication;
- PR close/linkage failure after publication: typed continuation, no republish;
- relevant path/dependency/policy drift: fails closed; provably disjoint churn may remain compatible;
- negative review provenance: `acceptance_authority: NONE`; no recursive review-of-review;
- producer self-review: never independent acceptance;
- aggregate review, verification, canonicalization, readiness, historical evidence, PolicyEpoch, and implementation barriers remain separate;
- integration of this candidate/review alone cannot activate Stage-B semantics.

## Concrete-publication capability boundary

The review does **not** assume that current GitHub REST merge/ref APIs provide the required safety primitive. Revision 3 explicitly forbids generic non-force ref updates and ordinary merge/squash endpoints as fallback when they lack caller-bound expected-old semantics.

A later canonical Stage-B schema/PolicyEpoch revision must name the concrete native/server API providing exact `expected_old=A`, prove repository permissions can use it without bypassing required branch policy, bind typed records/control surfaces/epoch semantics, migrate old units fail-closed, and verify the normative simulations before activation. Failure to prove that capability leaves publication blocked.

## Required next route

This review permits only the next architecture authority step: a **separately scoped canonical protocol/schema/PolicyEpoch revision plus migration/verification route** may become eligible under the live repository frontier.

Do not infer from this PASS:

- direct integration authorization for Issue #174 / PR #175;
- workflow activation;
- canonicality;
- verification completion;
- implementation readiness or production authority;
- release/legal/provider/engine authority;
- permission to bypass aggregate review, verification, branch policy, or squash-only integration.

Any eventual `main` integration remains separately authorized and squash-only.

## Terminalization checklist

Before publishing terminal schema-3 `STATUS(REVIEW_READY)` for Issue #176:

1. keep the reviewed candidate immutable at exact `dba063d20d63d74402f01e58c6a96bfd54909aa0`;
2. open a draft PR from exact `planning/issue-176` head to `main`;
3. verify PR head equals the final review task `head_sha`;
4. record final review/handoff blobs and exact PR identity in the terminal status.
