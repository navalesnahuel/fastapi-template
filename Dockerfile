# --- Base Image ---
FROM python:3.13.1-slim AS base

WORKDIR /app/

COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /uvx /bin/
RUN --mount=type=cache,target=/app/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_CACHE_DIR=/app/.cache/uv \
    PYTHONPATH=/app \
    PATH="/app/.venv/bin:$PATH" 

RUN mkdir -p /app/static/products

# --- Development ---
FROM base AS development

COPY ./pyproject.toml ./uv.lock ./alembic.ini ./logging.ini /app/
COPY ./entrypoints/uvicorn.sh /app/entrypoints/uvicorn.sh

ENTRYPOINT ["entrypoints/uvicorn.sh"]

# --- Production ---
FROM base AS production

ENV PROMETHEUS_MULTIPROC_DIR=/tmp/prometheus_multiproc_dir

COPY ./pyproject.toml /app/pyproject.toml
COPY ./uv.lock /app/uv.lock
COPY ./alembic.ini /app/alembic.ini
COPY ./logging_production.ini /app/logging_production.ini
COPY ./app /app/app
COPY ./alembic /app/alembic
COPY ./gunicorn/ /app/gunicorn
COPY ./entrypoints/gunicorn.sh /app/entrypoints/gunicorn.sh

RUN chmod +x /app/entrypoints/gunicorn.sh


# --- Add non-root user creation and switch at runtime ---
RUN groupadd --gid 1000 appgroup && \
    useradd --uid 1000 --gid appgroup appuser && \
    chown -R appuser:appgroup /app && \
    mkdir -p /logs && \
    chown -R appuser:appgroup /logs

USER appuser

ENTRYPOINT ["entrypoints/gunicorn.sh"]


