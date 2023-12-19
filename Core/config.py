from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')

PG_NAME=config('PG_NAME')
PG_USER=config('PG_USER')
PG_PASSWORD=config('PG_PASSWORD')
PG_HOST=config('PG_HOST')
PG_PORT=config('PG_PORT')