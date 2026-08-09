import pytest
from fastapi.testclient import TestClient

from src.backend.main import app


@pytest.fixture(scope="session")
def client():
    """
    Creates a FastAPI TestClient
    """
    with TestClient(app) as client:
        yield client