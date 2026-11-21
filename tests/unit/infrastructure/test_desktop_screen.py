"""!
@file test_desktop_screen.py
@brief Tests of the Pillow screen; the real screen is never grabbed.
"""

import pytest
from PIL import Image

from dino_bot.domain.box import Box
from dino_bot.infrastructure import desktop_screen
from dino_bot.infrastructure.desktop_screen import DesktopScreen, frame_from_image


def test_colour_image_becomes_a_grey_frame() -> None:
    image = Image.new("RGB", (4, 3), (83, 83, 83))
    frame = frame_from_image(image)
    assert (frame.width, frame.height) == (4, 3)
    assert set(frame.pixels) == {83}


def test_screenshot_of_a_region_passes_the_box_to_pillow(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: list[tuple[int, int, int, int] | None] = []

    def fake_grab(bbox: tuple[int, int, int, int] | None = None) -> Image.Image:
        seen.append(bbox)
        return Image.new("RGB", (10, 5), (255, 255, 255))

    monkeypatch.setattr(desktop_screen.ImageGrab, "grab", fake_grab)
    screen = DesktopScreen()
    assert screen.take_screenshot(Box(1, 2, 11, 7)).width == 10
    assert screen.take_screenshot().height == 5
    assert seen == [(1, 2, 11, 7), None]
