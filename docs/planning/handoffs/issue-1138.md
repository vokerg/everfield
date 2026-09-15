# Issue #1138 handoff — remediated lease canonical revision verification

## Identity

- mission: `FACTORY-LEASE-CANON-VERIFY-02`
- winning claim: `5674945897`
- branch: `planning/issue-1138`
- verified base: `main@8468daf824aee6e5ef48ffead0918a5512bd4b0c`
- trust mode: `DEGRADED_SINGLE_AGENT`
- producer: Issue #1137 terminal `5668329071`, PR #1139, head `e0f87494eea335ff195ace746689b486bc40909d`
- candidate blob: `2d98f95c58d15bddf7c00be3fd5905aa8ca501e5`
- manifest blob: `d075d7bd92e1c7636ab77a962a677c521c9db7b5`
- active canonical program: `e3120ec203c4156328770aa86c12fbb7187966dc`
- active binding: Issue #6 comment `5245368879`

## Result

Verification result: **PASS**.

Disposition: `PASS_FOR_SEPARATE_CANONICALIZATION`.

Findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

The fresh full suite re-passed all temporal and canonical-compatibility attacks from failed verification #1134. The remediation is bounded: after expected remediation header normalization, Sections 1–12 preserve the prior candidate bytes, while new Section 13 and manifest v2 fully specify deterministic promotion.

The former MAJOR `FACTORY-LEASE-CANON-VERIFY-MAJ01` is closed. Independently applying the manifest's exactly four replacements with test canonicalization issue `999999` produces Git blob `94561b26a7553f02c64da87f528f5d37b914a7e5`, exactly matching the producer dry-run. Missing/duplicate literals, invalid issue-number encodings, wrong payload identities, and undeclared byte drift fail closed.

## Required next route

Only a separately scoped canonicalization episode may consume this PASS. Its contract must bind the exact candidate blob, manifest blob, verified base, and this verification result before applying the transform; it must use expected-head/base checks, squash-only publication, and publish terminal schema-3 `INTEGRATION_STATUS` on that same canonicalization issue with the durable new binding.

Any candidate or manifest byte change requires a fresh full verification.

## Authority

`NOT_CANONICAL`. This verification grants no integration, maintenance implementation, implementation-readiness, engine-selection, release, production, decision, or canonical authority. The Issue #6 binding remains active until a separately authorized canonicalization completes.
