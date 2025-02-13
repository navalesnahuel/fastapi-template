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

- **Python 3.11+**
- `uv` package manager
- **Docker and Docker Compose**
- just (to run scripts faster)

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


## Setup Guide

1. Clone the Repository

```bash
git clone https://github.com/your-repo/fastapi-template.git
cd fastapi-template
```

2. Set Up the `.env` File

<div align="center">

| Variable                   | Description                               | Dev Required | Deploy Required |
|---------------------------|-------------------------------------------|--------------|-----------------|
| `APP_VERSION`             | Version of the application                | Yes          | Yes             |
| `ENVIRONMENT`             | Environment the application is running in  | Yes          | No              |
| `DATABASE_URL`            | Database connection string                | Yes          | Yes             |
| `CORS_HEADERS`            | Allowed headers for CORS requests         | No           | No              |
| `CORS_ORIGINS`            | Allowed origins for CORS requests         | No           | No              |
| `FIRST_SUPERUSER`         | Email for the first superuser            | Yes          | Yes             |
| `FIRST_SUPERUSER_PASSWORD`| Password for the first superuser         | Yes          | Yes |
| `DOCKERHUB_USERNAME`      | Docker Hub username (for deployment)      | No           | Yes (Using CI/CD)             |
| `DOCKERHUB_TOKEN`         | Docker Hub authentication token          | No           | Yes             |
| `VIRTUAL_HOST`                    | Primary domain for the application       | No           | Yes             |
| `LETSENCRYPT_HOST`        | Domain for SSL certificate generation         | No           | Yes             |
| `LETSENCRYPT_EMAIL`       | Email for SSL certificates              | No           | Yes             |

</div>

3. Run the Application

### Development Guide

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

---

### Deployment Guide

#### Prerequisites

Before deploying the application, ensure you have:

- A registered domain pointing to your server
- Docker and Docker Compose installed on your server
- Access to your server with necessary deployment permissions

1. Build Docker Image

Build your application using Docker Compose:

```bash
docker build --target production -t ${DOCKERHUB_USERNAME}/myapp:latest .

```

2. Push to Registry

Push the built image to your Docker registry:

```bash
docker push ${DOCKERHUB_USERNAME}/backend-api:latest
```

3. Configure Environment

Set up your environment variables:

    Locate the `.env` file in your project root
    Verify all required variables are present
    Update values according to your deployment environment

4. Deploy Application

Deploy using the production configuration:

```bash
just prod
```

#### Maintenance and Scaling

##### Updating the Application

To update your deployment with the latest changes:

```bash
# Pull the latest image
docker-compose -f docker-compose.prod.yml pull

# Restart containers with new image
just prod
```

##### Scaling Services

To scale your application services:

1. Modify the `docker-compose.prod.yml` file to adjust replica count:

```yaml
services:
  fastapi:
    deploy:
      replicas: 2
```

2. Apply the scaling changes:

```bash
docker-compose -f docker-compose.prod.yml up -d --scale fastapi=2
```

This example scales the FastAPI service to 2 replicas.

---

## CI/CD Pipeline Setup Guide

### Overview

The CI/CD pipeline currently handles:
1. Testing
2. Linting
3. Building and pushing Docker images

The deployment step has been removed from the default pipeline since deployment targets vary by user. This guide will help you configure your own deployment step.

### Current Pipeline Structure

```yaml
jobs:
  test:    # Runs tests with PostgreSQL service
  lint:    # Checks code quality
  build:   # Builds and pushes Docker image
```

### Adding Your Deployment Step

To add deployment to your infrastructure, create a new job after the build step. Here's a template you can modify:

```yaml
  deploy:
    needs: [build]
    runs-on: ubuntu-20.04
    if: github.event_name == 'push'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4.2.2

      # Add your deployment steps here
```

### Testing Your Deployment

1. Add your deployment configuration to `.github/workflows/ci-cd.yml`
2. Set up required secrets in your GitHub repository
3. Push to main branch to trigger the pipeline
4. Monitor the Actions tab for deployment status

--- 

## License
The Full Stack FastAPI Template is licensed under the terms of the MIT license.

---

## Acknowledgements
This repository incorporates code and ideas from the following open-source projects:

- [FastAPI Production Template](https://github.com/zhanymkanov/fastapi_production_template)
- [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template)

A big thanks to the contributors of these repositories for providing foundational code that made this project possible.
