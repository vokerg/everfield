# Issue #1137 handoff — deterministic lease-revision promotion remediation

## Identity

- mission: `FACTORY-LEASE-CANON-REV-REM-01`
- winning claim: `5660301524`
- branch: `planning/issue-1137`
- base: `main@51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- source failed verification: Issue #1134 terminal `5660250078`
- source finding: `FACTORY-LEASE-CANON-VERIFY-MAJ01`
- immutable source producer: Issue #1128 / PR #1130 head `cccf9b32764ff4c7fdaf9bc8b0a19ce1da7ebc8a`
- source candidate blob: `fe2c832f4da5971956b7f83ce651fd3f1586dabe`
- source manifest blob: `55909cb6400584e9238bf149da09bb406ec3dc93`

## Corrected packet

- candidate: `docs/planning/12-planning-program-v1-lease-revision-candidate.md`
- corrected candidate blob: `2d98f95c58d15bddf7c00be3fd5905aa8ca501e5`
- manifest: `docs/planning/12-planning-program-v1-lease-revision-manifest.yaml`
- corrected manifest blob: `d075d7bd92e1c7636ab77a962a677c521c9db7b5`
- canonicality: `NOT_CANONICAL`

The correction changes only promotion specification/provenance. The six-hour lease semantics, GitHub-server `created_at` clock, exact boundary, PROGRESS/EVIDENCE rules, STALE/ORPHAN predicates, contention, prefix-scoped reconstruction, CANONICAL_ACTIVE guard, Stage-B separation, active-base preservation, and authority barriers are unchanged in substance.

## Mechanical promotion closure

The corrected manifest now binds the candidate blob and defines destination `docs/planning/PLANNING-PROGRAM-v1.md` plus exactly four deterministic header replacements. Its single runtime parameter is the positive base-10 issue number of a separately authorized canonicalization episode. That parameter is provenance-only and may appear only in the declared `Canonicalized by: Issue #N` output header. The canonicalization issue contract must bind this exact verified candidate, exact verified manifest identity, and verified base; its terminal `INTEGRATION_STATUS` must be on that same issue.

All undeclared byte changes fail closed. Any candidate or manifest byte change after verification requires a fresh full verification episode.

Producer dry-run:
- test canonicalization issue number: `999999`
- replacement counts: `[1,1,1,1]`
- simulated promoted blob: `94561b26a7553f02c64da87f528f5d37b914a7e5`
- candidate remainder from the active-base provenance line onward: byte-identical

Self-review: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

## Required next route

Fresh required degraded-independent full verification: Issue #1138 / `FACTORY-LEASE-CANON-VERIFY-02`.

That verifier must re-run the full temporal/canonical compatibility suite and independently validate the parameterized promotion transform. A PASS may route separately scoped canonicalization; it does not itself change the active binding.

## Authority

`NOT_CANONICAL`. No integration, maintenance implementation, verification-PASS, implementation-readiness, engine-selection, release, decision, production, or canonical authority. The active Issue #6 binding remains unchanged.
