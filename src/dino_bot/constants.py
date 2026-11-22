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

## Key the bot presses to start the game and to jump.
JUMP_KEY: str = "space"
