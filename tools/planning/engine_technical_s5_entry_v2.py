#!/usr/bin/env python3
"""Issue #433 final bounded correction: parse candidate-prefixed metadata logs."""
from __future__ import annotations
import hashlib, importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
PREV = HERE.with_name('engine_technical_s5_entry.py')

def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

e = load(PREV, 'everfield_s5_entry_v1')
ENTRY_SHA = sha(HERE)
PREDECESSOR_ENTRY_SHA = sha(PREV)
MARKER = 'EVERFIELD_S5_METADATA:'

def metadata_line(result):
    if not result:
        return None
    for line in ((result.get('stdout') or '') + '\n' + (result.get('stderr') or '')).splitlines():
        pos = line.find(MARKER)
        if pos >= 0:
            return line[pos + len(MARKER):].strip()
    return None

# Defold prefixes script output with DEBUG:SCRIPT:, whereas Bevy/Godot emit the
# marker at column zero. Accept the marker at any position while preserving the
# exact suffix as the candidate-generated metadata value.
e._metadata_line = metadata_line
e.ENTRY_SHA = ENTRY_SHA
e.m.__file__ = str(HERE)
_prev_identity = e.m.toolchain_identity

def toolchain_identity(candidate, tool, validator_sha, runner_sha, run_identity):
    x = _prev_identity(candidate, tool, validator_sha, ENTRY_SHA, run_identity)
    x['body']['predecessor_entry_sha256'] = PREDECESSOR_ENTRY_SHA
    x['body']['metadata_log_prefix_parser'] = 'MARKER_SUBSTRING_FAIL_CLOSED_v1'
    x['identity_digest'] = 'sha256:' + e.m.digest_obj(x['body'])
    return x

e.m.toolchain_identity = toolchain_identity

def main() -> int:
    rc = e.main()
    if rc == 0 and '--out' in sys.argv:
        out = pathlib.Path(sys.argv[sys.argv.index('--out') + 1])
        d = json.loads(out.read_text())
        d.setdefault('producer_corrections', []).append({
            'run_id': 31959757285,
            'artifact_id': 9266994724,
            'artifact_digest': 'sha256:c1fd4cc41c989af24b38727f9c1e481b364678ec056ab2c1e9eda1636034a827',
            'evidence_sha256': '17d9f597566642f1dda1d621dc940942d08bfbbdf077ab93f83de2a105c3167a',
            'finding': 'DEFOLD_METADATA_LOG_PREFIX_PARSER_MISMATCH',
            'status': 'RETAINED_INCOMPLETE_PRODUCER_PROVENANCE',
        })
        out.write_text(json.dumps(d, indent=2, sort_keys=True) + '\n')
    return rc

if __name__ == '__main__':
    raise SystemExit(main())
