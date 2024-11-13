from pathlib import Path
import os
from dotenv import load_dotenv
import json

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = json.loads(os.getenv('ALLOWED_HOSTS', '[]'))

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = json.loads(os.getenv('CORS_ALLOWED_ORIGINS', '[]'))

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = json.loads(os.getenv('CSRF_TRUSTED_ORIGINS', '[]'))

CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["*"]

AUTH_USER_MODEL = 'videoflix_app.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'videoflix_app',
    'rest_framework',
    'debug_toolbar',
    'django_rq',
    'import_export',
    'corsheaders',
    'rest_framework.authtoken',
]

IMPORT_EXPORT_USE_TRANSACTIONS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


#media settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'videoflix.urls'

CACHES = {    
       'default': {        
           'BACKEND': 'django_redis.cache.RedisCache',        
           'LOCATION': os.getenv('REDIS_URL'),        
           'OPTIONS': {   
               'PASSWORD': os.getenv('REDIS_PASSWORD'),        
               'CLIENT_CLASS': 'django_redis.client.DefaultClient'
           },        
           'KEY_PREFIX': 'videoflix'    
   }
}

CACHE_TTL = 60 * 15

INTERNAL_IPS = [
    '127.0.0.1',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'videoflix_app/templates'),],
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

WSGI_APPLICATION = 'videoflix.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.postgresql',
	'NAME': os.getenv('DATABASE_NAME'),
	'USER': os.getenv('DATABASE_USER'),
	'PASSWORD': os.getenv('DATABASE_PASSWORD'),
	'HOST': os.getenv('DATABASE_HOST'),
	'PORT': os.getenv('DATABASE_PORT'),
    'OPTIONS': {
        'client_encoding': 'UTF8',
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
DOMAIN_NAME = os.getenv('DOMAIN_NAME')

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

RQ_QUEUES = {
    'default': {
        'HOST': os.getenv('RQ_HOST'),
        'PORT': os.getenv('RQ_PORT'),
        'DB': 0,
        'PASSWORD': os.getenv('RQ_PASSWORD'),  
        'DEFAULT_TIMEOUT': 1000,  
    }
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}