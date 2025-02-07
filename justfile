default:
  just --list

run *args:
  uv run uvicorn app.main:app --reload {{args}}

mm *args:
  uv run alembic revision --autogenerate -m "{{args}}"

migrate:
  uv run alembic upgrade head

downgrade *args:
  uv run alembic downgrade {{args}}

history:
  uv run alembic history

up:
  docker compose up -d

up-prod:
  docker compose -f docker-compose.prod.yml up --build -d

traefik:
  docker compose -f docker-compose.traefik.yml up --build -d

kill *args:
  docker compose kill {{args}}

build:
  docker compose build

ps:
  docker compose ps
