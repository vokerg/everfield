# Issue #1124 handoff — schema-3 ownership lease governance candidate

## Identity

- mission: `FACTORY-LEASE-SEMANTICS-01`
- winning ownership claim: `5659680708`
- later duplicate claim `5659680818`: non-winning by lowest-valid-comment-ID contention
- producer base: `main@51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- active canonical binding during production: Issue #6 comment `5245368879`
- active canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- source scope invalidation: Issue #1122 terminal `5659675428`
- blocked review finding: `FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01`

## Produced candidate

- path: `docs/planning/architecture/SCHEMA3-OWNERSHIP-LEASE-SEMANTICS-v1.md`
- candidate commit: `442942ed62417b6a4236354896b490efb94c24c5`
- candidate blob: `a59f04feb2c7e0344fdaab1fcbf4fa291e79a107`
- visibility PR: #1125, draft
- candidate state: `NONCANONICAL_GOVERNANCE_CANDIDATE`

The candidate makes the previously missing task-ownership expiry predicate explicit:

- schema-3 task-owner lease: 21,600 seconds / six hours;
- the six-hour value is a new reviewable governance decision aligned with historical repository provenance, not a claim that the current canonical machine contract already contains that duration;
- lease clock: GitHub server comment `created_at` only;
- generation anchor: winning ownership grant `created_at`;
- valid PROGRESS renews the same generation from its own `created_at`;
- exact expiry boundary is stale: `t >= anchor + 21,600s`;
- the existing maximum of three consecutive valid EVIDENCE renewals without HEAD_ADVANCE remains in force; a fourth EVIDENCE record is invalid and cannot move the lease anchor;
- an expired generation cannot self-renew;
- STALE intent/recovery must prove expiry plus the existing source/head/current-generation/winning-intent/first-valid-grant rules;
- ORPHAN intent/recovery must prove the existing ten-minute server-time maturity boundary and absence of a later valid owner;
- malformed/missing authoritative timestamps fail closed and never manufacture staleness;
- valid HANDOFF/terminal records still require an unexpired current owner when their canonical kind requires owner authority;
- inactive Stage-B IntegrationUnit/global coordination TTLs remain separate and unchanged.

## Scope / non-authority

No maintenance implementation was changed. The active `PLANNING-PROGRAM-v1.md`, Issue #6 binding, bootstrap activation, Stage-B candidate, and all v1-v5 frontier-maintenance code remain untouched.

This packet does **not** authorize maintenance consumption, integration, verification PASS, canonicality, implementation readiness, engine selection, release, or application-domain decisions.

## Self-review

Producer self-review: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

Attacks covered in the candidate include premature STALE, exact-boundary STALE, renewed lease, fourth-EVIDENCE rejection, premature/exact-boundary ORPHAN, losing duplicate ownership contenders, and stale prior-owner terminal publication.

## Required next gates

1. fresh required degraded-independent governance review of this exact candidate/head;
2. if clean, a separately scoped canonical-program/manifest revision incorporating the reviewed lease predicate;
3. fresh verification of that revised canonical candidate and compatibility with active work;
4. separately authorized squash-only canonicalization publishing a new durable binding;
5. only then may a fresh bounded maintenance remediation re-derive `FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01`;
6. that remediation still requires fresh required review before any integration.

No gate may be skipped because PR #1125 is open, draft, mergeable, or otherwise mechanically ready.
