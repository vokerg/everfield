# Required independent adversarial review — factory root-authority remediation #1638

**Review issue:** #1644 / mission `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-13-REV-01`  
**Independent reviewer episode:** `frontier-independent-root-review-1644-gpt6-20261011-1133-01`; first and sole unedited schema-3 CLAIM #6107638204. Different episode/actor from producer `frontier-remediate-root-1638-gpt6-20261011-1102-01`.  
**Disposition:** **CHANGES_NEEDED — 1 BLOCKER, 0 separately classified MAJOR, 0 correction-requiring MINOR.** This is a reviewer-only analysis, not producer verification or integration authority.

## Exact frozen source, canonical binding and positive controls

- Active program `docs/planning/PLANNING-PROGRAM-v1.md` blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; binding Issue #1147 unedited #5675066392; activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`, verified as ancestor of current `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.
- Producer #1638 winning CLAIM #6107386722 (GitHub created/updated `2026-10-11T09:02:11Z`) and unedited in-lease terminal `STATUS(REVIEW_READY)` #6107450556 (`2026-10-11T09:10:24Z`). Source draft PR #1640 is OPEN/DRAFT, base `main@3d7ce70...`, exact HEAD `e6bbaddf1e17b23ad9344983c3159d4f30990bfd`.
- Prior separate negative #1632 terminal #6107357316, reviewer-only draft PR #1636 HEAD `89990216c77fdec51163cb839a00b89c9336c36b`, blocker FSR-1632-B01; parent frozen source #1628 PR #1631 HEAD `27d452fe5ae03dd822e8fc357d6b72cc48913698`. No predecessors were mutated or merged.
- Independently enumerated PR-files API: #1640 has exactly 19 changed paths; 17 paths have *identical* Git blob SHAs to frozen #1631 (including v7 `28af0a1eeeddcc318b1faeca76c82dfd1efbed87`). The two new/changed identities are base `tools/planning/frontier_maintenance.py` `165eb8301715947be70f67474428cc2a7bdb3e7f` and handoff `docs/planning/handoffs/issue-1638.md` `761a7000835dbd969f192af5b69249613298c851`.
- Exact source-head pull_request run #38127342597 SUCCESS; job #114434343946 `validate-pr` SUCCESS, mutation-capable #114434344834 `maintain` SKIPPED. Actual proposed merge commit `1dd089ecbb0d774c570db69a2ac9c1c43f34e85e` has precisely the current-main and source-head parents, tree `40a1b7cbfe1d0afac4bdb62120ceb19d3b1fcbbd` equal source commit's tree. This proves producer test provenance, **not** independent correctness.
- Independently checked real Issue #1583 terminal #6009230681 and publication commit `ef75cc78a217695097f5d8f6cfb48ea04beaa7de`: single parent `e51703de82b9df3f5e676663d3a04fdc678bd5c6`; source #1545, separate verifier #1575 and separate review #1577 retain their distinct roles. This prior squash is NONCANONICAL; neither that evidence nor present CI upgrades readiness or grants any unrelated scoped/global gate.

## FSR-1644-B01 — BLOCKER: nested `evidence_refs` and `artifact_paths` still borrowed as root authority

**Exact source defect:** `_root_mapping_fields` (base lines 161–188) newly checks direct root *scalar* keys; `parse_operational` (461–493) calls it and correctly rejects nested-only fake CLAIM and STATUS. But `base.list_scalar` (228–265) is still its old unrestricted `re.compile(r"^(?P<indent>\s*)KEY:...")` search over the complete body, accepting arbitrarily indented key/list matches. It never consults `_root_mapping_fields` or checks that the matched list is a direct root key. `schema3_ownership_lease_state` (302–380, especially 358) trusts this list for a PROGRESS(EVIDENCE) lease renewal. v7 source/review integration path checks (around lines 941, 945 and verifier checks around 1173) also compare real PR file paths to `base.list_scalar(terminal.body, "artifact_paths")` instead of to a proved root declaration. These are **operational** authority consumers.

**Independent semantic negative fixture** (the 40-letter `a` value represents a syntactically valid immutable Git SHA):

    protocol: planning-v1
    schema: 3
    kind: PROGRESS
    issue: 10
    mission_id: M-10
    branch: planning/issue-10
    actor_session_id: actor-a
    state: IN_PROGRESS
    ownership_generation_comment_id: 1
    observed_head_sha: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    progress_basis: EVIDENCE
    extensions:
      evidence_refs:
        - aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

PyYAML **6.0.3** `safe_load` returns `root.get("evidence_refs") is None` and the SHA **only** at `root["extensions"]["evidence_refs"]`. Independently executed the precise current `base.list_scalar` regex/scan algorithm from source lines 228–265 against this same fixture: `list_scalar(body, "evidence_refs") == ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]`. This is a reproducible positive **violation**, not a hypothetical exact-viewport or CI claim. The root protocol/schema/kind/identity are genuine, so the new `parse_operational` guard accepts the PROGRESS capsule and does not correct the list-scope error.

**Authority consequence:** in the source `schema3_ownership_lease_state`, a same-actor, immutable trusted PROGRESS with this *nested-only* evidence list, valid observed unchanged head, created before six-hour expiry, and EVIDENCE counter below three is treated as a valid renewal despite no root-level `evidence_refs`. E.g. owner grant at 00:00Z and fake evidence progress at 05:59Z incorrectly extend the lease to 11:59Z instead of expiry 06:00Z. `schema3_owner_unexpired_at` consumes the resulting anchor; this affects stale recovery and any downstream current-owner check. A matching nested `extensions.artifact_paths` in source/review/verifier terminals can likewise supply a missing top-level declared path set to the v7 path-equality predicates; no exact root scope is proved. These are two surfaces of the **same** trust-boundary bug, not two independent findings.

**Required bounded fix:** retain the corrected root scalar parser and pinned 17 predecessor blobs; make list field reading root-scope-aware and fail closed for nested/sequence/flow/duplicated/quoted/tagged/shadow or prose-derived list authority while retaining genuine multiline root `evidence_refs` and `artifact_paths`. Assert that nested-only PROGRESS(EVIDENCE) does **not** change the lease anchor, that an authentic root EVIDENCE list still renews before expiry (but fourth consecutive EVIDENCE does not), and that nested-only `artifact_paths` cannot pass exact source/review/verifier PR path identity. Recheck ORPHAN's 600-second maturity, winning source ownership, real verified NONCANONICAL source ancestry, genuine scoped verifier-free vs verifier-required routing. Re-run Python compile/composed v1–v7 on an exact *new* final-head read-only PR CI, then obtain **another new genuinely distinct mandatory review**.

## Test and proof boundaries

This review executed a small **independent PyYAML-vs-exact-source-list-algorithm** experiment locally, inspected the actual immutable source file and exact v7 consumers, independently checked GitHub API source diff identities, actual CI job outcome and actual one-parent main squash provenance. It did not execute the 1,501-line source module or v7's complete harness locally: network access to clone the public repository was unavailable; producer's hosted SUCCESS is recorded separately and not misrepresented as our own run. A direct source-module regression should be added in the remediation and covered by hosted CI.

**Final review verdict:** CHANGES_NEEDED / FSR-1644-B01 BLOCKER. Do not mark #1640 reviewed-clean; do not merge source, frozen predecessors or this review-only PR; do not grant canonicality, implementation readiness, gameplay truth, consent, accessibility, engine selection, production or release authority. Materialize one bounded mandatory remediation successor, followed by exact final-head independent review and a *separate* owner-authorized squash-only NONCANONICAL source publication if and only if every required gate later passes.
