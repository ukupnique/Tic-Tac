from uuid import UUID
from domain.model.game import Game
from datasource.storage import InMemoryStorage
from datasource.mapper.game_mapper import GameMapper


class GameRepository:
    """Класс-хранилище для игры"""

    def __init__(self, storage: InMemoryStorage) -> None:
        self._storage = storage

    def save(self, game: Game) -> None:
        ds_model = GameMapper.to_datasource(game)
        self._storage.set_game(game_id=game.uid, game_data=ds_model)

    def load(self, game_id: UUID):

        ds_model = self._storage.get_game(game_id)

        if not ds_model:
            return None

        return GameMapper.to_domain(ds_model)
