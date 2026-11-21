"""!
@file test_box.py
@brief Tests of the Box value object.
"""

import pytest

from dino_bot.domain.box import Box


def test_box_has_width_and_height() -> None:
    box = Box(10, 20, 40, 70)
    assert (box.width, box.height) == (30, 50)


@pytest.mark.parametrize("corners", [(10, 20, 10, 30), (10, 20, 5, 30), (10, 20, 30, 20), (10, 20, 30, 10)])
def test_box_without_a_positive_size_is_refused(corners: tuple[int, int, int, int]) -> None:
    with pytest.raises(ValueError, match="positive size"):
        Box(*corners)


def test_box_can_be_moved() -> None:
    assert Box(1, 2, 3, 4).moved_by(10, 20) == Box(11, 22, 13, 24)
