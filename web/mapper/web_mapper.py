from domain.model.game import Game
from domain.service.game_service import GameService
from web.model.models import GameStepRequest, GameResponse


class WebMapper:
    @staticmethod
    def from_GameStepRequest(request: GameStepRequest):

        if request.row is None or request.col is None:
            raise ValueError("Координаты row и col обязательны")

        if not isinstance(request.row, int) or not isinstance(request.col, int):
            raise ValueError("Координаты должны быть целыми числами")

        if not (0 <= request.row <= 2 and 0 <= request.col <= 2):
            raise ValueError("Координаты должны быть в диапазоне от 0 до 2")

        return request.game_id, request.row, request.col

    @staticmethod
    def to_GameResponse(game: Game, game_service: GameService) -> GameResponse:
        "Отправка данных после обработки с четким статусом победителя"
        game_id = game.uid
        board = game.board.matrix

        is_over = game_service.end_game(game.board)

        winner_status = False

        if is_over:

            score = game_service.evaluate(game.board)

            if score <= -10:
                winner_status = 1
            elif score >= 10:
                winner_status = 2
            else:
                winner_status = 3

        return GameResponse(game_id, board, winner_status)
