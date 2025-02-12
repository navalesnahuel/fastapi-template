## FastAPI Project Template
A modern, production-ready template for building APIs with FastAPI, featuring OAuth2 authentication, SQLModel ORM, and comprehensive testing.

## Features

- 🚀 FastAPI – High-performance, modern web framework for building APIs
- 🔐 OAuth2 Authentication – Secure login flow with Password and JWT token support
- 📚 SQLModel – Type-safe SQL database integration for Python
- 🐘 PostgreSQL – Robust, open-source relational database management system
- 🧪 Pytest – Powerful testing framework for test-driven development
- 🔍 Ruff – Lightning-fast Python linter for maintaining code quality
- 🐋 Docker – Simplified deployment with containerization
- ⚙️ GitHub Actions – Automated CI/CD pipeline for continuous integration and delivery
- ⚡ Async Endpoints – High-performance, non-blocking API endpoints
- 🔒 JWT Authentication – Secure, token-based authentication using OAuth2
- 📊 SQLModel Integration – Type-safe database queries with SQLModel
- 🔄 Alembic – Database schema migrations for version control
- 🧪 Comprehensive Testing – Full test suite with Pytest for ensuring app stability
- 📝 Custom Logging – Tailored logging configuration for effective debugging and monitoring
- 🔍 Sentry – Real-time error tracking and alerting integration
- 🛡️ Secure Docker Configuration – Best practices for secure and efficient containerized deployment
- 🔧 Code Quality – Code enforcement with Ruff for cleaner and maintainable code
- 📦 Fast Dependency Management – Streamlined project setup with uv for rapid development

---

## Prerequisites

- Python 3.11+
- `uv` package manager
- Docker and Docker Compose
- just *to run scripts faster*

---

## Project Structure

This project follows a modular approach, with separate directories for different components:

- **`app/`**: Contains the core application code
  - **`auth/`**: Handles user authentication, JWT tokens, and security-related services
  - **`config.py`**: Centralized configuration settings
  - **`database.py`**: Database setup and connections
  - **`models.py`**: SQLAlchemy and SQLModel ORM models
  - **`main.py`**: Entry point for the FastAPI application
  - **`routes.py`**: All endpoint route definitions
  - **`tests/`**: Test suite using pytest for unit and integration testing
- **`alembic/`**: Database migration scripts managed by Alembic

### Key Files:
- **`main.py`**: FastAPI app initialization and middleware configuration
- **`config.py`**: Configuration file for environment variables
- **`database.py`**: Database connection and session management
- **`models.py`**: All ORM models (with SQLModel)
- **`routes.py`**: API routes and endpoints
- **`scripts/`**: Custom scripts for deployment and maintenance tasks

---

## Fastest Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/fastapi-template.git
   cd fastapi-template
   ```

2. Set up the .env file:

<div align="center">

| Variable                   | Description                                      | Required |
|----------------------------|--------------------------------------------------|----------|
| `APP_VERSION`              | Version of the application                      | Yes      |
| `ENVIRONMENT`              | Environment the application is running in       | Yes      |
| `DATABASE_URL`             | Database connection string                      | Yes      |
| `CORS_HEADERS`             | Allowed headers for CORS requests               | No       |
| `CORS_ORIGINS`             | Allowed origins for CORS requests               | No       |
| `FIRST_SUPERUSER`          | Email for the first superuser                   | Yes      |
| `FIRST_SUPERUSER_PASSWORD` | Password for the first superuser                | Yes      |

</div>

3. Run the development script
   ```just dev```

---

## Development
Backend docs: [Development.md](./development.md).

## Deployment 
Backend docs: [Development.md](./deployment.md).

---

## License
The Full Stack FastAPI Template is licensed under the terms of the MIT license.
