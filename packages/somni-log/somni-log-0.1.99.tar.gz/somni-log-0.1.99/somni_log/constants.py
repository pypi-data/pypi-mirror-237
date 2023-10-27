# Loglevels:
NOTSET: str = 'NOTSET'
DEBUG: str = 'DEBUG'
INFO: str = 'INFO'
WARNING: str = 'WARNING'
ERROR: str = 'ERROR'
CRITICAL: str = 'CRITICAL'
# Loglevel-Int:
NOTSET_INT: int = 0
DEBUG_INT: int = 10
INFO_INT: int = 20
WARNING_INT: int = 30
ERROR_INT: int = 40
CRITICAL_INT: int = 50


def validate_loglevel(level: str) -> str:
    level = level.upper().strip()
    valid_values: list[str] = [NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL]

    if level not in valid_values:
        raise Exception  # TODO: IllegalLevelValueError

    return level


def get_loglevel_int(level: str) -> int:
    valid_values: dict = {'NOTSET': NOTSET_INT,
                          'DEBUG': DEBUG_INT, 'INFO': INFO_INT,
                          'WARNING': WARNING_INT, 'ERROR': ERROR_INT, 'CRITICAL': CRITICAL_INT
                          }

    return valid_values[validate_loglevel(level)]
