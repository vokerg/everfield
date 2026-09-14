# Handoff — Issue #1120 / FACTORY-CONVERGENCE-06-REM-03

## State

`INVALIDATED` for the declared two-path remediation scope. No v5 candidate mutation was made.

## Ownership / basis

- winning claim: `5659662494`
- actor/session: `frontier-drain-factory-conv06-rem1120-gpt56sol-20260914-01`
- branch/base: `planning/issue-1120` @ `51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- source review: #1118 terminal `5659656349`
- finding: `FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01`
- predecessor candidate: #1116 v5 blob `477bc36ea788867cf2744f4f9b9ccfb161c875b6`

## Blocking scope result

The required correction cannot be implemented faithfully inside the declared v5-only code surface without inventing a second schema-3 lease validator.

The existing maintenance stack exposes parsing, immutable-comment checks, owner linkage, and progress records, but no reviewed helper that determines canonical ownership lease expiry at an arbitrary GitHub server timestamp. The canonical manifest makes `PROGRESS` a lease renewal and makes STALE recovery depend on lease expiry, while the #1120 contract explicitly forbids inventing a divergent lease model and requires scope revision when the needed helper lies outside v5.

ORPHAN maturity is mechanically specified as ten GitHub server minutes and could be implemented locally, but fixing only ORPHAN would leave the MAJOR STALE-recovery authority defect unresolved. A partial patch would therefore not satisfy #1120 acceptance.

## Required next route

Route one scope-revision remediation that may add/reuse a single reviewed schema-3 temporal-validity helper in the shared maintenance layer and then consume that helper from v5. The revised scope must define the exact canonical lease-expiry predicate from authoritative repository state, cover CLAIM/RESUME/RECOVER plus valid PROGRESS renewals, preserve comment-server-time authority, and add boundary tests for premature/valid STALE and ORPHAN recovery. It must then route a fresh required review.

## Authority boundary

- finding closed: false
- integration authority: false
- verification-PASS authority: false
- implementation-readiness authority: false
- canonicality: `NOT_CANONICAL`
