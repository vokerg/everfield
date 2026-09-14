# Handoff — Issue #1122 / FACTORY-CONVERGENCE-06-REM-03-SCOPE

## State

`INVALIDATED` pending canonical governance clarification. No maintenance code was changed.

## Ownership / frozen basis

- winning claim: `5659671939`
- actor/session: `frontier-drain-factory-conv06-rem1122-gpt56sol-20260914-01`
- branch/base: `planning/issue-1122` @ `51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- source #1120 terminal: `5659670610`
- source review #1118 terminal: `5659656349`
- finding: `FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01`

## Canonical contract check

The canonical Planning Program and schema-3 manifest define the qualitative stale transition (`IN_PROGRESS -> STALE: lease_expiry`), require `PROGRESS` to renew the current lease, make GitHub server creation time authoritative, and define ORPHAN probe maturity as exactly ten server minutes. They do **not** define a deterministic ownership lease duration or equivalent computable expiry predicate in the authoritative machine contract inspected for this task.

The existing `tools/planning/frontier_maintenance.py` through v4 likewise exposes no reviewed lease-expiry constant/helper from which that missing policy can be derived. Therefore implementing STALE temporal validation would require guessing a duration or inventing policy. #1122 explicitly forbids that and requires governance clarification when the canonical contract does not provide the predicate.

ORPHAN can be computed, but a partial ORPHAN-only patch cannot close the MAJOR because premature STALE recovery remains authority-effective in v5.

## Required next route

A bounded governance clarification must canonically specify the ownership lease duration/expiry rule, including:

- duration or exact deterministic expiry predicate;
- which record starts a generation lease;
- how valid `PROGRESS` renewals reset/extend it;
- exact boundary semantics (`>=` versus `>` at expiry);
- GitHub server-time parsing/failure behavior;
- interaction with HANDOFF/terminal records and recovery contention;
- whether the rule applies uniformly to CLAIM/RESUME/RECOVER generations.

After that clarification is reviewed/canonical under repository authority, re-route the temporal maintenance remediation and fresh required review. No implementation may infer this policy from chat history or convention.

## Authority boundary

- finding closed: false
- integration authority: false
- verification-PASS authority: false
- canonicality: `NOT_CANONICAL`
