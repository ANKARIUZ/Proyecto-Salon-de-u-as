import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

TEST_EMAIL = "testuser@correo.com"
TEST_PASSWORD = "123456"
FULL_NAME = "Test User"

def test_register_user():
    response = client.post("/api/v1/auth/register", json={
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD,
        "full_name": FULL_NAME
    })
    assert response.status_code in [200, 400]
    if response.status_code == 400:
        assert response.json()["detail"] == "Email ya registrado"

def test_login_and_get_token():
    response = client.post("/api/v1/auth/login", data={
        "username": TEST_EMAIL,
        "password": TEST_PASSWORD
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    return data["access_token"]

def test_get_current_user():
    token = test_login_and_get_token()
    response = client.get("/api/v1/auth/me", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == TEST_EMAIL
    assert data["full_name"] == FULL_NAME

def test_get_users_list():
    token = test_login_and_get_token()
    response = client.get("/api/v1/users/", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_by_id():
    token = test_login_and_get_token()
    response = client.get("/api/v1/users/", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0
    user_id = users[0]["id"]

    response = client.get(f"/api/v1/users/{user_id}", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    data = response.json()
    assert "email" in data
    assert "full_name" in data
