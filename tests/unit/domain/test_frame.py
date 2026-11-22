"""!
@file test_frame.py
@brief Tests of the Frame value object.
"""

import pytest

from dino_bot.domain.box import Box
from dino_bot.domain.frame import Frame


def numbered(width: int, height: int) -> Frame:
    return Frame(width, height, bytes(range(width * height)))


def test_frame_needs_a_positive_size() -> None:
    with pytest.raises(ValueError, match="positive size"):
        Frame(0, 5, b"")


def test_frame_needs_one_byte_per_pixel() -> None:
    with pytest.raises(ValueError, match="needs 6 bytes"):
        Frame(3, 2, b"\x00\x01")


def test_row_and_pixel_read_the_right_bytes() -> None:
    frame = numbered(4, 3)
    assert frame.row(1) == bytes([4, 5, 6, 7])
    assert frame.pixel(2, 2) == 10


def test_crop_returns_the_part_inside_the_box() -> None:
    frame = numbered(4, 3)
    cropped = frame.crop(Box(1, 1, 3, 3))
    assert (cropped.width, cropped.height) == (2, 2)
    assert cropped.pixels == bytes([5, 6, 9, 10])


@pytest.mark.parametrize("box", [Box(-1, 0, 2, 2), Box(0, -1, 2, 2), Box(0, 0, 5, 2), Box(0, 0, 2, 4)])
def test_crop_outside_the_frame_is_refused(box: Box) -> None:
    with pytest.raises(ValueError, match="not inside"):
        numbered(4, 3).crop(box)


def test_background_is_the_most_common_grey() -> None:
    frame = Frame(3, 2, bytes([255, 255, 255, 255, 83, 0]))
    assert frame.background() == 255
