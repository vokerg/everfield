# Issue #1604 — Blocking remediation handoff

**Mission:** `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-07`  
**State:** bounded producer remediation candidate; final owner status and exact-head CI evidence are authoritative only when published on Issue #1604.  
**Current main / branch base:** `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`  
**Canonical binding:** Issue #1147 terminal `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.  
**First-valid own CLAIM:** #6095245148 (2026-10-10T07:44:24Z), actor `frontier-remediate-1604-gpt6-20261010-0944-01`. Immediately rechecked: no competing owner. Own branch `planning/issue-1604`.

## Prerequisite and scope

Mandatory distinct required independent negative review #1602 terminal `6095224297`, review-only draft PR #1603 HEAD `078fded824af53f6188627b7395db6c626f79556`, reviewed source Issue #1600 terminal `6093645375`, frozen draft source PR #1601 HEAD `ddd695c42f99805100430e494cfa72db9f12c2f8`. Negative report blob `643394179a7162fb3f28dd4d1d7be4f673a6892f`: **1 BLOCKER, 2 MAJOR**.

- **FSR-1602-B01:** reject any second/shadow top-level `extensions` key, including null, flow, sequence, quoted and commented versions, independently of the scalar alias being read.
- **FSR-1602-M01:** use the same strictly scoped direct-child reader for disposition, result and counts; accept legal quoted/commented headers and direct quoted scalar values, rejecting duplicate/nested/foreign/flow/null placements.
- **FSR-1602-M02:** quoted explicit verifier identity keys must activate conditional authentication, including malformed/shadow/foreign verifier assertions failing closed, with no universal verifier requirement for genuinely unscoped paths.

Rehydrate the exact eleven-path frozen source packet with inherited workflow `999671d1ede00a25c66bd63d25bcdc14e4a9d40b`, v5 `babdd29389e06bc922d33bc285c82315fec8c237`, v6 `da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03`, inherited handoffs #1556 `ea2fce80a21d932a0f8f41d261abd85aa814775a`, #1570 `98744c4c302a4abca7e67d36301acf6ee16b5e6d`, #1579 `06b2ab2ff4d3a09778de4809f77edd6d5f47684a`, #1585 `53422ac29b568f42edc16d30488be744c5f273c2`, #1591 `3908f26b92cccd77b9ad65e2fab8ecc130062e51`, #1596 `b74e545b7f99b24ab8d0be391124f787666d8ff5`, #1600 `1c6989faa5f925f5c3efb1f47a8a8f5c4a747af9`. Replace only v7 blob `af7f04e9387e06c2f48daf5002566c678f9fd347` with corrected candidate blob `7ba46460a96d581da7d3b8605d33b8754555065a` and add this own handoff as twelfth path. No gameplay, canonical, implementation-readiness or production changes.

## Evidence and terminal gates

The corrected v7 code includes fresh adversarial executable fixtures for duplicate/shadow maps, valid quoted/commented headers, disposition/count scalar extraction, hostile nested/duplicate/null values and quoted verifier identity activation, alongside inherited ended-owner / HANDOFF / STALE / real published source / bounded v5-v6 tests. These authored tests **do not** substitute for a distinct required independent review.

Before terminal STATUS(REVIEW_READY), independently confirm the exact final changed-path/blob list, own draft PR to main, exact-final-HEAD GitHub pull_request read-only compile/composed v1-v7 test success, skipped mutating maintain job, checkout merge ref referencing this exact head and current main, and predecessor immutability. If any fails, record blocking state instead of claiming readiness. Only after these gates may the owner publish a six-hour-valid terminal and create a **new genuinely distinct mandatory independent adversarial review**. No self-review, source/review integration or canonicality is authorized. Separately eligible, explicitly authorized source publication, if later permitted after a clean required review, must be squash-only and NONCANONICAL.
