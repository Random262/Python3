import logging
import string
import sys
from logging.handlers import TimedRotatingFileHandler, HTTPHandler


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
        'http_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.HTTPHandler',
            'host': '127.0.0.1:3000',
            'url': '/log',
            'method': 'POST',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'app': {
            'handlers': ['console', 'file_debug', 'file_info', 'file_error', 'http_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'utils': {
            'handlers': ['file_utils', 'http_handler'],
            'level': 'INFO',
            'propagate': False
        }
    }
}