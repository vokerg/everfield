#!/usr/bin/env python3
"""Conservative, independent retirement of *proven rejected review-only* PRs.

A closed PR remains an immutable GitHub review/diff/provenance reference.
This tool never merges, promotes, deletes branches, or changes source PRs.
Default behavior is dry-run. Only a separately reviewed main workflow can apply.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
import re
import urllib.parse
import urllib.request
from typing import Any

import yaml

REPO = os.environ.get("GITHUB_REPOSITORY", "vokerg/everfield")
API = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
OWNER_LOGIN = "vokerg"
MIN_AGE = timedelta(hours=72)
MAX_OWNER_LEASE = timedelta(hours=6)
SHA40 = re.compile(r"^[0-9a-f]{40}$")
TITLE = re.compile(r"^\[PLAN-v1\]\[#([1-9][0-9]*)\]\s")
FENCE = re.compile(r"(?ms)^\x60\x60\x60yaml\s*\n(.*?)^\x60\x60\x60\s*$")


class StrictLoader(yaml.SafeLoader):
    """Refuse aliases and duplicate keys; never let YAML shadow authority."""

    def compose_node(self, parent: Any, index: Any) -> Any:
        if self.check_event(yaml.AliasEvent):
            raise ValueError("YAML aliases are not operational authority")
        if getattr(self.peek_event(), "tag", None) is not None:
            raise ValueError("explicit YAML tags are not operational authority")
        return super().compose_node(parent, index)

    def construct_mapping(self, node: yaml.nodes.MappingNode, deep: bool = False) -> dict:
        if not isinstance(node, yaml.nodes.MappingNode):
            raise ValueError("expected mapping")
        seen: set[str] = set()
        result: dict = {}
        for key_node, value_node in node.value:
            if not isinstance(key_node, yaml.nodes.ScalarNode):
                raise ValueError("complex YAML keys prohibited")
            if key_node.tag != "tag:yaml.org,2002:str":
                raise ValueError("only string mapping keys supported")
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in seen:
                raise ValueError("duplicate/invalid YAML authority key")
            seen.add(key)
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def operational(comment: dict[str, Any]) -> dict[str, Any] | None:
    if (
        comment.get("author_association") not in {"OWNER", "MEMBER", "COLLABORATOR"}
        or (comment.get("user") or {}).get("login") != OWNER_LOGIN
        or not comment.get("created_at")
        or comment.get("created_at") != comment.get("updated_at")
    ):
        return None
    blocks = FENCE.findall(comment.get("body") or "")
    if len(blocks) != 1:
        return None
    try:
        parsed = yaml.load(blocks[0], Loader=StrictLoader)
    except (yaml.YAMLError, ValueError, TypeError):
        return None
    if not isinstance(parsed, dict):
        return None
    if parsed.get("protocol") != "planning-v1" or parsed.get("schema") != 3:
        return None
    if not isinstance(parsed.get("kind"), str) or not isinstance(parsed.get("issue"), int):
        return None
    return parsed


def timestamp(text: str | None) -> datetime | None:
    if not isinstance(text, str) or not re.fullmatch(
        r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d)", text
    ):
        return None
    try:
        date = datetime.fromisoformat(text.replace("Z", "+00:00"))
        return date.astimezone(timezone.utc) if date.utcoffset() is not None else None
    except ValueError:
        return None


def eligibility(
    pr: dict[str, Any],
    review_issue: dict[str, Any],
    comments: list[dict[str, Any]],
    files: list[dict[str, Any]],
    open_issues: list[dict[str, Any]],
    now: datetime,
) -> tuple[bool, str]:
    """Never infer authority from PR prose, green CI, or mergeable alone."""
    number = pr.get("number")
    if not (
        isinstance(number, int)
        and pr.get("state") == "open"
        and pr.get("draft") is True
        and pr.get("merged_at") is None
        and (pr.get("user") or {}).get("login") == OWNER_LOGIN
        and pr.get("base", {}).get("ref") == "main"
    ):
        return False, "not owner-authored open draft against main"
    head = pr.get("head", {}).get("sha")
    if not isinstance(head, str) or SHA40.fullmatch(head) is None:
        return False, "unverifiable PR head"
    matched = TITLE.match(pr.get("title") or "")
    if matched is None:
        return False, "not a task-scoped reviewer PR"
    issue_number = int(matched.group(1))
    if (
        review_issue.get("number") != issue_number
        or review_issue.get("state") != "closed"
        or review_issue.get("state_reason") != "completed"
    ):
        return False, "review issue not terminal-closed"
    # Never delete or close the review surface while an open task references it.
    marker = re.compile(rf"(?<![0-9])#{number}(?![0-9])")
    if any(marker.search((issue.get("title") or "") + "\n" + (issue.get("body") or ""))
           for issue in open_issues if not issue.get("pull_request")):
        return False, "referenced by currently open issue"
    paths = [item.get("filename") for item in files]
    if not (
        len(paths) == 2
        and len(set(paths)) == 2
        and sum(str(p).startswith("docs/planning/wave-2/reviews/") for p in paths) == 1
        and sum(str(p).startswith("docs/planning/handoffs/") for p in paths) == 1
    ):
        return False, "not exact two-path review-only packet"

    records = [(item, operational(item)) for item in comments]
    records = [(item, r) for item, r in records if r is not None and r.get("issue") == issue_number]
    terminals = [(c, r) for c, r in records if r.get("kind") == "REVIEW_STATUS"
                 and r.get("state") == "CHANGES_NEEDED" and r.get("terminal") is True]
    if len(terminals) != 1:
        return False, "not exactly one valid negative review terminal"
    comment, terminal = terminals[0]
    if not (
        terminal.get("authority_mode") == "REVIEWER"
        and terminal.get("pr_number") == number
        and terminal.get("pr_head_sha") == head
        and terminal.get("head_sha") == head
        and terminal.get("pr_draft") is True
        and isinstance(terminal.get("required_next_route"), str)
        and terminal["required_next_route"].startswith(("MATERIALIZE_", "BLOCKING_"))
        and isinstance(terminal.get("mission_id"), str)
        and isinstance(terminal.get("actor_session_id"), str)
    ):
        return False, "terminal missing exact negative-review authority"
    owner_id = terminal.get("ownership_generation_comment_id")
    owners = [(c, r) for c, r in records if c.get("id") == owner_id
              and r.get("kind") in {"CLAIM", "RESUME", "RECOVER"}]
    if len(owners) != 1:
        return False, "missing unique owner generation"
    owner_c, owner = owners[0]
    terminal_time = timestamp(comment.get("created_at"))
    owner_time = timestamp(owner_c.get("created_at"))
    if (
        terminal_time is None
        or owner_time is None
        or terminal_time < owner_time
        or terminal_time >= owner_time + MAX_OWNER_LEASE
        or now - terminal_time < MIN_AGE
        or now < terminal_time
        or owner.get("state") != "IN_PROGRESS"
        or owner.get("mission_id") != terminal["mission_id"]
        or owner.get("actor_session_id") != terminal["actor_session_id"]
        or owner_c.get("id", 0) >= comment.get("id", 0)
    ):
        return False, "unproven in-lease negative terminal or recent review"
    return True, f"terminal #{comment['id']}, exact head {head}"


def request(path: str, method: str = "GET", data: dict | None = None) -> Any:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN required for live GitHub reads/writes")
    url = API + path
    payload = None if data is None else json.dumps(data).encode()
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "everfield-review-draft-retirement/1"}
    if payload is not None:
        headers["Content-Type"] = "application/json"
    with urllib.request.urlopen(urllib.request.Request(
        url, headers=headers, data=payload, method=method
    ), timeout=25) as response:
        raw = response.read()
        return json.loads(raw) if raw else None


def paged(path: str) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    page = 1
    while True:
        separator = "&" if "?" in path else "?"
        values = request(f"{path}{separator}per_page=100&page={page}")
        if not isinstance(values, list):
            raise RuntimeError("GitHub API returned non-list")
        result.extend(values)
        if len(values) < 100:
            break
        page += 1
    return result


def execute(*, apply: bool) -> None:
    root = "/repos/" + urllib.parse.quote(REPO, safe="/")
    now = datetime.now(timezone.utc)
    prs = paged(f"{root}/pulls?state=open")
    open_issues = paged(f"{root}/issues?state=open")
    possible = 0
    retired = 0
    for pr in prs:
        if not (pr.get("draft") is True and TITLE.match(pr.get("title") or "")):
            continue
        number = pr["number"]
        issue_number = int(TITLE.match(pr["title"]).group(1))
        issue = request(f"{root}/issues/{issue_number}")
        comments = paged(f"{root}/issues/{issue_number}/comments")
        files = paged(f"{root}/pulls/{number}/files")
        eligible, reason = eligibility(pr, issue, comments, files, open_issues, now)
        print(f"PR #{number}: {'eligible' if eligible else 'skip'} — {reason}")
        if not eligible:
            continue
        possible += 1
        if apply:
            # Re-read every mutable PR fact immediately before the state write.
            current = request(f"{root}/pulls/{number}")
            safe, why = eligibility(current, issue, comments, files, open_issues, now)
            if not safe or current["head"]["sha"] != pr["head"]["sha"]:
                print(f"PR #{number}: concurrent change, fail closed — {why}")
                continue
            request(f"{root}/pulls/{number}", "PATCH", {"state": "closed"})
            retired += 1
    print(f"negative-review retirement: eligible={possible} closed={retired} apply={apply}")


def self_test() -> None:
    now = datetime(2026, 10, 20, tzinfo=timezone.utc)
    head = "a" * 40
    claim_time = "2026-10-10T10:00:00Z"
    terminal_time = "2026-10-10T11:00:00Z"

    def comment(id: int, when: str, body: str) -> dict[str, Any]:
        return {"id": id, "created_at": when, "updated_at": when,
                "author_association": "OWNER", "user": {"login": OWNER_LOGIN}, "body": body}

    fence = chr(96) * 3
    claim = comment(1, claim_time, f"""{fence}yaml
protocol: planning-v1
schema: 3
kind: CLAIM
issue: 199
mission_id: R-01
actor_session_id: reviewer-1
state: IN_PROGRESS
{fence}""")
    terminal = comment(2, terminal_time, f"""{fence}yaml
protocol: planning-v1
schema: 3
kind: REVIEW_STATUS
issue: 199
mission_id: R-01
actor_session_id: reviewer-1
state: CHANGES_NEEDED
terminal: true
authority_mode: REVIEWER
ownership_generation_comment_id: 1
head_sha: {head}
pr_number: 200
pr_head_sha: {head}
pr_draft: true
required_next_route: MATERIALIZE_FIX
{fence}""")
    pr = {"number": 200, "title": "[PLAN-v1][#199] Required negative review",
          "state": "open", "draft": True, "merged_at": None,
          "head": {"sha": head}, "base": {"ref": "main"},
          "user": {"login": OWNER_LOGIN}}
    issue = {"number": 199, "state": "closed", "state_reason": "completed"}
    files = [{"filename": "docs/planning/wave-2/reviews/negative.md"},
             {"filename": "docs/planning/handoffs/issue-199.md"}]
    ok = lambda p=pr, c=[claim, terminal], f=files, opened=[], t=now: eligibility(
        p, issue, c, f, opened, t)[0]
    assert ok()
    assert not ok(p=dict(pr, draft=False))
    assert not ok(p=dict(pr, head={"sha": "b" * 40}))
    assert not ok(p=dict(pr, state="closed"))
    assert not ok(p=dict(pr, base={"ref": "other"}))
    assert not ok(f=[{"filename": "game/main.gd"}, files[1]])
    assert not ok(opened=[{"title": "Active successor", "body": "needs PR #200 OPEN/DRAFT"}])
    assert not ok(t=datetime(2026, 10, 11, tzinfo=timezone.utc))
    assert not ok(c=[claim, dict(terminal, updated_at="2026-10-10T11:01:00Z")])
    assert not ok(c=[claim, dict(terminal, author_association="NONE")])
    assert not ok(c=[dict(claim, body=claim["body"].replace("reviewer-1", "other")), terminal])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("CHANGES_NEEDED", "REVIEW_READY"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("pr_number: 200", "pr_number: 201"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("kind: REVIEW_STATUS", "kind: STATUS"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("terminal: true", "terminal: false"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("pr_draft: true", "pr_draft: false"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("state: CHANGES_NEEDED", "state: CHANGES_NEEDED\nstate: CHANGES_NEEDED"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("protocol: planning-v1", "protocol: *shadow"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("protocol: planning-v1", "protocol: !!str planning-v1"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"] + "\n\x60\x60\x60yaml\nkind: REVIEW_STATUS\n\x60\x60\x60")])
    assert not ok(c=[claim, dict(terminal, created_at="2026-10-10T17:00:00Z", updated_at="2026-10-10T17:00:00Z")])
    print("retire negative reviewer-only drafts self-test: PASS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Mutating operation; default is dry run")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        execute(apply=args.apply)
