from typing import List


class Board:
    """Создаем доску для игры"""

    def __init__(self, matrix: List[List[int]] | None = None):
        if matrix is None:
            matrix = [[0 for _ in range(3)] for _ in range(3)]
            self.matrix = matrix
        else:
            self.matrix = [row[:] for row in matrix]

    def __repr__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])
