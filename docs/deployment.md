## Deployment Guide

### Prerequisites

Before deploying the application, ensure you have:

- A registered domain pointing to your server
- Docker and Docker Compose installed on your server
- Access to your server with necessary deployment permissions


### 1. Configure Environment

Set up your environment variables:

- Create the `.env` file in your project root (If using github actions, set them at secrets)
- Verify all required variables are present
- Update values according to your deployment environment

### 2. Build Docker Image

Build your application using Docker Compose:

```bash
docker build --target production -t ${DOCKERHUB_USERNAME}/backend-api:latest .

```

### 3. Push to Registry

Push the built image to your Docker registry:

```bash
docker push ${DOCKERHUB_USERNAME}/backend-api:latest
```

### 4. Deploy Application

Deploy using the production configuration:

```bash
just prod
```

### 5. Scaling Services

To scale your application services:

- Modify the `docker-compose.prod.yml` file to adjust replica count:

```yaml
services:
  fastapi:
    deploy:
      replicas: 2
```

- Apply the scaling changes:

```bash
just prod
```

This example scales the FastAPI service to 2 replicas.

