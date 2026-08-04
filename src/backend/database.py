"""
database.py
Creates the PostgreSQL database connection using SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from src.backend.config import DATABASE_URL


# Create database engine
engine = create_engine(
    DATABASE_URL,
    echo=True
)

# Create session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for ORM models
Base = declarative_base()


def get_db():

    #Creates a database session.
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()