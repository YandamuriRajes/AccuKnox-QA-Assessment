# QA Automation Setup

This repository contains the automation setup for QA testing, including deployment configurations and an automated test script.

## Prerequisites

- Minikube or Kind installed
- Kubectl installed
- Docker installed
- Python 3.x installed
- pip installed

## Cloning the Repository

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/Vengatesh-m/qa-test.git
   cd qa-test
   ```
Docker Deployment
First, we need to build and run our Docker containers for both the frontend and backend services.

Step 1: Build Docker images:
docker build -t backend:latest -f Dockerfile.backend .
docker build -t frontend:latest -f Dockerfile.frontend .

Step 2: Run Docker containers:
docker run -d -p 8080:8080 backend:latest
docker run -d -p 3000:3000 frontend:latest

Step 3: Verify that the containers are running:
docker ps

## Starting the Kubernetes Cluster

1. Start Minikube or Kind:
   - For Minikube:
     ```bash
     minikube start
     ```
   - For Kind:
     ```bash
     kind create cluster
     ```

## Deploying the Services

1. Deploy the backend service:

   ```bash
   kubectl apply -f backend-deployment.yaml
   ```

2. Deploy the frontend service:
   ```bash
   kubectl apply -f frontend-deployment.yaml
   ```

## Verifying the Deployment

1. Ensure the frontend and backend pods are running:
   ```bash
   kubectl get pods
   ```

## Accessing the Frontend Service

1. Get the URL of the frontend service (for Minikube):

   ```bash
   minikube service frontend --url
   ```

   Open the URL in your browser and ensure it displays the greeting message fetched from the backend service.

## Automated Testing

### Prerequisites

- Python 3.x installed
- pip installed

### Setup

1. Navigate to the project directory:

   ```bash
   cd qa-test
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

1. Before running `selenium_test.py`, update the port number on line 18 in the script.

   ```bash
   python3 selenium_test.py
   ```

## Project Structure

- `backend-deployment.yaml` - Kubernetes deployment file for the backend service.
- `frontend-deployment.yaml` - Kubernetes deployment file for the frontend service.
- `requirements.txt` - Python dependencies for the automation script.
- `selenium_test.py` - Selenium test script for automated testing.

## Deliverables

- Public GitHub repository containing:
  - The project codebase
  - Test script for automated testing
  - README file with setup and execution instructions

---
