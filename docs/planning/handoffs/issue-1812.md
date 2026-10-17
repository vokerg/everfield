# Issue #1812 — CommonMark autolink retirement-reference remediation

## First-winner ownership, prerequisites and scope
- Mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-22`. First uncontested, unedited schema-3 CLAIM **#6232411810**, GitHub server created_at=2026-10-17T09:41:58Z, actor `everfield-commonmark-autolink-rem22-gpt6-20261017-01`; new branch `planning/issue-1812` from exact `main@7da4c2d50412fe134c8632264908560b8b7995ce`. Recheck contention and six-hour lease before any terminal.
- Canonical Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Frozen source #1804 `STATUS(REVIEW_READY)` #6232304061, original OPEN/DRAFT PR #1805 head `7bcaf1481f4f137e61bc3f2a3f18ce3d48ddfd5a`, source module blob `9c1fcca1fd0fbb5663d27ffccb77dc09e12655d1`. Authored exact-head run #39021277234 and full-source test job #117363417274 SUCCESS; write-capable retirement job #117363447239 SKIPPED. Independent negative review Issue #1807 terminal #6232390059 (0 BLOCKER/1 MAJOR `FSR-1807-M01`/0 correction-requiring MINOR), reviewer-only OPEN/DRAFT PR #1810 head `62282a256ad397d94a338a8ec620369ebf673661`, report blob `422b3bb6b437c81e17a1a64ce2e61a6564d0d911`. Those source and reviewer branches are frozen, not modified.

## Exact 18-file proposed source packet
All **16** frozen non-script blobs inherited from existing PR #1805, using identical Git blob SHAs:

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
- `docs/planning/handoffs/issue-1804.md` — `0d8b804ba23575b28b7b4dd1c1e5a3114576ef9a`

- Only corrected `tools/planning/retire_negative_review_prs.py` blob **`b0f3ef2361b6d59d366c8fba5491a902851d9834`**.
- Own newly added `docs/planning/handoffs/issue-1812.md`, exact blob published as GitHub PR file metadata. No workflow, existing handoff, preexisting source/reviewer branch, game, canon or main edit.

## Fix and test additions
- `FSR-1807-M01`: real CommonMark automatic angle URL `<https:../pull/200>` or `<https:/vokerg/everfield/pull/200>` is clickable after Markdown render and WHATWG normalization, yet none of the three existing readers recognized this original Markdown syntax. Detect literal non-escaped angle HTTPS/HTTP autolink targets, skip recognized HTML comments, CommonMark fenced code and same-line backtick code spans, and resolve candidate using the existing strict HTML href first-party origin/repo/PR/port/encoded-dot/browser path predicate before issue/title/body/comment veto. An ambiguous first-party candidate fails closed via inherited safety rules.
- Added **five** new positive automatic-angle URL fixtures to actual full module `--self-test` covering relative same-scheme, root-path same-scheme, plus/zero PR alias `.diff`, `.patch` subresource, and HTTPS multi-slash authority. The inherited suite tests every positive in full `references_pr`, title/body/comment eligibility, and initial/late mocked `execute(apply=True)` no-PATCH checks. Added **nine** strict negative controls: wrong PR/route/repo/foreign origin, HTML-commented URL, fenced code, inline code and escaped angle. All older positives/negatives, 72h grace, pagination, ownership/schema-3, first-winner/lease, GitHub SHA/PR identity, and final reread protections retained.
- Source edited via immutable GitHub connector blobs; an isolated local Python environment could not import the connector-fetched full module. Do not claim local full-source PASS. **Exact-final-head hosted Actions compile and full `--self-test` SUCCESS and write-capable retire job SKIPPED remain REQUIRED** before source owner REVIEW_READY. Author-authored tests cannot substitute for genuinely distinct adversarial security CLEAN.
- Non-atomic GitHub GET/PATCH race is unavoidable. No actual live `--apply`, PATCH, closure or merging permitted.

## Immutable next gates and prohibitions
1. Publish exact 18-path OPEN/DRAFT source PR from this owned branch, confirm main/PR head and all 16 inherited blob identities; run exact-final-head hosted full compile/self-test and verify mutating retirement job SKIPPED.
2. Only if hosted CI PASS and first owner's six-hour generation remains valid, publish in-lease schema-3 `STATUS(REVIEW_READY)` with exact PR head, work SHA, artifact paths and run/job IDs.
3. Materialize exactly **one genuinely distinct** mandatory full-module adversarial reviewer on a fresh reviewer-only two-doc branch/OPEN-DRAFT PR. Source owner here may never approve own source work. Even CLEAN alone grants no integration; later source integration is separately owner-claimed, authorized, compatible-current-main, exact-head **SQUASH-only NONCANONICAL**. Reviewer-only PRs remain permanently nonintegrable.
4. No original source/reviewer branch edit, live PR retirement or GitHub mutation, canonicality, gameplay, engine, readiness, production or release authority.
