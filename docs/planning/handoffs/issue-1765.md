# Issue #1765 — browser-normalized encoded-dot PR link remediation handoff

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-12`.  
**Owner:** first sole schema-3 CLAIM #6153424697, GitHub immutable 2026-10-13T19:25:48Z; actor `encoded-dot-remediation-1765-gpt6-20261013-cph-01`, branch `planning/issue-1765` created from then-main `7da4c2d50412fe134c8632264908560b8b7995ce`.  
**Binding:** Issue #1147 terminal #5675066392; program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Evidence and exact frozen inheritance

The genuinely distinct reviewer Issue #1761 negative terminal `REVIEW_STATUS(CHANGES_NEEDED)` #6153397669 identified one MAJOR FSR-1761-M01 in existing source Issue #1756, OPEN/DRAFT PR #1760 exact HEAD `480f1618be0b8a6e19c1777b7cda2cce042dc29e`, script blob `4d8e5bec3b1a152af5ef5a78e3728cdf7b3c03c3`. Evidence-only reviewer DRAFT PR #1766 MUST NEVER MERGE.

Created branch from fresh actual main, then imported the exact six inherited GitHub blobs without modification:
- `.github/workflows/retire-negative-review-prs.yml` `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`
- `docs/planning/handoffs/issue-1720.md` `088bb6afd8651c941ba1045d3ffab9b10da5d4c1`
- `docs/planning/handoffs/issue-1726.md` `904dd95551d79991f546317ae71283891a165dec`
- `docs/planning/handoffs/issue-1738.md` `ef7a69bafa5949bee8c16f0605340980529b736a`
- `docs/planning/handoffs/issue-1746.md` `f686b32aaebc387fbcac3d2cf5856853bb17cd54`
- `docs/planning/handoffs/issue-1756.md` `d2ddd859a277bfdaeb2843aa2ee87b58b5160e54`

Changed **only** inherited `tools/planning/retire_negative_review_prs.py` from `4d8e5bec3b1a152af5ef5a78e3728cdf7b3c03c3` to `a80b080dccbed14ed76fc8b8ec8121ded9bb7ca6`; added only this task handoff. No changes to older source or review PR.

## Actual correction and test additions

`browser_path_segments` emulates WHATWG `.` and `..` stack reduction **after decoding a path segment**, covering `%2e%2e`, `.%2e`, `%2e.` without treating innocuous `help%2efile` as a parent directory. Both first-party absolute and Markdown relative path consumers now use the same normalized segments. Existing fail-closed percent malformed/slash/backslash/double encoding checks, strict scheme/host/port/repo/number identity, numeric zero/`+` aliases, issue/comment pagination, owner terminal/lease/72h and initial/fresh pre-PATCH guards are preserved.

The actual full-module `self_test` received 9 additional positive encoded-dot browser-equivalence fixtures (direct web, API, relative inline/root/reference-definition) and 5 negative fixtures (other repository, wrong numeric identity, foreign host, harmless encoded dot in filename). Existing `self_test` loops drive all alias-positive variants through title, body, complete live-comment eligibility and through both mocked `execute(apply=True)` first and pre-PATCH scans with zero PATCH. New fixtures are exercised by the unmodified source-provided exact-head GitHub workflow once a draft PR is published. **Do not claim hosted CI SUCCESS until the exact final HEAD jobs actually report it**.

## Remaining required work and guards

Verify exact eight changed paths, immutable six carried blob identities and current main compatibility; open **DRAFT PR** before `STATUS(REVIEW_READY)`. Wait for GitHub-hosted read-only self-test/py_compile SUCCESS at exact final HEAD and mutating `retire` SKIPPED. Any failure -> fix own script and rerun at new exact head, or owner HANDOFF/BLOCKED if not fixable. Then publish owner `STATUS(REVIEW_READY)` within valid six-hour lease; materialize **new genuinely distinct mandatory security review**, including independent full-module first/fresh-pre-PATCH negative proofs. **No self-review, no automatic retirement or real PATCH, no reviewer-only PR integration, no source merge without separately owner-authorized current-main-compatible SQUASH-only NONCANONICAL integration.** No gameplay, canonical, production or release authority.
