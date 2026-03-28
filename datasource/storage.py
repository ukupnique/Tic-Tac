import threading
import uuid
from datasource.model.models import GameDSModel


class InMemoryStorage:
    """Создаем хранилище для игр"""

    def __init__(self) -> None:
        self._games = {}
        self._lock = threading.Lock()

    def set_game(self, game_id: uuid.UUID, game_data: GameDSModel) -> None:
        with self._lock:
            self._games[game_id] = game_data

    def get_game(self, game_id: uuid.UUID) -> GameDSModel | None:
        with self._lock:
            return self._games.get(game_id)
