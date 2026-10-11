# Required independent adversarial review — Issue #1628 / PR #1631

**Disposition: CHANGES_NEEDED — 1 BLOCKER (FSR-1632-B01), 0 MAJOR, 0 correction-requiring MINOR.** This is an independent reviewer-only assessment, not source verification, a review waiver, integration authority, or canonicalization.

## Scope, frozen identities and review authority

- Reviewer Issue #1632, winner schema-3 CLAIM #6107307058, actor `frontier-independent-review-1632-gpt6-20261011-1050-01`; independently distinct from producer `frontier-remediate-1628-gpt6-20261011-0933-01`, which owned Issue #1628 CLAIM #6106714285 and terminal #6106754904.
- Canonical Issue #1147 binding #5675066392: program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`; exact current main `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d` descends from activation.
- Source PR #1631 remains open **draft**, exact head `27d452fe5ae03dd822e8fc357d6b72cc48913698`, base `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`. Source base parser blob `37841faa17d82e798b90a192d972ded9ae29c5e2`, v7 blob `28af0a1eeeddcc318b1faeca76c82dfd1efbed87`, owner handoff `4267c53c62396fd556b43364b8bcbf06f3a122c2`. Changed paths: 18 (15 inherited, 2 parser files, 1 new handoff). Source's exact PR files API confirmed these identities.
- Negative parent review Issue #1623 terminal #6106678132 / review-only PR #1625 `ca9aa3a4f12b5983ee223f9a547bae4daf27cec4`; frozen prior source #1621 / PR #1622 `18a23b61d4fafd68d0def4c8fe8cfcc34ac4139e`. All must remain unmerged and unchanged.
- Actions run #38121977583 was a real successful `pull_request` at exact source head; `validate-pr` #114418397061 SUCCESS and mutating `maintain` #114418397768 SKIPPED. Checkout merge-ref `310f37c88da24767d7ebeb730e93db1cd190711f` has exact parents main `3d7ce70...` and source `27d452fe...`, tree `ec069d8677b732af3f79ed9614b1efcca3eb471c`. Green producer CI is not independent approval.
- Genuine historical noncanonical implementation source #1545 (terminal #6008457546), verifier #1575 (#6008823087), required reviewer #1577 (#6009157969) and distinct integrator #1583 (#6009230681) still identify source PR #1568 HEAD `1de1155429bfa657dd6e60c4f5abc969fabd86d5` and real single-parent squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de` with parent `e51703de82b9df3f5e676663d3a04fdc678bd5c6`. The review does not alter that published history.

## Independent method and results

Inspected exact GitHub source blobs for `base.yaml_scalar_identity` (lines 136–158), `base.scalar` (161–163), `base.parse_operational` (403–429), `base.reconcilable_terminal_from_comments` (441–481), v7 `_integration_field` (151–187), `_yaml_structural_lines` (338–363), `_consistent_extension_alias` (385–459), `_required_verifier_marker` (955–1012) and causal/squash gates. Compared concrete YAML semantics using **PyYAML 6.0.3** with a locally executed faithful extraction of the exact short base helper functions and terminal predicate; this was not a claimed end-to-end execution of the repository-wide workflow.

**Positive FSR-1623-B01 correction:** the new `yaml_scalar_identity` decodes at most one ordinary YAML quoting layer. `planning-v1`, `'planning-v1'`, `"planning-v1"` return the intended trusted string. A YAML single-quoted scalar enclosing embedded double-quote characters, or a YAML double-quoted scalar enclosing embedded single-quote characters, preserves those inner characters as data, so it cannot masquerade as the unquoted trusted token. The same principle now applies to `_integration_field`, which delegates to the shared identity helper. Unicode JSON escape `"\\u0070lanning-v1"` decodes once to `planning-v1`; malformed unterminated quotation returns `None`. This resolves the earlier *particular* two-layer stripping behavior on the inspected paths. Unsupported YAML double-quoted escape forms fail closed, not accepted as trusted authority.

**Negative FSR-1632-B01 (BLOCKER) — nested extension authority becomes a trusted root operational record.** The amended shared `base.scalar` still uses `re.search(r"(?m)^\\s*KEY:...")` against the **whole raw comment**. `\\s*` includes indentation and newlines. Neither that function nor `base.parse_operational` enforces exactly one root mapping or a YAML capsule boundary. A legitimate YAML document with only an `extensions` map can therefore be recognized as a root schema-3 CLAIM or STATUS. Reproduction (each is a separate trusted, unedited OWNER GitHub comment with ID 1 or 2 and valid ordered `created_at == updated_at`; IDs are illustrative):

```yaml
# Comment 1 — no operational top-level fields
extensions:
  protocol: planning-v1
  schema: 3
  kind: CLAIM
  issue: 9301
  mission_id: M-9301
  actor_session_id: example-owner
  state: IN_PROGRESS
```

```yaml
# Comment 2 — also no operational top-level fields
extensions:
  protocol: planning-v1
  schema: 3
  kind: STATUS
  issue: 9301
  mission_id: M-9301
  actor_session_id: example-owner
  state: DONE
  authority_mode: OWNER
  ownership_generation_comment_id: 1
  head_sha: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  work_sha: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
```

When each document is enclosed in the normal `\`\`\`yaml` comment fence, `yaml.safe_load` returns only the root key `extensions`, **never** a root `protocol`, `schema`, `kind`, or `state`. The exact amended `base.scalar` nevertheless resolves all those fields from the nested children; `base.parse_operational` produces `CLAIM` and `STATUS(DONE)` objects. The reproduced exact acceptance predicate in `reconcilable_terminal_from_comments(9301, [comment1, comment2])` returns the forged terminal (non-`None`). That path feeds `close_terminal_open_issues` (around lines 648–664): a trusted collaborator's sample/foreign nested metadata can cause a **false task closure** without a schema-3 root record or valid canonical ownership. This is an authority/terminal safety failure, not cosmetic parsing. The root/nested ambiguity predates the immediate scalar change, but it remains in the modified shared parser and explicitly violates Issue #1632's mandatory base-parser trust-boundary challenge. No arbitrary untrusted public commenter exploit or real GitHub task closure was attempted or claimed.

An additional lexical attack surface is YAML literal/folded block prose or a second fenced/prose section with `^\\s*`-matched lines; block prose must never borrow root authority. The concrete nested two-comment fixture above alone is sufficient for BLOCKER. Whether other v7 contextual gates reject some forged values does not cure base-level automated terminal reconciliation.

## Required correction and re-review boundary

1. Repair the *shared base* operational reader, not merely v7: strictly authenticate the one root YAML capsule, top-level field identity/cardinality, direct scalar values, semantic duplicate/shadow keys, and reject authority inherited from `extensions`, nested sequence/flow mappings, prose, block scalars, or an unrelated fenced example. Fail closed on unsupported syntax without losing valid ordinary root fields or canonical lease provenance.
2. Add executable negative regression on the exact two-comment fixture: `base.parse_operational` must return `None` and `reconcilable_terminal_from_comments` must not close the issue. Add positive original root CLAIM/STATUS and scalar single-quote/double-quote controls; verify layered quote rejection, aliases, shadow keys, verifier-free scoped source, explicit verifier assertions, ownership six-hour lease and real squash provenance remain sound.
3. Freeze this source PR and this reviewer-only PR. Create one new bounded remediation issue from then-current main, amend only authorized inherited packet/parser/handoff paths, rerun exact-final-head genuine read-only `pull_request` CI, and obtain a **new genuinely independent** required adversarial review before any separately authorized squash-only **NONCANONICAL** publication. Review-only documentation is never the source to integrate.

## Findings, limitations, authority

| ID | Severity | Finding | Required outcome |
| --- | --- | --- | --- |
| FSR-1632-B01 | BLOCKER | Indented `extensions` child fields can produce false root CLAIM and STATUS(DONE), including maintenance issue closure | Root-scoped semantic operational parser + negative/positive exact fixtures, fresh final-head CI and new required independent review |

No additional MAJOR or correction-requiring MINOR was established. Source's layered-scalar fix is favorable but **overall independent review is CHANGES_NEEDED**. Original v5 multi-target demand, v6 bounded routing, v7 scoped no-global-veto policy and previously integrated original source remain protected by non-expansion; this report does not assert a broad new global verifier gate. No gameplay, canon, engine, implementation-readiness, production, accessibility, decision, or release authority is conveyed.

**Required next route:** `MATERIALIZE_FRESH_BOUNDED_BLOCKING_REMEDIATION_OF_FSR_1632_B01_THEN_EXACT_FINAL_HEAD_READ_ONLY_CI_AND_NEW_DISTINCT_REQUIRED_ADVERSARIAL_REVIEW`.
