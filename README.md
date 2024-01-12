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
git clone https://github.com/esturide/esturide-backend.git
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

### Setting Up Your Development Environment

Before you start contributing, it's important to set up your development environment. This includes installing necessary tools and configuring pre-commit hooks to ensure code quality.

#### Pre-Commit Hooks

To maintain code quality and consistency, we use pre-commit hooks. Follow these steps to set up pre-commit hooks in your local development environment:

1. **Install Pre-Commit**:
   - Ensure you have Python installed on your system.
   - Install pre-commit globally using pip:
     ```
     pip install pre-commit
     ```

2. **Clone the Repository** (if not already done):
   ```
   git clone https://github.com/esturide/esturide-backend.git
   cd esturide-backend
   ```

3. **Set Up Pre-Commit Hooks**:
   - In the root directory of the cloned repository, run:
     ```
     pre-commit install
     ```
   - This will install the pre-commit hooks defined in the `.pre-commit-config.yaml` file into your local repository.

4. **Usage**:
   - Pre-commit hooks will now run automatically on the files you've staged whenever you commit.
   - You can manually run the hooks on all files in the repository at any time with:
     ```
     pre-commit run --all-files
     ```

### Creating a Pull Request with your changes

Now that you have done some changes and want to merge them in our repository, feel free to:

1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
2. Commit your Changes (`git commit -m "Add some AmazingFeature"`)
3. Push to the Branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request
