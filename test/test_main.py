from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_read_main():
    response = app.get("/")
    assert response.status_code == "200"