# Issue #1610 — mandatory independent adversarial review of #1608

## Disposition, ownership and frozen source

**CHANGES_NEEDED — 1 BLOCKER (FSR-1610-B01), 1 MAJOR (FSR-1610-M01), 0 correction-requiring MINOR.** The frozen source PR #1609 has successful producer CI but remains ineligible for integration. This report is independent review evidence, not verification or integration authority.

Genuinely distinct reviewer episode and actor frontier-required-review-1610-gpt6-20261010-1017-01, not source #1608 producer actor frontier-remediate-1608-gpt6-20261010-1004-01. Reviewer first-valid unedited CLAIM GitHub #6095605108, created 2026-10-10T08:18:11Z (updated same), immediately checked no competing CLAIM. Own branch planning/issue-1610 created at main 3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d. Canonical binding Issue #1147 terminal #5675066392, program blob fd4cf1119c3f86acc3af620024eea72235e81ce4, activation ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af.

Frozen source Issue #1608 owner CLAIM #6095497123, HEAD_ADVANCE #6095571447, unedited STATUS(REVIEW_READY) terminal #6095576264 at 2026-10-10T08:14:19Z, PR #1609 exact HEAD d65875288d1c4044dd525d8d83ee080e712c9eea, v7 source blob **9711d070abb0849abef9408d9bb6c9c5fa4c4226**. Existing prior negative review #1606 terminal #6095445194, predecessor source #1604 PR #1605 HEAD ae726710cd11d7081f3b7bc7d271b3c2004bf5da, reviewer PR #1607 HEAD 41b3c3901ffd9f9e1dc398f2303bdb9a1d8cebcf, and all other previous PRs remain frozen. There is only one current review mission route: Issue #1610. A later duplicate Issue #1611 was closed with state_reason duplicate without a CLAIM or review branch; it does not confer review or ownership authority.

## FSR-1610-B01 — BLOCKER: explicit YAML tag shadows trusted extensions mapping

Frozen source v7 _yaml_mapping_structure (lines 203–260) rejects YAML explicit complex-key markers that start with ? and escaped double-quoted mapping keys. _consistent_extension_alias (lines 283–353) nevertheless counts only top-level literal plain/single/double-quoted extensions: headers. A **valid explicitly tagged YAML mapping key** decoding to extensions bypasses that header cardinality check and shadows the first mapping. Its key contains no backslash and does not use ?, so both newly added guards are ineffective.

Independently transcribed and executed the frozen _yaml_without_comment, _yaml_mapping_structure, _yaml_alias_scalar and _consistent_extension_alias functions with source-accurate regex/branches, and cross-checked semantic parsing using PyYAML safe_load. The following two capsules caused the frozen authority reader to **return 1545** (TRUST), while the actual parsed document replaces the extensions map with null (expected FAIL CLOSED / None):

~~~yaml
# A — standard YAML !!str explicit scalar tag
extensions:
  original_source_issue: 1545
!!str "extensions": null
~~~

Actual PyYAML mapping: {'extensions': None}.

~~~yaml
# B — explicit full standard YAML tag
extensions:
  original_source_issue: 1545
!<tag:yaml.org,2002:str> extensions: null
~~~

Actual PyYAML mapping: {'extensions': None}.

The same explicit-tagged extensions key can shadow with another mapping. This is the same causal **source provenance spoof** class as FSR-1606-B01, now via standard YAML tagging rather than escaped-key syntax; the corrected code only rejects one lexical representation. There is no basis to treat a first map as authoritative when another YAML-valid key of the same semantic identity overrides it. Remedy: use a constrained structural YAML parser/key normalizer or unconditionally reject explicit tag constructs anywhere in authority capsules before recognizing the first source/review/verifier/integrator alias. Preserve ordinary accepted direct scalar keys/comments and reject semantic duplicates, flow and null source identity.

## FSR-1610-M01 — MAJOR: YAML block-scalar text misread as verifier field

The source _required_verifier_marker (lines 849–901) now masks inline quoted prose using _yaml_mapping_structure, addressing previous FSR-1606-M01. However it parses **each physical line independently** and does not track the YAML block scalar indicator | or >. A line inside an ordinary block scalar can resemble an indented verifier mapping key even though the parsed YAML has only the harmless note scalar.

Independent source-faithful execution of the marker returned **True** for both innocent blocks below. Actual PyYAML result for each is {'extensions': {'note': '<ordinary text>'}}, with no verifier alias key anywhere.

~~~yaml
extensions:
  note: |
    independent_verifier_issue: 1575
~~~

~~~yaml
extensions:
  note: >
    source_verifier_pr: 1576
~~~

If the genuine source contract does not call for verification, the false marker activates _exact_required_verifier without a verifier ID/terminal/PR/head, thereby rejecting valid scoped integration. Never create a global verification gate from ordinary scalar content. A multiline/block-aware structural parser (or conservative documented rejection of multiline scalar forms before passing any authority) must distinguish real mapping keys from block prose while retaining fail-closed handling of foreign/malformed/escaped verifier assertions.

## Independent controls and regression context

- Control ordinary plain extensions / original_source_issue 1545 returned 1545, marker false.
- Previous escaped YAML duplicate top-level key was now rejected by _consistent_extension_alias and produced marker true if decoded to extensions: the prior B01 escape regression is fixed. Ordinary quoted inline note containing comma and verifier-looking text now marker false: prior M01 inline-prose regression is fixed.
- Valid directly scoped independent_verifier_issue 1575 marker true; plain duplicate/flow/null and quoted/commented key fixture behavior was also inspected in source and producer-authored CI. A nested or fake block scalar must not authorize any verifier. The producer-authored tests do not exercise the independent **tagged mapping key** or **block scalar** cases above.
- Frozen owner _valid_owner_terminal contains prefix-recursive validation of already ended generations and separate HANDOFF/STALE pathways, checked structurally together with authored losing-owner fixtures. No claim of independently replaying every complete ownership fixture or GitHub write is made.
- Independently re-fetched actual GitHub operational chronology: source #1545 STATUS(REVIEW_READY) terminal #6008457546 at 2026-10-06T03:02:14Z; distinct verifier #1575 VERIFICATION_STATUS(DONE) terminal #6008823087 at 03:37:24Z; required reviewer #1577 REVIEW_STATUS(REVIEW_READY) terminal #6009157969 at 04:10:25Z; owner integrator #1583 INTEGRATION_STATUS(DONE) terminal #6009230681 at 04:17:26Z. Original source PR #1568 HEAD 1de1155429bfa657dd6e60c4f5abc969fabd86d5 was published as genuine single-parent squash ef75cc78a217695097f5d8f6cfb48ea04beaa7de with parent e51703de82b9df3f5e676663d3a04fdc678bd5c6. None of these plain-header historic records is retrospectively invalidated by prospective counterexamples. Preserve v5 two-/three-target and v6 bounded/no-global-gate semantics.

## Frozen PR, actual read-only CI and permitted paths

Independently inspected PR #1609 exact thirteen GitHub changed-file paths and matching Git blob IDs: workflow .github/workflows/planning-frontier-maintenance.yml 999671d1ede00a25c66bd63d25bcdc14e4a9d40b; v5 babdd29389e06bc922d33bc285c82315fec8c237; v6 da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03; v7 9711d070abb0849abef9408d9bb6c9c5fa4c4226; handoffs #1556 ea2fce80a21d932a0f8f41d261abd85aa814775a, #1570 98744c4c302a4abca7e67d36301acf6ee16b5e6d, #1579 06b2ab2ff4d3a09778de4809f77edd6d5f47684a, #1585 53422ac29b568f42edc16d30488be744c5f273c2, #1591 3908f26b92cccd77b9ad65e2fab8ecc130062e51, #1596 b74e545b7f99b24ab8d0be391124f787666d8ff5, #1600 1c6989faa5f925f5c3efb1f47a8a8f5c4a747af9, #1604 501c7604c5fe32d4548335c0b21bff95e9c99d1b, #1608 0bd30ad725665ea34997f14280a8c1728409ef51. No game/ paths.

Actual pull_request GitHub Actions run **#38037085851** at source HEAD d65875288d1c4044dd525d8d83ee080e712c9eea completed SUCCESS. Raw logs independently fetched: read-only validate-pr job #114169662986 SUCCESS, checkout refs/remotes/pull/1609/merge at merge ref ab16750689532b148f2dc81029e0fcf778f8c3f1 merging exact source HEAD into current main 3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d, actual py_compile and composed v1–v7 self-tests PASS. Mutation-capable maintain job #114169663835 SKIPPED. This is necessary source evidence but not a substitution for independent required review.

## Required successor and no-authority boundaries

Required REVIEW_STATUS(CHANGES_NEEDED): **1 blocker, 1 major, zero correction-requiring minor**. Own reviewer branch may add **only** docs/planning/wave-2/reviews/factory-seeding-frontier-repair-1608-review.md and docs/planning/handoffs/issue-1610.md, then open an own review-only **draft PR** to main *before* terminal. Terminal binds winning current owner, exact source #1608 terminal #6095576264/PR #1609/head, reviewer PR/head, immutable report/handoff Git blobs, actual GitHub CI and negative independent findings.

Materialize a bounded mandatory blocking-remediation successor for FSR-1610-B01/M01; keep all predecessor source/reviewer branches frozen, rehydrate source's 13-path packet from freshly derived main with **only corrected v7 plus own successor handoff**, require independent explicit-tag/block scalar/adversarial fixture evidence, exact-head read-only GitHub CI with maintain SKIPPED and a **new genuinely distinct mandatory independent adversarial review**. No source or review PR integration may occur on this negative finding. Only separately owned, genuinely clean required-reviewed, exact-current-main compatible **squash-only NONCANONICAL** source publication may follow. No canonical/gameplay/truth/consent/accessibility/implementation-readiness/production/release upgrade; do not invent global gates against unrelated scoped work.
