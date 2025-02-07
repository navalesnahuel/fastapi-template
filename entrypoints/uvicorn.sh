#! /usr/bin/env bash

set -e
set -x

# Let the DB start
uv run python -m app.scripts.backend_pre_start

uv run alembic upgrade head

# Create initial data in DB
uv run python -m app.scripts.initial_data

uvicorn app.main:app --host 0.0.0.0 --reload --log-config logging.ini
