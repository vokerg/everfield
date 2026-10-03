# Handoff — Issue #1421 / IMPLEMENTATION-DEMAND-OLD-WORKS-WORLD-01-REM-01

## Scope
Blocking runtime-evidence remediation only. Frozen producer #1410 bytes remain read-only.

## Authority and activation
- source required review: #1416 terminal comment `5970438414`
- review disposition: `CHANGES_NEEDED`
- sole material finding: exact Godot 4.7.1 component runtime smoke PASS not proven
- frozen producer issue/terminal: #1410 / `5969178423`
- frozen producer head: `20284fa9171d1d6f91e3e930d627f587062485cb`
- component blob: `8e498156bb9a5413f53a84b14fc279c4be6c8f23`
- smoke blob: `a69e4c93960cf459544d42a160cc532d03401e5d`
- canonical binding: #1147 comment `5675066392`
- base main: `848acba1bba430170265b56d3f2de71b3268b7df`

## Verification infrastructure
The temporary workflow `.github/workflows/old-works-world-component-runtime-evidence.yml`:
- checks out the exact frozen producer head, not this remediation branch;
- verifies the exact producer/component/smoke Git identities;
- resolves the repository-reviewed Godot artifact lock and requires `4.7.1-stable`;
- verifies the downloaded artifact against the reviewed SHA-256;
- runs the exact component smoke under headless Godot;
- requires sentinel `EVERFIELD_OLD_WORKS_WORLD_PRESENTATION_SMOKE_PASS`;
- uploads immutable run identity and smoke log evidence.

## Integration boundary
This workflow is temporary verification infrastructure. It MUST NOT be integrated into `main` absent a later separate explicit authorization.

## Runtime status
PENDING GitHub Actions execution on the verification-only draft PR. No runtime PASS is claimed by this handoff until exact run/job/log evidence is inspected.

## Terminal routing
- PASS -> materialize a fresh required review of exact frozen producer #1410.
- runtime failure -> bounded producer-code remediation.
- identity/engine/evidence ambiguity -> bounded recovery / invalidation.

## Authority boundary
Runtime evidence only. No producer mutation, component publication, live-scene integration, final canon, truth resolution, production/release, empirical accessibility certification, or integration authority.
