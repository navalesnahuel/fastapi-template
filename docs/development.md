## Development Guide

### 1. Environment Variables

Set up your development environment variables in a `.env` file in the project root.  See the main `README.md` for a list of required variables and their descriptions.

### 2. Running the Application

Run the application in development mode:

    ```bash
    just dev
    ```

### 3. Running Tests
Execute test cases using `pytest`:
    
    ```bash
    uv run pytest
    ```

### 4. Code Formatting and Linting
Format and lint the code using `Ruff`:

    ``` bash
    uv run ruff check .
    ```


### 5. Database Migrations
Apply Alembic migrations:

    ```bash
    just migrate
    ```

### Check every justfile commnand
Commands to handle migrations and docker containers:

    ```bash
    just -l
    ```
