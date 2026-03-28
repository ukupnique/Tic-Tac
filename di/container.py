from domain.service.game_application_service import GameApplicationService
from domain.service.game_service import GameService
from datasource.repository.game_repository import GameRepository
from datasource.storage import InMemoryStorage


class Container:
    """Отвечает за создание и связывание всех компонентов приложения."""

    def __init__(self) -> None:
        """Инициализирует зависимости приложения."""
        self._storage = InMemoryStorage()
        self._repository = GameRepository(self._storage)
        self._game_logic = GameService()
        self._app_service = GameApplicationService(self._repository, self._game_logic)

    def get_app_service(self) -> GameApplicationService:
        """Используется в Web-слое для обработки игровых ходов."""
        return self._app_service

    def get_game_logic(self) -> GameService:
        """Нужен для получения информации о правилах или текущем победителе."""
        return self._game_logic
