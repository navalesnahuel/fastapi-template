## Development Guide

- Set environment variables at `.env`

- Run the application in development mode with `just dev`.

- Use `pytest` to execute test cases:
  ```bash
  uv run pytest
  ```
- Format and lint the code with Ruff:
  ```bash
  uv run ruff check .
  ```
- Apply Alembic migrations:
  ```bash
  uv run alembic upgrade head 
  ```
