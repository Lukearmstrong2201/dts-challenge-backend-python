from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from sqlalchemy.orm import Session
from typing import List

from .database import Base, engine, get_db
from . import models, schemas, crud

app = FastAPI()

# Create database tables on startup
Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.
    """
    return crud.create_task(db, task)


@app.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse,
)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a task by ID.
    """
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return task


@app.get(
    "/tasks",
    response_model=List[schemas.TaskResponse],
)
def read_tasks(db: Session = Depends(get_db)):
    """
    Retrieve all tasks.
    """
    return crud.get_tasks(db)


@app.patch(
    "/tasks/{task_id}/status",
    response_model=schemas.TaskResponse,
)
def update_status(
    task_id: int,
    update: schemas.TaskUpdateStatus,
    db: Session = Depends(get_db),
):
    """
    Update the status of an existing task.
    """
    task = crud.update_task_status(db, task_id, update.status)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return task


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task by its ID.
    """
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return
    

