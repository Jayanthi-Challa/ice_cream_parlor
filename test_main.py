from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_seasonal_flavors():
    """
    Test the GET /seasonal_flavors/ endpoint.
    """
    response = client.get("/seasonal_flavors/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_seasonal_flavor():
    """
    Test the POST /seasonal_flavors/ endpoint.
    """
    response = client.post("/seasonal_flavors/", json={"name": "Mango"})
    assert response.status_code == 200
    assert response.json()["name"] == "Mango"
