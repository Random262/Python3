import logging
import string
import sys
from logging.handlers import TimedRotatingFileHandler


class AsciiFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        return all(char in string.printable for char in record.getMessage())


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
        }
    },
    'filters': {
        'ascii_filter': {
            '()': AsciiFilter
        }

    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'filters': ['ascii_filter'],
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
            'filters': ['ascii_filter'],
            'formatter': 'standard',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'calc_error.log',
            'filters': ['ascii_filter'],
            'formatter': 'standard',
        },
        'file_utils': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'utils.log',
            'filters': ['ascii_filter'],
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