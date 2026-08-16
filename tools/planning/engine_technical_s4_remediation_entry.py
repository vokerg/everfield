#!/usr/bin/env python3
"""Entry shim for W2-ENG-TECH-S4-REM-01 fail-closed remediation.

Keeps the main remediation implementation readable while removing ephemeral path
material from toolchain identity, locating Defold's candidate-produced save
surfaces inside its isolated copied bundle, and binding the exact remediation
implementation/entry bytes into candidate identity.
"""
from __future__ import annotations
import hashlib, pathlib
import engine_technical_s4_remediation as r


def _sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _scrub(value):
    ephemeral = {
        "path", "executable", "cmd", "seconds", "stdout", "stderr",
        "timed_out", "download", "probe", "vendor_digest_probe", "version",
        "unzip", "bob_version",
    }
    if isinstance(value, dict):
        return {k: _scrub(v) for k, v in sorted(value.items()) if k not in ephemeral}
    if isinstance(value, list):
        return [_scrub(v) for v in value]
    return value


def canonical_toolchain(tool):
    """Retain exact content/version facts while excluding temp-path/run noise."""
    return _scrub(tool)


def host_semantics(clean, ws, mode):
    """Verify the exact candidate output directory for all candidates.

    Bevy/Godot write directly under ws. Defold executes inside ws/bundle/...;
    find the unique candidate input there and run the unchanged producer host
    verifier against that directory rather than laundering/copying outputs.
    """
    ws = pathlib.Path(ws)
    if (ws / "input.save").exists():
        return clean.host_semantics(ws, mode)
    candidates = sorted(ws.rglob("input.save"))
    if len(candidates) != 1:
        return {"pass": False, "reason": "candidate_output_directory_not_unique", "input_candidates": len(candidates)}
    return clean.host_semantics(candidates[0].parent, mode)


_original_candidate_identity = r.candidate_identity
_BASE = pathlib.Path(r.__file__).resolve()
_ENTRY = pathlib.Path(__file__).resolve()


def candidate_identity(candidate, version, tool, binary_sha, build_body, validator_sha, producer_sha, run_identity):
    identity = _original_candidate_identity(
        candidate, version, tool, binary_sha, build_body,
        validator_sha, producer_sha, run_identity,
    )
    identity["body"]["remediation_base_sha256"] = _sha(_BASE)
    identity["body"]["remediation_entry_sha256"] = _sha(_ENTRY)
    identity["identity_digest"] = "sha256:" + r.H(identity["body"])
    return identity


r.canonical_toolchain = canonical_toolchain
r.host_semantics = host_semantics
r.candidate_identity = candidate_identity

if __name__ == "__main__":
    raise SystemExit(r.main())
