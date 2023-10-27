from logging import Logger, StreamHandler, Formatter
from .level_filter import LevelFilter
from .constants import DEBUG, INFO, WARNING, ERROR, CRITICAL, validate_loglevel, get_loglevel_int


class Log(Logger):
    MESSAGE_FORMAT: str = '%(name)s | %(asctime)s | %(levelname)s | %(filename)s | %(funcName)s() | %(message)s'
    DATETIME_FORMAT: str = '%Y.%m.%d %H:%M:%S'
    CAPITALIZE_NAME: bool = True

    def __init__(self, name: str, level: str = INFO, dev_mode: bool = False):  # TODO
        name = name.strip()
        if dev_mode:
            level = DEBUG
        if self.CAPITALIZE_NAME:
            name = name.upper()

        super().__init__(name=name.strip(), level=validate_loglevel(level=level))
        self.propagate = False

        stream_handler = StreamHandler()
        stream_handler.addFilter(LevelFilter(level=validate_loglevel(level=level)))
        stream_handler.setFormatter(Formatter(self.MESSAGE_FORMAT, datefmt=self.DATETIME_FORMAT))
        self.addHandler(stream_handler)

        self.debug(f'Started Logger (Name: {name}, Level: {level}).')

        # TODO: def suppress message (partly?)

        # TODO: def suppress logging():

        # TODO: def suppress_logger(cls, logger: Logger):
