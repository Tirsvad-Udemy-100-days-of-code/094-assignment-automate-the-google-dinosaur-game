"""!
@file test_system_clock.py
@brief Tests of the real clock.
"""

from dino_bot.infrastructure.system_clock import SystemClock


def test_time_does_not_go_backwards() -> None:
    clock = SystemClock()
    first = clock.now()
    assert clock.now() >= first


def test_sleep_waits_for_the_given_time() -> None:
    clock = SystemClock()
    start = clock.now()
    clock.sleep(0.05)
    assert clock.now() - start >= 0.04
