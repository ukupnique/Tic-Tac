import uuid
from domain.model.board import Board


class Game:
    """Создание игры"""

    def __init__(self, board: Board, id: uuid.UUID | None = None):
        self.board = board
        if id is None:
            id = uuid.uuid4()
            self.uid = id
        else:
            self.uid = id
