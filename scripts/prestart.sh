set -e

# Let the DB start
uv run python -m app.scripts.backend_pre_start

# Alembic upgrade
uv run alembic upgrade head

# Create initial data in DB
uv run python -m app.scripts.initial_data
