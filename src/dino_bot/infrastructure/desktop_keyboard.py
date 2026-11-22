"""!
@file desktop_keyboard.py
@brief Presses the space bar on the desktop with pyautogui.
"""

import importlib
from types import ModuleType

from dino_bot import constants
from dino_bot.application.ports import StopRequestedError


class DesktopKeyboard:
    """!
    @brief Sends key presses to the window in front, the way a person would.

    pyautogui is imported when the keyboard is made, not when this module is imported, so the rest of the package
    and its tests work on a computer without a desktop. Its fail-safe stays on: moving the mouse to a corner of the
    screen stops the bot.
    """

    def __init__(self, gui: ModuleType | None = None) -> None:
        """!
        @brief Make the keyboard.
        @param gui The pyautogui module, or a stand-in with the same press function; None imports pyautogui.
        """
        self._gui = gui if gui is not None else importlib.import_module("pyautogui")
        # pyautogui waits 0.1 s after every call by default; the bot cannot afford that.
        self._gui.PAUSE = 0

    def hit(self, key: str) -> None:
        """!
        @brief Press and release one key.
        @param key Name of the key, as pyautogui spells it, for example "space".
        @throws StopRequestedError When the mouse is in a corner of the screen (the pyautogui fail-safe).
        """
        try:
            self._gui.press(key)
        except self._gui.FailSafeException as error:
            raise StopRequestedError("Stopped by the fail-safe: the mouse is in a corner of the screen") from error

    def hit_space_bar(self) -> None:
        """!
        @brief Press and release the space bar once.
        @throws StopRequestedError When the mouse is in a corner of the screen (the pyautogui fail-safe).
        """
        self.hit(constants.JUMP_KEY)


def hit(key: str = constants.JUMP_KEY) -> None:
    """!
    @brief Press and release one key on the desktop; the name is the one the assignment uses.
    @param key Name of the key, as pyautogui spells it; the space bar by default.
    """
    DesktopKeyboard().hit(key)
