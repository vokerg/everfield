# W1-REC-01 — Planning liveness recovery

## Episode

- mission: `W1-REC-01`
- issue: `#21`
- recovery actor: `w1-rec-01-gpt56sol-20260813-1521-recovery`
- claim comment: `5280999394`
- claim/base main: `3828d50d3345ef0bc5a61321509f590b2e7b2ae1`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Bootstrap Issue #6 terminal `INTEGRATION_STATUS` comment `5245368879`, activation main `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- interpretation state: `CANONICAL_ACTIVE`

## Failure classification

`CORRUPTED_STATUS_AND_MISSING_LEASE_THRESHOLD`

The live frontier contains completed-looking branch/PR packets whose authoritative task state cannot legally advance under the active schema-3 contract.

### Affected aggregate review — Issue #84 / `W2-REV-01`

- original valid owner claim: `5280748633` at `planning/issue-84@082740ff455b2dd81966bdb06a413000d2e704bc`
- attempted `STATUS(HANDOFF_READY)`: `5280814925`
- repository clarification `5280894049` correctly records that `5280814925` is schema-invalid: it omits required `handoff_path` and includes top-level fields not admitted for `HANDOFF_READY`
- later `RESUME` generation `5280882773` therefore has no valid HANDOFF predecessor and cannot become authoritative
- PR #190 exists at head `25ecff8252a0065a6d54f819df9e114a269edbbf` and contains the materialized aggregate review packet
- attempted `REVIEW_STATUS` `5280974426` reports `CHANGES_REQUIRED`, 0 BLOCKER / 3 MAJOR, but GitHub records `created_at=2026-08-13T13:20:20Z` and `updated_at=2026-08-13T13:20:39Z`; canonical authority metadata requires `created_at == updated_at`, so the edited capsule has zero authority effect
- therefore Issue #85 / `W2-SYN-01` remains blocked; PR #190 is review visibility/provenance only and is not an authority substitute

### Affected Stage-B protocol candidate — Issue #181 / `ARCH-CONVERGENCE-CANON-01`

- valid owner claim: `5280677079`
- frozen candidate branch head / PR #183 head: `ef0187fedc1c00dc9b1f77dec2e84e8c548b8171`
- attempted structured handoff `5280737109` is schema-invalid; repository clarification `5280775612` records that the original claim remains the operative ownership generation
- PR #183 therefore does not make the Stage-B candidate `REVIEW_READY`, does not unlock independent Stage-B verification, and grants no activation/canonical-binding authority

## Canonical liveness defect

The active contract defines:

- derived `STALE_OWNER` as an ownership/renewal lease that has expired;
- `RESUME_INTENT(reason=STALE)` only from an expired current owner or `PROGRESS`;
- `RECOVER(STALE)` only from the winning stale intent while the source remains stale;
- GitHub server time as the time authority.

However, the active canonical program/manifest provides no numeric lease duration, TTL, expiry timestamp field, or deterministic function that maps an ownership-generation creation/renewal time to `lease_expiry`. The manifest contains the explicit ten-minute maturity window for `ORPHAN_PROBE`, demonstrating that time windows are specified when intended, but no corresponding ownership-lease threshold exists.

Consequently a fresh reader cannot prove either `current_unexpired_owner` or `STALE_OWNER` from elapsed time alone. Guessing 10, 20, 30, 60, or any other duration would invent protocol authority and could create competing mutation owners.

## External-retirement check

Schema-3 `STATUS(authority_mode=EXTERNAL)` cannot repair this deadlock autonomously. It is limited to `SUPERSEDED|INVALIDATED` and requires `external_authorization_comment_id` whose authorization kind is `REVIEW_STATUS` or `INTEGRATION_STATUS`. W1-REC-01 itself is neither of those authorization kinds. Therefore this recovery episode cannot lawfully retire #84 or #181 by assertion.

## Smallest safe recovery boundary

No review, verification, canonicalization, readiness, or squash-only gate is waived. The following are safe; anything weaker is rejected:

1. **Owner-completion route:** a still-valid current owner, under a separately established deterministic lease rule, publishes a fresh **unedited** schema-valid terminal record at the exact current task-branch head. For #84 that must be a valid aggregate-review terminal record; for #181 it must be a valid producer terminal record. PR text/mergeability is not a substitute.
2. **Protocol-repair route:** if current ownership cannot be proven unexpired, a separately reviewed and verified canonical protocol revision must define the missing ownership lease/expiry semantics and recovery transition before any stale takeover. The revision must preserve immediate winner recheck, immutable task packet identity, review/verification separation, and squash-only main integration.
3. Until one of those routes is valid, **do not** claim #85 from the edited #84 review capsule, do not integrate PR #190 as if it carried aggregate-review authority, do not start Stage-B verification from PR #183, and do not infer stale ownership from wall-clock age.

## Resulting frontier

The recovery episode identifies a control-plane deadlock rather than a substantive evidence defect. Existing evidence packets are preserved unchanged. There is currently no canonical-authorized autonomous mutation that can convert the two stuck ownership generations into new owners without first satisfying one of the safe routes above.

This is a fail-closed recovery result. It intentionally does not fabricate a lease threshold, rewrite an edited authority comment, impersonate another actor session, or create a parallel substitute for the required aggregate review.

## Reopen / completion conditions

Re-evaluate immediately when any of the following becomes durable repository state:

- a fresh unedited valid #84 aggregate-review terminal capsule at exact PR/task head;
- a fresh unedited valid #181 producer terminal capsule at exact PR/task head;
- an independently reviewed/verified canonical revision that gives ownership leases a deterministic expiry rule and stale-recovery semantics;
- a stronger explicit external authorization that is itself valid under the active schema.

At that point the dispatcher must re-derive the frontier from current `main` and take the highest-priority newly eligible continuation/integration/verification path.