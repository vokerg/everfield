# Issue #1596 — Factory seeding frontier repair REM-05

## Scope and authority
Required **blocking remediation** of #1594 terminal REVIEW_STATUS(CHANGES_NEEDED) comment `6054099880`: FSR-1594-M01 (nested/flow provenance keys bypass placement validation) and FSR-1594-M02 (losing duplicate owner contenders falsely displace a valid generation). This remains a **NONCANONICAL producer**. No integration, source review, verification, gameplay, implementation-readiness, truth, consent, accessibility, release, or production authority is conferred.

## Canonical binding and owner
- Current main at claim: `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.
- Canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`, Issue #1147 terminal binding comment `5675066392`; canonical activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- First valid owner CLAIM: #1596 comment `6076667400`, actor `frontier-remediate-1596-gpt6-20261009-1140-01`. Recheck after claim found no other owner.
- HEAD_ADVANCE: #1596 comment `6076744447`; independent branch `planning/issue-1596`.
- Source issue #1591 terminal `6053794956`, frozen draft PR #1593 HEAD `fa0c552bab1577f088dba271aeebe64f5150b1e0`. Negative independent review #1594 draft PR #1595 HEAD `6cc2a06914548e71fdaf3c4bf7af9d3d855c24be`. Neither branch was modified.

## Exact inherited packet
Rehydrated exact source blobs (unchanged) on a new branch from current main:
- `.github/workflows/planning-frontier-maintenance.yml`: `999671d1ede00a25c66bd63d25bcdc14e4a9d40b`.
- `tools/planning/frontier_maintenance_v5.py`: `babdd29389e06bc922d33bc285c82315fec8c237`.
- `tools/planning/frontier_maintenance_v6.py`: `da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03`.
- `docs/planning/handoffs/issue-1556.md`: `ea2fce80a21d932a0f8f41d261abd85aa814775a`.
- `docs/planning/handoffs/issue-1570.md`: `98744c4c302a4abca7e67d36301acf6ee16b5e6d`.
- `docs/planning/handoffs/issue-1579.md`: `06b2ab2ff4d3a09778de4809f77edd6d5f47684a`.
- `docs/planning/handoffs/issue-1585.md`: `53422ac29b568f42edc16d30488be744c5f273c2`.
- `docs/planning/handoffs/issue-1591.md`: `3908f26b92cccd77b9ad65e2fab8ecc130062e51`.

Only `tools/planning/frontier_maintenance_v7.py` is substantively changed (corrected blob `97161ea4c2c9ce1173eea987f3f6568f914295ee`) and this handoff is newly created.

## Corrections and independent review risks
- **M01:** `_consistent_extension_alias` now scans provenance mapping-key tokens throughout the YAML capsule (including `- key:` and `{key: value}` structures), accepting only one scalar direct child inside the sole top-level `extensions:` mapping per recognized key. Foreign, nested, null, collection, duplicated and disagreeing aliases fail closed, including when values agree with the direct alias. Added direct-accepted and sequence/flow/duplicate/null/foreign adversarial assertions. The real direct-extension #1583 provenance remains accepted.
- **M02:** `_valid_owner_terminal` reconstructs the effective generation from first valid CLAIM and first valid mature STALE intents and grants through the terminal prefix, not from every ownership-shaped record. Losing duplicate CLAIM/RECOVER/RESUME are inert. Added producer, reviewer, verifier and integrator first-winner duplicate tests; recovered producer plus losing contenders; valid later generation displacing stale prior-owner terminal; premature STALE grant fails to displace first owner. HANDOFF/ORPHAN without complete declared proof remain conservative fail-closed and do not gain inferred ownership authority.
- Required adversarial reviewer should challenge YAML placement scanner lexical edge cases, full schema-3 recovery winner semantics, genuine handoff transitions, causal source/provenance verifier chain #1545→#1575→#1577→#1583, and unsafe false positives/negatives. Authored tests do not substitute for independent review.

## Evidence and status at handoff commit
- Draft producer PR #1597, initial code HEAD `ae2a6ac8bb3a2ceb36bf8795a1d51d3d9cb05fc6`.
- Initial code-head PR Actions run `37901055665`, `validate-pr` job `113723457242` **PASS**, `maintain` job `113723458701` **SKIPPED**.
- Job checkout actual PR merge ref `5f8ca9db878be9a720adc4fa0c53c76830a3f544` = code HEAD into `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`; py_compile and all composed v1–v7 self-tests PASS including M01/M02 fixtures.
- Initial PR nine changed paths match inherited packet; final ten paths will include this handoff.
- **Do not treat initial code-head CI as final-head CI.** Recheck HEAD/main/PR changed paths, verify new exact final-head pull-request job, mutating job SKIPPED, and publish terminal producer REVIEW_READY only if every gate is met. Then require a distinct independently owned mandatory adversarial review before any separately authorized squash-only NONCANONICAL publication.

## Continuation
The owning actor should finalize exact-head read-only validation and durable terminal status against PR #1597. Any code change after this handoff requires a new exact-head CI and a new independent-review scope. The open draft PR is for visibility only; no merge before a clean distinct required review and separate integration authority.
