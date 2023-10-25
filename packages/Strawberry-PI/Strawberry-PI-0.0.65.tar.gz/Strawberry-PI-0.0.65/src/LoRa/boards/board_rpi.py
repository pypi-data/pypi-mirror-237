import RPi.GPIO as GPIO  # type:ignore
import spidev  # type:ignore

from .board import Board as IBoard


class Board(IBoard):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  #  Così posso utilizzare i numeri

        super().__init__(
            8,
            10,
            9,
            11,
            22,
            4,
            17,
            18,
            27,
            None,
            None,
        )

    # -------------------------------------------------------------------------------------------- #
    def pin(self, pin_id: int | None, in_out: object = GPIO.OUT) -> None:
        if pin_id is not None:
            GPIO.setup(pin_id, in_out, pull_up_down=GPIO.PUD_DOWN)

    def spi(self) -> object:
        spi = spidev.SpiDev()
        spi.open(0, 0)  # type: ignore
        spi.max_speed_hz = 5000000

        return spi  # type: ignore

    def add_event(self, pin: int | None, callback: object) -> None:
        if pin is not None:
            self.pin(pin, GPIO.IN)
            GPIO.add_event_detect(pin, GPIO.RISING, callback=callback)

    # -------------------------------------------------------------------------------------------- #
    def _write(self, reg: int, value: list[int]) -> None:
        self._spi.xfer([reg | 0x80] + value)

    def read(self, reg: int) -> int:
        return self._spi.xfer([reg] + [0])[1]

    def reads(self, reg: int, length: int) -> list[int]:
        return self._spi.xfer([reg] + [0] * length)[1:]
