import sys

if sys.implementation.name == "micropython":
    from .board_pico import Board  # type: ignore
else:
    from .board_rpi import Board  # type: ignore
