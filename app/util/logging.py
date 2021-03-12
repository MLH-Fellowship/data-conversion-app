import logging
from sys import stdout

LOGGING_NAME = 'cvtr'
DEFAULT_LEVEL = logging.INFO

logger = logging.getLogger(LOGGING_NAME)


def set_up_logger(level=DEFAULT_LEVEL, enable_file_log=False):
    # type: (int, bool) -> None
    '''Set up logging
    '''
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s: [ %(levelname)8s ] %(message)s')

    # Console Handler
    console_handler = logging.StreamHandler(stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    if enable_file_log:
        file_handler = logging.FileHandler('log')
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

