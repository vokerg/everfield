# Issue #1613 — Tagged YAML authority / scalar-prose remediation handoff

## Frozen authority
- Mission `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-09`, current task branch `planning/issue-1613`, main base `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.
- Winning schema-3 CLAIM #6101005232, actor `frontier-remediate-1613-gpt6-20261010-2250-01`; first-valid claim immediately rechecked without competitors.
- Canonical #1147 terminal #5675066392; program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Required independent negative reviewer #1610 terminal #6095642373, report blob `9ce72ea3e5f94cb22c16ba45c9694f04585d89d0`, review-only PR #1612 HEAD `0c436b53b804eb34a06239fda03688c86db05414`, **1 BLOCKER FSR-1610-B01 / 1 MAJOR FSR-1610-M01**.
- Frozen predecessor #1608 terminal #6095576264, draft producer PR #1609 HEAD `d65875288d1c4044dd525d8d83ee080e712c9eea`, original v7 Git blob `9711d070abb0849abef9408d9bb6c9c5fa4c4226`; prior source/reviewer PRs remain frozen and unmerged.

## Bounded correction packet (candidate, not terminal approval)
- New `tools/planning/frontier_maintenance_v7.py` blob `c35f895a0121ce329bda6f7220378c9f43e11335` reuses frozen predecessor v7 and changes only the two reviewed trust boundaries plus regression tests.
- FSR-1610-B01: reject unquoted YAML explicit tags, aliases, anchors and merge-key syntax before extracting any source/review/verifier/integrator provenance; ordinary quote-contained representations remain harmless scalar prose.
- FSR-1610-M01: recognize literal and folded YAML scalar blocks (including chomp/indent modifiers, blanks and dedent), exclude their bodies from alias extraction and conditional verifier detection, but detect actual verifier keys following the scalar block.
- Add source-faithful negative fixtures for both explicit-tag shadow spellings, tag-bearing direct aliases, anchor/merge constructs and verifier-key tags, as well as literal/folded verifier-looking prose across modifiers with a following real-verifier positive control.
- Preserve **12 inherited pinned paths** exactly (workflow, v5, v6, nine predecessor handoffs); this v7 plus this handoff yields exactly **14 changed paths** from current main. Pinned thirteen-file source PR tree independently cross-checked against declared Git blob SHAs before rehydration.
- This is a source producer draft, **not** a clean independent review, authorized integration, upgraded canonical binding, implementation readiness, gameplay, truth/consent/accessibility, production or release permission.

## Producer validation evidence and continuation
- First reviewable producer branch HEAD `44d9e639ad7f012f63aad750a11c3daf8bdc2de2` opened draft PR #1614 from unchanged main; fourteen changed paths and twelve inherited exact blob identities confirmed against the frozen #1609 tree.
- GitHub `pull_request` workflow run **38077785086** completed **SUCCESS** on that original code/head. Read-only `validate-pr` job **114288274197** completed PASS: Python `py_compile` and composed `frontier_maintenance_v7.py --self-test` passed all v1–v7 suites, explicitly including FSR-1610 tagged-YAML/block-scalar fixtures, prior escaped-key/quoted-prose, losing-claim/STALE owner and causal-source fixtures. Mutation-capable `maintain` job **114288275179** was **SKIPPED**. Actual CI checkout used `refs/remotes/pull/1614/merge`, result commit `9a50945e52288ae5a2a7801ed60f81eb545dd5c9`.
- This handoff update deliberately creates a **new** branch HEAD; the prior green run is historical only. The final head still requires a fresh read-only PR CI, checkout merge-ref, exact tree/blob, unchanged current-main and owner-lease check before STATUS(REVIEW_READY).
- Recheck exact branch/tree identity, then open a **draft** PR to main as a diff/provenance surface. Obtain **new exact-final-head** pull_request read-only Python compilation and composed v1–v7 self-test PASS with mutation-capable maintenance SKIPPED; examine CI run/jobs/log and actual merge checkout ref.
- Validate all fourteen changed path/blob identities and current-main compatibility, plus real causal implementation source #1545 → verifier #1575 → reviewer #1577 → integrator #1583 and one-parent squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de`.
- Only on successful gate and in-lease current ownership publish exact-head schema-3 `STATUS(REVIEW_READY)`, then materialize a **new genuinely distinct mandatory independent adversarial review**. Any review defect requires bounded successor remediation. Only a *separately* authorized squash-only **NONCANONICAL** integration after clean review is eligible.
- If CI/branch/ownership gates cannot be satisfied, preserve this candidate and record `HANDOFF_READY` instead of asserting review or integration.
