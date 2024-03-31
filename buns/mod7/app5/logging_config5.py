import logging
import sys
from logging.handlers import TimedRotatingFileHandler

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'standard'
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'calc_debug.log',
            'formatter': 'standard',
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'calc_info.log',
            'formatter': 'standard',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'calc_error.log',
            'formatter': 'standard',
        },
        'file_utils': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'utils.log',
            'formatter': 'standard',
            'when': 'H',
            'interval': 10,
            'backupCount': 1
        },
    },
    'loggers': {
        'app': {
            'handlers': ['console', 'file_debug', 'file_info', 'file_error'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'utils': {
            'handlers': ['file_utils'],
            'level': 'INFO',
            'propagate': False
        }
    }
}