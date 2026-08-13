# Issue #92 handoff — W2-REM-PLAT-01

**Mission:** `W2-REM-PLAT-01`  
**Issue:** #92  
**Branch:** `planning/issue-92`  
**Ownership generation:** Issue #92 comment `5270264203`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Source W2-PLAT-01 head/work:** `695d3cd1bc5a017e780db8016ffefa2379d4103d`  
**Source report blob:** `f47ad96baea765580ad9d016d527c932ce3b2768`  
**Source handoff blob:** `479a0b6dfeeec838b60593819ff355c2fb66ec2e`  
**Pre-gate review:** Issue #79 comment `5270240728`  
**Corrected report blob:** `d6a20c2200cedad97ede36beb9871d420ca7a8ca`  
**Immutable source-record blob:** `f2a9333436c9cbc4fe91ec71507997f46f2247e4`  
**Finding-dispositions blob:** `03341d3a54225571a1d4b8bfe46aa52b869e2369`  
**Intended terminal state:** `REVIEW_READY`  
**Required formal review:** `W2-REV-01`

## Completed work

Created a bounded remediation of the frozen W2-PLAT-01 producer evidence without editing the source branch.

The remediation:

- refreshed the Steam Hardware & Software Survey from the stale June 2026 producer snapshot to the newest first-party month visible at the remediation observation session, July 2026;
- corrected consumed values to Windows `93.67%` and Windows 11 64-bit `70.26%`;
- added an explicit fail-closed monthly-current rule so an older snapshot cannot be labeled current when a newer first-party month is already available;
- created an immutable normalized project citation packet for every external fact consumed by the corrected report;
- bound the corrected report to exact citation-record blob `f2a9333436c9cbc4fe91ec71507997f46f2247e4`;
- reverified the retained load-bearing external claims against current first-party sources and recorded source drift rather than silently carrying prior values;
- added an explicit decision/reassessment rule separating hard constraints, primary decisive dimensions, constraining evidence, and directional evidence;
- named explicit conditions that would flip/reopen `PLAT-PC-FIRST-R1`;
- re-evaluated the recommendation under corrected July survey evidence and retained it as `UNCHANGED_RECOMMENDATION_WITH_CORRECTED_EVIDENCE_PROVENANCE`;
- preserved the producer's reversible Windows + Deck research envelope, conditional macOS/native-Linux/storefront states, partner-gated console unknowns, downstream accessibility/engine/packaging/input/localization interfaces, and non-release/non-readiness authority limits.

## Immutable external-fact packet

`docs/planning/wave-2/research/target-platform-source-records.yaml` is the project-side frozen record of external facts consumed by the corrected report.

Each record binds:

- source ID and first-party authority;
- authoritative URL and title;
- observation time;
- explicit version/month/last-updated information where available;
- mutable/versionless status;
- normalized facts actually consumed;
- verification status;
- freshness/reopen rule;
- drift from Issue #79 where applicable.

The packet intentionally does not vendor complete third-party pages. External authority is refreshed when its trigger fires; the project blob preserves what the frozen candidate actually consumed.

## Material source drift

One material source freshness correction was required:

- producer: June 2026 Steam survey, Windows `94.10%`, Windows 11 64-bit `70.44%`;
- corrected: July 2026 Steam survey, Windows `93.67%`, Windows 11 64-bit `70.26%`.

The recommendation remains unchanged because survey percentages are explicitly directional rather than decisive. They cannot override current support status, evidence coverage per irreversible commitment, partner-gated uncertainty, accessibility findings, or measured platform/engine cost.

## Review finding dispositions

- `PG-PLAT-M01` MAJOR — RESOLVED: newest available July monthly source, exact corrected values, explicit drift, fail-closed monthly-current rule, recommendation re-evaluation.
- `PG-PLAT-M02` MAJOR — RESOLVED: immutable normalized project citation packet bound by exact blob from corrected report.
- `PG-PLAT-m01` MINOR — RESOLVED: ordered reassessment rule plus explicit flip/reopen conditions.

No finding was waived or downgraded by assertion.

## Self-review

Final remediation self-review against Issue #92 acceptance criteria:

- BLOCKER: 0;
- MAJOR: 0;
- correction-requiring MINOR: 0;
- exact source #79 provenance retained: PASS;
- newest available monthly survey used and labeled with exact month: PASS;
- stale monthly data cannot satisfy a current-source acceptance claim under declared rule: PASS;
- every external fact consumed by corrected report mapped to immutable project citation record: PASS;
- source facts separated from project inference: PASS;
- recommendation explicitly re-evaluated against refreshed evidence: PASS;
- decisive/constraining/directional evidence roles explicit: PASS;
- flip/reopen conditions explicit: PASS;
- partner-gated unknowns preserved: PASS;
- engine/accessibility/packaging/input/localization interfaces preserved: PASS;
- release promise / engine selection / readiness / canonicalization authority leakage: none identified;
- required formal critique remains `W2-REV-01`: PASS.

## Remaining risks / unresolved questions

- Steam survey is a Steam-user sample and remains directional rather than product-demand evidence;
- future monthly/live sources require re-observation when their freshness trigger fires;
- partner-gated console requirements remain unknown until official access;
- comparative engine and accessibility evidence can still reopen this platform sequence;
- macOS/native-Linux/storefront costs are not settled by documentation availability;
- formal aggregate adversarial review has not run.

## Next action

Cold-review exact branch diff and current `main`; verify ownership remains uncontested; publish owner schema-3 `STATUS(REVIEW_READY)` for the exact final Issue #92 branch head and the four artifact blobs. Then freeze `planning/issue-92`.

Record durable linkage on Issue #79 that Issue #92 supersedes the frozen producer payload as the substantive platform-scope evidence input for later `W2-REV-01`, while retaining Issue #79 as immutable historical provenance.

Do **not** treat this remediation, its self-review, a PR, or any future noncanonical main integration as the formal independent `W2-REV-01` disposition. No production implementation is authorized.
