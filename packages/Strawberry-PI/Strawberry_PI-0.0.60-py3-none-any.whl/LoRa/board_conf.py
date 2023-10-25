import sys

if sys.implementation.name == "micropython":
    from .boards.board_pico import Board  # type: ignore
else:
    from .boards.board_rpi import Board  # type: ignore
