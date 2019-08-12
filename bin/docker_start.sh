#!/bin/sh

echo "Apply database migrations"
python pat_test/manage.py migrate

echo "Collect static files"
python pat_test/manage.py collectstatic --no-input --clear

echo "Startup gunicorn"
gunicorn --chdir pat_test --bind :8000 pat_test.wsgi:application
python manage.py collectstatic --no-input --clear