from domain.model.board import Board
from domain.model.game import Game
from datasource.model.models import GameDSModel
from datasource.mapper.game_mapper import GameMapper
import uuid


def test_mapper_to_datasource():
    matrix = [[0, 1, 0], [0, 2, 0], [0, 0, 0]]
    board = Board(matrix)
    id = uuid.uuid4()
    game = Game(board=board, id=id)

    res = GameMapper.to_datasource(game=game)

    assert matrix == res.board
    assert id == res.game

    matrix[0][0] = 1
    assert res.board[0][0] == 0


def test_mapper_to_domain():
    matrix = [[0, 1, 0], [0, 2, 0], [0, 0, 0]]
    id = uuid.uuid4()

    ds_model = GameDSModel(id, matrix)

    game = GameMapper.to_domain(ds_model)

    assert game.board.matrix == matrix
    assert game.uid == id
    assert isinstance(game.board, Board)
