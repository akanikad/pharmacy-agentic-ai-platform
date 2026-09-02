from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_assist():
    response = client.post(
        "/v1/assist",
        json={"message": "What documentation is needed for prior authorization?"}
    )
    assert response.status_code == 200
    assert "answer" in response.json()
