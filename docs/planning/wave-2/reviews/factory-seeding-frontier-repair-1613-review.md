# Issue #1615 — mandatory independent adversarial review of #1613

## Disposition, independent ownership and immutable scope

**CHANGES_NEEDED — 1 BLOCKER (FSR-1615-B01), 1 MAJOR (FSR-1615-M01), 0 correction-requiring MINOR.** No source integration authority. This is a required distinct negative review, **not** a producer self-test, verification, canonicalization or a merge approval.

Reviewer session `frontier-independent-review-1615-gpt6-20261011-0004-01` is genuinely distinct from source producer `frontier-remediate-1613-gpt6-20261010-2250-01`. The reviewer won the only GitHub schema-3 CLAIM on #1615, **#6101660767**, server-created and unedited at **2026-10-10T20:05:39Z**, rechecked prior to own branch creation. Reviewer branch `planning/issue-1615` starts at unchanged `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`; Issue #1147 binding terminal #5675066392, canonical blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af` were independently checked.

Source is **Issue #1613** in-lease terminal #6101067517 (GitHub 2026-10-10T18:59:15Z), frozen draft **PR #1614** HEAD `faca0341a1d73702bc384f501712a105a97c2f50`, corrected v7 blob `c35f895a0121ce329bda6f7220378c9f43e11335`, source handoff `1c9e0c58c3e15e08b5a5d41b211bf6d05afaef4d`. GitHub PR file list independently confirms **14 paths**: inherited workflow, v5/v6 and nine predecessor handoffs, plus v7 and #1613 handoff. Frozen predecessor negative #1610 REVIEW_STATUS(CHANGES_NEEDED) #6095642373 / draft PR #1612 HEAD `0c436b53b804eb34a06239fda03688c86db05414`; source #1608 PR #1609 HEAD `d65875288d1c4044dd525d8d83ee080e712c9eea`. All source and predecessor branches/PRs remain unchanged.

## FSR-1615-B01 — BLOCKER: digit-leading YAML anchors/aliases defeat semantic provenance uniqueness and verifier assertions

The final v7 `_yaml_unsafe_node_syntax` (lines 290–302) rejects anchor/alias tokens only if `&` or `*` is followed by `[A-Za-z_]`. **YAML-valid digit-leading anchor names are missed**. `_consistent_extension_alias` (352–423) then sees exactly one unquoted direct source key and returns the *lexical first value*, while a later YAML alias key resolves to the **same key** and overrides it.

Minimal independent source-faithful reproducer (the outer GitHub comment would use a `yaml` fenced capsule):

~~~yaml
protocol: planning-v1
schema: 3
kind: INTEGRATION_STATUS
unknown: &7 source_producer_issue
extensions:
  source_producer_issue: 1545
  *7: 9999
~~~

Independent Python `re` reproduction of the exact source `_yaml_mask_quoted` / `_yaml_unsafe_node_syntax` patterns: **zero unsafe lines**; `_consistent_extension_alias`'s `token` pattern finds exactly **one** `source_producer_issue:` occurrence, its `direct_pattern` also finds exactly **one** direct value `1545`, and the scalar validator accepts it. The source algorithm consequently returns **1545 / trusted**. Actual `yaml.safe_load` (PyYAML 6.0.3), by contrast, produces `{'unknown': 'source_producer_issue', 'extensions': {'source_producer_issue': 9999}}`. Both `*7:` and `*7 :` forms parse, including an explicit-key variant. A consumer cannot claim exact source identity under this semantic disagreement. The new tagged YAML regression tests do not cover digit-leading anchor names.

A second form affects the *conditional* verifier gate, even where the immutable source route does not require a verifier:

~~~yaml
protocol: planning-v1
schema: 3
kind: INTEGRATION_STATUS
context: &7 verification_issue
extensions:
  source_producer_issue: 1545
  *7: 1575
~~~

PyYAML resolves `extensions.verification_issue=1575`. The source `_required_verifier_marker` (919–976) finds no unsafe syntax, no direct `verification_issue:` literal, and no matching assertion regex; it can return **false** for a source route without `VERIFICATION`. This turns an actual semantic verifier claim into invisible provenance, bypassing verifier authentication instead of failing closed. This does **not** justify adding a global verifier requirement to sources without one; the correct rule is to reject ambiguous tagged/anchored alias syntax before provenance or conditional verifier decisions.

**Required correction:** reject every YAML anchor/alias node property independent of anchor-name first character, including numeric names, wherever authority capsules are parsed; preferably use a tightly constrained structural YAML representation/semantic-key normalization that also rejects duplicate keys and unsupported node properties. Add final-head negative fixtures for numeric key aliases shadowing a source/review identity and a verifier assertion, with a safe non-verifier scoped-source control.

## FSR-1615-M01 — MAJOR: quoted duplicate top-level authority key overrides the accepted unquoted identity

The live v7 `_integration_field` (source lines 157–171) authenticates **only a plain unquoted top-level** `^key:` and stops before `extensions:`. Neither this helper nor inherited `base.parse_operational` (which uses unquoted-first `base.scalar`) rejects a semantically duplicate quoted top-level key.

Reproducer:

~~~yaml
protocol: planning-v1
schema: 3
kind: INTEGRATION_STATUS
state: DONE
canonicality: NOT_CANONICAL
"canonicality": CANONICAL
extensions:
  source_producer_issue: 1545
~~~

Exact-source regular-expression reproduction: `_integration_field(body, "canonicality") == "NOT_CANONICAL"`, which satisfies v7 `_integration_provenance`'s accepted noncanonical values (1157–1187). Independently, `yaml.safe_load` resolves `canonicality` to **CANONICAL** because the quoted key is identical. This demonstrates a semantic contradiction in the accepted top-level status. The same direct-vs-quoted ambiguity affects source terminal/comment identity fields; the GitHub squash identity check provides an independent constraint on *physical merge* provenance but does not make contradictory authority capsules trustworthy.

**Required correction:** fail closed on duplicate/quoted/escaped/complex top-level operational authority fields, or parse all mapping-key representations into one bounded semantic identity map before authenticating them. Preserve valid ordinary schema-3 unquoted fields and exact review/verifier/source checks. Regression must show the above returns no authority.

## Independent controls and bounded confidence

1. **The prior FSR-1610 corrections do work for their declared fixtures:** source v7 explicitly rejects `!!str` / full-tag / tagged direct aliases; `_yaml_structural_lines` masks ordinary `|` / `>` verifier-looking scalar prose; `_required_verifier_marker` still recognizes ordinary scoped aliases. The newly identified **digit-leading** alias hole is narrower and separately reproducible; the quoted top-level duplicate is an additional operational-authenticity gap. No claim of an exhaustive YAML grammar proof or replay of all compiled v1–v7 Python self-tests is made.
2. **Read-only producer CI is authentic but insufficient:** GitHub `pull_request` run **38077875730 SUCCESS**, exact source HEAD, `validate-pr` job **114288550243 SUCCESS** logs `py_compile` and composed v1–v7 PASS. The job checks out merge ref `f61f885098d0ce46281738b54b28e1b2c5cea86a` with exact two parents current main `3d7ce70...` and PR head `faca0341...`. Mutation-capable `maintain` job **114288551288 SKIPPED**. These tests exercise authored fixtures, not the reproduced vulnerabilities.
3. **Real historical causal chain independently checked via GitHub comments and commit:** original source #1545 STATUS(REVIEW_READY) **#6008457546** at 2026-10-06T03:02:14Z → independent verifier #1575 VERIFICATION_STATUS(DONE) **#6008823087** at 03:37:24Z → required reviewer #1577 REVIEW_STATUS(REVIEW_READY) **#6009157969** at 04:10:25Z → separate integrator #1583 INTEGRATION_STATUS(DONE) **#6009230681** at 04:17:26Z. Original source PR #1568 HEAD `1de1155429bfa657dd6e60c4f5abc969fabd86d5` is merged by genuine single-parent squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de`, parent `e51703de82b9df3f5e676663d3a04fdc678bd5c6`. No global verifier veto, historical backfill, two-/three-target demand collapse, or newly invented product authority is implied.
4. **Owner/lease and transition interface:** the unchanged canonical 21,600-second lease, first-valid claim contention and 600-second orphan maturity are normative; v7 has prefix-scoped first-win/STale/HANDOFF predicates and checks actual one-parent squash/blob identity. The new findings are in the authority-capsule reader upstream of those protections; green existing recovery fixtures cannot establish semantic provenance uniqueness.

## Required disposition and route

Freeze **PR #1614** at exact HEAD; freeze this report's review-only draft PR. Publish an unedited schema-3 `REVIEW_STATUS(CHANGES_NEEDED)` for #1615 with **1 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**. Materialize exactly one new **bounded blocking remediation** issue against FSR-1615-B01/M01, preserving predecessor source and review provenance. Remediation must run exact-final-head read-only CI and then route to **another genuinely distinct required adversarial reviewer** before any separately owned, exact-main-compatible, **squash-only NONCANONICAL** source integration could be considered. Do not integrate or canonicalize source/review drafts on review-only authority; no gameplay, truth, consent, accessibility, engine, implementation-readiness, production or release upgrade.
