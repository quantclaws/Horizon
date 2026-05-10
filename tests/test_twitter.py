"""Tests for TwitterScraper (Camoufox-based)."""

import asyncio
from datetime import datetime, timedelta, timezone

import httpx

from src.models import TwitterConfig
from src.scrapers.twitter import TwitterScraper


def _make_config(**kwargs) -> TwitterConfig:
    defaults = dict(
        enabled=True,
        users=["karpathy"],
        fetch_limit=3,
    )
    defaults.update(kwargs)
    return TwitterConfig(**defaults)


def test_disabled_returns_empty():
    client = httpx.AsyncClient()
    result = asyncio.run(
        TwitterScraper(_make_config(enabled=False), client).fetch(
            datetime.now(timezone.utc)
        )
    )
    asyncio.run(client.aclose())
    assert result == []


def test_no_users_returns_empty():
    client = httpx.AsyncClient()
    result = asyncio.run(
        TwitterScraper(_make_config(users=[]), client).fetch(
            datetime.now(timezone.utc)
        )
    )
    asyncio.run(client.aclose())
    assert result == []


def test_parse_metric_number():
    assert TwitterScraper._parse_metric_number("1.2K") == 1200
    assert TwitterScraper._parse_metric_number("5M") == 5000000
    assert TwitterScraper._parse_metric_number("123") == 123
    assert TwitterScraper._parse_metric_number("") == 0


def test_parse_metric_from_aria():
    assert TwitterScraper._parse_metric_from_aria("68006 Likes. Like") == 68006
    assert TwitterScraper._parse_metric_from_aria("1,234 Replies. Reply") == 1234
    assert TwitterScraper._parse_metric_from_aria("") == 0
    assert TwitterScraper._parse_metric_from_aria("No number here") == 0


def test_extract_tweet_id():
    assert TwitterScraper._extract_tweet_id("https://x.com/user/status/12345") == "12345"
    assert TwitterScraper._extract_tweet_id("https://twitter.com/user/status/67890") == "67890"
    assert TwitterScraper._extract_tweet_id("") is None
    assert TwitterScraper._extract_tweet_id("invalid") is None


def test_append_discussion_content_adds_marker():
    from src.models import ContentItem, SourceType

    item = ContentItem(
        id="twitter:tweet:1",
        source_type=SourceType.TWITTER,
        title="test",
        url="https://twitter.com/x/status/1",
        content="original text",
        author="x",
        published_at=datetime.now(timezone.utc),
        metadata={},
    )
    changed = TwitterScraper.append_discussion_content(item, ["[@alice | ❤️ 5 | 💬 1] reply text"])
    assert changed is True
    assert "--- Top Comments ---" in item.content
    assert "alice" in item.content


def test_append_discussion_content_empty_lines_no_change():
    from src.models import ContentItem, SourceType

    item = ContentItem(
        id="twitter:tweet:2",
        source_type=SourceType.TWITTER,
        title="test",
        url="https://twitter.com/x/status/2",
        content="original",
        author="x",
        published_at=datetime.now(timezone.utc),
        metadata={},
    )
    changed = TwitterScraper.append_discussion_content(item, [])
    assert changed is False
    assert item.content == "original"


def test_fetch_replies_disabled_by_default():
    """fetch_reply_text defaults to False — verify config default."""
    cfg = TwitterConfig()
    assert cfg.fetch_reply_text is False
