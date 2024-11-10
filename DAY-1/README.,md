# Day 1: Containerization and Configuration

This document outlines the containerization of the Simple User Management Application. By containerizing the frontend, backend, and database components, the app becomes more portable and easier to deploy in different environments. The following instructions detail how to create Docker images for each component, set up networking between them, and manage configurations using Docker Compose.

---

## Dockerization

### Create Dockerfiles for Each Component

#### 1. Backend Dockerfile

The backend service is a Flask API. To containerize it.

#### 2. Frontend Dockerfile

To serve the static HTML frontend, you may use a lightweight web server like NGINX.

## Deployment Steps ##
1. Set Up Docker Compose

To simplify managing multiple services, use Docker Compose to define and run the frontend, backend, and database services in one configuration file.

2. Expose Environment Variables in Docker Compose

Environment variables are defined in docker-compose.yml for database credentials and connectivity, allowing the backend service to communicate with the database service. Using these environment variables ensures that each component can securely and correctly connect to the necessary services.

To start all services with Docker Compose:

docker-compose up -d


This completes Day 1 of the Simple User Management Application setup. The application is now containerized, making it easier to deploy, manage, and scale in a Dockerized environment.



