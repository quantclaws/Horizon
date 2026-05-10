"""Twitter scraper using Camoufox browser with persistent cookies."""

import asyncio
import json
import logging
import os
import re
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import List, Optional

import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, TwitterConfig

logger = logging.getLogger(__name__)

# Camoufox site-packages path (shared with content-factory venv)
_CAMOUFOX_SITE = "/Users/openclaw/workspace/content-factory/venv/lib/python3.14/site-packages"

# Cookie storage path
_COOKIE_PATH = Path("data/twitter_cookies.json")

# Default proxy from environment
_DEFAULT_PROXY = os.environ.get("CAMOUFOX_PROXY", "http://127.0.0.1:7890")


def _ensure_camoufox_path():
    """Add camoufox to sys.path if needed."""
    import sys

    if _CAMOUFOX_SITE not in sys.path:
        sys.path.insert(0, _CAMOUFOX_SITE)


class TwitterScraper(BaseScraper):
    """Fetch tweets via Camoufox browser with cookie persistence."""

    def __init__(self, config: TwitterConfig, http_client: httpx.AsyncClient):
        super().__init__(config, http_client)
        self.config = config
        _ensure_camoufox_path()

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.config.enabled:
            return []

        users = [u.strip().lstrip("@") for u in self.config.users if u.strip()]
        if not users:
            logger.debug("No Twitter users configured, skipping.")
            return []

        logger.info(f"Fetching Twitter (Camoufox) for users: {users}")

        # Run blocking camoufox code in thread pool
        loop = asyncio.get_event_loop()
        items = await loop.run_in_executor(
            None, self._fetch_sync, users, since
        )
        logger.info(f"Fetched {len(items)} tweets via Camoufox.")
        return items

    def _fetch_sync(self, users: List[str], since: datetime) -> List[ContentItem]:
        """Synchronous fetch using Camoufox."""
        try:
            from camoufox.sync_api import Camoufox
        except ImportError:
            logger.error("Camoufox not available. Install it in the content-factory venv.")
            return []

        all_items: List[ContentItem] = []
        proxy = {"server": _DEFAULT_PROXY}

        with Camoufox(headless=True, proxy=proxy) as browser:
            # Load cookies if available
            storage_state = self._load_storage_state()
            context = browser.new_context(storage_state=storage_state)
            page = context.new_page()

            for user in users:
                try:
                    user_items = self._fetch_user_sync(page, user, since)
                    all_items.extend(user_items)
                except Exception as exc:
                    logger.warning(f"Error fetching Twitter user {user}: {exc}")

            # Save cookies for next run
            self._save_storage_state(context)
            context.close()

        return all_items

    def _fetch_user_sync(
        self, page, user: str, since: datetime
    ) -> List[ContentItem]:
        """Fetch tweets for a single user."""
        url = f"https://twitter.com/{user}"
        logger.debug(f"Navigating to {url}")

        page.goto(url, timeout=120000, wait_until="networkidle")
        page.wait_for_timeout(10000)

        # Wait for tweets to appear
        try:
            page.wait_for_selector('article[data-testid="tweet"]', timeout=15000)
        except Exception:
            logger.warning(f"No tweets found for {user}")
            return []

        items: List[ContentItem] = []
        seen_ids: set[str] = set()
        max_scrolls = 10
        no_new_count = 0

        for _ in range(max_scrolls):
            # Parse currently visible tweets
            tweets = page.query_selector_all('article[data-testid="tweet"]')
            new_found = 0

            for tweet in tweets:
                parsed = self._parse_tweet_element(tweet, user, since)
                if parsed and parsed.id not in seen_ids:
                    seen_ids.add(parsed.id)
                    items.append(parsed)
                    new_found += 1

            # Check if we should continue scrolling
            if len(items) >= self.config.fetch_limit:
                break

            if new_found == 0:
                no_new_count += 1
                if no_new_count >= 2:
                    break
            else:
                no_new_count = 0

            # Scroll down to load more
            page.evaluate("window.scrollBy(0, 800)")
            page.wait_for_timeout(2000)

        return items[: self.config.fetch_limit]

    def _parse_tweet_element(
        self, tweet, user: str, since: datetime
    ) -> Optional[ContentItem]:
        """Parse a single tweet DOM element into ContentItem."""
        try:
            # Extract tweet text
            text_el = tweet.query_selector('[data-testid="tweetText"]')
            if not text_el:
                return None
            text = text_el.inner_text().strip()
            if not text:
                return None
            text = unescape(text)

            # Extract tweet URL (from time link)
            time_el = tweet.query_selector("time")
            tweet_url = ""
            published_at = datetime.now(timezone.utc)

            if time_el:
                datetime_attr = time_el.get_attribute("datetime")
                if datetime_attr:
                    try:
                        published_at = datetime.fromisoformat(
                            datetime_attr.replace("Z", "+00:00")
                        )
                    except ValueError:
                        pass

                # Find parent link for tweet URL
                time_link = time_el.evaluate("el => el.closest('a')?.href")
                if time_link:
                    tweet_url = time_link

            # Filter by time
            if published_at < since:
                return None

            # Extract author
            author_el = tweet.query_selector('[data-testid="User-Name"]')
            author = user
            screen_name = user
            if author_el:
                author_text = author_el.inner_text().strip()
                # Format: "Display Name\n@handle"
                parts = author_text.split("\n")
                if len(parts) >= 2:
                    author = parts[0].strip()
                    screen_name = parts[1].strip().lstrip("@")

            # Extract engagement metrics
            metrics = self._extract_metrics(tweet)

            # Generate tweet ID from URL or content hash
            tweet_id = self._extract_tweet_id(tweet_url) or str(hash(text))

            # Build title
            title_body = text[:50].replace("\n", " ").strip()
            if len(text) > 50:
                title_body += "..."

            if not tweet_url:
                tweet_url = f"https://twitter.com/{screen_name}/status/{tweet_id}"

            return ContentItem(
                id=self._generate_id(SourceType.TWITTER.value, "tweet", tweet_id),
                source_type=SourceType.TWITTER,
                title=f"@{screen_name}: {title_body}",
                url=tweet_url,
                content=text,
                author=author,
                published_at=published_at,
                metadata={
                    "tweet_id": tweet_id,
                    "favorite_count": metrics.get("likes", 0),
                    "retweet_count": metrics.get("retweets", 0),
                    "reply_count": metrics.get("replies", 0),
                    "view_count": metrics.get("views"),
                },
            )
        except Exception as exc:
            logger.debug(f"Failed to parse tweet: {exc}")
            return None

    def _extract_metrics(self, tweet) -> dict:
        """Extract engagement metrics from tweet element."""
        metrics = {"likes": 0, "retweets": 0, "replies": 0, "views": None}

        # Find all metric buttons in the action bar
        buttons = tweet.query_selector_all('[role="group"] button, [role="group"] a')

        for btn in buttons:
            testid = btn.get_attribute("data-testid") or ""
            aria = btn.get_attribute("aria-label") or ""

            # Parse raw number from aria-label (e.g. "68006 Likes. Like")
            num = self._parse_metric_from_aria(aria)

            if testid == "like":
                metrics["likes"] = num
            elif testid == "reply":
                metrics["replies"] = num
            elif testid == "retweet":
                metrics["retweets"] = num
            elif "views" in aria.lower() and "view post analytics" in aria.lower():
                metrics["views"] = num

        return metrics

    @staticmethod
    def _parse_metric_from_aria(aria: str) -> int:
        """Parse raw number from aria-label like '68006 Likes. Like'."""
        if not aria:
            return 0
        # Extract first number from the string
        match = re.search(r"(\d+(?:,\d+)*)", aria)
        if match:
            return int(match.group(1).replace(",", ""))
        return 0

    @staticmethod
    def _parse_metric_number(text: str) -> int:
        """Parse metric string like '1.2K' or '5M' into number."""
        text = text.strip().lower().replace(",", "")
        if not text:
            return 0

        match = re.match(r"^([\d.]+)\s*([km]?)\b", text)
        if not match:
            return 0

        num_str, suffix = match.groups()
        try:
            num = float(num_str)
        except ValueError:
            return 0

        if suffix == "k":
            num *= 1000
        elif suffix == "m":
            num *= 1000000

        return int(num)

    @staticmethod
    def _extract_tweet_id(url: str) -> Optional[str]:
        """Extract tweet ID from Twitter URL."""
        if not url:
            return None
        match = re.search(r"/status/(\d+)", url)
        return match.group(1) if match else None

    def _load_storage_state(self) -> Optional[dict]:
        """Load camoufox storage state (cookies + localStorage)."""
        if _COOKIE_PATH.exists():
            try:
                with open(_COOKIE_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as exc:
                logger.debug(f"Failed to load Twitter cookies: {exc}")
        return None

    def _save_storage_state(self, context):
        """Save camoufox storage state for next run."""
        try:
            state = context.storage_state()
            _COOKIE_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(_COOKIE_PATH, "w", encoding="utf-8") as f:
                json.dump(state, f)
            logger.debug(f"Saved Twitter cookies to {_COOKIE_PATH}")
        except Exception as exc:
            logger.debug(f"Failed to save Twitter cookies: {exc}")

    async def fetch_replies_for_item(self, item: ContentItem) -> List[str]:
        """Fetch reply texts for one tweet."""
        if not self.config.fetch_reply_text:
            return []

        max_replies = max(self.config.max_replies_per_tweet, 0)
        if max_replies == 0:
            return []

        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, self._fetch_replies_sync, item, max_replies
        )

    def _fetch_replies_sync(self, item: ContentItem, max_replies: int) -> List[str]:
        """Synchronous reply fetch using Camoufox."""
        try:
            from camoufox.sync_api import Camoufox
        except ImportError:
            return []

        tweet_url = str(item.url)
        proxy = {"server": _DEFAULT_PROXY}
        reply_lines: List[str] = []

        with Camoufox(headless=True, proxy=proxy) as browser:
            storage_state = self._load_storage_state()
            context = browser.new_context(storage_state=storage_state)
            page = context.new_page()

            try:
                page.goto(tweet_url, timeout=120000, wait_until="domcontentloaded")
                page.wait_for_timeout(5000)

                # Look for reply tweets
                replies = page.query_selector_all('article[data-testid="tweet"]')
                min_likes = max(self.config.reply_min_likes, 0)
                candidates = []

                for reply in replies[1:]:  # Skip first (original tweet)
                    try:
                        text_el = reply.query_selector('[data-testid="tweetText"]')
                        if not text_el:
                            continue
                        text = text_el.inner_text().strip()
                        if not text:
                            continue

                        author_el = reply.query_selector('[data-testid="User-Name"]')
                        handle = "unknown"
                        if author_el:
                            author_text = author_el.inner_text().strip()
                            parts = author_text.split("\n")
                            if len(parts) >= 2:
                                handle = parts[1].strip().lstrip("@")

                        # Skip original author
                        if handle == (item.author or "").lstrip("@"):
                            continue

                        metrics = self._extract_metrics(reply)
                        likes = metrics.get("likes", 0)
                        if likes < min_likes:
                            continue

                        line = f"[@{handle} | ❤️ {likes}] {text[:280]}"
                        candidates.append((likes, line))
                    except Exception:
                        continue

                candidates.sort(key=lambda x: x[0], reverse=True)
                reply_lines = [line for _, line in candidates[:max_replies]]

            except Exception as exc:
                logger.warning(f"Failed to fetch replies for {item.id}: {exc}")
            finally:
                self._save_storage_state(context)
                context.close()

        return reply_lines

    @staticmethod
    def append_discussion_content(item: ContentItem, reply_lines: List[str]) -> bool:
        """Append reply lines under Top Comments marker."""
        if not reply_lines:
            return False

        existing = item.content or ""
        marker = "--- Top Comments ---"
        block = "\n".join(reply_lines)

        if marker in existing:
            if block in existing:
                return False
            item.content = existing + "\n" + block
            return True

        if existing:
            item.content = existing + f"\n\n{marker}\n" + block
        else:
            item.content = f"{marker}\n" + block
        return True
