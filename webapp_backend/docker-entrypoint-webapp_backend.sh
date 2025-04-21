#!/bin/bash

echo "Apply database migrations"
alembic upgrade head >&1

echo "Starting Backend"
uvicorn webapp_backend.webapp:app --host ${BACKEND_HOST} --port ${BACKEND_PORT} --reload