import pytest
from web.mapper.web_mapper import WebMapper
from web.model.models import GameResponse, GameStepRequest
from web.route.game_route import GameController
from domain.model.game import Game, Board
from domain.service.game_service import GameService

import uuid


def test_from_GameStepRequest():
    id = uuid.uuid4()
    row = 1
    col = 1

    request = GameStepRequest(id, row, col)

    assert request.game_id == id
    assert request.row == row
    assert request.col == col


def test_bad_GameStepRequest():

    request = GameStepRequest(game_id=uuid.uuid4(), row=4, col=0)

    with pytest.raises(ValueError) as excinfo:
        WebMapper.from_GameStepRequest(request)
    assert "Координаты должны быть в диапазоне от 0 до 2" in str(excinfo.value)

    request = GameStepRequest(game_id=uuid.uuid4(), row=str(1), col=0)

    with pytest.raises(ValueError) as excinfo:
        WebMapper.from_GameStepRequest(request)
    assert "Координаты должны быть целыми числами" in str(excinfo.value)

    request = GameStepRequest(game_id=uuid.uuid4(), row=None, col=0)

    with pytest.raises(ValueError) as excinfo:
        WebMapper.from_GameStepRequest(request)
    assert "Координаты row и col обязательны" in str(excinfo.value)


def test_to_new_GameResponse():
    board = Board()
    game = Game(board)
    service = GameService()
    responce = WebMapper.to_GameResponse(game, service)

    assert not responce.winner
    assert responce.game_id == game.uid
    assert responce.board == game.board.matrix

    assert isinstance(responce, GameResponse)


def test_to_in_Process_GameResponse():
    matrix = [[1, 2, 2], [2, 1, 1], [1, 2, 2]]

    board = Board(matrix)
    game = Game(board)
    service = GameService()
    responce = WebMapper.to_GameResponse(game, service)

    assert responce.winner == 3


def test_to_user_win_GameResponse():
    matrix = [[1, 1, 1], [2, 2, 0], [1, 2, 2]]

    board = Board(matrix)
    game = Game(board)
    service = GameService()
    responce = WebMapper.to_GameResponse(game, service)

    assert responce.winner == 1


def test_to_ai_win_GameResponse():
    matrix = [[2, 2, 2], [1, 0, 1], [1, 2, 1]]

    board = Board(matrix)
    game = Game(board)
    service = GameService()
    responce = WebMapper.to_GameResponse(game, service)

    assert responce.winner == 2
