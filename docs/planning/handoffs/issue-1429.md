# Handoff — Issue #1429 / IMPLEMENTATION-DEMAND-COMMONS-HEARING-01-REM-01

## Scope
Blocking runtime-evidence remediation only. The frozen #1411 producer component and smoke bytes remain read-only.

## Authority and activation
- ownership: Issue #1429 comment `5970816775`
- actor: `frontier-drain-commons-runtime-1429-gpt56sol-20261003-01`
- claim base main: `dcabab2a2f903a42ae55d6965511cf9207b0f0c6`
- source review: #1418 terminal comment `5970796361`
- source review disposition: `CHANGES_NEEDED`
- canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`

## Frozen producer
- producer issue: #1411
- producer terminal: comment `5970379802`
- producer PR: #1417
- exact producer head: `a610b00ed03282cc079cca4d4f9430ddd54e9bf0`
- component blob: `9682c47ee2c84ea42417651d0ca2e4f30ebf78b2`
- smoke blob: `0ebbccebf03e12386ba8fd31f593aade200b4323`

## Verification-only paths
- `.github/workflows/verify-commons-hearing-1429.yml`
- `docs/planning/handoffs/issue-1429.md`

The workflow is temporary evidence infrastructure and has **no authority to be integrated into `main`**.

## Verification contract
The workflow must:
1. check out the exact frozen producer head;
2. verify the exact component and smoke Git blob identities;
3. resolve and verify the repository-reviewed Godot `4.7.1-stable` artifact;
4. import the exact project under the locked engine;
5. execute `res://components/commons_hearing/commons_hearing_presentation_smoke.gd`;
6. require process success and exact sentinel `EVERFIELD_COMMONS_HEARING_PRESENTATION_SMOKE_PASS`;
7. upload immutable run identity and smoke logs.

## Evidence state
`PENDING_GITHUB_ACTIONS_EXECUTION`

## Authority boundary
Runtime evidence only. No producer mutation, component publication, live-scene integration, final character/social canon, relationship mutation, production/release, empirical accessibility certification, or integration authority.
