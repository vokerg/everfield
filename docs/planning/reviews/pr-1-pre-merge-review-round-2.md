# PR #1 Pre-Merge Review — Round 2

**Review target:** PR #1 — `planning/factory-seed` → `main`  
**Review type:** cold-start, post-merge consistency, governance, and continuation review  
**Result:** PASS AFTER FIXES  
**Canonicalization effect:** none; this review approves integration of the SEED corpus, not the truth of every SEED hypothesis.

## Scope

This review asks whether PR #1 is safe to integrate as the repository-owned seed for the PLAN-THE-PLAN phase and whether a fresh AI agent can continue from the merged repository without hidden conversation context.

The review specifically checks:

- cold-start discoverability;
- bootstrap work eligibility;
- deterministic claiming;
- branch/base semantics after the seed PR is merged;
- handoff/recovery requirements;
- review/canonicalization separation;
- prohibition on premature gameplay implementation;
- preservation of explicit human directives;
- integration-history policy.

## Evidence inspected

- root `AGENTS.md`;
- `docs/planning/START-HERE.md`;
- planning corpus index and seed documents;
- bootstrap Issues #2–#6;
- PR #1 metadata and branch relationship to `main`;
- default-branch README bootstrap pointer;
- current repository merge capabilities.

## Findings and dispositions

### MAJOR-1 — Post-merge task base would have remained stale

**Finding:** `planning/factory-seed` had diverged from `main` because the default-branch bootstrap README was added after the seed branch was created. Earlier bootstrap instructions still told new work to branch from `planning/factory-seed`. After PR #1 integration this would make new planning tasks start from a provenance branch rather than authoritative `main`.

**Disposition:** FIXED.

`docs/planning/START-HERE.md` now defines current `main` HEAD as the normal bootstrap task base after PR #1 integration. `planning/factory-seed` becomes provenance only. Issue #2 was updated to require a deterministic `planning/issue-2` branch from current `main` after PR #1 is merged.

### MAJOR-2 — Squash integration was descriptive, not normative

**Finding:** The seed corpus mentioned controlled squash integration, but there was no binding rule preventing a future agent from using merge-commit or rebase-merge when GitHub exposes those methods.

**Disposition:** FIXED by explicit human directive.

Root `AGENTS.md` and the project charter now state that every integration into `main` MUST use squash merge. The directive explicitly survives future planning work unless a later human directive supersedes it.

### MAJOR-3 — Issue #2 could have been claimed before its authoritative corpus existed on `main`

**Finding:** Before this review, Issue #2 was technically open/eligible while its authoritative corpus still lived only in draft PR #1.

**Disposition:** FIXED.

Issue #2 now has a hard prerequisite that PR #1 must first be squash-merged into `main`. Only then is `planning/issue-2` created from current `main`.

### MINOR-1 — Merging SEED documents could be misread as canonicalizing them

**Finding:** A naive continuation agent might interpret presence on `main` as CANONICAL status.

**Disposition:** ACCEPTED WITH EXISTING/UPDATED GUARDS.

The corpus state model already distinguishes SEED / PROPOSED / CANONICAL / SUPERSEDED. `START-HERE.md` explicitly warns that seed documents do not become reviewed truth merely because PR #1 is merged. This review also records that integration is provenance/availability, not canonicalization of design hypotheses.

## Cold-Start Simulation After Fixes

Expected path after merge:

```text
fresh agent
  -> main/README.md
  -> root AGENTS.md
  -> docs/planning/START-HERE.md
  -> inspect [PLAN-BOOTSTRAP] issues
  -> #2 is first eligible work
  -> verify no planning/issue-2 branch exists
  -> create planning/issue-2 from current main HEAD
  -> read only #2 authoritative inputs
  -> produce Planning Program v1 proposal
  -> commit + structured handoff
  -> leave proposal non-canonical
  -> #3 independent adversarial review
  -> #4 synthesis/revision
  -> #5 cold-start verification
  -> #6 canonicalization/first planning wave only after PASS
```

No prior chat transcript is required for this path.

## Remaining Open Questions

The following are intentionally NOT blockers for merging this seed corpus because the bootstrap planning program exists specifically to resolve them:

- mature atomic scheduler/claim service;
- stale-claim timeouts and recovery;
- exact issue state machine and GitHub Projects representation;
- protected evaluator topology;
- engine selection;
- final technical architecture;
- final game design;
- final two-review implementation protocol details;
- merge queue configuration and enforcement automation;
- exact CI/evidence schemas.

These must remain explicit planning work rather than implicit assumptions.

## Merge Recommendation

**PASS AFTER FIXES.**

PR #1 is suitable for integration as the seed planning corpus provided it is merged using **squash merge**.

After integration, update the default-branch README if necessary so that it no longer describes PR #1 as an unmerged draft and instead points directly to the merged bootstrap entry path and Issue #2.
