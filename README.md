

## Getting Started

These instructions will help you run a copy of the project on your local machine for development and testing.

### Prerequisites

Install the following tools:

- Docker
- Docker Compose

### Installation and Launch

1. **Cloning the repository**:
    ```
    
    ```

2. **Navigate to the project directory**:
    ```
    cd lead_management
    ```

3. **Create `.env` files using examples**:
    ```
    cat example.env > .env
    ```

4. **Run Docker Compose**:
    ```
    docker-compose up --build
    ```

### API Documentation

Access the Swagger documentation for API details at:

```
http://127.0.0.1:8000/redoc/
```

```
http://127.0.0.1:8000/swagger/
```

# Project Structure

This document outlines the structure of the Django project.

## Directory Structure

```

├── README.md # This file
├── docker-compose.yaml # Docker Compose configuration for development
├── Dockerfile # Dockerfile for the main server
├── requirements.txt # Python dependencies
├── .env # Environment variables
├── config # Main Django project folder
│ ├── settings.py # Import Base class here
│ └── ...
├── api/ # Django project api (deprecated)
│ ├── v1/ # api version control
├── apps/ # Django project apps
│ ├── user/ # User management app
│ ├── base/ # Manage soft deletion and default fields
│ │ ├── apps.py
│ │ ├── models.py # Base class imported here
│ │ └── ...
│ ├── leads/ # Manage leads


......
```

## Notes

- The `api/` directory is deprecated and should be replaced by the `apps/` directory.
- The `apps/` directory contains the core Django apps for user management, booking, and football field management.
- The `base/` app handles soft deletion and default fields for other apps.

Feel free to update this structure as your project evolves.
