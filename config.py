from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')

POSTGRES_DB = config('PG_NAME')
POSTGRES_USER = config('PG_USER')
POSTGRES_PASSWORD = config('PG_PASSWORD')
POSTGRES_HOST = config('PG_HOST')
POSTGRES_PORT = config('PG_PORT', cast=int)

# EMAIL

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = config('SERVER_EMAIL')

# CELERY

CELERY_BROKER_URL = config('CELERY_BROKER_URL')
CELERY_BROKER_TRANSPORT_OPTIONS = config('CELERY_BROKER_TRANSPORT_OPTIONS')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = config('CELERY_ACCEPT_CONTENT')
CELERY_TASK_SERIALIZER = config('CELERY_TASK_SERIALIZER')
CELERY_RESULT_SERIALIZER = config('CELERY_RESULT_SERIALIZER')

# REDIS