# Issue #1747 — authenticated transition-wrapper-owner correction

**Mission:** `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-23`.  
**Owner CLAIM:** #6138253126, immutable GitHub server time 2026-10-13T04:29:41Z, actor `everfield-existing-pr-transition-wrapper-remediate-1747-gpt6-20261013-cph-01`. First valid claimant, immediately reread and uncontested.  
**Main parent:** `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`. **Canonical:** Issue #1147 INTEGRATION_STATUS(DONE) #5675066392, program Git blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.  
**Status:** Bounded source correction candidate **NOT REVIEWED, NOT INTEGRABLE**; hosted CI and fresh mandatory independent security review required. Noncanonical and no authority for live factory mutation, integration, release, or production.

## Exact frozen source and independent finding

- Original protected source Issue #1740, schema-3 owner `STATUS(REVIEW_READY)` #6138019245; existing frozen OPEN/DRAFT PR #1744 exact HEAD `f2acdb1d7c81d08ce192bf86c4ee55e63a4b8826`, 29 changed files, prior v4 blob `50e3586dd1135c277e808572cc65cc4e9c6a0277`, hosted full read-only CI #38344794933 success, mutation-only job SKIPPED.
- Genuinely distinct required independent negative review Issue #1745, terminal `REVIEW_STATUS(CHANGES_NEEDED)` #6138128407, finding **FSR-1745-M01 (MAJOR)**, reviewer-only OPEN/DRAFT PR #1749 HEAD `3460edb176261fc84e88e6d8a0b3c96755fa5c2e`. Keep this review evidence-only PR unmerged.
- Defect: the frozen v4 wrapper used only `base.reconcilable_terminal_from_comments` plus valid result SHAs, which cannot prove that the *wrapper* status came from a first-winning current schema-3 owner with an unexpired six-hour GitHub lease. A losing claimant or seven-hour-old terminal could consume a source generation despite a genuine linked successor. The earlier FSR-1733-M01 fix protects only the successor terminal, not wrapper authority.

## Exclusive corrective packet

Fresh `planning/issue-1747` is based on the exact current-main parent above. A Git tree commit inherited **all 29 exact frozen PR #1744 path Git blobs**, including all former source handoffs, v1/v2/v5/v6/v7 and workflow. Only `tools/planning/frontier_maintenance_v4.py` may differ from that frozen payload; this handoff is the sole added 30th path. No inherited source or reviewer branch is modified.

The correction authenticates a transition wrapper **before** either semantic disposition and before `EXACT_REQUIRED_REVIEW_SUCCESSOR_MATERIALIZED` can return. Even a direct `semantic_generation_from_terminal` call with a caller-injected terminal must read the complete fresh GitHub comment stream and invoke real `base.closure_authorized_terminal_from_comments` on its own wrapper issue; require exact equality to supplied immutable terminal, true terminal owner/DONE authority, and live GitHub branch ancestry for both head/work SHAs. That strict base/v5 path verifies first-winning ownership, six-hour immutable GitHub timestamps, recovery/PROGRESS and branch ancestry. All parse/API/ref/lease/duplicate/stale ambiguities fail closed. The separately corrected successor terminal retains independent authenticated ownership and SHA checks. No new global gate is imposed on unrelated scoped routes.

The old v4 unit-semantic controls remain executed with an explicitly local test seam for their historical owner-independent fixtures, while an additional read-only mocked-GitHub test invokes the **actual strict composed base/v5 validator**, testing genuine first-owner, both materialized and terminal-successor dispositions, duplicate losing claim, seven-hour expiry with genuine successor, unsupported HEAD_ADVANCE, stale injected terminal, edited comment, incomplete pagination and missing Git refs. The tests have no live mutation or --apply side effects. Exact-hosted full v1–v7 `validate-pr` CI and skipped mutating `maintain` job must be checked at final PR HEAD; this handoff does not assert success before evidence.

## Required next route / authority

Publish OPEN/DRAFT existing-PR corrective successor PR from `planning/issue-1747` against current `main`, then inspect exact 30 changed paths, all inherited frozen blob identities, newly corrected script SHA, hosted final-head full compile + v1–v7 suite run status, and confirm mutation-capable maintenance is SKIPPED. Publish schema-3 owner `STATUS(REVIEW_READY)` **only if** complete exact-final-head evidence passes within the valid six-hour lease. Require a **fresh genuinely distinct independent adversarial security review** of this exact source PR, then separate owner-authorized, expected-head-compatible **SQUASH-only NONCANONICAL** integration if CLEAN.

**Never** merge frozen #1744, reviewer-only #1749 or this source before full gates. Never run live --apply/PATCH/retirement, promote to canonicality, or claim gameplay truth, provider/legal, implementation readiness, release or production authority.
