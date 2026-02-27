# DTS Challenge Backend – Python/FastAPI

## Overview

This project is a RESTful backend API built using **FastAPI**, designed to manage task resources with full CRUD functionality.

I Designed the backend follows a simple and clean, layered architecture with clear separation of concerns between routing, validation, database models, and dependency management. The goal was to build a structured, production ready API and automated test coverage.

### Separation of Concerns

- **main.py** → FastAPI application entry point
- **routers/** → API route definitions
- **schemas.py** → Pydantic models for validation and response
- **models.py** → SQLAlchemy ORM model for Tasks
- **database.py** → Database engine and session dependency

## Database Layer

- Built using **SQLAlchemy ORM**
- SQLite used for local development
- Dependency-injected database sessions
- Automatic table creation on application startup

## Validation Layer

- Uses **Pydantic v2**
- Request and response models enforce strict type validation

---

## Testing Strategy

Testing is implemented using:

- **Pytest**
- FastAPI `TestClient`
- Isolated test database
- 5 integration tests covering core CRUD operations

To run tests:

```bash
pytest
```

## Running backend locally

```bash
git clone <your-repo-url>
cd dts-challenge-backend-Python
```

## Create and Activate Virtual Environment

# MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

# Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Development server

```bash
uvicorn app.main:app --reload
```

# Swagger UI available at:

http://127.0.0.1:8000/docs

## Author

Luke Armstrong
