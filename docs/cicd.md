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
