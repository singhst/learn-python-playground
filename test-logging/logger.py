from datetime import datetime
import os
import logging
import logging.config

LOGGING_LEVEL = logging.DEBUG
LOGGING_FOLDER = "./logs"
LOGGING_FILENAME = f"{datetime.now().strftime('%Y%m%d')}.log"
LOGGING_PATH = f'{LOGGING_FOLDER}/{LOGGING_FILENAME}'
LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            'format': '%(asctime)s [%(filename)s|%(lineno)s|%(levelname)s]: %(message)s',
        },
        "detail": {
            'format': "%(asctime)s :: %(levelname)s :: %(funcName)s in %(filename)s (l:%(lineno)d) :: %(message)s",
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        "plain": {
            "format": "%(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
        },
        "console_plain": {
            "class": "logging.StreamHandler",
            "level": logging.INFO,
            "formatter": "plain"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": LOGGING_LEVEL,
            "filename": LOGGING_PATH,
            "formatter": "default",
        }
    },
    "loggers": {
        "console_logger": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "console_plain_logger": {
            "handlers": ["console_plain"],
            "level": "DEBUG",
            "propagate": False,
        },
        "file_logger": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False,
        }
    },
    "disable_existing_loggers": True,
}

if __name__=='__main__':
    # create folder if not exist
    if not os.path.exists(LOGGING_FOLDER):
        os.makedirs(LOGGING_FOLDER)

    # test
    logging.config.dictConfig(LOGGING_CONFIG)
    # logger = logging.getLogger("console_logger")
    # logger = logging.getLogger("console_plain_logger")
    logger = logging.getLogger("file_logger")


    logger.debug('debug message')
    logger.info('info message')
    # logger.warn('warning message')
    logger.error('error message')
    logger.critical('critical message')
