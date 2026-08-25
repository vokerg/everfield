# Issue #685 review handoff

Reviewed Issue #682 / PR #684 at exact head `040ddf86a4c2a71a89693c741a05986ff96be5a1` against `main@853ceee085253f05030e617141ad00883d4f6226`.

Disposition: `CHANGES_NEEDED`, 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.

M01/M02 from the first review are closed. New findings:
- M03: storage cleanup accepts terminal-shaped owner comments without validating ownership-generation/head/work linkage.
- M04: the generated factory-transition issue itself suppresses later registered dispatch retry if the first run dies between materialization and dispatch recording.

Required next route: bounded M03/M04 remediation with conservative terminal eligibility and explicit factory-dispatch marker/idempotence, then fresh review.
