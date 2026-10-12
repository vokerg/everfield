# Issue #1608 — Escaped YAML mapping-key and scoped verifier-prose remediation

- Mission: `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-08`; own branch `planning/issue-1608`, based on current main `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.
- Canonical binding: #1147 terminal #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- First valid owner CLAIM: #1608 comment **6095497123**; actor `frontier-remediate-1608-gpt6-20261010-1004-01`; first-owner recheck: no competing lower valid claim.
- Activation: required distinct negative review #1606 terminal **6095445194**, review-only PR #1607 HEAD `41b3c3901ffd9f9e1dc398f2303bdb9a1d8cebcf`. **1 BLOCKER (FSR-1606-B01), 1 MAJOR (FSR-1606-M01)**.
- Frozen predecessor producer: #1604 terminal #6095298553, draft PR #1605 HEAD `ae726710cd11d7081f3b7bc7d271b3c2004bf5da`, original v7 blob `7ba46460a96d581da7d3b8605d33b8754555065a`. Do not mutate predecessor heads, main or the canonical program.

## Corrective candidate

- Replacement `tools/planning/frontier_maintenance_v7.py`: Git blob **`9711d070abb0849abef9408d9bb6c9c5fa4c4226`**.
- FSR-1606-B01: lexical YAML mapping scanner preserves real quoted keys but masks quoted scalar values; escaped double-quoted mapping-key tokens are conservatively rejected before *any* authority can be authenticated, including duplicate/overwriting `extensions` and aliases.
- FSR-1606-M01: verifier gate scans structural mapping-key tokens only; escaped real verifier assertions still activate fail-closed authentication, whereas prose in quoted scalar fields does not.
- Additional pre-terminal structural regression covers YAML explicit complex-key shadows (`?` key with a following-line colon) that can overwrite `extensions` or an alias. The amended exact head requires fresh PR CI.
- Independent negative controls now include escaped `extensions`, directly escaped alias duplicates with conflicting/same/null values, nested/flow variants, escaped verifier keys, several quoted prose values, and legal commented/quoted direct aliases. The existing full v1–v7 composed suite and real #1545→#1575→#1577→#1583 causal route remain required.

## Exact bounded packet and gates

- Rehydrate the 11 pinned inherited source paths from #1605 unchanged: maintenance workflow/v5/v6 and eight preceding handoffs (#1556, #1570, #1579, #1585, #1591, #1596, #1600, #1604); replace only v7 and add this handoff (13 paths total).
- New draft producer PR is a review/provenance surface, **not integration authority**.
- Before owner terminal `STATUS(REVIEW_READY)`, independently inspect exact-final-head GitHub `pull_request` CI: Python compile plus composed v1–v7 tests PASS; mutation-capable `maintain` job SKIPPED; actual checkout merge ref; 13 exact path/blob identities and then-current-main compatibility.
- After eligible producer terminal, require a **genuinely distinct mandatory independent adversarial review**. Negative findings require another bounded remediation; only a separately authorized clean-reviewed exact-current-main-compatible **squash-only NONCANONICAL** source integration is possible.
- No gameplay, truth/consent/accessibility, canonicality, engine selection, readiness, production, release, review, verification or integration authority is conferred by this working candidate.

## Continuation

Inspect this branch, exact Git tree and PR CI, exercise further adversarial fixtures. If validation fails, correct only this branch, rerun exact-final-head CI, and record any blocker honestly. Preserve predecessor PRs unchanged.
