import os
import sys
from pathlib import Path
from django.utils import timezone
from corsheaders.defaults import default_headers


def get_list(text):
    return [t.strip() for t in text.split(',') if t.strip()]


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-2$mtn02e)(*z77=n@$rb!+)13^*+mk!^aox@*#de7p92snp2+0')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', 'True') == 'True')

ALLOWED_HOSTS = get_list(os.environ.get('ALLOWED_HOSTS', '*'))


# Application definition

INSTALLED_APPS = [
    'django.contrib.gis',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework_simplejwt',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'safedelete',
    'drf_yasg',
    'parler',
    'rosetta',


    'apps.base',
    'apps.user',
    'apps.leads',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'core.middlewares.languages.AdminLanguageMiddleware', # custom language middleware
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# custom user model
AUTH_USER_MODEL = "user.User"

AUTHENTICATION_BACKENDS = [
    'api.core.auth_backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
        "TEST": {
            "NAME": os.environ.get('TEST_DB_NAME', 'test_dev_db'),
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# django-rest-framework-simplejwt configurations
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timezone.timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timezone.timedelta(days=2),
    'APP_ACCESS_TOKEN_LIFETIME': timezone.timedelta(days=15),
    'APP_REFRESH_TOKEN_LIFETIME': timezone.timedelta(days=180),
    'AGENT_REFRESH_TOKEN_LIFETIME': timezone.timedelta(days=7),
    "APP_ENERGO_TOKEN_LIFETIME": timezone.timedelta(days=365),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
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
    "TOKEN_OBTAIN_SERIALIZER": "users.api.serializers.CustomTokenObtainPairSerializer",

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timezone.timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timezone.timedelta(days=2),
}

# rest-framework configuration
REST_FRAMEWORK = {
    # 'DATE_INPUT_FORMATS': [ISO_8601, '%d.%m.%Y'],
    'DEFAULT_PERMISSION_CLASSES': [
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'drf_excel.renderers.XLSXRenderer',
    ),
    # 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_THROTTLE_RATES': {
        "authentication": "100/hour",
        "verify_authentication": "100/hour",
        "create_two_step_password_authentication": "100/hour",
        "verify_two_step_password_authentication": "100/hour",
    },
    "DATE_INPUT_FORMATS": ["%d-%m-%Y", "%Y-%m-%d"],
    'DATETIME_FORMAT': '%d-%m-%Y %H:%M:%S',
    'DATE_FORMAT': '%d-%m-%Y',
    'NON_FIELD_ERRORS_KEY': 'message',
    'EXCEPTION_HANDLER': 'api.core.exceptions.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'api.core.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
}

# cors settings

CORS_ALLOW_ALL_ORIGINS = (os.environ.get('CORS_ALLOW_ALL_ORIGINS', 'True') == 'True')
CORS_ALL_ORIGINS_ALLOW = (os.environ.get('CORS_ALL_ORIGINS_ALLOW', 'True') == 'True')
CORS_ALLOW_CREDENTIALS = (os.environ.get('CORS_ALLOW_CREDENTIALS', 'True') == 'True')
CORS_ORIGIN_ALLOW_ALL = (os.environ.get('CORS_ORIGIN_ALLOW_ALL', 'True') == 'True')
CORS_ALLOWED_ORIGINS = get_list(os.environ.get('CORS_ALLOWED_ORIGINS', ''))
CSRF_TRUSTED_ORIGINS = get_list(os.environ.get('CSRF_TRUSTED_ORIGINS', ''))

CORS_ALLOW_HEADERS = default_headers + (
    'cache-control',
)

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "Content-Disposition"
]

CORS_ORIGIN_WHITELIST = (
    os.environ.get('UI_DOMAIN', 'http://127.0.0.1:8000'),
)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Russian'),
    ('uz-latin', 'Uzbek (Latin)'),
    ('uz-cyrillic', 'Ўзбек (Кирил)'),
    ('en', 'English'),
)

PARLER_LANGUAGES = {
    None: (
        {'code': 'ru'},
        {'code': 'uz-latin'},
        {'code': 'uz-cyrillic'},
        {'code': 'en'},
    ),
    'default': {
        'fallback': 'ru',
        'hide_untranslated': False,
    }
}

PARLER_ENABLE_CACHING=True

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True
USE_L10N = True

USE_TZ = False

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
]

MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_FILE_TYPES = get_list(os.environ.get('ALLOWED_FILE_TYPES', "doc,pdf,docx,xlsx"))

ALLOWED_IMAGE_TYPES = get_list(os.environ.get('ALLOWED_IMAGE_TYPES', "jpeg,jpg,png,svg"))

MAX_IMAGE_UPLOAD_SIZE = int(os.environ.get('MAX_IMAGE_UPLOAD_SIZE', 52428800))  # 50MB

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BACKEND_DOMAIN = os.environ.get('BACKEND_DOMAIN', '127.0.0.1:8000')

#qr_code url
QR_CODE_URL = os.environ.get('QR_CODE_URL', '')
# OTP code expiration time in seconds
EXPIRY_TIME_OTP = int(os.environ.get('EXPIRY_TIME_OTP', 300))

# eskiz credentials
ESKIZ_EMAIL = os.environ.get('ESKIZ_EMAIL', default='')
ESKIZ_PASSWORD = os.environ.get('ESKIZ_PASSWORD', default='')



### email credentials
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = os.environ.get('EMAIL_PORT', default=587)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', default=True)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', default='')
RECIPIENT_ADDRESS = os.environ.get('RECIPIENT_ADDRESS', default='')
SUPPORT_EMAIL = os.environ.get('SUPPORT_EMAIL', default='')
ARM_ADMIN_KEY = os.environ.get('ARM_ADMIN_KEY', default='')
### celery configuration
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://127.0.0.1:6379/0")
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

### redis configuration
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')




### cache configuration
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": [
            os.environ.get('CACHES_LOCATION', 'redis://127.0.0.1:6379/1'),
        ]
    }
}


### basic logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["default"]},
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        },
        "verbose": {
            "format": (
                "%(levelname)s %(name)s %(message)s [PID:%(process)d:%(threadName)s]"
            )
        },
        "json": {
            "format": '{"timestamp": "%(asctime)s", "level": "%(levelname)s", '
                      '"name": "%(name)s", "message": "%(message)s", '
                      '"process": %(process)d, "thread": "%(threadName)s"}',
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose" if DEBUG else "json",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server" if DEBUG else "json",
        },
    },
    "loggers": {
        "django": {"level": "INFO", "propagate": True},
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
        "core": {"level": "DEBUG", "propagate": True},
    },
}
#if os.name == 'nt':
#    GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal309'
#    import platform
#    OSGEO4W = r"C:\OSGeo4W"
#    # if '64' in platform.architecture()[0]:
#    #     OSGEO4W += "64"
#    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
#    os.environ['OSGEO4W_ROOT'] = OSGEO4W
#    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
#    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
#    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']
# else:
#     GDAL_LIBRARY_PATH = '/usr/gdal31/lib/libgdal.so.27'
