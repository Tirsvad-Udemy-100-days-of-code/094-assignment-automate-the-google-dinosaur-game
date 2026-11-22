"""!
@file constants.py
@brief Every constant of the dinosaur game bot, defined in one place.

Sizes in "game pixels" refer to the game canvas, which is 600 game pixels wide. On the screen the canvas is often
scaled; the bot measures the scale from the width of the ground line it finds.
"""

## Name of the program shown in help and in the log.
APP_TITLE: str = "Dino Bot"

## Address of the game the bot is written for. Any copy of the Chrome dinosaur game works.
GAME_URL: str = "https://elgoog.im/t-rex/"

## Width of the game canvas in game pixels.
GAME_WIDTH: int = 600

## Grey value (0 to 255) the game draws the dinosaur, the ground and the obstacles with (colour #535353).
INK_GREY: int = 83

## Grey value of the ink in night mode, where the game inverts its colours.
NIGHT_INK_GREY: int = 255 - INK_GREY

## How far a pixel may be from the ink grey and still count as ink when the ground line is searched.
INK_TOLERANCE: int = 40

## Fewest ink pixels a row must have to count as the ground line, in screen pixels.
MIN_GROUND_LINE_PIXELS: int = 300

## Right edge of the dinosaur, in game pixels from the left edge of the canvas.
DINO_RIGHT: float = 66.0

## Top of the detection box, in game pixels above the ground line. Birds that fly higher pass over the dinosaur.
BOX_TOP_ABOVE_GROUND: float = 36.0

## Bottom of the detection box, in game pixels above the ground line, so bumps in the ground are not seen.
BOX_BOTTOM_ABOVE_GROUND: float = 7.0

## Gap between the dinosaur and the near edge of the detection box, in game pixels.
BOX_NEAR_GAP: float = 4.0

## Distance from the dinosaur to the far edge of the detection box at the start speed, in game pixels.
START_LOOK_AHEAD: float = 75.0

## Speed of the game when it starts, in game pixels per frame.
START_SPEED: float = 6.0

## Highest speed of the game, in game pixels per frame.
MAX_SPEED: float = 13.0

## How much the speed grows each second (0.001 per frame at 60 frames per second).
SPEED_GAIN_PER_SECOND: float = 0.06

## Smallest grey difference from the background that counts as part of an obstacle.
OBSTACLE_CONTRAST: int = 60

## Fewest obstacle pixels in the detection box before the bot jumps; one pixel can be noise.
MIN_OBSTACLE_PIXELS: int = 3

## Seconds after a jump before the bot may jump again; a second press while in the air does nothing.
JUMP_COOLDOWN_SECONDS: float = 0.15

## Seconds to wait after the first press of the space bar, while the game widens its canvas; no obstacle comes yet.
START_ANIMATION_SECONDS: float = 1.0

## Seconds to wait between two looks at the screen. Zero looks as often as the screenshots allow.
POLL_INTERVAL_SECONDS: float = 0.0

## Seconds the command line waits before it starts, so the user can bring the game window to the front.
DEFAULT_COUNTDOWN_SECONDS: int = 3

## Key the bot presses to start the game and to jump.
JUMP_KEY: str = "space"

## Size of the browser window in headless mode, in pixels.
HEADLESS_VIEWPORT: tuple[int, int] = (1000, 600)

## Seconds the headless browser may take to load the game page.
HEADLESS_LOAD_TIMEOUT_SECONDS: float = 60.0
