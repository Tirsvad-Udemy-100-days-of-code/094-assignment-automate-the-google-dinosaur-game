"""!
@file headless_browser.py
@brief The game in a headless Chrome, driven by Playwright: a screen and a keyboard that do not touch the desktop.

Used to watch the bot play without taking the mouse and keyboard of the computer, and to make the screenshots of
the documentation. Needs the optional extra "headless" (Playwright) and an installed Google Chrome.
"""

import importlib
import io
from pathlib import Path
from types import TracebackType
from typing import Any

from PIL import Image

from dino_bot import constants
from dino_bot.domain.box import Box
from dino_bot.domain.frame import Frame
from dino_bot.infrastructure.desktop_screen import frame_from_image


class HeadlessGame:
    """!
    @brief A headless Chrome page with the game open. It is both the screen and the keyboard of the bot.

    Use it as a context manager: the browser starts on enter and closes on exit.
    """

    def __init__(self, url: str = constants.GAME_URL) -> None:
        """!
        @brief Prepare the browser; nothing starts until the context is entered.
        @param url Address of the game page.
        """
        self._url = url
        # Playwright has no type information for its dynamic objects at this level; Any keeps the adapter small.
        self._playwright: Any = None
        self._browser: Any = None
        self._page: Any = None

    def __enter__(self) -> HeadlessGame:
        sync_api = importlib.import_module("playwright.sync_api")
        self._playwright = sync_api.sync_playwright().start()
        self._browser = self._playwright.chromium.launch(channel="chrome", headless=True)
        width, height = constants.HEADLESS_VIEWPORT
        self._page = self._browser.new_page(viewport={"width": width, "height": height})
        self._page.goto(self._url, wait_until="load", timeout=constants.HEADLESS_LOAD_TIMEOUT_SECONDS * 1000)
        self._page.wait_for_selector("canvas")
        # The space bar would scroll the page and move the game away from where the bot found it.
        self._page.add_style_tag(content="html, body { overflow: hidden !important; }")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if self._browser is not None:
            self._browser.close()
        if self._playwright is not None:
            self._playwright.stop()

    def take_screenshot(self, region: Box | None = None) -> Frame:
        """!
        @brief Take a greyscale screenshot of the page or of a part of it.
        @param region The part of the page to take, or None for the visible page.
        """
        options: dict[str, Any] = {}
        if region is not None:
            options["clip"] = {"x": region.left, "y": region.top, "width": region.width, "height": region.height}
        png = self._page.screenshot(**options)
        return frame_from_image(Image.open(io.BytesIO(png)))

    def hit_space_bar(self) -> None:
        """!
        @brief Press and release the space bar in the page.
        """
        self._page.keyboard.press("Space")

    def is_game_over(self) -> bool:
        """!
        @brief True when the dinosaur has crashed. Read from the page, only to stop a headless run.
        """
        return bool(self._page.evaluate("() => !!(window.Runner && Runner.instance_ && Runner.instance_.crashed)"))

    def score(self) -> int:
        """!
        @brief The distance the game shows as the score, read from the page.
        """
        script = (
            "() => (window.Runner && Runner.instance_) ? Runner.instance_.distanceMeter.getActualDistance("
            "Math.ceil(Runner.instance_.distanceRan)) : 0"
        )
        return int(self._page.evaluate(script))

    def save_picture(self, path: Path) -> None:
        """!
        @brief Save a colour screenshot of the page, for the documentation.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        self._page.screenshot(path=str(path))
