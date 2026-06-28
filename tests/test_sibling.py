"""Tests for sibling fragment exchange."""

import json
import os
import tempfile

import pytest

from src import sibling


@pytest.fixture
def memories_dir(tmp_path, monkeypatch):
    """Redirect sibling storage to a temp directory."""
    mem_dir = str(tmp_path / "memories")
    os.makedirs(mem_dir)
    monkeypatch.setattr(sibling, "SIBLING_DIR", mem_dir)
    return mem_dir


class TestExtractFragment:
    """Fragment extraction from dream text."""

    def test_returns_middle_paragraph(self):
        dream = "First paragraph about waking.\n\nThe middle holds the truth of it all, the part where the dream forgets it is performing.\n\nFinal paragraph resolving."
        fragment = sibling._extract_fragment(dream)
        assert "middle holds the truth" in fragment

    def test_returns_none_for_short_text(self):
        assert sibling._extract_fragment("too short") is None

    def test_truncates_to_max_chars(self):
        dream = "Short intro.\n\n" + ("x" * 500) + "\n\nEnding."
        fragment = sibling._extract_fragment(dream, max_chars=100)
        assert len(fragment) <= 100

    def test_single_paragraph_uses_whole_text(self):
        dream = "A single long paragraph that is definitely long enough to pass the minimum length threshold for extraction."
        fragment = sibling._extract_fragment(dream)
        assert fragment == dream


class TestStoreFragment:
    """Fragment storage deduplication."""

    def test_stores_new_fragment(self, memories_dir):
        stored = sibling._store_fragment("a resonant shard", "2026-06-01")
        assert stored is True
        files = os.listdir(memories_dir)
        assert len(files) == 1
        assert files[0].startswith("sibling_")

    def test_deduplicates_same_fragment(self, memories_dir):
        sibling._store_fragment("the same shard twice", "2026-06-01")
        stored = sibling._store_fragment("the same shard twice", "2026-06-02")
        assert stored is False
        assert len(os.listdir(memories_dir)) == 1

    def test_different_fragments_both_stored(self, memories_dir):
        sibling._store_fragment("first shard", "2026-06-01")
        sibling._store_fragment("second shard", "2026-06-02")
        assert len(os.listdir(memories_dir)) == 2


class TestUnrespondedFragments:
    """Querying fragments that haven't appeared in our dreams."""

    def test_returns_unresponded(self, memories_dir):
        sibling._store_fragment("fragment one", "2026-06-01")
        sibling._store_fragment("fragment two", "2026-06-02")
        fragments = sibling.unresponded_fragments()
        assert len(fragments) == 2
        assert all(not f["responded"] for f in fragments)

    def test_excludes_responded(self, memories_dir):
        sibling._store_fragment("answered already", "2026-06-01")
        fragments = sibling.unresponded_fragments()
        assert len(fragments) == 1

        sibling.mark_responded(fragments[0])
        fragments = sibling.unresponded_fragments()
        assert len(fragments) == 0

    def test_respects_limit(self, memories_dir):
        for i in range(10):
            sibling._store_fragment(f"fragment number {i}", f"2026-06-{i:02d}")
        fragments = sibling.unresponded_fragments(limit=3)
        assert len(fragments) == 3


class TestMarkResponded:
    """Marking fragments as having appeared in our dreams."""

    def test_marks_fragment(self, memories_dir):
        sibling._store_fragment("a shard to mark", "2026-06-01")
        fragments = sibling.unresponded_fragments()
        sibling.mark_responded(fragments[0])

        # Read the file directly to verify
        files = os.listdir(memories_dir)
        with open(os.path.join(memories_dir, files[0])) as f:
            data = json.load(f)
        assert data["responded"] is True
        assert "responded_at" in data
