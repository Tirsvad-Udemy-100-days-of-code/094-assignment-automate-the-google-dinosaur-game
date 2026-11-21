"""!
@file test_play_game.py
@brief Tests of the use case that plays the game, with a fake screen, keyboard and clock.
"""

import pytest

from dino_bot import constants
from dino_bot.application.play_game import locate_game, play_game
from dino_bot.domain.box import Box
from dino_bot.domain.game_area import GameNotFoundError
from fakes import FakeClock, FakeKeyboard, FakeScreen
from pictures import Picture, draw_cactus, game_picture

LEFT = 100
GROUND = 400


def road_with_cactus() -> Picture:
    picture = game_picture(left=LEFT, ground_y=GROUND)
    draw_cactus(picture, LEFT, GROUND, 1.0, game_x=100)
    return picture


def test_locate_game_finds_the_ground_line() -> None:
    area = locate_game(FakeScreen(game_picture(left=LEFT, ground_y=GROUND)))
    assert (area.left, area.right, area.ground_y) == (LEFT, LEFT + 600, GROUND)


def test_locate_game_adds_the_offset_of_the_search_region() -> None:
    picture = game_picture(left=LEFT, ground_y=GROUND)
    region = Box(50, 300, 900, 500)
    area = locate_game(FakeScreen(picture), region)
    assert (area.left, area.ground_y) == (LEFT, GROUND)


def test_locate_game_fails_when_the_game_is_not_visible() -> None:
    with pytest.raises(GameNotFoundError):
        locate_game(FakeScreen(Picture(800, 600)))


def test_play_game_starts_the_game_with_the_space_bar_and_jumps_at_a_cactus() -> None:
    keyboard = FakeKeyboard()
    report = play_game(FakeScreen(road_with_cactus()), keyboard, FakeClock(), duration_seconds=3.0)
    assert report.jumps >= 1
    assert keyboard.presses == report.jumps + 1  # the first press starts the game
    assert report.looks > 1


def test_play_game_does_not_jump_on_an_empty_road() -> None:
    keyboard = FakeKeyboard()
    report = play_game(
        FakeScreen(game_picture(left=LEFT, ground_y=GROUND)), keyboard, FakeClock(), duration_seconds=3.0
    )
    assert report.jumps == 0
    assert keyboard.presses == 1


def test_play_game_waits_between_two_jumps() -> None:
    keyboard = FakeKeyboard()
    clock = FakeClock(step=0.05)
    report = play_game(FakeScreen(road_with_cactus()), keyboard, clock, duration_seconds=4.0)
    assert report.jumps <= 4.0 / constants.JUMP_COOLDOWN_SECONDS + 1
    assert report.jumps >= 2


def test_play_game_waits_for_the_game_to_widen_before_it_looks() -> None:
    clock = FakeClock()
    play_game(FakeScreen(road_with_cactus()), FakeKeyboard(), clock, duration_seconds=2.0)
    assert clock.slept[0] == constants.START_ANIMATION_SECONDS


def test_play_game_stops_when_asked() -> None:
    report = play_game(FakeScreen(road_with_cactus()), FakeKeyboard(), FakeClock(), should_stop=lambda: True)
    assert report.looks == 1


def test_play_game_without_a_game_presses_no_jump() -> None:
    keyboard = FakeKeyboard()
    with pytest.raises(GameNotFoundError):
        play_game(FakeScreen(Picture(800, 600)), keyboard, FakeClock(), duration_seconds=3.0)
    assert keyboard.presses == 1  # only the press that starts the game


def test_play_game_reports_the_seconds_it_played() -> None:
    report = play_game(FakeScreen(road_with_cactus()), FakeKeyboard(), FakeClock(), duration_seconds=3.0)
    assert report.seconds >= 3.0
