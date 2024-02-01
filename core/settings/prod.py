import config

SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

WORK_APPS = [
    'corsheaders',
]

MIDDLEWARE_APPS = [
    'corsheaders.middleware.CorsMiddleware',
]

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config.POSTGRES_DB,
       'USER': config.POSTGRES_USER,
       'PASSWORD': config.POSTGRES_PASSWORD,
       'HOST': config.POSTGRES_HOST,
       'PORT': config.POSTGRES_PORT,
    }
}

# CSRF
CSRF_USE_SESSIONS = True
CSRF_TRUSTED_ORIGINS = ['https://gulsdem.pp.ua',
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
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_PRIVATE_NETWORK = True
CORS_ALLOWED_ALL_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
