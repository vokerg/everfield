# Issue #1716 — mandatory independent source security review of PR #1714

**Disposition: CHANGES_NEEDED — 0 BLOCKER / 1 MAJOR (FSR-1716-M01) / 0 correction-requiring MINOR.** This is a reviewer-only, NON-INTEGRABLE negative review; no claim of CLEAN, canon, integration, production or issue/PR retirement authority.

## Scope, immutable provenance, and separation

Genuinely distinct reviewer execution `frontier-existing-pr-security-review-1716-gpt6-20261012-01`, first and sole winning review Issue #1716 schema-3 CLAIM #6131653149. Frozen source Issue #1711 first owner CLAIM #6131528483, unedited owner `STATUS(REVIEW_READY)` #6131619971; original **OPEN/DRAFT** source [PR #1714](https://github.com/vokerg/everfield/pull/1714) HEAD `0c62912a06246be1714e56cd1391b5ec80e56ec7`, base and unchanged current main at review claim `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`. Canonical Issue #1147 terminal binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. This review does not edit source.

Independent GitHub PR-file manifest comparison against frozen predecessor source #1698 PR #1702 found **24 current changed paths**, **21 inherited SHA-identical paths**, only 3 differences: `tools/planning/frontier_maintenance.py` = `f7dd6640210e27e18a170633ba8f8ab0d176835d` (prior `b30690ae302f28cb2295fddd0b78a882e2a71b83`); `tools/planning/frontier_maintenance_v5.py` = `415ac30decdaf39f27355223b03ec5d4664a0347` (prior `413dc3a5f0e1fc707ce709f1b6730b50fa142560`); new own `docs/planning/handoffs/issue-1711.md` = `9252804cf63e067f4a085247de60a66168e042e8`. No predecessor files were removed. Baseline review #1703 terminal #6131487384 (FSR-1703-M01) was independently read.

Exact final-head authored GitHub Actions [run #38301036503](https://github.com/vokerg/everfield/actions/runs/38301036503) completed SUCCESS at exact source head; `validate-pr` job #114983745203 SUCCESS, mutation-capable `maintain` #114983747475 SKIPPED. Source workflow was independently inspected: `pull_request` `validate-pr` narrows permissions to `contents: read`, compiles planning modules and runs v7 composed self-test; mutating job excludes `pull_request`. This is **producer CI, not independent security review**.

## Verified correction in direct paths

The corrected base module `github_verified_terminal_result_heads(issue_number,head_sha,work_sha)` obtains **one actual task-branch tip** and accepts each SHA only when equal to it or a GitHub compare `status=ahead, ahead_by >=1, behind_by=0` against that same tip; otherwise fails closed. `closure_authorized_terminal_from_comments` calls this after owner/lease resolution and before storage PATCH; the v5 no-route and stable-terminal paths call it as well. These specific FSR-1703-M01 closure paths are corrected. Existing non-atomic GET/PATCH and lack of historical reflog remain explicitly bounded.

## FSR-1716-M01 — MAJOR: legacy semantic terminal consumption bypasses the corrected live terminal HEAD/work proof

**Affected exact source call chain:**

1. In unchanged `tools/planning/frontier_maintenance_v5.py::v5_resolved_transition_generations` (~lines 361–382), the first consumed-generation path does `semantic = v4.semantic_generation_from_comments(issue, comments, issues_by_number)` then, if non-null, `consumed.add(semantic)`. It does **not** call `base.github_verified_terminal_result_heads`, `terminal_owner_generation_is_current`, or guarded closure.
2. In unchanged `tools/planning/frontier_maintenance_v4.py::semantic_generation_from_comments` (~lines 127–139), terminal retrieval is `base.reconcilable_terminal_from_comments`, which validates owner-linked schema-3 record/SHA40 **syntax** but not GitHub branch ancestry. `semantic_generation_from_terminal` (~lines 47–125) checks trusted closed wrapper, expected source generation, allowed disposition, successor identity/binding and chronology, but does not authenticate either `terminal.head_sha` or `terminal.work_sha` against the live task branch.
3. In composed `v5.materialize_missing_transitions` (~lines 630–670), the result is unioned into `resolved_generations`, which flows into the successor-consumption/redundancy logic. A closed existing wrapper with apparently legitimate successor can therefore falsely consume exact source generation even if the schema-3 owner terminal's work/result SHA refers to an unrelated commit.
4. Separate **audit-required adjacent surface**, not counted as an independently demonstrated second defect: `v2.resolved_transition_generations` → `resolved_dispatch_binding` → schema-3 `schema_terminal_resolution_from_comments` also reads syntactic `base.reconcilable_terminal_from_comments`. Its dispatch-marker-only path is a different authority route and must not be falsely characterized as requiring a schema-3 terminal.

**Independent read-only executable falsification, and its limit.** Read exact source code and ran a Python standard-library isolated reproduction of the above actual v4/v5 semantic decision clauses, using explicit stubs for GitHub intake, parsed trusted owner terminal and successor. Fixture: trusted closed factory wrapper issue 404 for generation `(42,99,REVIEW_SUCCESSOR)`, eligible linked open successor issue 405 with `factory transition #404` and proper chronological creation, a syntactically accepted owner `STATUS(DONE)` terminal with `head_sha=work_sha=b*40`, while a mocked live branch provenance oracle rejects both as unrelated to its tip. Result:

```text
FROZEN_LEGACY_SEMANTIC_CONSUMPTION_WITH_FORGED_TERMINAL_HEAD True
TERMINAL_RESULT_SHA_PROVENANCE_VALIDATOR_CALLS 0
EXPECTED_CONSERVATIVE_RESULT_IF_LIVE_REF_REJECTS_FORGED_SHA False
```

This executable witness is an **extracted exact-code-path reproduction with stubbed parsed records, not an import/execution of every full frozen Python module**, nor a live GitHub branch manipulation, destructive PATCH or independent full v1-v7 regression run. The missing call in the actual frozen v4/v5 implementation is independently confirmed by inspecting the real source. The already green hosted producer suite did not establish security sufficiency.

**Security consequence and boundary:** a terminal that is owner-shaped and route/successor-consistent but **not provably from the task branch** can make transition liveness accounting record a generation as consumed. This may suppress remediation/recovery or retire a wrapper despite invalid result provenance; it does not prove arbitrary outside users can impersonate the trusted owner. Treat as **one MAJOR correction-requiring finding**; 0 BLOCKER, 0 correction-requiring MINOR. Do not integrate #1714.

## Required exact next route

Materialized exactly **one bounded successor**, [Issue #1718](https://github.com/vokerg/everfield/issues/1718), blocked until this in-lease negative review terminal and reviewer-only exact-head draft. Preserve frozen source #1711/PR #1714, prior negative review #1703/PR #1706, earlier producer #1698/PR #1702 and this reviewer-only PR as immutable, unmerged evidence. Authorized new correction inherits #1714 frozen 24-path packet but may minimally correct v5 semantic consumption, v4/v2 underlying terminal-backed consumers, and (only if essential) base helper, plus its own handoff; it must retain genuine independently authorized dispatch-marker resolution, source temporal recovery semantics, no live `--apply`, and no new authority.

Require actual corrected-module negative/positive GitHub mock and full composed v1–v7 regression, exact source-head GitHub Actions read-only PASS with mutating job SKIPPED, in-lease source `STATUS(REVIEW_READY)`, then **new genuinely distinct mandatory security review**. Only separate claimed, clean, exact-head/current-main compatible **SQUASH-only NONCANONICAL** integration can ever publish source. Source PR mergeability/draft status and this negative reviewer PR confer no integration, canonicalization, gameplay, engine/readiness, production or release authority.
