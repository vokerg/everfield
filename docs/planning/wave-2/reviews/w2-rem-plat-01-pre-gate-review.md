# W2-PG-REM-PLAT-01 — Independent pre-gate review of corrected platform evidence

**Review mission:** `W2-PG-REM-PLAT-01` / Issue #100  
**Reviewed remediation:** `W2-REM-PLAT-01` / Issue #92  
**Reviewed work/head:** `9d51099be4d53eff876104f482e3c163d34519e3`  
**Reviewed report blob:** `d6a20c2200cedad97ede36beb9871d420ca7a8ca`  
**Reviewed source-record blob:** `f2a9333436c9cbc4fe91ec71507997f46f2247e4`  
**Reviewed disposition blob:** `03341d3a54225571a1d4b8bfe46aa52b869e2369`  
**Reviewed handoff blob:** `7fa553bb0fde055bd158b768e4bc6fbcf17ee103`  
**Source producer:** Issue #79 work/head `695d3cd1bc5a017e780db8016ffefa2379d4103d`  
**Source pre-gate findings:** Issue #79 comment `5270240728`  
**Review base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Result:** `CLEAN_FOR_W2_REVIEW_INPUT`  
**Severity:** `0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR`

## 1. Scope and authority

This is a bounded independent pre-gate attack on the exact frozen Issue #92 remediation payload. The reviewed branch is immutable input to this episode. This review does not replace `W2-REV-01`, does not certify a release platform, does not select an engine, does not resolve partner-gated console requirements, and creates no implementation-readiness or canonicalization authority.

The review tests whether Issue #92 actually closes the three defects identified against W2-PLAT-01:

- `PG-PLAT-M01` — stale monthly Steam survey presented as current;
- `PG-PLAT-M02` — mutable external sources not reconstructably bound;
- `PG-PLAT-m01` — recommendation lacked an explicit reassessment rule.

## 2. Attack plan executed

1. Compare every external source category consumed by the corrected report against the immutable source-record packet.
2. Independently re-open current first-party sources for the load-bearing claims rather than accepting Issue #92 self-review assertions.
3. Attack the monthly-current predicate using the Steam Hardware & Software Survey visible during this review episode.
4. Attack source-version reconstruction for mutable/versionless documentation and verify the packet preserves exact normalized facts plus freshness/reopen behavior rather than pretending mutable URLs are immutable.
5. Attack `PLAT-PC-FIRST-R1` for hidden scalar ranking or stale-survey dependence.
6. Recheck authority boundaries for release, engine selection, certification, readiness, and canonicalization leakage.

## 3. Evidence-packet coverage attack

The corrected report declares fourteen external source categories and the immutable packet contains the same fourteen IDs:

- `PLAT-SRC-STEAM-OS`
- `PLAT-SRC-STEAM-DECK`
- `PLAT-SRC-STEAM-SURVEY`
- `PLAT-SRC-STEAM-LANG`
- `PLAT-SRC-WIN10`
- `PLAT-SRC-WIN11`
- `PLAT-SRC-XAG`
- `PLAT-SRC-XAG-INPUT`
- `PLAT-SRC-MSSTORE`
- `PLAT-SRC-APPLE-PORT`
- `PLAT-SRC-APPLE-NOTARY`
- `PLAT-SRC-APPLE-INPUT`
- `PLAT-SRC-NINTENDO`
- `PLAT-SRC-PLAYSTATION`

For each record, the packet binds a first-party authority, source title, authoritative URL, exact observation time, source version/month/last-updated state where exposed or an explicit versionless-live classification, mutable flag, normalized facts consumed by the project, verification status, freshness/reopen rule, and drift from Issue #79 where relevant.

No consumed external source category in the corrected report was found outside this packet. Mutable/versionless pages remain explicitly typed as mutable; the packet does not claim that its normalized snapshot makes the external source permanently current.

**Disposition:** `PG-PLAT-M02` remains closed.

## 4. Fresh current-source attack

Fresh first-party checks during this review episode produced the following results.

| Source ID | Independent check | Result |
|---|---|---|
| `PLAT-SRC-STEAM-SURVEY` | Valve still exposes **July 2026** as the current survey page; participation remains optional/anonymous; Windows is `93.67%`; Windows 11 64-bit is `70.26%`. | MATCH |
| `PLAT-SRC-STEAM-DECK` | Current compatibility criteria still require controller access to all content, active-input glyph correctness, controller-usable text entry, playable default performance at `30fps`/`800p` on Deck, no unsupported-device warning, launcher controller usability, and the Proton Windows-compatibility path. Current Deck display guidance still states 1280x800 preferred and a 9px absolute minimum text-height criterion at that resolution. | MATCH |
| `PLAT-SRC-STEAM-OS` | Current Steamworks platform documentation still describes Windows/macOS/Linux-SteamOS release workflow, OS-specific depots/builds, and target-OS testing. Historical OS-minimum language exists on the page but is correctly excluded from the 2026 baseline claim. | MATCH |
| `PLAT-SRC-STEAM-LANG` | Current Steamworks documentation still separates `Full Platform Support` from `Game Support Only`, with game-support declarations surfaced through the store workflow. | MATCH |
| `PLAT-SRC-WIN10` | Microsoft still records Windows 10 Home/Pro end of support on `2025-10-14`, with 22H2 final and LTSC separate. | MATCH |
| `PLAT-SRC-WIN11` | Microsoft still records Windows 11 Home/Pro as `In Support`; current release rows are version-specific, including newer rows than the original producer needed to enumerate. | MATCH |
| `PLAT-SRC-XAG` | Microsoft still exposes XAG `V3.2`, describes XAGs as best-practice guidance, and explicitly says they are not a compliance/legal checklist. | MATCH |
| `PLAT-SRC-XAG-INPUT` | XAG 107 still states the goal that players can operate the interface through input mechanisms of their choice and recommends configurable alternatives. | MATCH |
| `PLAT-SRC-MSSTORE` | Microsoft still documents the self-service Win32 PC path, optional Xbox services for PC-only publishing, and a separately managed console-program route; page still reports last update `2026-06-19`. | MATCH |
| `PLAT-SRC-APPLE-PORT` | Apple still presents Game Porting Toolkit 4 and Metal 4-era porting/evaluation tooling; tool presence does not establish acceptable project port cost/performance. | MATCH |
| `PLAT-SRC-APPLE-NOTARY` | Apple still documents notarization for Developer ID-signed macOS distribution and `notarytool`/Notary API automation paths. | MATCH |
| `PLAT-SRC-APPLE-INPUT` | Apple still documents physical and virtual controller support and common controller/mouse/keyboard device coverage in Game Controller. | MATCH |
| `PLAT-SRC-NINTENDO` | Nintendo's public process still places detailed platform information behind registration/terms, a separate Switch application, and later game review before publication. | MATCH |
| `PLAT-SRC-PLAYSTATION` | Sony's current public indie roadmap still begins with PlayStation Partner registration and places detailed tools/publishing documentation behind approved partner access. | MATCH |

The independent current-source pass found no newer Steam survey month than July 2026 and no material drift invalidating a normalized fact used by the corrected report.

**Disposition:** `PG-PLAT-M01` remains closed.

## 5. Monthly-current negative attack

The remediation rule is:

`CURRENT(month, observed_at) := month == newest_first_party_month_visible_at(observed_at)`

The live Valve survey visible during this review is July 2026. Therefore:

- `July 2026` under the current packet remains admissible as current monthly evidence;
- the old `June 2026` Issue #79 snapshot would fail the rule today exactly as intended;
- a future August-or-later page would reopen the July record rather than silently mutate the frozen Issue #92 evidence.

The current report also limits the survey to **directional Steam-user evidence**. The monthly percentage is not permitted to select a storefront, final shipping platform set, or release strategy by itself.

## 6. Reassessment-rule attack

`PLAT-PC-FIRST-R1` is not derived from a scalar platform score. The corrected rule provides a deterministic judgment order:

1. fail hard constraints first: evidence authority/freshness, no invented partner-gated rules, no false release promise, and sufficient downstream evidence coverage;
2. among admissible envelopes, compare reversibility/exit cost, evidence coverage per commitment, supported baseline, and unknown containment;
3. allow measured engine/accessibility/partner/cost evidence to constrain or reopen the result;
4. treat survey share, storefront reach, unmeasured porting-tool availability, and brochure support as directional only.

The corrected alternatives are consistent with this rule: Windows-only is rejected for insufficient evidence coverage; tri-platform and PC+console assumptions are deferred because they increase irreversible commitment before corresponding evidence exists; Windows plus Deck/Proton remains a reversible evidence envelope rather than a launch promise.

Negative attack result: replacing the July survey percentages with another normal month-to-month directional movement does not mechanically change the recommendation, while a change in supported baseline, measured engine cost, accessibility feasibility, partner/product requirement, or material source freshness does trigger explicit reassessment.

**Disposition:** `PG-PLAT-m01` remains closed.

## 7. Authority-boundary attack

No prohibited authority promotion was found. The corrected payload keeps these states explicit:

- Windows desktop: primary **evidence** target, not final minimum OS/hardware or release promise;
- Steam: reference distribution surface, not exclusivity or launch commitment;
- Deck/SteamOS via Proton: required compatibility evidence target, not a claimed Valve `Verified` result or native-Linux shipping commitment;
- macOS/native Linux: conditional port candidates;
- consoles: deferred and partner-gated;
- mobile: deferred product scope;
- engine choice: unresolved/evidence-required;
- implementation readiness: unresolved;
- formal authority: still requires `W2-REV-01` and later declared gates.

## 8. Residual risks retained, not defects in this remediation

- A mutable first-party page can drift after this review; the packet's freshness rules correctly require re-observation when the fact becomes load-bearing again.
- Partner-gated console requirements remain deliberately `UNKNOWN` until access and scope promotion exist.
- Steam survey participation is self-selected and therefore cannot establish total-market demand.
- Tool availability for macOS or storefront packaging does not establish measured port cost, engine abstraction quality, or production readiness.
- Accessibility applicability remains downstream work; XAG evidence here is not promoted to legal compliance authority.

These are preserved uncertainties/reopen conditions, not unresolved defects against Issue #92's bounded acceptance criteria.

## 9. Disposition

`CLEAN_FOR_W2_REVIEW_INPUT`.

Independent attack found:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

The original `PG-PLAT-M01`, `PG-PLAT-M02`, and `PG-PLAT-m01` defects are mechanically/source-evidenced as closed for this bounded remediation scope. Issue #92 remains immutable provenance; no further platform-remediation successor is justified by this review.

Formal aggregate `W2-REV-01` remains required before stronger authority. This review does not authorize integration, release, engine selection, partner certification, production implementation, implementation readiness, synthesis, or canonicalization.
