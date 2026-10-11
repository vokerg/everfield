# Issue #1664 — bounded factory parser remediation

- Mission: `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-16`.
- Status: IN_PROGRESS / SOURCE DRAFT. No source terminal, independent review, integration, canon or readiness authority yet.
- First winning schema-3 CLAIM: Issue #1664 comment #6112347851; actor `frontier-remediate-1664-gpt6-20261011-2040-cph-01`.
- Current-main baseline: `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`; canonical Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af` ancestor.
- Mandatory negative distinct review: Issue #1661 terminal #6112258067; frozen reviewer-only draft PR #1663 HEAD `68b0d7094cfe2bb1b76c3d307150f8c4c086a555`, 1 BLOCKER FSR-1661-B01 and 1 MAJOR FSR-1661-M01.
- Frozen immediate producer: Issue #1656 terminal #6109748773, draft PR #1660 HEAD `3d5ebe385d4af096e04520fb3977d3e900bac87b`; prior base parser Git blob `2a8bbc64d200ffa2ac4711ea0dbdf8a7c070ed33`.

## Changes and scope

Inherit exactly 20 upstream files from frozen PR #1660 unchanged (19 prior inherited paths plus predecessor handoff). Correct only `tools/planning/frontier_maintenance.py`, expected blob `1a4774f894d18f5df11fccbf0d29792ad157e81e`, and add this task's handoff. This yields 22 changed paths, with no gameplay, engine, canon, original source, or review-PR modifications. Earlier v5-v7 scripts and workflow are byte-identical.

### FSR-1661-B01

Added a whole-document, intentionally restricted YAML structure validator before root scalar and list extraction. Reject partial/invalid flow sequences, flow mappings, indented descendants beneath non-container values, inconsistent/nested list structures, complex/shadow fields, and unsupported YAML syntax rather than extracting apparent authority from malformed text. Retain root indented/flow scalar lists and existing root scalar non-list rejection; use same parser at v7 source/reviewer/verifier `artifact_paths` consumers.

### FSR-1661-M01

A changed observed SHA alone never renews the ownership lease. `HEAD_ADVANCE` needs an explicit verifier; the live maintenance consumer supplies an authenticated GitHub task-branch tip read, true old-to-new compare/ancestry, and commit timestamp check. Unknown/expired/drifted head state fails closed. No verifier (e.g. standalone reconstruction) means no HEAD_ADVANCE renewal. The production helper cannot prove historical reflog states and intentionally rejects old head movement when live tip differs.

## Checks / next steps

- New in-module positive and negative fixtures exercise malformed source/review/verifier list, owner invalid YAML EVIDENCE, forged no-proof HEAD_ADVANCE, and mocked authenticated branch movement.
- Real final-head hosted CI **pending**. Do not assert PASS based on authored fixtures; confirm read-only `pull_request` Python compilation and composed v1–v7 self-tests, mutation-capable `maintain` SKIPPED, actual checkout ref and unchanged main.
- If CI fails, correct only the owned parser/handoff on this branch and rerun at exact final HEAD. If CI passes, record unedited current-owner schema-3 `STATUS(REVIEW_READY)` with exact draft PR/head and materialize one **new genuinely distinct required adversarial review**. Neither author nor this PR may self-approve or merge.
- Only a later independently authorized current-main-compatible squash-only **NONCANONICAL** source publication following a clean distinct review is eligible; all predecessor and reviewer-only PRs remain frozen unmerged.
