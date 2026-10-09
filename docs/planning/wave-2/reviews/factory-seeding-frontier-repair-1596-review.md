# Required adversarial review — Issue #1598 of factory remediation #1596

**Mission:** `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-05-REV-01`  
**Reviewer generation:** #1598 CLAIM `6085816104`, actor `frontier-required-review-1598-gpt6-20261009-2121-01`. Independent of producer #1596 actor `frontier-remediate-1596-gpt6-20261009-1140-01`.  
**Disposition:** **CHANGES_NEEDED — 1 BLOCKER, 1 MAJOR, 0 correction-requiring MINOR**. Review-only. **NO SOURCE MERGE**.

## Frozen subject and authority

- Current `main` during review: `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`; active binding #1147 comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Producer #1596 unedited, timely first-winner CLAIM `6076667400` (GitHub `2026-10-09T07:41:47Z`), HEAD_ADVANCE `6076744447` (`07:47:11Z`), and `STATUS(REVIEW_READY)` `6076787868` (`07:50:31Z`), well within the canonical six-hour lease. Distinct required review is expressly routed. Full merge-ref addendum `6076796827` supplies `b5633023c4f7958a98b27a99393b078b01854954`; the seven-character auxiliary display prefix in the unedited producer terminal is **not** treated as a full SHA or as independent authority.
- Producer draft PR #1597 stays open/unmerged, exact HEAD `c46c32aa03eb261c5438a5f96b335aee8cc793cb`, base current main; ten permitted changed paths. Eight inherited paths retain the pinned blobs enumerated in #1598; corrected v7 blob `97161ea4c2c9ce1173eea987f3f6568f914295ee`; new producer handoff blob `b74e545b7f99b24ab8d0be391124f787666d8ff5`. Frozen predecessor PR #1593 HEAD `fa0c552bab1577f088dba271aeebe64f5150b1e0` and required negative review #1595 HEAD `6cc2a06914548e71fdaf3c4bf7af9d3d855c24be` remain unmerged and unchanged.
- Actual final-head PR run `37901191543`, head `c46c32aa...`, `pull_request` on `main@3d7ce70...`: `validate-pr` job `113723900726` SUCCESS; `maintain` job `113723902083` SKIPPED. Retrieved decoded logs explicitly show checkout `b5633023...`, `Merge c46c32aa... into 3d7ce70...`, Python compilation and v1–v7 self-tests PASS, including authored alias and losing-contender fixtures. This is **producer-authored regression evidence**, not independent acceptance.

## FSR-1598-B01 — completed ownership generation can be resurrected (BLOCKER)

**Evidence:** `tools/planning/frontier_maintenance_v7.py` lines 346–434, particularly 403–424, and integration consumer lines 830–948 and 1004–1025.

`_valid_owner_terminal()` starts with the first valid CLAIM and walks earlier records. The only earlier terminal that ends the evaluation is `STATUS(HANDOFF_READY)`. A valid `STATUS(DONE)`, `STATUS(SUPERSEDED)`, `STATUS(INVALIDATED)`, `REVIEW_STATUS(CHANGES_NEEDED)`, `VERIFICATION_STATUS(DONE)`, or `INTEGRATION_STATUS(DONE)` ending the same generation is ignored by the loop. As a result, a subsequent record that reuses that ended `ownership_generation_comment_id` and actor can pass the owner, head, and lease checks provided the time is still inside six hours. The canonical program explicitly says a valid terminal ends the generation; later terminal attempts from that ended generation have zero authority effect.

**Minimal causal counterexample (not a claim of having run a full remote replay):** trusted schema-3 CLAIM at 12:00; valid same-owner `STATUS(DONE, terminal=true)` at 12:05; otherwise complete same-owner `INTEGRATION_STATUS(DONE)` at 12:10 binding the same CLAIM. The v7 loop does not consume the 12:05 terminal and therefore permits the later 12:10 integration terminal if its other causal source/review/squash evidence passes. The terminal-prefix owner gate cannot legitimately grant this authority; this is a provenance-authentication defect, not a mere liveness preference. The current authored losing-contender fixtures do not cover a *valid earlier terminal*.

**Required correction:** reconstruct all canonically valid terminal/HANDOFF transitions in prefix order; end a generation on any applicable valid terminal; reject attempts to reuse it without a separately valid successor generation. Preserve the precise winner/loser and temporal rules for first CLAIM, HANDOFF RESUME, matured STALE and ORPHAN recovery; do not revoke legitimate earlier terminal records retroactively. Add positive and negative source/reviewer/verifier/integrator consumer scenarios, including a legitimate later generation vs a reused ended generation.

## FSR-1598-M01 — valid direct YAML aliases rejected by lexical shortcut (MAJOR)

**Evidence:** `tools/planning/frontier_maintenance_v7.py` lines 181–247. A standalone isolated Python regex probe of the exact scanner patterns confirmed:

| Syntactically valid YAML direct child | Token recognized | Direct-child match | Consumer result |
| --- | --- | --- | --- |
| `  source_producer_issue: 1545` | yes | yes | accepted |
| `  source_producer_issue: 1545 # original source` | yes | **no** | **rejected** |
| `  "source_producer_issue": 1545` | yes | **no** | **rejected** |
| `  source_producer_issue: '1545' # reviewed` | yes | **no** | **rejected** |

The `re.fullmatch(r"  KEY:[ \\t]*([^\\n#]*?)[ \\t]*", line)` test disallows comments and quotes on a mapping key, even when the YAML *semantic* key is a unique non-null scalar, a sole direct child of the sole top-level `extensions:`. The header equality test `line == "extensions:"` also rejects a legitimate `extensions: # provenance` header. Legitimate reviewed aliases are consequently invisible, blocking latest-source recognition and liveness. This is a **false negative**, not a demonstrated forged-authority bypass. The authored nested/flow negative tests still pass; those do not establish acceptance of all compliant scalar YAML.

**Required correction:** use a bounded real YAML mapping-key/value structural check or an equivalent parser that handles comments, quoted direct keys, flow/sequence nesting, duplicate and synonym conflicts without accepting wrong-placement keys. Add genuine valid direct-comment/quoted-key fixtures alongside hostile nested/flow, duplicate, null, implicit scalar and foreign-section probes. Preserve legitimate #1583 alias handling.

## Other review results and authority boundary

- Prior #1594 findings FSR-1594-M01 and M02 are addressed in visible code for ordinary nested/flow keys and losing duplicate CLAIM/RESUME/RECOVER; a first-winner baseline and matured STALE path are present. Neither authored fixtures nor green CI close the newly identified terminal-reuse blocker or comment/quoted-key false negative.
- Independently checked real immutable terminal chronology: producer #1545 `6008457546` (`2026-10-06T03:02:14Z`); distinct verifier #1575 `6008823087` (`03:37:24Z`); distinct required reviewer #1577 `6009157969` (`04:10:25Z`); integrator #1583 `6009230681` (`04:17:26Z`), one-parent squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de`. The source/verification/review aliases visible in these records align with the v7 consumers. No independent new executable full-chain replay was performed; the negative decision rests on independently inspected control flow and isolated exact-regex probes.
- Scope remains the frozen ten-path packet. No regression is asserted against v5 multi-target successor or v6 bounded demand; their exact inherited blobs are unchanged and the composed authored suite passes. The current workflow has read-only `pull_request` validation and suppresses mutating maintenance for PR events.
- **Blocking route:** a fresh bounded remediation issue must correct B01 and M01 on its own branch from then-current main, preserve inherited immutable blobs, run exact-final-head read-only validation, and undergo a *new distinct required independent adversarial review*. Producer #1597 and this review-only PR are NOT authorized for squash integration. Nothing grants canonicality, gameplay, truth, consent, accessibility, implementation readiness, production or release authority.
