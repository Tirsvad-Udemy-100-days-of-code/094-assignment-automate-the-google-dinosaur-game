"""!
@file test_smoke.py
@brief Smoke tests: the package imports and its constants are consistent.
"""

import dino_bot
from dino_bot import constants


def test_package_has_a_version() -> None:
    assert dino_bot.__version__ == "0.1.0"


def test_game_address_is_a_web_address() -> None:
    assert constants.GAME_URL.startswith("https://")


def test_game_is_600_game_pixels_wide() -> None:
    assert constants.GAME_WIDTH == 600


def test_jump_key_is_the_space_bar() -> None:
    assert constants.JUMP_KEY == "space"


def test_app_title_names_the_bot() -> None:
    assert "Dino" in constants.APP_TITLE
