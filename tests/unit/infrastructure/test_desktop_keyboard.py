"""!
@file test_desktop_keyboard.py
@brief Tests of the pyautogui keyboard with a stand-in for pyautogui; no key is ever pressed.
"""

import pytest

from dino_bot.application.ports import StopRequestedError
from dino_bot.infrastructure import desktop_keyboard
from dino_bot.infrastructure.desktop_keyboard import DesktopKeyboard, hit


class FakeFailSafeError(Exception):
    pass


class FakeGui:
    """!
    @brief Has the names of pyautogui that the keyboard uses.
    """

    FailSafeException = FakeFailSafeError

    def __init__(self, fail: bool = False) -> None:
        self.PAUSE = 0.1
        self.pressed: list[str] = []
        self.fail = fail

    def press(self, key: str) -> None:
        if self.fail:
            raise FakeFailSafeError
        self.pressed.append(key)


def test_hit_space_bar_presses_the_space_bar() -> None:
    gui = FakeGui()
    DesktopKeyboard(gui).hit_space_bar()  # type: ignore[arg-type]
    assert gui.pressed == ["space"]


def test_keyboard_removes_the_pause_that_pyautogui_adds() -> None:
    gui = FakeGui()
    DesktopKeyboard(gui)  # type: ignore[arg-type]
    assert gui.PAUSE == 0


def test_hit_presses_any_key() -> None:
    gui = FakeGui()
    DesktopKeyboard(gui).hit("up")  # type: ignore[arg-type]
    assert gui.pressed == ["up"]


def test_fail_safe_stops_the_bot() -> None:
    with pytest.raises(StopRequestedError, match="fail-safe"):
        DesktopKeyboard(FakeGui(fail=True)).hit_space_bar()  # type: ignore[arg-type]


def test_hit_function_uses_the_assignment_name_and_the_space_bar_by_default(monkeypatch: pytest.MonkeyPatch) -> None:
    gui = FakeGui()
    monkeypatch.setattr(desktop_keyboard.importlib, "import_module", lambda name: gui)
    hit()
    hit("down")
    assert gui.pressed == ["space", "down"]
