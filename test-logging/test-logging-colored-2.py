'''
https://stackoverflow.com/questions/45465510/using-logging-with-coloredlogs
'''

import datetime
import logging.config
import os


LOGFILE = '/tmp/{0}.{1}.log'.format(
    os.path.basename(__file__),
    datetime.datetime.now().strftime('%Y%m%dT%H%M%S'))


my_logging_dict = {
    'version': 1,
    # set True to suppress existing loggers from other modules
    'disable_existing_loggers': True,
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
        },
    },
    'formatters': {
        'colored_console': {
            '()': 'coloredlogs.ColoredFormatter',
            'format': "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            'datefmt': '%H:%M:%S'
        },
        'format_for_file': {
            'format': "%(asctime)s :: %(levelname)s :: %(funcName)s in %(filename)s (l:%(lineno)d) :: %(message)s",
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'colored_console',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'format_for_file',
                'filename': LOGFILE,
                'maxBytes': 500000,
                'backupCount': 5
            }
        },
    }
}

logging.config.dictConfig(my_logging_dict)
logger = logging.getLogger(__name__)
