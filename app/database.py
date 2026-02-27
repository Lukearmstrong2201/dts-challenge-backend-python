from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

"""
Database configuration.

This module is responsible for:
- Creating the database engine
- Managing database sessions
- Provides a Base class for SQLAlchemy models
"""

# SQLite database stored locally.
DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Each request will use its own database session.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all ORM models.
Base = declarative_base()

def get_db():
    """
    FastAPI dependency providing a database session
    - ensures it is closed after the request completes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()