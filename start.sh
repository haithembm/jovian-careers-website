#!/bin/bash
python3 manage.py migrate --run-syncdb 2>/dev/null || true
exec python3 manage.py runserver 0.0.0.0:5000
