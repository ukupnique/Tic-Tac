from domain.model.board import Board
from domain.model.game import Game
from datasource.model.models import GameDSModel


class GameMapper:

    @staticmethod
    def to_datasource(game: Game) -> GameDSModel:
        """Превращаем живой Game в GameDSModel для хранения"""
        matrix_copy = [row[:] for row in game.board.matrix]
        return GameDSModel(game=game.uid, board=matrix_copy)

    @staticmethod
    def to_domain(game: GameDSModel):
        """Превращаем GameDSModel данных обратно в живой объект Game"""
        matrix_copy = [row[:] for row in game.board]
        board = Board(matrix_copy)
        return Game(board=board, id=game.game)
