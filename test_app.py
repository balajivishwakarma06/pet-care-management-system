from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Pet Care Management System is running" in response.data


def test_get_pets():
    client = app.test_client()
    response = client.get("/pets")
    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_get_single_pet():
    client = app.test_client()
    response = client.get("/pets/1")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Bruno"


def test_pet_not_found():
    client = app.test_client()
    response = client.get("/pets/999")
    assert response.status_code == 404