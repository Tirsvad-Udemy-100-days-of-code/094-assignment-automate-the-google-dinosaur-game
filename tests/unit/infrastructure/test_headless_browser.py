"""!
@file test_headless_browser.py
@brief Tests of the headless Chrome adapter with a stand-in for Playwright; no browser is started.
"""

import io
from pathlib import Path
from typing import Any

import pytest
from PIL import Image

from dino_bot.domain.box import Box
from dino_bot.infrastructure import headless_browser
from dino_bot.infrastructure.headless_browser import HeadlessGame


def png_bytes(width: int = 8, height: int = 6) -> bytes:
    buffer = io.BytesIO()
    Image.new("RGB", (width, height), (255, 255, 255)).save(buffer, format="PNG")
    return buffer.getvalue()


class FakeKeyboard:
    def __init__(self) -> None:
        self.keys: list[str] = []

    def press(self, key: str) -> None:
        self.keys.append(key)


class FakePage:
    def __init__(self) -> None:
        self.keyboard = FakeKeyboard()
        self.screenshots: list[dict[str, Any]] = []
        self.visited: list[str] = []
        self.styles: list[str] = []
        self.waited_for: list[str] = []
        self.crashed = False
        self.score = 123

    def goto(self, url: str, wait_until: str, timeout: float) -> None:
        self.visited.append(url)

    def wait_for_selector(self, selector: str) -> None:
        self.waited_for.append(selector)

    def add_style_tag(self, content: str) -> None:
        self.styles.append(content)

    def screenshot(self, **options: Any) -> bytes:
        self.screenshots.append(options)
        clip = options.get("clip")
        return png_bytes(clip["width"], clip["height"]) if clip else png_bytes()

    def evaluate(self, script: str) -> Any:
        return self.crashed if "crashed" in script else self.score


class FakeBrowser:
    def __init__(self, page: FakePage) -> None:
        self.page = page
        self.closed = False

    def new_page(self, viewport: dict[str, int]) -> FakePage:
        return self.page

    def close(self) -> None:
        self.closed = True


class FakePlaywright:
    def __init__(self, browser: FakeBrowser) -> None:
        self.chromium = self
        self.browser = browser
        self.stopped = False

    def launch(self, channel: str, headless: bool) -> FakeBrowser:
        assert channel == "chrome" and headless
        return self.browser

    def start(self) -> FakePlaywright:
        return self

    def stop(self) -> None:
        self.stopped = True


def game_with_page() -> tuple[HeadlessGame, FakePage]:
    game = HeadlessGame("https://example.test/game")
    page = FakePage()
    game._page = page
    return game, page


def test_context_opens_the_game_and_closes_the_browser(monkeypatch: pytest.MonkeyPatch) -> None:
    page = FakePage()
    browser = FakeBrowser(page)
    playwright = FakePlaywright(browser)

    class FakeSyncApi:
        @staticmethod
        def sync_playwright() -> FakePlaywright:
            return playwright

    monkeypatch.setattr(headless_browser.importlib, "import_module", lambda name: FakeSyncApi)
    with HeadlessGame("https://example.test/game") as game:
        assert page.visited == ["https://example.test/game"]
        assert page.waited_for == ["canvas"]
        assert "overflow" in page.styles[0]
        assert game._page is page
    assert browser.closed and playwright.stopped


def test_screenshot_is_grey_and_can_be_clipped() -> None:
    game, page = game_with_page()
    assert (game.take_screenshot().width, game.take_screenshot().height) == (8, 6)
    clipped = game.take_screenshot(Box(10, 20, 15, 29))
    assert (clipped.width, clipped.height) == (5, 9)
    assert page.screenshots[-1]["clip"] == {"x": 10, "y": 20, "width": 5, "height": 9}


def test_hit_space_bar_presses_space_in_the_page() -> None:
    game, page = game_with_page()
    game.hit_space_bar()
    assert page.keyboard.keys == ["Space"]


def test_game_over_and_score_are_read_from_the_page() -> None:
    game, page = game_with_page()
    assert not game.is_game_over()
    page.crashed = True
    assert game.is_game_over()
    assert game.score() == 123


def test_picture_is_saved_in_a_new_folder(tmp_path: Path) -> None:
    game, page = game_with_page()
    target = tmp_path / "shots" / "run.png"
    game.save_picture(target)
    assert target.parent.is_dir()
    assert page.screenshots[-1] == {"path": str(target)}
