import pytest

from domain.service.game_service import GameService
from domain.model.board import Board


def test_win_first():
    service = GameService()
    matrix = [[2, 2, 0], [1, 1, 1], [1, 2, 1]]
    board = Board(matrix)
    assert service.end_game(board)


def test_win_last():
    service = GameService()
    matrix = [[2, 2, 2], [1, 0, 1], [1, 2, 1]]
    board = Board(matrix)
    assert service.end_game(board)


def test_in_game():
    service = GameService()
    matrix = [[2, 0, 2], [1, 0, 1], [1, 2, 1]]
    board = Board(matrix)
    assert not service.end_game(board)


def test_start_game():
    service = GameService()
    board = Board()
    print(board.matrix)
    assert not service.end_game(board)


def test_pos_diag():
    service = GameService()
    matrix = [[2, 0, 1], [1, 2, 1], [1, 0, 2]]
    board = Board(matrix)
    assert service.end_game(board)


def test_neg_diag():
    service = GameService()
    matrix = [[0, 0, 1], [2, 1, 1], [1, 0, 2]]
    board = Board(matrix)
    assert service.end_game(board)


# validate_field tests
def test_good_field_one():
    service = GameService()
    matrix_1 = [[0, 0, 0], [0, 0, 0], [1, 0, 2]]
    matrix_2 = [[1, 0, 0], [0, 0, 0], [1, 0, 2]]
    old_board = Board(matrix_1)
    new_board = Board(matrix_2)

    assert service.validate_field(old_board, new_board)


def test_new_board():
    service = GameService()
    matrix_2 = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    old_board = Board()
    new_board = Board(matrix_2)

    assert service.validate_field(old_board, new_board)


def test_two_diff():
    service = GameService()
    matrix_2 = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
    old_board = Board()
    new_board = Board(matrix_2)

    assert not service.validate_field(old_board, new_board)


def test_last_diff():
    service = GameService()
    matrix_2 = [[2, 0, 0], [0, 0, 0], [0, 0, 0]]
    old_board = Board()
    new_board = Board(matrix_2)

    assert not service.validate_field(old_board, new_board)


def test_rewrite_diff():
    service = GameService()
    matrix_1 = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    matrix_2 = [[2, 0, 0], [0, 0, 0], [0, 0, 0]]

    old_board = Board(matrix_1)
    new_board = Board(matrix_2)

    assert not service.validate_field(old_board, new_board)


# test minimax


def test_win_move():

    matrix = [[1, 1, 2], [0, 2, 0], [0, 0, 0]]
    service = GameService()
    board = Board(matrix)
    res = service.get_next_move(board)
    assert res.matrix[2][0] == 2


def test_def_move():

    matrix = [[1, 1, 0], [0, 2, 0], [0, 0, 0]]
    service = GameService()
    board = Board(matrix)
    res = service.get_next_move(board)
    assert res.matrix[0][2] == 2


def test_fast_move():

    matrix = [[1, 1, 0], [0, 0, 0], [2, 2, 0]]
    service = GameService()
    board = Board(matrix)
    res = service.get_next_move(board)
    assert res.matrix[2][2] == 2


def test_last_move():
    matrix = [[1, 2, 1], [1, 2, 2], [2, 1, 0]]
    service = GameService()
    board = Board(matrix)
    res = service.get_next_move(board)

    assert res.matrix[2][2] == 2
    assert service.end_game(res)
