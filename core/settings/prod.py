import config

SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '*',
]

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': config.POSTGRES_DB,
       'USER': config.POSTGRES_USER,
       'PASSWORD': config.POSTGRES_PASSWORD,
       'HOST': config.POSTGRES_HOST,
       'PORT': config.POSTGRES_PORT,
    }
}
