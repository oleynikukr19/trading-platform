from fastapi.testclient import TestClient
import pytest
from server.app.server import app


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client  # Return test client
