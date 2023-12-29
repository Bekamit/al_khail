import os
from pathlib import Path
import config

SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '*',
]

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
   # 'default': {
   #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #     'NAME': config.PG_NAME,
   #     'USER': config.PG_USER,
   #     'PASSWORD': config.PG_PASSWORD,
   #     'HOST': config.PG_HOST,
   #     'PORT': config.PG_PORT,
   #  }

}
