# Issue #1134 handoff — lease canonical revision verification

## Identity

- mission: `FACTORY-LEASE-CANON-VERIFY-01`
- winning claim: `5660206853`
- branch: `planning/issue-1134`
- base: `main@51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- trust mode: `DEGRADED_SINGLE_AGENT`
- producer: Issue #1128 terminal `5659852198`, PR #1130, head `cccf9b32764ff4c7fdaf9bc8b0a19ce1da7ebc8a`
- candidate blob: `fe2c832f4da5971956b7f83ce651fd3f1586dabe`
- manifest blob: `55909cb6400584e9238bf149da09bb406ec3dc93`

## Result

Verification result: `FAIL` / disposition `CHANGES_NEEDED`.

Findings: 0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR.

The temporal semantics pass the required adversarial checks, including exact-boundary expiry, PROGRESS/EVIDENCE renewal, no resurrection, HANDOFF/terminal freshness, STALE/ORPHAN timing, losing-contender rejection, prefix-scoped non-retroactivity, bootstrap applicability, Stage-B separation, and active-base preservation.

The packet fails required mechanical-promotion attack 15.

### FACTORY-LEASE-CANON-VERIFY-MAJ01

The candidate is explicitly noncanonical and the manifest does not define an exact source-to-`PLANNING-PROGRAM-v1.md` promotion operation or deterministic header/authority/canonicalizer transformation. A future canonicalizer would need to invent post-verification bytes. This violates the exact-payload/no-post-verification-mutation requirement.

Required next route: one bounded revision of the noncanonical #1128 candidate/manifest to add a deterministic, pre-verifiable promotion transform, followed by fresh full exact-payload verification. Do not change the active canonical program or binding.

## Authority

`NOT_CANONICAL`. This handoff grants no integration, maintenance mutation, implementation-readiness, engine-selection, release, decision, production, or canonical authority. Six hours remains noncanonical.
