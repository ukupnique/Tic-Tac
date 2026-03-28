from uuid import UUID
from domain.service.game_service import GameService
from datasource.repository.game_repository import GameRepository
from domain.model.game import Game, Board
import copy


class GameApplicationService:
    def __init__(self, repository: GameRepository, domain_service: GameService):
        self._repository = repository
        self._domain_service = domain_service

    def make_move(self, game_id: UUID, row: int, col: int) -> Game:

        old_game = self._repository.load(game_id)
        if not old_game:
            raise ValueError(f"Игра {game_id} не найдена")

        new_board = copy.deepcopy(old_game.board)

        if new_board.matrix[row][col] != 0:
            raise ValueError("Клетка уже занята!")

        new_board.matrix[row][col] = 1

        if not self._domain_service.validate_field(old_game.board, new_board):
            raise ValueError("Ошибка валидации: некорректное изменение поля!")

        old_game.board = new_board

        if not self._domain_service.end_game(old_game.board):
            old_game.board = self._domain_service.get_next_move(old_game.board)

        self._repository.save(old_game)

        return old_game

    def create_new_game(self) -> Game:

        new_game = Game(board=Board())

        self._repository.save(new_game)

        return new_game
