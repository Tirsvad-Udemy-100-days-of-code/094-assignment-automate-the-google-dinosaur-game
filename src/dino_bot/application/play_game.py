"""!
@file play_game.py
@brief The use case: find the game on the screen, start it, and jump whenever an obstacle is ahead.
"""

import logging
from collections.abc import Callable
from dataclasses import dataclass

from dino_bot import constants
from dino_bot.application.ports import Clock, Keyboard, ScreenSource
from dino_bot.domain.box import Box
from dino_bot.domain.game_area import GameArea, find_game_area
from dino_bot.domain.obstacle import is_collision

_log = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class GameReport:
    """!
    @brief What happened during a game.
    """

    ## Times the bot hit the space bar to jump (the press that starts the game is not counted).
    jumps: int
    ## Times the bot looked at the screen.
    looks: int
    ## Seconds the bot played.
    seconds: float


def locate_game(screen: ScreenSource, search_region: Box | None = None) -> GameArea:
    """!
    @brief Take a screenshot and find the game in it.
    @param screen Where the screenshot comes from.
    @param search_region The part of the screen to search, or None for the whole screen.
    @return The game area in screen coordinates.
    @throws GameNotFoundError When the game is not visible.
    """
    frame = screen.take_screenshot(search_region)
    area = find_game_area(frame)
    if search_region is not None:
        area = area.moved_by(search_region.left, search_region.top)
    _log.info("Game found: ground line from x=%d to x=%d at y=%d", area.left, area.right, area.ground_y)
    return area


def play_game(
    screen: ScreenSource,
    keyboard: Keyboard,
    clock: Clock,
    search_region: Box | None = None,
    duration_seconds: float | None = None,
    should_stop: Callable[[], bool] | None = None,
) -> GameReport:
    """!
    @brief Play the game: hit the space bar to start, find the game, then look at the pixels ahead and jump in time.

    The game is searched after the start, because the ground line only gets its full width once the game runs.
    @param screen Where the screenshots come from.
    @param keyboard Where the space bar is pressed.
    @param clock Time source.
    @param search_region The part of the screen to search for the game, or None for the whole screen.
    @param duration_seconds Stop after this many seconds, or None to play until should_stop says so.
    @param should_stop Asked after each look; True ends the game. None never stops early.
    @return What happened.
    @throws GameNotFoundError When the game is not visible.
    """
    keyboard.hit_space_bar()
    start = clock.now()
    clock.sleep(constants.START_ANIMATION_SECONDS)
    area = locate_game(screen, search_region)
    last_jump = start - constants.JUMP_COOLDOWN_SECONDS
    jumps = 0
    looks = 0
    elapsed = 0.0
    while duration_seconds is None or elapsed < duration_seconds:
        now = clock.now()
        elapsed = now - start
        frame = screen.take_screenshot(area.detection_box(elapsed))
        looks += 1
        if is_collision(frame) and now - last_jump >= constants.JUMP_COOLDOWN_SECONDS:
            keyboard.hit_space_bar()
            last_jump = now
            jumps += 1
            _log.debug("Jump %d after %.2f s", jumps, elapsed)
        if should_stop is not None and should_stop():
            break
        if constants.POLL_INTERVAL_SECONDS > 0:
            clock.sleep(constants.POLL_INTERVAL_SECONDS)
    seconds = clock.now() - start
    _log.info("Played %.1f s: %d jumps, %d looks", seconds, jumps, looks)
    return GameReport(jumps=jumps, looks=looks, seconds=seconds)
