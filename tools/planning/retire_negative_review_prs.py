#!/usr/bin/env python3
"""Conservative, independent retirement of *proven rejected review-only* PRs.

A closed PR remains an immutable GitHub review/diff/provenance reference.
This tool never merges, promotes, deletes branches, or changes source PRs.
Default behavior is dry-run. Only a separately reviewed main workflow can apply.
"""
from __future__ import annotations

import argparse
import html
from datetime import datetime, timedelta, timezone
import json
import os
import re
import string
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



# FSR-1776-M01: CommonMark permits one line ending after an inline-link opener
# or a reference-definition colon. Do not broaden this to arbitrary blank
# paragraphs: consume at most one CRLF/LF and surrounding horizontal space.
# FSR-1776-M02: parenthesized path segments remain URL characters, including
# balanced (z)/.. which browsers normalize away before matching PR routes.

PR_URL = re.compile(
    r"(?<![A-Za-z0-9+.:/-])(?:https?:)?//[^\s<>\[\]{}\"'\x60]+",
    re.IGNORECASE,
)



# A GitHub issue is rendered at /OWNER/REPO/issues/N. CommonMark relative
# link destinations and reference definitions use that URL as the browser
# resolution base; a live reference need not contain an absolute host or #N.
# Scan only Markdown target slots so foreign full URLs with matching path text
# are not accidentally interpreted as root-relative GitHub links.
RELATIVE_MD_LINK_TARGET = re.compile(
    r"(?:\]\([ \t]*(?:\r?\n[ \t]*)?|(?m:^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*(?:\r?\n[ \t]*)?))"
    r"(?:<([^<>\n]+)>|([^\s<>]+))"
)


# FSR-1752-M01: only exact GitHub decimal PR aliases; validate the
# first-party origin, repo and route before applying this normalization.
def pr_segment_matches(segment: str, number: int) -> bool:
    for suffix in (".diff", ".patch"):
        if segment.endswith(suffix):
            segment = segment[:-len(suffix)]
            break
    if re.fullmatch(r"\+?0*[1-9][0-9]*", segment) is None:
        return False
    return segment.lstrip("+").lstrip("0") == str(number)


def unsafe_encoded_pr_path(path: str) -> bool:
    """Malformed/double/encoded-separator paths cannot prove non-reference."""
    return (re.search(r"%(?![0-9a-fA-F]{2})", path) is not None
            or re.search(r"%(?:2f|5c|25)", path, re.IGNORECASE) is not None)


def browser_path_segments(path: str) -> list[str]:
    """Apply browser URL dot-segment semantics, including percent-encoded dots.

    Python urljoin does not recognize %2e as a dot segment. WHATWG browser
    navigation does; otherwise an active relative link can secretly resolve
    into the live /pull/<number> route after our prefix check.
    Unsafe encoded separators/percent and malformed escapes are rejected
    separately by unsafe_encoded_pr_path before calling this function.
    """
    result: list[str] = []
    for segment in path.split("/"):
        if not segment:
            continue
        decoded = urllib.parse.unquote(segment).casefold()
        if decoded == ".":
            continue
        if decoded == "..":
            if result:
                result.pop()
            continue
        result.append(decoded)
    return result


def references_pr(text: str, number: int) -> bool:
    """Fail closed on first-party PR URL variants in active issues/comments.

    A first-party PR reference may use HTTPS, HTTP (redirects to HTTPS),
    browser-resolvable protocol-relative // links, explicit standard ports,
    .diff/.patch endpoints, encoded paths or PR subresources. Parse host
    and port separately. Unknown first-party authority fails closed.
    """
    # FSR-1724-M01: CommonMark resolves HTML named and numeric character
    # references in clickable link destinations, including host, path and ID.
    # Decode once before strict URL parsing and numeric boundary checks.
    # FSR-1729-M01: CommonMark backslash escapes resolve ASCII punctuation
    # inside clickable link destinations (scheme colon, host dots, query,
    # path suffix, slash). Decode entities first, then escaped punctuation.
    # Retain the strict first-party host/repo/number parser below.
    # Keep raw CommonMark escapes for inline-destination delimiter matching.
    # Decoding \) first makes literal path punctuation masquerade as a
    # Markdown closing parenthesis and can hide a still-linked review PR.
    raw_markdown = html.unescape(text)
    text = re.sub(r"\\([" + re.escape(string.punctuation) + r"])", r"\1",
                  raw_markdown)
    if re.search(rf"(?<![0-9])#{number}(?![0-9])", text):
        return True
    if not isinstance(REPO, str) or REPO.count("/") != 1:
        return True
    owner, repository = REPO.split("/")
    if not owner or not repository:
        return True
    # CommonMark escaped punctuation and HTML entities were normalized above;
    # continue with exact first-party host, repo, and PR-number boundaries.
    for match in PR_URL.finditer(text):
        # Markdown table pipes delimit cells, not GitHub PR URL paths.
        # Split before parsing so a following cell cannot shadow the PR ID.
        link = match.group(0).split("|", 1)[0].rstrip(".,;!:").rstrip("*_")
        # FSR-1776-M02: a balanced parenthesized segment is URL path data,
        # while extra terminal ')' closes a Markdown inline destination.
        # Preserve internal pairs so WHATWG dot processing can remove (z)/..
        # without falsely consuming a live /pull/<number> reference.
        unmatched_closers = max(0, link.count(")") - link.count("("))
        while unmatched_closers and link.endswith(")"):
            link = link[:-1]
            unmatched_closers -= 1
        try:
            # FSR-1772-M02: WHATWG special-scheme authorities permit three or
            # more slashes after https:/http:; Python urlsplit misreads these
            # as hostless paths and can miss a live first-party PR reference.
            # Repair the scheme delimiter before asking for authority identity;
            # a foreign host remains foreign, never rebased to GitHub.
            browser_link = re.sub(r"(?i)^(https?):/{3,}", r"\1://", link)
            url = urllib.parse.urlsplit(browser_link)
            # FSR-1772-M01: WHATWG browser IDNA maps U+3002/U+FF0E/U+FF61
            # and their percent-escaped UTF-8 spellings to DNS dots. Unquote
            # the complete UTF-8 authority host then apply IDNA before exact
            # first-party comparison. Unreadable encodings fail closed.
            host_text = urllib.parse.unquote_to_bytes(url.hostname or "").decode("utf-8", "strict")
            hostname = host_text.encode("idna").decode("ascii").casefold().rstrip(".")
        except (ValueError, UnicodeError):
            return True
        if hostname not in {"github.com", "api.github.com"}:
            continue
        try:
            port = url.port
        except ValueError:
            return True
        scheme = url.scheme.lower()
        allowed_ports = ((None, 80, 443) if scheme in ("http", "")
                         else (None, 443))
        if (
            scheme not in ("http", "https", "")
            or url.username is not None or url.password is not None
            or port not in allowed_ports
        ):
            # First-party but malformed/unexpected authority: veto, never retire.
            return True
        if unsafe_encoded_pr_path(url.path):
            return True
        segments = browser_path_segments(url.path)
        prefix = ([owner, repository, "pull"] if hostname == "github.com"
                  else ["repos", owner, repository, "pulls"])
        prefix = [item.casefold() for item in prefix]
        if len(segments) <= len(prefix) or segments[:len(prefix)] != prefix:
            continue
        # Markdown emphasis abutting a PR number is presentation, not part
        # of the numeric GitHub path. Never strip letters or digits.
        pr_segment = segments[len(prefix)].rstrip("*_")
        if pr_segment_matches(pr_segment, number):
            return True

    # FSR-1743-M01: GitHub-flavored Markdown in issue body/comments can link
    # to this same PR using a root-relative or repository-relative destination:
    # [review](/vokerg/everfield/pull/200), [review](../pull/200).
    # These are clickable even though PR_URL (correctly) requires // authority.
    # Use a fixed issue-page path (the numeric issue ID is immaterial to
    # relative resolution), validate the resolved *first-party* repo/path and
    # exact PR segment; never use substring numeric matching.
    # Browser navigation resolves relative links against the *directory* of
    # /OWNER/REPO/issues/1. Preserve raw and escaped dot segments together:
    # urllib.parse.urljoin first collapses literal '..' but leaves '%2e%2e'
    # untouched, which is NOT equivalent to the ordered WHATWG algorithm.
    for relative in RELATIVE_MD_LINK_TARGET.finditer(raw_markdown):
        destination = relative.group(1) or relative.group(2) or ""
        # FSR-1782-M01: CommonMark accepts balanced parentheses in unquoted
        # relative link destinations. The closing delimiter is the FIRST
        # unmatched ')' (not the first ')'); internal (z)/.. is URL path data.
        # Reference definitions do not use the inline ')' delimiter.
        if relative.group(2) is not None and relative.group(0).startswith("]("):
            depth = 0
            offset = 0
            while offset < len(destination):
                ch = destination[offset]
                # FSR-1786-M01: escaped parentheses are literal URL data,
                # not CommonMark depth delimiters. Decode only AFTER the
                # actual unescaped closing ')' has been located.
                if (ch == "\\" and offset + 1 < len(destination)
                        and destination[offset + 1] in string.punctuation):
                    offset += 2
                    continue
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    if depth == 0:
                        destination = destination[:offset]
                        break
                    depth -= 1
                offset += 1
        destination = re.sub(
            r"\\([" + re.escape(string.punctuation) + r"])", r"\1", destination
        )
        if not destination.startswith(("/", "./", "../")):
            continue
        # Scheme-relative authorities belong to the absolute URL reader above.
        # In particular, never reinterpret //evil.test/OWNER/REPO as local.
        if destination.startswith("//"):
            continue
        if unsafe_encoded_pr_path(destination):
            return True
        try:
            target = urllib.parse.urlsplit(destination)
            if target.scheme or target.netloc:
                continue
            raw_path = target.path
            path = (raw_path if raw_path.startswith("/")
                    else f"/{owner}/{repository}/issues/{raw_path}")
            path_parts = browser_path_segments(path)
        except (ValueError, UnicodeError):
            # Ambiguous origin/path cannot certify non-reference.
            return True
        if path_parts[:3] != [owner.casefold(), repository.casefold(), "pull"]:
            continue
        if len(path_parts) < 4:
            continue
        pr_path_segment = path_parts[3]
        if pr_segment_matches(pr_path_segment, number):
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


    # FSR-1705-M01: direct first-party HTTP-upgraded and browser-resolvable
    # protocol-relative URLs are equivalent links to the same review PR.
    http_web = f"http://github.com/{REPO}/pull/200"
    http_api = f"http://api.github.com/repos/{REPO}/pulls/200"
    relative_web = f"//github.com/{REPO}/pull/200"
    relative_api = f"//api.github.com/repos/{REPO}/pulls/200"
    upgraded_variants = (
        http_web, http_api, relative_web, relative_api,
        http_web + "/files?diff=split#discussion",
        http_api + ".patch", relative_web + ".diff",
        f"http://github.com:80/{REPO}/pull/200",
        f"http://api.github.com:80/repos/{REPO}/pulls/200.patch",
        f"//github.com:443/{REPO}/pull/200/files",
        f"http://github.com./{REPO}/pull/200",
        f"http://github.com/{REPO}/%70ull/%32%30%30",
        f"[review]({relative_web})",
    )
    for variant in upgraded_variants:
        assert not ok(opened=[{**clean, "title": "Keep " + variant}]), variant
        assert not ok(opened=[{**clean, "body": "Keep " + variant}]), variant
        assert not ok(opened=[{**clean, "live_comments": [
            {"id": 1, "body": "Keep " + variant}]}]), variant
    # FSR-1710-M01: Markdown emphasis and table boundaries in any active
    # title, body or loaded comment must veto retirement.
    markdown_variants = (
        f"**{web}**", f"*{web}*", f"__{web}__", f"_{web}_",
        f"**{api}**", f"*{http_web}*", f"__{http_api}__",
        f"**{relative_web}**", f"__{relative_api}__",
        f"**{web}.diff**", f"__{api}.patch__",
        f"{web}|", f"{web}|Next", f"{api}|Next column",
        f"{http_web}|", f"{relative_api}|More",
        f"| {web} |", f"|{relative_web}|Next",
        f"**{web_port}.patch**", f"__{api_port}.diff__",
        f"**{web}**|following", f"{web}__|following",
    )
    for variant in markdown_variants:
        assert references_pr("Keep " + variant, 200), variant
        assert not ok(opened=[{**clean, "title": "Keep " + variant}]), variant
        assert not ok(opened=[{**clean, "body": "Keep " + variant}]), variant
        assert not ok(opened=[{**clean, "live_comments": [
            {"id": 1, "body": "Keep " + variant}]}]), variant

    # FSR-1717-M01: escaped CommonMark link destination slashes must not
    # bypass first-pass or second pre-PATCH open-issue reference vetoes.
    escaped_variants = (
        r"[review](https:\/\/github.com/vokerg/everfield/pull/200)",
        r"[review](https:\/\/github.com\/vokerg\/everfield\/pull\/200)",
        r"[review](https://github.com\/vokerg\/everfield\/pull\/200)",
        r"[review](https://github.com/vokerg/everfield/pull\/200)",
        r"[review](http:\/\/github.com/vokerg/everfield/pull/200)",
        r"[review](\/\/github.com/vokerg/everfield/pull/200)",
        r"[review](https:\/\/api.github.com/repos/vokerg/everfield/pulls/200)",
    )
    for variant in escaped_variants:
        assert references_pr(variant, 200), variant
        for location in (
            {**clean, "title": "Keep " + variant},
            {**clean, "body": "Keep " + variant},
            {**clean, "live_comments": [{"id": 1, "body": "Keep " + variant}]},
        ):
            assert not ok(opened=[location]), variant
    # FSR-1724-M01: CommonMark decodes named, decimal and hex entities.
    # Exercise actual predicate and eligibility's title/body/loaded comments.
    html_variants = (
        "[review](https://github&#46;com/vokerg/everfield/pull/200)",
        "[review](https://github.com/vokerg/everfield/pull&#47;200)",
        "[review](https&#58;&#47;&#47;github.com/vokerg/everfield/pull/200)",
        "[review](https://github.com/vokerg/everfield/pull/20&#48;)",
        "[review](https://github.com/vokerg/everfield/pull/200&#63;tab=files)",
        "[review](https://github&#x2e;com/vokerg/everfield/pull/200)",
        "[review](https&colon;&sol;&sol;github&period;com/vokerg/everfield/pull/200)",
        "[review](https://github.com/vokerg/everfield/pull&sol;200)",
        "[review](https://api.github&#46;com/repos/vokerg/everfield/pulls/200)",
        "[review](http&#58;&#47;&#47;github.com:80/vokerg/everfield/pull/200)",
        "[review](//github&#46;com:443/vokerg/everfield/pull/200.diff)",
        "[review](https://github.com/vokerg/everfield/pull/200&#46;patch)",
        "[review](https://github.com/vokerg/everfield/pull/20&#x30;?tab=files)",
        r"[review](https:\/\/github&#46;com\/vokerg\/everfield\/pull\/200)",
        r"[review](https:\/\/api.github&period;com\/repos\/vokerg\/everfield\/pulls\/200)",
        "**[review](https://github&#46;com/vokerg/everfield/pull/200)**",
        "| [review](https://github.com/vokerg/everfield/pull&#47;200) | other |",
    )
    for variant in html_variants:
        assert references_pr(variant, 200), variant
        for location in (
            {**clean, "title": "Keep " + variant},
            {**clean, "body": "Keep " + variant},
            {**clean, "live_comments": [{"id": 1, "body": "Keep " + variant}]},
        ):
            assert not ok(opened=[location]), variant

    # FSR-1729-M01: CommonMark escapes ASCII punctuation in rendered link
    # destinations, not only slashes. Test the production gate with active
    # open-issue title, body and fully loaded comment references.
    commonmark_escaped_variants = (
        r"[review](https\://github.com/vokerg/everfield/pull/200)",
        r"[review](https://github\.com/vokerg/everfield/pull/200)",
        r"[review](https://api.github\.com/repos/vokerg/everfield/pulls/200)",
        r"[review](https://github.com/vokerg/everfield/pull/200\.diff)",
        r"[review](https://github.com/vokerg/everfield/pull/200\?tab=files)",
        r"[review](https://github.com:443/vokerg/everfield/pull/200\.patch)",
        r"[review](http\://github.com/vokerg/everfield/pull/200)",
        r"[review](//api.github\.com/repos/vokerg/everfield/pulls/200)",
        r"[review](https\://github&#46;com/vokerg/everfield/pull/200\.diff)",
        r"[review](https&#58;//github\.com/vokerg/everfield/pull/200\?tab=files)",
        r"[review](https://api.github&#46;com/repos/vokerg/everfield/pulls/200\.patch)",
    )
    for variant in commonmark_escaped_variants:
        assert references_pr(variant, 200), variant
        for location in (
            {**clean, "title": "Keep " + variant},
            {**clean, "body": "Keep " + variant},
            {**clean, "live_comments": [{"id": 1, "body": "Keep " + variant}]},
        ):
            assert not ok(opened=[location]), variant

    # FSR-1743-M01: actual GitHub issue pages resolve these Markdown
    # destinations to first-party PR #200 without requiring an absolute URL.
    # Run title, body and fully paged comment vetoes through eligibility.
    relative_positive_variants = (
        "[review](/vokerg/everfield/pull/200)",
        "[review](../pull/200)",
        "[review](../../everfield/pull/200)",
        "[review](../pull/200.diff)",
        "[review](../pull/200#issuecomment-123)",
        "[review](../pull/200?tab=files)",
        "[review](<../pull/200>)",
        "[review](../pull/%32%30%30)",
        "[review](../pull/20&#48;)",
        r"[review](..\/pull\/200)",
        "[ref]: ../pull/200\n\n[review][ref]",
        "[ref]: /vokerg/everfield/pull/200.diff\n\n[review][ref]",
    )
    for variant in relative_positive_variants:
        assert references_pr(variant, 200), variant
        # A CommonMark reference definition must begin on its own line, not
        # after decorative prose ("Keep "), to be a real resolved link.
        active_text = variant if variant.startswith("[ref]:") else "Keep " + variant
        for location in (
            {**clean, "title": active_text},
            {**clean, "body": active_text},
            {**clean, "live_comments": [{"id": 1, "body": active_text}]},
        ):
            assert not ok(opened=[location]), variant

    # FSR-1752-M01: exact first-party numeric aliases in title/body/comments.
    alias_positive_variants = (
        f"https://github.com/{REPO}/pull/0200",
        f"https://github.com/{REPO}/issues/%2e%2e/pull/0200",
        f"https://github.com/vokerg/other/%2e%2e/everfield/pull/+0200",
        f"https://api.github.com/repos/{REPO}/issues/%2e%2e/pulls/0200",
        "[review](../issues/%2e%2e/pull/+0200)",
        "[review](../issues/.%2e/pull/0200)",
        "[review](../issues/%2E./pull/0200)",
        "[review](/vokerg/everfield/issues/%2E%2E/pull/0200)",
        "[ref]: ../issues/%2E./pull/0200\n\n[review][ref]",
        f"https://github.com/{REPO}/pull/+200",
        f"https://github.com/{REPO}/pull/+0200.diff",
        f"https://github.com/{REPO}/pull/000200.patch/files",
        f"https://api.github.com/repos/{REPO}/pulls/0200",
        f"https://api.github.com/repos/{REPO}/pulls/+200",
        f"https://api.github.com/repos/{REPO}/pulls/+0200.patch",
        f"https://api.github.com/repos/{REPO}/pulls/000200/files",
        "[review](/vokerg/everfield/pull/0200)",
        "[review](../pull/+200)",
        "[review](../pull/+0200.diff)",
        "[review](<../pull/000200.patch>)",
        "[ref]: ../pull/+0200\n\n[review][ref]",
        "[ref]: /vokerg/everfield/pull/0200.diff\n\n[review][ref]",
        f"[review](https://github&#46;com/{REPO}/pull/+0200)",
        "[review](../pull/%2B0200)",
        "[review](../pull/0&#50;00)",
        r"[review](https\://github\.com/vokerg/everfield/pull/+0200)",
    )
    for variant in alias_positive_variants:
        assert references_pr(variant, 200), variant
        active_text = variant if variant.startswith("[ref]:") else "Keep " + variant
        for location in (
            {**clean, "title": active_text},
            {**clean, "body": active_text},
            {**clean, "live_comments": [{"id": 1, "body": active_text}]},
        ):
            assert not ok(opened=[location]), variant
    alias_negative_variants = (
        f"https://github.com/{REPO}/pull/02000",
        f"https://github.com/vokerg/other/issues/%2e%2e/pull/+0200",
        f"https://github.com/{REPO}/issues/%2e%2e/pull/+0201",
        "[review](../issues/%2e%2e/pull/+0201)",
        "[review](//evil.invalid/vokerg/everfield/issues/%2e%2e/pull/+0200)",
        f"https://github.com/{REPO}/docs/help%2efile",
        f"https://github.com/{REPO}/pull/+201",
        f"https://github.com/{REPO}/pull/0200abc",
        f"https://github.com/{REPO}/pull/00+200",
        f"https://github.com/{REPO}/pull/0200.diffuse",
        f"https://api.github.com/repos/{REPO}/pulls/+2000",
        "https://github.com.evil.test/vokerg/everfield/pull/+200",
        "https://github.com/vokerg/other/pull/+0200",
        "[review](../issues/+200)",
        "[review](/vokerg/other/pull/0200)",
        "[review](../pull/+200tail)",
        "[review](../pull/0201.patch)",
    )
    for variant in alias_negative_variants:
        assert not references_pr(variant, 200), variant
        assert ok(opened=[{**clean, "body": variant}]), variant
    # FSR-1768-M01: WHATWG processes raw '..' and percent-encoded '..'
    # in a single ordered stream. Python urljoin pre-normalization is unsafe.
    # Expected actual browser route for every positive below is
    # https://github.com/vokerg/everfield/pull/<PR-200-alias>.
    # Independently cross-checked against Node 22 WHATWG URL, not urljoin.
    ordered_dot_positive_variants = (
        "[review](../issues/tmp/%2e%2e/../pull/+0200)",
        "[review](../issues/tmp/.%2E/../pull/200)",
        "[review](../issues/tmp/%2E./../pull/0200)",
        "[review](../issues/tmp/%2e%2e/../pull/200.patch)",
        "[review](<../issues/tmp/%2E%2E/../pull/+0200.diff>)",
        "[ref]: ../issues/tmp/%2e%2e/../pull/+0200\n\n[review][ref]",
        "[review](../issues/tmp/deep/%2e%2e/%2E%2e/../pull/200)",
        "[review](/vokerg/everfield/issues/tmp/%2e%2e/../pull/200)",
    )
    for variant in ordered_dot_positive_variants:
        assert references_pr(variant, 200), variant
        active_text = variant if variant.startswith("[ref]:") else "Keep " + variant
        for location in (
            {**clean, "title": active_text},
            {**clean, "body": active_text},
            {**clean, "live_comments": [{"id": 1, "body": active_text}]},
        ):
            assert not ok(opened=[location]), variant

    ordered_dot_negative_variants = (
        "[review](../issues/tmp/%2e%2e/../pull/+0201)",
        "[review](../issues/tmp/%2e%2e/../issues/200)",
        "[review](/vokerg/other/issues/tmp/%2e%2e/../pull/200)",
        "[review](//evil.test/vokerg/everfield/issues/tmp/%2e%2e/../pull/200)",
        "[review](../issues/tmp/help%2efile/../pull/200)",
    )
    for variant in ordered_dot_negative_variants:
        assert not references_pr(variant, 200), variant
        assert ok(opened=[{**clean, "body": variant}]), variant

    # FSR-1772-M01/M02: independent security review of frozen #1771 found
    # valid browser first-party absolute links with IDNA dot-equivalent hosts
    # and special-scheme extra slash separators. The first/fresh issue scans
    # must both retain each PR even when only one live link is present.
    browser_authority_positive_variants = (
        "[review](https://github。com/vokerg/everfield/pull/200)",
        "[review](https://github．com/vokerg/everfield/pull/0200)",
        "[review](https://github｡com/vokerg/everfield/pull/+0200)",
        "[review](https://github%E3%80%82com/vokerg/everfield/pull/200.patch)",
        "[review](https://api.github%EF%BD%A1com/repos/vokerg/everfield/pulls/0200)",
        "[review](https://api.github%E3%80%82com/repos/vokerg/everfield/pulls/+0200.patch)",
        "[review](https:////github.com/vokerg/everfield/pull/+0200)",
        "[review](https:///github.com/vokerg/everfield/pull/0200)",
        "[review](http:////api.github.com/repos/vokerg/everfield/pulls/0200)",
        "[review](https:////github。com/vokerg/everfield/pull/200.diff)",
        "[ref]: https:////github.com/vokerg/everfield/pull/0200\n\n[review][ref]",
        "[review](<https://github．com/vokerg/everfield/pull/+0200>)",
        "https://github%E3%80%82com/vokerg/everfield/pull/+0200/files",
    )
    for variant in browser_authority_positive_variants:
        assert references_pr(variant, 200), variant
        active_text = variant if variant.startswith("[ref]:") else "Keep " + variant
        for location in (
            {**clean, "title": active_text},
            {**clean, "body": active_text},
            {**clean, "live_comments": [{"id": 1, "body": active_text}]},
        ):
            assert not ok(opened=[location]), variant

    browser_authority_negative_variants = (
        "[review](https://github。com/vokerg/other/pull/200)",
        "[review](https://github．com/vokerg/everfield/pull/+0201)",
        "[review](https://github｡com/vokerg/everfield/issues/200)",
        "[review](https://github%E3%80%82com.evil.test/vokerg/everfield/pull/200)",
        "[review](https:////evil.test/vokerg/everfield/pull/0200)",
        "[review](https:////github.com/vokerg/other/pull/200)",
        "[review](https:///github.com/vokerg/everfield/pull/2000)",
        "[review](http:////api.github.com/repos/vokerg/other/pulls/200)",
        "[review](https://github。com/vokerg/everfield/docs/help%2efile)",
    )
    for variant in browser_authority_negative_variants:
        assert not references_pr(variant, 200), variant
        assert ok(opened=[{**clean, "body": variant}]), variant


    # FSR-1776-M01/M02: the independent reviewer proved that valid CommonMark
    # multiline destinations and balanced-parenthesis dot-removal routes
    # escaped both initial and fresh active-link scans in frozen PR #1775.
    # These remain ordinary first-party targets, not ambiguous foreign links.
    multiline_parenthesis_positive_variants = (
        "[review](\n../pull/200)",
        "[review]( \n../pull/+0200)",
        "[review](\n<../pull/200>)",
        "[review](\r\n/vokerg/everfield/pull/0200)",
        "[review]:\n../pull/200\n\n[review]",
        "[review]:\n/vokerg/everfield/pull/200\n\n[review]",
        "[review](<https://github.com/(z)/../vokerg/everfield/pull/200>)",
        "[review](https://github.com/(z)/../vokerg/everfield/pull/+0200/files)",
        "[review](<https://api.github.com/(z)/../repos/vokerg/everfield/pulls/0200>)",
        "[review](<https:////github。com/(z)/../vokerg/everfield/pull/200.patch>)",
    )
    for variant in multiline_parenthesis_positive_variants:
        assert references_pr(variant, 200), variant
        for location in (
            {**clean, "title": variant},
            {**clean, "body": variant},
            {**clean, "live_comments": [{"id": 1, "body": variant}]},
        ):
            assert not ok(opened=[location]), variant

    multiline_parenthesis_negative_variants = (
        "[review](\n../pull/201)",
        "[review]:\n../issues/200\n\n[review]",
        "[review](\n/vokerg/other/pull/200)",
        "[review](<https://github.com/(z)/../vokerg/everfield/pull/201>)",
        "[review](https://github.com/(z)/../vokerg/other/pull/200)",
        "[review](<https://evil.test/(z)/../vokerg/everfield/pull/200>)",
        "[review](<https://github.com/(z)/../vokerg/everfield/issues/200>)",
    )
    for variant in multiline_parenthesis_negative_variants:
        assert not references_pr(variant, 200), variant
        assert ok(opened=[{**clean, "body": variant}]), variant

    # FSR-1782-M01: actual CommonMark/browser balanced-parenthesis relative
    # targets must protect an actively linked PR through both retirement scans.
    # A nonangle inline target terminates at its first UNMATCHED ')' only.
    balanced_relative_positive_variants = (
        "[review](../(z)/../pull/200)",
        "[review](../(z)/../pull/+0200.diff)",
        "[review](../(z)/../pull/0200.patch/files)",
        "[review](/vokerg/everfield/(z)/../pull/200)",
        "[review](/vokerg/everfield/(z)/../pull/+0200)",
        "[review](../(x(y))/../pull/200)",
        "[review](../(z)/../pull/200)following",
        "[review](\n../(z)/../pull/200)",
        "[review](\r\n/vokerg/everfield/(z)/../pull/0200)",
        "[review]: ../(z)/../pull/200\n\n[review]",
        "[review]: /vokerg/everfield/(z)/../pull/+0200.diff\r\n\r\n[review]",
        "[review](<../(z)/../pull/200>)",
    )
    for variant in balanced_relative_positive_variants:
        assert references_pr(variant, 200), variant
        for location in (
            {**clean, "title": variant},
            {**clean, "body": variant},
            {**clean, "live_comments": [{"id": 1, "body": variant}]},
        ):
            assert not ok(opened=[location]), variant

    balanced_relative_negative_variants = (
        "[review](../(z)/../pull/201)",
        "[review](../(z)/../pull/2000)",
        "[review](../(z)/../pull/200abc)",
        "[review](/vokerg/other/(z)/../pull/200)",
        "[review](../../other/(z)/../pull/200)",
        "[review](//evil.test/vokerg/everfield/(z)/../pull/200)",
        "[review](https://evil.test/vokerg/everfield/(z)/../pull/200)",
        "[review]: /vokerg/other/(z)/../pull/200\n\n[review]",
        "[review](../(z)/../issues/200)",
    )
    for variant in balanced_relative_negative_variants:
        assert not references_pr(variant, 200), variant
        assert ok(opened=[{**clean, "body": variant}]), variant

    # FSR-1786-M01: independent review found escaped ')' must remain literal
    # until CommonMark's true unescaped inline delimiter has been located.
    escaped_parenthesis_live_links = (
        r"[review](../a\)b/../pull/200)",
        r"[review](../a\)b/../pull/+0200.diff)",
        r"[review](/vokerg/everfield/a\)b/../pull/0200.patch/files)",
        r"[review](../(z\))/../pull/200)",
        "[review](" + "\n" + r"../a\)b/../pull/200)",
        r"[review]: ../a\)b/../pull/200" + "\n\n[review]",
    )
    for variant in escaped_parenthesis_live_links:
        assert references_pr(variant, 200), variant
        for location in (
            {**clean, "title": variant},
            {**clean, "body": variant},
            {**clean, "live_comments": [{"id": 1, "body": variant}]},
        ):
            assert not ok(opened=[location]), variant
    for variant in (
        r"[review](../a\)b/../pull/201)",
        r"[review](../a\)b/../pull/2000)",
        r"[review](/vokerg/other/a\)b/../pull/200)",
        r"[review](https://foreign.example/a\)b/../pull/200)",
    ):
        assert not references_pr(variant, 200), variant
        assert ok(opened=[{**clean, "body": variant}]), variant

    # Ambiguous first-party percent paths are conservative closure vetoes.
    for ambiguous in (
        f"https://github.com/{REPO}/pull/%2F0200",
        f"https://github.com/{REPO}/pull/%252B200",
        f"https://api.github.com/repos/{REPO}/pulls/%zz",
        "[review](../pull/%2f0200)",
    ):
        assert references_pr(ambiguous, 200), ambiguous
        assert not ok(opened=[{**clean, "body": ambiguous}]), ambiguous

    # Real relative references to different PRs, repos or paths do not veto
    # retirement of reviewer PR #200; foreign full URLs are never rebased.
    relative_nonreferences = (
        "[review](../pull/201)",
        "[review](../pull/2000)",
        "[review](../pull/200abc)",
        "[review](../pull/200.diffuse)",
        "[review](../issues/200)",
        "[review](/vokerg/other/pull/200)",
        "[review](/evil/everfield/pull/200)",
        "[review](../../other/pull/200)",
        "[review](https://evil.test/vokerg/everfield/pull/200)",
        "[review](//evil.test/vokerg/everfield/pull/200)",
    )
    for variant in relative_nonreferences:
        assert not references_pr(variant, 200), variant
        assert ok(opened=[{**clean, "body": variant}]), variant

    # Foreign hosts, repositories, paths and numeric prefixes remain distinct.
    commonmark_escaped_nonreferences = (
        r"[review](https\://github\.com/vokerg/everfield/pull/2000)",
        r"[review](https://github\.com/vokerg/everfield/pull/200abc)",
        r"[review](https://github\.com/vokerg/everfield/pull/200\.diffuse)",
        r"[review](https://github\.com/vokerg/everfield/issues/200)",
        r"[review](https://github\.com/vokerg/other/pull/200\?tab=files)",
        r"[review](https://github\.com.evil.test/vokerg/everfield/pull/200)",
        r"[review](https://api.github\.com/repos/vokerg/other/pulls/200)",
        r"[review](https://foreign.example/vokerg/everfield/pull/200)",
        r"[review](https\://github&#46;com.evil.test/vokerg/everfield/pull/200)",
    )
    for variant in commonmark_escaped_nonreferences:
        assert not references_pr(variant, 200), variant
        assert ok(opened=[{**clean, "body": variant}]), variant

    html_nonreferences = (
        "[review](https://github&#46;com/vokerg/everfield/pull/2000)",
        "[review](https://github.com/vokerg/everfield/pull/200abc)",
        "[review](https://github.com/vokerg/everfield/pull/200.diffuse)",
        "[review](https://github.com/vokerg/everfield/issues/200)",
        "[review](https://github.com/vokerg/other/pull&#47;200)",
        "[review](https://github&#46;com.evil.test/vokerg/everfield/pull/200)",
        "[review](https://api.github&#46;com/repos/vokerg/other/pulls/200)",
        "[review](https://foreign.example/vokerg/everfield/pull/200)",
        r"[review](https:\/\/github&#46;com\/vokerg\/everfield\/pull\/2000)",
        "[review](https://github.com:443/vokerg/everfield/pull/2000)",
    )
    for variant in html_nonreferences:
        assert not references_pr(variant, 200), variant
        assert ok(opened=[{**clean, "body": variant}]), variant

    for nonreference in (
        r"[review](https:\/\/github.com/vokerg/everfield/pull/2000)",
        r"[review](https:\/\/github.com/vokerg/everfield/pull/200abc)",
        r"[review](https:\/\/github.com/vokerg/everfield/pull/200.diffuse)",
        r"[review](https:\/\/github.com/vokerg/everfield/issues/200)",
        r"[review](https:\/\/github.com/vokerg/other/pull/200)",
        r"[review](https:\/\/github.com.evil.test/vokerg/everfield/pull/200)",
        r"[review](https:\/\/api.github.com/repos/vokerg/other/pulls/200)",
    ):
        assert not references_pr(nonreference, 200), nonreference
        assert ok(opened=[{**clean, "body": nonreference}]), nonreference

    # Genuine nonreferences preserve eligible retirement; no substring #200
    # extraction from 2000/200abc, untrusted host, issue path or foreign repo.
    for nonreference in (
        f"http://github.com/{REPO}/pull/2000",
        f"//github.com/{REPO}/pull/200abc",
        f"http://github.com/{REPO}/issues/200",
        "http://github.com/vokerg/other/pull/200",
        f"//github.com.evil.test/{REPO}/pull/200",
        f"http://api.github.com/repos/{REPO}/pulls/2000",
        f"//api.github.com/repos/vokerg/other/pulls/200",
        f"ftp://github.com/{REPO}/pull/200",
    ):
        assert ok(opened=[{**clean, "body": nonreference}]), nonreference

    # Formatting must not reinterpret a different number/repo/path as #200.
    for nonreference in (
        f"**https://github.com/{REPO}/pull/2000**",
        f"__https://github.com/{REPO}/pull/200abc__",
        f"https://github.com/{REPO}/pull/2000|Next",
        f"**https://github.com/{REPO}/issues/200**",
        "**https://github.com/vokerg/other/pull/200**",
        f"__https://github.com.evil.test/{REPO}/pull/200__",
        f"**https://api.github.com/repos/{REPO}/pulls/2000**",
        f"https://github.com/{REPO}/pull/200abc|Next",
        f"https://github.com/{REPO}/pull/200.diffuse|Next",
    ):
        assert not references_pr(nonreference, 200), nonreference
        assert ok(opened=[{**clean, "body": nonreference}]), nonreference

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

    # Verify real full live-issue pagination reader carries the ordered-dot
    # active reference from a server-returned comment into eligibility.
    try:
        globals()["paged"] = lambda path: [live] if path.endswith(
            "/issues?state=open") else [{**live_comment, "body":
                "[review](../issues/tmp/%2e%2e/../pull/+0200)"}]
        complete_ordered = live_open_issue_references(f"/repos/{REPO}")
        assert not ok(opened=complete_ordered)
    finally:
        globals()["paged"] = original_paged

    # Browser-equivalent first-party authority in a fully loaded comment
    # remains a veto through the real live issue/comment coverage reader.
    for browser_reference in (browser_authority_positive_variants +
                              multiline_parenthesis_positive_variants +
                              balanced_relative_positive_variants):
        try:
            globals()["paged"] = lambda path: [live] if path.endswith(
                "/issues?state=open") else [{**live_comment, "body": browser_reference}]
            complete_browser = live_open_issue_references(f"/repos/{REPO}")
            assert not ok(opened=complete_browser), browser_reference
        finally:
            globals()["paged"] = original_paged

    # Exercise execute(apply=True) with a changing live comment between its
    # first pass and the immediate pre-PATCH recheck. Never send a real PATCH.
    original_request = request
    original_datetime = datetime
    scans = 0
    late_link = f"Keep {web_port}.diff"
    early_link = ""
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
            return [{**live_comment, "body": early_link or ("No link" if scans == 1 else late_link)}]
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
        for late_link in (
            f"Keep {web_port}.diff",
            f"Keep {http_web}/files",
            f"Keep {http_api}.patch",
            f"[review]({relative_web})",
            f"Keep {relative_api}/files",
            f"**{web}**", f"__{http_web}__", f"{relative_web}|Later cell",
            f"**{api}.patch**", f"{api}|Adjacent",
            *escaped_variants,
            *html_variants,
            *commonmark_escaped_variants,
            *relative_positive_variants,
            *alias_positive_variants,
            *ordered_dot_positive_variants,
            *browser_authority_positive_variants,
            *multiline_parenthesis_positive_variants,
            *balanced_relative_positive_variants,
        ):
            scans = 0
            patches.clear()
            execute(apply=True)
            assert scans == 2 and not patches, (
                "active reference introduced before PATCH escaped veto: " + late_link
            )
        # Real first-pass execute(apply=True) vetoes a pre-existing linked
        # issue before any second scan or closure PATCH.
        for early_link in (
            f"**{web}**", f"*{http_web}*", f"__{relative_api}__",
            f"{api}|Adjacent cell", f"|{relative_web}|More",
            *escaped_variants,
            *html_variants,
            *commonmark_escaped_variants,
            *relative_positive_variants,
            *alias_positive_variants,
            *ordered_dot_positive_variants,
            *browser_authority_positive_variants,
            *multiline_parenthesis_positive_variants,
            *balanced_relative_positive_variants,
        ):
            scans = 0
            patches.clear()
            execute(apply=True)
            assert scans == 1 and not patches, (
                "first-pass Markdown reference escaped veto: " + early_link
            )
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
