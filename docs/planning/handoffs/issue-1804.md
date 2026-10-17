# Issue #1804 — bounded same-scheme and network-path PR-retirement correction

## Role, authority, frozen source
- Mission: `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-21`; mandatory continuation of existing source PR #1801, not authorization for live retirement or integration.
- First valid immutable claim: Issue #1804 comment **#6232234753**, actor `everfield-source-commonmark-networkpath-rem21-gpt6-20261017-01`, GitHub `created_at=2026-10-17T09:21:50Z`. Later competing CLAIM #6232235583 is not ownership authority. Task branch `planning/issue-1804` from `main@7da4c2d50412fe134c8632264908560b8b7995ce`.
- Canonical Issue #1147 binding #5675066392, exact program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Source Issue #1800 in-lease REVIEW_READY #6217098781; existing OPEN/DRAFT PR #1801 frozen HEAD `54cc76a3a33d84dfd3edf3dd80637981d6edbd8b`; old script blob `69f47c52d4a9a45b3eb18a3f7f05a50c4670a1aa`.
- Independent mandatory negative review #1802 REVIEW_STATUS(CHANGES_NEEDED) **#6232221347**, 0 BLOCKER / 2 MAJOR `FSR-1802-M01`, `FSR-1802-M02` / 0 correction-requiring MINOR; evidence-only OPEN/DRAFT PR #1803 frozen HEAD `352335f6c9a6169609ee0c720b41ce79ec5cc810`; reviewer report blob `08f49653410283e2ca5727e6255ebbc0804e6add`. The reviewer-only PR must never be merged.

## Exclusive 17-path packet
Exactly fifteen predecessor non-script Git blobs below are inherited by Git-tree SHA, byte-identical; ONLY the full retirement Python module is corrected and this new handoff is added.

- `.github/workflows/retire-negative-review-prs.yml` — `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`
- `docs/planning/handoffs/issue-1720.md` — `088bb6afd8651c941ba1045d3ffab9b10da5d4c1`
- `docs/planning/handoffs/issue-1726.md` — `904dd95551d79991f546317ae71283891a165dec`
- `docs/planning/handoffs/issue-1738.md` — `ef7a69bafa5949bee8c16f0605340980529b736a`
- `docs/planning/handoffs/issue-1746.md` — `f686b32aaebc387fbcac3d2cf5856853bb17cd54`
- `docs/planning/handoffs/issue-1756.md` — `d2ddd859a277bfdaeb2843aa2ee87b58b5160e54`
- `docs/planning/handoffs/issue-1765.md` — `a74397422eb7ddceabc4b00f3d8d93d20dbf7348`
- `docs/planning/handoffs/issue-1769.md` — `72b4ad4435170e97893b17b0f1b6fd17674853d3`
- `docs/planning/handoffs/issue-1773.md` — `81d59da9083fc5ff6f4d3d16b3e1b9f0de85aee2`
- `docs/planning/handoffs/issue-1780.md` — `6402bd2df2f1abf85a784a17c8a727fd7e8a04ce`
- `docs/planning/handoffs/issue-1784.md` — `16ed7fff37a7ce1013053468cdd87bd70098ad4b`
- `docs/planning/handoffs/issue-1788.md` — `c6440a022a1354bd4c669ebfab00059700af7d71`
- `docs/planning/handoffs/issue-1792.md` — `d40e050c19b66cc86426370e7e593f69964841fb`
- `docs/planning/handoffs/issue-1796.md` — `d26280a5da18b248378a7460285dd03d15c8741a`
- `docs/planning/handoffs/issue-1800.md` — `1e45291b091984eea56453a6f5c40c9a89adfaea`

- Corrected `tools/planning/retire_negative_review_prs.py`: new Git blob **`9c1fcca1fd0fbb5663d27ffccb77dc09e12655d1`**, based on all 1695 original source lines, preserving untouched workflow, claims, pagination, 72h grace, SHA/head, initial and late fresh pre-PATCH readers.
- This handoff: `docs/planning/handoffs/issue-1804.md`, new path; exact blob and source PR HEAD supplied by GitHub file/PR metadata and issue terminal.

## Changes and regression matrix
- `FSR-1802-M01`: same-scheme CommonMark `https:../pull/200` and `https:/vokerg/everfield/pull/200` (inline and reference-definition) now reach the strict first-party browser-equivalent href predicate before a malformed Python-hostless disposition could lose their live PR identity.
- `FSR-1802-M02`: HTML/browser and plain PR URL readers normalize three-or-more leading slash/backslash-equivalent network-path authorities and `https:////...` to an explicit authority before exact origin/repo/PR checks, preserving foreign-host, wrong-PR and wrong-repo negatives.
- Added **eight** positive same-scheme/triple-slash/multi-backslash fixtures and **six** negative controls to the actual full module `self_test`; each positive feeds `references_pr`, live title/body/comment eligibility, both initial and late mocked `execute(apply=True)` zero-PATCH safety scenarios through the existing suite.
- Prior source CI #38911729664 was SUCCESS with writer job SKIPPED for frozen original head, but does not validate this correction. Final source branch requires a NEW hosted exact-HEAD full compile/self-test SUCCESS and mutating retire job SKIPPED; check live Actions before terminal. No independent security CLEAN may be inferred from authored tests.

## Verification, limitations, next route
This connector-side edit used the complete original source bytes and GitHub Git blobs. Locally available execution cannot mount the connector-fetched module for independent Python import; no local complete module run or live `--apply` is represented. Authored PR-triggered GitHub Actions must actually compile/run the full module at final HEAD. All PR references/checks are non-atomic relative to GitHub PATCH; no CAS guarantee. Source #1801, reviewer #1803 and historic source/review branches remain untouched OPEN/DRAFT/unmerged.

After valid source exact-head hosted CI and owner terminal `STATUS(REVIEW_READY)`, materialize **one NEW genuinely distinct** required independent full-module adversarial security review. This task owner MUST NOT self-review. Only CLEAN plus separately owned/authorized, then-current-main-compatible, expected-head SQUASH-only NONCANONICAL integration may later merge corrected source; draft/CI/review-ready do not grant any merge authority. No live PR retirement, main change, canonical, engine/readiness, gameplay, production or release authority.
