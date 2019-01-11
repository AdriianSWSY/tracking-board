from .base import *

import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration


DEBUG = False

SHOW_DOCS = os.getenv('SHOW_DOCS', False)

if SHOW_DOCS:
    INSTALLED_APPS += ('drf_yasg', )

ALLOWED_HOSTS = ['*']

sentry_sdk.init(dsn=os.environ['SENTRY_DSN'],
                integrations=[DjangoIntegration()])

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    'anymail',
)

EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'
ANYMAIL = {'SENDGRID_API_KEY': os.getenv('SENDGRID_API_KEY')}
