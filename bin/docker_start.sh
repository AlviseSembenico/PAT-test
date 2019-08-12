#!/bin/sh

db_host=${DB_HOST:-localhost}
db_user=${DB_USER:-admin}
db_password=${DB_PASSWORD:-pwd_admin}
db_port=${DB_PORT:-5432}

until PGPORT=$db_port PGPASSWORD=$db_password psql -h "$db_host" -U "$db_user" -c '\q'; do
  >&2 echo "Waiting for database connection..."
  sleep 1
done

echo "Apply database migrations"
python pat_test/manage.py migrate

echo "Collect static files"
python pat_test/manage.py collectstatic --no-input --clear

echo "Startup gunicorn"
gunicorn --chdir pat_test --bind :8000 pat_test.wsgi:application
