#!/bin/bash
rm -rf barbershopapi/migrations
rm db.sqlite3
python3 manage.py makemigrations barbershopapi
python3 manage.py migrate
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata barbers
python3 manage.py loaddata customers
python3 manage.py loaddata services
python3 manage.py loaddata appointments
python3 manage.py loaddata waitlist
python3 manage.py loaddata work_schedules