"""!
@file pictures.py
@brief Draws small greyscale pictures of the game for the tests, so no screen is needed.
"""

from dino_bot import constants
from dino_bot.domain.box import Box
from dino_bot.domain.frame import Frame

## Grey value of the background in day mode.
DAY_BACKGROUND = 255
## Grey value of the background in night mode, where the game inverts its colours.
NIGHT_BACKGROUND = 0


class Picture:
    """!
    @brief A greyscale canvas with a few drawing functions.
    """

    def __init__(self, width: int, height: int, background: int = DAY_BACKGROUND) -> None:
        self.width = width
        self.height = height
        self._pixels = bytearray([background]) * (width * height)

    def rect(self, left: int, top: int, right: int, bottom: int, grey: int) -> None:
        """!
        @brief Fill a rectangle; right and bottom are just outside it.
        """
        for y in range(top, bottom):
            start = y * self.width
            self._pixels[start + left : start + right] = bytes([grey]) * (right - left)

    def frame(self) -> Frame:
        """!
        @brief The picture as a frame.
        """
        return Frame(self.width, self.height, bytes(self._pixels))


def game_picture(
    scale: float = 1.0,
    night: bool = False,
    left: int = 100,
    ground_y: int = 400,
    width: int = 1500,
    height: int = 600,
) -> Picture:
    """!
    @brief A screenshot with the ground line of the game and nothing else.
    @param scale Screen pixels per game pixel.
    @param night True to draw light ink on a dark background.
    @param left Left end of the ground line.
    @param ground_y Row of the ground line.
    """
    background = NIGHT_BACKGROUND if night else DAY_BACKGROUND
    picture = Picture(width, height, background)
    picture.rect(left, ground_y, left + round(constants.GAME_WIDTH * scale), ground_y + 1, ink(night))
    return picture


def ink(night: bool) -> int:
    """!
    @brief The grey value the game draws with.
    """
    return constants.NIGHT_INK_GREY if night else constants.INK_GREY


def draw_cactus(
    picture: Picture, area_left: int, ground_y: int, scale: float, game_x: float, night: bool = False
) -> None:
    """!
    @brief Draw a cactus 17 game pixels wide and 35 high, standing on the ground line.
    @param game_x Distance of the cactus from the left end of the game, in game pixels.
    """
    left = area_left + round(game_x * scale)
    picture.rect(left, ground_y - round(35 * scale), left + round(17 * scale), ground_y, ink(night))


def zone(area_left: int, ground_y: int, scale: float, picture: Picture, elapsed: float = 0.0) -> Frame:
    """!
    @brief The picture inside the detection box of a game area.
    """
    from dino_bot.domain.game_area import GameArea

    area = GameArea(area_left, area_left + round(constants.GAME_WIDTH * scale), ground_y)
    box: Box = area.detection_box(elapsed)
    return picture.frame().crop(box)
