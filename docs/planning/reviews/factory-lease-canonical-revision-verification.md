# Verification — schema-3 ownership lease canonical revision packet

**Verification issue:** #1134 / `FACTORY-LEASE-CANON-VERIFY-01`  
**Producer:** #1128 / PR #1130  
**Trust mode:** `DEGRADED_SINGLE_AGENT`  
**Verified base:** `main@51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`  
**Producer head:** `cccf9b32764ff4c7fdaf9bc8b0a19ce1da7ebc8a`  
**Candidate blob:** `fe2c832f4da5971956b7f83ce651fd3f1586dabe`  
**Manifest blob:** `55909cb6400584e9238bf149da09bb406ec3dc93`  
**Active canonical program blob:** `e3120ec203c4156328770aa86c12fbb7187966dc`

## Disposition

`CHANGES_NEEDED` / verification result `FAIL`.

Findings: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

The temporal lease semantics are internally consistent and preserve the reviewed governance decision, but the exact packet cannot pass required attack 15 because it does not define the bytes/mechanical transform that a later canonicalization episode is authorized to publish. A canonicalizer would have to invent a destination/header transformation after verification, so the verified candidate/manifest identities would not fully determine the promoted canonical program.

## Frozen identities checked

- Issue #1128 terminal producer comment: `5659852198`.
- PR #1130 changed paths: exactly the lease revision candidate, lease revision manifest, and #1128 handoff.
- Active binding: Issue #6 comment `5245368879`; activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.
- Reviewed governance source: Issue #1124 blob `a59f04feb2c7e0344fdaab1fcbf4fa291e79a107`.
- Required governance review: Issue #1126 terminal `5659773876`, `PASS_FOR_CANONICAL_LEASE_SEMANTICS_REVISION`.
- Current main remained exactly `51cc20dbbc4ebbbdea9bbde91e480776b0e4b047` through verification.

## Required attacks

1. **Exact source composition — PASS.** Candidate Section 1 explicitly preserves every active canonical clause except the temporal overlay and fails closed on conflicts. The manifest binds the exact active canonical blob and preservation rule.
2. **Six-hour status — PASS.** Candidate and manifest consistently mark 21,600 seconds as a new reviewed governance decision that is not active canon.
3. **Authoritative clock / malformed time — PASS.** GitHub API comment `created_at` is sole authority; body/local/workflow/`updated_at` are excluded; missing, malformed, null, or timezone-naive required timestamps fail closed and cannot manufacture STALE authority.
4. **Exact-boundary expiry — PASS.** Live is `t < anchor + 21600s`; expiry is `t >= anchor + 21600s`.
5. **PROGRESS renewal and EVIDENCE cap — PASS.** Renewal is current-generation-only and pre-expiry; existing HEAD_ADVANCE rules remain; only three consecutive EVIDENCE renewals are valid and E4 does not move the anchor.
6. **No post-expiry resurrection — PASS.** PROGRESS at or after the boundary is invalid.
7. **HANDOFF / terminal freshness — PASS.** Owner-required handoff/terminal publication requires current unexpired ownership; valid pre-expiry HANDOFF remains on the existing HANDOFF intent -> RESUME route.
8. **STALE temporal predicate — PASS.** Premature STALE has zero authority; exact-boundary STALE is only temporally eligible and all existing source/head/current-generation/winner/first-grant predicates remain mandatory.
9. **ORPHAN maturity — PASS.** Existing 600-second server-time boundary is preserved; exact boundary is mature; later valid owner invalidates the route.
10. **Losing ownership contenders — PASS.** Existing lowest-valid-comment-ID contention is preserved; losing CLAIM/RESUME/RECOVER records have no authority.
11. **Prefix-scoped non-retroactivity — PASS.** Evaluation is through the operational comment; later recovery does not invalidate an earlier authoritative terminal, while a stale prior-owner terminal after valid recovery is invalid.
12. **CANONICAL_ACTIVE guard — PASS.** Bootstrap-numbered work remains provenance-only and restart/refresh is not broadened beyond declared tasks.
13. **Stage-B separation — PASS.** IntegrationUnit/global coordination TTLs remain inactive and separate.
14. **Canonical-base regressions — PASS.** Root queue, durable binding, implementation barrier, independent review/verification gates, and squash-only integration are expressly preserved by reference to the exact active canonical blob.
15. **Mechanical promotion without post-verification mutation — FAIL (MAJOR).** The manifest's `canonicalization_route` names a separately authorized squash publication but does not define an exact destination, literal/header transformation, source-to-destination composition operation, or expected promoted blob derivation. The candidate remains headed `REVIEWED-LEASE-REVISION-CANDIDATE` with `NON-CANONICAL` authority. Copying it unchanged cannot yield a canonical program; changing those bytes later would be a post-verification candidate mutation whose exact semantics/bytes were not verified. Prior canonical promotion manifests solved this with deterministic literal replacements. This packet therefore is not mechanically promotable as required.
16. **Current-base exact-payload selection — PASS.** The manifest requires then-current main and exact candidate/manifest identities and requires fresh verification after payload change. This FAIL is bound to the exact frozen packet and base above.

## Finding

### FACTORY-LEASE-CANON-VERIFY-MAJ01 — missing deterministic canonical promotion transform

**Severity:** MAJOR.

The verification packet does not mechanically specify how the reviewed noncanonical candidate becomes `docs/planning/PLANNING-PROGRAM-v1.md` with canonical state/authority and a new canonicalizer identity. The later canonicalization episode would need to invent or choose unverified bytes.

**Required correction:** revise only the noncanonical candidate/manifest as needed to define a deterministic promotion operation whose source identities are the exact corrected candidate/manifest, whose destination is explicit, whose header/authority/canonicalizer transformation is exact and simulatable before verification, and whose body preserves the verified temporal overlay and active-base composition without semantic drift. Any corrected candidate or manifest bytes require a fresh full verification episode.

## Authority boundary

This verification is `NOT_CANONICAL`. It does not alter the active Issue #6 binding, authorize maintenance implementation/integration, or activate the six-hour lease. The active canonical basis remains program blob `e3120ec203c4156328770aa86c12fbb7187966dc`.
