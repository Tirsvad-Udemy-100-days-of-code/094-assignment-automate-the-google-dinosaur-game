"""!
@file ports.py
@brief The ports of the use case: how it looks at the screen, presses keys and tells time.
"""

from typing import Protocol

from dino_bot.domain.box import Box
from dino_bot.domain.frame import Frame


class StopRequestedError(Exception):
    """!
    @brief The user asked the bot to stop, for example with the fail-safe of the keyboard.
    """


class ScreenSource(Protocol):
    """!
    @brief Something that can take a greyscale screenshot: the desktop, or a headless browser page.
    """

    def take_screenshot(self, region: Box | None = None) -> Frame:
        """!
        @brief Take a greyscale screenshot.
        @param region The part of the screen to take, or None for all of it.
        @return The screenshot; its pixel (0, 0) is the top left corner of the region.
        """
        ...


class Keyboard(Protocol):
    """!
    @brief Something that can press the space bar in the game.
    """

    def hit_space_bar(self) -> None:
        """!
        @brief Press and release the space bar once: it starts the game and makes the dinosaur jump.
        @throws StopRequestedError When the user asked the bot to stop.
        """
        ...


class Clock(Protocol):
    """!
    @brief Time, so the use case can be tested without waiting.
    """

    def now(self) -> float:
        """!
        @brief Seconds from a fixed point; only differences are used.
        """
        ...

    def sleep(self, seconds: float) -> None:
        """!
        @brief Wait for some seconds.
        """
        ...
