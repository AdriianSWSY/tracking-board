import os
import sys
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
           os.path.dirname(os.path.abspath(__file__))))

sys.path.append(os.path.join(BASE_DIR, 'apps'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5m(c)mr$cg)sif_0!3%(y=!1^l@fgu&r9!)+6z63$!34i^1981'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

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
    'phonenumber_field',
    'rest_auth',

    # Apps:
    'apps.core.apps.CoreConfig',
    'apps.users.apps.UsersConfig'

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

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/gorilla'),
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')

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

ADMIN_SITE_HEADER = 'Gorilla API Admin'

ADMIN_SITE_TITLE = 'Gorilla API Portal'

ADMIN_INDEX_TITLE = 'Welcome to Gorilla API Admin'

# Account Settings

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    # "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_USERNAME_REQUIRED = False

SITE_ID = 1

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'users.serializers.PasswordResetCustomSerializer',
}

# Email Settings

DEFAULT_FROM_EMAIL = 'noreply@gorilla.com'

URL_FRONT_RESET_PASSWORD = os.getenv('URL_FRONT_RESET_PASSWORD')

# Rest Framework Settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
