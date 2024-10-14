from fastapi.testclient import TestClient

from app.main import root

client = TestClient(root)


def test_hello_world():
    response = client.get("/")

    assert response.status_code == 200
