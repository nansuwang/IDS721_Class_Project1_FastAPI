from os import path

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_necessary_files():
    assert path.exists("regression_model.pkl")
    assert path.exists("predictors.py")
    assert path.exists("app.py")


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message`": "Hello World!"}
