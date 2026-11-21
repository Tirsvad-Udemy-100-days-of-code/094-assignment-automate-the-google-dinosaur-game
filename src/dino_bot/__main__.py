"""!
@file __main__.py
@brief Command line and composition root: python -m dino_bot.
"""

import argparse
import logging
import sys
import time
from collections.abc import Sequence
from pathlib import Path

from dino_bot import constants
from dino_bot.application.play_game import GameReport, play_game
from dino_bot.application.ports import StopRequestedError
from dino_bot.domain.box import Box
from dino_bot.domain.game_area import GameNotFoundError

_log = logging.getLogger("dino_bot")

## Exit code when the game was not found on the screen.
EXIT_GAME_NOT_FOUND: int = 2


def build_parser() -> argparse.ArgumentParser:
    """!
    @brief The command line options.
    """
    parser = argparse.ArgumentParser(
        prog="dino-bot",
        description=f"{constants.APP_TITLE}: plays the Google Dinosaur Game ({constants.GAME_URL}) by looking at "
        "screen pixels and hitting the space bar. Move the mouse to a screen corner to stop it.",
    )
    parser.add_argument("--seconds", type=float, default=None, help="stop after this many seconds (default: play on)")
    parser.add_argument(
        "--countdown",
        type=int,
        default=constants.DEFAULT_COUNTDOWN_SECONDS,
        help="seconds to wait before starting, to bring the game to the front (default: %(default)s)",
    )
    parser.add_argument(
        "--region",
        type=int,
        nargs=4,
        metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
        help="search for the game only in this part of the screen",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="play in a headless Chrome instead of on the desktop (needs the 'headless' extra)",
    )
    parser.add_argument("--picture", type=Path, help="headless only: save a screenshot of the page at the end")
    parser.add_argument("-v", "--verbose", action="store_true", help="log every jump")
    return parser


def run_desktop(seconds: float | None, countdown: int, region: Box | None) -> GameReport:
    """!
    @brief Play on the desktop: Pillow looks at the screen and pyautogui presses the space bar.
    """
    from dino_bot.infrastructure.desktop_keyboard import DesktopKeyboard
    from dino_bot.infrastructure.desktop_screen import DesktopScreen
    from dino_bot.infrastructure.system_clock import SystemClock

    for left in range(countdown, 0, -1):
        _log.info("Starting in %d ...", left)
        time.sleep(1)
    return play_game(DesktopScreen(), DesktopKeyboard(), SystemClock(), region, seconds)


def run_headless(seconds: float | None, picture: Path | None) -> GameReport:
    """!
    @brief Play in a headless Chrome until the dinosaur crashes or the time is up.
    """
    from dino_bot.infrastructure.headless_browser import HeadlessGame
    from dino_bot.infrastructure.system_clock import SystemClock

    with HeadlessGame() as game:
        report = play_game(game, game, SystemClock(), None, seconds, should_stop=game.is_game_over)
        _log.info("Score shown by the game: %d", game.score())
        if picture is not None:
            game.save_picture(picture)
            _log.info("Picture saved to %s", picture)
    return report


def main(argv: Sequence[str] | None = None) -> int:
    """!
    @brief Run the bot from the command line.
    @return 0 when the game was played, 2 when it was not found on the screen.
    """
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    _log.setLevel(logging.DEBUG if args.verbose else logging.INFO)
    region = Box(*args.region) if args.region else None
    try:
        if args.headless:
            report = run_headless(args.seconds, args.picture)
        else:
            report = run_desktop(args.seconds, args.countdown, region)
    except GameNotFoundError as error:
        _log.error("%s", error)
        return EXIT_GAME_NOT_FOUND
    except StopRequestedError as error:
        _log.info("%s", error)
        return 0
    except KeyboardInterrupt:
        _log.info("Stopped.")
        return 0
    _log.info("Done: %d jumps in %.1f s.", report.jumps, report.seconds)
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
