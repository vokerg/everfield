# Issue #1606 — required independent adversarial review

## Verdict and authority

CHANGES_NEEDED — **1 BLOCKER, 1 MAJOR, 0 correction-requiring MINOR**. Do not integrate frozen source PR #1605. Mandatory distinct reviewer actor: frontier-required-review-1606-gpt6-20261010-0953-01. Winning unedited first CLAIM #6095347224 at 2026-10-10T07:55:45Z, later losing CLAIM #6095348144 at 07:55:48Z. This reviewer did not produce Issue #1604 source; producer actor is frontier-remediate-1604-gpt6-20261010-0944-01. Reviewer branch planning/issue-1606 starts from main 3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d.

Canonical Issue #1147 terminal #5675066392; program blob fd4cf1119c3f86acc3af620024eea72235e81ce4; ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af. Source Issue #1604 terminal #6095298553; frozen open draft PR #1605 HEAD ae726710cd11d7081f3b7bc7d271b3c2004bf5da; v7 blob 7ba46460a96d581da7d3b8605d33b8754555065a.

## FSR-1606-B01 — BLOCKER: escaped quoted YAML mapping key substitutes another authority identity

Frozen v7 _consistent_extension_alias at lines 224–286 counts and validates only literal plain, single-quoted or double-quoted mapping-key spellings. Valid double-quoted YAML keys may contain escape sequences and *decode to the same key*. The scanner misses these equivalent keys, trusts earlier authority, and disagrees with actual YAML semantics.

Independent Python reproduction using exact frozen source logic for _yaml_without_comment, _yaml_alias_scalar and _consistent_extension_alias, cross-checked using yaml.safe_load, gave three negative cases: source reader **returns 1545** in all three despite semantically shadowed/contradictory source identity (expected REJECT / None).

~~~yaml
# A — second top-level extensions key decodes to extensions
extensions:
  original_source_issue: 1545
"exten\u0073ions": null
~~~

PyYAML result: {'extensions': None}. The scanner ignores the valid escaped second header and authenticates nonexistent original provenance.

~~~yaml
# B — second direct alias decodes to original_source_issue
extensions:
  original_source_issue: 1545
  "original_source_issu\u0065": 1559
~~~

PyYAML result: {'extensions': {'original_source_issue': 1559}}. Reader still trusts 1545.

~~~yaml
# C — second direct alias nulls original source identity
extensions:
  original_source_issue: 1545
  "original_source_issu\u0065": null
~~~

PyYAML result: {'extensions': {'original_source_issue': None}}. Reader still trusts 1545.

This is a source/reviewer/verifier/integrator causal identity spoofing risk, not a cosmetic parsing mismatch. Existing ordinary duplicate/null checks do not guard escaped-equivalent map/alias keys. Repair must use a genuinely structural key decoder/canonicalizer or reject escaped mapping keys throughout authority capsules before accepting any provenance. Accept valid plain or ordinary quoted/commented direct scalar declarations without allowing semantically duplicated, null, foreign, nested, flow or shadowed aliases.

## FSR-1606-M01 — MAJOR: verifier marker matches quoted prose, inventing scoped verification requirement

Frozen _required_verifier_marker lines 782–820 uses a raw fallback key regex with a comma or left-brace prefix, scanning lines without quote context. Actual quoted prose (not a YAML verifier mapping key) therefore activates the conditional verifier gate:

~~~yaml
extensions:
  note: "ordinary, independent_verifier_issue: 1575"
~~~

~~~yaml
extensions:
  note: "illustration {independent_verifier_issue: 1575}"
~~~

Independent execution of the exact source regex returned True for both lines; the actual direct key independent_verifier_issue: 1575 also returns True (correct). For a source contract whose required_next_route does not require verification, innocent quoted explanatory prose triggers _exact_required_verifier with missing real verifier provenance and rejects an otherwise valid scoped integration source. A proper structural key scan must recognize valid quoted direct verifier keys and fail closed on real malformed/foreign ones, while excluding ordinary quoted prose. Do not add a blanket verifier gate beyond the effective task contract.

## Independently exercised positive and negative controls

- Plain extensions map/direct source ID 1545 accepted. Commented extensions header and ordinary double-quoted key/value accepted.
- Ordinary quoted direct aliases individually accepted: original_source_issue=1545, original_source_pr_number=1568, independent_verifier_issue=1575, source_verifier_pr=1576, required_independent_review_issue=1577, disposition=CLEAN_FOR_TEST, result=PASS and blocker_count=0. The corrected _extension_field delegates to the structural alias reader, resolving prior false-negative in ordinary quoted/commented map headers.
- Plain duplicate header, repeated direct alias, null alias, sequence scalar, nested-only alias, and flow header correctly rejected. These positive improvements are not sufficient against escaped equivalent keys.
- The ended owner-generation code includes prefix-recursive earlier terminal validation, distinct handoff/recovery and six-hour lease conditions. It was inspected statically together with successful authored regressions; no independently replayed complete owner-generation state-machine suite is claimed.
- Independently re-fetched unedited original chronology: #1545 STATUS(REVIEW_READY) terminal #6008457546 at 2026-10-06T03:02:14Z → distinct verifier #1575 VERIFICATION_STATUS(DONE) #6008823087 at 03:37:24Z → distinct reviewer #1577 REVIEW_STATUS(REVIEW_READY) #6009157969 at 04:10:25Z → integrator #1583 INTEGRATION_STATUS(DONE) #6009230681 at 04:17:26Z; original source PR #1568 HEAD 1de1155429bfa657dd6e60c4f5abc969fabd86d5, one-parent squash ef75cc78a217695097f5d8f6cfb48ea04beaa7de, parent e51703de82b9df3f5e676663d3a04fdc678bd5c6. Plain-header actual provenance is not retrospectively invalidated. Preserve scoped v5 2-/3-target and v6 bounded successor/no-global-gate behavior.

## Exact branch isolation and CI

GitHub PR #1605 paginated files: exactly twelve allowed paths, all blob IDs match the immutable source issue #1606 contract:
- Workflow .github/workflows/planning-frontier-maintenance.yml 999671d1ede00a25c66bd63d25bcdc14e4a9d40b; v5 babdd29389e06bc922d33bc285c82315fec8c237, v6 da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03, v7 7ba46460a96d581da7d3b8605d33b8754555065a.
- Handoffs #1556 ea2fce80a21d932a0f8f41d261abd85aa814775a, #1570 98744c4c302a4abca7e67d36301acf6ee16b5e6d, #1579 06b2ab2ff4d3a09778de4809f77edd6d5f47684a, #1585 53422ac29b568f42edc16d30488be744c5f273c2, #1591 3908f26b92cccd77b9ad65e2fab8ecc130062e51, #1596 b74e545b7f99b24ab8d0be391124f787666d8ff5, #1600 1c6989faa5f925f5c3efb1f47a8a8f5c4a747af9, #1604 501c7604c5fe32d4548335c0b21bff95e9c99d1b.
- Earlier producer PR #1601 HEAD ddd695c42f99805100430e494cfa72db9f12c2f8 and negative review PR #1603 HEAD 078fded824af53f6188627b7395db6c626f79556 remain unchanged and unmerged.

Independently inspected GitHub Actions exact-head pull_request run #38035703053, validate-pr job #114165553037 SUCCESS and mutation-capable maintain job #114165553731 SKIPPED. Read-only logs show checkout refs/remotes/pull/1605/merge, merge ref b1bd6627ef297f692e0d832d7508cb85b269b5bb merging ae726710cd11d7081f3b7bc7d271b3c2004bf5da into current main 3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d; py_compile and v1–v7 composed authored tests PASS. Those tests omit the independently demonstrated escaped-key spoof and prose false-positive.

## Next required route

Publish this report and issue-1606 handoff on an own review-only branch as an open draft review-only PR to main before a schema-3 current-owner REVIEW_STATUS(CHANGES_NEEDED). Terminal must bind exact reviewer PR/head, report/handoff blobs, frozen source #1604 PR #1605/head, exact GitHub evidence, 1 BLOCKER + 1 MAJOR + 0 correction MINOR. No source or review PR integration.

Materialize a fresh bounded **mandatory blocking remediation** for FSR-1606-B01/M01. Keep all frozen predecessors immutable, rehydrate the reviewed 12-path packet into a new main-based branch while changing only corrected v7 plus new handoff. Require independent adversarial escaped/duplicate YAML key fixtures and quoted prose/directed verifier marker fixtures, exact-head read-only CI with mutation job skipped, and another genuinely distinct mandatory required review. Clean review alone grants no integration. Only separately owner-authorized exact-current-main-compatible **squash-only NONCANONICAL** source publication may follow clean required review. No gameplay, canon, truth, consent, accessibility, readiness, production or release authority upgrade.
