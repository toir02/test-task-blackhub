import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture()
def test_client():
    return TestClient(app)


def test_get_html_content(test_client):

    response = test_client.get("/politica.html")
    assert response.status_code == 200
    assert "message" in response.json()
    content = response.json()["message"]
    assert "Black Russia" not in content
    assert "Black <span> Russia" not in content
    assert "BLACK\n span RUSSIA" not in content
    assert "BlackHub Games" in content


def test_get_html_content_patch_response(test_client):
    response = test_client.patch("/politica.html")
    assert response.status_code == 405
