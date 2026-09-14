# Required governance review — schema-3 ownership lease semantics

**Review issue:** #1126 / `FACTORY-LEASE-SEMANTICS-REV-01`  
**Judged producer:** #1124 / PR #1125  
**Trust mode:** `DEGRADED_SINGLE_AGENT`  
**Candidate head:** `d5a04ee0bd7d3dab00c0de518c1c8b73aa01f024`  
**Candidate blob:** `a59f04feb2c7e0344fdaab1fcbf4fa291e79a107`  
**Candidate handoff blob:** `53163cd454e09b618377840176b082f586b034e0`  
**Active canonical binding during review:** Issue #6 comment `5245368879`, Planning Program blob `e3120ec203c4156328770aa86c12fbb7187966dc`.

## Disposition

`PASS_FOR_CANONICAL_LEASE_SEMANTICS_REVISION`

Findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR / 2 INFO**.

This PASS is review provenance only. It does not make the candidate canonical, does not modify the active binding, and does not authorize maintenance implementation or integration. The next gate is a separately scoped canonical-program/manifest revision followed by fresh verification/compatibility and separate canonicalization.

## Frozen packet and scope

PR #1125 is open, draft, mergeable, and remains exactly at head `d5a04ee0bd7d3dab00c0de518c1c8b73aa01f024`. Its changed paths are exactly:

- `docs/planning/architecture/SCHEMA3-OWNERSHIP-LEASE-SEMANTICS-v1.md`;
- `docs/planning/handoffs/issue-1124.md`.

No active canonical program, maintenance implementation, predecessor branch, or Stage-B protocol path is changed by the judged packet.

## Adversarial review results

1. **Proposed value vs existing canon — PASS.** The candidate labels six hours / 21,600 seconds as a new governance proposal, not an existing canonical rule. Historical Issue #27 comment `5248796920` explicitly described a six-hour lease expectation as non-authoritative; the candidate uses that only as behavioral provenance and retains the full review/verification/canonicalization sequence.
2. **Choice narrowness — PASS.** The proposal changes only the missing task-owner lease predicate and preserves the existing state-machine, contention, renewal, handoff, terminal, review, verification, and squash-only authority gates.
3. **Authoritative clock — PASS.** GitHub API comment `created_at` is the sole lease clock. Body timestamps, commit/local/workflow clocks, and `updated_at` have zero lease authority. Missing, malformed, null, or timezone-naive required timestamps fail closed and cannot manufacture staleness.
4. **Generation anchor and exact boundary — PASS.** A valid winning owner-generation record anchors at its authoritative `created_at`; live is `t < anchor + 21600s`; expired is `t >= anchor + 21600s`. Exact-boundary recovery is therefore mechanically decidable.
5. **PROGRESS renewal — PASS.** Renewal applies only to the current unexpired generation and preserves existing HEAD_ADVANCE validity/reset semantics. EVIDENCE renewals are capped at three consecutive valid records; the fourth is invalid and cannot move the anchor.
6. **No resurrection — PASS.** PROGRESS at or after expiry cannot self-renew an expired generation.
7. **STALE recovery — PASS.** Premature STALE intent/recovery has zero authority. At/after the boundary, existing source/head/current-generation/winning-intent/first-valid-grant predicates remain mandatory, and intervening valid renewal/status/owner transitions invalidate the stale route.
8. **ORPHAN recovery — PASS.** Existing ten-minute GitHub-server maturity is preserved; exact boundary is mature; later valid ownership invalidates the orphan route; structural/winning-intent/head/first-valid-grant constraints remain intact.
9. **Losing contenders and non-retroactivity — PASS.** Losing duplicate CLAIM/RESUME/RECOVER records cannot supersede the winning owner. Later recovery does not retroactively invalidate a terminal that was authoritative when created, while a stale prior-owner terminal after valid recovery remains invalid.
10. **HANDOFF and terminal authority — PASS.** HANDOFF_READY and owner-required terminal records must be created while the current generation is unexpired. Valid pre-expiry handoff continues through the existing HANDOFF intent/RESUME route; STALE is not substituted.
11. **Bootstrap / verification scope — PASS.** Historical bootstrap-numbered work remains provenance-only. `BOOTSTRAP_RESUME`, `VERIFICATION_RESTART`, `VERIFICATION_REFRESH`, or later ownership kinds are covered only where a canonical task contract already permits/declares them; the candidate does not create generic new activation authority.
12. **Stage-B separation — PASS.** Inactive IntegrationUnit/global coordination TTLs are explicitly separate and remain inactive; they are not substituted for schema-3 task ownership.
13. **Path confinement — PASS.** PR #1125 changes exactly the candidate and handoff paths. It does not edit `PLANNING-PROGRAM-v1.md`, maintenance code, or predecessor branches.
14. **Authority sequence — PASS.** The candidate requires clean review -> separately scoped canonical-program/manifest revision -> fresh verification/compatibility -> separately authorized squash-only canonicalization -> fresh bounded maintenance remediation -> fresh required remediation review. PR/review/mergeability state is never treated as canonicality or integration authority.

## Informational observations

- **INFO-01 — six-hour provenance is historical, not normative.** Issue #27 comment `5248796920` is useful evidence that six hours matches prior repository expectations, but it was explicitly non-authoritative and was later subject to a project-owner continuation directive. The candidate correctly treats six hours as a new governance decision; canonical revision/verification must continue to do so.
- **INFO-02 — consumer implementation must evaluate time relative to each operational comment.** The candidate correctly states that ownership reconstruction at terminal/comment X uses only records available through X. The future maintenance remediation should preserve this prefix-scoped evaluation and deterministic exact-boundary tests rather than using wall-clock “now” as a substitute.

## Required next route

`SEPARATELY_SCOPED_CANONICAL_PROGRAM_AND_MANIFEST_LEASE_REVISION`

The revision must incorporate the reviewed semantics without weakening existing schema-3 rules and must itself proceed through fresh verification/compatibility and separate canonicalization. This review grants no maintenance mutation, integration, verification-PASS, implementation-readiness, engine-selection, release, decision, or canonical authority.
