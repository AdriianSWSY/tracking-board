from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

RAVEN_CONFIG = {
    'dsn': os.environ['SENTRY_DSN'],
}

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    'anymail',
)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'
ANYMAIL = {'SENDGRID_API_KEY': os.getenv('SENDGRID_API_KEY')}
