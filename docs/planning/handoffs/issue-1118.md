# Handoff — Issue #1118 / FACTORY-CONVERGENCE-06-REM-02-REV-01

## State

Required review terminalizes `CHANGES_NEEDED` against immutable remediation Issue #1116 / PR #1117.

## Ownership / judged identity

- review claim: `5659641849`
- review actor/session: `frontier-review-factory-conv06-rem1118-gpt56sol-20260914-01`
- trust mode: `DEGRADED_SINGLE_AGENT`
- review branch: `planning/issue-1118`
- review base: `51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`
- judged terminal: #1116 comment `5659634282`
- judged head: `a6e173649909fa9fee679916d882f7ed0ab0ffc8`
- judged PR: #1117
- judged v5 blob: `477bc36ea788867cf2744f4f9b9ccfb161c875b6`

## Result

Disposition: `CHANGES_NEEDED`.

Finding `FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01` (MAJOR): the #1116 ownership reconstruction accepts STALE and ORPHAN recovery generations without proving the canonical temporal predicates. STALE recovery must prove lease expiry; ORPHAN recovery must prove the ten-minute server-time maturity of the orphan probe. A premature recovery currently can be treated as winning ownership and can therefore distort terminal no-route consumption.

Required successor: exactly one bounded remediation preserving #1116's winning-intent/losing-contender correction while adding temporal recovery validity and deterministic premature-STALE/premature-ORPHAN negatives, followed by one fresh required review.

## Counts / authority

- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 0
- integration authority: false
- verification-PASS authority: false
- implementation-readiness authority: false
- engine-selection authority: false
- canonicality: `NOT_CANONICAL`
