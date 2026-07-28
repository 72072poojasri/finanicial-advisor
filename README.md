# Financial Advisor Process Management API

A production-ready RESTful API built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication** for managing users, projects, and tasks. The application follows the **Repository Pattern**, **Service Layer Architecture**, and is fully containerized using **Docker**.

---

# Features

- JWT Authentication & Authorization
- Secure Password Hashing (Bcrypt)
- User Registration & Login
- User Profile API
- Project CRUD Operations
- Task CRUD Operations
- Project Ownership Authorization
- Repository Pattern
- Service Layer Architecture
- PostgreSQL Database
- SQLAlchemy ORM
- Docker & Docker Compose
- Swagger Documentation
- Automated Tests using Pytest

---

# Technology Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT (python-jose)
- Passlib (Bcrypt)
- Docker
- Docker Compose
- Pytest

---

# Project Structure

```
financial-advisor-api/
│
├── app/
│   ├── controllers/
│   ├── core/
│   ├── database/
│   ├── dependencies/
│   ├── exceptions/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── openapi.json
```

---

# Environment Variables

Create a `.env` file for local development.

Example:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/financial_advisor_db

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=financial_advisor_db

SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

For Docker, configure the values in `.env.docker`.

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd financial-advisor-api
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Locally

```bash
uvicorn app.main:app --reload
```

Application:

```
http://localhost:8000
```

---

# Run with Docker

```bash
docker compose up --build
```

---

# API Documentation

Swagger UI

```
http://localhost:8000/docs
```

OpenAPI Specification

```
http://localhost:8000/openapi.json
```

---

# Authentication

1. Register a user.
2. Login to receive a JWT access token.
3. Click **Authorize** in Swagger.
4. Use the generated token to access protected endpoints.

---

# API Endpoints

## Authentication

- POST `/api/auth/register`
- POST `/api/auth/login`

## Users

- GET `/api/users/me`

## Projects

- POST `/api/projects`
- GET `/api/projects`
- GET `/api/projects/{project_id}`
- PUT `/api/projects/{project_id}`
- DELETE `/api/projects/{project_id}`

## Tasks

- POST `/api/projects/{project_id}/tasks`
- GET `/api/projects/{project_id}/tasks`
- GET `/api/tasks/{task_id}`
- PUT `/api/tasks/{task_id}`
- DELETE `/api/tasks/{task_id}`

---

# Database Schema

```
User
│
├── id
├── email
├── password_hash
└── created_at
        │
        ▼
Project
│
├── id
├── name
├── description
├── owner_id
└── created_at
        │
        ▼
Task
│
├── id
├── title
├── description
├── status
├── priority
└── project_id
```

Relationships

- One User → Many Projects
- One Project → Many Tasks

---

# Running Tests

```bash
pytest
```

or

```bash
python -m pytest
```

---

# Docker Services

- API Service
- PostgreSQL Database
- Persistent Docker Volume
- Database Healthcheck

---

# Author

**Poojasri Kurru**