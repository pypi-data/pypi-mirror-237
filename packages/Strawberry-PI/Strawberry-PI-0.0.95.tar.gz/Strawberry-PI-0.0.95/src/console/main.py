from .Ansi import ANSI


def log(
    *values: object,
    sep: str | None = " ",
    end: str | None = f"{ANSI.RESET}\n",
):
    print(*values, sep=sep, end=end)


def info(
    *values: object,
    sep: str | None = " ",
    end: str | None = f"{ANSI.RESET}\n",
):
    print(ANSI.CYAN, sep="", end="")
    print(*values, sep=sep, end=end)


def error(
    *values: object,
    sep: str | None = " ",
    end: str | None = f"{ANSI.RESET}\n",
):
    print(ANSI.RED, sep="", end="")
    print(*values, sep=sep, end=end)


def ex(
    value: Exception,
    sep: str | None = " ",
    end: str | None = f"{ANSI.RESET}\n",
):
    print(ANSI.RED, sep="", end="")
    print(f"[{type(value)}] {value}", sep=sep, end=end)


def debug(
    *values: object,
    sep: str | None = " ",
    end: str | None = f"{ANSI.RESET}\n",
):
    print(ANSI.GREEN, sep="", end="")
    print(*values, sep=sep, end=end)
