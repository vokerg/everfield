# Issue #1153 handoff — required review of recovery-lease remediation

## State

Required review of immutable producer Issue #1151 / PR #1152 completed with disposition `CHANGES_NEEDED`.

Review owner: comment `5739808132`, actor `everfield-agent-review1153-gpt56sol-20260919-01`.

## Frozen producer

- producer terminal: Issue #1151 comment `5739787607`
- producer head/work: `52ad92145e757d7eb86a2e3b9bd94f789dafc82c`
- producer PR: #1152, draft
- v1 blob: `37aa2162f9c0d95ad8cbed015cf9ec8aa3b0c9c0`
- v5 blob: `3a0eae39a9b99a34a5b45f4f0af535b8d4e002be`
- producer handoff: `0716732f5764b5e2819120a01699f31d5b4b43d5`

## Review result

Independent exact-byte compile/self-tests and the bounded attack suite passed except for two correction findings:

1. `FACTORY-CONVERGENCE-06-REM-04-REV-MAJ01` — malformed owner terminal records lacking valid exact head/work identities can be treated as temporal displacement and suppress lawful STALE recovery.
2. `FACTORY-CONVERGENCE-06-REM-04-REV-MIN01` — `parse_github_server_time()` accepts non-RFC3339 ISO spellings although the canonical temporal contract requires strict RFC3339/fail-closed parsing.

Counts: 0 BLOCKER / 1 MAJOR / 1 correction-requiring MINOR.

All other required attacks and current-main composition checks are non-findings. The full report is `docs/planning/wave-2/reviews/factory-convergence-06-rem-04-review.md`.

## Next required action

Materialize exactly one bounded remediation that fixes both findings without editing unrelated maintenance semantics. After remediation, rerun exact-byte v1-v5 compile/self-tests and both attack reproductions, then route one fresh required degraded-independent review.

The review terminal comment will bind the exact final review branch head/report/handoff and the remediation successor identity.

## Authority boundary

`NOT_CANONICAL`. Review provenance only. No producer integration, verification-PASS, implementation-readiness, engine-selection, release, production, decision, or canonical authority.
