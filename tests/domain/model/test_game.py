import pytest
from domain.model.game import Game
from domain.model.board import Board
import uuid


def test_game_create():
    matrix = Board()
    game = Game(matrix)

    assert game.board == matrix
    assert isinstance(game.uid, uuid.UUID)


def test_uid():
    my_id = uuid.uuid4()
    matrix = Board()
    game = Game(matrix, my_id)

    assert game.uid == my_id
