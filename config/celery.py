from __future__ import absolute_import
import os

import sentry_sdk

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from sentry_sdk.integrations.celery import CeleryIntegration


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

sentry_sdk.init(integrations=[CeleryIntegration()])

app = Celery(__name__)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

TASK_SERIALIZER = 'json'
ACCEPT_CONTENT = ['json']

app.conf.update(
    BROKER_URL=settings.CELERY_BROKER_URL,
    # CELERY_IMPORTS=(
    #     'apps.chats.tasks',
    # ),
    # CELERYBEAT_SCHEDULE={
    #     "close_open_chat_after_limit_hours": {
    #         "task": "apps.chats.tasks.close_open_chat_after_limit_hours",
    #         "schedule": crontab(hour='0'),
    #         "args": (72, )
    #     },
    # },
)
