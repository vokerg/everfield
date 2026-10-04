# Issue #1527 — Exact corrected public presentation composite verifier

## Authority, identity and isolation

**VERIFICATION ONLY; no runtime PASS is claimed from workflow creation or general CI.** This verifier is independently owned by `frontier-drain-composite-verifier-1527-gpt56sol-20261004-1254-c`, winning CLAIM `5979215172`. Canonical Planning Program v1 binding: Issue #1147 comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Claim base: `main@d7cf5ddf1afaa8e546f81f8aeee940e72b96a98c`.

Required correction source: Independent Review #1515 `REVIEW_STATUS(CHANGES_NEEDED)` comment `5979151959`, report PR #1524 head `e14f514f628c2a230337abc8749531e4f1edc9e6` (one MAJOR malformed speaker/phase, one correction-requiring MINOR empty station ID). Remediation #1525 `STATUS(REVIEW_READY)` comment `5979194789`, draft PR #1526 immutable head `31869366ba234db92e0b6fda48eb7fc24ea3004a`. Earlier verifier #1514 exact original head PASS `5978373146` is **not** evidence for remediated bytes.

## Exact executable source composition

The correction PR contains only 3 overlay scripts and 1 handoff because the original producer is unpublished. The workflow explicitly checks out original Producer #1506 draft PR #1513 head `37833b1e482adaa2f123edeed02b81e24a2f3688` (terminal `5978324440`), verifies original SHA identities, fetches only frozen Remediation #1525 full commit `31869366ba234db92e0b6fda48eb7fc24ea3004a`, proves the correction handoff blob and overlays **exactly** the three changed scripts. A git-diff exact-path check rejects additional changed original paths.

| Source path | Original frozen blob | Exact tested overlay |
|---|---|---|
| `game/components/playable_presentation/playable_presentation.gd` | `340f955c6977d43cbe735216c1758764dd25f202` | `ba819915fc55e444d54d46671892cea35cb6b3cf` |
| `game/components/playable_presentation/hearing_reader.gd` | `2c06223e5d25761523ca038e160e0bce3630f0ad` | `b7ce32ea0d3b841fce49f946d6efce0ccbcaf139` |
| `game/components/playable_presentation/playable_presentation_smoke.gd` | `c4f224d93c6260e6f42b93f61d7f998544893e0c` | `ef2628c4d691e753316fe81d218e1534e6e37a5f` |

Frozen read-only original helper `world_reader.gd` is `018d3c5908eca22593c7b8a6eef4a29ed1a23f0f`, `consequence_reader.gd` is `3cb9cb6887508f94fba865ebc428ba43fbdd38b2`, Producer #1506 handoff is `561be48210a2637acf37a137b6951cfbefb97aac`, correction #1525 handoff is `2094304dae533e5e2d2fb94623fdbe5024cd95f8`.

Unchanged published providers: Old Works `8e498156bb9a5413f53a84b14fc279c4be6c8f23`, Commons Hearing `9682c47ee2c84ea42417651d0ca2e4f30ebf78b2`, commitment consequences `419688e17515bf5f67b383182c0b6330111ce4be`, live `game/main.gd` `9b406cc0a0115f0818df633eda67d69ab7779a06`, `game/project.godot` `9da4153ed378945ef5e9634e0e5cae48289845d8`, Godot engine lock `4a88990ae24768eb4f83a8a1311e2a830834649f`.

## Exclusive verifier paths, checks and pending evidence

- `.github/workflows/verify-playable-presentation-remediation-1527.yml` — intended immutable Git blob `9663cb81e5db1f1eea58cd1fbf71ef47309465ca`.
- `docs/planning/handoffs/issue-1527.md` — this reconstructable provenance handoff.

The PR workflow must run from the **final verifier PR head**, check both frozen source SHA sets and the exact 3-script overlay, resolve reviewed Godot `4.7.1-stable` Linux x86_64 ZIP SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`, inspect exact binary banner `4.7.1.stable.official.a13da4feb`, then execute:

```sh
godot --headless --path game --script res://components/playable_presentation/playable_presentation_smoke.gd
```

**PASS must be observed**, never inferred: exit 0; `EVERFIELD_PLAYABLE_PRESENTATION_SMOKE_PASS` literal; no failed assertions or GDScript errors; original public source parity plus six malformed injected hearing negative tests, empty station rejection, no private provenance, explicit nonconsent and unresolved truth; new final-head workflow run/job conclusions; uploaded artifact with exact ID, digest and logs. Preserve failures and route corrections if any identity, engine download, parser, test or log condition fails. The prior 29-PASS original-head run #37191047245 does not apply.

The existing **independent required fresh Review #1528** remains blocked until this verifier publishes an exact final-head schema-3 `VERIFICATION_STATUS(DONE)` PASS and separate activation. The source/remediator/review branches are frozen and read-only. Temporary verifier workflow is **not integrable**, and this issue grants no clean review, component publication, canonicality, gameplay mutation, consent/truth resolution, persistence, accessibility readiness, production or release authority. Any eventual integration into main is separately gated and squash-only.
