#!/bin/sh
set -e

# Run Django management commands
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

# Start the server
python manage.py runserver 0.0.0.0:8000
