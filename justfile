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

development:
  docker compose up -d --build -p dev

production:
  docker compose -f docker-compose.prod.yml up -d --build -p prod

kill *args:
  docker compose kill {{args}}

build:
  docker compose build

ps:
  docker compose ps
