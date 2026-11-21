"""!
@file desktop_screen.py
@brief Screenshots of the desktop with Pillow's ImageGrab.
"""

from PIL import Image, ImageGrab

from dino_bot.domain.box import Box
from dino_bot.domain.frame import Frame


def frame_from_image(image: Image.Image) -> Frame:
    """!
    @brief Turn a Pillow image of any mode into a greyscale frame.
    """
    grey = image.convert("L")
    return Frame(grey.width, grey.height, grey.tobytes())


class DesktopScreen:
    """!
    @brief Takes screenshots of the primary screen with Pillow.
    """

    def take_screenshot(self, region: Box | None = None) -> Frame:
        """!
        @brief Take a greyscale screenshot of the screen or of a part of it.
        @param region The part of the screen to take, or None for all of it.
        """
        bbox = None if region is None else (region.left, region.top, region.right, region.bottom)
        return frame_from_image(ImageGrab.grab(bbox=bbox))
