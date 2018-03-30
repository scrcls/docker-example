# -*- coding:utf-8 -*-
import os
BASE_DIR = '/home/test/var/log'

APP_LOGGING_FILE = os.path.join(BASE_DIR, 'app.log')
SYSTEM_LOGGING_FILE = os.path.join(BASE_DIR, 'system.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detail': {
            'format': '%(asctime)s %(pathname)s/[line:%(lineno)d] %(levelname)s\n\t%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'complex': {
            'format': '%(asctime)s %(module)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'system_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'detail',
            'filename': SYSTEM_LOGGING_FILE,
            'level': 'DEBUG',
        },
        'app_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'complex',
            'filename': APP_LOGGING_FILE,
            'level': 'DEBUG',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['system_handler'],
            'propagate': False,
            'level': 'ERROR',
        },
        'app': {
            'handlers': ['app_handler'],
            'propagate': False,
            'level': 'DEBUG',
        }
    },
    'root': {
        'handlers': ['app_handler'],
        'level': 'ERROR',
    }
}
