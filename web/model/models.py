import uuid
from dataclasses import dataclass
from typing import List


@dataclass
class GameStepRequest:
    "Запрос шага от пользователя"

    game_id: uuid.UUID
    row: int
    col: int


@dataclass
class GameResponse:
    "Отправка данных после обработки"

    game_id: uuid.UUID
    board: List[List[int]]
    winner: int | None
