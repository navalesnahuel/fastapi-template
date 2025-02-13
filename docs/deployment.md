## Deployment Guide

### Prerequisites

Before deploying the application, ensure you have:

*   A registered domain name pointing to your server's IP address.
*   Docker and Docker Compose installed on your server.
*   SSH access to your server with the necessary permissions for deployment.

### 1. Environment Configuration

1.  Create a `.env` file in your project's root directory *on your server*.
2.  Populate the `.env` file with the required environment variables. See the main `README.md` for a list of these variables and their descriptions. If using GitHub Actions for deployment, set these variables as secrets in your repository settings instead.
3.  Ensure all required variables are present and their values are correct for your production environment.

### 2. Building and Pushing the Docker Image

    ```
    DOCKERHUB_USERNAME=$(grep -oP '(?<=^DOCKERHUB_USERNAME=).*' .env) && \
    docker build --target production -t ${DOCKERHUB_USERNAME}/backend-api:latest . && \
    docker push ${DOCKERHUB_USERNAME}/backend-api:latest
    ```

### 3. Deploying the Application

Deploy using the production configuration:

    ```
    just prod
    ```

### 4. Scaling the Application

To scale your application, adjust the number of replicas in your `docker-compose.prod.yml` file and then redeploy:

1.  Edit `docker-compose.prod.yml` *on your server* and modify the `replicas` value within the `fastapi` service definition:

    ```yaml
    services:
      fastapi:
        deploy:
          replicas: 2  # Example: Scale to 2 replicas
    ```

2.  Redeploy the application to apply the scaling changes:
    ```
    just prod
    ```

This example scales the FastAPI service to 2 replicas. Adjust the `replicas` value as needed.  Remember to redeploy after making changes to the `docker-compose.prod.yml` file.
