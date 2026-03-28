import pytest
import uuid
from domain.model.game import Game
from domain.model.board import Board
from datasource.storage import InMemoryStorage
from datasource.repository.game_repository import GameRepository


@pytest.fixture
def repository():
    storage = InMemoryStorage()
    return GameRepository(storage)


def test_save_and_load(repository):
    id = uuid.uuid4()
    game = Game(Board(), id)

    repository.save(game)

    new_game = repository.load(game.uid)

    assert new_game
    assert new_game.uid == game.uid
    assert new_game.board.matrix == game.board.matrix


def load_incorrect_game(repository):
    new_game = repository.load(uuid.uuid4())
    assert not new_game
