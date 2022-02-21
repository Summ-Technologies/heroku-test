#!/bin/sh
export FLASK_APP=/app/app.py 
exec flask run --port=${PORT} --host="0.0.0.0"