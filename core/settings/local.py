import config
from .base import BASE_DIR

SECRET_KEY = config.SECRET_KEY

DEBUG = config.DEBUG

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.POSTGRES_DB,
        'USER': config.POSTGRES_USER,
        'PASSWORD': config.POSTGRES_PASSWORD,
        'HOST': config.POSTGRES_HOST,
        'PORT': config.POSTGRES_PORT,
    }
}

# CELERY
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visible_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://localhost:6379/1',
    }
}
