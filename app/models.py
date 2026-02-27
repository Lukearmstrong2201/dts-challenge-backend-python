from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

"""
Database models for the task application.

This module defines SQLAlchemy ORM models that map
to database tables.

Validation is performed at schema level.
"""

class Task(Base):
    """
    Task model representing a task.

    Fields:
    - id: Primary key (Auto increments)
    - title: title of the task (required)
    - description: detailed description (Optional)
    - status: Current state of the task
    - due_date: Deadline for completion
    - created_at: Timestamp when task was created
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False, default="pending")
    due_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)