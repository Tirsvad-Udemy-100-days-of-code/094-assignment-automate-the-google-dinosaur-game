"""!
@file obstacle.py
@brief The rule that looks at the pixels in front of the dinosaur and decides whether to jump.
"""

from dino_bot import constants
from dino_bot.domain.frame import Frame


def count_obstacle_pixels(frame: Frame) -> int:
    """!
    @brief Count the pixels that stand out from the background of the frame.

    The background is the most common grey value, so the rule works in day mode (dark ink on white) and in night
    mode (light ink on black).
    @param frame The detection box as a greyscale frame.
    @return Pixels whose grey value differs from the background by at least the obstacle contrast.
    """
    background = frame.background()
    table = bytes(1 if abs(value - background) >= constants.OBSTACLE_CONTRAST else 0 for value in range(256))
    return frame.pixels.translate(table).count(1)


def is_collision(frame: Frame) -> bool:
    """!
    @brief True when a cactus or a low bird is in the detection box, so the dinosaur must jump now.

    The name is the one the assignment uses for this check.
    @param frame The detection box as a greyscale frame.
    """
    return count_obstacle_pixels(frame) >= constants.MIN_OBSTACLE_PIXELS
