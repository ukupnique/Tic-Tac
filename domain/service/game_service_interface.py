from abc import ABC, abstractmethod
from domain.model.board import Board


class GameServiceInterface(ABC):

    @abstractmethod
    def get_next_move(self, board: Board) -> Board:
        """метод получения следующего хода текущей игры алгоритмом Минимакс"""
        pass

    @abstractmethod
    def validate_field(self, old_board: Board, new_board: Board) -> bool:
        """Проверяет, что ход сделан по правилам."""
        pass

    @abstractmethod
    def end_game(self, board: Board) -> bool:
        """метод проверки окончания игры"""
        pass
