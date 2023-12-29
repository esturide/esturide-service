# ESTU-RIDE Backend Service

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

The ESTU-RIDE Backend Service, built using the modern, fast (high-performance) FastAPI framework, is designed to provide robust backend functionality for the ESTU-RIDE platform.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Commands](#docker-commands)
- [Contributing](#contributing)

## Introduction

This project encapsulates the backend service of ESTU-RIDE, offering high scalability, speed, and ease of use. FastAPI's elegant design and Docker's containerization ensure a seamless development and deployment experience.

## Installation

Ensure you have the latest versions of [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your system to work with containerization.

### Initial Setup

1. **Clone the Repository**:
```
git clone https://github.com/your-repo/esturide-backend.git
cd esturide-backend
```

2. **Install Docker**:
- Follow the instructions at [Docker's website](https://www.docker.com/get-started) to install Docker.

### To Run the Application

Execute the following command in the terminal:
```
docker-compose up --build
```

This command will build the Docker image if it doesn't exist and start the service.

## Usage

Once the application is running, visit the `/docs` endpoint (e.g., http://localhost:8000/docs) to view the Swagger UI documentation, which provides a detailed explanation of each endpoint and the ability to test them directly.

## Docker Commands

- `docker-compose up`: Starts the containers. If the image does not exist, Docker Compose automatically builds it using the `Dockerfile`.
- `docker-compose up --build`: Forces the build of the image even if it already exists and then starts the container. Useful when you have made changes to the `Dockerfile` or need to rebuild the image for any other reason.

## Contributing

Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
2. Commit your Changes (`git commit -m "Add some AmazingFeature"`)
3. Push to the Branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

