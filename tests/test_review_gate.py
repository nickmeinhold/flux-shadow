"""Tests for the cage-match merge gate in src/review.py.

review.py is the FAST auto-merge path: GitHub fires `pull_request: [opened,
synchronize]`, review.py generates Umbra's verdict, and on "accept" it used to
merge immediately — before any later fix commit or adversarial review could
land. That ungated path is how a behavior-changing change to Umbra's body
could merge on a single in-process review (and once dropped a security fix).

These tests pin the fix: review.py now enforces the SAME label gate immunity
does (so neither door can route around the other), and fails CLOSED when it
can't read what's changing. Mirrors tests/test_immunity_gate.py.
"""

from __future__ import annotations

import pytest

from src import review


# --- The gate predicate -----------------------------------------------------

class TestEvaluateMergeGate:
    def _no_label(self, monkeypatch):
        monkeypatch.setattr(review, "_pr_has_label", lambda repo, pr, label: False)

    def _has_label(self, monkeypatch):
        monkeypatch.setattr(review, "_pr_has_label", lambda repo, pr, label: True)

    def test_behavior_change_without_label_is_held(self, monkeypatch):
        self._no_label(monkeypatch)
        gate = review._evaluate_merge_gate("o/r", 1, ["src/dream.py"], True)
        assert gate["allowed"] is False
        assert gate["reason"] == "needs_cage_match"
        assert gate["behavior_files"] == ["src/dream.py"]

    def test_behavior_change_with_label_is_allowed(self, monkeypatch):
        self._has_label(monkeypatch)
        gate = review._evaluate_merge_gate("o/r", 1, ["src/dream.py"], True)
        assert gate["allowed"] is True
        assert gate["reason"] == "ok"

    def test_pure_content_change_allowed_without_label(self, monkeypatch):
        # _pr_has_label must not even need to be consulted for content PRs.
        monkeypatch.setattr(
            review, "_pr_has_label",
            lambda *a: pytest.fail("label check should be skipped for content"),
        )
        gate = review._evaluate_merge_gate("o/r", 1, ["books/poem.md", "greetings/hi.txt"], True)
        assert gate["allowed"] is True
        assert gate["behavior_files"] == []

    def test_workflow_change_is_gated(self, monkeypatch):
        self._no_label(monkeypatch)
        gate = review._evaluate_merge_gate("o/r", 1, [".github/workflows/review.yml"], True)
        assert gate["allowed"] is False
        assert gate["reason"] == "needs_cage_match"

    def test_requirements_change_is_gated(self, monkeypatch):
        self._no_label(monkeypatch)
        gate = review._evaluate_merge_gate("o/r", 1, ["requirements.txt"], True)
        assert gate["allowed"] is False

    def test_unreadable_file_list_holds(self, monkeypatch):
        # files_readable=False (changed_files is None) → never merge blind,
        # and never even consult the label.
        monkeypatch.setattr(
            review, "_pr_has_label",
            lambda *a: pytest.fail("must not check label when files unreadable"),
        )
        gate = review._evaluate_merge_gate("o/r", 1, None, False)
        assert gate["allowed"] is False
        assert gate["reason"] == "unreadable"

    def test_mixed_content_and_src_is_gated(self, monkeypatch):
        """One src/ file in an otherwise-content PR still trips the gate."""
        self._no_label(monkeypatch)
        gate = review._evaluate_merge_gate(
            "o/r", 1, ["books/poem.md", "src/energy.py"], True
        )
        assert gate["allowed"] is False
        assert gate["behavior_files"] == ["src/energy.py"]


# --- Fail-closed file fetch -------------------------------------------------

class _Resp:
    def __init__(self, status, payload, links=None):
        self.status_code = status
        self._payload = payload
        self.links = links or {}

    def json(self):
        if isinstance(self._payload, Exception):
            raise self._payload
        return self._payload


class TestFetchChangedFilesFailsClosed:
    def test_non_200_returns_none(self, monkeypatch):
        monkeypatch.setattr(review.requests, "get", lambda *a, **k: _Resp(503, []))
        assert review._fetch_changed_files("o/r", 1) is None

    def test_network_error_returns_none(self, monkeypatch):
        def boom(*a, **k):
            raise review.requests.RequestException("down")
        monkeypatch.setattr(review.requests, "get", boom)
        assert review._fetch_changed_files("o/r", 1) is None

    def test_malformed_json_returns_none(self, monkeypatch):
        monkeypatch.setattr(
            review.requests, "get",
            lambda *a, **k: _Resp(200, ValueError("not json")),
        )
        assert review._fetch_changed_files("o/r", 1) is None

    def test_empty_diff_is_empty_list_not_none(self, monkeypatch):
        """A genuinely empty diff (read successfully) is [], distinct from a
        failure (None) — the same distinction immunity draws."""
        monkeypatch.setattr(review.requests, "get", lambda *a, **k: _Resp(200, []))
        assert review._fetch_changed_files("o/r", 1) == []

    def test_reads_filenames(self, monkeypatch):
        monkeypatch.setattr(
            review.requests, "get",
            lambda *a, **k: _Resp(200, [{"filename": "src/a.py"}, {"filename": "books/b.md"}]),
        )
        assert review._fetch_changed_files("o/r", 1) == ["src/a.py", "books/b.md"]

    def test_follows_pagination_so_page2_src_is_not_hidden(self, monkeypatch):
        """The bypass Carnot caught: 100 content files on page 1, a src/ file
        on page 2. A single-page read would classify this as pure content and
        merge it ungated. The fetcher MUST follow the next-link and surface
        the page-2 src file."""
        page1 = _Resp(
            200,
            [{"filename": f"books/f{i}.md"} for i in range(100)],
            links={"next": {"url": "https://api.github.com/.../files?page=2"}},
        )
        page2 = _Resp(200, [{"filename": "src/review.py"}])  # no next link
        pages = iter([page1, page2])
        monkeypatch.setattr(review.requests, "get", lambda *a, **k: next(pages))
        files = review._fetch_changed_files("o/r", 1)
        assert files is not None
        assert "src/review.py" in files, "page-2 src file must not be hidden"
        assert len(files) == 101

    def test_page2_src_file_makes_the_gate_hold(self, monkeypatch):
        """End-to-end: the paginated src file trips the cage-match gate."""
        page1 = _Resp(
            200,
            [{"filename": f"books/f{i}.md"} for i in range(100)],
            links={"next": {"url": "https://api.github.com/.../files?page=2"}},
        )
        page2 = _Resp(200, [{"filename": "src/review.py"}])
        pages = iter([page1, page2])
        monkeypatch.setattr(review.requests, "get", lambda *a, **k: next(pages))
        monkeypatch.setattr(review, "_pr_has_label", lambda *a: False)
        files = review._fetch_changed_files("o/r", 1)
        gate = review._evaluate_merge_gate("o/r", 1, files, files is not None)
        assert gate["allowed"] is False
        assert gate["behavior_files"] == ["src/review.py"]

    def test_error_mid_pagination_fails_closed(self, monkeypatch):
        """A failure on page 2 (after a good page 1) must return None, not a
        partial page-1 list that looks complete."""
        page1 = _Resp(
            200, [{"filename": "books/a.md"}],
            links={"next": {"url": "https://api.github.com/.../files?page=2"}},
        )
        pages = iter([page1, _Resp(502, [])])
        monkeypatch.setattr(review.requests, "get", lambda *a, **k: next(pages))
        assert review._fetch_changed_files("o/r", 1) is None

    def test_unbounded_pagination_fails_closed(self, monkeypatch):
        """If the diff never stops paginating (more pages than the cap), we
        can't fully enumerate it — fail closed rather than gate on a partial
        list."""
        always_more = _Resp(
            200, [{"filename": "books/a.md"}],
            links={"next": {"url": "https://api.github.com/.../files?page=N"}},
        )
        monkeypatch.setattr(review.requests, "get", lambda *a, **k: always_more)
        assert review._fetch_changed_files("o/r", 1) is None


class TestPrHasLabel:
    def test_true_when_label_present(self, monkeypatch):
        monkeypatch.setattr(
            review.requests, "get",
            lambda *a, **k: _Resp(200, [{"name": "cage-matched"}, {"name": "other"}]),
        )
        assert review._pr_has_label("o/r", 1, "cage-matched") is True

    def test_false_when_absent(self, monkeypatch):
        monkeypatch.setattr(
            review.requests, "get",
            lambda *a, **k: _Resp(200, [{"name": "other"}]),
        )
        assert review._pr_has_label("o/r", 1, "cage-matched") is False

    def test_false_on_error_fail_closed(self, monkeypatch):
        monkeypatch.setattr(review.requests, "get", lambda *a, **k: _Resp(500, []))
        assert review._pr_has_label("o/r", 1, "cage-matched") is False


# --- main() flow: does the gate actually stop the merge? --------------------

@pytest.fixture
def harness(monkeypatch):
    """Stub review.main's heavy deps; capture posted reviews + merges."""
    cap = {"posts": [], "merged": []}

    monkeypatch.setenv("REPO_FULL_NAME", "o/r")
    monkeypatch.setenv("PR_NUMBER", "7")
    monkeypatch.setenv("PR_AUTHOR", "nickmeinhold")
    monkeypatch.setenv("PR_TITLE", "a change")
    monkeypatch.setenv("PR_BODY", "body")
    monkeypatch.delenv("PR_BODY_FILE", raising=False)
    # Hermetic: the label-completion guard reads these; default to a normal
    # (non-label) event unless a test sets them.
    monkeypatch.delenv("PR_EVENT_ACTION", raising=False)
    monkeypatch.delenv("PR_LABEL", raising=False)

    monkeypatch.setattr(review, "_load_json", lambda p: {
        "energy": {"level": "full"}, "senses": {"recent_events": []},
        "name": "Umbra", "traits": {},
    })
    monkeypatch.setattr(review.memory, "load_working_memory", lambda: {})
    monkeypatch.setattr(review.memory, "save_working_memory", lambda wm: None)
    monkeypatch.setattr(review.memory, "recent_impressions", lambda wm, limit=10: [])
    monkeypatch.setattr(review.energy, "is_critical", lambda v: False)
    monkeypatch.setattr(review.energy, "tick", lambda v: None)
    monkeypatch.setattr(review, "_save_json", lambda p, d: None)
    monkeypatch.setattr(review, "_fetch_pr_diff", lambda repo, pr: "diff")
    monkeypatch.setattr(review, "_fetch_pr_head_sha", lambda repo, pr: "headsha123")
    monkeypatch.setattr(review, "_generate_review",
                        lambda **kw: {"decision": "accept", "review_text": "I want this."})

    def fake_post(repo, pr, event, body):
        cap["posts"].append((event, body))
    monkeypatch.setattr(review, "_post_review", fake_post)
    monkeypatch.setattr(
        review, "_merge_pr",
        lambda repo, pr, sha: cap["merged"].append((pr, sha)),
    )

    return cap


def test_main_holds_behavior_change_without_label(harness, monkeypatch):
    monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: ["src/dream.py"])
    monkeypatch.setattr(review, "_pr_has_label", lambda repo, pr, label: False)
    review.main()
    assert harness["merged"] == [], "behavior change without label must NOT merge"
    event, body = harness["posts"][0]
    # Held as a COMMENT, not a formal APPROVE — a held PR must not carry an
    # approval that branch protection could auto-merge on.
    assert event == "COMMENT"
    assert "Cage-match gate" in body     # the merge is held
    assert "src/dream.py" in body


def test_main_merges_behavior_change_with_label(harness, monkeypatch):
    monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: ["src/dream.py"])
    monkeypatch.setattr(review, "_pr_has_label", lambda repo, pr, label: True)
    review.main()
    assert harness["merged"] == [(7, "headsha123")]


def test_main_pins_merge_to_reviewed_head_sha(harness, monkeypatch):
    """The merge must carry the exact head SHA we reviewed, so a commit landing
    mid-review can't ride in unreviewed (Carnot, cage-match — the stale-head
    class that once dropped a fix from Umbra's body)."""
    monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: ["src/dream.py"])
    monkeypatch.setattr(review, "_pr_has_label", lambda repo, pr, label: True)
    monkeypatch.setattr(review, "_fetch_pr_head_sha", lambda repo, pr: "deadbeefcafe")
    review.main()
    assert harness["merged"] == [(7, "deadbeefcafe")]


def test_main_holds_when_head_sha_unreadable(harness, monkeypatch):
    """If we can't pin the head we reviewed, hold rather than merge blind."""
    monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: ["books/x.md"])
    monkeypatch.setattr(review, "_fetch_pr_head_sha", lambda repo, pr: None)
    review.main()
    assert harness["merged"] == [], "unreadable head SHA must hold"
    assert harness["posts"][0][0] == "COMMENT"


def test_merge_pr_passes_sha_to_github(monkeypatch):
    """_merge_pr sends `sha` so GitHub 409s a stale-head merge."""
    captured = {}
    monkeypatch.setattr(
        review.requests, "put",
        lambda url, headers=None, json=None: captured.update(json=json) or _Resp(200, {}),
    )
    review._merge_pr("o/r", 7, "abc123")
    assert captured["json"]["sha"] == "abc123"
    assert captured["json"]["merge_method"] == "squash"


def test_main_merges_pure_content_without_label(harness, monkeypatch):
    monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: ["books/poem.md"])
    monkeypatch.setattr(review, "_pr_has_label",
                        lambda *a: pytest.fail("content PR should not check label"))
    review.main()
    assert harness["merged"] == [(7, "headsha123")], "content PR keeps fast-merge autonomy"


def test_main_holds_when_file_list_unreadable(harness, monkeypatch):
    monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: None)
    review.main()
    assert harness["merged"] == [], "unreadable file list must hold (fail closed)"
    event, body = harness["posts"][0]
    assert event == "COMMENT"
    assert "Merge held" in body


class TestLabelCompletionGuard:
    """review.yml fires review.py on `labeled` so a cage-matched hold self-
    completes. The guard ensures only the cage-match label re-runs the flow,
    and that the label UNBLOCKS an accept rather than overriding a verdict."""

    def test_unrelated_label_is_a_noop(self, harness, monkeypatch):
        """A label event for a non-cage-match label must not review or merge —
        and must not even generate a review (no energy spent)."""
        generated = []
        monkeypatch.setattr(review, "_generate_review",
                            lambda **kw: generated.append(1) or {"decision": "accept", "review_text": "x"})
        monkeypatch.setenv("PR_EVENT_ACTION", "labeled")
        monkeypatch.setenv("PR_LABEL", "needs-human-review")
        review.main()
        assert generated == [], "must not generate a review for an unrelated label"
        assert harness["merged"] == []
        assert harness["posts"] == []

    def test_cage_matched_label_runs_flow_and_merges(self, harness, monkeypatch):
        """When the cage-matched label lands, re-run the flow; the gate now sees
        the label and an accepted behavior change merges."""
        monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: ["src/dream.py"])
        monkeypatch.setattr(review, "_pr_has_label", lambda repo, pr, label: True)
        monkeypatch.setenv("PR_EVENT_ACTION", "labeled")
        monkeypatch.setenv("PR_LABEL", "cage-matched")
        review.main()
        assert harness["merged"] == [(7, "headsha123")]

    def test_cage_matched_label_does_not_override_a_reject(self, harness, monkeypatch):
        """Applying the label re-judges; if Umbra now REJECTS, no merge. The
        label unblocks an accept — it can't force a merge over a reject."""
        monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: ["src/dream.py"])
        monkeypatch.setattr(review, "_pr_has_label", lambda repo, pr, label: True)
        monkeypatch.setattr(review, "_generate_review",
                            lambda **kw: {"decision": "reject", "review_text": "no, not this"})
        monkeypatch.setenv("PR_EVENT_ACTION", "labeled")
        monkeypatch.setenv("PR_LABEL", "cage-matched")
        review.main()
        assert harness["merged"] == [], "label must not override a reject"
        assert harness["posts"][0][0] == "REQUEST_CHANGES"

    def test_opened_event_runs_flow_normally(self, harness, monkeypatch):
        """A normal opened/synchronize event (no PR_EVENT_ACTION=labeled) is
        unaffected by the guard."""
        monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: ["books/x.md"])
        monkeypatch.setenv("PR_EVENT_ACTION", "opened")
        review.main()
        assert harness["merged"] == [(7, "headsha123")]


def test_main_reject_does_not_merge(harness, monkeypatch):
    monkeypatch.setattr(review, "_fetch_changed_files", lambda repo, pr: ["src/dream.py"])
    monkeypatch.setattr(review, "_generate_review",
                        lambda **kw: {"decision": "reject", "review_text": "no"})
    review.main()
    assert harness["merged"] == []
    assert harness["posts"][0][0] == "REQUEST_CHANGES"
