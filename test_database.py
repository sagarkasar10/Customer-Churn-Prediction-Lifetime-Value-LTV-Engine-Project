from src.backend.database import SessionLocal
from sqlalchemy import text

def test_database_connection():

    db = SessionLocal()

    try:
        result = db.execute(text("SELECT 1"))
        assert result.scalar() == 1

    finally:
        db.close()


def test_session_close():

    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))
    finally:
        db.close()

    assert db.is_active is True