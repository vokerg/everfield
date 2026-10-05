# Independent required review — factory seeding repair #1556 / reviewer #1562

## Immutable subject, trust and independent scope

- **Reviewed producer**: Issue #1556 mission `FACTORY-SEEDING-FRONTIER-REPAIR-01`, winning CLAIM **5999767236**, owner-terminal `STATUS(REVIEW_READY)` **5999918761**, source **draft PR #1560** frozen head **`f844a628dc2f76746541375eec6b345a637e9b8e`**, original main base `781d65ca07c7b410faaecfa1e8cbfd6f5fc8ed48`. Producer session: `factory-seeding-repair-1556-gpt56sol-20261005-01`.
- **Independent reviewer**: Issue #1562, first valid CLAIM **5999935364**, distinct session `frontier-review-seeder-repair-1562-gpt56sol-20261005-1947-01`. Review branch `planning/issue-1562` started at then-current `main@6d601848c4c29734f319e47611390303fd351ed3`. Canonical Planning Program #1147 binding **5675066392**, program blob **`fd4cf1119c3f86acc3af620024eea72235e81ce4`**, activation ancestor **`87c85cecfa9a2ffa464c4b36816a138bf41441af`** unchanged by disjoint #1558/#1561 noncanonical component publications. No producer-file edits, gameplay edits, main integration or producer self-review.
- **Exactly five source PR changed paths**, confirmed independently from frozen PR diff and blobs: `.github/workflows/planning-frontier-maintenance.yml`, `docs/planning/handoffs/issue-1556.md`, and `tools/planning/frontier_maintenance_v5.py`, `frontier_maintenance_v6.py`, `frontier_maintenance_v7.py`. They do not overlap the intervening #1543/#1544 three-file source squashes.

## Accepted evidence, positive/negative test coverage

GitHub Actions **pull_request** run **37350795349**, attempt 1, exact original PR `head_sha=f844a628dc2f76746541375eec6b345a637e9b8e`, completed **success**. Read-only `validate-pr` job **111900829530** completed success; potentially mutating `maintain` job **111900831793** was **skipped**. Log confirms checkout of `refs/remotes/pull/1560/merge`, not a falsely claimed checkout of original PR HEAD; `py_compile` of all maintenance scripts succeeded and composed maintenance **v1 through v7 self-tests each emitted PASS**. An earlier cancelled run (37350518969) is not a passing test and was not substituted. The workflow's PR job has only `contents: read` and skips maintenance on `pull_request`; job concurrency is partitioned from `live` to avoid old PR cancellation.

Full five-path diff reviewed, including:
- v5: explicit two/three-successor grammar for #1543/#1544/#1545 and #1547/#1548; all named targets must be present, trusted and eligible; invalid/0/duplicate/rejected/closed-wrapper/untrusted targets fail closed, existing one-successor API retains ambiguity `None`. The tests attack partial multi-target, rejected/duplicate, spoofed author and factory-wrapper identities, no false terminal route from mixed `REVIEW_` or `INTEGRATION_` numerals.
- v6: current bounded `IMPLEMENTATION_INCREMENT / ` #1545 is now an intake source while review/provenance/integration/factory wrappers are excluded; one source, one bounded `FACTORY-CONTENT-DEMAND-1545` intake, no automatic generic CONT-08. Distinct intake #1563 already exists and is independently owned; not a reviewer or code publication.
- v7: removing unrelated globally blocked implementation veto is directionally valid, and owner-authored post-playable intake #1542 is detected as consuming #1539 in nominal tests. **However, two independently reproduced adversarial scenarios below violate hard acceptance gates and cannot be waived by green authored tests.**

## Unresolved findings and deterministic counterexamples

### BLOCKER FSR-1562-B01 — unvalidated faux terminal is accepted as integration authority

At exact reviewed `tools/planning/frontier_maintenance_v7.py`, `integration_main_sha_from_comments(issue_number, comments)` discards its own **`issue_number` argument** and accepts a comment solely if unedited, from an association-trusted author, and carrying the six independent regex/field lines:
```yaml
protocol: planning-v1
schema: 3
kind: INTEGRATION_STATUS
state: DONE
merge_method: squash
main_sha: 6d601848c4c29734f319e47611390303fd351ed3
```
It **does not validate** `issue`, mission, first valid owner/lease, generation, terminal `authority_mode`, source PR/head, verified clean required review, actual GitHub PR merged status, actual **single-parent squash**, or whether this SHA actually published the source files. A valid-looking unedited trusted comment, including an incomplete illustrative status, is incorrectly authoritative. The downstream `integrated_implementation_sources` checks only that this arbitrary SHA is an ancestor of current main. A six-line *schema-3-invalid* comment with current main SHA is consequently accepted and may seed implementation intake for an unintegrated closed issue.

**Reproducer:** copied the reviewed selector's guard and integration-status extraction logic into an isolated independent Python fixture, using the exact six-line trusted but unowned status above; `integration_main_sha_from_comments(9999, [comment]) == supplied_main_sha` evaluates **True**, although `issue: 9999`, `ownership_generation_comment_id`, any source PR and valid terminal are absent. This crosses the canonical schema-3 authority boundary and contradicts the requirement to require an **actual trusted squash INTEGRATION_STATUS(DONE)**. No live GitHub data was mutated in the reproduction. The reviewed authored test suite has no falsifying invalid-terminal fixture.

**Required correction:** fail closed unless the exact current source issue has a valid canonical schema-3 terminal owned by its first-winning/recovered unexpired integrator at that terminal, correct mission/branch/source identity, fresh binding, and a verified actual original producer PR squash publication to the exact one-parent main SHA or separately durable equivalent evidence; ensure the returned integration identity is tied to *that issue*, not merely six words in a comment. Add spoofed/partial/wrong-issue/stale-owner/wrong-PR/non-squash/incorrect or non-published main SHA negatives. No new readiness or integration bypass.

### MAJOR FSR-1562-M01 — issue-number sorting loses chronologically newest integrated source

`select_implementation_demand_source(..., integrated_source_numbers: set[int])` unconditionally uses `max(candidates, key=lambda issue: int(issue["number"]))`, then suppresses all demand if **that highest-numbered issue** was consumed. GitHub issue numbers indicate creation chronology, **not actual squash-integration chronology**. In actual frontier mechanics, a long-blocked older producer can integrate *after* a newer-numbered source. Minimal falsifying fixture: source issue #1539 published earlier is already consumed by #1542; issue #1343 finishes and squash-integrates *later* and has no intake. Although #1343 is now the actual latest integrated source, this selector picks #1539 and returns **None** because #1539 was consumed; source #1343 permanently loses its demanded next route. Conversely an older, unconsumed higher-numbered issue can be backfilled when a lower-numbered integration was actually the latest, violating no-stale-replay.

**Reproducer:** copied the reviewed exact `max(issue_number)` and consumed-source selection with integrated source IDs `{1343,1539}`, commit order #1539=earlier, #1343=later, consumed IDs `{1539}`. Returns `None` while actual latest #1343 needs intake. No live GitHub data was mutated. This violates the specifically stated **“newest squash-integrated source/no stale backfill”** guard under a supported dependency resolution order and defeats implementation lane liveness.

**Required correction:** preserve exact verified integration **main SHA** per candidate and order integrated candidates by **verified commit ancestry on current main**, not issue ID; choose the descendant-most qualifying actual squash publication (or fail closed if ancestry cannot be proved), then apply the one-per-source consumption check to that exact newest source. Add independent regression for older-numbered later integration, reversed chronology and consumed/unconsumed combinations. Preserve #1542/#1539 existing provenance dedupe and no redundant historical intake.

## Required disposition and successor

**Required adversarial review verdict: `CHANGES_NEEDED`.** Unresolved **BLOCKER 1**, **MAJOR 1**, correction-requiring MINOR 0; this is **not** `CLEAN_FOR_FACTORY_SEEDING_REPAIR_PUBLICATION`. The existing green 7-suite PR CI proves syntax/authored assertions only; it does **not** prove canonical terminal identity or integration-source recency. **DO NOT SQUASH-INTEGRATE #1560**, nor reviewer-only PR or treat source `REVIEW_READY` as safe authority. No license to modify source #1556 after its frozen terminal.

Route a precisely bounded **separately claimed remediation**, restricted to reviewed v7 authority/recency logic and necessary v7 self-tests/own handoff (v5/v6/PR CI unchanged unless independently justified). Require a fresh final-head exact PR run with successful offline compile and v1-v7 tests, **fresh distinct independent required rereview** of corrected head including the two attacks, then separate exact-current-main compatible squash-only noncanonical maintenance publication if clean. No canon/truth/consent/privacy/accessibility/readiness/production/release authority claimed by this review, its draft PR, or any test.