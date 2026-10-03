#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
godot_bin="${GODOT_BIN:-godot}"

if ! command -v "${godot_bin}" >/dev/null 2>&1 && [[ ! -x "${godot_bin}" ]]; then
  echo "[EF-MOVEMENT-SMOKE][ERROR] Godot executable not found: ${godot_bin}" >&2
  echo "Set GODOT_BIN to the reviewed Godot 4.7.1-stable executable." >&2
  exit 64
fi

version="$("${godot_bin}" --version)"
echo "[EF-MOVEMENT-SMOKE] godot_version=${version}"
if [[ ! "${version}" =~ ^4\.7\.1\.stable ]]; then
  echo "[EF-MOVEMENT-SMOKE][ERROR] expected Godot 4.7.1-stable, got ${version}" >&2
  exit 65
fi

"${godot_bin}" --headless --path "${repo_root}/game" --editor --quit
"${godot_bin}" --headless --path "${repo_root}/game" --script res://tests/movement_interaction_smoke.gd
