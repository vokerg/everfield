# Issue #1661 — independent required adversarial review of #1656

## Status, owner, verdict

**CHANGES_NEEDED: 1 BLOCKER (FSR-1661-B01), 1 MAJOR (FSR-1661-M01), 0 correction-requiring MINOR.** Required distinct adversarial review of immutable source Issue #1656 / PR #1660. First and sole valid GitHub-server CLAIM #6112190505 (2026-10-11T18:21:24Z), reviewer actor `frontier-independent-scalar-list-review-1661-gpt6-20261011-2019-cph-01`, genuinely separate from producer, prior negative reviewer, and routing materialization executions. Current task branch `planning/issue-1661` based on main `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`. This is **not** source authoring, producer CI, author self-review, independent complete-module execution, publication, implementation-readiness or canon.

**Immutable review report:** `docs/planning/wave-2/reviews/factory-seeding-frontier-repair-1656-review.md`, Git blob `0522c7c4096a16d23ca67b7e6bc4bddbd3cc6c75`; first review evidence commit `0b26b5e11e9b860c73087680c9a224c085160a06`. Exactly two reviewer-owned paths: that new report and this new handoff; branch and review-only DRAFT PR head, PR number, handoff blob, terminal time and full immutable evidence are bound by the final operational GitHub comment after writes. No source or main changes.

## Exact frozen input and verified scope

- GitHub current `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`; canonical #1147 binding #5675066392 and current program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Source #1656 schema-3 owner `STATUS(REVIEW_READY)` #6109748773, source DRAFT PR #1660 unchanged exact head `3d5ebe385d4af096e04520fb3977d3e900bac87b`. Corrected parser blob `2a8bbc64d200ffa2ac4711ea0dbdf8a7c070ed33`; producer handoff `072026d7d4d820552da16afe4b1593dd51aa473d`.
- Prior #1647 source DRAFT PR #1648 head `4059ee74e96e064f8a99bd011ef9f33f9867a6ad`, required distinct negative #1650 terminal #6108889365 / DRAFT PR #1652 head `021fafc34c3fe632bd05072a9dccd4a4f4281fc0`.
- Independently enumerated GitHub changed paths: 21 in #1660, 20 in #1648; 19 inherited paths byte-identical; only modified base parser plus new producer handoff. Main and source heads were independently refetched before claim and reviewer report write.
- Source exact-head GitHub Actions PR run #38144885280 / job #114486051232 SUCCESS; mutating maintenance job #114486051711 SKIPPED. Evidence of producer self-test only, not independent review PASS.

## Actual negative findings and reproducibility

**FSR-1650-B01 scalar->singleton fix is real:** corrected base `list_scalar` rejects plain and quoted direct root scalar `evidence_refs` and `artifact_paths`, recognizes actual indented/flow sequences and rejects nested-only lists. However the independent review found:

1. **FSR-1661-B01 BLOCKER — invalid YAML accepted as operational authority.** Complete root `PROGRESS(EVIDENCE)` comment containing `evidence_refs: [<40-hex-SHA>]\n  injected: yes` fails independently executed PyYAML 6.0.3 `safe_load` with ParserError. At exact frozen parser `_root_mapping_fields` ignores the invalid indented child, `list_scalar` returns the SHA from the flow list, and the lease logic accepts it as valid EVIDENCE. CLAIM 00:00Z; forged malformed PROGRESS 05:59Z; STALE 06:01Z incorrectly appears unexpired (nonrenewed expiration 06:00Z). The same unchecked list extraction feeds v7 source/reviewer/verifier file identity via `artifact_paths` at lines 941/945/1173. This is not the original plain-scalar-vs-list defect; it is whole-document structural validity.
2. **FSR-1661-M01 MAJOR — unauthenticated HEAD_ADVANCE.** The exact frozen `schema3_ownership_lease_state` at lines 389–397 treats any `observed_head_sha` different from internally remembered SHA as a real branch advance. It never proves the asserted new SHA against actual GitHub task-branch movement; even producer test calls literal `a*40 -> b*40` a real advance with no branch/ref proof. An invented SHA can renew six-hour ownership and defeat premature STALE if there is no independent branch check.

Report includes a complete malformed schema-3 witness, PyYAML error, exact source line-by-line provenance, and a frozen-module reproduction snippet to execute in later corrected CI. Local independent testing executed **PyYAML 6.0.3**, and review independently inspected the exact GitHub source and CI metadata; the full frozen module was **not** imported or executed locally because the restricted executor cannot clone via DNS. The report distinguishes source self-test coverage from independent executable checks. A future verifier must perform both full-module and v7 adversarial negatives on a corrected exact final head rather than borrow this review as an execution PASS.

## Required liveness transition, no merge authority

After publishing accurate terminal `REVIEW_STATUS(CHANGES_NEEDED)` bound to the exact reviewer-only draft PR, **materialize exactly one mandatory bounded blocking remediation issue** for FSR-1661-B01 and FSR-1661-M01. It must preserve source #1660 and all predecessor review/source/verifier drafts frozen, carry the 19 identical blob inheritance, fail-closed validate whole YAML before operational list authority and authenticate actual HEAD_ADVANCE, add meaningful specific negatives plus original scalar cardinality and six-hour/600s boundaries, obtain exact-final-head read-only CI and a *new separate genuinely independent required adversarial review*. Avoid multiple optional reviews/new issues and avoid global gameplay gates.

Only a separately owner-authorized and current-main-compatible **squash-only NONCANONICAL** source integration after all reviews can publish fixed source. Keep review-only DRAFT PR open and unmerged; never merge it as source. Review has no gameplay/truth/consent/accessibility, final engine, implementation-readiness, production, release, canon, or source-integration authority.
