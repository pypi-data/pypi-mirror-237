from logging import Filter
from .constants import get_loglevel_int


class LevelFilter(Filter):  # TODO: Docstring
    """
    https://stackoverflow.com/a/7447596/190597 (robert)
    """
    level = None

    def __init__(self, level: str | int):  # TODO: Docstring
        if isinstance(level, str):
            self.level = get_loglevel_int(level)
        elif isinstance(level, int):
            self.level = level

    def filter(self, record):  # TODO: Docstring
        return record.levelno >= self.level
