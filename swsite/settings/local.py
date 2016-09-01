from .base import *

DEBUG = True

MIDDLEWARE += [
    'apps.swu.middleware.middleware.StoreRequestsMiddleware',
]

DATABASE_ROUTERS = [
    'apps.swu.routers.LogRouter',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'log_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'log_db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'log_db': {
            'level': 'INFO',
            'class': 'apps.swu.handlers.DBHandler',
            'model': 'apps.swu.models.SpecialLog',
            'expiry': 86400,
            # 'formatter': 'verbose',
        },
        'signals_db': {
            'level': 'INFO',
            'class': 'apps.swu.handlers.DBHandler',
            'model': 'apps.swu.models.SignalLog',
        },
    },
    'loggers': {
        'apps.swu.middleware': {
            'handlers': ['log_db'],
            'level': 'INFO',
        },
        'apps.swu.models': {
            'handlers': ['signals_db'],
            'level': 'INFO',
        },
    },
}
