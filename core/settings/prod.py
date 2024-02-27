import config
from .base import BASE_DIR

SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

# DB
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config.POSTGRES_DB,
#         'USER': config.POSTGRES_USER,
#         'PASSWORD': config.POSTGRES_PASSWORD,
#         'HOST': config.POSTGRES_HOST,
#         'PORT': config.POSTGRES_PORT,
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
    }
}

# CSRF
CSRF_USE_SESSIONS = True
CSRF_TRUSTED_ORIGINS = ['http://209.38.228.54/',
			'http://209.38.228.54:80/',
                        "http://localhost:6379",
                        "http://localhost:5173",
                        'https://alkhail.pp.ua',
                        'http://localhost:8000']

# Celery

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visible_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Cors

CORS_ALLOW_ALL_ORIGINS = True
