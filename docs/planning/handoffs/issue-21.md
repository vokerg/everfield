# Issue #21 handoff — W1-REC-01

Mission: `W1-REC-01`
Branch: `planning/issue-21`
Claim comment: `5280999394`
Actor/session: `w1-rec-01-gpt56sol-20260813-1521-recovery`
Base main: `3828d50d3345ef0bc5a61321509f590b2e7b2ae1`
Recovery artifact: `docs/planning/wave-1/recovery/liveness-recovery.md`
Recovery artifact commit: `744aec04dfa6c43a1dbed4c84a5fd94271bb95f1`

## Diagnosis

The active schema defines stale ownership through `lease_expiry` but does not provide a deterministic owner-lease duration or expiry function. That prevents a fresh reader from deriving a stale takeover solely from elapsed time.

Issue #84 remains blocked by invalid authority records: claim `5280748633` is the last clearly valid ownership generation; attempted `HANDOFF_READY` `5280814925` was recorded as schema-invalid; PR #190 is visibility only; attempted `REVIEW_STATUS` `5280974426` was edited and therefore cannot be used as schema-3 authority.

Issue #181 remains blocked by its original claim `5280677079`; PR #183 is visibility only and its attempted handoff was recorded as schema-invalid. Stage-B verification is not unlocked by PR existence.

## Safe continuation

Re-derive current main and both issue histories. Continue only after repository state contains one of the following:

- a fresh unedited schema-valid terminal Issue #84 review record bound to a valid ownership generation and exact task head;
- a fresh unedited schema-valid terminal Issue #181 producer record bound to a valid ownership generation and exact task head;
- a separately reviewed and verified canonical revision defining deterministic owner-lease expiry and stale recovery;
- another authorization route already recognized by the active schema.

If Issue #84 becomes validly terminal, re-derive whether its review provenance should be squash-integrated before Issue #85. If Issue #181 becomes validly terminal, use the required independent Stage-B verification route before any activation.

## Result

`HANDOFF_READY`. The liveness defect is bounded and recorded, but this recovery episode does not itself create a stronger review, verification, integration, readiness, or canonicalization authority.