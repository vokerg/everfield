#!/usr/bin/env python3
"""Constrain untrusted AI-produced patches before any GitHub write token is used.

The AI job has no contents:write permission. A separate publishing job fetches
this guard from trusted main, verifies the untrusted patch, and only then opens
a draft PR. Neither job integrates a change or grants review authority.
"""
from __future__ import annotations

import base64
import contextlib
import io
import tempfile
from pathlib import Path
import os
from pathlib import PurePosixPath
import re
import subprocess
import sys

MAX_FILES = 5
MAX_BYTES = 80_000
MAX_CHANGED_LINES = 1_000
ALLOWED_EXTENSIONS = {".gd", ".tscn", ".tres", ".gdshader", ".md", ".json", ".cfg"}
HEADER = re.compile(r"^diff --git a/(game/[A-Za-z0-9_./-]+) b/\1$")
FORBIDDEN = (
    "GIT binary patch", "Binary files ", "rename from ", "rename to ",
    "copy from ", "copy to ", "old mode ", "new mode ", "deleted file mode ",
    "new file mode 100755", "Submodule ",
)


def git(*args: str, input_bytes: bytes | None = None) -> bytes:
    result = subprocess.run(
        ["git", *args], input=input_bytes, capture_output=True, check=False
    )
    if result.returncode:
        raise ValueError(
            f"git {args[0]} failed: {result.stderr.decode(errors='replace')[:500]}"
        )
    return result.stdout


def valid_path(path: str) -> bool:
    p = PurePosixPath(path)
    return (
        path.startswith("game/")
        and not path.startswith("game/.godot/")
        and p.as_posix() == path
        and len(p.parts) >= 2
        and all(part not in {".", ".."} for part in path.split("/"))
        and p.suffix in ALLOWED_EXTENSIONS
        and len(path) <= 180
        and not path.endswith("/project.godot")
    )


def inspect_patch(patch: bytes) -> list[str]:
    if not patch or len(patch) > MAX_BYTES or b"\x00" in patch:
        raise ValueError("empty, oversized, or binary patch")
    content = patch.decode("utf-8")
    paths: list[str] = []
    changed_lines = 0
    for line in content.splitlines():
        if any(line.startswith(token) for token in FORBIDDEN):
            raise ValueError("forbidden binary, file mode, rename or copy operation")
        if line.startswith("diff --git "):
            match = HEADER.fullmatch(line)
            if not match or not valid_path(match.group(1)):
                raise ValueError("patch path outside restricted game source")
            if match.group(1) in paths:
                raise ValueError("duplicate diff path")
            paths.append(match.group(1))
        if (line.startswith("+") and not line.startswith("+++ ")) or (
            line.startswith("-") and not line.startswith("--- ")
        ):
            changed_lines += 1
    if not paths or len(paths) > MAX_FILES or changed_lines > MAX_CHANGED_LINES:
        raise ValueError("patch exceeds file or change budget")
    return paths


def capture() -> None:
    # Intent-to-add exposes new game source files to git diff; no commit/push.
    git("add", "-N", "--", "game")
    entries = git("status", "--porcelain=v1", "-z", "--untracked-files=all").decode().split("\x00")
    for entry in entries:
        if entry and (len(entry) < 4 or not entry[3:].startswith("game/") or
                      entry[:2].strip() in {"R", "C"}):
            raise ValueError("model touched an out-of-scope or renamed path")
    git("diff", "--check", "HEAD", "--", "game")
    patch = git("diff", "--binary", "--no-ext-diff", "HEAD", "--", "game")
    paths = inspect_patch(patch)
    for path in paths:
        if os.path.islink(path):
            raise ValueError("symbolic links prohibited")
    print(base64.b64encode(patch).decode("ascii"))


def publish() -> None:
    raw = os.environ.get("PATCH_B64", "")
    if not raw or len(raw) > 115_000:
        raise ValueError("missing or oversized patch transfer")
    patch = base64.b64decode(raw, validate=True)
    expected_paths = inspect_patch(patch)
    git("apply", "--check", "--index", "-", input_bytes=patch)
    git("apply", "--index", "-", input_bytes=patch)
    staged = git("diff", "--cached", "--name-only", "-z").decode().rstrip("\x00").split("\x00")
    if sorted(staged) != sorted(expected_paths):
        raise ValueError("staged files differ from reviewed patch header")
    for path in staged:
        if os.path.islink(path):
            raise ValueError("symbolic links prohibited")
        entries = git("ls-files", "--stage", "--", path).decode().splitlines()
        if len(entries) != 1 or not entries[0].startswith("100644 "):
            raise ValueError("only regular non-executable files allowed")
    git("diff", "--cached", "--check")
    print(f"guarded patch accepted: {len(staged)} game files (draft publication only)")


def self_test() -> None:
    good = (b"diff --git a/game/tests/fixture.gd b/game/tests/fixture.gd\n"
            b"new file mode 100644\nindex 0000000..1234567\n"
            b"--- /dev/null\n+++ b/game/tests/fixture.gd\n"
            b"@@ -0,0 +1 @@\n+extends Node\n")
    assert inspect_patch(good) == ["game/tests/fixture.gd"]
    for attack in (
        good.replace(b"game/tests/fixture.gd", b".github/workflows/inject.yml"),
        good.replace(b"new file mode 100644", b"new file mode 100755"),
        good + good,
        good.replace(b"@@ -0,0", b"GIT binary patch\n@@ -0,0"),
        b"",
        b"x" * (MAX_BYTES + 1),
        good.replace(b"game/tests/fixture.gd", b"game/../AGENTS.md"),
    ):
        try:
            inspect_patch(attack)
        except (ValueError, UnicodeDecodeError):
            pass
        else:
            raise AssertionError("unsafe patch was accepted")
    for path in ("game/../AGENTS.md", "game/project.godot", "tools/factory/a.gd",
                 "game/.godot/cache.json", "game/foo.exe", "game//tests/a.gd"):
        assert not valid_path(path), path
    # Exercise the complete capture -> cross-job transfer -> publish round trip
    # in a disposable real Git repository, without GitHub credentials.
    cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as directory:
        try:
            os.chdir(directory)
            git("init", "-q")
            git("config", "user.name", "Worker test")
            git("config", "user.email", "worker@example.invalid")
            Path("game/tests").mkdir(parents=True)
            existing = Path("game/tests/existing.gd")
            existing.write_text("extends Node\n")
            git("add", "--", "game")
            git("commit", "-q", "-m", "baseline")
            existing.write_text("extends Node\nvar tested = true\n")
            Path("game/tests/new.gd").write_text("extends Node2D\n")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                capture()
            encoded = output.getvalue().strip()
            assert inspect_patch(base64.b64decode(encoded))
            git("reset", "--hard", "HEAD")
            git("clean", "-fd")
            os.environ["PATCH_B64"] = encoded
            with contextlib.redirect_stdout(io.StringIO()):
                publish()
            assert existing.read_text() == "extends Node\nvar tested = true\n"
            assert Path("game/tests/new.gd").read_text() == "extends Node2D\n"
            assert sorted(git("diff", "--cached", "--name-only").decode().splitlines()) == [
                "game/tests/existing.gd", "game/tests/new.gd"
            ]
            git("reset", "--hard", "HEAD")
            git("clean", "-fd")
            Path("secrets.env").write_text("out-of-scope")
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    capture()
            except ValueError:
                pass
            else:
                raise AssertionError("out-of-scope untracked file accepted")
        finally:
            os.chdir(cwd)
            os.environ.pop("PATCH_B64", None)
    print("guarded worker patch self-test: PASS")


if __name__ == "__main__":
    try:
        if sys.argv[1:] == ["capture"]:
            capture()
        elif sys.argv[1:] == ["publish"]:
            publish()
        elif sys.argv[1:] == ["self-test"]:
            self_test()
        else:
            raise ValueError("expected capture, publish or self-test")
    except (ValueError, UnicodeError) as error:
        print(f"guarded worker rejected: {error}", file=sys.stderr)
        sys.exit(1)
