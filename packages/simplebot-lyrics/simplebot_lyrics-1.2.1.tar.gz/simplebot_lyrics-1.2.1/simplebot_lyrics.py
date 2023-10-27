"""Plugin's commands definition."""

import functools
from urllib.parse import quote, unquote_plus

import bs4
import requests
import simplebot
from deltachat import Message
from pkg_resources import DistributionNotFound, get_distribution
from simplebot.bot import Replies

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = "0.0.0.dev0-unknown"
session = requests.Session()
session.headers.update(
    {
        "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
    }
)
session.request = functools.partial(session.request, timeout=15)  # type: ignore


@simplebot.filter
def search_lyrics(message: Message, replies: Replies) -> None:
    """Send me a song name or part of the lyrics to search."""
    if not message.chat.is_multiuser():
        _search(message.text, replies)


@simplebot.command
def lyrics(payload: str, replies: Replies) -> None:
    """Get song lyrics.

    Example:
    /lyrics Baby Jane
    """
    _search(payload, replies)


def _search(query: str, replies: Replies) -> None:
    base_url = "https://www.lyrics.com"
    url = f"{base_url}/lyrics/{quote(query)}"
    with session.get(url) as resp:
        resp.raise_for_status()
        soup = bs4.BeautifulSoup(resp.text, "html.parser")
    best_matches = soup.find("div", class_="best-matches")
    anchor = best_matches and best_matches.a
    if not anchor:
        soup = soup.find("div", class_="sec-lyric")
        anchor = soup and soup.a
    if anchor:
        artist, name = map(unquote_plus, anchor["href"].split("/")[-2:])
        url = base_url + anchor["href"]
        with session.get(url) as resp:
            resp.raise_for_status()
            soup = bs4.BeautifulSoup(resp.text, "html.parser")
            lyric = soup.find(id="lyric-body-text")
            if lyric:
                text = f"🎵 {name} - {artist}\n\n{lyric.get_text()}"
                replies.add(text=text)
                return

    replies.add(text=f"❌ No results for: {query!r}")


class TestPlugin:
    """Online tests"""

    def test_lyrics(self, mocker):
        msg = mocker.get_one_reply("/lyrics Baby Jane")
        assert "🎵" in msg.text

    def test_filter(self, mocker) -> None:
        msg = mocker.get_one_reply("Baby Jane")
        assert "🎵" in msg.text

        # filter should work only in private/direct chat
        msgs = mocker.get_replies("Baby Jane", group="group1")
        assert not msgs
