# Required independent adversarial review — Issue #1602 / source #1600

## Disposition
**CHANGES_NEEDED — 1 BLOCKER, 2 MAJOR, 0 correction-requiring MINOR.** Do **not** integrate frozen producer PR #1601. The producer's exact-head read-only CI is green, but the reviewed parser still accepts structurally invalid authority capsules and inconsistently interprets valid aliases. Independent negative reproduction below is separate from producer-authored tests.

**Reviewer isolation.** Mission `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-06-REV-01`. Winning first-valid schema-3 CLAIM #6095162752, actor `frontier-required-review-1602-gpt6-20261010-0932-01`, GitHub server `2026-10-10T07:34:02Z`; independent of recovered producer `frontier-recover-1600-gpt6-20261010-0608-01` and original producer `frontier-remediate-1600-gpt6-20261009-2132-01`. Immediately rechecked contention: later claims #6095163104 (07:34:04Z) and #6095165434 (07:34:18Z) lose to the earlier unedited, structurally valid CLAIM. All work is review-only on own branch `planning/issue-1602`, created from `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`. No source or predecessor mutation.

Canonical Issue #1147 terminal #5675066392 binds current program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af` (confirmed ancestor of main). Frozen source Issue #1600 unedited recovered-owner terminal #6093645375 (`2026-10-10T04:12:54Z`) and open draft PR #1601 HEAD `ddd695c42f99805100430e494cfa72db9f12c2f8`; source terminal ownership RECOVER #6093622351, earlier valid first CLAIM #6085975637, STALE intent #6093620686 and in-lease HEAD_ADVANCE #6093635784. Exact source v7 blob `af7f04e9387e06c2f48daf5002566c678f9fd347`.

## FSR-1602-B01 — BLOCKER: duplicate/shadow top-level extensions declarations accepted

Frozen v7 `_consistent_extension_alias` lines 239–250 counts **only** headers matching the regex `(?:extensions|'extensions'|"extensions"):[ \\t]*` **with an empty right-hand side**. It ignores another top-level `extensions: {unexpected: shadow}`, `extensions: null`, `extensions: []`, or `"extensions": {}`; lines 263–283 can then trust a recognized direct child from the *first* map. This contradicts the required sole top-level mapping and schema-3 fail-closed authority rule. The canonical lightweight `base.parse_operational` (`frontier_maintenance.py` lines 382–412) is regex-based, not a duplicate-key YAML validator, so it does not independently repair this hole.

Independently authored Python reproduction of **the frozen source's** `_yaml_without_comment`, `_yaml_alias_scalar` and `_consistent_extension_alias` logic produced `1545` (accepted) in all three adversarial capsules below. Expected: `None` / structurally invalid.

```yaml
# A — second top-level flow map shadows trusted first mapping
extensions:
  original_source_issue: 1545
extensions: {unexpected: shadow}
```

```yaml
# B — second top-level null shadows trusted first mapping
extensions:
  original_source_issue: 1545
extensions: null
```

```yaml
# C — alternate quoted spelling of duplicate top-level key
extensions:
  original_source_issue: 1545
"extensions": {}
```

The independent reference `yaml.safe_load` experiments returned, respectively, `{'extensions': {'unexpected': 'shadow'}}`, `{'extensions': None}`, and `{'extensions': {}}`: none retains the trusted original source ID. This is an exploitable trust-boundary mismatch for integration/source/review/verifier alias groups, rather than merely a cosmetic error. Reject **every** second top-level `extensions` key independent of its value, quoting, comments, flow syntax or other alias presence.

## FSR-1602-M01 — MAJOR: downstream scalar reader rejects supported commented/quoted headers

Frozen `_consistent_extension_alias` lines 239–246 deliberately accepts `extensions: # legitimate comment` and `"extensions":`. Yet v7 `_extension_field` lines 169–178 demands the literal substring `\nextensions:\n`. Required review `_exact_causal_source_review` lines 711–721 consumes `disposition`, `blocker_count`, `major_count`, `correction_requiring_minor_count`, `required_review_disposition` through that older parser; verifier `_exact_required_verifier` lines 932–944 likewise consumes `result` and disposition. A legitimate clean required-review terminal with a commented or quoted extensions header is recognized by alias matching but rejected as missing disposition/count fields.

Independent probe: `_consistent_extension_alias` returned `1545` for each of:

```yaml
extensions: # permitted inline header comment
  original_source_issue: 1545
  required_review_disposition: CLEAN_FOR_TEST
```

```yaml
"extensions":
  original_source_issue: 1545
  required_review_disposition: CLEAN_FOR_TEST
```

In both cases frozen `_extension_field(body, "required_review_disposition")` returned `None` rather than `CLEAN_FOR_TEST`. This creates valid-source liveness false negatives across accepted direct-header representations; a simple regex fix must not open nested, null, duplicate or flow structures.

## FSR-1602-M02 — MAJOR: quoted verifier marker can bypass conditional verifier validation

Frozen v7 `_required_verifier_marker` lines 779–802 searches for unquoted bare field names with `^[ \\t]*key:\s*`. Independently authored variants with `'independent_verifier_issue': 1575` and `"independent_verifier_issue": 1575` both returned **false**, whereas the equivalent unquoted key returned **true**. But `_consistent_extension_alias` explicitly recognizes both quoted direct scalar keys. In a source whose `required_next_route` lacks literal `VERIFICATION`, a quoted integration verifier identity is therefore silently skipped instead of activating `_exact_required_verifier` authentication (lines 725–736). An explicit verifier provenance claim must not bypass verification merely because of a YAML-valid key spelling. This does **not** establish bypass of the original #1545 chain, whose route does require verification; it is a distinct prospective trust regression.

## Independent safety/compatibility checks

- **Source freeze and diff.** Independently fetched PR #1601's GitHub paginated changed-file list: exactly 11 allowed paths. Exact SHA matches: workflow `999671d1ede00a25c66bd63d25bcdc14e4a9d40b`; v5 `babdd29389e06bc922d33bc285c82315fec8c237`; v6 `da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03`; v7 `af7f04e9387e06c2f48daf5002566c678f9fd347`; inherited handoffs #1556 `ea2fce80a21d932a0f8f41d261abd85aa814775a`, #1570 `98744c4c302a4abca7e67d36301acf6ee16b5e6d`, #1579 `06b2ab2ff4d3a09778de4809f77edd6d5f47684a`, #1585 `53422ac29b568f42edc16d30488be744c5f273c2`, #1591 `3908f26b92cccd77b9ad65e2fab8ecc130062e51`, #1596 `b74e545b7f99b24ab8d0be391124f787666d8ff5`; successor handoff `1c6989faa5f925f5c3efb1f47a8a8f5c4a747af9`. No gameplay path. Frozen predecessor PR #1597 remains draft HEAD `c46c32aa03eb261c5438a5f96b335aee8cc793cb`, negative reviewer PR #1599 remains draft HEAD `a32b0fe6e2d8f6a5a9c36bb1797689dc31951238`.
- **Actual GitHub CI.** PR workflow run #38023197873 was `pull_request` at exact source HEAD `ddd695c42f99805100430e494cfa72db9f12c2f8`, conclusion success. Job #114128424385 `validate-pr` success; independently inspected logs show checkout `refs/remotes/pull/1601/merge`, actual merge ref `3a40c50f235852a04fab81ed8e7474a3a409cfe5` merging source into exact current main `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`; Python py_compile and composed v1–v7 self-tests all PASS. Mutation-capable job #114128425117 was SKIPPED. These authored tests did **not** include the adversarial cases above.
- **Actual reviewed source continuity.** Re-fetched unedited live terminals #1545 `STATUS(REVIEW_READY)` #6008457546 (2026-10-06T03:02:14Z), #1575 required `VERIFICATION_STATUS(DONE)` #6008823087 (03:37:24Z), #1577 required `REVIEW_STATUS(REVIEW_READY)` #6009157969 (04:10:25Z), #1583 owner `INTEGRATION_STATUS(DONE)` #6009230681 (04:17:26Z). Original source PR #1568 retains HEAD `1de1155429bfa657dd6e60c4f5abc969fabd86d5`, merged by single-parent squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de` parent `e51703de82b9df3f5e676663d3a04fdc678bd5c6`. Source, review and verifier provenance aliases exist in real records. No regression claim is made against these real plain-header terminals.
- **Ended owner generation.** Frozen v7 `_valid_owner_terminal` lines 532–587 includes recursively prefix-scoped validation of earlier valid terminal kinds (564–575); invalid later records are not automatically given authority, and valid HANDOFF/STALE transitions are separately checked. Static and authored-CI evidence suggests FSR-1598-B01 was addressed, but these observations are not a claim of independently replaying every ownership generation fixture. Negative alias findings already prohibit clean disposition.
- **Scope and gates.** No modification of producer, verification, canonical program, engine choice, gameplay, truth, consent, accessibility, readiness, production, or release state. This report is a review-only evidence artifact; its future draft PR is not an integration surface. Under the canonical scoped dependency model, negative review blocks only the source chain requiring correction; do not invent a global gate against unrelated scoped completion.

## Required next route

After an unedited, current-owner, in-lease schema-3 `REVIEW_STATUS(CHANGES_NEEDED)` binds this review report, the handoff and exact own draft review PR/head, materialize a **bounded mandatory blocking remediation successor** for FSR-1602-B01/M01/M02, starting from then-current main in a fresh single-owned branch and keeping #1601, #1597 and #1599 frozen. Require independently authored adversarial alias fixtures plus ended-owner-generation regression, exact-head read-only CI with skipped mutating job, and a **new distinct mandatory review**. No source or review PR integration is authorized by this verdict.
