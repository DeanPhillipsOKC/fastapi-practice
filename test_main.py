from fastapi.testclient import TestClient
from main import app
import os


client = TestClient(app)

def test_get_all_blogs():
    response = client.get("/blog/all")
    assert response.status_code == 200

def test_auth_error():
    response = client.post("/token",
                           data={"username": "", "password": ""})
    access_token = response.json().get("access_token")
    assert access_token == None
    message = response.json().get("detail")
    assert message == "Invalid credentials"

def test_auth_success():
    response = client.post("/token",
                           data={"username": os.getenv("TEST_USER_USERNAME"), "password": os.getenv("TEST_USER_PASSWORD")})
    access_token = response.json().get("access_token")
    assert access_token != None

def _get_access_token():
    response = client.post("/token",
                           data={"username": os.getenv("TEST_USER_USERNAME"), "password": os.getenv("TEST_USER_PASSWORD")})
    access_token = response.json().get("access_token")
    return access_token

def test_post_article():
    access_token = _get_access_token()

    response = client.post(
        "/article/",
        json={
            'title': 'Test article',
            'content': 'Test content',
            'published': True,
            "creator_id": 1
        },
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200
    assert response.json().get("title") == "Test article"