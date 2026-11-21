"""!
@file test_system_clock.py
@brief Tests of the real clock.
"""

import pytest

from dino_bot.infrastructure import system_clock
from dino_bot.infrastructure.system_clock import SystemClock


def test_time_does_not_go_backwards() -> None:
    clock = SystemClock()
    first = clock.now()
    assert clock.now() >= first


def test_sleep_waits_through_the_time_module(monkeypatch: pytest.MonkeyPatch) -> None:
    waited: list[float] = []
    monkeypatch.setattr(system_clock.time, "sleep", waited.append)
    SystemClock().sleep(0.25)
    assert waited == [0.25]
