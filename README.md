A simulated fullstack project **Frontend -> Backend API -> Database**
This project is a simulated fullstack application that I built as part of my DevOps learning journey.  
The goal was to connect a simple frontend with a backend API and persist data into a database, while practicing DevOps tools like Docker, CI/CD, and Ansible.

## Stack
- Frontend: HTML/CSS/JavaScript
- Backend: FastAPI (Python)
- Database: MongoDB
- DevOps: Docker, Docker Compose, GitHub Actions, Ansible

## Features
- CI/CD pipeline using GitHub Actions
- Containerized app with Docker
- MongoDB for backend data storage
- Simulated user interactions from frontend to backend to DB


From a DevOps perspective, the app is designed to be containerized and automated:
- The backend and database will run inside **Docker containers** with Docker Compose handling orchestration.
- I added a small **pytest smoke test** that verifies the backend starts correctly and responds as expected. Later this will be integrated into **GitHub Actions**, so tests run automatically on every commit.
- Eventually, I plan to use **Ansible** for provisioning and configuration, and extend the CI/CD pipeline for deployments.
