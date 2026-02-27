from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum

"""
Pydantic schemas for request validation and response.

This schemas defines:
- What data the API accepts
- How data is validated
- What the API returns
"""

class TaskStatus(str, Enum):
    """
    Enumeration of valid task statuses, ensuring only predefined values are accepted.
    """
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskBase(BaseModel):
    """
    Shared task fields.
    """
    title: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None
    status: TaskStatus
    due_date: datetime


class TaskCreate(TaskBase):
    """
    Schema used when creating a task.
    """
    pass


class TaskUpdateStatus(BaseModel):
    """
    Schema used when updating only the task status.
    """
    status: TaskStatus


class TaskResponse(TaskBase):
    """
    Schema returned in API response.
    """
    id: int
    created_at: datetime

    class Config:
        from_attributes = True 