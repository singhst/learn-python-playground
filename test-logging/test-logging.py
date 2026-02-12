'''
https://gist.github.com/gongzhitaao/0072e4df3533d282b5b3928447df7195

'''

import logging
import logging.config
from datetime import datetime
import os
import sys

LOG_LEVEL = 'DEBUG'
LOGFILE = './logs/test-logging.py-{0}.{1}.log'.format(
    os.path.basename(__file__),
    # datetime.now().strftime('%Y%m%dT%H%M%S')
    datetime.now().strftime('%Y%m%d')
    )

DEFAULT_LOGGING = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': 'simple :: %(levelname)s :: %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'DEBUG',
            'stream': sys.stdout,
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'level': 'INFO',
            'filename': LOGFILE,
            # 'mode': 'w',
            'mode': 'a',
        },
    },
    'loggers': {
        __name__: {
            'level': LOG_LEVEL,
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    }
}

if __name__ == "__main__":
    # logging.basicConfig(level=logging.ERROR)
    logging.config.dictConfig(DEFAULT_LOGGING)
    logger = logging.getLogger(__name__)

    logger.critical('================================')

    logger.debug('This is a debug-level message')
    logger.info('This is an info-level message')
    logger.warning('This is a warning-level message')
    logger.error('This is an error-level message')
    logger.critical('This is a critical-level message')

    test_error_message
