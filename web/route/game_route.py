from flask import Blueprint, request, jsonify, render_template
from dataclasses import asdict
import uuid

from web.model.models import GameStepRequest
from web.mapper.web_mapper import WebMapper
from domain.service.game_application_service import GameApplicationService
from domain.service.game_service import GameService

# Создаем Blueprint для группировки игровых маршрутов
game_usage = Blueprint("game_usage", __name__)


class GameController:
    """
    Контроллер для обработки HTTP-запросов.
    Служит прослойкой между сетью и бизнес-логикой.
    """

    def __init__(self, app_service: GameApplicationService, game_service: GameService):
        self.app_service = app_service
        self.game_service = game_service

    def create_game(self):
        """
        Метод для инициализации новой игры (POST /game).
        Возвращает UUID новой игры и пустое поле.
        """
        try:
            # Вызываем метод создания в прикладном сервисе
            game = self.app_service.create_new_game()

            # Преобразуем доменную модель в DTO для ответа
            response_dto = WebMapper.to_GameResponse(game, self.game_service)
            return jsonify(asdict(response_dto)), 201
        except Exception as e:
            return jsonify({"error": f"Не удалось создать игру: {str(e)}"}), 500

    def post_game(self, game_id: uuid.UUID):
        """
        Метод для совершения хода (POST /game/<uuid:game_id>).
        Обрабатывает ход игрока и возвращает ответ компьютера.
        """
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Пустое тело запроса"}), 400

            step_request = GameStepRequest(
                game_id=game_id, row=data.get("row"), col=data.get("col")
            )

            g_id, row, col = WebMapper.from_GameStepRequest(step_request)

            game = self.app_service.make_move(g_id, row, col)

            response_dto = WebMapper.to_GameResponse(game, self.game_service)
            return jsonify(asdict(response_dto)), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        except Exception as e:

            import traceback

            print(traceback.format_exc())
            return jsonify({"error": str(e)}), 500


def register_routes(app, app_service, game_service):
    controller = GameController(app_service, game_service)

    # Главная страница
    app.add_url_rule(
        "/", view_func=lambda: render_template("index.html"), methods=["GET"]
    )

    # API методы
    app.add_url_rule("/game", view_func=controller.create_game, methods=["POST"])
    app.add_url_rule(
        "/game/<uuid:game_id>", view_func=controller.post_game, methods=["POST"]
    )
