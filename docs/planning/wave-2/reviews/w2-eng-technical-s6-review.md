# W2-ENG-TECH-S6-REV-01 — required review of bounded identity-bound capture evidence

## Review identity

- Review issue: #458 / `W2-ENG-TECH-S6-REV-01`
- Trust mode: `DEGRADED_SINGLE_AGENT`
- Judged producer: Issue #456 / PR #457
- Judged producer head: `0719199237d3ac46505f52a06df0a0fc93429c9f`
- Judged final trigger: `b744552663d8dbaf4b8fa27b250ff6507dffe7d8`
- Judged run: `31967674130` attempt 1, success
- Judged artifact: `9268994399`, `w2-eng-tech-s6-01-31967674130-1`
- Artifact digest independently recomputed: `sha256:da5db6666e1297ec210bcb9d0db6849925421209dee3497346c08de577650fa5`
- `evidence.json` SHA-256 independently recomputed: `f14b961ce316e0796b3f17753e15d91fc943f79b721db17e5adb58f324521887`
- `independent-verification.json` SHA-256 independently recomputed: `63db2aa4d01586accb9d8f4497fd289727c97e4e82a0491466ab290bb821067d`
- Reviewed validator: `W2-ENG-PROTOCOL-VALIDATOR-v5` / validator file SHA-256 retained by run `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`
- Provisional producer generation under judgment: Godot `GEN-S6-8665917a0eb4a88a0e0f2f16`

## Disposition

`CHANGES_NEEDED`

Findings: **0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR**.

The producer packet is internally consistent in several important ways, but it does not yet satisfy the exact S6 capture-authenticity/reuse and required failure-injection obligations strongly enough to promote the Godot generation to trusted bounded comparison evidence.

No S6 generation is trusted by this review. Bevy and Defold remain `INCONCLUSIVE_HARNESS_OR_INFRA`; Unity and Unreal remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`.

## Independent checks that passed

The review downloaded the immutable final Actions artifact rather than relying on branch prose. The ZIP contains exactly the retained machine packet (`evidence.json`, its digest, validator self-test output, independent-verification JSON/log/digest, run identity, summary and Xvfb log). The artifact digest and both principal machine-file hashes match the terminal producer identities.

For Godot, independent recomputation confirmed:

- raw-attempt digests match canonical JSON of the retained raw records;
- capture-binding digests match their retained binding bodies;
- formal registry refs map one-to-one to raw/source digests;
- N1/N2/FI1 have three distinct reset IDs and three distinct workspace IDs, each with retained pre-absence and exclusive-creation facts;
- candidate identity is bound to exact Godot 4.7.1-stable archive/executable identity, exact run identity, exact runner/validator digests and reviewed S5 provenance;
- deterministic work/generation derivation recomputes exactly `WORK-S6-c51872e5cd4afb8893878dfd` / `GEN-S6-8665917a0eb4a88a0e0f2f16`;
- the retained S6 adaptation uses exact fixed refs, bounds, injection and common cold/reconstruct resource and is accepted by unchanged v5 semantics;
- formal N1/N2/FI1 identity/result/reset shapes satisfy the unchanged-v5 envelope and its retained aggregate is exactly `PASS_FOR_COMPARISON` / `valid_envelope=true`;
- both normal records retain `CAPTURE-STATE-042`, the exact three screen IDs/routes, live candidate process state at capture time, 1280×720 / one-frame metadata, three expected rendered-surface sample colors and exact candidate/project/executable/run/state binding metadata;
- FI1 retains the exact state marker and a live candidate process while the producer classifies capture separately as unavailable;
- Bevy/Defold/provider-bound cells and Issue #82 / reviewed S3-S5 preservation flags are not inflated.

Those checks establish that the packet is not broadly malformed. They do **not** cure the two material defects below.

## MAJOR — W2-ENG-TECH-S6-REV-M01: exact capture bytes and cross-attempt capture identity are not retained fail-closed

The producer contract required exact capture bytes/digest to be retained and required reuse of a capture from another attempt/candidate/generation to invalidate trusted representation.

The immutable final artifact contains **no PNG/frame bytes at all**. The workflow uploads only `docs/planning/wave-2/evidence/ci/engine-technical-s6/`; each real screenshot is created under the temporary per-attempt workspace and only its digest/metadata are copied into `evidence.json`. Consequently a reviewer cannot independently hash, decode, inspect or bind the actual frame bytes after the run.

The retained N1 and N2 Godot capture digests are also byte-identical:

- N1: `01a900635c799cd77a6ac809111c9499eb7438cdb310dc5fa643b41efd9284ea`
- N2: `01a900635c799cd77a6ac809111c9499eb7438cdb310dc5fa643b41efd9284ea`

The final correction at `b744552...` changes the producer negative from replacing N2's capture SHA field to replacing N2's **capture-binding metadata object** with N1's binding. That mutation correctly fails because the binding body contains `attempt: N1` and therefore disagrees with the N2 formal/raw envelope. It does **not** demonstrate that substituting/reusing the actual N1 frame bytes in N2 fails. With byte-identical frames and no retained bytes, byte reuse is observationally indistinguishable from a fresh capture.

This is material to S6's `identity_bound_capture` obligation and the task's explicit fail-closed reuse requirement. The producer self-test name `capture_reuse_substitution_rejected=true` overstates what the corrected negative actually attacks.

### Required remediation for M01

A bounded successor must preserve the exact producer branch and create fresh evidence that:

1. retains each trusted normal frame's actual bytes in the immutable evidence artifact (or an equivalently immutable byte-bearing object) and verifies the retained bytes against the recorded digest/format/dimensions;
2. mechanically binds those bytes to candidate, generation, attempt, run, state, executable/project identity and capture mechanism;
3. makes cross-attempt substitution/reuse of the **retained frame bytes/object** fail closed, not merely substitution of attempt-labelled binding metadata;
4. provides a meaningful negative even when the rendered visual state is deterministic—for example via a mechanically rendered attempt nonce/watermark or another candidate-visible per-attempt binding whose pixels are independently validated.

## MAJOR — W2-ENG-TECH-S6-REV-M02: `FI-S6-CAPTURE-DOWN-v2` is a synthetic return record, not an observed capture-pipeline failure

The exact producer runner's `capture(path, inject=True)` branch does not execute or disable a real capture operation. It immediately returns a hard-coded record containing:

- `command: ["everfield-s6-capture-disabled"]`;
- `exit: 97`;
- `expected_unavailable: true`;
- zero frames / no path;
- injection id `FI-S6-CAPTURE-DOWN-v2`.

No process corresponding to that command is executed, and the exit code is not an observed process exit. The subsequent `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE` classification is therefore derived from a harness-controlled synthetic record rather than a mechanically observed failure of the same candidate-bound capture path used by normal attempts.

The retained state-channel facts are useful: Godot reaches exact `CAPTURE-STATE-042` and remains alive. But the required S6 injection was specifically meant to show that state remains independently reachable **while the capture path is deliberately unavailable/failing** and to distinguish the two observed failure surfaces. A fabricated unavailable result demonstrates the classifier branch, not the capture-pipeline failure boundary.

### Required remediation for M02

A bounded successor must inject an actual, controlled failure into the candidate-bound capture path and retain its observed command/action, exit/error/absence facts. The same external semantic checker must then prove that exact state remains reachable and the candidate process remains alive while the capture operation genuinely fails/unavailable, and that relabelling it as `STATE_REACHABILITY` fails closed.

## Negative-control assessment

The packet retains producer negatives for wrong state marker, wrong viewport, missing frame, host-fabricated mechanism label, FI misclassification, generation mismatch, duplicate registry, reused workspace, raw/source substitution and candidate-process validation bypass. These are structurally useful and the retained final run reports them true. The independent producer verifier separately attacks wrong marker, wrong viewport, FI misclassification and duplicate registry.

However, M01 and M02 are outside what those booleans prove: the first concerns absent byte-bearing evidence / actual-byte substitution, and the second concerns whether an injection failure was observed rather than synthesized. Passing metadata mutations cannot promote those missing empirical facts.

## Scope and authority boundaries

- Godot `GEN-S6-8665917a0eb4a88a0e0f2f16`: remains **untrusted producer evidence pending remediation + fresh review**.
- Bevy 0.19.0: remains `INCONCLUSIVE_HARNESS_OR_INFRA`.
- Defold 1.13.0: remains `INCONCLUSIVE_HARNESS_OR_INFRA`.
- Unity 6000.5.6f1 / Unreal Engine 5.8: remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`.
- Failed/incomplete predecessor run `31967222552` / artifact `9268882622` remains non-authoritative provenance.
- Reviewed S3/S4/S5 evidence and Issue #82 historical 50 `NOT_RUN` cells remain unchanged.

This review grants no S1/S2/S7-S10 completion, five-candidate completion, engine ranking/selection, gameplay/high-throughput implementation, implementation/production readiness, provider/commercial/legal/platform/release authority, verification-PASS, decision, canonicality, or integration authority.

## Required next route

Route exactly one bounded S6 remediation successor from current `main`, preserving Issue #456 / PR #457 immutable. The remediation should address M01 and M02 only (plus any directly exposed fail-closed consequences), execute fresh evidence, retain immutable byte-bearing capture evidence and a real capture-down failure observation, and then receive a fresh independent/degraded-independent review before any bounded S6 comparison trust or integration consideration.
