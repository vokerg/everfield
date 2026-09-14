# Issue #1128 handoff — canonical program lease revision candidate

## Identity

- mission: `FACTORY-LEASE-CANON-REV-01`
- winning claim: `5659822962`
- branch: `planning/issue-1128`
- base: `main@51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- active canonical binding during production: Issue #6 comment `5245368879`
- active canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- active canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`

## Source governance and review

- reviewed governance producer: Issue #1124 / PR #1125
- producer terminal: `5659746316`
- producer exact head: `d5a04ee0bd7d3dab00c0de518c1c8b73aa01f024`
- producer candidate blob: `a59f04feb2c7e0344fdaab1fcbf4fa291e79a107`
- required governance review: Issue #1126
- review terminal: `5659773876`
- disposition: `PASS_FOR_CANONICAL_LEASE_SEMANTICS_REVISION`
- review report blob: `f7d2ec84570c6691931f1d3c9d6a6b6ee3e9face`

## Produced revision packet

- candidate: `docs/planning/12-planning-program-v1-lease-revision-candidate.md`
- manifest: `docs/planning/12-planning-program-v1-lease-revision-manifest.yaml`
- candidate state: `NOT_CANONICAL`

The packet is a narrow overlay over active canonical program blob `e3120ec203c4156328770aa86c12fbb7187966dc`. It adds only the reviewed temporal predicates: six-hour / 21,600-second task-owner lease as a new governance decision, GitHub-server `created_at` as sole clock, exact-boundary expiry, valid unexpired PROGRESS renewal, existing HEAD_ADVANCE and three-consecutive-EVIDENCE rules, no post-expiry resurrection, deterministic STALE/ORPHAN temporal eligibility, losing-contender rejection, owner-required handoff/terminal freshness, fail-closed malformed time, and prefix-scoped non-retroactive reconstruction.

Bootstrap-numbered work remains provenance-only in `CANONICAL_ACTIVE`; generic verification mechanisms are not broadened beyond declared tasks; inactive Stage-B coordination TTLs remain separate and inactive.

## Producer self-review

Self-review: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

Checks performed:
- candidate explicitly preserves all active canonical semantics outside the temporal overlay;
- six hours is explicitly labeled proposed/reviewed and not active canon;
- active program path and Issue #6 binding are untouched;
- maintenance and Stage-B implementation paths are untouched;
- manifest binds the active program, #1124 candidate, #1126 review, temporal constants, exact-boundary behavior, fail-closed requirements, adversarial verification scenarios, and post-verification canonicalization route;
- required verification PASS is forbidden with any BLOCKER, MAJOR, or correction-requiring MINOR;
- canonicalization remains a separate squash-only authority episode and a durable new binding is required before maintenance consumption.

## Required next route

`FRESH_REQUIRED_DEGRADED_INDEPENDENT_VERIFICATION_COMPATIBILITY_OF_EXACT_REVISION_PACKET`

Verification must bind the exact candidate/manifest blobs and then-current `main`, exercise the manifest scenarios, and verify no regression in the active canonical base. Any candidate/manifest byte change after verification requires a fresh full verification episode. A PASS may route a separately scoped canonicalization mission; it does not itself activate the lease semantics.

This producer grants no integration, verification-PASS, maintenance mutation, implementation-readiness, engine-selection, release, decision, or canonical authority.
