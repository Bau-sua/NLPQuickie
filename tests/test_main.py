import pytest
from fastapi.testclient import TestClient
from main import app

def test_live_endpoint(client: TestClient):
    resp = client.get("/live")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "200 OK"
    assert data["alive"] is True

def test_process_post_valid(client: TestClient):
    resp = client.post("/process", json={"text": "Hola mundo test"})
    assert resp.status_code == 200
    data = resp.json()
    assert "word_count" in data
    assert "most_common_word" in data
    assert "entities" in data
    assert isinstance(data["word_count"], int)

def test_process_post_invalid(client: TestClient):
    resp = client.post("/process", json={})  # No text
    assert resp.status_code == 422  # Pydantic validation

def test_root(client):
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert "endpoints" in data

def test_process_get(client):
    resp = client.get("/process")
    assert resp.status_code == 200
    data = resp.json()
    assert "example" in data