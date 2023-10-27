from logging import log, debug, info, warning, error, critical
from .logger import Log
from .constants import NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL


def create_logger(name: str, level: str = INFO, dev_mode: bool = False) -> Log:  # TODO:
    return Log(name=name, level=level, dev_mode=dev_mode)
