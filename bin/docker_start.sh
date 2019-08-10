#!/bin/sh

echo "Apply database migrations"
python src/manage.py migrate

echo "Collect static files"
python src/manage.py collectstatic --no-input --clear

echo "Startup gunicorn"
gunicorn --chdir src --bind :8001 AllarmiWs.wsgi:application
