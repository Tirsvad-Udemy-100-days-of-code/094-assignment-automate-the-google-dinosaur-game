"""!
@file test_cli.py
@brief Tests of the command line, with the desktop adapters replaced by fakes.
"""

from pathlib import Path

import pytest

from dino_bot import __main__ as cli
from dino_bot.application.play_game import GameReport
from dino_bot.application.ports import StopRequestedError
from dino_bot.domain.box import Box
from dino_bot.domain.game_area import GameNotFoundError
from dino_bot.infrastructure import desktop_keyboard, desktop_screen, headless_browser, system_clock
from fakes import FakeClock, FakeKeyboard, FakeScreen
from pictures import Picture, draw_cactus, game_picture

REPORT = GameReport(jumps=3, looks=10, seconds=1.5)


def use_fake_desktop(monkeypatch: pytest.MonkeyPatch, picture: Picture) -> FakeKeyboard:
    keyboard = FakeKeyboard()
    monkeypatch.setattr(desktop_screen, "DesktopScreen", lambda: FakeScreen(picture))
    monkeypatch.setattr(desktop_keyboard, "DesktopKeyboard", lambda: keyboard)
    monkeypatch.setattr(system_clock, "SystemClock", lambda: FakeClock())
    monkeypatch.setattr(cli.time, "sleep", lambda seconds: None)
    return keyboard


def test_parser_defaults() -> None:
    args = cli.build_parser().parse_args([])
    assert args.seconds is None
    assert args.countdown == 3
    assert args.region is None
    assert not args.headless


def test_desktop_run_plays_the_game_and_exits_with_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    picture = game_picture(left=100, ground_y=400)
    draw_cactus(picture, 100, 400, 1.0, game_x=100)
    keyboard = use_fake_desktop(monkeypatch, picture)
    assert cli.main(["--seconds", "1", "--countdown", "2"]) == 0
    assert keyboard.presses >= 2


def test_game_not_found_exits_with_two(monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture) -> None:
    use_fake_desktop(monkeypatch, Picture(800, 600))
    with caplog.at_level("ERROR"):
        assert cli.main(["--seconds", "1", "--countdown", "0"]) == cli.EXIT_GAME_NOT_FOUND
    assert "No ground line found" in caplog.text


def test_region_is_passed_on_as_a_box(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: list[Box | None] = []
    monkeypatch.setattr(cli, "run_desktop", lambda seconds, countdown, region: seen.append(region) or REPORT)
    assert cli.main(["--region", "1", "2", "3", "4"]) == 0
    assert seen == [Box(1, 2, 3, 4)]


def test_fail_safe_stops_the_bot_with_exit_code_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    def stop(*_: object) -> GameReport:
        raise StopRequestedError("Stopped by the fail-safe")

    monkeypatch.setattr(cli, "run_desktop", stop)
    assert cli.main([]) == 0


def test_ctrl_c_stops_the_bot_with_exit_code_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    def interrupt(*_: object) -> GameReport:
        raise KeyboardInterrupt

    monkeypatch.setattr(cli, "run_desktop", interrupt)
    assert cli.main([]) == 0


def test_headless_option_runs_the_headless_game(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    calls: list[tuple[float | None, Path | None]] = []
    monkeypatch.setattr(cli, "run_headless", lambda seconds, picture: calls.append((seconds, picture)) or REPORT)
    picture = tmp_path / "run.png"
    assert cli.main(["--headless", "--seconds", "5", "--picture", str(picture)]) == 0
    assert calls == [(5.0, picture)]


def test_game_not_found_in_headless_mode_also_exits_with_two(monkeypatch: pytest.MonkeyPatch) -> None:
    def missing(*_: object) -> GameReport:
        raise GameNotFoundError("No ground line found")

    monkeypatch.setattr(cli, "run_headless", missing)
    assert cli.main(["--headless"]) == cli.EXIT_GAME_NOT_FOUND


class FakeHeadlessGame(FakeScreen, FakeKeyboard):
    """!
    @brief Stands in for the headless Chrome: a screen and a keyboard, with a game that ends after a few looks.
    """

    def __init__(self) -> None:
        FakeScreen.__init__(self, headless_picture())
        FakeKeyboard.__init__(self)
        self.saved: list[Path] = []

    def __enter__(self) -> FakeHeadlessGame:
        return self

    def __exit__(self, *_: object) -> None:
        return None

    def is_game_over(self) -> bool:
        return len(self.regions) > 6

    def score(self) -> int:
        return 42

    def save_picture(self, path: Path) -> None:
        self.saved.append(path)


def headless_picture() -> Picture:
    picture = game_picture(left=100, ground_y=400)
    draw_cactus(picture, 100, 400, 1.0, game_x=100)
    return picture


def test_headless_run_plays_until_the_dinosaur_crashes_and_saves_the_picture(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    game = FakeHeadlessGame()
    monkeypatch.setattr(headless_browser, "HeadlessGame", lambda: game)
    monkeypatch.setattr(system_clock, "SystemClock", lambda: FakeClock())
    picture = tmp_path / "run.png"
    report = cli.run_headless(None, picture)
    assert report.jumps >= 1
    assert game.saved == [picture]
