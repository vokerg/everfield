# Issue #1126 handoff — schema-3 ownership lease governance review

## Identity

- mission: `FACTORY-LEASE-SEMANTICS-REV-01`
- winning review claim: `5659749162`
- review branch: `planning/issue-1126`
- review base: `main@51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- trust mode: `DEGRADED_SINGLE_AGENT`
- active canonical binding during review: Issue #6 comment `5245368879`
- active canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`

## Immutable judged packet

- producer Issue #1124 terminal: `5659746316`
- producer PR: #1125, open/draft/mergeable at review
- exact producer head: `d5a04ee0bd7d3dab00c0de518c1c8b73aa01f024`
- candidate path/blob: `docs/planning/architecture/SCHEMA3-OWNERSHIP-LEASE-SEMANTICS-v1.md` / `a59f04feb2c7e0344fdaab1fcbf4fa291e79a107`
- producer handoff blob: `53163cd454e09b618377840176b082f586b034e0`
- changed paths: exactly candidate + producer handoff

## Review result

- report: `docs/planning/reviews/factory-lease-semantics-review.md`
- disposition: `PASS_FOR_CANONICAL_LEASE_SEMANTICS_REVISION`
- findings: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR / 2 INFO
- reviewed temporal semantics: six-hour / 21,600-second proposed owner lease; GitHub-server `created_at` only; exact-boundary expiry; PROGRESS renewal and three-EVIDENCE cap; no post-expiry self-renewal; STALE/ORPHAN maturity; losing-contender rejection; handoff/terminal current-owner requirement; prefix-scoped non-retroactive reconstruction
- historical provenance check: Issue #27 comment `5248796920` explicitly records a non-authoritative six-hour expectation, so the candidate's alignment claim is supported without promoting that audit note to canon

## Authority boundary and next route

This review is `NOT_CANONICAL` provenance only. It does not alter `PLANNING-PROGRAM-v1.md`, the Issue #6 binding, maintenance code, or integration authority.

Required next route: `SEPARATELY_SCOPED_CANONICAL_PROGRAM_AND_MANIFEST_LEASE_REVISION`.

That revision must preserve the reviewed semantics, then pass fresh verification/compatibility and separate canonicalization before any maintenance remediation may consume the lease predicate. The blocked factory finding `FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01` remains open until that canonical sequence completes and a fresh bounded maintenance remediation plus required review closes it.
