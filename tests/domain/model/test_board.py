from domain.model.board import Board
import pytest


def test_board():
    board = Board()
    assert len(board.matrix) == 3
    assert all(len(row) == 3 for row in board.matrix)
    assert all(c == 0 for r in board.matrix for c in r)


def test_created_board():
    test_matrix = [[0, 1, 1], [0, 2, 2], [2, 1, 0]]
    board = Board(test_matrix)

    assert board.matrix == test_matrix
    assert board.matrix[2] == [2, 1, 0]
    test_matrix[0][0] = 2
    assert board.matrix[0][0] == 0
