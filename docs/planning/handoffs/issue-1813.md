# Issue #1813 — Emergency owner-directed continuation of stalled Copilot probe hardening

## Status
SOURCE PREPARED / INDEPENDENT SECURITY REVIEW STILL REQUIRED. NOT INTEGRATION AUTHORIZED; NOT A WORKER.

## Incident, authority and provenance
- User explicitly requested intervention in the stalled factory on 2026-10-17; initial first-owner claim on Issue #1813 is comment #6232440589 with actor `everfield-copilot-probe-hardening-1813-gpt6-20261017-prg-01`. That generation **has not been presumed expired or replaced**.
- On inspection the prescribed `planning/issue-1813` branch and corrective commit were missing; a separate assistant execution prepared the declared task branch from fresh `main@0650bc05acfcd3966b3bee87070587cdd0f831b5` under the direct user incident instruction. This is a visible technical continuation, **not** an invented valid first-winner CLAIM, HANDOFF, RECOVER, security review or terminal STATUS. A downstream operator must reconcile this ownership situation under the effective canonical protocol before any authority-dependent terminal/merge.
- Canonical program `docs/planning/PLANNING-PROGRAM-v1.md`, Git blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, bound by Issue #1147 terminal comment #5675066392, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Frozen negative review #1809 terminal #6232397142 identified 2 MAJOR (floating executable package and privileged PR workflow) and 1 correction-requiring MINOR (grep allowing extra model output) against frozen source PR #1808 HEAD `cecb683a10beb082a2721fdf04cfd69fdfb092df`. Reviewer-only PR #1811 must NEVER merge.
- Original source `docs/planning/handoffs/issue-1806.md` blob `b7c9b14b62adea299d07f27ec92b2c99fecc92b0` is copied byte-identically and retained as provenance.

## Corrective changed paths and explicit owner incident scope
1. `.github/workflows/everfield-frontier-copilot-probe.yml` — single trusted MAIN `workflow_dispatch` trigger, job-level `contents: read` and `copilot-requests: write`, pinned checkout, SHA-512 verified package, no git credentials or write-capable model tools; strict entire stdout match of the one-line sentinel (allows a single terminal LF, never extra lines). No scheduled/PR-triggered billable inference.
2. `.github/workflows/planning-frontier-maintenance.yml` — existing main-established PR-only `validate-pr` job extended to do no-model read-only static and exact-tarball integrity/CLI version tests, with `contents: read` and no Copilot privilege; **its mutating `maintain` remains manual `workflow_dispatch` only**, preserving the emergency freeze. This narrow shared-workflow path addition is required to obtain hosted PR CI without allowing any unreviewed PR workflow definition to trigger a paid model job. It is an owner-directed security scope intervention beyond Issue #1813 original owned paths and requires scope reconciliation before integration.
3. `docs/planning/handoffs/issue-1806.md` — immutable inherited source provenance.
4. This file — accurate task continuation.

## Package integrity
- Distribution: fixed npm registry tarball `@github/copilot-linux-x64@1.0.80`, pinned URL, exact SHA-512 hexadecimal `aafd72b553700372032bb91c428c3e7c08a40faeede36f8043c5f8d9b2bfee8b9d362bf87eb55930ed328750d821e6d545c9848663ef6d53d8fe9b5550addc6c`.
- Its sha512 SRI from the npm lockfile in the publicly available `karaage0703/xangi` project: `sha512-qv1ytVNwA3IDK7kcQow+fAikD67t42+AQ8X42bK/7oudNiv4frVZMO0yh1DYIebVRcmEhmPvbVPY/ptVUK3cbA==`; decoded independently to the exact hex above. The PR-hosted validation must check actual downloaded bytes and actual CLI `--version` on ubuntu-24.04 x86_64. A lockfile assertion alone is not execution evidence.

## Honest proof and gates
- Previous original source `#1808` Actions run #39021587655 was SUCCESS and demonstrated actual built-in `GITHUB_TOKEN` Copilot inference, but predates this correction and does NOT security approve or prove this new final version.
- NEW PR validation is static, non-billable, and must run at exact final HEAD. At source preparation there is no new verified main-branch inference run: by design it cannot run before main integration; never advertise it otherwise.
- Mandatory next: independent code/security review of this **exact** source and its extra validation workflow, valid ownership/owner override reconciliation, then separately authorized current-main-compatible expected-head **squash-only noncanonical** integration if CLEAN. After merge, a deliberate main/manual actual model probe may test runtime reachability. Only a later separate reviewed cost-bounded write-capable dispatcher can take an issue, write code, and open a PR.
- No autonomous issue/branch/PR mutation, registered route, gameplay authority, live retirement or chargeable recurring schedule added.

## Reproduction
- Static integrity: inspect manual-only `on: workflow_dispatch`, role- and job-specific permissions, absence of PR/push/schedule on paid workflow, exact `github.sha` checkout and no token-bearing git remote.
- Hosted existing `Everfield planning frontier maintenance` PR `validate-pr` job: strict manual-only workflow checks, package tarball SHA-512 and actual `copilot --version` without model token. Fail closed on missing CLI or mismatched hash.
- Manual inference test is intentionally NOT triggered from any PR; it requires this reviewed workflow on trusted main and an explicit owner-invoked `workflow_dispatch`.

## Outcome
A previously absent task branch now contains reviewable, bounded corrective infrastructure. Pending external gates remain pending; no self-CLEAN or fabricated integration authority.
