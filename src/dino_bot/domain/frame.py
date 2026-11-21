"""!
@file frame.py
@brief A greyscale screenshot as plain bytes, so the rules can be tested without a screen.
"""

from collections import Counter
from dataclasses import dataclass

from dino_bot.domain.box import Box


@dataclass(frozen=True, slots=True)
class Frame:
    """!
    @brief A greyscale picture: one byte per pixel (0 black, 255 white), row after row from the top left.
    """

    ## Width in pixels.
    width: int
    ## Height in pixels.
    height: int
    ## The grey values, width times height bytes.
    pixels: bytes

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError(f"A frame needs a positive size, got {self.width}x{self.height}")
        if len(self.pixels) != self.width * self.height:
            raise ValueError(f"A {self.width}x{self.height} frame needs {self.width * self.height} bytes")

    def row(self, y: int) -> bytes:
        """!
        @brief The grey values of one row.
        @param y Row number, 0 at the top.
        """
        start = y * self.width
        return self.pixels[start : start + self.width]

    def pixel(self, x: int, y: int) -> int:
        """!
        @brief The grey value of one pixel.
        """
        return self.pixels[y * self.width + x]

    def crop(self, box: Box) -> Frame:
        """!
        @brief The part of the frame inside the box.
        @throws ValueError When the box is not inside the frame.
        """
        if box.left < 0 or box.top < 0 or box.right > self.width or box.bottom > self.height:
            raise ValueError(f"{box} is not inside a {self.width}x{self.height} frame")
        rows = (self.row(y)[box.left : box.right] for y in range(box.top, box.bottom))
        return Frame(box.width, box.height, b"".join(rows))

    def background(self) -> int:
        """!
        @brief The most common grey value, taken as the background colour of the frame.
        """
        return Counter(self.pixels).most_common(1)[0][0]
