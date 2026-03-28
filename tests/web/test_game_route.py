import pytest
import uuid
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_create_game_endpoint(client):
    response = client.post("/game")
    assert response.status_code == 201
    data = response.get_json()
    assert "game_id" in data
    assert "board" in data


def test_make_move_success(client):

    res = client.post("/game")
    game_id = res.get_json()["game_id"]

    move_data = {"row": 1, "col": 1}
    response = client.post(f"/game/{game_id}", json=move_data)

    assert response.status_code == 200
    assert response.get_json()["board"][1][1] != 0


def test_make_move_invalid_coordinates(client):
    game_id = str(uuid.uuid4())

    response = client.post(f"/game/{game_id}", json={"row": 5, "col": 0})

    assert response.status_code == 400

    data = response.get_json()
    assert data is not None
    assert "error" in data
    assert "диапазоне от 0 до 2" in data["error"]
