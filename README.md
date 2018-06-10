# Django Empty Skeleton

## Features:

- Pipenv as enviroment
- celery + redis, django-rest-framework from box
- MailTrap (dev) and SendGrid (production) mail settings
- Auto generated schemas Swagger/OpenAPI 2.0 for you project
- Abstaract User and User Manager
- Login/Logout, Password Change, Forgot Request and Forgot Confirm


## Quick Start:

0) Create `.env` file with you enviriment variables, example:
```
export DATABASE_URL=postgres://postgres:@localhost/db

export CELERY_BROKER_URL=redis://localhost

export MAILTRAP_EMAIL_HOST_USER=user

export MAILTRAP_EMAIL_HOST_PASSWORD=pass

export URL_FRONT_RESET_PASSWORD=http://localhost:8000/reset-password/
```

1) Install Pipenv
```
    pip install pipenv
```

2) Activate Pipenv
```
    pipenv shell
```

3) Install dev package
```
    pipenv install --dev
```

4) Django start
```
    pipenv run migrate
    pipenv run collectstatic
    pipenv run runserver
```

5) Celery Start (optional)
```
    pipenv run celery
```

6) *Startapp*
