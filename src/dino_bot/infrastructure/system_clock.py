"""!
@file system_clock.py
@brief The real clock.
"""

import time


class SystemClock:
    """!
    @brief Time from the operating system's monotonic clock.
    """

    def now(self) -> float:
        """!
        @brief Seconds from a fixed point.
        """
        return time.monotonic()

    def sleep(self, seconds: float) -> None:
        """!
        @brief Wait for some seconds.
        """
        time.sleep(seconds)
