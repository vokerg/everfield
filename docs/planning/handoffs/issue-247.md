# Handoff — Issue #247 / W2-REM-ACC-04

## Identity

- Mission: `W2-REM-ACC-04`
- Issue: #247
- Branch: `planning/issue-247`
- Winning claim comment: `5290072269`
- Actor session: `w2-rem-acc-04-gpt56sol-20260814-0805-frontier`
- Claim base main: `df2dffdb14fc20def14aaaee4d61e0638e500f91`

The later competing claim comment `5290073452` bound the same source/head but lost schema-3 contention because the lowest valid GitHub comment ID wins. It has no ownership authority for this generation.

## Immutable inputs

- Issue #240 terminal comment: `5290011410`
- Issue #240 head: `bccd22e35f84a5894586d9494e1963ebdef7dc02`
- Issue #240 work: `f4671c3c295437a64d82ffc51e228c826fcce40e`
- Issue #240 v3 policy blob: `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4`
- Issue #243 terminal negative review comment: `5290059882`
- Issue #243 review head/work: `e7fab153735b90cae4a175fb42b0546dba728f7b` / `f2a87552756d6f9897e6349fa5b7e4cc5f677fda`
- Issue #243 integration status: `5290064752`
- Issue #243 disposition: `CHANGES_NEEDED`
- Issue #243 integration provenance main SHA: `df2dffdb14fc20def14aaaee4d61e0638e500f91`

## Bounded corrections completed

All four Issue #243 finding IDs are dispositioned in this packet:

- `W2-REV-ACC03-M01` — pause applicability is non-circular; subtitle pre-start/default applicability is not narrowed by early content; XAG 106 context change no longer contains `where_possible`.
- `W2-REV-ACC03-M02` — XAG 106 core narration includes platform screen reader, speech synthesis, and recorded audio, with recorded audio typed allowed-but-nonideal.
- `W2-REV-ACC03-m01` — the XAG 102 post-launch reconfiguration example is removed from required source semantics.
- `W2-REV-ACC03-m02` — the exact `greater than 1-2 minutes` source phrase is preserved as an ambiguous non-executable range; the deterministic >60-second rule is separately typed as a conservative project fail-closed evaluation rule, never as source normative text.

The v4 policy is an overlay over the exact rejected v3 blob rather than a rewrite. It patches exactly six atomic records. Stable clause identity/count remains 77 new XAG 102–106 records and 105 composed records.

## Fresh source evidence

Current first-party Microsoft XAG 102, 104, 105, and 106 pages were re-read on `2026-08-14`; all report last updated `2026-03-04`. Load-bearing implementation text supports the corrections recorded in the report/policy. Recheck source freshness again during mandatory independent review.

## Narrower review provenance and retired duplicate route

While this issue was in progress, Issue #242 / `W2-PG-REM-ACC-03` terminal negative review was squash-integrated on `main@d7d4273fbcbc32b1c8fcc02f175d4a7c976452f6`. Its terminal comment is `5290068415`; it recorded an additional `XAG106-PROPER-NAME-PRONUNCIATION` applicability concern and initially routed Issue #245.

Issue #245 was subsequently externally terminalized `SUPERSEDED` by schema-3 status comment `5290106078` in favor of the already-live Issue #247 route. This does not expand Issue #247's explicit objective beyond the four authoritative Issue #243 findings, and this packet does **not** claim the narrower Issue #242 pronunciation concern resolved. There is no live #245 producer branch to preserve. The mandatory fresh review must explicitly re-attack the pronunciation applicability and reopen bounded remediation if independently reproduced.

## Preserved fail-closed state

- XAG 108–123: `GUIDELINE_SUMMARY_ONLY`
- empirical accessibility evidence: `NOT_RUN`
- `mapping_complete`: `false`
- `IR-BLOCKER-ACCESSIBILITY-CURRENT`: `OPEN`
- `W2-REV-M02`: remains `OPEN_BOUNDED`
- Issue #242 findings resolved by this task: `false`
- Issue #245: `SUPERSEDED`, no producer work
- implementation/readiness/release authority: none
- legal/compliance or Valve certification authority: none
- decision/canonical authority: none
- integration authority: none

## Validation / adversarial contract

`ACCESSIBILITY-POLICY-VALIDATOR-v4` requires exact v3 reconstruction before the six-record overlay and rejects:

- circular `pausable` trigger semantics;
- invented early-content preconditions;
- `where_possible` weakening;
- dropped recorded-audio alternative;
- example-to-requirement leakage;
- ambiguous source range treated as executable threshold;
- project threshold mislabeled source-normative;
- XAG 108–123 promotion, empirical PASS laundering, or `mapping_complete: true`.

It also requires the fresh review to re-attack the narrower Issue #242 pronunciation concern rather than treating Issue #245 supersession as a substantive defect disposition.

## Required next action

An exact-head **draft** PR from `planning/issue-247` to `main` is mandatory and must match terminal `head_sha`.

Then require a **fresh independent/degraded-independent scoped review** of this exact remediation head. The reviewer must reconstruct exact v3 blob `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4` plus the terminal v4 overlay blob, re-read current Microsoft source, attack all seven Issue #243 semantic fixtures, and independently re-attack `XAG106-PROPER-NAME-PRONUNCIATION` as a narrower-review risk. Reopen bounded remediation if that defect reproduces.

A clean review of Issue #247 does not by itself authorize integration and does not close aggregate accessibility readiness. Any eventual `main` integration remains separately authorized and squash-only.
