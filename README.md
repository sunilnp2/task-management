# Task Management System API

This Django REST Framework (DRF) project manages a task of user with task created, update and delete.
with complete unit testing of models, serializer, and views.

# Features
1. User Authentication: Users can register, log in, and manage tasks only if authenticated.
2. Task Management: CRUD (Create, Read, Update, Delete) operations for tasks.
3. Task Permissions: Users can only manage their own tasks.
4. Task Status and Difficulty Levels: Tasks can be marked as "Open," "In Progress," or "Done," with difficulties categorized as "Easy," "Medium," or "Hard."
5. Dockerized Setup: Run the project seamlessly in a Docker container.
6. Documentation and Unit Testing: Detailed API documentation and unit tests to ensure robust functionality.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Documentation](#api-documentation)
  - [Endpoint 1: Get Own tasks](#http://localhost:8000/api/tasks/)
  - [Endpoint 2: Create Task](#http://localhost:8000/api/tasks/)
  - [Endpoint 3: Retrieve Task](#http://localhost:8000/api/tasks/id)
  - [Endpoint 3: Update Task](#http://localhost:8000/api/tasks/id)
  - [Endpoint 1: Delete Task](#http://localhost:8000/api/tasks/id)


## Getting Started

### Prerequisites

Ensure you have the following installed on your machine(system):

- Docker
- Docker Compose

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sunilnp2/task-management.git
   cd task-management  
   
2. Set Up Environment Variables

    in .env file add credentials following variables:

    ```bash
   
   # Create Database First 
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres_db_name
    DB_USER=dB_user
    DB_PASSWORD=db_password
    DB_HOST=db
    DB_PORT=5432

3. Run Docker Compose

    ```bash
    docker-compose up --build
    
    This command will build and start the containers, including the web server and PostgreSQL database.

4. Run Migrations
    ```bash
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate


5. Create a Superuser (Admin)
 
   ```bash
    docker-compose exec web python manage.py createsuperuser
   
    email:- test@gmail.com
    pw:- test123

6. Access the API:

    The API will be accessible at http://localhost:8000


## API Documentation

### API Endpoint: Retrieve a list of own tasks

- **URL:** `http://localhost:8000//api/tasks/`
- **Method:** GET
- **Authentication:** Session Auth
- **Data:**

  ```json
  [
    {
        "id": 2,
        "title": "First Task",
        "description": "First task",
        "created_by": {
            "id": 1,
            "username": "admin",
            "first_name": "",
            "last_name": "",
            "email": "admin@email.com"
        },
        "difficulty": "easy",
        "status": "open",
        "created_at": "2024-11-01T11:54:30.934916Z",
        "updated_at": "2024-11-01T11:54:30.934925Z"
    }
  ]

### API Endpoint: Create a new task

- **URL:** `http://localhost:8000/api/tasks/`
- **Method:** POST
- **Authentication:** Session Auth
- **Data:**

  ```json
  {
    "title": "First Task",
    "description": "task desc",
    "difficulty": easy,
    "status": open
}

### API Endpoint: Get All User

- **URL:** `http://localhost:8000/auth/api/getalluser/`
- **Method:** Get
- **Authentication:** No Auth

### API Endpoint: Retrieve Specific Task

- **URL:** `http://localhost:8000/auth//api/tasks/id/`
- **Method:** Get
- **Authentication:** Session Auth

### API Endpoint: Update Task

- **URL:** `http://localhost:8000/auth//api/tasks/id/`
- **Method:** PUT
- **Authentication:** Session Auth
- **Data:**

  ```json
   {
    "status": completed
  }

Status updated

### API Endpoint: Delete Own Task

- **URL:** `http://localhost:8000/auth//api/tasks/id/`
- **Method:** Delete
- **Authentication:** Session Auth


# Running Tests
```bash
docker-compose exec web python manage.py test









