"""!
@file fakes.py
@brief Fakes of the ports, so the use case and the command line run without a screen, keyboard or clock.
"""

from dino_bot.domain.box import Box
from dino_bot.domain.frame import Frame
from pictures import Picture


class FakeClock:
    """!
    @brief A clock that moves forward a fixed step each time it is read, and when it sleeps.
    """

    def __init__(self, step: float = 0.05) -> None:
        self.time = 0.0
        self.step = step
        self.slept: list[float] = []

    def now(self) -> float:
        value = self.time
        self.time += self.step
        return value

    def sleep(self, seconds: float) -> None:
        self.slept.append(seconds)
        self.time += seconds


class FakeScreen:
    """!
    @brief A screen that always shows the same picture.
    """

    def __init__(self, picture: Picture) -> None:
        self.picture = picture
        self.regions: list[Box | None] = []

    def take_screenshot(self, region: Box | None = None) -> Frame:
        self.regions.append(region)
        frame = self.picture.frame()
        return frame if region is None else frame.crop(region)


class FakeKeyboard:
    """!
    @brief A keyboard that counts the presses of the space bar.
    """

    def __init__(self) -> None:
        self.presses = 0

    def hit_space_bar(self) -> None:
        self.presses += 1
