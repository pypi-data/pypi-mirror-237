import sys

if sys.implementation.name == "micropython":
    from .board_pico import Board
else:
    from .board_rpi import Board  # type: ignore
