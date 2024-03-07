from fastapi.testclient import TestClient

from cgapi.api import api

client = TestClient(api)


def test_create_player_via_api():
    response = client.post(
        "/",
        json={"name": "Loui", "points": 82},
    )
    assert response.status_code >= 200 and response.status_code < 300
    result = response.json()
    assert result["id"] == 1
    assert result["name"] == "Loui"
    assert result["points"] == 82
