#! /bin/bash

python manage.py makemigrations --settings=src.settings.prod --no-input

python manage.py migrate --settings=src.settings.prod --no-input

python manage.py collectstatic --settings=src.settings.prod --no-input

exec gunicorn --env DJANGO_SETTINGS_MODULE=src.settings.prod src.wsgi:application -b 0.0.0.0:8080 --reload