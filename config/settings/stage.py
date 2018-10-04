from .base import *

DEBUG = False

SHOW_DOCS = os.getenv('SHOW_DOCS', False)

if SHOW_DOCS:
    INSTALLED_APPS += ('drf_yasg', )

ALLOWED_HOSTS = ['*']

RAVEN_CONFIG = {
    'dsn': os.environ['SENTRY_DSN'],
}

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    'anymail',
)

EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'
ANYMAIL = {'SENDGRID_API_KEY': os.getenv('SENDGRID_API_KEY')}
