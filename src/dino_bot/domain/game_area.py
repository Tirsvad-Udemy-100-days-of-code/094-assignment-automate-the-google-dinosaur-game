"""!
@file game_area.py
@brief Where the game is on the screen, found from its ground line, and where the bot looks for obstacles.
"""

from dataclasses import dataclass

from dino_bot import constants
from dino_bot.domain.box import Box
from dino_bot.domain.frame import Frame


class GameNotFoundError(LookupError):
    """!
    @brief No ground line of the game was found in the screenshot.
    """


@dataclass(frozen=True, slots=True)
class GameArea:
    """!
    @brief The game on the screen: the left and right end of its ground line and the row the line is on.
    """

    ## First pixel of the ground line, inside the game.
    left: int
    ## Just right of the last pixel of the ground line.
    right: int
    ## Row of the ground line.
    ground_y: int

    def __post_init__(self) -> None:
        if self.right <= self.left:
            raise ValueError(f"A game area needs a positive width: {self}")

    @property
    def scale(self) -> float:
        """!
        @brief Screen pixels per game pixel.
        """
        return (self.right - self.left) / constants.GAME_WIDTH

    def moved_by(self, dx: int, dy: int) -> GameArea:
        """!
        @brief The same area moved right by dx and down by dy pixels, for an area found in a part of the screen.
        """
        return GameArea(self.left + dx, self.right + dx, self.ground_y + dy)

    def detection_box(self, elapsed_seconds: float) -> Box:
        """!
        @brief The box in front of the dinosaur where an obstacle means "jump now".

        The box starts just in front of the dinosaur and reaches further ahead as the game speeds up, so the jump
        starts in time. An obstacle that is still close when the dinosaur lands makes it jump again.
        @param elapsed_seconds Seconds since the game started.
        @return The box in screen pixels.
        """
        left = self.left + (constants.DINO_RIGHT + constants.BOX_NEAR_GAP) * self.scale
        right = self.left + (constants.DINO_RIGHT + look_ahead(elapsed_seconds)) * self.scale
        top = self.ground_y - constants.BOX_TOP_ABOVE_GROUND * self.scale
        bottom = self.ground_y - constants.BOX_BOTTOM_ABOVE_GROUND * self.scale
        return Box(round(left), round(top), max(round(right), round(left) + 1), max(round(bottom), round(top) + 1))


def speed_at(elapsed_seconds: float) -> float:
    """!
    @brief The speed of the game after some seconds, in game pixels per frame.
    """
    speed = constants.START_SPEED + constants.SPEED_GAIN_PER_SECOND * max(elapsed_seconds, 0.0)
    return min(speed, constants.MAX_SPEED)


def look_ahead(elapsed_seconds: float) -> float:
    """!
    @brief How far in front of the dinosaur the detection box reaches, in game pixels. It grows with the speed.
    """
    return constants.START_LOOK_AHEAD * speed_at(elapsed_seconds) / constants.START_SPEED


def _ink_table() -> bytes:
    """!
    @brief A translation table that maps a grey value to 1 when it is the ink of the game (day or night) and to 0.
    """
    return bytes(
        1
        if abs(value - constants.INK_GREY) <= constants.INK_TOLERANCE
        or abs(value - constants.NIGHT_INK_GREY) <= constants.INK_TOLERANCE
        else 0
        for value in range(256)
    )


_INK = _ink_table()


def find_game_area(frame: Frame) -> GameArea:
    """!
    @brief Find the game in a screenshot: the row with the most ink pixels is the ground line.
    @param frame A greyscale screenshot that shows the game.
    @return The game area in the coordinates of the frame.
    @throws GameNotFoundError When no row has enough ink pixels to be the ground line.
    """
    best_y = -1
    best_count = 0
    for y in range(frame.height):
        count = frame.row(y).translate(_INK).count(1)
        if count > best_count:
            best_y, best_count = y, count
    if best_count < constants.MIN_GROUND_LINE_PIXELS:
        raise GameNotFoundError(
            f"No ground line found: the best row has {best_count} ink pixels, "
            f"{constants.MIN_GROUND_LINE_PIXELS} are needed. Is the game visible?"
        )
    marks = frame.row(best_y).translate(_INK)
    left = marks.index(1)
    right = marks.rindex(1) + 1
    return GameArea(left, right, best_y)
