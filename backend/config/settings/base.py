import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Packages:
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'corsheaders',
    'dj_rest_auth',
    'django_extensions',

    # Apps:
    'apps.core.apps.CoreConfig',
    'apps.users.apps.UsersConfig',
    'apps.board.apps.BoardConfig',
    'apps.columns.apps.ColumnsConfig',

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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (BASE_DIR / 'static',)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Celery

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')

# CORS HEADERS:

CORS_ORIGIN_ALLOW_ALL = True

# DOCS

SHOW_DOCS = True

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# User model config

AUTH_USER_MODEL = 'users.User'

# Django Admin settings

ADMIN_SITE_HEADER = os.getenv('ADMIN_SITE_HEADER', 'API Admin')

ADMIN_SITE_TITLE = os.getenv('ADMIN_SITE_TITLE', 'API Portal')

ADMIN_INDEX_TITLE = os.getenv('ADMIN_INDEX_TITLE', 'Welcome to API Admin')

ADMIN_SITE_URL = os.getenv('ADMIN_SITE_URL', 'http://localhost:8000/')

# Account Settings

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    # "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_LOGOUT_ON_GET = False

ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_USERNAME_REQUIRED = False

SITE_ID = 1

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Rest Auth Settings

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'apps.users.serializers.TokenCustomSerializer'
}
