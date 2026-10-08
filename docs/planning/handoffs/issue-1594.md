# Issue #1594 — required review handoff

## Ownership and immutable source

- Winning reviewer CLAIM: #1594 comment `6053854593`, actor `frontier-review-verifieralias-1594-gpt56sol-20261008-0825-01`.
- Later duplicate CLAIM `6053862291` is a losing contender under the canonical lowest-valid-comment-ID rule and does not supersede the winning generation.
- Review branch: `planning/issue-1594`, based on `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.
- Active canonical binding: #1147 comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Immutable producer: #1591 terminal `6053794956`; draft PR #1593 frozen HEAD `fa0c552bab1577f088dba271aeebe64f5150b1e0`.
- Producer exact final run: `37737135621`; validate job `113179136786` PASS; maintain job `113179138470` SKIPPED; merge ref `63582c2b828f3c7d52f1ae410d3d92fbfa084e55`.

Reviewer did not mutate producer #1591/#1593, predecessor #1585/#1586, or negative review #1589/#1590.

## Review result

Disposition: **CHANGES_NEEDED**, 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.

**FSR-1594-M01 (MAJOR):** `_consistent_extension_alias()` does not fail closed when a recognized provenance alias is nested under top-level `extensions:` inside a YAML sequence-item mapping (`- alias: value`) or flow mapping (`{alias: value}`). A valid direct alias remains accepted while a contradictory foreign nested occurrence is ignored. The shared schema-3 parser supplies no structural YAML rejection that neutralizes the bypass. This violates the required “direct children of top-level extensions only” rule and leaves FSR-1589-M01 incompletely remediated across source/review/verifier alias families.

**FSR-1594-M02 (MAJOR):** `_valid_owner_terminal()` rejects any later CLAIM/RESUME/RECOVER between the selected owner and terminal, even when that later record is only a losing duplicate. The active canonical program says losing duplicate ownership contenders have zero authority effect and preserves lowest-valid-comment-ID contention. This produces false-negative authority/liveness for otherwise valid producer/reviewer/verifier/integrator terminals and can suppress the newest implementation source.

Verifier causality itself was independently rechecked against the real #1545/#1575/#1577/#1583 provenance chain and no additional material finding was identified.

## Required continuation

Create a bounded blocking remediation from current main; do not mutate frozen PR #1593. Replace or augment regex-only placement detection so **every** occurrence of recognized provenance aliases fails closed unless it is exactly one non-null direct scalar child of the sole top-level `extensions:` mapping. Also reconstruct effective owner generations so losing duplicate CLAIM/RESUME/RECOVER contenders do not invalidate the canonical winner, while genuinely winning later generations still displace stale owners. Add source/review/verifier sequence-item and flow-map nested fixtures plus first-winner/losing-duplicate ownership fixtures across producer/reviewer/verifier/integrator paths. Preserve legitimate direct aliases, run fresh exact-head read-only compile/composed v1-v7 tests with mutation skipped, then route a **new distinct required adversarial review**.

No integration, canonicality, gameplay/truth/consent/accessibility/readiness/production/release authority is conveyed by this handoff.
