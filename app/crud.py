from sqlalchemy.orm import Session
from . import models, schemas

"""
CRUD operations for Task model.

This module handles database interactions.
Keeping database logic separate and ensures separation of concerns.
"""

def create_task(db: Session, task: schemas.TaskCreate):
    """
    Create a new task in the database.
    """
    db_task = models.Task(**task.model_dump())
    db.add(db_task) # Add ORM session
    db.commit()  # commit to database
    db.refresh(db_task) 
    return db_task


def get_task(db: Session, task_id: int):
    """
    Retrieve a task by its ID.
    Returns None if not found.
    """
    return db.query(models.Task).filter(models.Task.id == task_id).first() 


def get_tasks(db: Session):
    """
    Retrieve all tasks from the database.
    """
    return db.query(models.Task).all()


def update_task_status(db: Session, task_id: int, status: schemas.TaskStatus):
    """
    Update the status of a specific task.
    Returns updated task or None if not found.
    """
    task = get_task(db, task_id)
    if task:
        task.status = status
        db.commit()
        db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    """
    Delete a task by ID.
    Returns deleted task or None if task not found.
    """
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task