from datetime import datetime
import os
import logging
import logging.config
import sys
from typing import Literal


LOGGER_TYPE = Literal[
    "file_console_logger", 
    "console_logger", 
    "console_plain_logger", 
    "console_custom_logger", 
    "file_logger"
    ]


class loggerSetup():
    def __init__(self,
                 logger_type: LOGGER_TYPE = "console_logger",
                 log_level_lowest: int = logging.INFO,
                 log_filename: str = f"{datetime.now().strftime('%Y%m%d')}.log",
                 log_folder: str = "./logs",
                 custom_log_format: str = "%(message)s",
                 ) -> None:
        self.logging_level_lowest = log_level_lowest
        self.logging_folder = log_folder
        self.logging_filename = log_filename
        self.logging_path = f'{self.logging_folder}/{self.logging_filename}'
        self.logging_config = {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "%(asctime)s [%(levelname)s|%(funcName)s|%(filename)s|l:%(lineno)s]: %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S"
                },
                "detail": {
                    "format": "%(asctime)s :: %(levelname)s :: %(funcName)s in %(filename)s (l:%(lineno)d) :: %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S"
                },
                "plain": {
                    "format": "%(message)s",
                },
                "custom_formatter": {
                    "format": custom_log_format,
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "level": self.logging_level_lowest,
                    "formatter": "default",
                },
                "console_plain": {
                    "class": "logging.StreamHandler",
                    "level": self.logging_level_lowest,
                    "formatter": "plain"
                },
                "console_detail": {
                    "class": "logging.StreamHandler",
                    "level": self.logging_level_lowest,
                    "formatter": "detail"
                },
                "file": {
                    "class": "logging.FileHandler",
                    "level": logging.DEBUG,
                    "filename": self.logging_path,
                    "formatter": "default",
                },
                "console_custom_format": {
                    "class": "logging.StreamHandler",
                    "level": self.logging_level_lowest,
                    "formatter": "custom_formatter",
                },
            },
            "loggers": {
                "console_logger": {
                    "handlers": ["console"],
                    "level": self.logging_level_lowest,
                    "propagate": False,
                },
                "console_plain_logger": {
                    "handlers": ["console_plain"],
                    "level": self.logging_level_lowest,
                    "propagate": False,
                },
                "console_custom_logger": {
                    "handlers": ["console_custom_format"],
                    "level": self.logging_level_lowest,
                    "propagate": False,
                },
                "file_logger": {
                    "handlers": ["file"],
                    "level": self.logging_level_lowest,
                    "propagate": False,
                },
                "file_console_logger": {
                    "handlers": ["file", "console"],
                    "level": self.logging_level_lowest,
                    "propagate": False,
                }
            },
            "disable_existing_loggers": True,
        }
        self.logger = self.initLogger(logger_type=logger_type)


    def setupExcepthookLogger(self, logger: logging.Logger):
        def handle_exception(exc_type, exc_value, exc_traceback):
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
                return
            logger.critical(
                "[SYSTEM]::Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback)
            )
        sys.excepthook = handle_exception


    def initLogger(self,
                   logger_type: str,
                   ):
        # create folder if not exist
        if not os.path.exists(self.logging_folder):
            os.makedirs(self.logging_folder)
        # test
        logging.config.dictConfig(self.logging_config)

        return logging.getLogger(logger_type)


    def getLogger(self) -> logging.Logger:
        return self.logger


def main():
    logger_setup = loggerSetup(
        logger_type="file_console_logger",
        log_level_lowest=logging.DEBUG,
    )
    logger = logger_setup.getLogger()

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

    test_logger_can_log_sys_excepthook


if __name__ == '__main__':
    main()

    ### output
    # $ venv/bin/python logger.py
    # 2023-11-06 23:40:45 [DEBUG|main|logger.py|l:144]: debug message
    # 2023-11-06 23:40:45 [INFO|main|logger.py|l:145]: info message
    # 2023-11-06 23:40:45 [WARNING|main|logger.py|l:146]: warning message
    # 2023-11-06 23:40:45 [ERROR|main|logger.py|l:147]: error message
    # 2023-11-06 23:40:45 [CRITICAL|main|logger.py|l:148]: critical message
    # Traceback (most recent call last):
    # File "/xxxxx/test-logging/logger.py", line 153, in <module>
    #     main()
    # File "/xxxxx/test-logging/logger.py", line 150, in main
    #     test_logger_can_log_sys_excepthook
    # NameError: name 'test_logger_can_log_sys_excepthook' is not defined