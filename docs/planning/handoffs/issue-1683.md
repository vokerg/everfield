# Issue #1683 — bounded factory security remediation handoff

**Mission:** FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-17  
**Source:** frozen Issue #1673 / OPEN DRAFT PR #1675 exact HEAD `b8c4d54b80fbc360c2c036ffe886371d545edbc9`  
**Mandatory negative independent review:** Issue #1677 terminal #6118813482 (FSR-1677-B01 BLOCKER, FSR-1677-M01 MAJOR)  
**Owner claim:** Issue #1683 comment #6130017581, GitHub created 2026-10-12T18:17:13Z  
**Session:** frontier-factory-terminal-liveness-remediate-1683-gpt6-20261012-2015-cph-01  
**Base main:** `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`  
**Binding:** #1147 comment #5675066392, canonical blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Bounded work

Reassembled 19 source-inherited paths byte-identically from frozen #1675: hosted maintenance workflow, inherited v6/v7, 16 historical issue handoffs. Intentionally did **not** copy #1673's task-specific handoff. Corrective code changes are restricted to `tools/planning/frontier_maintenance.py` (FSR-1677-B01), `tools/planning/frontier_maintenance_v5.py` (FSR-1677-M01), and this handoff.

- B01: a new conservative terminal-closure authority predicate checks immutable GitHub comments, branch identity, first-winning/current in-lease schema-3 ownership through v5 prefix reconstruction, authenticated HEAD_ADVANCE provenance when used, and unambiguous terminal linkage. The mutation consumer re-reads terminal authority and current issue-open state immediately before PATCH. GitHub REST GET/PATCH are *not* atomic; this does not claim a transactional guarantee.
- M01: pin exactly the real #1664 and #1673 terminal generation IDs and full route strings to #1673/#1677 existing successors, requiring trusted eligible issue metadata, exact title/mission identity, and preservation of active wrapper ownership. Other route strings and stale/wrong source identities cannot manufacture successor authority.
- Embedded negative/positive self-tests cover source-specific mapping, missing/duplicate/closed/wrong-actor/wrapper-only successor cases and closure expiry, counterfeit grants and edited records.

## Hosted verification and authority

**Current state: bounded source corrected; authored exact-code-head CI succeeded, mandatory independent review not yet performed, source not merge-authorized.** Hosted read-only pull-request run #38291046728 at corrective code head `536d2afe4d60562bad7c8f648a02ba5a75b7edd7`: validation job #114950947108 **SUCCESS** (Python compilation plus full composed v1–v7 self-tests); mutation-capable `maintain` job #114950949202 **SKIPPED**. The predecessor initial draft head `3220beca1800131cc288b29c9cde0cd7212e50f3` also passed hosted read-only CI #38290806579 but was superseded by strengthened EVIDENCE-E4, authenticated HEAD_ADVANCE and pre-PATCH regression tests. This handoff update creates a new task HEAD, which must receive its **own exact-final-head read-only PR CI PASS** before any terminal.

Preserve the full composed `frontier_maintenance_v7.py --self-test` and hosted exact-final-HEAD read-only PR validation; mutation-capable maintenance must be SKIPPED on PR. Inspect any failure, correct only own bounded paths, and repeat at exact final HEAD. OPEN DRAFT PR #1690 has existed since before the intended owner terminal.

After an exact-final-head green validation, route to one **new genuinely distinct mandatory independent code/security reviewer** who did not author this corrective source or reviewer #1677. Only a clean required review could later support a separately owner-authorized, expected-head/current-main-compatible **squash-only, NONCANONICAL** source integration. Do not merge this draft, source #1675, any reviewer-only draft, or deploy mutating factory maintenance; no gameplay, canon, engine, accessibility, release or production authority.
