import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

"""
Unit tests for Task API endpoints.
This does not touch the tasks.db but cretaes a test database
Overides dependency injection
Keeps tasks.db untouched
"""

# Use separate SQLite test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db # Forces  endpoints to user 'override_get_db' instead of 'get_db' 

client = TestClient(app) # Used to Simulate a HTTP Client

#---------------------------------------------------
def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "status": "pending",
            "due_date": "2026-12-31T12:00:00"
        },
    )

    assert response.status_code == 201
    data = response.json() # Convert response body to a python dictionary
    assert data["title"] == "Test Task"
    assert data["status"] == "pending"
    assert "id" in data

#---------------------------------------------------

def test_get_all_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


#---------------------------------------------------

def test_get_task_by_id():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Another Task",
            "description": None,
            "status": "pending",
            "due_date": "2026-12-31T12:00:00"
        },
    )

    task_id = create_response.json()["id"] # obtain id from response

    response = client.get(f"/tasks/{task_id}") #id is inserted into test endpoint
    assert response.status_code == 200
    assert response.json()["id"] == task_id

#---------------------------------------------------

def test_update_task_status():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Status Task",
            "description": None,
            "status": "pending",
            "due_date": "2026-12-31T12:00:00"
        },
    )

    task_id = create_response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}/status",
        json={"status": "completed"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "completed"

#---------------------------------------------------

def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Delete Task",
            "description": None,
            "status": "pending",
            "due_date": "2026-12-31T12:00:00"
        },
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404