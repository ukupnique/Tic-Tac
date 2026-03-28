from domain.service.game_service_interface import GameServiceInterface
from domain.model.board import Board


class GameService(GameServiceInterface):

    def end_game(self, board: Board) -> bool:
        """Метод проверки окончания игры: победа кого-то из игроков или ничья"""
        # 1. Проверяем, есть ли победитель (10 или -10)
        if self.evaluate(board) != 0:
            return True

        # 1. Проверяем ничью
        res = all(0 not in row for row in board.matrix)

        return res

    def get_next_move(self, board: Board) -> Board:
        """метод получения следующего хода текущей игры алгоритмом Минимакс"""
        if self.end_game(board):
            return board

        best_score = float("-inf")
        best_move = None
        moves = self.get_available_moves(board)
        for move in moves:
            board.matrix[move[0]][move[1]] = 2
            score = self._minimax(board, 0, False)
            board.matrix[move[0]][move[1]] = 0

            if score > best_score:
                best_score = score
                best_move = move
        if best_move:
            board.matrix[best_move[0]][best_move[1]] = 2

        return board

    def validate_field(self, old_board: Board, new_board: Board) -> bool:
        """метод валидации игрового поля текущей игры"""

        old_matrix = old_board.matrix
        new_matrix = new_board.matrix
        diff = 0
        for i in range(3):
            for j in range(3):
                if old_matrix[i][j] != 0:
                    if old_matrix[i][j] != new_matrix[i][j]:
                        return False

                if old_matrix[i][j] == 0 and new_matrix[i][j] != 0:
                    if new_matrix[i][j] != 1:
                        return False
                    diff += 1
        return diff == 1

    def _minimax(self, board: Board, depth: int, is_maximizing: bool) -> int:
        status = self.evaluate(board)
        if status == 10:
            return status - depth

        if status == -10:
            return status + depth

        moves = self.get_available_moves(board)
        if not moves:
            return 0
        if is_maximizing:
            max_eval = float("-inf")
            for cell in moves:
                board.matrix[cell[0]][cell[1]] = 2
                res = self._minimax(board, depth + 1, False)
                max_eval = max(res, max_eval)
                board.matrix[cell[0]][cell[1]] = 0
            return int(max_eval)
        else:
            min_eval = float("inf")
            for cell in moves:
                board.matrix[cell[0]][cell[1]] = 1
                res = self._minimax(board, depth + 1, True)
                min_eval = min(res, min_eval)
                board.matrix[cell[0]][cell[1]] = 0
            return int(min_eval)

    @staticmethod
    def _create_all_lines(board: Board) -> list[list[int]]:
        """Собираем значения всех 8 линий: 3 строки, 3 столбца и 2 диагонали"""
        res_matrix = []
        # Строки
        res_matrix.extend([list(row) for row in board.matrix])
        # Столбцы
        res_matrix.extend([list(col) for col in zip(*board.matrix)])
        # Главная диагональ
        res_matrix.append([board.matrix[i][i] for i in range(3)])
        # Побочная диагональ
        res_matrix.append([board.matrix[i][2 - i] for i in range(3)])

        return res_matrix

    @staticmethod
    def evaluate(board: Board) -> int:
        """Возвращает +10, если выиграл компьютер (2), -10, если выиграл человек (1), и 0, если ничья"""
        res_matrix = GameService._create_all_lines(board)

        for line in res_matrix:
            if all(cell == 2 for cell in line):
                return 10
            if all(cell == 1 for cell in line):
                return -10

        return 0

    @staticmethod
    def get_available_moves(board: Board) -> list[tuple[int, int]]:
        res = []
        for i in range(3):
            for j in range(3):
                if board.matrix[i][j] == 0:
                    res.append((i, j))
        return res
