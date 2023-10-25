import RPi.GPIO as GPIO  # type:ignore
import spidev  # type:ignore

from .board import Board as IBoard


class Board(IBoard):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  # type: ignore -> Così posso utilizzare i numeri

        super().__init__(
            8,
            19,
            16,
            18,
            9,
            7,
            10,
            None,
            None,
            None,
            None,
        )

    # -------------------------------------------------------------------------------------------- #
    def pin(self, id: int | None, in_out: object = GPIO.OUT) -> None:  # type: ignore
        if id is not None:
            GPIO.setup(id, in_out, pull_up_down=GPIO.PUD_DOWN)  # type: ignore

    def spi(self) -> object:
        spi = spidev.SpiDev()  # type: ignore
        spi.open(0, 0)  # type: ignore
        spi.max_speed_hz = 5000000  # type: ignore

        return spi  # type: ignore

    def add_event(self, pin: int | None, callback: object) -> None:
        if pin is not None:
            self.pin(pin, GPIO.IN)  # type: ignore
            GPIO.add_event_detect(pin, GPIO.RISING, callback=callback)  # type: ignore

    # -------------------------------------------------------------------------------------------- #
    def _write(self, reg: int, value: list[int]) -> None:
        self.spi.xfer([reg | 0x80] + value)  # type: any

    def read(self, reg: int) -> int:
        return self.spi.xfer([reg] + [0])[1]  # type: ignore

    # TODO :METTERE QUEL pin_ss.lou() e high()

    def reads(self, reg: int, length: int) -> list[int]:
        return self.spi.xfer([reg] + [0] * length)[1:]  # type: ignore
