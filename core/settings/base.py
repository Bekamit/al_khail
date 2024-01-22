"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import config
from .env_reader import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PRODUCTION = env('PRODUCTION', default=False, cast=bool)

ALLOWED_HOSTS = [
    # "http://localhost:5173",
    # "http://localhost:6379",
    # "http://localhost:8000",
    # "http://localhost:654",
    # "http://16.171.129.40",
    # "https://gulsdem.pp.ua",
    # "http://gulsdem.pp.ua",
    "*",
    # 'gulsdem.pp.ua',
    # 'localhost',
]

# Cors

CORS_ALLOWED_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_PRIVATE_NETWORK = True
CORS_ALLOWED_ALL_CREDENTIALS = True

# Application definition
THEME_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'drf_spectacular',
    'solo.apps.SoloAppConfig',
    'corsheaders',
    'debug_toolbar',
]
THEME = [
    'modeltranslation',
    'jazzmin',
]
APPS = [
    'apps.admin_app',
    'apps.appeal',
    'apps.city',
    'apps.company',
    'apps.estate',
    'apps.staticdata',
    'apps.project',
]
INSTALLED_APPS = [
    *THEME,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THEME_PARTY_APPS,
    *APPS,
]


# JAZZMIN

JAZZMIN_SETTINGS = {
    'site_title': 'Gulsdem Admin panel',
    'site_header': 'Gulsdem Admin panel',
    'site_brand': 'Gulsdem Admin panel',
    'show_sidebar': True,
    'navigation_expanded': False,
    'hide_models': [],
    'custom_css': None,
    'custom_js': None,
}

# CSRF
CSRF_USE_SESSIONS = True
CSRF_TRUSTED_ORIGINS = ['https://gulsdem.pp.ua',"http://localhost:6379/", "http://localhost:5173",]

# REST_FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DATETIME_FORMAT': '%d.%m.%Y %H:%M:%S',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

SPECTACULAR_SETTINGS = {
    # set 'COMPONENT_SPLIT_REQUEST' to 'True' will enable POST execute in swagger ui
    'COMPONENT_SPLIT_REQUEST': True,
    "TITLE": "Al-Khail API",
    "DESCRIPTION": "API for Al-Khail web service",
    "VERSION": "v1",
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'ar', 'tr', 'ru')
MODELTRANSLATION_TRANSLATION_REGISTRY = 'core.translation'

# STATIC (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'back_static/'
STATIC_ROOT = os.path.join(f'{BASE_DIR}', 'back_static')

# MEDIA (Images, PDF)

MEDIA_URL = '/back_media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'back_media')


# EMAIL
EMAIL_BACKEND = config.EMAIL_BACKEND
EMAIL_HOST = config.EMAIL_HOST
EMAIL_PORT = config.EMAIL_PORT
EMAIL_USE_TLS = config.EMAIL_USE_TLS
EMAIL_HOST_USER = config.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = config.EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = config.DEFAULT_FROM_EMAIL
SERVER_EMAIL = config.SERVER_EMAIL

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = 'tolomushev33@gmail.com'
# EMAIL_HOST_PASSWORD = 'ymiaghfkrwoelcgl'

# Redis
REDIS_HOST = 'redis'
REDIS_PORT = 6379



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'admin_app.CustomUser'
INTERNAL_IPS = ["127.0.0.1"]

if not PRODUCTION:
    from .local import *
else:
    from .prod import *
