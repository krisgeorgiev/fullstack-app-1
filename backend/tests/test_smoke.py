from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_works():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "FastAPI is working!"}
