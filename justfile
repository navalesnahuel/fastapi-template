default:
  just --list

mm *args:
  env DATABASE_URL=postgresql://app:app@localhost:5432/app uv run alembic revision --autogenerate -m "{{args}}"

migrate:
  env DATABASE_URL=postgresql://app:app@localhost:5432/app uv run alembic upgrade head

downgrade *args:
  env DATABASE_URL=postgresql://app:app@localhost:5432/app uv run alembic downgrade {{args}}

history:
  env DATABASE_URL=postgresql://app:app@localhost:5432/app uv run alembic history

dev:
  docker compose up -d --build 

prod:
  docker compose -f docker-compose.prod.yml up -d  --build

kill *args:
  docker compose kill {{args}}

build:
  docker compose build

ps:
  docker compose ps

test:
  uv run pytest

