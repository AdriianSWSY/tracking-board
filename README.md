# DJANGO PROJECT TEMPLATE

## Technologies
 - Python 3.9.6
 - Poetry 1.1.6
 - Django 3.2.4
 - DRF 3.12.4
 - gunicorn 20.1.0
 - Docker 20.10.7
 - Docker Compose 1.29.2
 - Postgres 13.3
 - NGINX 1.21.0
 
## QUICKSTART
 - install "Docker" and "Docker Compose"
 - create and fill dev.env or prod.env with .env.template 
 - docker-compose <dev/prod/stage file> up -d --build
    - for dev version add "-f docker-compose.dev.yml" after "docker-compose"
    - go into backend container and run ./manage.py migrate

## TIPS
 - use /docker catalog for nginx, redis, and so on...