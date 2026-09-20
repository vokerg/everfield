# Required review — CONT-03 reviewed-root fan-in

**Mission:** `W2-CONTENT-SYN-CONT-03-REV-01`  
**Issue:** #1195  
**Judged producer:** #1193 / draft PR #1194 / exact head `4c9e9f92545f5c8a6d8aa479b9f813533af35011`  
**Trust mode:** `DEGRADED_SINGLE_AGENT`  
**Disposition:** `CHANGES_NEEDED`

## Frozen judged identity

The review inspected only the immutable producer packet bound by #1193 terminal comment `5745526313`:

- Markdown blob `1ac7e595695ec5358e4788776355c5adc487c21e`;
- YAML blob `6f68bd2b0f20dd8d1266f477ccf318aaf5eee0b8`;
- handoff blob `9e8c4260e6e3789d8130e56229d4d6f372a3e40f`;
- PR #1194 base `b665969b56fea4b2c31beee43153ef52a0b252c3`, head `4c9e9f92545f5c8a6d8aa479b9f813533af35011`, draft, open, exactly three changed paths.

All five required reviewed-root tokens were re-resolved from their exact terminal review comments and are valid:
`W2-CONTENT-WORLD-CONT-03_REVIEWED`,
`W2-CONTENT-SOCIAL-CONT-03_REVIEWED`,
`W2-CONTENT-CHAR-CONT-03_REVIEWED`,
`W2-CONTENT-NARR-CONT-03_REVIEWED`,
`W2-CONTENT-EVAL-CONT-03_REVIEWED`.

## Findings

### SYN-CONT03-REV-MAJ-01 — unapproved OPEN-state renaming

**Severity:** MAJOR  
**Status:** unresolved; correction required before bounded consumption.

The reviewed CONT-03 evaluator packet #1174, YAML blob `af3bbd4112ed6099dbf564c1b209c5078f932282`, defines the clean cross-root fiction-scope unresolved-state vocabulary as:

- `OPEN`
- `OPEN_OPTIONAL`
- `OPEN_BOUNDED_SET`
- `UNRESOLVED`
- `TYPED_ROLE_OR_INTERFACE`

It separately attacks both `NARROW_OPEN_WITHOUT_REVIEWED_EVIDENCE` and `HIDDEN_INCOMPATIBILITY_BY_RENAME`.

The judged #1193 YAML changes three inherited open bindings into new, evaluator-undefined state values:

- `SYN-CONT02-OPEN-002: OPEN_WITH_BOUNDED_HYPOTHESES`
- `SYN-CONT02-OPEN-003: OPEN_WITH_TYPED_INTERFACES`
- `SYN-CONT02-OPEN-004: OPEN_WITH_COMPATIBILITY_ENVELOPES`

The Markdown table mirrors those renamed states. The prose and `effect` fields correctly say that no concrete identity, membership, office, site, character, or narrative branch is selected, but that does not make the new machine-readable state names equivalent to the inherited `OPEN` state. Downstream consumers may interpret state values directly; silently replacing `OPEN` with an unreviewed refinement vocabulary can narrow or alter authority semantics and fails the evaluator's exact-state contract.

This is not a final-fiction leak and does not invalidate the five reviewed inputs. It is a bounded representation defect in the synthesis output.

### Required correction

A separate remediation must preserve the judged producer and review branches as immutable provenance and make only the minimum correction:

1. Restore `state: OPEN` for `SYN-CONT02-OPEN-002`, `OPEN-003`, and `OPEN-004` in the machine-readable fan-in.
2. Restore `OPEN` in the corresponding Markdown open-ledger table.
3. Preserve the useful refinements as non-authority metadata, for example:
   - `reviewed_refinement: BOUNDED_HYPOTHESES_AVAILABLE`
   - `reviewed_refinement: TYPED_INTERFACES_AVAILABLE`
   - `reviewed_refinement: COMPATIBILITY_ENVELOPES_AVAILABLE`
   while keeping the inherited state unchanged.
4. Make the handoff explicitly record that those three items remain `OPEN`.
5. Preserve all existing compatibility-envelope content, exact reviewed input identities, all six route-cardinality null/N/A measurements, all 17 packet-local reopen-condition classifications, private-information fail-closed behavior, relative chronology, append-only history, agency/refusal, baseline-play legality, BranchImpactEvidence requirement, WSN E3/E4/E5/E8 states, and every negative authority boundary.
6. Do not use the remediation to select concrete fiction, broaden/narrow reviewed candidate sets, create runtime evidence, or add authority.

## Other required attacks

No additional correction-requiring finding was found.

- **Identity / token barrier:** PASS. Exact producer blobs/PR/head and all five terminal review tokens resolve.
- **Unsupported final binding:** PASS apart from the state-vocabulary defect above. Compatibility envelopes do not select final fiction or concrete authored instances.
- **Reviewed bounded sets:** PASS. The three world surface candidates remain exact and unselected.
- **Epistemic separation:** PASS. Fact, claim, belief, testimony, interpretation, knowledge, exposure, absence records and generated presentation remain distinct.
- **Private information:** PASS. Default deny, optional-only, no foundational or route-minimum dependency.
- **Chronology / schedule / reachability:** PASS. Relative-only; exact dates/durations/schedules/weather/travel/NPC reachability are not authored.
- **History / relationships / legitimacy:** PASS. Material history is append-only; six relationship dimensions remain independent; legitimacy/public standing are not aliases.
- **Agency / refusal:** PASS. No grind, gift, standing, legitimacy, prior success or relationship bypass.
- **Foundational play:** PASS. New foundational-gate count is zero and baseline/nonalignment remain legal.
- **Route cardinality:** PASS. Exactly six reviewed contracts are emitted; there are zero active concrete objective instances, six `observed_active_route_count: null` values and six explicit `NOT_APPLICABLE_NO_ACTIVE_CONCRETE_OBJECTIVE_INSTANCE` statuses. Recompute triggers include activation, refusal, rejection, substitution, recovery and route loss.
- **Branch compatibility / high impact:** PASS. No mutually exclusive branches are jointly required and no concrete high-impact/irreversible branch is authorized without later reviewed BranchImpactEvidence.
- **Reopen conditions:** PASS. All 17 exact classes are present and packet-locally classified `CLEARED_IN_THIS_EVALUATION`; later instances are not pre-cleared.
- **WSN:** PASS. E3/E4/E5/E8 remain exactly `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`, `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`, `PASS_BOUNDED_MODEL_ONLY`, `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`.
- **Generated / engine / higher authority:** PASS. No generated-state mutation, engine coupling, human-quality, production, aggregate verification, readiness, release, final-canon or canonical inflation.
- **Markdown/YAML/handoff consistency:** CONSISTENT with the same state-renaming defect; no second inconsistency finding.

## Finding counts

- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 0

## Required next route

Exactly one bounded remediation successor:

`W2-CONTENT-SYN-CONT-03-REM-01`

The remediation must target only `SYN-CONT03-REV-MAJ-01`, after which exactly one fresh remediation review is required. This review grants no integration or consumption authority.
