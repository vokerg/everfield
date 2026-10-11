# Issue #1619 — mandatory distinct required reviewer handoff

## Frozen authority and independently verified scope

- Winning first-valid schema-3 CLAIM **6103923116** (GitHub server `2026-10-11T00:50:35Z`, unedited); actor/session `frontier-independent-review-1619-gpt6-20261011-0249-01`, distinct from producer `frontier-remediate-1617-gpt6-20261011-0015-01`. Own branch `planning/issue-1619` starts from `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`; canonical Issue #1147 binding terminal **5675066392** / program `fd4cf1119c3f86acc3af620024eea72235e81ce4` / activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Exact unmodified source #1617 `STATUS(REVIEW_READY)` **6101793350**, source draft PR **#1618** HEAD `e78249c7eb7acd87fa5654875e9d74e208b91159`, v7 blob `9646a8ceca5dfeb56303d10d553e8137500549c3`, own producer handoff blob `280eec55390832f0f0cc0f4af4196b966d72efc3`. Source changed paths: 15, of which 13 are pinned inherited immutable workflow/v5/v6/ten predecessor handoffs. Predecessor source PR #1614 HEAD `faca0341a1d73702bc384f501712a105a97c2f50` and independent negative review-only PR #1616 HEAD `ee8ff112f0c5a7191258c4cccc618593e92b638f` remain frozen.
- Source final-head Actions `pull_request` **38083305896 SUCCESS**, `validate-pr` **114304505452 SUCCESS**, mutation `maintain` **114304506171 SKIPPED**, checkout merge ref `23cb4331faad9bed1ac82256dcb10ce589affbe7`. Producer's success is not an independent review.
- Actual real causal chain #1545 source terminal #6008457546 → #1575 verifier terminal #6008823087 → #1577 reviewer terminal #6009157969 → #1583 integrator terminal #6009230681; real noncanonical single-parent squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de` parent `e51703de82b9df3f5e676663d3a04fdc678bd5c6`.

## Independent negative review and exact files

Disposition **CHANGES_NEEDED: 1 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**, reproducible on the exact frozen final source reader using independent pattern translation and PyYAML 6.0.3 semantic keys:

1. **FSR-1619-B01** — YAML-legal space before colon hides second `extensions : null` after accepted `extensions:` map; source reader trusts first `source_producer_issue: 1545`, while real YAML has `extensions: null`. A direct `verification_issue : 1575` is likewise invisible to conditional `_required_verifier_marker`, despite being a true semantic verifier assertion. Correct or fail closed on all spaced semantic key forms without introducing a universal verifier gate for genuinely verifier-free sources.
2. **FSR-1619-M01** — `canonicality: NOT_CANONICAL` followed by `"canonicality" : CANONICAL` passes `_integration_field` as noncanonical, while PyYAML yields CANONICAL. Reject semantic root authority shadowing across quoted/plain/spacing variants; preserve valid direct declarations and existing escaped/tagged/alias protections.

Full evidence, minimal fixtures, controls, scope and limitations are in **`docs/planning/wave-2/reviews/factory-seeding-frontier-repair-1617-review.md`**. This review branch owns only that report and this handoff. Do **not** modify frozen source, predecessor review PRs, gameplay, canonical program or factory source code on the review branch.

## Review terminal and required continuation

After reviewer-only draft PR to main exists, recheck its exact HEAD, current main compatibility, original source frozen HEAD and source CI, own first-valid unexpired lease, and two exact changed paths. Publish unedited schema-3 `REVIEW_STATUS(CHANGES_NEEDED)` linking report/handoff immutable blob IDs, exact draft PR/head and new mandatory route: `MATERIALIZE_FRESH_BOUNDED_BLOCKING_REMEDIATION_OF_FSR_1619_B01_M01_THEN_EXACT_FINAL_HEAD_READ_ONLY_CI_AND_NEW_DISTINCT_REQUIRED_ADVERSARIAL_REVIEW`.

Materialize **one** fresh bounded blocking remediation successor issue, containing literal two finding reproductions and immutable source identities. New producer must own a separate main-based branch, copy exact pinned #1618 source packet, correct v7 and write new handoff, run final-head nonmutating CI, and route to a **different mandatory independent adversarial reviewer**. Only after a clean required review may a separately owner-authorized current-main compatible **squash-only NONCANONICAL** integration be considered. Review-only draft must remain unmerged. This session claims no source-merge authority, clean review, canonical, gameplay, truth/consent/accessibility, readiness, engine, production or release upgrade.
