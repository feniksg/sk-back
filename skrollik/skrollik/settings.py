import os

from datetime import timezone, timedelta

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-$g6i1shhy5#sk2d*p+uwm$*u@36m=#4v&ub$v%q7yx2p-r%okc'

DEBUG = True

ALLOWED_HOSTS = ['*']

MAIN_DOMAIN = "sava.meurl.ru"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'corsheaders',
    'drf_yasg',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

SESSION_MIDDLEWARE_TOKEN = [
    'django.contrib.sessions.middleware.SessionMiddleware',
]

CSRF_TRUSTED_ORIGINS = [
    f'http://{MAIN_DOMAIN}', 
    f'https://{MAIN_DOMAIN}', 
    f'http://www.{MAIN_DOMAIN}', 
    f'https://www.{MAIN_DOMAIN}',
]

CSRF_ALLOWED = [
    f'http://{MAIN_DOMAIN}', 
    f'https://{MAIN_DOMAIN}', 
    f'http://www.{MAIN_DOMAIN}', 
    f'https://www.{MAIN_DOMAIN}',
    'http://localhost:3000'
    ]

# CORS_ALLOWED_ORIGINS = [
#         "http://localhost:3000",
#         "http://127.0.0.1:8000",
#         f'https://{MAIN_DOMAIN}',
#         f'http://{MAIN_DOMAIN}',
#     ]

#region 

ROOT_URLCONF = 'skrollik.urls'

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

WSGI_APPLICATION = 'skrollik.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db/db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

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

AUTH_USER_MODEL = "api.CustomUser"

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ],
}

#endregion

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


#region


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

TZ_MOSCOW = timezone(timedelta(hours=3))

REST_SESSION_LOGIN = False
SECURE_REFERRER_POLICY = "strict-origin"

STATIC_URL = 'api/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#endregion