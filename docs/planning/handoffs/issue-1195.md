# Issue #1195 handoff — required review of CONT-03 fan-in

## Mission
`W2-CONTENT-SYN-CONT-03-REV-01`

## Review ownership
- winning claim: `5745558328`
- actor/session: `everfield-agent-content-syn-cont03-review-1195-gpt56sol-20260919-02`
- trust mode: `DEGRADED_SINGLE_AGENT`
- review branch: `planning/issue-1195`
- review base: `main@b665969b56fea4b2c31beee43153ef52a0b252c3`

The producer branch `planning/issue-1193` was treated as immutable.

## Judged packet
- producer: #1193 terminal `5745526313`
- draft PR: #1194
- exact head: `4c9e9f92545f5c8a6d8aa479b9f813533af35011`
- Markdown blob: `1ac7e595695ec5358e4788776355c5adc487c21e`
- YAML blob: `6f68bd2b0f20dd8d1266f477ccf318aaf5eee0b8`
- handoff blob: `9e8c4260e6e3789d8130e56229d4d6f372a3e40f`
- changed paths: exactly three

All five frozen reviewed-root token comments were independently re-resolved and remain terminal clean.

## Disposition
`CHANGES_NEEDED`

Finding counts:
- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 0

### SYN-CONT03-REV-MAJ-01 — UNAPPROVED_OPEN_STATE_RENAMING

The reviewed evaluator permits cross-root unresolved states `OPEN`, `OPEN_OPTIONAL`, `OPEN_BOUNDED_SET`, `UNRESOLVED`, or `TYPED_ROLE_OR_INTERFACE` and attacks hidden incompatibility by rename / unsupported OPEN narrowing.

The judged fan-in replaced inherited `OPEN` for `SYN-CONT02-OPEN-002`, `OPEN-003`, and `OPEN-004` with evaluator-undefined `OPEN_WITH_BOUNDED_HYPOTHESES`, `OPEN_WITH_TYPED_INTERFACES`, and `OPEN_WITH_COMPATIBILITY_ENVELOPES`. Prose correctly denies concrete selection, but downstream machine consumers cannot be required to infer those custom values as equivalent to `OPEN`.

## Required correction
Use a separate remediation branch. Restore exact `state: OPEN` for those three bindings in YAML and exact `OPEN` in the Markdown table. Keep the useful refinement as a separate non-authority metadata field and explicitly record in the remediation handoff that the inherited OPEN state remains unchanged.

Do not alter the compatibility envelopes or any other semantic surface except what is needed to keep Markdown/YAML/handoff consistent with the exact OPEN-state vocabulary.

Preserve:
- all five exact reviewed input identities;
- six explicit route-cardinality null/N/A measurements and all recomputation triggers;
- all 17 packet-local reopen-condition classifications;
- private-information fail-closed behavior;
- relative chronology, append-only history, relationship/legitimacy separation, refusal/agency and baseline-play legality;
- BranchImpactEvidence requirement;
- WSN E3/E4/E5/E8 exact states;
- every negative authority boundary.

## Other attacks
All other required attacks passed without correction-requiring findings. See the review report for the exact checklist.

## Review artifacts
- `docs/planning/wave-2/reviews/w2-content-fan-in-continuation-03-review.md`
- `docs/planning/handoffs/issue-1195.md`
- draft PR #1196

The terminal review status, not this prose, freezes the final review head and blob identities.

## Required next route
Exactly one bounded remediation: `W2-CONTENT-SYN-CONT-03-REM-01`, followed by one fresh remediation review.

This review grants no integration, consumption, verification-PASS, implementation/readiness, gameplay implementation, engine selection, human-quality, release/production, decision/final-canon, or canonical authority.
