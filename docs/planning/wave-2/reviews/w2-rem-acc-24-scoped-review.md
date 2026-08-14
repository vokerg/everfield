# W2-REV-ACC-24 — scoped review of XAG 123 resource-localization remediation

## Ownership and frozen review input

- Issue: `#326`
- Mission: `W2-REV-ACC-24`
- Winning claim: `5297279112`
- Actor/session: `w2-rev-acc-24-gpt56sol-20260814-frontier`
- Trust mode: `DEGRADED_INDEPENDENT`
- Review branch: `planning/issue-326`
- Claim/base main: `db2fbcc2684d257b462715533b9862cde5280534`
- Canonical Planning Program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Producer issue: `#324 / W2-REM-ACC-17`
- Producer winning claim: `5297219148`
- Producer terminal status: `5297275147`
- Producer work/head: `606057016e371fc5a4141037a314cfae5bc8bc79` / `21c6ede8f3f4c4fa2569219cf700b95286ad70ec`
- Producer PR: `#327`, draft at the exact producer head and based on `main@db2fbcc2684d257b462715533b9862cde5280534`
- Producer policy v16 blob: `5e3c932dd34ca81945e345eff30860ade540f2b4`
- Producer report v16 blob: `c2b60278dc5a4e689756d6a73bcbd5dd7f8acad4`
- Producer handoff blob: `25579720efb3b20721d936148e18a6466fce1a15`
- Immutable v15 policy/report inputs: `bba27a68a6922751c4b2c1ccdc3a6c164ac3a2dd` / `b46e924dff194a61993d445ad66cbee5fb79d1df`
- Source review issue/terminal: `#323 / 5297205043`
- Finding under review: `W2-REV-ACC23-M01 / MAJOR / RESOURCE_LOCALIZATION_ADVISORY_PROMOTION`
- Affected atom: `XAG123-MENTAL-HEALTH-RESOURCES`

The claim was immediately re-fetched. Claim `5297279112` precedes later competing claim `5297281840`, so this is the winning ownership generation. The shared review branch was then verified still at the exact claim base before mutation.

## Fresh first-party source re-read

Current first-party Microsoft XAG 123 was independently re-read on `2026-08-14`:

- `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/123`
- title: Xbox Accessibility Guideline 123 — Mental health best practices
- page last updated: `2026-03-04`

The source establishes two distinct semantic levels relevant to this finding:

1. In the Implementation guidelines, applicable games are directed to provide in-game resources that support players with mental-health conditions or help players learn more about mental health. Regional helplines, mental-health websites, and similar resources are examples of what that resource category can include.
2. In the broader approaches section, developers are told to **consider** locale- or region-specific support resources. That locale/region specificity is advisory context, not a second mandatory implementation condition.

The producer correction therefore matches the current source boundary: suitable in-game support/learning resources remain load-bearing; locale/region specificity must not independently reject an otherwise source-faithful candidate. The source remains Xbox accessibility best-practice guidance and does not establish legal/compliance, certification, or `MUST` authority.

## Exact PR and composition attack

PR `#327` contains exactly three changed files:

1. `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`
2. `docs/planning/wave-2/research/accessibility-current-requirements.md`
3. `docs/planning/handoffs/issue-324.md`

The first substantive producer commit `606057016e371fc5a4141037a314cfae5bc8bc79` changes only the policy and report. The producer head adds the handoff. No unrelated repository surface is in the PR.

The v16 policy is an overlay over the exact immutable v15 policy/report blobs. This matters mechanically: the diff replaces the prior overlay's top-level mission/correction metadata because v16 becomes the new overlay, but it explicitly loads exact v15 as its base. Therefore the earlier XAG 122 correction is preserved through composition rather than deleted from the resolved mapping.

The only new material semantic patch is:

```yaml
XAG123-MENTAL-HEALTH-RESOURCES:
  source_id: XAG-123
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: game_contains_content_related_to_mental_health_self_harm_suicide_eating_disorders_addiction_or_other_serious_psychological_risk
  required_semantics:
    in_game_resources_for_support_or_learning_more_available: true
  evidence_requirement_refs:
    - ACC-EV-XAG123
  gap_ref: ACC-GAP-XAG123
```

Compared with the inherited reviewed atom, `resources_localized_or_region_appropriate_when_applicable: true` is removed from `required_semantics`. Atom identity, source id, best-practice authority, `SHOULD` modality, conditional applicability, trigger, evidence route, and gap route remain unchanged.

## Load-bearing witness attack

The v16 validator contract encodes the required source/mechanical boundary and survives adversarial inspection:

- applicable + suitable nonlocalized in-game support/learning resources -> `PASS`;
- applicable + suitable localized/region-specific in-game resources -> `PASS`;
- applicable + no in-game support/learning resources -> `REJECT_REQUIRED_IN_GAME_RESOURCES_MISSING`;
- localization restored to `required_semantics` -> `REJECT_ADVISORY_PROMOTION`;
- authority inflated to `MUST` / compliance -> `REJECT_AUTHORITY_INFLATION`;
- source/identity/trigger/evidence/gap mutation -> `REJECT_SCOPE_LEAKAGE`;
- live helpline identity pinned into the policy -> `REJECT_SCOPE_AND_FRESHNESS_ERROR`.

This closes the exact false-negative reproduced by Issue #323 without creating a false-positive path that permits omission of support/learning resources.

## Preservation attack

The v16 composition contract binds exact v15 inputs and requires every other v15-composed semantic record to remain unchanged. The review found no producer diff that redefines the preserved reviewed lineage:

- XAG 112 navigation corrections;
- XAG 114 `titles` reading-level exception;
- XAG 115 stored-data operator correction;
- XAG 115 permanent-action conjunction correction;
- XAG 115 no-button-hold record;
- XAG 116 reviewed timing correction;
- XAG 117 camera-view required-if-applicable / `SHOULD` correction;
- XAG 120 notification example/feature-existence correction;
- all six XAG 121 atoms accepted by Issue #316;
- XAG 122 no-extra-cost semantics and the named accessible support-method correction reviewed by Issue #321;
- the first five XAG 123 atoms accepted with no material finding by Issue #323.

Issue #323's early-negative boundary is preserved exactly:

- first five XAG 123 atoms: `ACCEPTED_NO_MATERIAL_FINDING_BY_ISSUE_323`;
- `XAG123-MENTAL-HEALTH-RESOURCES`: corrected by v16 and clean in this scoped review;
- `XAG123-WARNINGS-SETTINGS-ACCESSIBLE`: `UNACCEPTED_NOT_REVIEWED_TO_COMPLETION`;
- `XAG123-RESPECTFUL-MENTAL-HEALTH-REPRESENTATION`: `UNACCEPTED_NOT_REVIEWED_TO_COMPLETION`.

The final two atoms were not reviewed to completion here and receive no implicit acceptance.

Declared inventory remains unchanged and internally consistent:

- XAG 112: `14`;
- XAG 114: `16`;
- XAG 108–123: `113`;
- inherited XAG 101–107: `105`;
- composed XAG 101–123: `218`.

No atom/source/evidence/gap identity is added, removed, split, renamed, or rerouted by this bounded correction.

## Authority and fail-closed attack

The exact producer packet preserves:

```yaml
empirical_accessibility_evidence: NOT_RUN
empirical_accessibility_successor_eligible: false
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
production_implementation_ready: false
readiness_authority: NONE
verification_pass_authority: NONE
implementation_authority: NONE
release_authority: NONE
legal_or_compliance_authority: NONE
platform_certification_authority: NONE
decision_authority: NONE
canonicality: NOT_CANONICAL
```

Neither producer `REVIEW_READY` status nor this review grants integration authority. Any integration remains a separate owner-authorized, exact-head, squash-only episode. A later required full-review continuation is still needed for the two unaccepted XAG 123 atoms before an empirical-accessibility successor can become derivable.

## Findings and disposition

Independent/degraded-independent scoped review result for the exact terminal Issue #324 packet:

- unresolved BLOCKER: `0`
- unresolved MAJOR: `0`
- correction-requiring MINOR: `0`
- reviewed finding `W2-REV-ACC23-M01`: `RESOLVED_IN_EXACT_BOUNDED_SCOPE`
- disposition: `CLEAN_FOR_NONCANONICAL_INTEGRATION`

This disposition means only that the exact producer packet may be considered by the separately authorized squash-only noncanonical integration route. It does not accept the final two XAG 123 atoms, make empirical accessibility eligible, set `mapping_complete: true`, close aggregate blockers, or grant readiness, verification-PASS, implementation/release, legal/compliance, platform-certification, decision, integration-by-review, or canonical authority.