from __future__ import absolute_import
import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

app = Celery('gorilla')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

TASK_SERIALIZER = 'json'
ACCEPT_CONTENT = ['json']

app.conf.update(
    BROKER_URL=settings.CELERY_BROKER_URL,
    # CELERYBEAT_SCHEDULE={
    #     "some_task": {
    #         "task": " module.tasks.function",
    #         "schedule": timedelta(seconds=10),
    #         "args": ()
    #     },
    # },
)