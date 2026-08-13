# W2-REM-ENG-05 — Issue #122 finding dispositions

**Mission:** `W2-REM-ENG-05` / Issue #126  
**Reviewed finding source:** Issue #122 / `W2-PG-REM-ENG-04`, exact work/head `c535bb9e94cb0da3aeb0d66dcc2606c034d7412f`, terminal comment `5276962394`  
**Corrected predecessor source:** Issue #112 exact work/head `6c5777ca56d43e22cba9b5e776e436d11b846325`  
**Authority:** bounded remediation evidence only; formal `W2-REV-01` remains required.

## Dispositions

### `PG-REM4-M01` — MAJOR — RESOLVED

The predecessor validator performed membership against `MATRIX` before closing the value type, so list-valued `result` or `failure_class` could raise `TypeError`.

The v5 validator validates both fields as nonempty strings before matrix lookup. Fresh list and dict regressions (`AG-30`, `AG-31`, `AG-42`, `AG-43`) all return structural `INCONCLUSIVE` with `valid_envelope=false`. No malformed value reaches comparison authority and no tested malformed shape raises.

### `PG-REM4-M02` — MAJOR — RESOLVED

The predecessor compared registry references with sets, allowing duplicate existing refs to alias to a valid set and retain `PASS_FOR_COMPARISON`.

The v5 validator requires each registry to be a list of nonempty unique IDs, requires cardinality equality with retained attempts, and then requires exact set/key equality. Duplicate, null, string, dict, omitted, and extra registry cases reject structurally. Fresh regressions `AG-32`, `AG-33`, `AG-34`, `AG-35`, `AG-44`, and `AG-45` cannot retain comparison authority.

### `PG-REM4-m01` — MINOR — RESOLVED

The predecessor assumed several nested adaptation/registry values were containers of the expected type before set/dict/hash operations.

The v5 validator closes `scenario_id`, `fixed_input_refs`, `mappings`, `bounds`, `failure_injections`, `start_profile`, and both registry shapes before consuming them. Fresh regressions `AG-36` through `AG-41` and `AG-46` through `AG-49` all reject deterministically.

## Mechanical evidence

- validator source SHA-256: `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`;
- predicted Git blob SHA: `2c646988dc16e212f43df6a4ee5ce646622ac2a6`;
- validator contract SHA-256: `ed1de63a02872c18981259a15eb8393b3d94d5f7af774b4b1f771c1c4e2e77ef`;
- feature slice SHA-256: `9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`;
- scenario manifest SHA-256: `be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`;
- fixture inputs SHA-256: `45555e8370f821d66fa8febdd58d475b88c15b0505ab996a4a8954ef8ef11613`;
- result object SHA-256: `8612a359c029e4d921356d214177a3478a0ee45011f8d26a629850180748a071`;
- deterministic stdout SHA-256: `e4a5279f4abb0a5b7eb4cfc2b4e64615be966c9e656dc4d6a610741b66a82ff0`;
- remediation attack evidence SHA-256: `58294d195025f32235bac3b6a7d4ea0eb20aebe0a79fb760fe80750eb069b9ef`;
- `python -m py_compile`: PASS;
- two full executions: byte-identical;
- inherited truth classes preserved: 51/51;
- fresh remediation regressions: 20/20 typed fail-closed;
- self-review: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

## Preserved boundaries

No engine was executed, scored, ranked, or selected. The v5 validator remains non-production planning experiment code. This disposition creates no implementation readiness, integration, verification, release, or canonicalization authority.

Formal aggregate `W2-REV-01` remains the required independent adjudication gate.
