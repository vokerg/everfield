# Issue #1619 — mandatory distinct adversarial review of remediation #1617

## Disposition and independent scope

**CHANGES_NEEDED — 1 BLOCKER (FSR-1619-B01), 1 MAJOR (FSR-1619-M01), 0 correction-requiring MINOR.** This is a required independent negative review, not source acceptance, a verifier decision, canonicalization, or source integration.

The reviewer is `frontier-independent-review-1619-gpt6-20261011-0249-01`, distinct from producer `frontier-remediate-1617-gpt6-20261011-0015-01`. The only first-valid reviewer CLAIM is GitHub comment **6103923116**, server-created and unedited **2026-10-11T00:50:35Z**. Reviewer branch `planning/issue-1619` originates at `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`; canonical Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Source Issue #1617 terminal **6101793350**, frozen draft PR **#1618** HEAD `e78249c7eb7acd87fa5654875e9d74e208b91159`, v7 blob `9646a8ceca5dfeb56303d10d553e8137500549c3`. Exactly 15 source changed paths: 13 pinned inherited artifacts, corrected v7 and #1617 handoff. Earlier source PR #1614, negative review-only PR #1616 and their frozen heads remain untouched.

## FSR-1619-B01 — BLOCKER: legal whitespace before YAML colon hides map shadow and scoped verifier assertion

The final v7 `_consistent_extension_alias` (lines 371–443) counts top-level `extensions:` declarations using a header regex requiring the colon **immediately** after the unquoted or quoted key. YAML also permits a space before the colon. Consequently an ordinary later `extensions : null` semantically replaces the original extensions mapping but is not counted as another header. The first direct source alias is still accepted. Minimal capsule (add the normal GitHub fenced YAML envelope):

```yaml
extensions:
  source_producer_issue: 1545
extensions : null
```

Independent PyYAML 6.0.3 `safe_load` returns `{'extensions': None}`. An independently transcribed source-faithful execution of `_yaml_structural_lines`, `_yaml_mapping_structure`, `_yaml_unsafe_node_syntax` and `_consistent_extension_alias` on the frozen source patterns returns **`1545`**. Neither numeric-anchor correction nor escaped-key rejection detects this completely ordinary, untagged, unanchored semantic duplicate.

The same lexical disagreement can conceal a *real* scoped verifier declaration when the source route has no explicit `VERIFICATION` requirement:

```yaml
extensions:
  source_producer_issue: 1545
  verification_issue : 1575
```

PyYAML returns `extensions.verification_issue = 1575`. However `_consistent_extension_alias(..., ('verification_issue',))` returns None: its token count sees `verification_issue\s*:` but direct-child pattern requires `verification_issue:`. `_required_verifier_marker` (lines 938–996) also requires immediate colon in its marker regex and therefore returns **False** when the frozen source's required-next-route does not contain VERIFICATION. An actual verifier assertion becomes invisible, rather than authenticated or rejected. This is a **conditional authentication defect**, not a basis for imposing a global verifier requirement on verifier-free scoped sources.

Required correction: detect the semantic map key before trusting any source/reviewer/verifier/integrator alias; recognize or fail closed on YAML-valid whitespace around mapping-key separators for all root/extension authority fields. Count semantic duplicate `extensions` maps and fail closed on ambiguous or unsupported keyed forms. Require valid asserted verifier keys (including spaced forms) to activate authentication, while preserving truly verifier-free scoped sources and literal/folded scalar prose.

## FSR-1619-M01 — MAJOR: spaced quoted top-level authority override passes canonicality reader

The final v7 `_integration_field` (lines 151–184) requires an authority key's colon to be adjacent in `variants.fullmatch` and in the legacy root extraction. A second, semantically identical quoted root key with a space before its colon is skipped while the first lexical authority wins:

```yaml
protocol: planning-v1
schema: 3
kind: INTEGRATION_STATUS
canonicality: NOT_CANONICAL
"canonicality" : CANONICAL
extensions:
  source_producer_issue: 1545
```

The frozen reader's independently transcribed patterns return **`NOT_CANONICAL`**, which satisfies `_integration_provenance`'s noncanonical allowlist. PyYAML 6.0.3 returns **`CANONICAL`**. This contradicts authenticated identity despite the preceding remediation's tests for `"canonicality":` with an adjacent colon. Equivalent spacing can shadow other root operational fields (state, source/review IDs, ownership/PR and squash provenance); the existing physical-squash check does not repair contradictory provenance text.

Required correction: fail closed on quoted/unquoted/spaced semantic duplicate root operational authority identities regardless of position relative to `extensions`; retain valid single ordinary declarations. Add independent adversarial fixtures for both key orderings, comments, quoted and unquoted keys, extra spaces/tabs and scoped no-verifier controls.

## Evidence, controls and authority limits

- Frozen source PR #1618 final-head `pull_request` run **38083305896 SUCCESS**, read-only `validate-pr` job **114304505452 SUCCESS** (compile and composed v1–v7 self-tests); mutation-capable `maintain` **114304506171 SKIPPED**. Its checkout merge ref `23cb4331faad9bed1ac82256dcb10ce589affbe7` corresponds to the unchanged main and frozen head. All 15 changed files and immutable blobs were inspected through GitHub's PR file API, including v5 `babdd29389e06bc922d33bc285c82315fec8c237`, v6 `da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03`, and workflow `999671d1ede00a25c66bd63d25bcdc14e4a9d40b`. Green source-owned regressions are genuine but do not exercise the above counterexamples.
- The previous FSR-1615-B01 numeric `&7/*7` and FSR-1615-M01 immediate-colon quoted top-level duplicate cases are closed *for their literal tested forms*. The new defects are not evidence that all prior corrected paths fail. The ordinary single declaration `canonicality: NOT_CANONICAL` and `extensions.source_producer_issue: 1545` remains accepted in the independent reproduction.
- Historical legitimate causality was cross-checked against actual GitHub terminal comments: source #1545/#6008457546 → verifier #1575/#6008823087 → distinct reviewer #1577/#6009157969 → separate integrator #1583/#6009230681; actual squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de` has exactly one parent `e51703de82b9df3f5e676663d3a04fdc678bd5c6` and six published source paths. This chain must remain accepted under its genuine scoped requirements.
- This review specifically reproduces upstream YAML mapping-identity defects. It does **not** assert complete independent execution of all composed v1–v7 tests or a general YAML parser proof. Existing valid first-claim/STALE/HANDOFF/ORPHAN and v5/v6 multi-target/bounded-demand behavior must remain regression-protected. No speculative historical backfill, global unrelated blocked-work veto, gameplay authorization, canonicality or readiness upgrade is justified.

## Mandatory disposition and next route

Freeze source PR #1618 at exact HEAD and this reviewer-only draft. Publish in-lease unedited schema-3 `REVIEW_STATUS(CHANGES_NEEDED)` for #1619 (**1 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**). Materialize **one** fresh bounded blocking remediation successor for FSR-1619-B01/M01, inherit the exact #1618 packet, correct only v7 and add its own handoff, then require new exact-final-head read-only CI and another genuinely distinct mandatory independent reviewer. A separate owner-authorized exact-current-main-compatible squash-only **NONCANONICAL** publication could be considered only after an independently clean review; neither this reviewer nor its draft PR may integrate source. No verification, canonical, gameplay, truth/consent/accessibility, implementation-readiness, engine, production or release authority.
