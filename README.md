# DCelery

This project is a web application built with Django, Celery, Redis, and Celery Beat for scheduling tasks. The application is containerized with Docker, making setup and deployment easy.

## Features

- **Django** - A powerful Python web framework for rapid web development.
- **Celery** - A distributed task queue for handling background tasks asynchronously.
- **Redis** - An in-memory data structure store used as a message broker for Celery.
- **Celery Beat** - A scheduler for Celery to run tasks at regular intervals.
- **Docker** - Simplifies environment setup by using containers.
- **Docker Compose** - Orchestrates multiple services like Django, Celery, Redis, and Celery Beat.

## Prerequisites

Make sure you have Docker and Docker Compose installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to get the project up and running.

### 1. Clone the Repository

```bash
git clone https://github.com/sohan-me/dcelery
cd dcelery
```
## Run the Project

Once you've set up and built the project, follow these steps to run it and ensure everything is working as expected.

### 1. Start the Docker Containers

Use the following command to start all services in the background:

```bash
docker-compose up -d
```
