#!/bin/sh

# modified by mjuric:
exec gunicorn app.main:app -w 4 --threads 4 -k uvicorn.workers.UvicornH11Worker --access-logfile -

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

exec uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"
# gunicorn example:app -w 4 -k uvicorn.workers.UvicornWorker
