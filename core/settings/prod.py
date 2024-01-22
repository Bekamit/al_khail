import config

SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

ALLOWED_HOSTS = [
    "http://localhost:5173/",
    "http://localhost:6379/"
    "http://localhost:8000",
    "http://localhost:654"
    "http://16.171.129.40/",
    "https://gulsdem.pp.ua/",
    "http://gulsdem.pp.ua/",
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

# Celery

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visible_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


# Cors

CORS_ALLOWED_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_PRIVATE_NETWORK = True


# CORS_ALLOW_METHODS = (
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# )
#
# CORS_ALLOW_HEADERS = (
#     "accept",
#     "authorization",
#     "content-type",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
# )