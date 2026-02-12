'''
https://cloud.tencent.com/developer/article/1772559
'''

#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
@CreateTime: 2020/12/29 14:08
@Author : shouke
'''

import datetime
import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            'format':'%(asctime)s %(filename)s %(lineno)s %(levelname)s %(message)s',
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
            "level":logging.INFO,
            "formatter": "plain"
        },
        "file":{
            "class": "logging.FileHandler",
            "level":20,
            "filename": f"./logs/test-logging-2.py-{datetime.datetime.now().date()}.log",
            "formatter": "default",
            "mode": "a",
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
        "file_logger":{
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False,
        },
        "all_in_one_logger":{
            "handlers": ["console", "file"],
            # "level": "INFO",
            "propagate": False,
        }
    },
    "disable_existing_loggers": True,
}

if __name__ == "__main__":
    # 运行测试
    logging.config.dictConfig(LOGGING_CONFIG)
    # logger = logging.getLogger("console_logger")
    logger = logging.getLogger("all_in_one_logger")
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warning message')
    logger.error('error message')
    logger.critical('critical message')

    test_error_message