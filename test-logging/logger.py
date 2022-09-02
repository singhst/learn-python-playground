from datetime import datetime
import os
import logging
import logging.config


class loggerSetup():
    def __init__(self,
                 log_level: int = logging.INFO,
                 log_filename: str = f"{datetime.now().strftime('%Y%m%d')}.log",
                 log_folder: str = "./logs",
                 log_format: str = "%(message)s",
                 ) -> None:
        self.logging_level = log_level
        self.logging_folder = log_folder
        self.logging_filename = log_filename
        self.logging_path = f'{self.logging_folder}/{self.logging_filename}'
        self.logging_config = {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "%(asctime)s [%(funcName)s|%(filename)s|l:%(lineno)s|%(levelname)s]: %(message)s",
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
                    "format": log_format,
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "level": self.logging_level,
                    "formatter": "default",
                },
                "console_plain": {
                    "class": "logging.StreamHandler",
                    "level": self.logging_level,
                    "formatter": "plain"
                },
                # "file": {
                #     "class": "logging.FileHandler",
                #     "level": self.logging_level,
                #     "filename": self.logging_path,
                #     "formatter": "detail",
                # },
                "custom_handler": {
                    "class": "logging.StreamHandler",
                    "level": self.logging_level,
                    "formatter": "custom_formatter",
                },
            },
            "loggers": {
                "console_logger": {
                    "handlers": ["console"],
                    "level": self.logging_level,
                    "propagate": False,
                },
                "console_plain_logger": {
                    "handlers": ["console_plain"],
                    "level": self.logging_level,
                    "propagate": False,
                },
                # "file_logger": {
                #     "handlers": ["file"],
                #     "level": self.logging_level,
                #     "propagate": False,
                # },
                "custom_logger": {
                    "handlers": ["custom_handler"],
                    "level": self.logging_level,
                    "propagate": False,
                }
            },
            "disable_existing_loggers": True,
        }

    def get_logger(self,
                   logger_type: str = "console_logger",
                   ):
        # create folder if not exist
        if not os.path.exists(self.logging_folder):
            os.makedirs(self.logging_folder)
        # test
        logging.config.dictConfig(self.logging_config)

        return logging.getLogger(logger_type)


if __name__ == '__main__':
    logger_setup = loggerSetup(log_level=20)  # 10 debug
    # logger = logger_setup.get_logger('console_logger')
    logger = logger_setup.get_logger('console_plain_logger')

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
