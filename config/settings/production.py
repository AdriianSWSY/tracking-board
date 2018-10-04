from .base import *

DEBUG = False

SHOW_DOCS = False

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['*']

RAVEN_CONFIG = {
    'dsn': os.environ['SENTRY_DSN'],
}

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    'storages',
    'anymail',
)

EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'
ANYMAIL = {'SENDGRID_API_KEY': os.getenv('SENDGRID_API_KEY')}
