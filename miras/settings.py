"""
Django settings for miras project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import environ
from corsheaders.defaults import default_methods, default_headers
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False),
    HTTPS_ENABLED=(bool, False),
    ALLOWED_HOSTS=(list, []),
    OTP_EXPIRY_SECONDS=(int, 60),
)
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nested_admin',
    'import_export',

    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'file_resubmit',
    'accounts',
    'courses',
    'enrollments',
    'part',
    'payments',
    'exams',
    'notes',
    'content',
    'contactus',
    'common',
    'django_celery_results',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miras.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(BASE_DIR / 'templates')],
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

WSGI_APPLICATION = 'miras.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db()
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# User model pointing to custom User model
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model

AUTH_USER_MODEL = 'accounts.User'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = env('STATIC_URL')
if DEBUG:
    STATICFILES_DIRS = [(BASE_DIR / "static")]
else:
    STATICFILES_ROOT = [(BASE_DIR / "static")]
STATIC_ROOT = (BASE_DIR / 'static-live')

# Media files
MEDIA_ROOT = (BASE_DIR / 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Setting up Django Rest Framework
# https://www.django-rest-framework.org/#installation
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

# Cors

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = list(default_methods) + []
CORS_ALLOW_HEADERS = list(default_headers) + [
    'Access-Control-Allow-Origin',
    'Access-Control-Allow-Headers',
]

APPEND_SLASH = True


# Email configuration
EMAIL_CONFIG = env.email_url(
    'EMAIL_URL', default='consolemail://test@example.com:password@localhost:25')
vars().update(EMAIL_CONFIG)
# Email configuration end

# simple jwt start
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=env.int('ACCESS_EXPIRY_TIME')),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=env.int('REFRESH_EXPIRY_TIME')),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

IMPORT_EXPORT_USE_TRANSACTIONS = True
# simple jwt end

# OTP settings
OTP_EXPIRY_SECONDS = env('OTP_EXPIRY_SECONDS')
OTP_SEND_URL = env(
    'OTP_SEND_URL', default='https://sms.aakashsms.com/sms/v3/send')
SMS_TOKEN = env('SMS_TOKEN', default='aakash')
# OTP settings end

# Frontend IP start
FRONTEND_URL = env('FRONTEND_URL', default='http://localhost:3000')
# Frontend IP end

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

SERVER_EMAIL = EMAIL_CONFIG['EMAIL_HOST_USER']
ADMINS = [('atharva', 'miras@atharvatech.io')]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    "file_resubmit": {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        "LOCATION": '/tmp/file_resubmit/'
    },
}


SWAGGER_SETTINGS = {
    'DEFAULT_API_URL': env("SWAGGER_DEFAULT_API_URL", default=None),
}
# Celery settings
# CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_BROKER_URL = 'amqp://localhost'
CELERY_BROKER_URL = 'amqp://rabbitmq'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kathmandu'

HTTPS_ENABLED = env('HTTPS_ENABLED')

if HTTPS_ENABLED:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
