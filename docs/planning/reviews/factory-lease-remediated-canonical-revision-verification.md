# Verification — remediated schema-3 ownership lease canonical revision packet

**Verification issue:** #1138 / `FACTORY-LEASE-CANON-VERIFY-02`  
**Producer:** #1137 / PR #1139  
**Trust mode:** `DEGRADED_SINGLE_AGENT`  
**Verified base:** `main@8468daf824aee6e5ef48ffead0918a5512bd4b0c`  
**Producer head:** `e0f87494eea335ff195ace746689b486bc40909d`  
**Candidate blob:** `2d98f95c58d15bddf7c00be3fd5905aa8ca501e5`  
**Manifest blob:** `d075d7bd92e1c7636ab77a962a677c521c9db7b5`  
**Active canonical program blob:** `e3120ec203c4156328770aa86c12fbb7187966dc`

## Disposition

`PASS_FOR_SEPARATE_CANONICALIZATION`.

Findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

This is a fresh full verification of the exact remediated packet. The prior verification #1134 failed only because the packet lacked a deterministic promotion transform. The corrected packet preserves the previously-passing temporal semantics and now fully determines the mechanical promotion bytes, subject to a separately authorized canonicalization issue binding this exact candidate, manifest identity, and verified base.

This PASS grants no integration, maintenance mutation, canonicality, implementation-readiness, engine-selection, release, production, or decision authority.

## Frozen identities and compatibility basis

- Producer #1137 terminal: comment `5668329071`, `VERIFICATION_READY`.
- Producer head: `e0f87494eea335ff195ace746689b486bc40909d`; its single commit is directly based on `51cc20dbbc4ebbbdea9bbde91e480776b0e4b047` and changes exactly the candidate, manifest, and #1137 handoff.
- PR #1139 remains the exact producer surface and contains exactly those three paths.
- Candidate Git-blob SHA independently recomputed from bytes: `2d98f95c58d15bddf7c00be3fd5905aa8ca501e5`.
- Manifest Git-blob SHA independently recomputed from bytes: `d075d7bd92e1c7636ab77a962a677c521c9db7b5`.
- Original failed packet: candidate `fe2c832f4da5971956b7f83ce651fd3f1586dabe`, manifest `55909cb6400584e9238bf149da09bb406ec3dc93`.
- Reviewed governance source #1124 blob: `a59f04feb2c7e0344fdaab1fcbf4fa291e79a107`.
- Required governance review #1126 terminal: `5659773876`, `PASS_FOR_CANONICAL_LEASE_SEMANTICS_REVISION`.
- Active binding remains Issue #6 comment `5245368879`, program blob `e3120ec203c4156328770aa86c12fbb7187966dc`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.
- Activation ancestry check: current verified base is 260 commits ahead and 0 behind activation; the activation commit is the merge base.
- The active canonical program bytes are unchanged at the exact bound blob.

## Full verification attacks

1. **Exact source composition — PASS.** Candidate Section 1 preserves every active canonical clause except the explicit temporal overlay and fails closed on outside conflicts. The manifest binds the exact active canonical blob and preservation rule.
2. **Remediation boundedness — PASS.** After normalizing only the expected remediation header identities, candidate Sections 1–12 are byte-equivalent to the prior #1128 packet. The substantive new content is Section 13, the deterministic promotion contract.
3. **Six-hour status — PASS.** Candidate and manifest consistently mark 21,600 seconds as a reviewed governance decision not yet active canon.
4. **Authoritative clock / malformed time — PASS.** GitHub comment `created_at` is sole temporal authority; `updated_at`, body/local/workflow clocks are excluded. Missing, malformed, null, or timezone-naive timestamps fail closed without manufacturing STALE authority.
5. **Exact-boundary expiry — PASS.** Claim at 12:00:00Z is live through 17:59:59.999Z; 18:00:00Z is expired and STALE becomes only temporally eligible subject to all structural predicates.
6. **PROGRESS renewal — PASS.** Valid PROGRESS at 17:00Z moves expiry to 23:00Z, therefore STALE at 18:01Z remains premature.
7. **EVIDENCE cap — PASS.** E1/E2/E3 may renew; E4 without HEAD_ADVANCE is invalid and the anchor remains E3.
8. **No resurrection — PASS.** PROGRESS at or after exact expiry is invalid and cannot restore ownership.
9. **HANDOFF / terminal freshness — PASS.** Owner-required handoff and terminal publication require current, unexpired ownership; valid pre-expiry HANDOFF retains the existing HANDOFF intent -> RESUME route rather than STALE.
10. **STALE recovery — PASS.** Premature STALE has zero authority; exact-boundary STALE is only temporally eligible; source/head/current-generation/winner/first-grant and no-intervening-authority predicates remain mandatory.
11. **ORPHAN recovery — PASS.** Existing 600-second boundary is preserved; 12:09:59.999 is premature and 12:10:00 is mature only absent a later valid owner.
12. **Losing ownership contenders — PASS.** Existing lowest-valid-comment-ID contention is preserved; losing CLAIM/RESUME/RECOVER records have no authority.
13. **Prefix-scoped non-retroactivity — PASS.** Evaluation is through the operational comment. Later recovery cannot retroactively invalidate an earlier authoritative terminal; a stale prior-owner terminal after valid recovery is invalid.
14. **CANONICAL_ACTIVE guard — PASS.** Bootstrap-numbered work remains provenance-only and generic restart/refresh is not broadened beyond tasks that declare it.
15. **Stage-B separation — PASS.** Inactive IntegrationUnit/global coordination TTLs remain inactive and separate.
16. **Canonical-base regression guards — PASS.** The exact active program continues to expose the single normal open-`[PLAN-v1]` queue, preserve durable binding, keep high-throughput gameplay implementation blocked, retain review/verification gates, and require squash-only integration.
17. **Manifest exact-payload binding — PASS.** The manifest binds candidate blob `2d98f95c58d15bddf7c00be3fd5905aa8ca501e5`; this verification binds the manifest itself to exact blob `d075d7bd92e1c7636ab77a962a677c521c9db7b5`.
18. **Deterministic promotion transform — PASS.** Each of the four declared source literals occurs exactly once. Applying the four declared replacements with test canonicalization issue `999999` produces canonical title/state/authority/provenance headers and Git-blob SHA `94561b26a7553f02c64da87f528f5d37b914a7e5`.
19. **Byte-identical remainder — PASS.** The promotion operation is exactly the four declared replacements; all other candidate bytes remain identical.
20. **Canonicalization issue parameter — PASS.** Valid positive canonical base-10 values such as `1` and `999999` pass encoding; `0`, negative, leading-zero (`001`), non-numeric, and fractional forms fail. The parameter is provenance-only and may appear only in the declared `Canonicalized by: Issue #N` output.
21. **Canonicalization contract binding — PASS.** The parameter is usable only by a separately scoped/authorized canonicalization issue contract binding this exact verified candidate, this exact verified manifest identity, and this verified base; terminal schema-3 `INTEGRATION_STATUS` must be published on that same issue and bind the promoted program blob.
22. **Fail-closed literal identity — PASS.** Removing any source literal or duplicating a source literal makes the transform ineligible. Wrong candidate/manifest identity or undeclared byte mutation is expressly fail-closed.
23. **Post-PASS drift — PASS.** Any candidate or manifest byte change requires a new full verification episode; refresh cannot substitute for changed payload.
24. **Current-base exact-payload selection — PASS.** This verification branch was created from exact then-current `main@8468daf824aee6e5ef48ffead0918a5512bd4b0c`, with current main unchanged through evidence recording, and is bound to the immutable producer head and exact payload above.

## Closure of prior finding

### FACTORY-LEASE-CANON-VERIFY-MAJ01 — CLOSED

The prior packet left canonical promotion bytes unspecified. The corrected candidate/manifest now define the destination, exact four source literals, exact canonical replacements, the sole provenance-only parameter, parameter encoding, exact-payload/base preconditions, same-issue terminal binding requirement, byte-identical remainder rule, and fail-closed behavior.

The independent dry run reproduces the producer-declared promoted Git blob exactly: `94561b26a7553f02c64da87f528f5d37b914a7e5`.

## Required next route

A **separately scoped canonicalization issue** may now be materialized only if its contract binds:
- candidate blob `2d98f95c58d15bddf7c00be3fd5905aa8ca501e5`;
- manifest blob `d075d7bd92e1c7636ab77a962a677c521c9db7b5`;
- verified base `8468daf824aee6e5ef48ffead0918a5512bd4b0c`;
- this verification PASS;
- exact expected-head/base checks, squash-only publication, and same-issue terminal durable binding.

Until that separately authorized episode completes, the Issue #6 binding and program blob `e3120ec203c4156328770aa86c12fbb7187966dc` remain the sole active canonical basis and the six-hour lease remains inactive.
