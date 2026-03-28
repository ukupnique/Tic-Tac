import uuid
from dataclasses import dataclass


@dataclass
class GameDSModel:
    """Модель данных для хранения в datasource"""

    game: uuid.UUID
    board: list[list[int]]
