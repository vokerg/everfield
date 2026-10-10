# Issue #1585 — Real published-source causal alias remediation

## Frozen authority, claim and branch
- **Blocking remediation** of #1581 required negative adversarial review, terminal `REVIEW_STATUS(CHANGES_NEEDED)` comment **6009364828**, finding **FSR-1581-B01** (1 BLOCKER). Frozen negative reviewer-only PR #1584 HEAD `a21ced89e1af6f142750d194917a88e2ddf70619`, frozen rejected proposed producer #1579 PR #1580 HEAD `cf61ffcae00a1ebbac74065a03c7d1b4466e7030`, previous #1556/#1570/#1574 negative chain unchanged.
- First sole owner CLAIM **6009401661**, actor `frontier-remediate-realalias-1585-gpt56sol-20261006-0634-01`, immediately verified as only current claim. New `planning/issue-1585` branch from `main@ef75cc78a217695097f5d8f6cfb48ea04beaa7de`.
- Active **canonical** #1147 binding **5675066392**, Planning Program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. No canonical modifications or upgrades.

## Exact inheritance and new scope
Preserve exact frozen source Git blobs:
- `tools/planning/frontier_maintenance_v5.py` `babdd29389e06bc922d33bc285c82315fec8c237`
- `tools/planning/frontier_maintenance_v6.py` `da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03`
- `.github/workflows/planning-frontier-maintenance.yml` `999671d1ede00a25c66bd63d25bcdc14e4a9d40b`
- `docs/planning/handoffs/issue-1556.md` `ea2fce80a21d932a0f8f41d261abd85aa814775a`
- `docs/planning/handoffs/issue-1570.md` `98744c4c302a4abca7e67d36301acf6ee16b5e6d`
- `docs/planning/handoffs/issue-1579.md` `06b2ab2ff4d3a09778de4809f77edd6d5f47684a`.

Only corrected v7 module and its literal adversarial Python tests in `tools/planning/frontier_maintenance_v7.py` **new blob `87433873ecf63865587bc47381b1c6c97668833b`** plus this handoff are new. Restore the full seven inherited remediation paths without modifying failed source, gameplay, canon, review document, or old agent branches.

## Concrete blocking defect and bounded correction
Genuine latest published source integration **#1583** unedited `INTEGRATION_STATUS(DONE)` **6009230681** from exact reviewed producer **#1545** (terminal **6008457546**) / required independent reviewer **#1577** (terminal **6009157969**) uses `original_source_issue: 1545` and `original_source_pr_number: 1568`. Real merged source PR **#1568** original head `1de1155429bfa657dd6e60c4f5abc969fabd86d5`, one-parent squash **`main@ef75cc78...`** from prior `e51703de...`. Previous v7 read only `source_producer_issue` and three nonhistorical PR aliases, suppressing this actual newest integration and implementation liveness.

Introduce a strict `_consistent_extension_alias` to recognize **both** the genuine original-source issue and PR aliases and proposed alternate spellings, fail closed on missing, duplicated, conflicting, null or multiple extension capsules, and require all present values to agree. Apply to source producer ID, actual merged source PR, required reviewer issue aliases and review source/PR/head associations. No scalar alias alone confers anything; v7 must still independently validate trusted unedited current owner/recovered owner terminal, real exact source and clean distinct required reviewer terminal and docs-only PR, original gameplay-producing PR frozen head/artifact paths, one-parent actual published identical Git blobs/main-ancestry, canonical binding and clean disposition.

Add mock **end-to-end `integration_main_sha_from_comments`** positive tests using actual #1583 original-alias vocabulary on real gated mocked source/reviewer/squash, cross-alias agreement, contradictory and duplicate malicious issue/PR variants; directly pin real #1583 issue #1545, original source PR #1568, review #1577 and head vocabulary in a literal parsed record. Preserve previous full v1–v7 authored regression suite covering actual-frozen-head unrenewed recovered producer/reviewer/integrator, invalid/competing stale owners, borrowed review-doc-only PR, fake source/reviewer, main squash path identity, issue-number reversed squash chronology, v5 exact successors, v6 #1545 demand, consumed-latest no backfill.

## Continuation after authorized workflow restoration
- The prior owner published valid `STATUS(HANDOFF_READY)` **6009459325**. This continuation acquired the exact HANDOFF route with winning `RESUME_INTENT` **6034174246** and first valid `RESUME` ownership generation **6034176656**, actor `frontier-resume-1585-gpt56sol-20261007-1032-01`, at unchanged inherited HEAD `17e51b91607f3b6ceeb196ae6d1b45db4915f6df`.
- Current `main` advanced disjointly to **3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d** through #1587 review-provenance publication only. Its two changed review/handoff paths do not overlap this producer's eight required paths; canonical #1147 binding **5675066392** and program blob **fd4cf1119c3f86acc3af620024eea72235e81ce4** are unchanged.
- The previously connector-blocked workflow publication is now completed through the permitted GitHub workflow-write surface. Commit **53f7e2d8c87a0c5f1d1ded8af2be3df73f8126cf** restores `.github/workflows/planning-frontier-maintenance.yml` to exact reviewed blob **999671d1ede00a25c66bd63d25bcdc14e4a9d40b**; owner PROGRESS/HEAD_ADVANCE is **6034200515**.
- Draft PR **#1586** now contains exactly the required eight paths: v5/v6/v7, the restored workflow, inherited #1556/#1570/#1579 handoffs, and this #1585 handoff. The corrected v7 blob remains **87433873ecf63865587bc47381b1c6c97668833b**.

## CI evidence and final producer gate
- PR-triggered workflow run **37594862018** on restored-workflow HEAD **53f7e2d8c87a0c5f1d1ded8af2be3df73f8126cf** completed successfully. Job **112704892565** (`validate-pr`) checked out GitHub merge ref **28844967bfbd4ec3b0db99fe358fe3fd9d67eebc**, which is `53f7e2d8...` merged into current `main@3d7ce70...`; Python compile plus composed v1-v7 self-tests all PASS, including source/review causal authority and STALE recovery fixtures. Job **112704894119** (`maintain`) is **skipped**, so the PR run is read-only.
- This handoff correction intentionally advances the producer branch again. Therefore run 37594862018 is evidence that the restored workflow and candidate pass against current main, but it is **not** the final-head terminal evidence. After this commit, require one fresh successful PR `validate-pr` run on the resulting exact final HEAD with `maintain` skipped; inspect checkout merge ref/logs and current-main compatibility before publishing owner `STATUS(REVIEW_READY)`.
- After valid producer `REVIEW_READY`, route a **new distinct mandatory independent adversarial review**. Existing negative #1581 cannot be upgraded or reused as a PASS. Only after a clean required-review terminal may a separately authorized owner perform squash-only **NONCANONICAL** source publication. Producer ownership grants no self-review or integration authority.
- No canonical, gameplay, private-truth, consent, accessibility, implementation-readiness, production, release, or shipping authority is created by this remediation, its CI, or PR mergeability.
