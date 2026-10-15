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



PR_URL = re.compile(r"https://[^\s<>\[\](){}\"'\x60]+", re.IGNORECASE)


def references_pr(text: str, number: int) -> bool:
    """Fail closed on first-party PR URL variants in active issues/comments.

    A canonical PR reference may use GitHub's explicit HTTPS port 443, a
    .diff/.patch endpoint, encoded path segments, or PR subresources. Parse
    host and port separately: netloc includes :443 and is not the hostname.
    Unknown/malformed first-party authority is a veto, not proof of absence.
    """
    if re.search(rf"(?<![0-9])#{number}(?![0-9])", text):
        return True
    if not isinstance(REPO, str) or REPO.count("/") != 1:
        return True
    owner, repository = REPO.split("/")
    if not owner or not repository:
        return True
    for match in PR_URL.finditer(text):
        link = match.group(0).rstrip(".,;!:")
        try:
            url = urllib.parse.urlsplit(link)
            # Percent-encoded host dots/case and a DNS trailing dot cannot
            # turn a first-party URL into apparently unrelated provenance.
            hostname = urllib.parse.unquote(url.hostname or "").casefold().rstrip(".")
        except (ValueError, UnicodeError):
            return True
        if hostname not in {"github.com", "api.github.com"}:
            continue
        try:
            port = url.port
        except ValueError:
            return True
        if (url.scheme.lower() != "https"
                or url.username is not None or url.password is not None
                or port not in (None, 443)):
            # Do not interpret ambiguous first-party authorities as absence.
            return True
        segments = [item.casefold() for item in
                    urllib.parse.unquote(url.path).split("/") if item]
        prefix = ([owner, repository, "pull"] if hostname == "github.com"
                  else ["repos", owner, repository, "pulls"])
        prefix = [item.casefold() for item in prefix]
        if len(segments) <= len(prefix) or segments[:len(prefix)] != prefix:
            continue
        pr_segment = segments[len(prefix)]
        candidate = str(number)
        if pr_segment in {candidate, candidate + ".diff", candidate + ".patch"}:
            return True
    return False

def eligibility(
    pr: dict[str, Any],
    review_issue: dict[str, Any],
    comments: list[dict[str, Any]],
    files: list[dict[str, Any]],
    open_issues: list[dict[str, Any]],
    now: datetime,
) -> tuple[bool, str]:
    """Prove a very conservative canonical subset; unknown history stays open.

    Deliberately permits only one first CLAIM with no subsequent progress,
    handoff, resume, recovery, revision or rival ownership. Complete canonical
    renewal semantics are not needed for this storage-only safe subset.
    """
    number = pr.get("number")
    if not (
        type(number) is int
        and pr.get("state") == "open"
        and pr.get("draft") is True
        and pr.get("merged_at") is None
        and (pr.get("user") or {}).get("login") == OWNER_LOGIN
        and (pr.get("base") or {}).get("ref") == "main"
    ):
        return False, "not a sole owner-authored unmerged draft"
    head_record = pr.get("head")
    base_record = pr.get("base")
    if not isinstance(head_record, dict) or not isinstance(base_record, dict):
        return False, "missing actual GitHub PR head/base repository"
    head = head_record.get("sha")
    if not isinstance(head, str) or SHA40.fullmatch(head) is None:
        return False, "missing exact head"
    matched = TITLE.match(pr.get("title") or "")
    if matched is None:
        return False, "not a reviewer task PR"
    issue_number = int(matched.group(1))
    # A shared SHA, title or login is not authority for a task branch or fork.
    if (
        head_record.get("ref") != f"planning/issue-{issue_number}"
        or not isinstance(head_record.get("repo"), dict)
        or head_record["repo"].get("full_name") != REPO
        or not isinstance(base_record.get("repo"), dict)
        or base_record["repo"].get("full_name") != REPO
    ):
        return False, "actual PR task branch or repository identity mismatch"
    if not (
        review_issue.get("number") == issue_number
        and review_issue.get("state") == "closed"
        and review_issue.get("state_reason") == "completed"
        and (review_issue.get("user") or {}).get("login") == OWNER_LOGIN
        and (review_issue.get("title") or "").startswith("[PLAN-v1]")
    ):
        return False, "unproven review issue terminal and trusted author"
    # The independently authored task contract, not terminal artifact_paths,
    # is the source of authority for a review's exact mission/report identity.
    contract = review_issue.get("body")
    if not isinstance(contract, str):
        return False, "unreadable authoritative reviewer issue contract"
    mission_matches = re.findall(
        r"(?m)^## Mission ID\s*\n\s*([A-Z][A-Z0-9_-]+)\s*$", contract
    )
    report_matches = re.findall(
        r"docs/planning/wave-2/reviews/[A-Za-z0-9][A-Za-z0-9_.-]*-review\.md",
        contract,
    )
    if (
        len(mission_matches) != 1
        or len(set(report_matches)) != 1
        or not report_matches
        or "independent" not in contract.lower()
        or "review" not in contract.lower()
    ):
        return False, "uncertain reviewer mission/report contract"
    required_report_path = report_matches[0]
    required_mission_id = mission_matches[0]

    # All active references, including comments, must be freshly covered.
    for issue in open_issues:
        if issue.get("pull_request"):
            continue
        live_comments = issue.get("live_comments")
        if (
            issue.get("state") != "open"
            or type(issue.get("number")) is not int
            or issue.get("comments_coverage_complete") is not True
            or not isinstance(live_comments, list)
            or not isinstance(issue.get("title"), str)
            or not isinstance(issue.get("body"), str)
            or any(not isinstance(c, dict) or not isinstance(c.get("body"), str)
                   for c in live_comments)
        ):
            return False, "incomplete live open-issue comment reference coverage"
        if references_pr(issue["title"] + "\n" + issue["body"], number) or any(
            references_pr(c["body"], number) for c in live_comments
        ):
            return False, "open issue or its comment still references this PR"

    if len(files) != 2:
        return False, "not exact two-path reviewer-only diff"
    paths = [f.get("filename") for f in files]
    if not all(
        isinstance(f.get("filename"), str)
        and f.get("status") == "added"
        and isinstance(f.get("sha"), str)
        and SHA40.fullmatch(f["sha"]) is not None
        for f in files
    ) or len(set(paths)) != 2:
        return False, "unverifiable reviewer-only file status or blobs"
    handoff = f"docs/planning/handoffs/issue-{issue_number}.md"
    reports = [p for p in paths if p != handoff]
    if (
        handoff not in paths
        or len(reports) != 1
        or reports[0] != required_report_path
        or re.fullmatch(
            r"docs/planning/wave-2/reviews/[A-Za-z0-9][A-Za-z0-9_.-]*-review\.md",
            reports[0],
        ) is None
    ):
        return False, "wrong reviewer report/handoff identity"

    # Any unreadable or edited operational-looking comment disqualifies closure.
    # A later new status (including a valid REOPEN/REVIEW_READY) defeats a stale
    # negative even if the old negative terminal is immutable.
    operational_records = []
    for c in comments:
        parsed = operational(c)
        capsule_like = "protocol: planning-v1" in (c.get("body") or "") and "kind:" in (c.get("body") or "")
        if parsed is None:
            if capsule_like:
                return False, "unknown or edited operational-looking history"
            continue
        if parsed.get("issue") != issue_number:
            return False, "conflicting issue-local authority"
        operational_records.append((c, parsed))
    if len(operational_records) != 2:
        return False, "not a simple single-owner canonical prefix"
    operational_records.sort(key=lambda item: item[0]["id"])
    (owner_c, owner), (terminal_c, terminal) = operational_records
    if not (
        owner.get("kind") == "CLAIM"
        and owner.get("state") == "IN_PROGRESS"
        and owner.get("previous_ownership_comment_id") is None
        and owner.get("branch") == f"planning/issue-{issue_number}"
        and isinstance(owner.get("mission_id"), str)
        and bool(owner["mission_id"])
        and owner["mission_id"] == required_mission_id
        and isinstance(owner.get("actor_session_id"), str)
        and bool(owner["actor_session_id"])
        and isinstance(owner.get("base_sha"), str)
        and SHA40.fullmatch(owner["base_sha"]) is not None
        and owner.get("observed_head_sha") == owner["base_sha"]
        and terminal.get("kind") == "REVIEW_STATUS"
        and terminal.get("state") == "CHANGES_NEEDED"
        and terminal.get("terminal") is True
        and terminal.get("authority_mode") == "REVIEWER"
        and terminal.get("issue") == issue_number
        and terminal.get("branch") == owner["branch"]
        and terminal.get("mission_id") == owner["mission_id"]
        and terminal.get("actor_session_id") == owner["actor_session_id"]
        and terminal.get("ownership_generation_comment_id") == owner_c["id"]
        and terminal.get("base_sha") == owner["base_sha"]
        and terminal.get("pr_number") == number
        and terminal.get("pr_head_sha") == head
        and terminal.get("work_sha") == head
        and terminal.get("head_sha") == head
        and terminal.get("pr_draft") is True
        and isinstance(terminal.get("required_next_route"), str)
        and terminal["required_next_route"].startswith(("MATERIALIZE_", "BLOCKING_"))
        and isinstance(terminal.get("artifact_paths"), list)
        and len(terminal["artifact_paths"]) == 2
        and set(terminal["artifact_paths"]) == set(paths)
    ):
        return False, "invalid first-owner/exact-terminal/actual-artifacts proof"
    owner_time = timestamp(owner_c.get("created_at"))
    terminal_time = timestamp(terminal_c.get("created_at"))
    if (
        owner_time is None
        or terminal_time is None
        or not owner_time <= terminal_time < owner_time + MAX_OWNER_LEASE
        or terminal_c["id"] <= owner_c["id"]
        or now < terminal_time
        or now - terminal_time < MIN_AGE
    ):
        return False, "expired owner, invalid comment ordering or grace period"
    return True, f"single-CLAIM in-lease negative #{terminal_c['id']} at immutable {head}"


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


def live_open_issue_references(root: str) -> list[dict[str, Any]]:
    """Conservatively cover EVERY active issue and all of its comments.

    Unknown pagination, inconsistent API comment counts or excessive scan
    volume aborts before PATCH. These separate reads cannot be atomic with a
    subsequent GitHub PATCH; the residual last-millisecond race remains.
    """
    issues = paged(f"{root}/issues?state=open")
    if len(issues) > 200:
        raise RuntimeError("open-issue frontier too large for bounded comment scan")
    refs: list[dict[str, Any]] = []
    seen: set[int] = set()
    for issue in issues:
        if not isinstance(issue, dict):
            raise RuntimeError("malformed live GitHub issue")
        if issue.get("pull_request"):
            continue
        number = issue.get("number")
        count = issue.get("comments")
        if (
            type(number) is not int or number <= 0 or number in seen
            or issue.get("state") != "open"
            or type(count) is not int or count < 0 or count > 1000
            or not isinstance(issue.get("title"), str)
            or not isinstance(issue.get("body"), str)
        ):
            raise RuntimeError("incomplete active issue identity/comment count")
        seen.add(number)
        comments = paged(f"{root}/issues/{number}/comments") if count else []
        if len(comments) != count:
            raise RuntimeError("incomplete active issue comment pagination")
        comment_ids: set[int] = set()
        for comment in comments:
            if not isinstance(comment, dict):
                raise RuntimeError("malformed live issue comment")
            cid = comment.get("id")
            if (
                type(cid) is not int or cid <= 0 or cid in comment_ids
                or not isinstance(comment.get("body"), str)
                or not isinstance(comment.get("created_at"), str)
            ):
                raise RuntimeError("duplicate or unauthenticated live issue comment")
            comment_ids.add(cid)
        refs.append(dict(issue, live_comments=comments,
                         comments_coverage_complete=True))
    return refs


def execute(*, apply: bool) -> None:
    root = "/repos/" + urllib.parse.quote(REPO, safe="/")
    now = datetime.now(timezone.utc)
    prs = paged(f"{root}/pulls?state=open")
    open_issues = live_open_issue_references(root)
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
            # Force fresh independent API reads immediately before each PATCH.
            # GitHub does not offer a compare-and-swap close endpoint, so this
            # narrows but cannot make the check+PATCH atomic.
            current_pr = request(f"{root}/pulls/{number}")
            current_issue = request(f"{root}/issues/{issue_number}")
            current_comments = paged(f"{root}/issues/{issue_number}/comments")
            current_files = paged(f"{root}/pulls/{number}/files")
            current_open = live_open_issue_references(root)
            safe, why = eligibility(
                current_pr, current_issue, current_comments, current_files,
                current_open, datetime.now(timezone.utc),
            )
            if (
                not safe
                or current_pr["head"]["sha"] != pr["head"]["sha"]
                or current_pr["head"]["ref"] != pr["head"]["ref"]
                or current_pr["head"]["repo"]["full_name"] != pr["head"]["repo"]["full_name"]
                or current_pr["base"]["repo"]["full_name"] != pr["base"]["repo"]["full_name"]
            ):
                print(f"PR #{number}: fresh-state veto — {why}")
                continue
            request(f"{root}/pulls/{number}", "PATCH", {"state": "closed"})
            retired += 1
    print(f"negative-review retirement: eligible={possible} closed={retired} apply={apply}")


def self_test() -> None:
    now = datetime(2026, 10, 20, tzinfo=timezone.utc)
    head, base_head = "a" * 40, "b" * 40
    claim_time = "2026-10-10T10:00:00Z"
    terminal_time = "2026-10-10T11:00:00Z"
    report = "docs/planning/wave-2/reviews/negative-review.md"
    handoff = "docs/planning/handoffs/issue-199.md"
    fence = chr(96) * 3

    def comment(cid: int, when: str, body: str) -> dict[str, Any]:
        return {"id": cid, "created_at": when, "updated_at": when,
                "author_association": "OWNER", "user": {"login": OWNER_LOGIN}, "body": body}

    claim = comment(1, claim_time, f"""{fence}yaml
protocol: planning-v1
schema: 3
kind: CLAIM
issue: 199
branch: planning/issue-199
mission_id: R-01
actor_session_id: reviewer-1
state: IN_PROGRESS
previous_ownership_comment_id: null
base_sha: {base_head}
observed_head_sha: {base_head}
{fence}""")
    terminal = comment(2, terminal_time, f"""{fence}yaml
protocol: planning-v1
schema: 3
kind: REVIEW_STATUS
issue: 199
branch: planning/issue-199
mission_id: R-01
actor_session_id: reviewer-1
state: CHANGES_NEEDED
terminal: true
authority_mode: REVIEWER
ownership_generation_comment_id: 1
base_sha: {base_head}
work_sha: {head}
head_sha: {head}
pr_number: 200
pr_head_sha: {head}
pr_draft: true
required_next_route: MATERIALIZE_FIX
artifact_paths:
  - {report}
  - {handoff}
{fence}""")
    pr = {"number": 200, "title": "[PLAN-v1][#199] Required negative review",
          "state": "open", "draft": True, "merged_at": None,
          "head": {"sha": head, "ref": "planning/issue-199",
                   "repo": {"full_name": REPO}},
          "base": {"ref": "main", "repo": {"full_name": REPO}},
          "user": {"login": OWNER_LOGIN}}
    issue = {"number": 199, "state": "closed", "state_reason": "completed",
             "user": {"login": OWNER_LOGIN}, "title": "[PLAN-v1][REVIEW-199] Challenge",
             "body": "## Mission ID\nR-01\n\n## Mandatory independent review\n"
                     "Produce " + report + " and " + handoff + "."}
    files = [{"filename": report, "status": "added", "sha": "c" * 40},
             {"filename": handoff, "status": "added", "sha": "d" * 40}]

    def ok(p=pr, c=None, f=None, opened=None, t=now, rev_issue=issue) -> bool:
        return eligibility(
            p, rev_issue, [claim, terminal] if c is None else c,
            files if f is None else f, [] if opened is None else opened, t,
        )[0]

    assert ok(), eligibility(pr, issue, [claim, terminal], files, [], now)

    # B01: same SHA/title/login, wrong actual GitHub PR head or fork.
    assert not ok(p={**pr, "head": {**pr["head"], "ref": "planning/issue-777"}})
    assert not ok(p={**pr, "head": {**pr["head"], "repo": {"full_name": "vokerg/other-fork"}}})
    assert not ok(p={**pr, "base": {**pr["base"], "repo": {"full_name": "vokerg/other-fork"}}})
    assert not ok(p={**pr, "head": {**pr["head"], "repo": None}})
    assert not ok(p={**pr, "base": {"ref": "main"}})
    assert not ok(rev_issue={**issue, "body": issue["body"].replace(
        "## Mission ID\nR-01", "## Mission ID\nR-02")})

    # M02: self-consistent terminal/file rename cannot override review contract.
    bad_report = "docs/planning/wave-2/reviews/unrelated-review.md"
    changed_terminal = {**terminal, "body": terminal["body"].replace(report, bad_report)}
    changed_files = [{**files[0], "filename": bad_report}, files[1]]
    assert not ok(c=[claim, changed_terminal], f=changed_files)
    assert not ok(rev_issue={**issue, "body": "## Mission ID\nR-01\n"
                           "## Independent review\nNo exact report path"})
    assert not ok(rev_issue={**issue, "body": issue["body"] +
                           "\nAlso docs/planning/wave-2/reviews/other-review.md"})

    # M01: a live active issue's comment-only reference is a veto.
    active = {"number": 300, "state": "open", "title": "Active remediation",
              "body": "Review still in progress", "comments_coverage_complete": True,
              "live_comments": [{"id": 1, "body": "Do not retire reviewer PR #200"}]}
    assert not ok(opened=[active])
    assert not ok(opened=[{**active, "comments_coverage_complete": False,
                            "live_comments": [{"id": 1, "body": "No ref"}]}])
    assert not ok(opened=[{**active, "live_comments": None}])

    # FSR-1689-M01: independent review's direct web/API URL-only bypass.
    clean = {**active, "body": "No numeric reference",
             "live_comments": [{"id": 1, "body": "No reference"}]}
    web = f"https://github.com/{REPO}/pull/200"
    api = f"https://api.github.com/repos/{REPO}/pulls/200"
    assert not ok(opened=[{**clean, "live_comments": [
        {"id": 1, "body": f"Retain {web}"}]}])
    assert not ok(opened=[{**clean, "body": f"Needs {web}/files"}])
    assert not ok(opened=[{**clean, "body": f"Needs {web}?tab=files#discussion"}])
    assert not ok(opened=[{**clean, "live_comments": [
        {"id": 1, "body": f"Retain {api}"}]}])
    assert not ok(opened=[{**clean, "body": f"Retain {api}/files"}])
    assert not ok(opened=[{**clean, "title": "Please preserve #200"}])
    # FSR-1697-M01: first-party HTTPS :443 and .diff/.patch are live references.
    # Exercise issue title, body AND fully loaded comment as separate consumers.
    web_port = f"https://github.com:443/{REPO}/pull/200"
    api_port = f"https://api.github.com:443/repos/{REPO}/pulls/200"
    variants = (
        web_port, api_port, web + ".diff", web + ".patch",
        api + ".diff", api + ".patch",
        web_port + ".diff", web_port + ".patch",
        api_port + ".diff", api_port + ".patch",
        web_port + "/files?diff=split#discussion",
        f"https://github.com/{REPO}/%70ull/%32%30%30",
        f"https://api.github.com:443/repos/{REPO}/pulls/%32%30%30.patch",
        f"https://github.com./{REPO}/pull/200",
        f"https://github.com:invalid/{REPO}/pull/200",
        f"https://github.com:444/{REPO}/pull/200",
    )
    for variant in variants:
        assert not ok(opened=[{**clean, "title": "Keep " + variant}]), variant
        assert not ok(opened=[{**clean, "body": "Keep " + variant}]), variant
        assert not ok(opened=[{**clean, "live_comments": [
            {"id": 1, "body": "Keep " + variant}]}]), variant

    # Non-reference positives: no substring numeric, foreign repo or host.
    assert ok(opened=[clean])
    assert ok(opened=[{**clean, "body": f"https://github.com/{REPO}/pull/2000"}])
    assert ok(opened=[{**clean, "body": f"https://github.com/{REPO}/issues/200"}])
    assert ok(opened=[{**clean, "body": "https://github.com/vokerg/other/pull/200"}])
    assert ok(opened=[{**clean, "body": f"https://github.com.evil.test/{REPO}/pull/200"}])
    assert ok(opened=[{**clean, "body": f"https://api.github.com/repos/{REPO}/pulls/2000"}])
    assert ok(opened=[{**clean, "body": f"https://github.com:443/{REPO}/pull/2000"}])
    assert ok(opened=[{**clean, "body": f"https://github.com:443/{REPO}/pull/200abc"}])
    assert ok(opened=[{**clean, "body": f"https://github.com/{REPO}/pull/200.diffuse"}])
    assert ok(opened=[{**clean, "body": f"https://api.github.com:443/repos/{REPO}/pulls/2000"}])
    assert ok(opened=[{**clean, "body": f"https://github.com:443/{REPO}/issues/200"}])
    assert ok(opened=[{**clean, "body": f"https://github.com.evil.test:443/{REPO}/pull/200.patch"}])
    assert ok(opened=[{**clean, "body": f"https://api.github.com:443/repos/vokerg/other/pulls/200.patch"}])


    # Exercise the LIVE snapshot reader, not only the pure eligibility gate.
    original_paged = paged
    live = {"number": 300, "state": "open", "title": "Active remediation",
            "body": "No direct link", "comments": 1}
    live_comment = {"id": 50, "created_at": "2026-10-10T12:00:00Z",
                    "body": "This open successor needs review PR #200"}
    try:
        def one_page(path: str) -> list[dict[str, Any]]:
            if path.endswith("/issues?state=open"):
                return [live]
            if path.endswith("/issues/300/comments"):
                return [live_comment]
            raise AssertionError("unexpected snapshot API path")
        globals()["paged"] = one_page
        complete = live_open_issue_references(f"/repos/{REPO}")
        assert len(complete) == 1 and complete[0]["comments_coverage_complete"]
        assert not ok(opened=complete)

        # A changed server comment count invalidates scan before any close.
        globals()["paged"] = lambda path: [live] if path.endswith(
            "/issues?state=open") else []
        try:
            live_open_issue_references(f"/repos/{REPO}")
            assert False, "partial comment coverage incorrectly accepted"
        except RuntimeError:
            pass
    finally:
        globals()["paged"] = original_paged


    # Same live snapshot reader must preserve web links supplied only by the
    # server's comment endpoint, even when the issue body contains none.
    try:
        globals()["paged"] = lambda path: [live] if path.endswith(
            "/issues?state=open") else [{**live_comment, "body": f"Keep {web}/files"}]
        complete_url = live_open_issue_references(f"/repos/{REPO}")
        assert not ok(opened=complete_url)
    finally:
        globals()["paged"] = original_paged

    # Exercise execute(apply=True) with a changing live comment between its
    # first pass and the immediate pre-PATCH recheck. Never send a real PATCH.
    original_request = request
    original_datetime = datetime
    scans = 0
    patches: list[str] = []
    class TestClock(datetime):
        @classmethod
        def now(cls, tz=None):
            return now

    def racing_paged(path: str) -> list[dict[str, Any]]:
        nonlocal scans
        if path.endswith("/pulls?state=open"):
            return [pr]
        if path.endswith("/issues?state=open"):
            scans += 1
            return [live]
        if path.endswith("/issues/300/comments"):
            return [{**live_comment, "body": "No link" if scans == 1 else f"Keep {web_port}.diff"}]
        if path.endswith("/issues/199/comments"):
            return [claim, terminal]
        if path.endswith("/pulls/200/files"):
            return files
        raise AssertionError(f"unexpected mocked page {path}")

    def racing_request(path: str, method="GET", data=None) -> Any:
        if method == "PATCH":
            patches.append(path)
            return {"state": "closed"}
        if path.endswith("/issues/199"):
            return issue
        if path.endswith("/pulls/200"):
            return pr
        raise AssertionError(f"unexpected mocked request {method} {path}")

    try:
        globals()["paged"] = racing_paged
        globals()["request"] = racing_request
        globals()["datetime"] = TestClock
        execute(apply=True)
        assert scans == 2 and not patches, "active URL added before PATCH escaped veto"
    finally:
        globals()["paged"] = original_paged
        globals()["request"] = original_request
        globals()["datetime"] = original_datetime

    assert ok(opened=[{**active, "live_comments": [
        {"id": 1, "body": "No reference to the reviewer PR"}]}])

    assert not ok(p=dict(pr, draft=False))
    assert not ok(p=dict(pr, merged_at="2026-10-11T00:00:00Z"))
    assert not ok(p=dict(pr, head={"sha": "e" * 40}))
    assert not ok(p=dict(pr, state="closed"))
    assert not ok(p=dict(pr, base={"ref": "other"}))
    assert not ok(rev_issue=dict(issue, state="open"))
    assert not ok(rev_issue=dict(issue, user={"login": "outsider"}))
    assert not ok(opened=[{"title": "Active successor", "body": "needs PR #200 OPEN/DRAFT"}])
    assert not ok(t=datetime(2026, 10, 11, tzinfo=timezone.utc))
    assert not ok(f=[{"filename": "game/main.gd", "status": "added", "sha": "c"*40}, files[1]])
    assert not ok(f=[dict(files[0], filename="docs/planning/wave-2/reviews/unrelated.md"), files[1]])
    assert not ok(f=[files[0], dict(files[1], filename="docs/planning/handoffs/issue-777.md")])
    assert not ok(f=[dict(files[0], sha="bogus"), files[1]])
    assert not ok(f=[dict(files[0], status="modified"), files[1]])
    assert not ok(c=[claim, dict(terminal, updated_at="2026-10-10T11:01:00Z")])
    assert not ok(c=[claim, dict(terminal, author_association="NONE")])
    assert not ok(c=[dict(claim, body=claim["body"].replace("reviewer-1", "other")), terminal])
    assert not ok(c=[dict(claim, body=claim["body"].replace("kind: CLAIM", "kind: RESUME")), terminal])
    assert not ok(c=[dict(claim, body=claim["body"].replace("base_sha:", "forged_sha:")), terminal])
    assert not ok(c=[dict(claim, body=claim["body"].replace("planning/issue-199", "planning/issue-777")), terminal])
    assert not ok(c=[dict(claim, body=claim["body"].replace("previous_ownership_comment_id: null", "previous_ownership_comment_id: 999")), terminal])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("CHANGES_NEEDED", "REVIEW_READY"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("pr_number: 200", "pr_number: 201"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("kind: REVIEW_STATUS", "kind: STATUS"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("terminal: true", "terminal: false"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("pr_draft: true", "pr_draft: false"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("state: CHANGES_NEEDED", "state: CHANGES_NEEDED\nstate: CHANGES_NEEDED"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("protocol: planning-v1", "protocol: *shadow"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"].replace("protocol: planning-v1", "protocol: !!str planning-v1"))])
    assert not ok(c=[claim, dict(terminal, body=terminal["body"] + f"\n{fence}yaml\nkind: REVIEW_STATUS\n{fence}")])
    assert not ok(c=[claim, dict(terminal, created_at="2026-10-10T17:00:00Z", updated_at="2026-10-10T17:00:00Z")])
    # Genuine negative reviewer cannot be superseded by a subsequent status.
    newer = comment(3, "2026-10-10T11:05:00Z", terminal["body"].replace("CHANGES_NEEDED", "REVIEW_READY"))
    assert not ok(c=[claim, terminal, newer])
    # Even malformed or edited attempted later authority fails closed.
    assert not ok(c=[claim, terminal, dict(newer, updated_at="2026-10-10T11:06:00Z")])
    # Any additional competing owner or PROGRESS record is outside the
    # proven safe subset: no guessed first-winner or renewal authority.
    extra_claim = comment(4, "2026-10-10T10:05:00Z", claim["body"])
    assert not ok(c=[claim, extra_claim, terminal])
    extra_progress = comment(5, "2026-10-10T10:10:00Z", claim["body"].replace("kind: CLAIM", "kind: PROGRESS"))
    assert not ok(c=[claim, extra_progress, terminal])
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
