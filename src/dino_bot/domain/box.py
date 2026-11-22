"""!
@file box.py
@brief A rectangle on the screen, in pixels.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Box:
    """!
    @brief A rectangle in pixels. Left and top are inside the box; right and bottom are just outside it, the same
    convention Pillow uses for a bounding box.
    """

    ## Left edge, inside the box.
    left: int
    ## Top edge, inside the box.
    top: int
    ## Right edge, just outside the box.
    right: int
    ## Bottom edge, just outside the box.
    bottom: int

    def __post_init__(self) -> None:
        if self.right <= self.left or self.bottom <= self.top:
            raise ValueError(f"A box needs a positive size: {self}")

    @property
    def width(self) -> int:
        """!
        @brief Width of the box in pixels.
        """
        return self.right - self.left

    @property
    def height(self) -> int:
        """!
        @brief Height of the box in pixels.
        """
        return self.bottom - self.top

    def moved_by(self, dx: int, dy: int) -> Box:
        """!
        @brief The same box moved right by dx and down by dy pixels.
        """
        return Box(self.left + dx, self.top + dy, self.right + dx, self.bottom + dy)
