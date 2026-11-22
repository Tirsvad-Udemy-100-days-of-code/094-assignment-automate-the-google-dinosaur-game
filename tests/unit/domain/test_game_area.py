"""!
@file test_game_area.py
@brief Tests of finding the game on a screenshot and of the detection box.
"""

from pathlib import Path

import pytest
from PIL import Image

from dino_bot import constants
from dino_bot.domain.frame import Frame
from dino_bot.domain.game_area import GameArea, GameNotFoundError, find_game_area, look_ahead, speed_at
from pictures import Picture, game_picture


@pytest.mark.parametrize("scale", [1.0, 0.8, 1.5, 2.0])
@pytest.mark.parametrize("night", [False, True])
def test_game_is_found_at_any_scale_in_day_and_night(scale: float, night: bool) -> None:
    frame = game_picture(scale=scale, night=night, left=120, ground_y=350).frame()
    area = find_game_area(frame)
    assert area.left == 120
    assert area.right == 120 + round(constants.GAME_WIDTH * scale)
    assert area.ground_y == 350
    assert area.scale == pytest.approx(scale, rel=0.01)


def test_game_is_found_on_a_real_screenshot() -> None:
    image = Image.open(Path(__file__).parents[2] / "fixtures" / "game_day.png").convert("L")
    area = find_game_area(Frame(image.width, image.height, image.tobytes()))
    assert (area.left, area.right, area.ground_y) == (22, 978, 218)
    assert area.scale == pytest.approx(956 / 600)


def test_screen_without_a_game_is_refused() -> None:
    with pytest.raises(GameNotFoundError, match="No ground line found"):
        find_game_area(Picture(800, 600).frame())


def test_short_dark_line_is_not_the_ground() -> None:
    picture = Picture(800, 600)
    picture.rect(10, 100, 10 + constants.MIN_GROUND_LINE_PIXELS - 1, 101, constants.INK_GREY)
    with pytest.raises(GameNotFoundError):
        find_game_area(picture.frame())


def test_the_longest_dark_row_is_the_ground_line() -> None:
    picture = game_picture(ground_y=400)
    picture.rect(300, 200, 330, 260, constants.INK_GREY)  # a tall object has many short rows
    assert find_game_area(picture.frame()).ground_y == 400


def test_game_area_needs_a_positive_width() -> None:
    with pytest.raises(ValueError, match="positive width"):
        GameArea(10, 10, 5)


def test_game_area_can_be_moved() -> None:
    assert GameArea(10, 610, 100).moved_by(5, 7) == GameArea(15, 615, 107)


def test_speed_grows_with_time_up_to_the_highest_speed() -> None:
    assert speed_at(0) == constants.START_SPEED
    assert speed_at(-5) == constants.START_SPEED
    assert speed_at(10) > speed_at(0)
    assert speed_at(10_000) == constants.MAX_SPEED


def test_look_ahead_grows_with_the_speed() -> None:
    assert look_ahead(0) == constants.START_LOOK_AHEAD
    assert look_ahead(30) > look_ahead(0)


def test_detection_box_sits_in_front_of_the_dinosaur_at_scale_one() -> None:
    box = GameArea(100, 700, 400).detection_box(0)
    assert box.left == 100 + round(constants.DINO_RIGHT + constants.BOX_NEAR_GAP)
    assert box.right == 100 + round(constants.DINO_RIGHT + constants.START_LOOK_AHEAD)
    assert box.top == 400 - round(constants.BOX_TOP_ABOVE_GROUND)
    assert box.bottom == 400 - round(constants.BOX_BOTTOM_ABOVE_GROUND)


def test_detection_box_scales_with_the_screen() -> None:
    small = GameArea(0, 600, 400).detection_box(0)
    large = GameArea(0, 1200, 400).detection_box(0)
    assert large.width == pytest.approx(2 * small.width, abs=2)
    assert large.height == pytest.approx(2 * small.height, abs=2)


def test_detection_box_reaches_further_as_the_game_speeds_up() -> None:
    area = GameArea(0, 600, 400)
    assert area.detection_box(60).right > area.detection_box(0).right
    assert area.detection_box(60).left == area.detection_box(0).left
