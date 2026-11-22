"""!
@file test_obstacle.py
@brief Tests of the rule that decides whether an obstacle is in front of the dinosaur.
"""

import pytest

from dino_bot import constants
from dino_bot.domain.frame import Frame
from dino_bot.domain.obstacle import count_obstacle_pixels, is_collision
from pictures import Picture, draw_cactus, game_picture, ink, zone

LEFT = 100
GROUND = 400


def scene(scale: float, night: bool) -> Picture:
    return game_picture(scale=scale, night=night, left=LEFT, ground_y=GROUND)


def looking(scale: float, night: bool, picture: Picture, elapsed: float = 0.0) -> bool:
    return is_collision(zone(LEFT, GROUND, scale, picture, elapsed))


@pytest.mark.parametrize("night", [False, True])
@pytest.mark.parametrize("scale", [1.0, 1.6])
def test_empty_road_is_not_a_collision(scale: float, night: bool) -> None:
    assert not looking(scale, night, scene(scale, night))


@pytest.mark.parametrize("night", [False, True])
@pytest.mark.parametrize("scale", [1.0, 1.6])
def test_cactus_in_the_zone_is_a_collision(scale: float, night: bool) -> None:
    picture = scene(scale, night)
    draw_cactus(picture, LEFT, GROUND, scale, game_x=100, night=night)
    assert looking(scale, night, picture)


def test_cactus_beyond_the_zone_is_not_seen_yet() -> None:
    picture = scene(1.0, False)
    draw_cactus(picture, LEFT, GROUND, 1.0, game_x=constants.DINO_RIGHT + constants.START_LOOK_AHEAD + 5)
    assert not looking(1.0, False, picture)


def test_cactus_is_seen_further_ahead_when_the_game_is_faster() -> None:
    picture = scene(1.0, False)
    draw_cactus(picture, LEFT, GROUND, 1.0, game_x=constants.DINO_RIGHT + constants.START_LOOK_AHEAD + 5)
    assert looking(1.0, False, picture, elapsed=60)


def test_low_bird_in_the_zone_is_a_collision() -> None:
    picture = scene(1.0, False)
    picture.rect(LEFT + 110, GROUND - 25, LEFT + 135, GROUND - 12, constants.INK_GREY)
    assert looking(1.0, False, picture)


def test_high_bird_above_the_zone_is_ignored() -> None:
    picture = scene(1.0, False)
    picture.rect(LEFT + 110, GROUND - 80, LEFT + 135, GROUND - 60, constants.INK_GREY)
    assert not looking(1.0, False, picture)


def test_bump_in_the_ground_below_the_zone_is_ignored() -> None:
    picture = scene(1.0, False)
    picture.rect(LEFT + 100, GROUND - 4, LEFT + 120, GROUND, constants.INK_GREY)
    assert not looking(1.0, False, picture)


def test_one_stray_pixel_is_noise() -> None:
    picture = scene(1.0, False)
    picture.rect(LEFT + 100, GROUND - 20, LEFT + 101, GROUND - 19, ink(False))
    assert not looking(1.0, False, picture)


def test_pale_cloud_is_not_an_obstacle() -> None:
    picture = scene(1.0, False)
    picture.rect(LEFT + 100, GROUND - 30, LEFT + 130, GROUND - 20, 225)
    assert not looking(1.0, False, picture)


def test_count_obstacle_pixels_counts_pixels_that_differ_from_the_background() -> None:
    frame = Frame(4, 2, bytes([255, 255, 255, 255, 255, 83, 83, 255]))
    assert count_obstacle_pixels(frame) == 2
