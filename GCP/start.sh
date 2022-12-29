#!/bin/bash

source ../venv/bin/activate
python manage.py makemigrations user
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8001