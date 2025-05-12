form fastapi.testclient import TestClient
from app.main import app

client =TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={
        "title": "Test Task",
        "description": "This is a test task",
        "due_date": "2025-05-20",
        "status": "pending",
        "priority": 1
    })
    assert response.status_code == 200
    assert response.json()['title'] == "Test Task"

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_task():
    response =client.get("/tasks/0")
    assert response.status_code == 200
    assert response.json()['title'] == "Test Task"

def test_update_task():
    response = client.put("/tasks/0", json={
        "title": "Updated Task",
        "description": "This is an updated test task",
        "due_date": "2025-05-21",
        "status": "completed",
        "priority": 2
    })
    assert response.status_code == 200
    assert response.json()['title'] == "Updated Task"