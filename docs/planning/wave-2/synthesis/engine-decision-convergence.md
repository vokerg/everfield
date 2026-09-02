# W2-ENG-DECISION-CONVERGENCE-01 — engine recommendation from current evidence

## Status and authority

- issue: `#804`
- mission: `W2-ENG-DECISION-CONVERGENCE-01`
- claim: `5511538149`
- frozen base: `main@eb81d354931c67ef2193f5242e49ee181a270b8c`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- owner engine-decision convergence directive: Issue #84 comment `5511466516`
- disposition: `ENGINE_SELECTION_READY_FOR_CANONICAL_DECISION`
- recommendation: **Godot `4.7.1-stable`**
- engine selected: **false**
- comparison evidence complete: **false**
- implementation ready: **false**
- canonicality: `NOT_CANONICAL`

This packet is a bounded recommendation, not an engine ADR, canonical selection, readiness grant, or implementation authorization. It separates development operability, hosted-CI/provider unlock, and comparison completeness as distinct predicates.

## Decision question

Is the evidence already accumulated sufficient to recommend one engine for the formal engine-selection gate now, without requiring complete provider/toolchain parity across all five candidates?

**Answer: yes.** Current reviewed evidence is decision-materially sufficient to recommend Godot `4.7.1-stable`. No remaining single missing fact is required before the recommendation can enter the required independent review and formal decision/readiness route.

## Frozen decision-material evidence

### Reviewed comparison evidence

The public-toolchain programme has exact bounded reviewed evidence under the unchanged v5 comparison envelope for:

- **S3**: Bevy, Defold, Godot — Issue #358 terminal review `5305399666`, `PASS_WITH_MINOR_NOTES_BOUNDED_S3_V5`;
- **S4**: Bevy, Defold, Godot — Issue #374 terminal review `5305617167`, `PASS_BOUNDED_REMEDIATED_S4_V5_ENVELOPE`;
- **S5**: Bevy, Defold, Godot — Issue #454 terminal review `5309016465`, `PASS_BOUNDED_S5_V5_ENVELOPE`;
- **S6**: Godot has a later formal-bound reviewed remediation through Issues #591/#596, exact run `32043481976`, artifact `9292381852`, generation `GEN-S6R2-8368fa27bb014316e11cc5bf`, with zero BLOCKER / MAJOR / correction-requiring MINOR and disposition `PASS_BOUNDED_FORMAL_BOUND_GODOT_S6_V5_ENVELOPE`; Bevy/Defold S6 outcomes remain inconclusive and are not promoted;
- **S7**: Bevy, Defold, Godot — Issue #517 terminal review `5312812966`, `PASS_BOUNDED_S7_BROKEN_REFERENCE_EVIDENCE`.

S1, S2, S8, S9, and S10 remain incomplete. That incompleteness is retained. The owner convergence directive explicitly removes complete parity as a global selection prerequisite when the remaining uncertainty is not decision-material.

### Unity development operability

Unity `6000.5.6f1` executed native S3 successfully on the approved persistent runner `everfield-unity-mac` in evaluator run `33595213169`, attempt `2`, job `100160452746`; the job records `native_s3_pass: true`. The later failure occurred at `actions/upload-artifact` with GitHub `403 Forbidden: job is completed`.

Therefore:

- `development_usable_now = true` for the approved persistent Unity context;
- that native success is **not** relabelled as GitHub-hosted provider PASS;
- that native success is **not** promoted here to reviewed-v5 `PASS_FOR_COMPARISON`;
- hosted GitHub ephemeral-provider state remains blocked at `UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED`.

Unity is not rejected as technically unusable. Its remaining hosted licensing/session and comparison-lineage debt are operational/comparison uncertainties, not proof of development failure.

### Unreal development/provider state

Current repository-controlled Unreal evidence has progressed through registry authorization and container pull, but remains blocked at `UE_NATIVE_EDITOR_BINARY_NOT_FOUND_IN_PINNED_CONTAINER`; native editor/S3 execution has not been reached in the current route.

Per owner directive `5511466516`, that incomplete Unreal path is not a global engine-selection blocker unless one concrete fact can plausibly overturn the recommendation and can be resolved in one bounded continuation. No such recommendation-flipping fact is identified below.

## Compact comparison

| Candidate | Technical fit / reviewed evidence | Reproducibility | Tooling maturity for this project | Development usable now | Hosted-CI/provider state | Comparison complete | Material unresolved risk | Decision result |
|---|---|---|---|---|---|---|---|---|
| Bevy `0.19.0` | Trusted S3/S4/S5/S7 | Strong public-toolchain repeatability | Strong repo-native/code-first evidence | Yes | Public toolchain executes without a commercial-provider credential gate in the reviewed route | No | S6 remains inconclusive; S1/S2/S8-S10 incomplete | Viable alternative |
| Defold `1.13.0` | Trusted S3/S4/S5/S7 | Strong public-toolchain repeatability | Lean candidate-native tooling demonstrated | Yes | Public toolchain executes without a commercial-provider credential gate in the reviewed route | No | S6 remains inconclusive; S1/S2/S8-S10 incomplete | Viable alternative |
| **Godot `4.7.1-stable`** | **Trusted S3/S4/S5/S6/S7** | **Strong public-toolchain repeatability** | **General-purpose editor/runtime plus headless automation demonstrated across the broadest trusted scenario set** | **Yes** | **Public toolchain executes without a commercial-provider credential gate in the reviewed route** | No | S1/S2/S8-S10 incomplete | **RECOMMEND** |
| Unity `6000.5.6f1` | Exact-current-main persistent native S3 succeeds, but no reviewed-v5 comparison generation is promoted by this packet | Persistent-runner execution is proven; formal comparison/publication lineage remains incomplete | Mature editor/runtime; approved persistent development context works | Yes, persistent context | Hosted ephemeral lane remains `UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED` | No | Hosted license/session friction plus formal reviewed comparison debt | Do not select over Godot from current evidence |
| Unreal Engine `5.8` | No current native editor/scenario comparison result | Repository-controlled path has not reached editor execution | Heavy provider/editor path remains unresolved | Not proven in current repo-controlled path | `UE_NATIVE_EDITOR_BINARY_NOT_FOUND_IN_PINNED_CONTAINER` | No | Highest immediate execution/toolchain uncertainty | Non-blocking alternative pending future evidence |

`Hosted-CI/provider state` above is not treated as the same predicate as development usability. For Bevy/Defold/Godot the reviewed route is a public-toolchain execution path rather than a protected commercial-provider unlock.

## Recommendation

Recommend **Godot `4.7.1-stable`** to the formal engine-selection decision gate.

The recommendation rests on the conjunction of decision-material facts already established in the programme:

1. **Broadest trusted scenario envelope.** Godot is the only candidate with bounded reviewed comparison evidence across S3, S4, S5, S6, and S7. Bevy and Defold remain strong alternatives but lack trusted S6 evidence; Unity's fresh persistent native S3 proves development operability but is not yet reviewed comparison evidence; Unreal has not reached native editor execution.
2. **Reproducible repository-controlled execution.** Godot's evidence is produced through the public toolchain and has survived repeated producer/remediation/review gates under the v5 envelope.
3. **Development operability now.** Godot is runnable in the repository-owned execution path without a current external licensing/session predicate. This is an operational advantage, not a claim about commercial superiority.
4. **Lower current critical-path friction.** Choosing Godot does not require the hosted Unity licensing gate or the unresolved Unreal editor/container path before selected-engine bootstrap can begin after formal decision/readiness gates.
5. **No current evidence-supported comparative advantage requires waiting.** Unity's demonstrated native S3 success correctly prevents an “Unity cannot run” conclusion, but it does not supply a reviewed comparative advantage that outweighs Godot's broader trusted envelope. Unreal's first future native-editor success would narrow uncertainty but would not by itself erase the current multi-scenario evidence gap. Additional parity work therefore is not decision-material enough to remain on the critical path.

This is an evidence-bound recommendation, not a reputation/project-size judgment and not a scalar-score winner.

## Explicit predicate separation

- `development-usable now`:
  - Bevy: true in reviewed public-toolchain route;
  - Defold: true in reviewed public-toolchain route;
  - Godot: true in reviewed public-toolchain route;
  - Unity: true in approved persistent-runner context;
  - Unreal: not proven in current repository-controlled editor path.
- `hosted-CI fully provider-unlocked`:
  - Unity: false (`UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED`);
  - Unreal: false (`UE_NATIVE_EDITOR_BINARY_NOT_FOUND_IN_PINNED_CONTAINER`);
  - Bevy/Defold/Godot: no protected commercial-provider unlock is required by their reviewed public-toolchain routes.
- `comparison evidence complete`: false for every candidate and for the five-candidate matrix as a whole.

None of those predicates is silently substituted for another.

## Decision-material missing fact test

No exact missing fact currently meets both conditions required to block the recommendation:

1. it could plausibly reverse the recommendation; and
2. it can be resolved through one short bounded continuation whose value exceeds the existing evidence gap.

A fresh Unity reviewed-v5 S3 binding would strengthen Unity but would still leave Godot with a broader trusted scenario envelope. A first Unreal native-editor/S3 result would prove basic operability but would still leave a larger comparison-evidence gap. Finishing arbitrary S1/S2/S8-S10 parity for all candidates is precisely the open-ended completeness campaign the owner convergence directive forbids.

Therefore the stopping disposition is **`ENGINE_SELECTION_READY_FOR_CANONICAL_DECISION`**, not `ONE_DECISION_MATERIAL_FACT_REQUIRED`.

## Required next gate

This producer cannot self-authorize engine selection. The exact immutable synthesis head must receive one fresh required independent/degraded-independent review that attacks:

- frozen evidence identity and scope;
- the Godot-vs-Bevy/Defold evidence distinction, including S6;
- Unity native-S3 success versus upload/provider/comparison authority boundaries;
- Unreal non-blocking treatment under owner directive `5511466516`;
- the separation of development usability, hosted provider unlock, and comparison completeness;
- whether any omitted fact could materially reverse the recommendation;
- authority inflation, implementation/readiness leakage, or hidden parity gates.

A clean review may route only the existing/smallest formal Wave-2 engine decision/readiness/canonical gate. It does not itself select Godot, integrate this packet, or authorize gameplay/high-throughput implementation.

## Residual debt after recommendation

Remaining Unity hosted-provider/publication work, Unreal provider/editor work, and incomplete scenario evidence remain noncanonical technical debt and may continue in parallel where separately eligible. They reopen the recommendation only if later reviewed evidence establishes a concrete material contradiction or a decision-gate reviewer finds a recommendation-flipping defect.

## Authority boundary

`NOT_CANONICAL`. This packet grants no engine selection, canonical ADR, implementation readiness, gameplay/high-throughput implementation, provider PASS, license/entitlement, production/commercial/legal/platform/release authority, verification PASS, integration authority, or canonical authority.
