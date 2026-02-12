from datetime import datetime
import os
import logging
import logging.config

LOGGING_LEVEL = logging.DEBUG
LOGGING_FOLDER = "./logs"
LOGGING_FILENAME = f"self-logger.py_{datetime.now().strftime('%Y%m%d')}.log"
LOGGING_PATH = f'{LOGGING_FOLDER}/{LOGGING_FILENAME}'
LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            'format': '%(asctime)s [%(funcName)s|%(filename)s|l:%(lineno)s|%(levelname)s]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
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
            "level": logging.DEBUG,
            "filename": LOGGING_PATH,
            "formatter": "detail",
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
            "level": "DEBUG",
            "propagate": False,
        },
        "all_in_one_logger": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": False,
        }
    },
    # "disable_existing_loggers": True,
}

def main():
    # create folder if not exist
    if not os.path.exists(LOGGING_FOLDER):
        os.makedirs(LOGGING_FOLDER)

    # test
    logging.config.dictConfig(LOGGING_CONFIG)

    logger_all_in_one = logging.getLogger("all_in_one_logger")
    logger_all_in_one.debug('all_in_one_logger: debug message')
    logger_all_in_one.info('all_in_one_logger: info message')
    logger_all_in_one.warning('all_in_one_logger: warning message')
    logger_all_in_one.error('all_in_one_logger: error message')
    logger_all_in_one.critical('all_in_one_logger: critical message')

    logger_plain = logging.getLogger("console_plain_logger")
    logger_plain.debug('debug message')
    logger_plain.info('info message')
    logger_plain.warning('warning message')
    logger_plain.error('error message')
    logger_plain.critical('critical message')

    logger_console = logging.getLogger("console_logger")
    logger_console.debug('debug message')
    logger_console.info('info message')
    logger_console.warning('warning message')
    logger_console.error('error message')
    logger_console.critical('critical message')

    logger_file = logging.getLogger("file_logger")
    logger_file.error('file: error message')


if __name__ == '__main__':
    main()