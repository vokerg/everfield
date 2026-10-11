# Issue #1655 — independent executable verification of frozen public-text navigation #1626

## Role, eligibility and current work state

Mandatory distinct scoped Godot 4.7.1 runtime verifier, mission `IMPLEMENTATION-VERIFY-PUBLIC-TEXT-NAVIGATION-1626-02`. Independent from broader producer/resume #1626 authoring execution (`frontier-resume-public-text-navigation-1626-gpt6-20261011-1206-01`) and prior #1642 empirical measurement. Fresh first-valid unedited schema-3 CLAIM **#6109052214**, verifier actor `frontier-distinct-public-text-verifier-1655-gpt6-20261011-1432-cph-01`. Post-CLAIM rechecked GitHub server times, sole valid owner, canonical program/binding and exact source PR. Branch `planning/issue-1655` created from exact then-current `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.

**State: FIRST HOSTED EXACT-HEAD EXECUTABLE PASS OBSERVED — MUST RERUN ON FINAL PR HEAD AFTER THIS HANDOFF EVIDENCE COMMIT.** Original verifier PR #1658 HEAD `9b85663d31bca36b95e069d0122be042f49cc05e` actual `pull_request` Actions run #38139803091 (attempt 1) SUCCESS, job #114471139306 SUCCESS. New source exact Godot 4.7.1 isolated component suite emitted one `EVERFIELD_PUBLIC_TEXT_NAV_PASS checks=426`, no test/parse/script FAIL, both existing first-playable and movement/interaction regressions PASS. Source checkout and all four immutable Git blobs, reviewed `game/project.godot`, Godot official ZIP SHA256 and exact binary version checks passed. GitHub artifact #11702750456, `public-text-navigation-1626-38139803091-1`, size 12,159 bytes, uploaded archive SHA256 `46e0d7e5652ad3ce64a2998cd178708670fa5b1e517c005fdde29686ee643c18`, containing raw logs and identity/SHA manifest. **This edit advances the verifier PR HEAD, so a new hosted run and artifact verification on the final immutable PR HEAD is mandatory before publishing PASS; first-run success is not transferable.**

## Frozen corrected producer source and authority

- Source Issue #1626 original owner CLAIM #6107400582, prior corrected viewport probe HANDOFF #6107651917, valid separate producer HANDOFF RESUME_INTENT #6107889528 / RESUME #6107894292 and **latest HANDOFF_READY #6107964587**. Exact OPEN/DRAFT source PR **#1641 HEAD `d4d6ce1f55670fa6c7986a05cf82a2face4d398d`** is not source verified by earlier #1642.
- Only source PR changed paths and immutable GitHub Git blob identities:
  1. `game/components/public_text_navigation/public_text_navigation.gd` `b081bfe234c18884650992d7251b55effbec8c2f`;
  2. `game/tests/public_text_navigation/public_text_navigation_smoke.gd` `ff355251c9b2f303c5c9ba1633a6a0b18b6689a3`;
  3. `game/tests/public_text_navigation/public_text_fit_smoke.gd` `a64c88036f95f4b9e7a84219fb3bd5ebd8b6bd9a`;
  4. `docs/planning/handoffs/issue-1626.md` `c5a2fc1e8270bfdec2d7d903a804a4bbe3184883`.
- Previous independent measurement verification #1642 terminal #6107838152, old #1645 verifier only, 13 scenarios with 7 nominally over 134px at 960x540; it does **not** prove new pagination/real scene fit or accessibility. Current source isolated navigation smoke is new and not covered by common first-playable CI.
- Canonical planning program Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Exclusive immutable verifier branch/PR scope

Only two own branch paths may change:
- `.github/workflows/verify-public-text-navigation-1626.yml` initial Git blob **`28f8bbc4886dfcac5343b973221ec627df97b6f3`**, new pinned read-only workflow, not an inherited old-verifier mutation;
- `docs/planning/handoffs/issue-1655.md`, this durable handoff.

Workflow triggers only on relevant verifier-only PR file changes targeting main, GitHub Actions read-only permissions, runner Ubuntu 24.04, SHA-pinned checkout & artifact upload. Crucially source checkout is immutable **`d4d6ce1f55670fa6c7986a05cf82a2face4d398d`**, never verifier PR code or default main. Assert all four exact source blob IDs and reviewed project `game/project.godot` Git blob `9da4153ed378945ef5e9634e0e5cae48289845d8`, archive source/published provider Git tree, Git/source SHA manifest, verifier PR HEAD and run identity.

Reviewed immutable official Godot artifact lock `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json` blob `4a88990ae24768eb4f83a8a1311e2a830834649f`, ZIP URL `https://github.com/godotengine/godot/releases/download/4.7.1-stable/Godot_v4.7.1-stable_linux.x86_64.zip`, sha256 **`c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`**, binary full version **`4.7.1.stable.official.a13da4feb`**. Download, enforce SHA check before executing. On exact source, call `godot --headless --path game --script res://tests/public_text_navigation/public_text_navigation_smoke.gd`, require exit 0, **exactly one** full-line `EVERFIELD_PUBLIC_TEXT_NAV_PASS checks=N` with N positive, zero source `SCRIPT ERROR`, `Parse Error`, `Assertion failed`, `[EVERFIELD][PUBLIC-TEXT-NAV][FAIL]`. New source smoke covers 13 reviewed provider cases, exact text/line breaks and SHA preservation, next/back bounds, no private text leakage, fail-closed malformed inputs, read-only session state and provider contract. Execute existing first-playable and movement/interaction regressions with same locked engine and negative marker rejection. Archive raw stdout/stderr, immutable runner/source/verifier identities, SHA256 manifests and all CI artifacts; log failures must be preserved.

## Required next steps and terminal gates

1. Verifier-only DRAFT PR #1658 exists, and exact changed-file GitHub API confirms only owned workflow/handoff paths; original source PR #1641 remains OPEN/DRAFT/unchanged. First run #38139803091 is genuine runtime PASS but is not the final verifier HEAD after this handoff commit.
2. Inspect genuine **new final verifier PR HEAD** `pull_request` Actions run/job, locked exact source checkout, all four source blobs and project/provider hash, Godot ZIP/version, isolated `checks=426` sentinel and both regressions, actual artifact ZIP archive and independent SHA256 manifest. Do not mutate this branch after the final verifier run.
3. If confirmed, publish in-lease `VERIFICATION_STATUS(DONE,result=PASS)` with exact final immutable PR/source hashes, true runner/job/artifact IDs and digest, scoped PASS and route back to a **different source owner execution** for #1626 HANDOFF/REVIEW_READY and then **fresh genuinely independent adversarial source review**. If new runner FAIL, publish real negative evidence and source handoff; no fake PASS.
4. **Never** merge this verifier-only PR, older verifier/reviewer drafts or source PR from verifier role. Do not touch sibling route-history, shared scene #1629, live providers, game or canon. This is component runtime verification, not scene/viewport accessibility, historical truth, engine selection, readiness, production, release or any canonical decision. Later integration still separately owner-authorized squash-only NONCANONICAL.
